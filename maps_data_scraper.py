# -*- coding: utf-8 -*-
from exportData import ExportDataMaps
import requests
from bs4 import BeautifulSoup
import mylogger
import time
import random
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

        # try:
        #     # prox = self.check_proxies()
        #     # prox = '158.69.71.245:9300'
        # except Exception as e:
        #     print(e)
        try:
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            # chrome_options.add_argument(f'--proxy-server={prox}')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--log-level=3')
            self.driver = webdriver.Chrome(
                executable_path=CM().install(), options=chrome_options)
            self.log.info("Driver initialized successfully.")
            return True
        except Exception as e:
            self.log.exception("Exception occurred", exc_info=True)
            # print(e)
            return False
        
    def get(self, url, proxy): 
        VALID_STATUSES = [200, 301, 302, 307, 404] 
        try: 
            response = requests.get(url, proxies={'http': f"http://{proxy}"}, timeout=10) 
            if response.status_code in VALID_STATUSES: # valid proxy 
                print(response.status_code, response.text) 
            
            return True
        except Exception as e: 
            print("Exception: ", type(e)) 
            return False
    def check_proxies(self): 
        proxies_list = open("rotating_proxies_list.txt", "r").read().strip().split("\n")
        while True:
            index = random.randint(0,len(proxies_list))
            proxy = proxies_list[index]

            # proxy = proxies_list.pop()
            status =self.get("http://ident.me/",proxy) 
            if status:
                print(f"Proxy: {proxy} - Status: OK")
                break
            else:
                print(f"Proxy: {proxy} - Status: Not OK")

        print(proxy)
        return proxy
    

    def fetch_data(self):
        sd_time = time.time()
        time.sleep(2)
        elements = {}
        try:
            #CATEGORY
            category_xpath = ["//div[@class= 'fontBodyMedium']/span/span/button","//div[@class= 'fontBodyMedium dmRWX']/span/span/span/span[2]/span/span"]
            for i in category_xpath:
                try:
                    category = self.driver.find_element(By.XPATH, i).text
                    self.log.info(f"category value of {self.name} found from this xpath and is {category}.")
                    if category is not None:
                        break
                except NoSuchElementException:
                    category = None
                    self.log.info(f"Category not found with the current xapth, continue with the next xpath.")
                    continue
            #RATING
            try:
                rating = self.driver.find_element(By.XPATH, "//div[@class = 'fontDisplayLarge']").text
            except NoSuchElementException:
                rating = None
                self.log.warning(f"Rating value not found for {self.name}.")
                #logger.exception("Exception occurred")
            #ADDRESS
            try:
                address = self.driver.find_element(By.XPATH, "//button[@data-item-id='address']/div/div[3]/div[1]").text
                    # elements[key] = element.text
            except NoSuchElementException:
                address = None
                self.log.warning(f"Address value not found for {self.name}.")
                #logger.exception("Exception occurred")
            #WEBSITE
            try:
                website = self.driver.find_element(By.XPATH, "//a[@data-item-id='authority']/div/div[3]/div[1]").text
                    # elements[key] = element.text
            except NoSuchElementException:
                website = None
                self.log.warning(f"Website value not found for {self.name}.")
                #logger.exception("Exception occurred")
            #PHONE NUMBER
            try:
                phone = self.driver.find_element(By.XPATH, "//a[@data-item-id='authority']/div/div[3]/div[1]").text
                    # elements[key] = element.text
            except NoSuchElementException:
                phone = None
                self.log.warning(f"Phone value not found for {self.name}.")
                #logger.exception("Exception occurred")
            #REVIEW COUNT
            try:
                reviewCount = self.driver.find_element(By.XPATH, "//button[@class = 'HHrUdb fontTitleSmall rqjGif']/span").text
            except NoSuchElementException:
                reviewCount = None
                self.log.warning(f"Rating value not found for {self.name}.")
                #logger.exception("Exception occurred")
            #OPEN HOURS
            openHours_xpath = ["//div[@class= 't39EBf GUrTXd']","//button[@aria-label='Open 24 hours · See more hours']/div[1]/div[3]/div[1]/span"]
            for i in openHours_xpath:
                try:
                    if openHours_xpath[0]:
                        time.sleep(2)
                        ele = self.driver.find_element(By.XPATH, i)
                        openHours = ele.get_attribute('aria-label')
                    if openHours_xpath[1]:
                        openHours = self.driver.find_element(By.XPATH, i).text
                    self.log.info(f"Open Hours value of {self.name} found from this xpath and is {openHours}.")
                    if openHours is not None:
                        break
                except NoSuchElementException:
                    openHours = None
                    self.log.info(f"Open Hours not found with the current xapth, continue with the next xpath.")
                    continue
        except Exception as e:
            print(e)
        crnt_url = self.driver.current_url

        try:
            coordinates = crnt_url.split('/@')[1].split(',')[0:2]
            latitude = float(coordinates[0])
            longitude = float(coordinates[1])
        except:
            print("We cant get the exact location")
        if self.name is None:
            self.name = ''
        elif address is None:
            address = ''
        self.req = (self.name+' '+address).replace(' ', '+').replace(',', '')
        # print(self.req)
        # print(self.name, rating, address, website, phone, crnt_url, latitude, longitude)
        elements['Title'] = self.name
        elements['Category'] = category
        elements['Place ID'] = self.place_id()
        elements['Address'] = address
        elements['Website'] = website
        elements['Phone'] = phone
        # elements['URL'] = crnt_url
        elements['Review Count'] = reviewCount
        elements['Rating'] = rating
        elements['Open Hours'] = openHours

        if latitude:
            elements['Latitude'] = latitude
        else:
            elements['Latitude'] = None

        if longitude:
            elements['Longitude'] = longitude
        else:
            elements['Longitude'] = None

        self.log.info(f"Get the value of {self.name} attributes\n-----------------------")

        # self.log.info(f"-----------------------\nInserting the value of {name} into excel file name is {filename}.")
        # export = ExportDataMaps(filename, para, d)
        # export.exportExcel()

        ed_time = time.time()- sd_time
        print(f'{ed_time:0.4f} taken for scraping data of one place')
        return elements


    def scraperData(self, kw, para, filename):
        try:
            self.log.info(f"Starting scraper for keyword: {kw}")
            # https://www.google.com/maps/search/land+marks+in+toronto+on+canada/
            self.driver.get('https://www.google.com/maps/search/'+kw.replace(" ", "+"))
            # print(kw.replace(" ", "+"))
            time.sleep(1)
            # Find the div element you want to scroll
            s_list_time  = time.time()
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
                time.sleep(1)
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
                if new_height == last_height or len(lst) >= 100:
                    break

                # Otherwise, update the last height and continue scrolling
                last_height = new_height

            # Get the HTML content of the entire scrollable element
            time.sleep(2)
            div = self.driver.find_element(
                By.XPATH, "//div[@role= 'feed'][@tabindex = '-1']")
            self.log.info(f'Get {len(lst)} value in list on this {kw}')
            print(lst)
            e_list_time  = time.time() - s_list_time
            print(f"The list takes time : {e_list_time:0.4f}")
            data = {}
            # Iterate over the child div elements of the parent div
            for child_div in div.find_elements(By.XPATH, "//div[@role = 'article']/a"):
                self.name = child_div.get_attribute('aria-label')
                # print(data)
                child_div.click()
                data[self.name] = self.fetch_data()
            # print(data)
            return data
        except Exception as e:
            self.log.error(
                'Error occurred while scraping for keyword {}: {}'.format(kw, str(e)))
            self.errorCont += 1
            return data
        
    def place_id(self):

        pid_time = time.time()
        # Open a new tab
        self.driver.execute_script("window.open('');")
        # Switch to the new tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get('https://www.google.com/search?q='+self.req)

        try:
            element = self.driver.find_element(By.XPATH,"//a[@id = 'wrkpb']")
            # Get the value of the attribute
            place_id = element.get_attribute("data-pid")
        except NoSuchElementException:
            place_id = None
            self.log.warning(f"Place ID value not found for {self.name}.")
            #logger.exception("Exception occurred")
        # Perform scraping operations on the new tab
        # Example: Get the URL of the new tab
        # new_tab_url = self.driver.current_url
        # print("New tab URL:", new_tab_url)

        # Close the new tab
        self.driver.close()

        # Switch back to the original tab (if needed)
        self.driver.switch_to.window(self.driver.window_handles[0])
        # print(place_id)
        gpid_time = time.time() - pid_time
        print(f"Timt Take for place id: {gpid_time/60:0.4f}")
        return place_id
    
    def place_id1(self):
        # Specify the URL of the website you want to scrape
        url = 'https://www.google.com/search?q='+self.req
        print(url)
        # Send a GET request to the website
        try:
            response = requests.get(url)

            # Get the HTML content from the response
            html_code = response.content

            # Create a BeautifulSoup object
            soup = BeautifulSoup(html_code, 'html.parser')
            # div_tag = soup.find('div', attrs={'data': 'pid'})
            a_tag = soup.find('a', text='Write a review')

            print("how are you?")

            # Extract the value of the data=pid attribute
            pid_value = a_tag['data-pid']

            # Now you can work with the BeautifulSoup object
            # For example, print the title of the webpage
            # print(pid_value)
            return pid_value
        except Exception as e:
            print(e)

    def endDriver(self):
        self.log.info('Quitting the driver...')
        self.driver.quit()
