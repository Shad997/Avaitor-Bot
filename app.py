from flask import Flask
from requests import get
import time, traceback

class bot: 
    def glt(): return 0
app = Flask(__name__)

@app.route('/')
def index():
    return f'Server is UP v1.3 <br> Last signal sent {int(time.time() - bot.glt())}sec ago'

def keep_alive():
    while 1:
        time.sleep(5 * 60) # Every 5 mins
        print('[+] Keep Alive', flush=True)
        try: get('https://avaitor-bot.onrender.com')
        except: print(traceback.format_exc(), flush=True)


if __name__ == '__main__':
    from threading import Thread
    Thread(target=lambda: app.run('0.0.0.0')).start()
    Thread(target=keep_alive).start()
    import bot
    bot.run()


