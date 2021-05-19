from __future__ import unicode_literals
import os, sys
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import *
from linebot.exceptions import InvalidSignatureError
import requests
import configparser
import random

xapp = Flask(__name__)

#這是註冊 line 給的 
channel_token = "LnaF+kFrRaEfCpGTeHmjCaZuHEI77T7VdHYJfrYxr3UFN/KL5Cb+TAhQJWYld2U2Cjx9CLkuwSclMcxupjsYBnQmz7NCuq0dey8IkjB2ZQXEGfs1oyReCIlJ44/Nats/972/aoApYbjDFE1GjgAa1AdB04t89/1O/w1cDnyilFU="
channel_secret = "3604eceb8524e24dd7eede2dcfbd95d1"

if channel_secret is None:
   print('Set LINE_CHANNEL_SECRET as environment variable.')
   sys.exit(1)
if channel_token is None:
   print('Set LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
   sys.exit(1)

line_bot_api = LineBotApi(channel_token)
handler = WebhookHandler(channel_secret)

# https://a2ee41a6d68a.ngrok.io/bot_wsgi/linebot   && 這是給line Webhook settings 的 RUL, USE Webhook 要打勾

@xapp.route("/linebot", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    handler.handle(body, signature)
    return ""

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    msg = event.message.text
    msg = msg.encode('utf-8')	
	#因為LINE有些預設資料,我們在此排除
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef": 
       input_text = event.message.text       
       #print("AAA" + input_text)
       if input_text == '查詢匯率':
            #print("BBB" + input_text)
            resp = requests.get('https://tw.rter.info/capi.php')
            currency_data = resp.json()
            usd_to_twd = currency_data['USDTWD']['Exrate']
            print(usd_to_twd)
            line_bot_api.reply_message( event.reply_token,
                TextSendMessage(text=f'美元 USD 對台幣 TWD：1:{usd_to_twd}')   )
       elif event.message.text == "貼圖":
            line_bot_api.reply_message( event.reply_token,
                StickerSendMessage(package_id=1, sticker_id=2)  )
       elif event.message.text == "愛睏":
            line_bot_api.reply_message( event.reply_token,
                StickerSendMessage(package_id=1, sticker_id=1)  )
       else:
            line_bot_api.reply_message( event.reply_token,
                TextSendMessage(text="您的訊息："+event.message.text) )

    return ""

if __name__ == "__main__":
   xapp.run(debug=True)
