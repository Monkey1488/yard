import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


# # options = webdriver.ChromeOptions()
# # options.add_argument("accept=*/*")
# # options.add_argument(
# #     "user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.132 YaBrowser/22.3.1.892 Yowser/2.5 Safari/537.36")
# # options.add_argument("--disable-blink-features=AutomationControlled")# отключаем режим webdriver
# # # options.add_argument("--log-level=3") #отключает вывод webdriver selenium

class BotMobile:
    def bot_start(self, driver, url, theme, name):
        try:
            driver.get(url=url)
            time.sleep(random.uniform(1.01, 2.15))
            try:
                # закрываем окно с предложением установить Яндекс.Карты на смартфон
                start_display_close_wait = WebDriverWait(driver, 50).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[4]/div/div[3]/button")))
                start_display_close = driver.find_element(
                    by=By.XPATH, value="/html/body/div[1]/div[2]/div[4]/div/div[3]/button").click()
                ActionChains(driver).move_to_element(
                    start_display_close).click(start_display_close).perform()
            except:
                pass
            time.sleep(random.uniform(1.01, 2.15))
            input = driver.find_element(
                by=By.XPATH, value="//form/div[2]/div/span/span/input")
            input.send_keys(theme)
            input.send_keys(Keys.ENTER)
            time.sleep(random.uniform(2.01, 3.15))
            click_to_scroll_list = driver.find_element(
                by=By.XPATH, value="/html/body/div[1]/div[2]/div[7]/div/div[1]/div[1]/div[2]/div[1]")
            ActionChains(driver).move_to_element(
                click_to_scroll_list).click(click_to_scroll_list).perform() 
            # начало скроллинга
            last_div = 0
            while True:
                try:
                    a = driver.find_elements(by=By.CLASS_NAME, value="search-snippet-view")
                    last_div = a[-1]
                    for _ in range(10):
                        a = driver.find_elements(by=By.CLASS_NAME, value="search-snippet-view")
                        a[-1].location_once_scrolled_into_view
                        time.sleep(0.5)
                except: 
                    break
                time.sleep(random.uniform(1.01, 2.15))
                publics = driver.find_elements(
                    by=By.CLASS_NAME, value="search-snippet-view")    
                for i in publics:
                    if i.find_element(by=By.CLASS_NAME, value="search-business-snippet-view__title").text == name:
                        ActionChains(driver).move_to_element(i).click(i).perform()
                        break

                if a[-1] == last_div:
                    print("Точка не найдена")
                    driver.quit()
                    break
            # конец скроллинга
        
        except Exception as ex:
            # driver.quit()
            print(ex)
        print("КОНЕЦ")
        time.sleep(random.uniform(3.01, 6.15))

    def photo_action(self, driver):
        pf = driver.find_element(by=By.XPATH, value=f"//div[1][text()='Фото']")
        ActionChains(driver).move_to_element(pf).click(pf).perform()
        time.sleep(random.uniform(2.50, 7.99))
        # time.sleep(100)
        for _ in range(random.randrange(4,10)):
            pf = driver.find_element(
                by=By.TAG_NAME, value='body').send_keys(Keys.DOWN)
        time.sleep(random.uniform(2.50, 4.99))
        for _ in range((random.randrange(3,6))):
            pf = driver.find_element(
                by=By.TAG_NAME, value='body').send_keys(Keys.UP)
        time.sleep(random.uniform(2.50, 4.99))
        try:
            pf = driver.find_element(
                by=By.XPATH, value="/html/body/div[1]/div[2]/div[8]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[4]/div/div[6]/div/div/div[4]/div/div/div/div/div/div/button")
            ActionChains(driver).move_to_element(pf).click(pf).perform()
            time.sleep(3)
            pf = driver.find_element(
                by=By.XPATH, value="/html/body/div[1]/button")
            ActionChains(driver).move_to_element(pf).click(pf).perform()
        except Exception as ex:
            print(ex)
        time.sleep(random.uniform(2.50, 7.99))
        
        # pf = driver.find_elements(
        #     by=By.CLASS_NAME, value="photo-list__frame-wrapper")[0]
        # ActionChains(driver).move_to_element(pf).click(pf).perform()
        # time.sleep(3)
        # pf = driver.find_element(by=By.TAG_NAME, value="body")
        # pf.send_keys(Keys.RIGHT)
        # time.sleep(2)
        # pf.send_keys(Keys.RIGHT)
        # time.sleep(3)
        # pf.send_keys(Keys.LEFT)
        # time.sleep(4)
        # pf.send_keys(Keys.RIGHT)
        # time.sleep(3)
        # pf = driver.find_elements(
        #     by=By.XPATH, value="/html/body/div[1]/div[2]/div[10]/div[1]/div[2]/div/div/span/svg/path")
        # ActionChains(driver).move_to_element(pf).click(pf).perform()
        # time.sleep(14)

    def comment_action(self, driver):
        pf = driver.find_element(
            by=By.XPATH, value="//div[1][text()='Отзывы']")
        ActionChains(driver).move_to_element(pf).click(pf).perform()
        time.sleep(2.5)
        for _ in range(8):
            pf = driver.find_element(
                by=By.TAG_NAME, value='body').send_keys(Keys.DOWN)
        time.sleep(1)
        for _ in range(7):
            pf = driver.find_element(
                by=By.TAG_NAME, value='body').send_keys(Keys.UP)
        time.sleep(6)
        try:
            pf = driver.find_element(
                by=By.XPATH, value="//div/span[text()='ответить']")
            ActionChains(driver).move_to_element(pf).click(pf).perform()
            time.sleep(3)
            pf = driver.find_element(
                by=By.XPATH, value="/html/body/div[1]/button")
            ActionChains(driver).move_to_element(pf).click(pf).perform()
        except Exception as ex:
            print(ex)

    
        # time.sleep(7)
        # pf = driver.find_element(
        #     by=By.XPATH, value="//div[1][text()='Посмотреть все товары и услуги']")
        # ActionChains(driver).move_to_element(pf).click(pf).perform()
        # time.sleep(2)
        # for _ in range(24):
        #     pf = driver.find_element(
        #         by=By.TAG_NAME, value='body').send_keys(Keys.DOWN)
        # time.sleep(1)
        # for _ in range(15):
        #     pf = driver.find_element(
        #         by=By.TAG_NAME, value='body').send_keys(Keys.UP)
        # time.sleep(6)
    def overview_action(self, driver):
        pf = driver.find_element(by=By.XPATH, value= "//div[text()='Обзор']")
        ActionChains(driver).move_to_element(pf).click(pf).perform()
        time.sleep(4)
        for _ in range(8):
            pf = driver.find_element(
                by=By.TAG_NAME, value='body').send_keys(Keys.DOWN)
        time.sleep(random.uniform(7.50, 16.99))

    def going_to_website(self, driver):
        pf = driver.find_element(
            by=By.XPATH, value= "//span[text()='www.symphonyflowers.ru']")
        ActionChains(driver).move_to_element(pf).click(pf).perform()
        time.sleep(random.uniform(4.50, 7.99))
        driver.back()
        time.sleep(random.uniform(3.50, 8.99))
    


