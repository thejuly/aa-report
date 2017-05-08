import os
from flask import Flask, request
import json
import requests

userThongpoon = '12f28ead31c048fe8de91270e807c871'

app = Flask(__name__)

# for test route
@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'

@app.route('/profile/<user>')
def profile(user):
    return '<h2>Tuna is good %s</h2>' % user

@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h2>Tuna is good %s</h2>' % post_id

@app.route('/temp')
def temp():
    sendMessage = 'Temp report in period'
    sendText(userThongpoon,sendMessage)
    return '',200

# end test route


# for line bot
@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)

    #user = user who send message to me
    #messageGet = message that user send to me
    #typeGet = type of data that user send to me
    user = decoded["events"][0]['replyToken']
    messageGet = decoded["events"][0]['message']['text']
    typeGet = decoded["events"][0]['message']['type']
    #print('print User',user)

    if messageGet == 'Temp':
        sendMessage = 'report temp'

    if messageGet == 'Rec':
        sendMessage = 'report rectifier'

    if messageGet == 'Cont':
        sendMessage = 'report Controller'        

    if messageGet == 'Netw':
        sendMessage = 'report Network'   
    
    #sendText(user,'sendText')
    sendText(user,sendMessage)
    return '',200

def sendText(user, text):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer wbeBaLPb7xIuGymdaHU9yHy300QZ383XYgewhXLSoRe3TnlWo1xQuypNFpis1ExGrSTV1WpmtmQEiaR9tRPQHFUspwI9rVk2Ajfrg1WUwFpV9ewvq/vDx9LItfeNW+9y6Ih/OcwNpJPB/UfE9afIFwdB04t89/1O/w1cDnyilFU='
 
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }
 
    data = json.dumps({
        "replyToken":user,
        "messages":[{
            "type":"text",
            "text":text
        }]
    })
 
    r = requests.post(LINE_API, headers=headers, data=data)
    

# end line bot

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
