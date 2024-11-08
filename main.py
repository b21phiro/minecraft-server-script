from mcrcon import MCRcon as r
import schedule
import time

server = "192.168.50.161"
pwd = "1234Qwer!"

def save():
    with r(server, pwd) as mcr:
        mcr.command('/say Saving...')
        mcr.command('/save-all')

schedule.every().hour.do(save)

while True:
    schedule.run_pending()
    time.sleep(10)