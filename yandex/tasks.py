import datetime
from .models import Point
from yard.celery import app
from celery import shared_task
from .botY import *
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from seleniumwire import webdriver
import random


@app.task
def start():
    for process in Point.objects.all():
        if process.activate:
            start_bot.delay(process.url, process.keywords, process.title, process.start_time, process.end_time)

@app.task
def start_bot(url, keyword, name, start, end):
    b = keyword.split("\n")
    list_theme = ''
    for i in b:
        c = i.split("-")
        list_theme+=(c[0]+'|')*int(c[1])
    list_theme = list_theme.split("|")
    random.shuffle(list_theme)
    list_theme.remove("")
    # print(list_theme)

    # print(start)
    start = start.split(":")
    start = datetime.datetime(2022, 1, 1, hour=int(start[0]), minute=int(start[1]), second=int(start[2]))
    # print(start, type(start))
    end = end.split(":")
    end = datetime.datetime(2022, 1, 1, hour=int(end[0]), minute=int(end[1]), second=int(end[2]))
    # print(end, type(end))
    delta = end - start
    # print('Difference: ', delta.seconds)
    interval = delta.seconds / len(list_theme)
    print("количество",  len(list_theme))
    print("интервал", interval)
    delay_to_start = start - datetime.datetime.now() 
    print( "задержка", delay_to_start.seconds)
    # sleep(delay_to_start.seconds)
    for theme in list_theme:
        options = webdriver.ChromeOptions()
        options.add_argument(
            "user-agent= Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36")
        options.add_argument('--no-sandbox')
        options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        bot = BotMobile()
        proxy_options = {
            "proxy": {
                "https": "https://iparchitect_12166_02_06_22:d5RafhEEhb28GeEk37@188.143.169.28:30147"
            }
        }
        

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, seleniumwire_options=proxy_options)
        bot.bot_start(driver, url, theme, name)
        
        sleep(interval)

