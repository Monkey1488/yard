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
from pyvirtualdisplay import Display 

# # options = webdriver.ChromeOptions()
# # options.add_argument("accept=*/*")
# # options.add_argument(
# #     "user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.132 YaBrowser/22.3.1.892 Yowser/2.5 Safari/537.36")
# # options.add_argument("--disable-blink-features=AutomationControlled")# отключаем режим webdriver
# # # options.add_argument("--log-level=3") #отключает вывод webdriver selenium



# class BotPC():
#     def bot_start(self, driver, url, theme, name):
#         try:
#             driver.get(url=url)
#             time.sleep(random.uniform(2.01, 3.15))
            
#             #если появился запрос на cookie
#             try:
#                 wait = WebDriverWait(driver, 20).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "close-button _color_black _circle _offset_small")))
#                 click = driver.find_element(
#                 By.CLASS_NAME, "close-button _color_black _circle _offset_small").click()
#             except:
#                 pass

#             input_wait = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//span/input")))
#             input = driver.find_element(By.XPATH, "//span/input")
#             input.clear()
#             input.send_keys(theme)
#             time.sleep(1.13)
#             input.send_keys(Keys.ENTER)

#             # начало скроллинга
#             scroll_wait = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CLASS_NAME, "search-snippet-view")))
#             while driver.find_element(by=By.TAG_NAME, value='div'):
#                 try:
#                     scroll = driver.find_elements(
#                         by=By.CLASS_NAME, value="search-snippet-view")
#                     scroll[-1].location_once_scrolled_into_view
#                     time.sleep(0.5)
                    
#                     try:
#                         #кликаем на страницу точки
#                         time.sleep(1.63)
#                         publics = driver.find_elements(by=By.CLASS_NAME, value="search-snippet-view")
#                         for i in publics:
#                             if i.find_element(by=By.CLASS_NAME, value="search-business-snippet-view__title").text == name:
#                                 ActionChains(driver).move_to_element(i).click(i).perform()
#                                 break
#                     except:
#                         pass
#                     try:
#                         c = driver.find_element_by_class_name(
#                             "add-business-view").click()
#                         print("Точка не найдена")
#                         break
#                     except:
#                         pass  
#                 except:
#                     driver.implicitly_wait(1)
#                     continue
#             # конец скроллинга
#             time.sleep(10)

#         except Exception as ex:
#             print(ex)

class BotSimple():
    def bot_start(self, driver, url, theme, name):
        theme = theme.replace(" ", "%20")
        url = url + f"&text={theme}"
        driver.get(url=url)
        time.sleep(random.uniform(5.01, 10.15))

