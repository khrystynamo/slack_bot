import os
import logging
import monthly_report
from user_service import UserService
from support_service import SupportService
from charity_service import CharityService
from views import create_collect_thanks_form, thanks_form_callback_id
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

token = os.environ.get("SLACK_BOT_TOKEN")
signing_secret = os.environ.get("SLACK_SIGNING_SECRET")

app = App(token=token, signing_secret=signing_secret)
user_service = UserService()
support_service = SupportService()
charity_service = CharityService()


@app.event("message")
def message_hello(message, say):
    logger.debug(message)
    say(f"Hey there <@{message['user']}>!")


@app.command("/get_support")
def handle_get_support(ack, body, client):
    ack()
    user_id = body["user_id"]
    support_message = support_service.get_random_message()
    client.chat_postMessage(channel=user_id, text=support_message)


@app.command("/charity")
def handle_charity(ack, body, client):
    ack()
    user_id = body["user_id"]
    charity_message = charity_service.get_charity_info()
    client.chat_postMessage(channel=user_id, blocks=charity_message)


@app.command("/thank_user")
def handle_thank_user(ack, body, client):
    ack()
    client.views_open(trigger_id=body["trigger_id"], view=create_collect_thanks_form())


@app.view(thanks_form_callback_id)
def handle_thanks_form_submission(ack, body, view, client):
    ack()
    user_id = body["user"]["id"]
    chosen_user = view["state"]["values"]["user_block"]["chosen_user"]["selected_user"]
    description = view["state"]["values"]["description_block"]["description_input"][
        "value"
    ]
    score = view["state"]["values"]["score_block"]["score_input"]["value"]

    logger.info(f"{chosen_user}, {description}, {score}")
    user_service.add_thanks_to_user(user_id, chosen_user, description, score)

    try:
        client.chat_postMessage(
            channel=user_id, text=(f"Thank you for submitting the 'Thank you' form!")
        )
    except Exception as e:
        logger.error(f"Opps! Error {e}")


if __name__ == "__main__":
    monthly_report.schedule_monthly_message()
    app.start(port=int(os.environ.get("PORT", 3000)))
