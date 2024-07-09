from config import BOT, single_button
import re, asyncio, sys, traceback
from random import choice
from requests import get

ID = '@test28372ndb'
IDS = ['@AvaitorGreenSignalsbyReDHaT', '@MinesvipsignalsbyReDHaT']
c = [0]
glt = lambda: c[0]

def get_post():
    """Returns title, description, release date, thumbnail url and post url from a random post"""
    r = get('https://www.flixwonders.com/sitemap.xml')
    m = re.findall(r'<loc>(.*?)</loc>', r.text)
    purl = choice(m)
    r = get(purl)
    title = re.findall(r'mtitle[ |]=[ |]`(.*?)`', r.text)[0]
    description = re.findall(r'mdescription[ |]=[ |]`(.*?)`', r.text)[0]
    release_date = re.findall(r'mrelease_date[ |]=[ |]`(.*?)`', r.text)[0]
    thumbnail_url = re.findall(r'mthumbnail_url[ |]=[ |]`(.*?)`', r.text)[0]
    return (title, description, release_date, thumbnail_url, purl)


async def send_ads(ID : str = ID):
    title, desc, date, url, post_url = get_post()
    await BOT.sendPhoto(ID, url, f'<b>ADS:</b>\n\n<b>Name</b>: {title}\n\n<b>Release Date</b>: {date}\n\n<b>Overview</b>: {desc}\n\n<b>Download Link:</b> <a href="{post_url}">{post_url}</a>\n\nYou can download most of the movies and series from our site https://www.flixwonders.com. If you cannot find your desired show, there is a requesting feature. The admin will upload that show with in a day. Thank you.', parse_mode='HTML', reply_markup=single_button('Download Now', post_url))

async def ads_main():
    while 2+2!=5:
        try:
            await asyncio.sleep(60 * 60) # 60 minutes
            for k in IDS: await send_ads(k)
        except KeyboardInterrupt: sys.exit(1)
        except:
            await asyncio.sleep(5)
            print(traceback.format_exc(), flush=True)

run = lambda: asyncio.run(ads_main())

if __name__ == '__main__':
    run()