class BotPC():
    def bot_start(self, driver, url, theme, name):
        try:
            driver.get(url=url)
            time.sleep(random.uniform(1.01, 3.15))
            
            #если появился запрос на cookie
            try:
                wait = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div")))
                click = driver.find_element(
                By.XPATH, "/html/body/div[3]/div/div[1]/table/tbody/tr/td[2]/table/tbody/tr/td[2]/button").click()
            except:
                pass

            input_wait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span/input")))
            input = driver.find_element(By.XPATH, "//span/input")
            input.clear()
            input.send_keys(theme)
            time.sleep(1.13)
            input.send_keys(Keys.ENTER)

            # начало скроллинга
            scroll_wait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-snippet-view")))
            while driver.find_element(by=By.TAG_NAME, value='div'):
                try:
                    scroll = driver.find_elements(
                        by=By.CLASS_NAME, value="search-snippet-view")
                    scroll[-1].location_once_scrolled_into_view
                    time.sleep(0.5)
                    
                    try:
                        #кликаем на страницу точки
                        time.sleep(1.63)
                        publics = driver.find_elements(by=By.CLASS_NAME, value="search-snippet-view")
                        for i in publics:
                            if i.find_element(by=By.CLASS_NAME, value="search-business-snippet-view__title").text == name:
                                ActionChains(driver).move_to_element(i).click(i).perform()
                                break
                    except:
                        pass
                    try:
                        c = driver.find_element_by_class_name(
                            "add-business-view").click()
                        print("Точка не найдена")
                        break
                    except:
                        pass  
                except:
                    driver.implicitly_wait(1)
                    continue
            # конец скроллинга
            time.sleep(10)

        except Exception as ex:
            print(ex)













if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent= Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")# отключаем режим webdriver
    options.add_argument("--log-level=3") #отключает вывод webdriver selenium


    theme_list = ["Цветы", ]
    url = "https://yandex.ru/maps/213/moscow/?ll=37.497251%2C55.837208&z=15"
    name = "Симфония цветов" 

    for theme in theme_list:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        mob = BotMobile()
        mob.bot_start(driver, url, theme, name)
        mob.photo_action(driver)
        mob.comment_action(driver)
        mob.overview_action(driver)
        mob.going_to_website(driver)
        driver.quit()