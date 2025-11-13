#!/usr/bin/env python3

import argparse
import subprocess


def get_uptime():
    try:
        out = subprocess.check_output(["uptime", "-p"], text=True).strip()
        return out
    except FileNotFoundError:
        return "Uptime command not found"
    except subprocess.CalledProcessError as exc:
        return f"uptime command failed with status {exc.returncode}"
    except Exception as exc:
        return f"error getting uptime: {exc}"


def main():
    parser = argparse.ArgumentParser(description="single-function demo: get_uptime()")
    parser.add_argument(
        "--quiet", action="store_true", help="Print only the uptime string"
    )
    args = parser.parse_args()

    uptime_str = get_uptime()
    if args.quiet:
        print(uptime_str)
    else:
        print("Result of get_uptime():")
        print(uptime_str)


if __name__ == "__main__":
    main()
