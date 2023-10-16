
from telethon import TelegramClient
import subprocess

# Use your own values from https://my.telegram.org
api_id = 15327260
api_hash = '5eb6e313b64a21157e207cacae1c0b5d'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('myUserName', api_id, api_hash) as client :
    # Linux Specific shell command
    arg = 'ip route list'
    p = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
    data = p.communicate()[0].decode().split()
    ip = data[data.index('src')+1]
    msg = 'The ip of your RaspberryPi is ' + ip
    client.loop.run_until_complete(client.send_message('me', msg))
    print('ip sent')