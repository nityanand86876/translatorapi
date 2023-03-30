import requests
from urllib.parse import quote
from flask import Flask
app = Flask(__name__)
@app.route('/<text>')
def perform_function(text):
    text1=quote(text)
    headers = {
        'authority': 'www.google.com',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://www.google.com',
        'referer': 'https://www.google.com/',
    }

    params = {
        'vet': '12ahUKEwiVkuSpvIP-AhXg8zgGHWtnApwQqDh6BAgIECw..i',
        'ei': '8GclZJXaDODn4-EP686J4Ak',
        'yv': '3',
        'cs': '0',
    }

    data = 'async=translate,sl:auto,tl:en,st:'+text1+',id:1680173079660,qc:true,ac:true,_id:tw-async-translate,_pms:s,_fmt:pc'

    response = requests.post('https://www.google.com/async/translate', params=params, headers=headers, data=data)
    response1=response.text
    response2=response1.split('<span id="tw-answ-target-text">')[1].split('</span>')[0]
    return response2


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1492)
