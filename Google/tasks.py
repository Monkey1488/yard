import datetime
from .models import GPoint
from yard.celery import app
from .botG import *
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep, perf_counter
from seleniumwire import webdriver
import random
from math import ceil
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"


@app.task
def start():
    delay = 1
    for process in GPoint.objects.all():
        if process.activate:
            start_bot.delay(delay, process.url, process.keywords, process.mode_keywords, process.title, process.start_time, process.end_time, process.total_number)
            delay+=60

@app.task
def start_bot(delay, url, keyword, mode_keywords, name, start, end, total_number):
    
    if mode_keywords:
        base = keyword.split("\n")
        list_theme = ''
        for i in base:
            i = i[i.find(".") + 1:]
            c = i.split("-")
            list_theme+=(c[0]+'|')*(int(c[1]))
        list_theme = list_theme.split("|")
        list_theme.remove("")
        random.shuffle(list_theme)
    else:
        base = keyword.split("\n")
        list_theme = ''
        for i in base:
            i = i[i.find(".") + 1:]
            c = i.split("-")
            list_theme+=(c[0]+'|')*ceil(int(c[1])*(total_number / 100))
        list_theme = list_theme.split("|")
        list_theme.remove("")
        random.shuffle(list_theme)

    final_list = []
    for theme in list_theme:
        final_list.append([theme])
    
    start = start.split(":")
    start = datetime.datetime(2022, 1, 1, hour=int(start[0]), minute=int(start[1]), second=int(start[2]))
    end = end.split(":")
    end = datetime.datetime(2022, 1, 1, hour=int(end[0]), minute=int(end[1]), second=int(end[2]))
    delta = end - start
    interval = delta.seconds / len(list_theme)
    delay_to_start = start - datetime.datetime.now() 
    

    sleep(delay_to_start.seconds)
    print(f"START - {name}")
    sleep(delay)
    for theme in final_list:
        try:
            display = Display(visible = 0, size=(1536, 1024)) 
            display.start()
            options = webdriver.ChromeOptions()
            options.add_argument(
                "user-agent= Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36")
            options.add_argument('--no-sandbox')
            # options.add_argument("--headless")
            options.add_argument("--disable-blink-features=AutomationControlled")
            proxy_list = ["https://4bgc8fuw:1yppm77g@marina.onlinesim.ru:14714", "https://iparchitect_12166_02_06_22:d5RafhEEhb28GeEk37@188.143.169.28:30147"]
            proxy_options = {"proxy": {"https": "https://4bgc8fuw:1yppm77g@marina.onlinesim.ru:14714" }}
            
            starti = perf_counter()

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options, seleniumwire_options=proxy_options, desired_capabilities=capa)
            bot = GBotSimple()
            print(theme)
            action =  ActionChains(driver)
            bot.bot_start(action, driver, url, theme[0])

            try:
                driver.quit()
            except:
                pass
            display.stop()
            print("Конец")
            endi = perf_counter()
            interval_delta = round(endi) - round(starti)
            if interval > interval_delta:
                sleep(interval-interval_delta)
            elif interval > (interval_delta//2):
                sleep(interval-(interval_delta//2))
            else:
                sleep(interval)
        except Exception as ex:
            print(ex)
    


def change_pf(vpf, total_number):
    if "%" in vpf:
        vpf = int(vpf.replace("%", ""))
        pf = round(total_number/100*vpf)
        return pf
    else:
        pf = int(vpf)
        return pf


def append_pf(pf, list):
    random.shuffle(list)
    pf = pf
    for i in list:
        if pf <= 0:
            i.append(0)
        else:
            i.append(1)
            pf-=1
