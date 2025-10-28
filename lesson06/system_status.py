#!/usr/bin/env python3

import os  # For system-level operations like getting the hostname
import shutil  # For disk usage information


def get_hostname():
    """
    Gets the system's hostname (the name of the computer).

    Returns:
        str: The hostname, or None if something goes wrong.
    """
    try:
        hostname = os.uname().nodename  # Gets hostname from system info
        return hostname
    except Exception as exc:
        print(f"Error getting hostname: {exc}")
        return None


def get_disk_space(path="/"):
    """
    Gets disk space info for a given path (like the root directory "/").

    Args:
        path (str): The folder to check (defaults to "/").

    Returns:
        tuple: Three numbers (total, used, free disk space in bytes), or None if an error occurs.
    """
    try:
        disk_info = shutil.disk_usage(path)  # Returns a tuple (total, used, free)
        return disk_info
    except Exception as exc:
        print(f"Error getting disk space for {path}: {exc}")
        return None


def check_cpu_load():
    """
    Gets system load info as a tuple using os.getloadvg module in 1,5,15 load averages.
    """
    try:
        load_averages = os.getloadavg()
        return load_averages
    except Exception as exc:
        print(f"Error getting load averages {exc}")
        return None


load_averages = check_cpu_load()
print(f"{load_averages}")


def print_system_status():
    """
    Combines hostname and disk space info into a report.
    """
    hostname = get_hostname()  # Call the first function
    disk_info = get_disk_space()  # Call the second function
    load_averages = check_cpu_load()

    if hostname:
        print(f"System Hostname: {hostname}")
    else:
        print("Could not retrieve hostname.")

    if disk_info:
        total, used, free = disk_info  # Unpack the tuple into three variables
        print("Disk Space (root):")
        print(f"  Total: {total / (1024 ** 3):.2f} GB")  # Convert bytes to GB
        print(f"  Used: {used / (1024 ** 3):.2f} GB")
        print(f"  Free: {free / (1024 ** 3):.2f} GB")
    else:
        print("Could not retrieve disk space info.")

    if load_averages:
        one_min, five_min, fifteen_min = load_averages  # unpack tuple
        print("One, Five and Fifteen minute load averages.")
        print(f" One minute: {one_min:.2f}")
        print(f" Five minute:{five_min:.2f}")
        print(f" Fifteen minute: {fifteen_min:.2f}")
    else:
        print("Could not retrieve system load averages")


if __name__ == "__main__":
    print_system_status()
