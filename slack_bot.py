import os
from slack import WebClient
from slack.errors import SlackApiError

slack_token = os.environ.get('SLACK_API_TOKEN')

client = WebClient(token=slack_token)

#code here that loads the CSV and finds a specific call
#location = row['location']
#date=row['date']

location = "1600 Pennsylvania Ave"
date = "March 7, 2023"

msg = f"Call placed from {location} on {date}!"


try:
    response = client.chat_postMessage(
        channel="slack-bots",
        text=msg,
        unfurl_links=True, 
        unfurl_media=True
    )
    print("success!")
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")