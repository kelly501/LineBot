from linebot import LineBotApi
import random
from linebot.models import TextSendMessage
import UUID
import TOKEN

line_uuid = UUID
token = TOKEN
fortune = random.choice(['大凶', '凶', '末吉', '吉','中吉','大吉'])
line_bot_api = LineBotApi(token)
line_bot_api.push_message(
    line_uuid,
    TextSendMessage(text=fortune))
