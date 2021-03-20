import requests
import json
url = 'http://127.0.0.1:8089/api/tr-run/'
img1_file = {
    'file': open('chinese.jpeg', 'rb')
}
res = requests.post(url=url, data={'compress': 0}, files=img1_file)
text = res.text.encode('utf-8').decode('unicode_escape')
print(json.loads(text).get('data').get('raw_out'))
