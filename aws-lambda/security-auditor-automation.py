"""
Security Group Audit and Auto-Remediation Lambda

Scans AWS security groups for common security violations and can automatically
remediate issues or send alerts.

Common violations detected:
1. Security groups with 0.0.0.0/0 access on sensitive ports (SSH, RDP, database ports)
2. Unused security groups (not attached to any resources)
3. Security groups with overly permissive rules
4. Security groups without proper tagging

Required IAM Permissions:
- ec2:DescribeSecurityGroups
- ec2:DescribeNetworkInterfaces
- ec2:RevokeSecurityGroupIngress
- ec2:CreateTags
- sns:Publish

Environment Variables:
- SNS_TOPIC_ARN: ARN of SNS topic for alerts
- AUTO_REMEDIATE: Set to 'true' to automatically fix violations (default: false)
- SENSITIVE_PORTS: Comma-separated list of ports to monitor (default: 22,3389,3306,5432,27017)
- WHITELIST_TAG: Tag key/value to whitelist SGs (format: key=value)
"""

import json
import os
from datetime import datetime, timezone
import boto3
from botocore.exceptions import ClientError

ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

# Default sensitive ports
DEFAULT_SENSITIVE_PORTS = [22, 3389, 3306, 5432, 27017, 6379, 1433, 5439]

def lambda_handler(event, context):
    """
    Main handler for security group audit
    """
    try:
        # Configuration
        sns_topic_arn = os.environ['SNS_TOPIC_ARN']
        auto_remediate = os.environ.get('AUTO_REMEDIATE', 'false').lower() == 'true'
        sensitive_ports_str = os.environ.get('SENSITIVE_PORTS', '')
        whitelist_tag = os.environ.get('WHITELIST_TAG', '')
        
        # Parse sensitive ports
        if sensitive_ports_str:
            sensitive_ports = [int(p.strip()) for p in sensitive_ports_str.split(',')]
        else:
            sensitive_ports = DEFAULT_SENSITIVE_PORTS
        
        # Parse whitelist tag
        whitelist_key, whitelist_value = None, None
        if '=' in whitelist_tag:
            whitelist_key, whitelist_value = whitelist_tag.split('=', 1)
        
        violations = {
            'open_world_access': [],
            'unused_security_groups': [],
            'missing_tags': [],
            'remediated': []
        }
        
        # Get all security groups
        security_groups = ec2_client.describe_security_groups()['SecurityGroups']
        print(f"Scanning {len(security_groups)} security groups")
        
        # Get all network interfaces to identify unused SGs
        network_interfaces = ec2_client.describe_network_interfaces()['NetworkInterfaces']
        used_sg_ids = set()
        for ni in network_interfaces:
            for sg in ni.get('Groups', []):
                used_sg_ids.add(sg['GroupId'])
        
        for sg in security_groups:
            sg_id = sg['GroupId']
            sg_name = sg['GroupName']
            
            # Skip default security groups
            if sg_name == 'default':
                continue
            
            # Check if whitelisted
            is_whitelisted = False
            if whitelist_key:
                for tag in sg.get('Tags', []):
                    if tag['Key'] == whitelist_key and tag['Value'] == whitelist_value:
                        is_whitelisted = True
                        break
            
            if is_whitelisted:
                print(f"Skipping whitelisted SG: {sg_id}")
                continue
            
            # Check for open world access on sensitive ports
            for rule in sg.get('IpPermissions', []):
                from_port = rule.get('FromPort', 0)
                to_port = rule.get('ToPort', 0)
                
                # Check if rule covers any sensitive port
                for port in sensitive_ports:
                    if from_port <= port <= to_port:
                        # Check for 0.0.0.0/0
                        for ip_range in rule.get('IpRanges', []):
                            if ip_range.get('CidrIp') == '0.0.0.0/0':
                                violation = {
                                    'sg_id': sg_id,
                                    'sg_name': sg_name,
                                    'port': port,
                                    'protocol': rule.get('IpProtocol', 'tcp'),
                                    'cidr': '0.0.0.0/0'
                                }
                                violations['open_world_access'].append(violation)
                                
                                # Auto-remediate if enabled
                                if auto_remediate:
                                    try:
                                        remediate_open_access(sg_id, rule)
                                        violations['remediated'].append(
                                            f"Removed 0.0.0.0/0 access on port {port} from {sg_id}"
                                        )
                                    except ClientError as e:
                                        print(f"Failed to remediate {sg_id}: {str(e)}")
            
            # Check for unused security groups
            if sg_id not in used_sg_ids:
                violations['unused_security_groups'].append({
                    'sg_id': sg_id,
                    'sg_name': sg_name,
                    'vpc_id': sg.get('VpcId', 'N/A')
                })
            
            # Check for missing tags
            tags = {tag['Key']: tag['Value'] for tag in sg.get('Tags', [])}
            if 'Environment' not in tags or 'Owner' not in tags:
                violations['missing_tags'].append({
                    'sg_id': sg_id,
                    'sg_name': sg_name,
                    'missing': [k for k in ['Environment', 'Owner'] if k not in tags]
                })
        
        # Generate report
        summary = generate_report(violations, auto_remediate, sensitive_ports)
        
        # Send SNS notification
        send_notification(sns_topic_arn, summary, violations)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'total_violations': sum(len(v) for k, v in violations.items() if k != 'remediated'),
                'open_world_access': len(violations['open_world_access']),
                'unused_security_groups': len(violations['unused_security_groups']),
                'missing_tags': len(violations['missing_tags']),
                'remediated': len(violations['remediated']),
                'auto_remediate_enabled': auto_remediate
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

