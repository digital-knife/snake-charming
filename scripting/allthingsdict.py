#!/usr/bin/env python3

# servers = {
#     "web01": {"cpu": 75, "disk": 60, "cpu_limit": 80, "disk_limit": 85},
#     "db01": {"cpu": 96, "disk": 92, "cpu_limit": 90, "disk_limit": 90},
# }

# servers["log01"] = {"cpu": 80, "disk": 50, "cpu_limit": 60, "disk_limit": 70}

# for name, data in servers.items():
#     cpu = data["cpu"]
#     cpu_limit = data["cpu_limit"]
#     disk = data["disk"]
#     disk_limit = data["disk_limit"]

#     if cpu > cpu_limit:
#         print(f"ALERT CPU: {name}")
#     if disk > disk_limit:
#         print(f"ALERT DISK: {name}")
#     if cpu <= cpu_limit:
#         print(f"CPU capacity for {name} is ok")
#     if disk <= disk_limit:
#         print(f"Disk capacity for {name} is ok")

# config = {"web01": 80, "db01": 90}

# for server in config.keys():
#     print(f"{server}: {config[server]}")

# print(f"Total: {len(config)}")

# servers = {
#     "web01": {"cpu": 70, "disk": 65},
#     "db01": {"cpu": 80, "disk": 50},
#     "log01": {"cpu": 50, "disk": 80},
#     "cache01": {"cpu": 90, "disk": 85},
# }

# for server, stats in servers.items():
#     message = f"{server}: OK"
#     if stats["cpu"] > 85:
#         message = f"{server} CPU ALERT"
#     if stats["disk"] > 90:
#         message = f"{server} DISK ALERT"
#     if stats["cpu"] > 85 and stats["disk"] > 90:
#         message = f"CPU + DISK ALERT on {server}"
#     print(message)

servers = {
    "web01": {"cpu": 72, "ram": 68},
    "web02": {"cpu": 88, "ram": 92},
    "web03": {"cpu": 65, "ram": 55},
    "web04": {"cpu": 79, "ram": 88},
}

servers["db01"] = {"cpu": 95, "ram": 45}

for server, resource in servers.items():

    cpu = resource["cpu"]
    ram = resource["ram"]
    diff = cpu - ram

    if resource["cpu"] > 90:
        msg = f"{server}: CPU monster"
    elif resource["cpu"] > resource["ram"] + 10:
        msg = f"{server}: CPU heavy"
    elif resource["ram"] > resource["cpu"] + 10:
        msg = f"{server}: RAM heavy"
    else:
        msg = f"{server}: balanced"
    print(msg)
