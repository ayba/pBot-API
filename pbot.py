import json
import random
import requests
import js2py
import time

apiName = 'mobile-api'
apiKey1 = 'h7k7vxesorsqjzux'
apiKey2 = 'fkk1qj0o4cxrnvzooi1uwayhlj1z5k1j'

def getTimeStamp():
    r = requests.get('http://p-bot.ru/api/getTimestamp')
    html = r.text
    data = json.loads(html)
    return data['timestamp']

def current_milli_time():
    return round(time.time() * 1000)

c32 = js2py.eval_js("function(t) {for (var e = function() {for (var t, e = [], n = 0; n < 256; n++) {t = n;for (var s = 0; s < 8; s++) t = 1 & t ? 3988292384 ^ t >>> 1 : t >>> 1;e[n] = t}return e}(), n = -1, s = 0; s < t.length; s++) n = n >>> 8 ^ e[255 & (n ^ t.charCodeAt(s))];return (-1 ^ n) >>> 0}")

def getC(t):
    global apiName, apiKey1, apiKey2, c32
    preC = apiName + str(t) + apiKey1 + apiKey2
    return c32(preC)

class DialogRequest:
    def __init__(self, request: str, answer: str):
        self.request = request
        self.answer = answer

class Dialog:
    
    def __init__(self, dialogId, userName):
        self.dialogId = dialogId
        self.lang = 'ru'
        self.botName = 'ρBot'
        self.userName = userName
        self.a = apiName
        self.b = ''
        self.c = 0
        self.d = 0
        self.e = 0
        self.t = 0
        self.x = 0
        self.requests = [DialogRequest('', ''), DialogRequest('', ''), DialogRequest('', '')]

    def reset(self):
        global c32
        t = getTimeStamp()
        self.b = str(t) + 'b'
        self.t = t
        self.c = getC(t)
        self.d = c32(str(current_milli_time()) + "d")
        self.e = random.random()
        self.x = random.random() * 10

    def sendMessage(self, text):
        self.reset()
        r = requests.post('http://p-bot.ru/api/getAnswer', data = {
            'request': text,
            'request_1': self.requests[0].request,
            'answer_1': self.requests[0].answer,
            'request_2': self.requests[1].request,
            'answer_2': self.requests[1].answer,
            'request_3': self.requests[2].request,
            'answer_3': self.requests[2].answer,
            'dialog_lang': self.lang,
            'prefLang': self.lang,
            'bot_name': self.botName,
            'user_name': self.userName,
            'dialog_id': self.dialogId,
            'allowAbuse': False,
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'd': self.d,
            't': self.t,
            'e': self.t,
            'x': self.x,
        }, headers = {
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'file://',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G955N Build/NRD90M.G955NKSU1AQDC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'X-Requested-With': 'air.kengineairpro',
            'Connection': 'keep-alive'
        })
        html = r.text
        #print(html)
        data = json.loads(html)


        self.requests[2].request = self.requests[1].request
        self.requests[2].answer = self.requests[1].answer

        self.requests[1].request = self.requests[0].request
        self.requests[1].answer = self.requests[0].answer

        self.requests[0].request = text
        self.requests[0].answer = data['answer']

        return data['answer']
    