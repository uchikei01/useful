import requests
import json
import datetime
import sys

def postSlack(msg=None, username=None, status=None): #status good warning danger
  DATETIME = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
  requests.post("your_webhook_url", data = json.dumps({
      'username': username,
      'icon_emoji': ':ghost:',
      'link_names': 1, # enable mention
      "attachments": [
          {
            "color":status,
            "text":'{0}({1})'.format(msg, DATETIME)
          }
          ]
  }))



if __name__ == '__main__':
  args = sys.argv
  msg = args[1]
  username = args[2]
  status = args[3]
  postSlack(msg, username, status)
