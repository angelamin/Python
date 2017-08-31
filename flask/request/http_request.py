import requests
import base64


file_path = './test.jpg'
image_str = base64.b64encode(open(file_path).read())
# print(image_str)
payload = {'img_data':"xiamin"}
import json
#payload = json.dumps(payload)
url = 'http://127.0.0.1:8888/mtcnn'
# for i in range(0, 10000):
r = requests.post(url, payload)
print(r.text)
