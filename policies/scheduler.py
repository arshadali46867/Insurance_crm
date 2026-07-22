from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import renewal_job


def start():

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        renewal_job,
        "cron",
        hour=9,
        minute=0
    )

    scheduler.start()