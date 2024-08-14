from apscheduler.schedulers.background import BackgroundScheduler
import calendar
from datetime import datetime, timedelta
from slack_sdk import WebClient
import os

from user_service import UserService

client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))


def create_message_template(messages, score):
    text = "\n".join([f"• {m}" for m in messages])
    return {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Hello!* :wave:\nIt's been a lovely month and you received a bunch of kind words.",
                },
            },
            {"type": "divider"},
            {"type": "section", "text": {"type": "mrkdwn", "text": text}},
            {"type": "divider"},
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*Total score*: {score}"},
            },
        ]
    }


def get_last_working_day(year, month):
    last_day = calendar.monthrange(year, month)[1]
    last_date = datetime(year, month, last_day)
    if last_date.weekday() == 5:
        last_date -= timedelta(1)
    elif last_date.weekday() == 6:
        last_date -= timedelta(2)
    return last_date


def send_monthly_messages():
    user_service = UserService()
    user_records_dict = user_service.get_all_records_dict()
    for user_id, thanks in user_records_dict.items():
        user_total_score = 0
        messages = []
        for thank in thanks:
            user_total_score += int(thank["score"])
            messages.append(thank["describe"])

        text = create_message_template(messages, user_total_score)
        client.chat_postMessage(channel=user_id, blocks=text["blocks"])


def schedule_monthly_message():
    today = datetime.today()
    last_working_day = get_last_working_day(today.year, today.month)
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_monthly_messages, "date", run_date=last_working_day)
    scheduler.start()
