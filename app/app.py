#from __future__ import unicode_literals
import os
import sys
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
# @app.route('/', methods=['POST'])
def hello():
    print("AAA111-2222")

    # print('聯'.encode('utf-8'))
    # print('聯'.encode('big5'))
    # print('聯')
    # VSCode 中文無法輸入，不要用ubuntu軟體 安裝，要透過微軟官方庫安裝
    # wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
    # sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
    # sudo apt update && sudo apt install code
    # 突然顯示又正常了，可能是因為 Ubuntu 沒有安裝中文語系的關係
    conn = fdb.connect(
        # 要指定字集，不然預設是ASCII轉碼會錯誤
        host='192.168.3.35', database='002', port=3050, user='sysdba', password='masterkey', sql_dialect=3, charset='Big5'
    )
    # 我算算的可以正常顯示
    # conn = fdb.connect(
    #    host='192.168.3.35', database='C:/xOneServer/DATAS/001.FDB', port=3055, user='sysdba', password='admin123' , sql_dialect=3  , charset='UTF-8'
    # )
    # print("AAA222")
    print('Firebird version:', conn.version)
    print('ODS version:', conn.ods)
    cur = conn.cursor()

    cur.execute("select cusno,cusname from custom order by cusno rows 2 ")

    print("BBB")
    html = '<html>\n'
    html = html + ' <head>\n'
#    html = html + ' <style>\n'
#    html = html + '  table, th, td { \n'
#    html = html + '  border: 1px solid black;\n'
#    html = html + '  } \n'
#    html = html + ' </style>\n'
    html = html + '  <meta charset="utf-8">\n'
    html = html + '  <title>客戶資料</title>\n'
    html = html + '  <link href="minimal-table.css" rel="stylesheet" type="text/css">\n'
    html = html + ' </head>\n'
    html = html + '<body>\n'
    html = html + 'Hooray, mod_wsgi is working\n'
    html = html + '<h1> 客戶資料 </h1>\n'
 
    html = html + '<Table>\n'  
    html = html + '<tr>\n'  
    for fieldDesc in cur.description:
        html = html + '<th>\n'  
        html = html + fieldDesc[fdb.DESCRIPTION_NAME].ljust(fieldDesc[fdb.DESCRIPTION_DISPLAY_SIZE]) + '\n'
        html = html + '</th>\n'  
    html = html + '</tr>\n'  
    print('-' * 78 )

    # For each row, print the value of each field left-justified within
    # the maximum possible width of that field.
    fieldIndices = range(len(cur.description))
    for row in cur:
        html = html + '<tr>\n'  
        for fieldIndex in fieldIndices:
            fieldValue = str(row[fieldIndex])
            fieldMaxWidth = cur.description[fieldIndex][fdb.DESCRIPTION_DISPLAY_SIZE]
            html = html + '<td>\n'  
            html = html + fieldValue.ljust(fieldMaxWidth) + '\n'
            html = html + '</td>\n'  

        html = html + '</tr>\n'  

    html = html + '</Table>\n'  

    print(html)
    cur.execute("select cusno,cusname from custom order by cusno rows 2 ")
    print("DDD")


    print("DDD-1-1-聯")
    for xrow in cur:
        print("DDD-2-2")
        html = html + '<br>' + xrow[1] + '\n'
        #html = html + '<br>' + str((''+xrow[1]).encode('utf-8').strip()) + '\n'
      #  print("DDD-3" )
    #    html = html + row[1] + '\n'  # .encode("utf-8").strip() + b'\n' .encode('cp950').decode('utf-8')
    html = html + '</body>\n'
    html = html + '</html>\n'
    # response_header = [('Content-type','text/html')]
    # start_response(status,response_header)

    conn.close()
    print("FFF")

    return html  # "<h1>Hello World!</h1>"


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
