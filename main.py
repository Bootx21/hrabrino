from datetime import datetime
from time import strptime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import smtplib
import os
from dotenv import load_dotenv

load_dotenv('.env')
smtp = os.environ['SMTP_ADDRESS']
address= os.environ['EMAIL_ADDRESS']
password = os.environ['EMAIL_PASSWORD']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.9',
'Accept-Encoding' : 'gzip, deflate, br',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}

def send_email(link):
    with smtplib.SMTP(smtp) as connection:
        connection.starttls()
        connection.login(user=address, password=password)
        connection.sendmail(
            from_addr=address,
            to_addrs=[address, 'mari_laroy@yahoo.com'],
            msg=f"Subject:New house for sale in Hrabrino!!\n\n"
                f"{link}")
def search_alo():
    ALO_HRABRINO ='https://www.alo.bg/obiavi/imoti-prodajbi/kashti-vili/?region_id=16&location_ids=3380'
    driver.get(ALO_HRABRINO)
    ads = driver.find_elements(By.CSS_SELECTOR, value='.listvip-params div a')
    how_many = len(ads)
    ads_list = []
    for _ in ads:
        ads_list.append(_.get_attribute("href").split("-")[-1])
    with open('/Users/nickboone/Documents/Coding/PycharmProjects/Hrabrino/homes_in_bg_alo.txt') as file:
        home_list = []
        for line in file.readlines():
            home_list.append(line.strip("\n"))
    for _ in ads_list:
        if _ not in home_list:
            send_email(f"https://www.alo.bg/searchq/?q={_}")
            home_list.append(_)

    with open('/Users/nickboone/Documents/Coding/PycharmProjects/Hrabrino/homes_in_bg_alo.txt', 'w') as file:
        for _ in home_list:
            file.write(f'{_}\n')


def search_imot():
    imot_hrabrino = 'https://www.imot.bg/pcgi/imot.cgi?act=3&slink=b81fhx&f1=1'
    driver.get(imot_hrabrino)

    ads = driver.find_elements(By.CLASS_NAME, value='lnk1')
    how_many = len(ads)

    ads_list = []
    for _ in ads:
        ads_list.append(_.get_attribute('href').split("=")[2].split("&")[0])

    with open('/Users/nickboone/Documents/Coding/PycharmProjects/Hrabrino/homes_in_bg_imot.txt') as file:
        home_list = []
        for line in file.readlines():
            home_list.append(line.strip("\n"))
    for _ in ads_list:
        if _ not in home_list:
            # send_email(f'https://www.imot.bg/pcgi/imot.cgi?act=5&adv={_}&slink=b81fhx&f1=1')
            home_list.append(_)

    with open('/Users/nickboone/Documents/Coding/PycharmProjects/Hrabrino/homes_in_bg_imot.txt', 'w') as file:
        for _ in home_list:
            file.write(f'{_}\n')



def search_homesbg():
    homesbg_hrabrino = 'https://www.homes.bg/?currencyId=1&filterOrderBy=0&locationId=3011&municipalityId=0&radiusId=0&typeId=HouseSell'
    driver.get(homesbg_hrabrino)
    ads = driver.find_elements(By.CSS_SELECTOR, value='.ListItemDesktop a')
    how_many = len(ads)

    ads_list = []
    for _ in ads:
        ads_list.append((_.get_attribute('href')).split("prodazhba/")[1])


    with open('/Users/nickboone/Documents/Coding/PycharmProjects/Hrabrino/homes_in_bg_homesbg.txt') as file:
        home_list = []
        for line in file.readlines():
            home_list.append(line.strip("\n"))
    for _ in ads_list:
        if _ not in home_list:
            send_email(f'https://www.homes.bg/offer/kyshta-za-prodazhba/{_}')
            home_list.append(_)

    with open('/Users/nickboone/Documents/Coding/PycharmProjects/Hrabrino/homes_in_bg_homesbg.txt', 'w') as file:
        for _ in home_list:
            file.write(f'{_}\n')
    driver.quit()



search_alo()
time.sleep(3)
search_imot()
time.sleep(3)
search_homesbg()



