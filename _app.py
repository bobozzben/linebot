from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import requests
import configparser

import random

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

#line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
#handler = WebhookHandler(config.get('line-bot', 'channel_secret'))
line_bot_api = LineBotApi("LnaF+kFrRaEfCpGTeHmjCaZuHEI77T7VdHYJfrYxr3UFN/KL5Cb+TAhQJWYld2U2Cjx9CLkuwSclMcxupjsYBnQmz7NCuq0dey8IkjB2ZQXEGfs1oyReCIlJ44/Nats/972/aoApYbjDFE1GjgAa1AdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("3604eceb8524e24dd7eede2dcfbd95d1")


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print("body: "+body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    print( "user_id :" + event.source.user_id )
	#因為LINE有些預設資料,我們在此排除
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef": 
       input_text = event.message.text
       
       print("AAA" + input_text)
       if input_text == '查詢匯率':
            print("BBB" + input_text)
            resp = requests.get('https://tw.rter.info/capi.php')
            currency_data = resp.json()
            usd_to_twd = currency_data['USDTWD']['Exrate']
            print(usd_to_twd)
       line_bot_api.reply_message(
          event.reply_token,
          TextSendMessage(text=f'美元 USD 對台幣 TWD：1:{usd_to_twd}')   )

     
        # Phoebe 愛唱歌
    #    pretty_note = '♫♪♬'
    #    pretty_text = ''
        
    #    for i in event.message.text:        
    #        pretty_text += i
    #        pretty_text += random.choice(pretty_note)      

    
     #   line_bot_api.reply_message(
     #       event.reply_token,
     #       TextSendMessage(text=pretty_text)
     #   )
        
     #   message = StickerSendMessage(
     #        package_id='1',
     #        sticker_id='1'
     #   )
     #   line_bot_api.reply_message(event.reply_token, message)     

if __name__ == "__main__":
    app.run()
    