from linebot import LineBotApi
import random
from linebot.models import TextSendMessage
import os

version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"
      time: "09:00"
      # Use Japan Standard Time (UTC +09:00)
      timezone: "Asia/Taipei"

line_uuid = os.environ['LINE_UUID']
token = os.environ['TOKEN']
fortune = random.choice(['大凶', '凶', '末吉', '吉','中吉','大吉'])
line_bot_api = LineBotApi(token)

line_bot_api.push_message(
    line_uuid,
    TextSendMessage(text=fortune))

