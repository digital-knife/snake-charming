#!/usr/bin/env python3

import argparse
import socket


def get_hostname():
    """
        python3 challenge_one.py
    expected output:
    hostname: my-machine-name
    """
    try:
        hostname = socket.gethostname().lower()
        return hostname
    except socket.error as exc:
        return f"no hostname found {exc}"
    except Exception as exc:
        return f"error getting hostname {exc}"


def main():
    parser = argparse.ArgumentParser(
        description="Single fucntion to check hostname of current machine."
    )
    parser.add_argument(
        "--quiet", action="store_true", help="Print only the hostname string"
    )
    args = parser.parse_args()
    hostname_str = get_hostname()

    if args.quiet:
        print(hostname_str)
    else:
        print(f"hostname: {hostname_str}")


if __name__ == "__main__":
    main()
