import requests
import json
url = 'http://127.0.0.1:5000/api/ocr'
img1_file = {
    'file1': open('chinese.jpeg', 'rb')
}
res = requests.post(url=url, data={'compress': 0}, files=img1_file)
text = res.text.encode('utf-8').decode('unicode_escape')
print(text)
