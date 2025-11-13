#!/usr/env/bin python3

# retries = 0

# while retries < 5:
#     print(f"retries not at 5 yet. It is at {retries}")
#     retries += 1
#     if retries == 5:
#         print("retries hit 5. Work complete")

# debug challenge

servers = ["web01", "web02", "db01"]

for server in servers:
    print(f"Checking {server}")

servers.append("cache01")

print(f"Total servers: {len(servers)}")
