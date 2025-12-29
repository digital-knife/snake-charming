#!/usr/bin/env python3

import sys
import os
import boto3
import json

REGION = "us-east-1"
ec2 = boto3.client("ec2", region_name=REGION)


def get_instance_name(tags):
    """Extract the 'Name' tag value if it exists, else return placeholder."""
    if not tags:
        return "No Name tag"
    for tag in tags:
        if tag["Key"] == "Name":
            return tag["Value"]
    return "No Name tag"


def list_all_instances():
    try:
        response = ec2.describe_instances()

        instances_found = False
        print("All EC2 Instances:\n")
        print(f"{'Instance ID':<20} {'Name':<30}")
        print("-" * 50)

        for reservation in response.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                instances_found = True
                instance_id = instance.get("InstanceId", "N/A")
                name = get_instance_name(instance.get("Tags", []))
                print(f"{instance_id:<20} {name:<30}")

        if not instances_found:
            print("No instances found in us-east-1.")

    except Exception as e:
        print(f"Error: {e}")


# TO DO
# Turn instances off or on
# add multiple regions support
# add in other resources through prettytable
# optional snapshot of instances before shutdown

if __name__ == "__main__":
    list_all_instances()
