from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from flask import Flask, request
from google_sheets import add_thank, get_thanks_summary

app = Flask(__name__)
client = WebClient(token='your-slack-bot-token')

@app.route('/thank', methods=['POST'])
def thank_user():
    data = request.form
    user_id = data.get('user_id')
    recipient_id = data.get('text').split()[0]
    message = " ".join(data.get('text').split()[1:])
    points = int(data.get('points', 0))

    # Додати подяку в Google Sheets
    add_thank(user_id, recipient_id, message, points)

    try:
        client.chat_postMessage(channel=recipient_id, text=f"You've been thanked! {message}")
    except SlackApiError as e:
        return str(e), 400

    return "", 200

if __name__ == "__main__":
    app.run(port=3000)

# Відправка підсумків вдячностей наприкінці місяця

from google_sheets import get_thanks_summary
from collections import defaultdict

def send_monthly_summary():
    thanks_list = get_thanks_summary()

    summary = defaultdict(list)
    for thanks in thanks_list:
        summary[thanks['recipient_id']].append(thanks['message'])

    for recipient, messages in summary.items():
        summary_message = "\n".join(messages)
        try:
            client.chat_postMessage(channel=recipient, text=f"Summary of thanks: {summary_message}")
        except SlackApiError as e:
            print(f"Failed to send summary: {e}")

#Надання доступу HR

@app.route('/hr_summary', methods=['GET'])
def hr_summary():
    thanks_list = get_thanks_summary()

    summary = defaultdict(int)
    for thanks in thanks_list:
        summary[thanks['recipient_id']] += thanks['points']

    sorted_summary = sorted(summary.items(), key=lambda x: x[1], reverse=True)
    return {"summary": sorted_summary}, 200

