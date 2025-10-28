#!/usr/bin/env python3

import argparse


def start_service(args):
    print(f"Starting service '{args.name}' on port {args.port}")


def stop_service(args):
    print(f"Stopping service '{args.name}' on port {args.port}")


def main():
    parser = argparse.ArgumentParser(description="Mini service management CLI")
    subparser = parser.add_subparsers(dest="command", required=True)

    # Subcommand: start
    start_parser = subparser.add_parser("start", help="Start a service")
    start_parser.add_argument("--name", required=True, help="Service name")
    start_parser.add_argument("--port", type=int, default=8000, help="Port number")
    start_parser.set_defaults(func=start_service)

    # subcommand: stop
    stop_parser = subparser.add_parser("stop", help="Stop a service")
    stop_parser.add_argument("--name", required=True, help="Service name")
    stop_parser.set_defaults(func=stop_service)

    # parse args and execute
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
