# #from bs4 import BeautifulSoup
# import pandas as pd
# import time, datetime, requests
#
# # Selenium Drivers
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.keys import Keys
#
# inc_5000_2022_url = "https://www.inc.com/inc5000/2022"
# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "en-US,en;q=0.9",
#     "referer": "https://www.google.com/",
#     "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-Ua-platform": '"Windows"',
#     "sec-fetch-dest": "document",
#     "sec-fetch-mode": "navigate",
#     "sec-fetch-site": "cross-site",
#     "sec-fetch-user": "?1",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
#   }
# # print(headers)
# # print(inc_5000_2022_url)
# # r = requests.get(inc_5000_2022_url,headers=headers)
# # print(r.status_code)
#
# # Selenium driver details
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()) )
# driver.get(inc_5000_2022_url)
# time.sleep(3)
# table_selector = driver.find_element('xpath','//*[@id="mainApp"]/div[2]/div[1]/div/div[3]')
#
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')