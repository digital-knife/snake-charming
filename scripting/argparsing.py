#!/usr/bin/env python3

import argparse
import subprocess

parser = argparse.ArgumentParser(description="Disk Monitor for multiple hosts")
parser.add_argument(
    "hosts", nargs="+", help="One of more hostnames to check diskspace for"
)
parser.add_argument(
    "--threshold", type=int, default=90, help="alert threshold in percent"
)
parser.add_argument(
    "--dry-run", action="store_true", help="simulate run without using ssh"
)
args = parser.parse_args()


def disk_usage(host):
    if args.dry_run:
        return f"{host}: DRY RUN"
    try:
        cmd = ["ssh", host, "df", "-h", "/"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return f"{host} unreachable or offline {e}"


for host in args.hosts:
    usage = disk_usage(host)
    print(usage)
