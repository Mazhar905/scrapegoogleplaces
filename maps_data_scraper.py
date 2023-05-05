# -*- coding: utf-8 -*-
import mylogger
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

logger = mylogger.MyLogger().get_logger()


class GoogleMapsDataScraper:

    def __init__(self):
        self.driver = None
        self.errorCont = 0
        # define an explicit wait with a timeout of 10 seconds
        self.wait = WebDriverWait(self.driver, 10)
        self.log = logger

    def initDriver(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--log-level=3')
            # s = Service(ChromeDriverManager().install())
            # self.driver = webdriver.Chrome(service=s, options=chrome_options)
            self.driver = webdriver.Chrome(
                executable_path=CM().install(), options=chrome_options)
            self.driver.get('https://www.google.com/maps/')
            self.log.info("Driver initialized successfully.")
            return True
        except Exception as e:
            self.log.exception("Exception occurred", exc_info=True)
            # print(e)
            return False

    def fetch_data(self, name):
        time.sleep(5)
        xpaths = {"Category": ["//div[@class= 'fontBodyMedium']/span/span/button","//div[@class= 'fontBodyMedium dmRWX']/span/span/span/span[2]/span/span"],
                  "Title": "//h1",
                  "Rating": "//div[@class = 'fontDisplayLarge']",
                  "Description": "//button/div[2][@class ='WeS02d fontBodyMedium']/div/div[1]",
                  "Address": "//button[@data-item-id='address']/div/div[3]/div[1]",
                  "Hours": ["//div[@role='button'][@tabindex = '0']/div/div/span/span/span", "//button[@aria-label='Open 24 hours · See more hours']/div[1]/div[3]/div[1]/span",],
                  "Website": "//a[@data-item-id='authority']/div/div[3]/div[1]",
                  "Phone": "//button[@data-tooltip='Copy phone number']/div/div[3]/div[1]"
                  #   "langitude": "",
                  #   "longitude": ""
                  }

        elements = {}
        for key, xpath in xpaths.items():
                time.sleep(5)
                try:
                    time.sleep(2)
                    # code for getting category value
                    if key == "Category":
                        category_text = None
                        for i in xpath:
                            try:
                                element = self.driver.find_element(By.XPATH, i)
                                category_text = element.text
                                # self.log.info(f"{key} value of {name} found from this xpath and the {key} is {category_text}.")
                                if category_text is not None:
                                    break
                            except NoSuchElementException:
                                self.log.info(f"{key} not found with the current xapth, continue with the next xpath.")
                                continue
                        elements[key] = category_text
                        if category_text is None:
                            self.log.warning(f"{key} element not found for {name}.")

                    # code for getting hours value
                    elif key == "Hours":
                        hours_text = None
                        for j in xpath:
                            try:
                                element = self.driver.find_element(By.XPATH, j)
                                hours_text = element.text

                                if hours_text != "Open 24 hours" and hours_text is not None:
                                    self.driver.find_element(By.XPATH, "//div[@role='button'][@tabindex = '0']/div/div/span/span/span").click()
                                    ele =self.driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[2]/ul/li")
                                    hours_text = ele.text
                                # self.log.info(f"{key} value of {name} found from this xpath and the {key} is {hours_text}.")
                                if hours_text is not None:
                                    break
                            except NoSuchElementException:
                                self.log.info(f"{key} not found with the current xpath, continue with the next xpath.")
                                continue
                        elements[key] = hours_text
                        if hours_text is None:
                            self.log.warning(f"{key} element not found for {name}.")
                    else:
                        try:
                            element = self.driver.find_element(By.XPATH, xpath)
                            elements[key] = element.text
                        except NoSuchElementException:
                            elements[key] = None
                            self.log.warning(f"{key} value not found for {name}.")
                            continue
                            #logger.exception("Exception occurred")
                except Exception as e:
                    self.log.warning(f"{key} value not found for {name}.")
                    continue
                    #logger.exception("Exception occurred")

        return elements


    def scraperData(self, kw):
        try:
            self.log.info(f"Starting scraper for keyword: {kw}")
            time.sleep(3)
            inputBox = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="searchboxinput"]')))
            inputBox.click()
            inputBox.clear()
            time.sleep(1)
            inputBox.send_keys(kw)
            inputBox.send_keys(Keys.ENTER)
            time.sleep(5)
            # Find the div element you want to scroll
            div = self.driver.find_element(
                By.XPATH, "//div[@role= 'feed'][@tabindex = '-1']")
            # Get the initial height of the scrollable element
            last_height = self.driver.execute_script(
                "return arguments[0].scrollHeight;", div)

            # Scroll the element to the bottom until all content has loaded
            while True:
                # Scroll to the bottom of the element
                self.driver.execute_script(
                    "arguments[0].scrollTop = arguments[0].scrollHeight;", div)

                # Wait for the page to load
                time.sleep(2)
                div = self.driver.find_element(
                    By.XPATH, "// div[@role='feed'][@tabindex= '-1']")
                lst = []
                for child_div in div.find_elements(By.XPATH, "//div[@role = 'article']/a"):
                    name = child_div.get_attribute('aria-label')
                    lst.append(name)

                # Get the new height of the element
                new_height = self.driver.execute_script(
                    "return arguments[0].scrollHeight;", div)

                # If the new height is the same as the last height, all content has loaded
                if new_height == last_height or len(lst) >= 10:
                    break

                # Otherwise, update the last height and continue scrolling
                last_height = new_height
                # print(len(lst))

            # Get the HTML content of the entire scrollable element
            time.sleep(5)
            div = self.driver.find_element(
                By.XPATH, "//div[@role= 'feed'][@tabindex = '-1']")
            self.log.info(f'Get {len(lst)} value in list on this {kw}')
            print(lst)
            data = {}
            # Iterate over the child div elements of the parent div
            for child_div in div.find_elements(By.XPATH, "//div[@role = 'article']/a"):
                name = child_div.get_attribute('aria-label')
                # print(data)
                child_div.click()
                data[name] = self.fetch_data(name)

            print(data)
            return data
        except Exception as e:
            self.log.error(
                'Error occurred while scraping for keyword {}: {}'.format(kw, str(e)))
            self.errorCont += 1
            return None

    def endDriver(self):
        self.log.info('Quitting the driver...')
        self.driver.quit()
