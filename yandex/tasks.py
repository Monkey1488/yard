import datetime
from .models import Point
from yard.celery import app
from .botY import *
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
    for process in Point.objects.all():
        if process.activate:
            start_bot.delay(delay, process.url, process.keywords, process.mode_keywords, process.title, process.start_time, process.end_time, process.total_number, process.pf1, process.pf2, process.pf3, process.pf4, process.pf5, process.pf6, process.pf7, process.pf8, process.pf9, process.pf10, process.pf11)
            delay+=60

@app.task
def start_bot(delay, url, keyword, mode_keywords, name, start, end, total_number, vpf1, vpf2, vpf3, vpf4, vpf5, vpf6, vpf7, vpf8, vpf9, vpf10,  vpf11):
    
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

    pf1 = round(total_number/100*vpf1)
    pf2 = round(total_number/100*vpf2)
    pf3 = round(total_number/100*vpf3)
    pf4 = round(total_number/100*vpf4)
    pf5 = round(total_number/100*vpf5)
    pf6 = round(total_number/100*vpf6)
    pf7 = round(total_number/100*vpf7)
    pf8 = vpf8
    pf9 = vpf9
    pf10 = vpf10
    pf11 = vpf11

    append_pf(pf1, final_list)
    append_pf(pf2, final_list)
    append_pf(pf3, final_list)
    append_pf(pf4, final_list)
    append_pf(pf5, final_list)
    append_pf(pf6, final_list)
    append_pf(pf7, final_list)
    append_pf(pf8, final_list)

    random.shuffle(final_list)
    for i in final_list:
        if pf9>0 and i[8]==0:
            i.append(1)
            pf9-=1
        else:
            i.append(0)

    random.shuffle(final_list)
    for i in final_list:
        if pf10>0 and i[9]==0 and i[8]==0:
            i.append(1)
            pf10-=1
        else:
            i.append(0)
            
    random.shuffle(final_list)
    for i in final_list:
        if pf11>0 and i[10]==0 and i[9]==0 and i[8]==0:
            i.append(1)
            pf11-=1
        else:
            i.append(0)
    random.shuffle(final_list)

    print(final_list)

    sleep(delay_to_start.seconds)
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
            bot = BotMobile()
            print(theme)
            action =  ActionChains(driver)
            bot.bot_start(action, driver, url, theme[0], name)
            if theme[1]:
                bot.act_menu(action, driver)
                bot.back_overview(action, driver)
            if theme[2]:
                bot.act_goods_and_services(action, driver)
                bot.back_overview(action, driver)
            if theme[3]:
                bot.act_news(action, driver)
                bot.back_overview(action, driver)
            if theme[4]:
                bot.act_photo(action, driver)
                bot.back_overview(action, driver)
            if theme[5]:
                bot.act_comment(action, driver)
                bot.back_overview(action, driver)
            if theme[6]:
                bot.act_watch_history(action, driver)
            if theme[7]:
                bot.act_watch_schedule(action, driver)
            if theme[8]:
                bot.act_going_to_website(action, driver)
            if theme[9]:
                bot.act_build_route(action, driver)
            if theme[10]:
                bot.act_phone(action, driver)
            if theme[11]:
                bot.act_watch_input(action, driver)
                
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
    




def append_pf(pf, list):
    random.shuffle(list)
    pf = pf
    for i in list:
        if pf <= 0:
            i.append(0)
        else:
            i.append(1)
            pf-=1