class BotMobile:
    def bot_start(self, driver, url, theme, name):
        print("СТАРТ")
        for _ in range(3):
            success = 0
            try:
                driver.get(url=url)
                action =  ActionChains(driver)
                print("СТАРТ")
                time.sleep(random.uniform(1.01, 2.15))
                try:
                    # закрываем окно с предложением установить Яндекс.Карты на смартфон
                    start_display_close_wait = WebDriverWait(driver, 16).until(
                        EC.presence_of_element_located((By.XPATH, "//div[2]/div[4]/div/div[3]/button")))
                    start_display_close = driver.find_element(
                        by=By.XPATH, value="//div[2]/div[4]/div/div[3]/button")
                    action.move_to_element(
                        start_display_close).click(start_display_close).perform()
                except Exception as ex:
                    print("ошибка с закрытием первого окна")
                time.sleep(random.uniform(1.01, 2.15))
                try:
                    wait = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.TAG_NAME, "input")))
                    input = driver.find_element(
                        by=By.TAG_NAME, value="input")
                    input.send_keys(theme)
                    input.send_keys(Keys.ENTER)
                except:
                    print("ошибки при вводе")
                time.sleep(random.uniform(2.01, 3.15))

                wait = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, "//div[text()='Результаты поиска']")))
                click_to_scroll_list = driver.find_element(
                    by=By.XPATH, value="//div[text()='Результаты поиска']")
                action.move_to_element(click_to_scroll_list).click(click_to_scroll_list).perform() 
                # начало скроллинга
                last_div = 0
                while True:
                    a = 0
                    time.sleep(random.uniform(1.01, 2.15))
                    publics = driver.find_elements(
                        by=By.CLASS_NAME, value="search-snippet-view")    
                    for i in publics:
                
                        wait = WebDriverWait(driver, 30).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "search-business-snippet-view__title")))

                        if i.find_element(by=By.CLASS_NAME, value="search-business-snippet-view__title").text == name:
                            action.move_to_element(i).click(i).perform()
                            print(f"УСПЕХ - СТАРТ {theme}")
                            a = 1
                            success = 1
                            break
                    if a:
                        break
                    try:
                        wait = WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "search-snippet-view")))
                        a = driver.find_elements(by=By.CLASS_NAME, value="search-snippet-view")
                        last_div = a[-1]
                        for _ in range(10):
                            a = driver.find_elements(by=By.CLASS_NAME, value="search-snippet-view")
                            a[-1].location_once_scrolled_into_view
                            time.sleep(0.5)
                    except: 
                        print("ошибка при скролле")
                    
                    if a[-1] == last_div:
                        print(f"Точка не найдена, {theme}")
                        break
                # конец скроллинга
                if success:
                    print("КОНЕЦ - СТАРТ")
                    break

            except:
                print(f"ОШИБКА - СТАРТ, {theme} {url}")
            
        
        time.sleep(random.uniform(8.01, 16.15))

    def act_photo(self, driver):
        pf = driver.find_element(by=By.XPATH, value=f"//div[text()='Фото']")
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

    def act_watch_history(self, driver):
        pass
        # action =  ActionChains(driver)
        # wait = WebDriverWait(driver, 60).until(
        #     EC.presence_of_element_located((By.CLASS_NAME, "story-preview")))
        # pf = driver.find_elements(by=By.CLASS_NAME, value="story-preview")[1]
        # action.move_to_element(pf).click(pf).perform()
        # time.sleep(random.uniform(2.50, 5.99))
        # # wait = WebDriverWait(driver, 30).until(
        # #     EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[15]/div/div/div/div[3]/div/div/div/div/div[4]/div/div[3]/span/svg/path")))
        # # pf = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[2]/div[15]/div/div/div/div[3]/div/div/div/div/div[4]/div/div[3]/span/svg/path")
        # # action.move_to_element(pf).click(pf).perform()
        
        # time.sleep(random.uniform(4.50, 10.99))


    def act_comment(self, driver):
        try:
            wait = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//div[text()='Отзывы']")))
            action =  ActionChains(driver)
            pf = driver.find_element(
                by=By.XPATH, value="//div[text()='Отзывы']")
            action.move_to_element(pf).click(pf).perform()
            time.sleep(5.5)
            wait = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div/div/div[2]/div[5]")))
            pf = driver.find_element(
                by=By.XPATH, value="//div/div/div[2]/div[5]")
            action.move_to_element(pf).click(pf).perform()
            time.sleep(3)
            wait = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/button")))
            pf = driver.find_element(
                by=By.XPATH, value="/html/body/div[1]/button")
            action.move_to_element(pf).click(pf).perform()

            # try:
            #     wait = WebDriverWait(driver, 10).until(
            #             EC.presence_of_element_located((By.XPATH, "//span[text()='Посмотреть комментарии']")))
            # except:
            #     pass
            # try:
            #     wait = WebDriverWait(driver, 10).until(
            #                 EC.presence_of_element_located((By.XPATH, "//span[text()='ответить']")))
            # except:
            #     pass
            # for _ in range(20):
            #     pf = driver.find_element(
            #         by=By.TAG_NAME, value='body').send_keys(Keys.DOWN)
            # time.sleep(1)
            # try:
            #     pf = driver.find_element(
            #         by=By.XPATH, value="//span[text()='ответить']")
            #     action.move_to_element(pf).click(pf).perform()
            #     time.sleep(3)
            #     wait = WebDriverWait(driver, 60).until(
            #         EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/button")))
            #     pf = driver.find_element(
            #         by=By.XPATH, value="/html/body/div[1]/button")
            #     action.move_to_element(pf).click(pf).perform()
            # except:
            #     print("Нет кнопки ОТВЕТИТЬ")
            # try:
            #     pf = driver.find_element(
            #         by=By.XPATH, value="//span[text()='Посмотреть комментарии']")
            #     action.move_to_element(pf).click(pf).perform()
            # except:
            #     print("Нет кнопки Посмотреть комментарии")
            
            print("УСПЕХ - Отзывы")
            
        except Exception as ex:
            print(ex)
            print("ОШИБКА - Отзывы")

    def act_news(self, driver):
        pass
    #     action =  ActionChains(drыiver)
    #     wait = WebDriverWait(driver, 60).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[1][text()='Новости']")))
    #     pf = driver.find_element(
    #         by=By.XPATH, value="//div[1][text()='Новости']")
    #     action.move_to_element(pf).click(pf).perform()
    #     time.sleep(random.uniform(4.50, 8.70))
    
    #     wait = WebDriverWait(driver, 1ы0).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "business-posts-list-post-view__date")))
    #     pf = driver.find_element(
    #         by=By.CLASS_NAME, value="business-posts-list-post-view__date")
    #     action.move_to_element(pf).click(pf).perform()
    #     time.sleep(random.uniform(2.50, 5.70))
        
    #     wait = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "business-post-view__photos")))
    #     pf = driver.find_element(
    #         by=By.CLASS_NAME, value="business-post-view__photos")
    #     action.move_to_element(pf).click(pf).perform()
    #     time.sleep(random.uniform(2.50, 5.70))
        
    #     wait = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[10]/div[1]/div[2]/div/div/span")))
    #     pf = driver.find_element(
    #         by=By.XPATH, value="/html/body/div[1]/div[2]/div[10]/div[1]/div[2]/div/div/span")
    #     action.move_to_element(pf).click(pf).perform()
    #     time.sleep(random.uniform(2.50, 5.70))
    #     print("УСПЕХ - Новости")

    def act_phone(self, driver):
        action =  ActionChains(driver)
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "card-phones-view__phone-number-link")))
        pf = driver.find_element(
            by=By.CLASS_NAME, value="card-phones-view__phone-number-link")
        action.move_to_element(pf).click(pf).perform()
        time.sleep(random.uniform(4.50, 6.70))
        print("УСПЕХ - Звонок")

    def act_watch_input(self, driver):
        pass
        # action =  ActionChains(driver)
        # wait = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[text()='Показать входы']")))
        # pf = driver.find_element(
        #     by=By.XPATH, value="//div[text()='Показать входы']")
        # action.move_to_element(pf).click(pf).perform()
        # time.sleep(random.uniform(2.50, 3.70))
        # # wait = WebDriverWait(driver, 10).until(
        # #     EC.presence_of_element_located((By.CLASS_NAME, "business-card-title-view__bottom-item _working-status")))
        # # pf = driver.find_element(
        # #     by=By.CLASS_NAME, value="business-card-title-view__bottom-item _working-status")
        # # time.sleep(random.uniform(1.50, 3.70))
        # for _ in range(10):
        #     pf = driver.find_element(
        #         by=By.TAG_NAME, value='body').send_keys(Keys.DOWN)
        # time.sleep(random.uniform(4.50, 6.70))
        # print("УСПЕХ - Показать входы")

    def act_watch_schedule(self, driver):
        action =  ActionChains(driver)
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div/div[1]/div[5]/div[4]/div[2]/div/div[1]/div[1]/div[2]")))
        pf = driver.find_element(
            by=By.XPATH, value="//div/div[1]/div[5]/div[4]/div[2]/div/div[1]/div[1]/div[2]")
        action.move_to_element(pf).click(pf).perform()
        time.sleep(random.uniform(3.50, 5.70))
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sidebar-panel-header-view__controls")))
        pf = driver.find_element(by=By.CLASS_NAME, value= "sidebar-panel-header-view__controls")
        action.move_to_element(pf).click(pf).perform()
        time.sleep(random.uniform(2.50, 4.70))
        print("УСПЕХ - Время работы")

    def act_menu(self, driver):
        pass
    
    
    def act_goods_and_services(self, driver):
        try:
            action =  ActionChains(driver)

            wait = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//div[text()='Товары и услуги']")))
            pf = driver.find_element(
                by=By.XPATH, value="//div[text()='Товары и услуги']")
            action.move_to_element(pf).click(pf).perform()
            time.sleep(random.uniform(5.50, 10.70))

            wait = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[8]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[4]/div/div[4]/div/div/div/div/div[1]/div/div[2]/div/button")))
            pf = driver.find_element(
                by=By.XPATH, value="/html/body/div[1]/div[2]/div[8]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[4]/div/div[4]/div/div/div/div/div[1]/div/div[2]/div/button")
            action.move_to_element(pf).click(pf).perform()
            time.sleep(random.uniform(2.50, 4.70))

            wait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[8]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[4]/div/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]")))
            pf = driver.find_element(
                by=By.XPATH, value="/html/body/div[1]/div[2]/div[8]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[4]/div/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]")
            action.move_to_element(pf).click(pf).perform()
            time.sleep(random.uniform(4.50, 6.70))

            # for _ in range(random.randint(18, 25)):
            #     pf = driver.find_element(
            #         by=By.TAG_NAME, value='body').send_keys(Keys.DOWN)
            # time.sleep(1)
            # for _ in range(random.randint(14, 20)):
            #     pf = driver.find_element(
            #         by=By.TAG_NAME, value='body').send_keys(Keys.UP)
            # time.sleep(6)

            wait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[9]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[4]/div/div[4]/div/div/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div/div/div/div[1]/div")))
            pf = driver.find_element(
                by=By.XPATH, value="/html/body/div[1]/div[2]/div[9]/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[4]/div/div[4]/div/div/div/div/div/div/div[3]/div[1]/div[2]/div[1]/div/div/div/div[1]/div")
            action.move_to_element(pf).click(pf).perform()
            time.sleep(random.uniform(4.50, 6.70))
            
            wait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[10]/div[1]/div[2]/div/div/span")))
            pf = driver.find_element(
                by=By.XPATH, value="/html/body/div[1]/div[2]/div[10]/div[1]/div[2]/div/div/span")
            action.move_to_element(pf).click(pf).perform()
            time.sleep(random.uniform(4.50, 6.70))

            print("УСПЕХ - Товары и услуги")
        except Exception as ex:
            print(ex)
            print("ОШИБКА - Товары и услуги")

    def back_overview(self, driver):
        action =  ActionChains(driver)
        pf = driver.find_element(by=By.XPATH, value= "//div[text()='Обзор']")
        action.move_to_element(pf).click(pf).perform()
        time.sleep(2)
        for _ in range(10):
            pf = driver.find_element(
                by=By.TAG_NAME, value='body').send_keys(Keys.UP)
        time.sleep(random.uniform(3.50, 5.99))
        print("УСПЕХ - Обзор")

    def act_going_to_website(self, driver):
        action =  ActionChains(driver)
        pf = driver.find_element(
            by=By.CLASS_NAME, value= "business-urls-view__text")
        ActionChains(driver).move_to_element(pf).click(pf).perform()
        time.sleep(random.uniform(4.50, 7.99))
        driver.back()
        time.sleep(random.uniform(3.50, 8.99))
        print("УСПЕХ - Переход на сайт")
    
    def act_build_route(self, driver):
        action =  ActionChains(driver)
        
        wait = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button__text")))
        pfs = driver.find_elements(by=By.CLASS_NAME, value="button__text")
        for i in pfs:
            if i.text == 'Маршрут':
                action.move_to_element(i).click(i).perform()
        # action.move_to_element(pf).click(pf).perform()

        time.sleep(random.uniform(1.50, 3.90))
        try:
            wait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "route-field-view__wrapper")))
            pf = driver.find_element(by=By.CLASS_NAME, value="route-field-view__wrapper")
            action.move_to_element(pf).click(pf).perform()
            time.sleep(random.uniform(1.50, 2.90))
            wait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[2]/div/div[2]/div/div/span/span[1]/input")))
            pf = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div[2]/div/div[2]/div/div/span/span[1]/input")
            time.sleep(random.uniform(1.50, 2.90))
            pf.send_keys("ресторан")
            time.sleep(random.uniform(1.50, 2.90))
            pf.send_keys(Keys.ENTER)
            time.sleep(random.uniform(2.50, 3.90))
            pf.send_keys(Keys.DOWN)
            time.sleep(random.uniform(2.50, 3.90))
            pf.send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(random.uniform(3.50, 4.99))
        wait = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button__text")))
        pfs = driver.find_elements(by=By.CLASS_NAME, value="button__text")
        for i in pfs:
            if i.text == 'Поехали':
                action.move_to_element(i).click(i).perform()
        time.sleep(random.uniform(2.50, 3.90))
        wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "collapsed-route-panel-form-view__distribution-close")))
        pf = driver.find_element(by=By.CLASS_NAME, value="collapsed-route-panel-form-view__distribution-close")        
        action.move_to_element(pf).click(pf).perform()
        print("УСПЕХ - Маршрут")
        time.sleep(random.uniform(2.50, 3.90))

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent= Mozilla/5.0 (Linux; arm_64; Android 12; CPH2159) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 YaBrowser/20.9.0.203.00 SA/3 Mobile Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")# отключаем режим webdriver
    options.add_argument("--log-level=3") #отключает вывод webdriver selenium
    options.add_argument('--no-sandbox')
    # options.add_argument("--headless")

    theme_list = ["Бар", "eда", "где поесть"]
    url = "https://yandex.ru/maps/213/moscow/?indoorLevel=1&ll=37.641621%2C55.734747&z=14.01"
    name = "Beersach.bar" 

    display = Display(visible = 1, size=(1536, 1024)) 
    display.start()

    for theme in theme_list:
        mob = BotMobile()
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
        seleniumwire_options=proxy_options
        )    
        mob.bot_start(driver, url, theme, name)
        # mob.act_watch_schedule(driver)
        # mob.act_phone(driver)
        # mob.act_watch_input(driver)
        # mob.act_watch_schedule(driver)
        # mob.act_goods_and_services(driver)
        # mob.back_overview(driver)
        # mob.act_comment(driver)
        # mob.back_overview(driver)
        # mob.act_build_route(driver)
        # mob.act_going_to_website(driver)
        time.sleep(1)
        # mob.photo_action(driver)
        
        
        # driver.quit()
    display.stop()