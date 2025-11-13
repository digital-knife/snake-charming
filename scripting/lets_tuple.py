#!/usr/bin/env python3

# location = ("rack-42", 19)
# row, slot = location  # unpack
# print(f"server in {row}, slot {slot}")

# # set
# down = {"web01", "web02", "web01", "db01"}
# print(f"Unique down servers: {len(down)}")

# healthy = {"web01", "web02", "web03"}
# reported_down = {"web02", "web04"}

# false_alarms = healthy & reported_down
# print(f"False alarms: {false_alarms}")


# # immutable limits (tuple)
# LIMITS = (85, 90)
# cpu_max, disk_max = LIMITS

# # unique critical hosts
# critical = {"db01", "db02", "db01"}
# critical.add("web01")

# # find overlap
# all_hosts = {"web01", "web02", "db01", "cache01"}
# down_hosts = {"web02", "db01", "web99"}

# real_problems = all_hosts & down_hosts

# # print it all
# print(f"CPU limit: {cpu_max}%")
# print(f"Disk limit: {disk_max}%")
# print(f"Critical hosts: {critical}")
# print(f"Real problems: {real_problems}")


location = ("A", 42)
row, slot = location
print(f"Server in row {row}, slot {slot}")

down = {"web01", "web02", "web01"}
print(f"Unique down: {len(down)}")
