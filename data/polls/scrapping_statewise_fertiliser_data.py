from selenium import webdriver 

from selenium.webdriver.common.by import By 

from selenium.webdriver.support.ui import WebDriverWait 

from selenium.webdriver.support import expected_conditions as EC 

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq


option = webdriver.ChromeOptions()

browser = webdriver.Chrome(executable_path='/home/farmguide/Downloads/chromedriver', chrome_options=option)


url = 'http://urvarak.co.in/'
browser.get(url)


browser.switch_to_frame('fullfrm')
browser.find_element_by_xpath('//*[@id="trHome1"]/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]/a').click()
browser.switch_to_window(browser.window_handles[1])
browser.switch_to_default_content()
browser.switch_to_frame('fullfrm')
browser.implicitly_wait(30)


month=np.arange(1,13,1)
year=np.arange(7,13,1)
month2=np.arange(10,13,1)

import time
import re

all_data = pd.DataFrame()
for y in year:
    x_path = '//*[@id="ddl_Year"]/option[{0}]'.format(y)
    browser.find_element_by_xpath(x_path).click()
    browser.implicitly_wait(6)
    yr=browser.find_element_by_xpath(x_path).text
    print(yr)
    for m in month:
        x_path = '//*[@id="ddl_Month"]/option[{0}]'.format(m) 
        browser.find_element_by_xpath(x_path).click()
        mnth=browser.find_element_by_xpath(x_path).text
        print(mnth)
        browser.implicitly_wait(5)
        browser.find_element_by_xpath('//*[@id="goBtn"]').click()
        time.sleep(23)
        browser.implicitly_wait(5)
        browser.switch_to_default_content()
        browser.switch_to_frame('fullfrm')
        soup= BeautifulSoup(browser.page_source,'lxml')
        right_table=soup.find('table',{"id":'Table4'})

        A=[]
        B=[]
        C=[]
        D=[]
        E=[]
        F=[]
        G=[]
        H=[]
        I=[]
        J=[]
        L=[]
        M=[]
        for match in right_table.findAll('tr'):
            cells=match.findAll('td')

            if len(cells)==10:
                A.append(cells[0].findChildren(text=True)[-1])
                B.append(cells[1].findChildren(text=True)[-1])
                C.append(cells[2].findChildren(text=True)[-1])
                D.append(cells[3].findChildren(text=True)[-1])
                E.append(cells[4].findChildren(text=True)[-1])
                F.append(cells[5].findChildren(text=True)[-1])
                G.append(cells[6].findChildren(text=True)[-1])
                H.append(cells[7].findChildren(text=True)[-1])
                I.append(cells[8].findChildren(text=True)[-1])
                J.append(cells[9].findChildren(text=True)[-1])
                L.append(yr)
                M.append(mnth)
            else:
                break
                
        DF = pd.DataFrame()
        DF['Year']=L
        DF['Month']=M
        DF['State']=A
        DF['FG']=B
        DF['Requirement']=C
        DF['Opening Stock']=D
        DF['Monthly Plan']=E
        DF['Dispatches']=F
        DF['Net Receipts']=G
        DF['Availability']=H
        DF['Sales']=I
        DF['Closing Stock']=J
        all_data = all_data.append(DF,ignore_index=True)
        
browser.quit()





# for setting tor

# class BlockAll(cookiejar.CookiePolicy):
#     return_ok = set_ok =domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
#     netscape = True
#     rfc2965 = hide_cookie2 = False

# #activate tor session
# def get_tor_session():
#     session = requests.session()
#     # Tor uses the 9050 port as the default socks port
#     session.proxies = {'http':  'socks5://127.0.0.1:9050',
#                        'https': 'socks5://127.0.0.1:9050'}
#     return session
# #127.0.0.1:9050
# from stem import Signal
# from stem.control import Controller
# import stem


# #get port Ip,proxy from tor
# # signal TOR for a new connection    #switchIP():
# def renew_connection():
#     with Controller.from_port(port = 9051) as controller:
#         controller.authenticate(password='mypassword')
#         controller.signal(Signal.NEWNYM)


# # Choose a random proxy
# ua = UserAgent()
# headers = {
#           'User-Agent': ua.random
#           }
# #url = "https://www.forestryimages.org/pests.cfm"
# renew_connection()
# session = get_tor_session()
# #session.cookies.clear()
# session.cookies.set_policy(BlockAll())





# renew_connection()


# # from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


# import os
# import time


# proxyIP = "127.0.0.1"
# proxyPort = 8118



# profile = webdriver.FirefoxProfile()

# profile.set_preference('network.proxy.type', 1)
# profile.set_preference('network.proxy.socks', proxyIP)
# profile.set_preference('network.proxy.socks_port', proxyPort)
# profile.set_preference("general.useragent.override", ua.random)
# profile.set_preference("network.proxy.ssl", proxyIP)
# profile.set_preference("network.proxy.ssl_port", proxyPort)
# profile.set_preference("network.proxy.socks_remote_dns", True)
# profile.set_preference("network.proxy.ftp", proxyIP)
# profile.set_preference("network.proxy.ftp_port", proxyPort)


# # configuring profile
# # profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.folderList', 2)
# profile.set_preference('browser.download.manager.showWhenStarting', False)
# profile.set_preference('browser.download.dir', '/home/farmguide/Desktop/soil_data_testing_8/correctfile')
# profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain, application/vnd.ms-excel, text/csv, text/comma-separated-values, application/octet-stream, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
# options = FirefoxOptions()