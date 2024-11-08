import os
from mcrcon import MCRcon as r
import schedule
import time
from dotenv import load_dotenv

env = load_dotenv()
host = os.getenv('RCON_HOST')
pwd = os.getenv('RCON_PASSWORD')

def save():
    with r(host, pwd) as mcr:
        mcr.command('/say Saving...')
        mcr.command('/save-all')

schedule.every().hour.do(save)

while True:
    schedule.run_pending()
    time.sleep(10)