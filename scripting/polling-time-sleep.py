#!/usr/bin/env python3

import time
import json
import csv
import subprocess
from datetime import datetime

# -----CONFIG
CSV_FILE = "csvtest.csv"
REPORT_FILE = "alerts.json"
POLL_INTERVAL = 60


def load_hosts():
    hosts = []
    with open(CSV_FILE) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            hosts.append({"host": row[0], "threshold": int(row[1])})
    return hosts


def get_disk(host):
    try:
        cmd = ["ssh", host, "df", "-h", "/"]
        result = subprocess.run(
            cmd, capture_output=True, text=True, check=True, timeout=5
        )
        line = result.stdout.strip().splitlines()[-1]
        usage = int(line.split()[4].rstrip("%"))
        return {"status": "OK", "Usage": usage}
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}


print("Starting monitor... CTRL-C to STOP")
iteration = 0

try:
    while True:
        iteration += 1
        hosts = load_hosts()
        alerts = {
            "Generated_at": datetime.now().isoformat(),
            "iteration": iteration,
            "summary": {"total": len(hosts), "alerts": 0, "errors": 0},
            "hosts": [],
        }

        for h in hosts:
            result = get_disk(h["host"])
            entry = {"host": h["host"], "threshold": h["threshold"], **result}
            if result["status"] == "OK" and result["usage"] > h["threshold"]:
                entry["alert"] = True
                alerts["summary"]["alerts"] += 1
            elif result["status"] == "ERROR":
                alerts["summary"]["errors"] += 1
            alerts["hosts"].append(entry)

        with open(REPORT_FILE, "w") as f:
            json.dump(alerts, f, indent=2, default=str)

        print(
            f"[{datetime.now().strftime('%H:%M:%S')}] Poll #{iteration} complete ---> {REPORT_FILE}"
        )
        time.sleep(POLL_INTERVAL)

except KeyboardInterrupt:
    print("\nShutting down gracefully due to keyboard interrupt used...")


print(type(hosts))
print(type(hosts[0]))
