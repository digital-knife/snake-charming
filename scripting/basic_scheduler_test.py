#!/usr/bin/env python3

import time
import schedule
import logging

# configure loggin to file
logging.basicConfig(
    level=logging.INFO,
    filename="task.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def job():
    """
    Simple print to stdout when run.
    """
    print("Running Task!")
    logging.info("Scheduled task executed")


# schedule job
schedule.every(5).seconds.do(job)

# run scheduler
logging.info("Starting Scheduler")
print("Starting Scheduler. Press CRTL+C to stop")
while True:
    schedule.run_pending()
    time.sleep(1)
