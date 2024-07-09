import time, traceback, asyncio
from threading import Thread
from requests import get
from flask import Flask

class bot: glt = lambda: 0
class bot2(bot): pass
class ads(bot): pass
app = Flask(__name__)

@app.route('/')
def index():
    bot_time = int(time.time() - bot.glt())
    bot2_time = int(time.time() - bot2.glt())
    ads_time = int(time.time() - ads.glt())
    return f'Server is UP v1.8 <br> Last avaitor signal sent {bot_time}sec ago <br> Last mines signal sent {bot2_time}sec ago <br> Last ads sent {ads_time}sec ago'

def keep_alive():
    while 1:
        time.sleep(5 * 60) # Every 5 mins
        print('[+] Keep Alive', flush=True)
        try: get('https://avaitor-bot.onrender.com')
        except: print(traceback.format_exc(), flush=True)


if __name__ == '__main__':
    Thread(target=lambda: app.run('0.0.0.0')).start()
    Thread(target=keep_alive).start()
    import bot, bot2, ads
    async def run_bots():
        for task in asyncio.as_completed([bot.bot_main(), bot2.bot_main(), ads.ads_main()]):
            await task
    asyncio.run(run_bots())
    


