from flask import Flask, render_template, jsonify
import time, traceback, asyncio
from threading import Thread
from requests import get


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def keep_alive():
    while 1:
        time.sleep(5 * 60) # Every 5 mins
        print('[+] Keep Alive', flush=True)
        try: get('https://avaitor-bot.onrender.com')
        except: print(traceback.format_exc(), flush=True)


if __name__ == '__main__':
    Thread(target=lambda: app.run('0.0.0.0')).start()
    Thread(target=keep_alive).start()
    import avaitor_bot, luckyjet_bot, mines_bot, ads
    async def run_bots():
        for task in asyncio.as_completed([avaitor_bot.bot_main(), luckyjet_bot.bot_main(), mines_bot.bot_main()]):
            await task
    asyncio.run(run_bots())
    


