#!/usr/bin/env python3

import subprocess  
import yaml 
import logging 
import schedule
import time
import datetime

# Configure logging to file
logging.basicConfig(
    level=logging.INFO,
    filename="monitor.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def read_config(config_file):
    """
    Reads a YAML config file.

    Args:
        config_file (str): Path to YAML file.

    Returns:
        tuple: (dict, message), or (None, error_message).
    """
    try:
        logging.debug(f"Reading config: {config_file}")
        with open(config_file, "r") as file:
            config = yaml.safe_load(file)
        logging.info(f"Config read: {config}")
        return config, "OK"
    except FileNotFoundError:
        logging.error(f"Config file {config_file} not found")
        return None, "Config file not found"
    except yaml.YAMLError:
        logging.error(f"Invalid YAML format")
        return None, "Invalid YAML format"
    except Exception as exc:
        logging.error(f"Error: {exc}")
        return None, f"Error: {exc}"


def get_disk_usage():
    """
    Runs `df -h /` to get root disk usage percentage.

    Returns:
        tuple: (used_percent, message), or (None, error_message).
    """
    try:
        logging.debug("Running df -h /")
        result = subprocess.run(
            ["df", "-h", "/"], capture_output=True, text=True, check=True
        )
        lines = result.stdout.splitlines()
        disk_line = lines[-1]
        columns = disk_line.split()
        used_percent = float(columns[4].rstrip("%"))
        logging.info(f"Disk usage: {used_percent}%")
        return used_percent, "OK"
    except subprocess.CalledProcessError as exc:
        logging.error(f"Error running df: {exc.stderr}")
        return None, f"Error: {exc.stderr}"
    except Exception as exc:
        logging.error(f"Error: {exc}")
        return None, f"Error: {exc}"


def get_uptime():
    """
    Runs `uptime` to get 1-minute load average.

    Returns:
        tuple: (load_1min, message), or (None, error_message).
    """
    try:
        logging.debug("Running uptime")
        result = subprocess.run(["uptime"], capture_output=True, text=True, check=True)
        output = result.stdout
        parts = output.split("load average:")
        load_part = parts[1]
        load_1min = float(load_part.split(",")[0])
        logging.info(f"CPU load (1-min): {load_1min}")
        return load_1min, "OK"
    except subprocess.CalledProcessError as exc:
        logging.error(f"Error running uptime: {exc.stderr}")
        return None, f"Error: {exc.stderr}"
    except Exception as exc:
        logging.error(f"Error: {exc}")
        return None, f"Error: {exc}"


def monitor_system(config_file):
    """
    Checks disk usage and CPU load, logs alerts if thresholds exceeded.

    Args:
        config_file (str): Path to YAML config file.
    """
    try:
        logging.info("Running system check")
        config, config_status = read_config(config_file)
        if config is None:
            logging.error(f"Cannot proceed: {config_status}")
            return

        used_percent, disk_status = get_disk_usage()
        load_1min, load_status = get_uptime()

        if used_percent is None or load_1min is None:
            logging.error("Cannot proceed due to metric errors")
            return

        disk_threshold = config.get("disk_threshold_percent", 90.0)
        cpu_threshold = config.get("cpu_threshold", 1.0)
        server = config.get("server", "unknown")

        if used_percent > disk_threshold:
            logging.warning(
                f"Disk usage {used_percent}% exceeds threshold {disk_threshold}% on {server}"
            )
        else:
            logging.info(
                f"Disk usage {used_percent}% is below threshold {disk_threshold}%"
            )

        if load_1min > cpu_threshold:
            logging.warning(
                f"CPU load {load_1min:.2f} exceeds threshold {cpu_threshold} on {server}"
            )
        else:
            logging.info(f"CPU load {load_1min:.2f} is below threshold {cpu_threshold}")

    except Exception as exc:
        logging.error(f"Monitor failed: {exc}")


if __name__ == "__main__":
    config_file = "monitor_config.yaml"
    # Schedule the monitor every 10 seconds
    schedule.every(10).seconds.do(monitor_system, config_file=config_file)
    logging.info("Starting scheduler")
    print("Scheduler running. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)
