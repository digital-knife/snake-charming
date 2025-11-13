#!/usr/bin/env python3

import csv
import subprocess


def disk_usage(host, threshold):
    try:
        cmd = ["ssh", host, "df", "-h", "/"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        line = result.stdout.strip().splitlines()[-1]
        usage = int(line.split()[4].rstrip("%"))
        if usage > threshold:
            return f"Alert: {host} {usage}% > {threshold}%"
        return f"OK: {host} {usage}%"
    except Exception:
        return f"OFFLINE or UNREACHABLE: {host}"


# ---READ CSV---#
with open("csvtest.csv") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        host = row[0]
        threshold = int(row[1])
        print(disk_usage(host, threshold))
