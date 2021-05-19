#from __future__ import unicode_literals
import os,sys 
from flask import Flask, request, abort
#from linebot import LineBotApi, WebhookHandler
#from linebot.exceptions import InvalidSignatureError
#from linebot.models import MessageEvent, TextMessage, TextSendMessage
import fdb
#import requests
#import configparser
#import random

app = Flask(__name__)

#line_bot_api = LineBotApi("LnaF+kFrRaEfCpGTeHmjCaZuHEI77T7VdHYJfrYxr3UFN/KL5Cb+TAhQJWYld2U2Cjx9CLkuwSclMcxupjsYBnQmz7NCuq0dey8IkjB2ZQXEGfs1oyReCIlJ44/Nats/972/aoApYbjDFE1GjgAa1AdB04t89/1O/w1cDnyilFU=")
#handler = WebhookHandler("3604eceb8524e24dd7eede2dcfbd95d1")

# 接收 LINE 的資訊
@app.route("/")
#@app.route('/', methods=['POST'])
def hello():
    conn = fdb.connect(
        host='127.0.0.1', database='001',
        port=3050,
        user='sysdba', password='masterkey'
    )
    print("AAA" )
    cur = conn.cursor()
    cur.execute("select * from custom order by cusno")
    print("BBB" )
    print( cur.fetchall() )
   # for c in cur.fetchall():
   #     print("CCC" )
   #     print(c.encode('big-5'))
    #    print("DDD" )
    #print("EEE" )
    conn.close()
    print("FFF" )
    #status = '200 OK'
    html = '<html>\n' \
           '<body>\n' \
           ' Hooray, mod_wsgi is working\n' \
           '</body>\n' \
           '</html>\n'
   # response_header = [('Content-type','text/html')]
   # start_response(status,response_header)
    return html  ##"<h1>Hello World!</h1>"

if __name__ == "__main__":
   app.run(debug=True)



# #這是註冊 line 給的 
# channel_token = "LnaF+kFrRaEfCpGTeHmjCaZuHEI77T7VdHYJfrYxr3UFN/KL5Cb+TAhQJWYld2U2Cjx9CLkuwSclMcxupjsYBnQmz7NCuq0dey8IkjB2ZQXEGfs1oyReCIlJ44/Nats/972/aoApYbjDFE1GjgAa1AdB04t89/1O/w1cDnyilFU="
# channel_secret = "3604eceb8524e24dd7eede2dcfbd95d1"
# if channel_secret is None:
#    print('Set LINE_CHANNEL_SECRET as environment variable.')
#    sys.exit(1)
# if channel_token is None:
#    print('Set LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
#    sys.exit(1)
# line_bot_api = LineBotApi(channel_token)
# handler = WebhookHandler(channel_secret)
# # https://a2ee41a6d68a.ngrok.io/bot_wsgi/linebot   && 這是給line Webhook settings 的 RUL, USE Webhook 要打勾
# @app.route("/linebot", methods=['POST'])
# def callback():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)
#     handler.handle(body, signature)
#     try:
#         print("body: "+body, signature)
#         handler.handle(body, signature)        
#     except InvalidSignatureError:
#         abort(400)
#     return 'OK'
# # # 學你說話
# @handler.add(MessageEvent, message=TextMessage)
# def pretty_echo(event):
#     print( "user_id :" + event.source.user_id )
#     #因為LINE有些預設資料,我們在此排除
#     if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef": 
#        input_text = event.message.text       
#        print("AAA" + input_text)
#        if input_text == '查詢匯率':
#           print("BBB" + input_text)
#           resp = requests.get('https://tw.rter.info/capi.php')
#           currency_data = resp.json()
#           usd_to_twd = currency_data['USDTWD']['Exrate']
#           print(usd_to_twd)
#           line_bot_api.reply_message( event.reply_token
#              , TextSendMessage(text=f'美元 USD 對台幣 TWD：1:{usd_to_twd}')   )

