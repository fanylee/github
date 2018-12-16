import requests
import webbrowser
import time

api = 'https://api.github.com/repositories/59720190'
web_page = 'https://github.com/channelcat/sanic'
last_update = '2018-12-13T04:05:45Z'
all_info = requests.get(api).json()
cur_update = all_info['updated_at']
print(cur_update)



if not last_update:
    last_update = cur_update

if last_update < cur_update:
    webbrowser.open(web_page)

