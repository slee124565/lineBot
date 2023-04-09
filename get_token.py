import os

import requests
import logging
import dotenv

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

dotenv.load_dotenv()

# 以下三個變數需要您填寫相應的資訊
CHANNEL_ID = os.getenv('CHANNEL_ID')
CHANNEL_SECRET = os.getenv('CHANNEL_SECRET')
CALLBACK_URL = os.getenv('CALLBACK_URL')

# 定義 API 網址
TOKEN_API_URL = "https://api.line.me/v2/oauth/accessToken"

# 設定 post 請求的參數
params = {
    "grant_type": "client_credentials",
    "client_id": CHANNEL_ID,
    "client_secret": CHANNEL_SECRET
}

# 發送 post 請求
response = requests.post(TOKEN_API_URL, data=params)

# 解析回應的 JSON
access_token = response.json()["access_token"]

# 印出取得的 Channel Access Token
print(access_token)
print(response.json())

headers = {
    'Authorization': 'Bearer ' + access_token
}

# 使用 get_group_list API 獲取 Channel 加入的所有 Group Name 和 ID
api_url = 'https://api.line.me/v2/bot'
response = requests.get(api_url + '/groups/ids', headers=headers)

if response.status_code == requests.codes.ok:
    # 獲取成功
    groups = response.json()['groupIds']
    for group_id in groups:
        # 使用 get_group_summary API 獲取群組名稱
        response = requests.get(api_url + '/groups/' + group_id + '/summary', headers=headers)
        if response.status_code == requests.codes.ok:
            # 獲取成功
            group_name = response.json()['groupName']
            print(f"Group Name: {group_name}, Group ID: {group_id}")
        else:
            print(f"Failed to get group summary for group ID {group_id}: {response.status_code}")
else:
    print(f"Failed to get group IDs: {response.status_code}")

# # 設定 headers
# headers = {
#     'Authorization': 'Bearer ' + access_token
# }

# 使用 get_friends API 獲取好友列表
response = requests.get(api_url + '/bot/friends', headers=headers)

if response.status_code == requests.codes.ok:
    # 獲取成功
    friends = response.json()['friends']
    for friend in friends:
        # 印出好友的 ID 和顯示名稱
        print(f"Friend ID: {friend['displayName']}, Friend ID: {friend['userId']}")
else:
    print(f"Failed to get friend list: {response.status_code}")