def remediate_open_access(sg_id, rule):
    """
    Revoke overly permissive security group rule
    """
    ec2_client.revoke_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[rule]
    )
    print(f"Revoked open world access rule from {sg_id}")

def generate_report(violations, auto_remediate, sensitive_ports):
    """
    Generate human-readable report
    """
    mode = "[AUTO-REMEDIATION ENABLED] " if auto_remediate else ""
    
    report = f"""
{mode}Security Group Audit Report
Generated: {datetime.now(timezone.utc).isoformat()}

SUMMARY:
========
• Open World Access Violations: {len(violations['open_world_access'])}
• Unused Security Groups: {len(violations['unused_security_groups'])}
• Missing Required Tags: {len(violations['missing_tags'])}
"""
    
    if auto_remediate:
        report += f"• Rules Remediated: {len(violations['remediated'])}\n"
    
    report += f"\nMonitored Ports: {', '.join(map(str, sensitive_ports))}\n"
    
    if violations['open_world_access']:
        report += "\n\nOPEN WORLD ACCESS (0.0.0.0/0):\n"
        report += "=" * 40 + "\n"
        for v in violations['open_world_access'][:20]:  # Limit to 20
            report += f"• {v['sg_id']} ({v['sg_name']}): Port {v['port']}/{v['protocol']}\n"
    
    if violations['unused_security_groups']:
        report += "\n\nUNUSED SECURITY GROUPS:\n"
        report += "=" * 40 + "\n"
        for v in violations['unused_security_groups'][:20]:
            report += f"• {v['sg_id']} ({v['sg_name']}) in {v['vpc_id']}\n"
    
    if violations['remediated']:
        report += "\n\nREMEDIATION ACTIONS:\n"
        report += "=" * 40 + "\n"
        for action in violations['remediated']:
            report += f"• {action}\n"
    
    return report

def send_notification(topic_arn, summary, violations):
    """
    Send SNS notification with audit results
    """
    total_violations = sum(len(v) for k, v in violations.items() if k != 'remediated')
    
    subject = f"Security Group Audit: {total_violations} violations found"
    
    if violations['remediated']:
        subject += f" ({len(violations['remediated'])} remediated)"
    
    try:
        sns_client.publish(
            TopicArn=topic_arn,
            Subject=subject,
            Message=summary
        )
        print("Notification sent via SNS")
    except ClientError as e:
        print(f"Failed to send SNS notification: {str(e)}")
