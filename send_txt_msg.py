import requests
import json
import dotenv
import os

dotenv.load_dotenv()

# 以下三個變數需要您填寫相應的資訊
# access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
# GROUP_ID = "YOUR_GROUP_ID"
# MEMBER_IDS = os.getenv('TEST_USER_ID').split(',')

# 設定 API 網址和 Channel Access Token
api_url = 'https://api.line.me/v2/bot/message/push'
access_token = os.getenv('CHANNEL_ACCESS_TOKEN')

# 設定 headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + access_token
}

# 設定傳送的訊息
user_id = os.getenv('TEST_USER_ID')  # 這裡請填入要傳送訊息的用戶 ID
message = {
    'type': 'text',
    'text': 'Hello, World!'
}

# 組合傳送的訊息和接收者
data = {
    'to': user_id,
    'messages': [message]
}

# 發送 POST 請求
response = requests.post(api_url, headers=headers, json=data)

# 處理回應
if response.status_code == requests.codes.ok:
    print('訊息已傳送')
else:
    print(f"傳送失敗: {response.status_code} {response.text}")