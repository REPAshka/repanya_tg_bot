import json

with open('/home/repa/my_projects/repanya_tg_bot/creds.json') as json_file:
    data = json.load(json_file)
    print(data['repanya_tg_bot_token'])