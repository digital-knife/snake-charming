# # #!/usr/bin/env python3
# # def is_high(usage):
# #     if usage > 90:
# #         return "ALERT"
# #     return "OK"


# # status = is_high(90)
# # # print(status)  # ALERT
# # def disk_status(host):
# #     fake_df = {"web01": 72, "db01": 95}
# #     usage = fake_df.get(host, 0)
# #     if usage > 90:
# #         return f"ALERT: {host} {usage}%"
# #     return f"OK: {host} {usage}%"


# # for h in ["web01", "db01", "cache01"]:
# #     print(disk_status(h))


# def disk_status(host):
#     data = {"web01": 72, "db01": 95, "log01": 88}
#     usage = data.get(host, 0)
#     if usage > 90:
#         return f"ALERT: {host} {usage}%"
#     return f"OK: {host} {usage}%"


# for h in ["web01", "db01", "log01"]:
#     print(disk_status(h))


def disk_status(host):
    data = {"web01": 72, "db01": 95}
    usage = data.get(host, 0)
    if usage > 90:
        print(f"ALERT: {host} {usage}%")
    else:
        print(f"OK: {host} {usage}%")


disk_status("db01")
disk_status("web01")
