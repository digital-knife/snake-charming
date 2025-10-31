#!/usr/bin/env python3

import requests
import yaml
import logging
import schedule
import time
import datetime

# configure logging to file
logging.basicConfig(
    level=logging.INFO,
    filename="api_monitor.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def read_config(config_file):
    """
    Read a YAML config file.

    Args:
        config_file (str): Path to YAML file.

    Returns:
        Tuple: (dict, message), or (None, error_message)
    """
    try:
        logging.debug(f"Reading config file: {config_file}")
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


def fetch_metrics(api_url):
    """
    Fetches metrics from an API (mocked with json placeholder).

    Args:
        api_url (str): API endpoint URL.

    Returns:
        tuple: (cpu_usage, disk_usage, message), or (None, None, error_message).
    """
    try:
        logging.debug(f"fetching metrics from {api_url}")
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise error for non-200 status
        # data = response.json()
        # logging.debug(f"Raw API payload: {data}")
        cpu_usage = 75.0
        disk_usage = 85.0
        logging.info(f"Metrics fetched: CPU={cpu_usage}%, Disk={disk_usage}%")
        return cpu_usage, disk_usage, "OK"
    except requests.HTTPError as exc:
        logging.error(f"HTTP error: {exc}")
        return None, None, f"HTTP error: {exc}"
    except requests.ConnectionError:
        logging.error(f"Network connection failed")
        return None, None, "Network connection failed"
    except Exception as exc:
        logging.error(f"Error: {exc}")
        return None, None, f"Error: {exc}"


def monitor_system(config_file):
    """
    Fetches metrics from API, logs alerts if thresholds exceeded

    Args:
        config_file (str): Path to YAML config file.
    """
    try:
        logging.info("Running API monitor")
        config, config_status = read_config(config_file)
        if config is None:
            logging.error(f"Cannot proceed: {config_status}")
            return

        api_url = config.get("api_url", "https://jsonplaceholder.typicode.com/posts/1")

        # debug
        raw = fetch_metrics(api_url)
        logging.debug(f"fetch_metrics raw return: {raw}")
        cpu, disk, status = raw
        # end debug

        cpu_threshold = config.get("cpu_threshold", 90.0)
        disk_threshold = config.get("disk_threshold_percent", 90.0)
        server = config.get("server", "unknown")

        cpu_usage, disk_usage, status = fetch_metrics(api_url)
        if cpu_usage is None or disk_usage is None:
            logging.error(f"Cannot proceed: {status}")
            return

        if cpu_usage > cpu_threshold:
            logging.warning(
                f"CPU usage {cpu_usage}% exceeds threshold {cpu_threshold}% on {server}"
            )
        else:
            logging.info(
                f"CPU usage {cpu_usage} is below threshold {cpu_threshold} on {server}"
            )

        if disk_usage > disk_threshold:
            logging.warning(
                f"Disk usage {disk_usage}% exceeds thrshold {disk_threshold} on {server}"
            )
        else:
            logging.info(
                f"Disk usage {disk_usage}% is below threshold {disk_threshold} on {server}"
            )

    except Exception as exc:
        logging.error(f"Monitor failed: {exc}")


if __name__ == "__main__":
    config_file = "monitor_config.yaml"
    # schedule monitor everyt 30 seconds
    schedule.every(30).seconds.do(monitor_system, config_file=config_file)
    logging.info("Starting Scheduler")
    print("Scheduler running. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)
