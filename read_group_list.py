import requests
import logging
import dotenv
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

dotenv.load_dotenv()

# 定義 API 網址和 Channel Access Token
api_url = 'https://api.line.me/v2/bot'
access_token = os.getenv('CHANNEL_ACCESS_TOKEN')

# 設定 headers
headers = {
    'Authorization': 'Bearer ' + access_token
}

# 使用 get_group_list API 獲取 Channel 加入的所有 Group Name 和 ID
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
