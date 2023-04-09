import requests
import os
import dotenv

dotenv.load_dotenv()

# 設定 Line bot 的 Channel Access Token
CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')

# 設定 API 端點
API_ENDPOINT = 'https://api.line.me/v2/bot'

# 設定 API 路徑
API_PATH = '/followers/ids'

# 設定 headers
headers = {
    'Authorization': f'Bearer {CHANNEL_ACCESS_TOKEN}'
}

# 呼叫 API
response = requests.get(API_ENDPOINT + API_PATH, headers=headers)

# 解析回應
if response.status_code == requests.codes.ok:
    # 列印每個已加入好友的 user ID
    user_ids = response.json()['userIds']
    for user_id in user_ids:
        print(user_id)
else:
    print(f'Error: {response.status_code} {response.text}')
