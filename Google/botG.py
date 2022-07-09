import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from seleniumwire import webdriver
# from pyvirtualdisplay import Display 


# class BotMobile:
#     def bot_start(self, driver, url, theme, name):
#         print("СТАРТ")
        # try:
        #     driver.get(url=url)
        #     action = ActionChains(driver)
        #     print("СТАРТ")
        #     time.sleep(random.uniform(1.01, 2.15))
        #     try:
        #         wait = WebDriverWait(driver, 30).until(
        #                     EC.presence_of_element_located((By.XPATH, "//span[text()='Используйте веб-версию']")))
        #         act = driver.find_element(
        #             by=By.XPATH, value="//span[text()='Используйте веб-версию']")
        #         action.move_to_element(act).click(act).perform() 

        #     except Exception as ex:
        #         print(ex)
            
        #     wait = WebDriverWait(driver, 30).until(
        #                     EC.presence_of_element_located((By.XPATH, "//div[text()='Найдите место']")))
        #     act = driver.find_element(
        #         by=By.XPATH, value="//div[text()='Найдите место']")
        #     action.move_to_element(act).click(act).perform() 

        #     time.sleep(random.uniform(2.01, 3.15))

        #     wait = WebDriverWait(driver, 30).until(
        #                     EC.presence_of_element_located((By.TAG_NAME, "input")))
        #     act = driver.find_element(
        #         by=By.TAG_NAME, value="input")
        #     act.send_keys(theme)
        #     act.send_keys(Keys.ENTER)

            # try:
            #     wait = WebDriverWait(driver, 10).until(
            #                     EC.presence_of_element_located((By.XPATH, "//span[text()='Посмотреть список']")))
            #     act = driver.find_element(
            #         by=By.XPATH, value="//span[text()='Посмотреть список']")
            #     action.move_to_element(act).click(act).perform() 
            # except:
            #     pass  
            
            # try:
            #     wait = WebDriverWait(driver, 5).until(
            #         EC.presence_of_element_located((By.CLASS_NAME, "Nv2PK THOPZb")))
            #     a = driver.find_elements(by=By.CLASS_NAME, value="Nv2PK THOPZb")
            #     last_div = a[-1]
            #     for _ in range(10):
            #         a = driver.find_elements(by=By.CLASS_NAME, value="Nv2PK THOPZb")
            #         a[-1].location_once_scrolled_into_view
            #         time.sleep(0.5)
            # except: 
            #     print("ошибка при скролле")
            
            # time.sleep(5)

            # wait = WebDriverWait(driver, 30).until(
            #                 EC.presence_of_element_located((By.CLASS_NAME, "y7PRA")))
            # for _ in range(2):
            #     act = driver.find_elements(
            #         by=By.CLASS_NAME, value="y7PRA")[-1]
            #     action.move_to_element(act).perform() 
            #     action.move_by_offset(50, 50).perform()
            #     pf = driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.DOWN)
            #     time.sleep(1)

            # for _ in range(10):
            #     pf = driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.DOWN)
            #     time.sleep(0.5)


            # SCROLL_PAUSE_TIME = 0.5

            # # Get scroll height
            # last_height = driver.execute_script("return document.body.scrollHeight")

            # while True:
            #     # Scroll down to bottom
            #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            #     # Wait to load page
            #     time.sleep(SCROLL_PAUSE_TIME)

            #     # Calculate new scroll height and compare with last scroll height
            #     new_height = driver.execute_script("return document.body.scrollHeight")
            #     if new_height == last_height:
            #         break
            #     last_height = new_height

            # time.sleep(1)
            # wait = WebDriverWait(driver, 30).until(
            #                 EC.presence_of_element_located((By.XPATH, "//span[text()='beersach.bar']")))
            # act = driver.find_element(
            #     by=By.XPATH, value="//span[text()='beersach.bar']")
            # action.move_to_element(act).click(act).perform() 
            # print("успех")
            # OFFONBIZ digital agency
        # except Exception as ex:
        #     print(ex)

class GBotSimple:
    def bot_start(self, driver, url, theme):
        try:
            url = url.replace("KEY_NAME", theme)
            driver.get(url=url)
            time.sleep(random.uniform(16.01, 26.15))
            print("УСПЕХ - СТАРТ")
        except:
            print("ОШИБКА - СТАРТ")













if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent= Mozilla/5.0 (Linux; arm_64; Android 12; CPH2159) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 YaBrowser/20.9.0.203.00 SA/3 Mobile Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")# отключаем режим webdriver
    options.add_argument("--log-level=3") #отключает вывод webdriver selenium
    options.add_argument('--no-sandbox')
    # options.add_argument("--headless")

    theme_list = ["Бар", "bar", "еда"]
    url = "https://www.google.ru/maps/place/beersach.bar/@55.728898,37.6425166,17z/data=!4m9!1m2!2m1!1sKEY_NAME!3m5!1s0x46b54b8c97a89e2f:0x581c4069f32105f4!8m2!3d55.728886!4d37.646894!15sCgNiYXJaBSIDYmFykgEDYmFymgEjQ2haRFNVaE5NRzluUzBWSlEwRm5TVU54Ym1WNVRFcDNFQUU"
    name = "Beersach.bar"

    # display = Display(visible = 1, size=(768, 1024)) 
    # display.start()

    for theme in theme_list:
        
        # proxy_list = ["https://4bgc8fuw:1yppm77g@marina.onlinesim.ru:14714", "https://iparchitect_12166_02_06_22:d5RafhEEhb28GeEk37@188.143.169.28:30147"]
        proxy_options = {
            "proxy": {
                "https": "https://4bgc8fuw:1yppm77g@marina.onlinesim.ru:14714"
            }
        }
#https://4bgc8fuw:1yppm77g@marina.onlinesim.ru:14714
#https://iparchitect_12166_02_06_22:d5RafhEEhb28GeEk37@188.143.169.28:30147

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options, 
        # seleniumwire_options=proxy_options
        )    
        mob = GBotSimple()
        mob.bot_start(driver, url, theme, name)
        # time.sleep(1000)