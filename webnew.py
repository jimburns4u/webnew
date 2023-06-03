import re,xlsxwriter,os,threading,time,datetime,shutil,sys,re,ctypes,atexit,zmq,glob,random
import win32gui,win32con,win32api
from pycoingecko import CoinGeckoAPI
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm
from tqdm import trange
from urllib.request import urlretrieve
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from infi.systray import SysTrayIcon
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
from PIL import Image
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
now2 = datetime.datetime.now()
now = (now2.strftime("%d-%m-%Y %H:%M"))
client = Client('xxQMGgCx3pEsomOLfzTVmaPadRGTxTiBTAKQm8vDPubyGC7WcQsdkgSJdNKIZdBI', 'BJWIjUrGYKDIquAtcRltaquwzxEPxGmM0guXhlP4Tyl0CVGSR57Pg52kgYrs8pJC')
checknet= "//Desktop-mi103fq/c/Users/Public/Documents/Excels"
localuser = 'excels/users.txt'
localaccounts = 'excels/waccounts.txt'
date7,firstdate7,oz,oz2,date,firstdate,firstbans,datein,firstusers,firstwunits,firstpoints,firstwunits2,firstpoints2,firstdate2,total= [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
pig4,pig5,tb,wb,s1,w1,i,p,z,start,stop,pig,pig1,pig2,pig3,bi,start1,start2,start3,start4,start5,start6,start7,start8,start9,start10,start11,start12,start13,start101,start202,xx,fpswitch,r1 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
def exit_handler():    
    try:
        driver.close()
    except:
        pass

atexit.register(exit_handler)
def startup():
    cullovertime()
    systray()
    workouttime()
    workouttimecom()
    workouttimeran()
    workouttimeres()

def restart():
    global start13
    print(now,'restart initiated')
    x = 1
    start13 = 1
    while start13 == 1:
        time.sleep(1)
        x = x+1
        if x == 120:
            start13 == 0
            print(now,'restart taking too long, forcing')
            time.sleep(15)
    os.system("shutdown /r /t 0")
    
def show(systray):
    hWnd = kernel32.GetConsoleWindow()
    SW_HIDE = 1
    if hWnd:
        user32.ShowWindow(hWnd, SW_HIDE)

def show2():
    hWnd = kernel32.GetConsoleWindow()
    SW_HIDE = 1
    if hWnd:
        user32.ShowWindow(hWnd, SW_HIDE)
    
def hide(systray):
    hWnd = kernel32.GetConsoleWindow()
    SW_HIDE = 0
    if hWnd:
        user32.ShowWindow(hWnd, SW_HIDE)
def doover(systray):
    global start
    start = 1

def picday(systray):
    global s1
    print(now,'- Pic of the day initiating')
    s1 = 1

def on_quit_callback(systray):
    global stop
    print(now,'- Close Manually')
    stop = 1
    show2()
   
def monoff():	
    win32api.PostMessage(win32con.HWND_BROADCAST,
                 win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
    #os.popen('python closeblue.pyw')
def monon():
    win32api.keybd_event(32, 0, 0, 0)
def systray():
    menu_options = (("Show", None, show),("Hide", None, hide),("The Do Over", None, doover),("Pic of the day", None, picday),)
    systray = SysTrayIcon("lightning.ico", "Web Scraper", menu_options, on_quit=on_quit_callback)
    systray.start()
    hide(systray)

def assets():
    global nano,banano,xe,comsec,audnano,audbanano
    getbanano()
    getxe()
    getcomsec()
    getnano()
    getrose()
    getvite()
    getbtc()
    getrams()
    audnvite = vite * xe
    audrose = rose * xe
    audnano = nano * xe
    audbanano = banano * xe
    print(now," - Assets in sync")
def getnano():
    global nano,pig2,hnano
    try:
        nanoprice2 = (client.get_symbol_ticker(symbol='XNOUSDT'))
        nanoprice2 = float(nanoprice2['price'])
        nano = float(round(nanoprice2,4))        
        if pig2 == 0:
            hnano = nano
            print(now," - Nano =$",nano,sep="")
            pig2 = 1        
    except:        
        print(now,'- Error getnano')

def getvite():
    global vite,pig5,hvite
    #cg = CoinGeckoAPI()
    #try:
        #banano2 = cg.get_price(ids='shiboki', vs_currencies='usd')
        #banano1 =  float(re.sub("[^\d\.]", "", str(banano2)))
        #vite1 = float(banano1 * .001)
        #vite = float(round(vite1, 6))
    vite = float(0.000)
    if pig5 == 0:
        hvite = vite
        pig5=1
        print(now,'- Shiboki: $',vite)
    #except:        
        #if pig5 == 0:
            #vite = 0.00
            #hvite = vite
        #print(now,'- Error Shiboki')


        
def getrose():
    global rose,pig4,hrose
    cg = CoinGeckoAPI()
    try:
        banano2 = cg.get_price(ids='floki', vs_currencies='usd')
        banano1 =  float(re.sub("[^\d\.]", "", str(banano2)))
        rose = float(round(banano1, 6))
        if rose > 100:
            rose = float(round(banano1 / 100, 6))
            if rose > 20:
                rose = float(round(banano1 / 10, 6))
        if pig4 == 0:
            hrose = rose
            pig4=4
            print(now,'- Floki-inu: $',rose)
    except:        
        if pig4 == 0:
            rose = 0.00
            hrose = rose
        print(now,'- Error Floki-inu')

def getnanos(): 
    url = "https://nanocrawler.cc/explorer/account/nano_1w3thphsi4pdwf4q3naq8yxk53pbj9kd5hat5c6dzr8r6fq8fa799stahpi1/history"
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1366x768")
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(2)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        h4_tag = soup.h4
        data = soup.find_all('h3')
        mlist = []
        mlist2 = []
        for each in data:
            mlist.append(each.text)
        if mlist == []:
           data = soup.find_all('h5')
           for each in data:
              mlist.append(each.text)
        total2 = mlist[0].replace(" NANO", "")
        total2 = total2.replace(",", "")
        total2 = float(total2)
        data = soup.find_all("p", class_="text-muted mb-0")
        for each in data:
           mlist2.append(each.text)
        y = [mlist2.index(q) for q in mlist2 if 'NANO pending' in q]
        pend=(mlist2[y[0]].replace(" NANO pending",""))
        pend = pend.replace(",", "")
        pend = float(pend)
        ftotal = total2+pend
        if ftotal > 0.00000000000001:            
            with open('nano.txt', 'w') as f:
                f.write(str(ftotal))
        driver.close()
    except:
        driver.close()
        print(now,'- Error getnanos')

def getether(): 
    url = "https://nanocrawler.cc/explorer/account/nano_3qsor485bgztja8gzsoidfemihia4zhfhxg4ggpztg5qwaapy1d7wghb6wz4/history"
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1366x768")
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(2)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        h4_tag = soup.h4
        data = soup.find_all('h3')
        mlist = []
        mlist2 = []
        for each in data:
            mlist.append(each.text)
        if mlist == []:
           data = soup.find_all('h5')
           for each in data:
              mlist.append(each.text)
        total2 = mlist[0].replace(" NANO", "")
        total2 = total2.replace(",", "")
        total2 = float(total2)
        data = soup.find_all("p", class_="text-muted mb-0")
        for each in data:
           mlist2.append(each.text)
        y = [mlist2.index(q) for q in mlist2 if 'NANO pending' in q]
        pend=(mlist2[y[0]].replace(" NANO pending",""))
        pend = pend.replace(",", "")
        pend = float(pend)
        ftotal = total2+pend
        if ftotal > 0.00000000000001:
            with open('ether.txt', 'w') as f:
                f.write(str(ftotal))
        driver.close()
    except:
        driver.close()
        print(now,'- Error getdata2')
        
def getbtc():
    global btc,pig3,hbtc
    try:
        btc2 = (client.get_symbol_ticker(symbol='BTCUSDT'))
        btc2 = float(btc2['price'])
        btc = int(btc2)       
        if pig3 == 0:
            hbtc = btc
            print(now," - Bitcoin =$",btc,sep="")
            pig3 = 1        
    except:        
        print(now,'- Error getnano')

def getrams():
    global rams
    url = "https://inetbnkp.adelaidebank.com.au/OnlineBanking/TicToc/BankFast-Username-Logon#sst"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(url)    
    wait = WebDriverWait(driver, 600)
    time.sleep(1)
    try:
        x_arg = '//*[@id="id8"]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        inp_xpath = '//*[@id="id8"]'
        input_box = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath)))
        input_box.send_keys("42549931")
        x_arg = '//*[@id="id12"]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        inp_xpath = '//*[@id="id12"]'
        input_box = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath)))    
        input_box.send_keys("2710mouseAnnerie"+ Keys.ENTER)
        time.sleep(3)    
        rams2 = driver.find_element(By.XPATH, '//*[@id="id60"]/tr/td[4]/span/span[2]').text
        rams2 = float(rams2.replace(",",""))
        today = datetime.datetime.now()
        dnow = today.strftime('%#d')
        dnow = int(dnow)
        if dnow > 25:
            dnow = int(dnow -25)
        else:
            dnow = int(dnow + 5)
        interest = float(dnow * 55)
        unifees = float(2200)   #CHANGE UNIFEES HERE
        rams3 = float(rams2-interest)
        rams3 = round(rams3, 2)
        rams = float(rams3-unifees)
        rams =round(rams, 2)
        print(now,'- available tictoc - $',rams,sep='')
        driver.close()
    
    except:
        print(now,'- Error gettictoc')
        driver.close()
        rams = 0.00

def getramsOLD():
    global rams 
    url = "https://auth.securebanking.myrams.com.au/Account/Login?ReturnUrl=%2Foauth%2Fauthorize%3Fclient_id%3DWeb%26redirect_uri%3Dhttps%253A%252F%252Fapi.securebanking.myrams.com.au%252Fsignin-localauth%26response_type%3Dcode%26scope%3Dopenid%2520profile%26response_mode%3Dform_post%26nonce%3D637584709553078857.MTVjM2UxM2ItMzIxZC00OTMzLTk4NzAtMTdiOGRjMmU0MTdkM2MxYTZhNDEtODVkZi00ZTZiLWIzOWMtMmZmMzljNjNjN2Qx%26state%3DCfDJ8KSp6WoVlstDpvrzBov92-t8kUEhbCPzcm1W790DG_8InIvrS4_OV7ItSlUP-vXj-AOIGF_0oHjIK6IM-BJFNWrZKIgTsu1EoyUprG5CBiNP_ESSYBXmXzwtnFxQSuYyBmPWh9_44KfZRmqrIy37r6VwCejXERqd6ph3RcG11VI2yS0_af2Tq0SQvt-nfDjLN91l_b1vZZeN-iYbicZbWKGplZh_edVj2NlF_-W6fzuXlegCvWi9BD2UMyiblB6iq9WJHRGiKwmG6g3CWmgrADx9EI5ouLaLG2lvLYudefPYWNweG4vIDTG8A61ACFhbaKOqyE0nUHiLUTlO1dgwO365-xNS3YG1-PLyWONSIXO72a7op9WisLgmc9Odm2Iegw%26backUrl%3Dhttps%253A%252F%252Fsecurebanking.myrams.com.au%252F&client_id=Web"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--user-data-dir=C:\\Users\\bluei\\AppData\\Local\\GoogleChrome\\User Data\\Profile 13")
    options.add_argument("--window-size=1366x768")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(url)    
    wait = WebDriverWait(driver, 20)
    time.sleep(2)
    try:
        x_arg = '//*[@id="Username"]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        inp_xpath = '//*[@id="Username"]'
        input_box = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath)))
        input_box.send_keys("10350697")
        x_arg = '//*[@id="Secret"]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        inp_xpath = '//*[@id="Secret"]'
        input_box = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath)))
    
        input_box.send_keys("Jimburns4u"+ Keys.ENTER)
        time.sleep(6)
        try:
            x_arg = '/html/body/div[2]/div/div[3]/button'
            group_title = wait.until(EC.presence_of_element_located((
                By.XPATH, x_arg)))
            group_title.click()
        except:
            pass
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        data = soup.find_all("div", class_="ui available balance region right aligned")
        mlist = []
        for each in data:
            mlist.append(each.text)
        if mlist == []:
            print(now,'Rams error getting balance')
        rams2 = (mlist[0].replace("Available Funds:$","")).replace(",","").replace(":Available Funds","")
        rams2 = float(rams2)
        time.sleep(2)
        x_arg2 = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg2)))
        group_title.click()
        time.sleep(2)
        x_arg3 = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[4]/a[2]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg3)))
        group_title.click()
        time.sleep(3)
        try:
            x_arg5 = '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[5]/div[2]/div/div[2]/div/div[4]/div[2]/span/span'
            group_title5 = wait.until(EC.presence_of_element_located((
                By.XPATH, x_arg5)))
            interest = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[5]/div[2]/div/div[2]/div/div[4]/div[2]/span/span').text
            interest = float(interest.replace("-$",""))
        except:
            print(now,'new rams error')
            interest = '0.00'
        rams = float(rams2-float(interest))
        rams = round(rams, 2)           
        driver.close()
        print(now,'rams = $', rams)
    except:
        print(now,'- Error getrams')
        driver.close()
        rams = '0.00'
    
def getbanano():
    global banano,pig1,hbanano
    cg = CoinGeckoAPI()
    try:
        banano2 = cg.get_price(ids='banano', vs_currencies='usd')
        banano1 =  float(re.sub("[^\d\.]", "", str(banano2)))
        banano = float(round(banano1, 5))
        if pig1 == 0:
            hbanano = banano
            pig1=1
            print(now,'- Banano: $',banano)
    except:
        if pig1 ==0:
            banano = 0.00
            hbanano = banano
        print(now,'- Error getbanano')
def getxe():
    global xe
    url = "https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=AUD"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--user-data-dir=C:\\Users\\bluei\\AppData\\Local\\GoogleChrome\\User Data\\Profile 5")
    options.headless = True
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(1)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        data = soup.find_all('td')
        mlist = []
        for each in data:
            mlist.append(each.text)
        y = [mlist.index(q) for q in mlist if 'AUD' in q]
        xe=float(mlist[y[0]].replace(" AUD",""))
        driver.close()
    except:
        driver.close()
        print(now,'- Error getxe')
def getcomsecliveprice():
    global comsec,pig,hcomsec
    url = "https://www2.commsec.com.au/quotes/summary?stockCode=JNO&exchangeCode=ASX"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')
    options.headless = True
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 30)
        time.sleep(4)
        x_arg2 = '//*[@id="username_input"]'       
        group_title2 = wait.until(EC.presence_of_element_located((
           By.XPATH, x_arg2)))
        group_title2.click()
        inp_xpath2 = '//*[@id="username_input"]'
        input_box2 = wait.until(EC.presence_of_element_located((
           By.XPATH, inp_xpath2)))    
        input_box2.send_keys("54802969")
        time.sleep(2)
        x_arg = '//*[@id="password_input"]'
        group_title = wait.until(EC.presence_of_element_located((
           By.XPATH, x_arg)))
        group_title.click()
        inp_xpath = '//*[@id="password_input"]'
        input_box = wait.until(EC.presence_of_element_located((
           By.XPATH, inp_xpath)))    
        input_box.send_keys("im2ys4ustreek" + Keys.ENTER)
        time.sleep(3)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        data = soup.find_all("div", class_="stock-price__last-price-value")
        mlist = []
        for each in data:
            mlist.append(each.text)
            comsec = float(mlist[0].replace(" $","").replace(" (AUD) ",""))
            with open('comsec.txt', 'w') as f:
                f.write(str(comsec))
        if pig == 0:
            hcomsec=comsec
            pig=1
            
    except:
            try:
                comsec            
            except NameError:
                with open('comsec.txt') as ff:
                    comsec = float(ff.readline())
                    hcomsec = comsec
                    print(comsec)
            driver.close()            
            print(now,'- Error getcomsec')
            return
    driver.close()
def getcomsec():
    global comsec,pig,hcomsec
    with open('comsec.txt') as ff:
        comsec = float(ff.readline())
        hcomsec = comsec
        print(comsec)
def comstart():
    global start3
    start3 = 1

def comsecend():
    global comsec,comsecclose,start10   
    getcomsec()
    comsecclose = ('Comsec closed the day at $'+str(comsec))
    start10 =1
    workouttimecom()
    timer2 = threading.Timer(delaycom, comsecend).start()
def workouttime():
   global delay
   nextDay = datetime.datetime.now() + datetime.timedelta(days=1)
   dateString = nextDay.strftime('%d-%m-%Y') + " 09-15-00"
   newDate = nextDay.strptime(dateString,'%d-%m-%Y %H-%M-%S')
   delay = (newDate - datetime.datetime.now()).total_seconds()
   if delay > 86400:
      delay = delay - 86400
      if delay > 43200:
         delay = delay - 43200
   else:
      if delay > 43200:
         delay = delay - 43200
def workouttimecom():
   global delaycom
   nextDay = datetime.datetime.now() + datetime.timedelta(days=1)
   dateString = nextDay.strftime('%d-%m-%Y') + " 14-15-00"
   newDate = nextDay.strptime(dateString,'%d-%m-%Y %H-%M-%S')
   delaycom = (newDate - datetime.datetime.now()).total_seconds()
   if delaycom > 86400:
      delaycom = delaycom - 86400
def workouttimeres():
   global delayres
   nextDay = datetime.datetime.now() + datetime.timedelta(days=1)
   dateString = nextDay.strftime('%d-%m-%Y') + " 02-30-00"
   newDate = nextDay.strptime(dateString,'%d-%m-%Y %H-%M-%S')
   delayres = (newDate - datetime.datetime.now()).total_seconds()
   if delayres > 86400:
      delayres = delayres - 86400
def workouttimeran():
    global delayran,tuesday
    nextDay = datetime.datetime.now() + datetime.timedelta(days=1)
    dateString = nextDay.strftime('%d-%m-%Y') + " 20-00-00"
    newDate = nextDay.strptime(dateString,'%d-%m-%Y %H-%M-%S')
    delayran = (newDate - datetime.datetime.now()).total_seconds()
    today = datetime.datetime.now()
    day= today.weekday()
    if delayran > 86400:
        delayran = delayran - 86400
    tuesday= (8-int(day))*86400
    tuesday = tuesday + int(delayran)
    if tuesday > 604800:
        tuesday = tuesday - 604800
    if delayran > 71999:
        tuesday= tuesday - 86400
        if tuesday < 0:
            tuesday = tuesday +604800
        
    print(now,(tuesday/60)/60,'hours until ing')
    if delayran > 43200:
            delayran = delayran - 43200
def ing():
    global rams,tb,start1,ing1
    url = "https://www.ing.com.au/securebanking/"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.headless = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--window-size=1366x768")
    options.add_argument("--user-data-dir=C:\\Users\\bluei\\AppData\\Local\\GoogleChrome\\User Data\\Profile 12")
    driver = webdriver.Chrome(options=options)
    driver.get(url)    
    wait = WebDriverWait(driver, 600)
    time.sleep(8)
    x_arg = '//*[@id="cifField"]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()
    inp_xpath = '//*[@id="cifField"]'
    input_box = wait.until(EC.presence_of_element_located((
        By.XPATH, inp_xpath)))
    input_box.send_keys('42541798')
    r=0
    num = ['//*[@id="keypad"]/div/div[1]/div[1]/div/img', '//*[@id="keypad"]/div/div[1]/div[2]/div/img','//*[@id="keypad"]/div/div[1]/div[3]/div/img','//*[@id="keypad"]/div/div[2]/div[1]/div/img','//*[@id="keypad"]/div/div[2]/div[2]/div/img',
        '//*[@id="keypad"]/div/div[2]/div[3]/div/img', '//*[@id="keypad"]/div/div[3]/div[1]/div/img','//*[@id="keypad"]/div/div[3]/div[2]/div/img','//*[@id="keypad"]/div/div[3]/div[3]/div/img','//*[@id="keypad"]/div/div[4]/div[2]/div/img']
    while r < 10:
        img = driver.find_element_by_xpath(num[r])
        src = img.get_attribute('src')
        urlretrieve(src, "ing\download ("+str(r)+").png")
        r=r+1
    jim= []
    jim.append (os.path.getsize('ing\download (0).png'))
    jim.append (os.path.getsize('ing\download (1).png'))
    jim.append (os.path.getsize('ing\download (2).png'))
    jim.append (os.path.getsize('ing\download (3).png'))
    jim.append (os.path.getsize('ing\download (4).png'))
    jim.append (os.path.getsize('ing\download (5).png'))
    jim.append (os.path.getsize('ing\download (6).png'))
    jim.append (os.path.getsize('ing\download (7).png'))
    jim.append (os.path.getsize('ing\download (8).png'))
    jim.append (os.path.getsize('ing\download (9).png'))
    i=0
    while i < 10:
        if 1114<= jim[i] <= 1119:
           num9 = i
        if 1124<= jim[i] <= 1134:
           num6 = i
        i=i+1
    try:  
        x_arg2 = num[num6]
        group_title2 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg2)))
        group_title2.click()
        time.sleep(.5)
        x_arg3 = num[num9]
        group_title3 = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg3)))
        
    except:
        driver.close()
        print(now,'ing error1- restarting')
        if tb < 2:
            timer10 = threading.Timer(2, ing).start()
            tb=tb+1
        return
    try:
        tb=0    
        group_title3.click()
        time.sleep(.5)
        group_title2.click()
        time.sleep(.5)
        group_title3.click()
        time.sleep(.5)
        x_arg4 = '//*[@id="login-btn"]'
        group_title4 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg4)))
        time.sleep(5)
        group_title4.click()
        time.sleep(2)

        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        data = soup.find_all("span", class_="uia-account-category-available-balance style-scope ing-all-accounts-summary")
        mlist = []
        for each in data:
            mlist.append(each.text)
        balance = (mlist[0].replace("$",""))
        balance = balance.replace(",","")
        balance = float(balance)
        #NEEDED IS AMOUNT WANT TO KEEP IN ACCCOUNT FOR MORTGAGE
        needed = float('5')
        if balance <= needed:
            ing1= ('Low funds... Only $'+str(balance))
            print(now,ing1)
            start1=1
            try:
                timer11 = threading.Timer(tuesday, ing).cancel()
            except:
                ing1= ('Transfers starting - Current balance = $'+str(balance))
                print(now,ing1)
                start1=1
                pass
            timer11 = threading.Timer(tuesday, ing).start()
            driver.close()
            return
        transfer = float(balance - needed)
        transfer = round(transfer,2)
        maxi = float(950)
        maxi2 = float(954)
        if transfer > maxi2:
            transfer = maxi  
        x_arg5 = '//*[@id="mainMenuList"]/li[4]/div/div[2]/span'
        group_title5 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg5)))
        group_title5.click()
        time.sleep(1)
        x_arg6 = '//*[@id="navigation-transfer"]/li[3]/div'
        group_title6 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg6)))
        group_title6.click()
        time.sleep(1)
        x_arg7 = '//*[@id="from_targetInput"]'
        group_title7 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg7)))
        group_title7.click()
        time.sleep(2)
        x_arg8 = '//*[@id="from_listboxitem0"]/div[2]/div/div'
        group_title8 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg8)))
        group_title8.click()
        time.sleep(2)
        x_arg9 = '//*[@id="to_targetInput"]'
        group_title9 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg9)))
        group_title9.click()
        time.sleep(2)
        x_arg10 = '//*[@id="to_listboxitem0"]'
        group_title10 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg10)))
        group_title10.click()
        time.sleep(2)
        x_arg = '//*[@id="amount"]/div'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        time.sleep(2)
        inp_xpath15 = '/html/body/ing-index/div/ing-pages/iron-pages/ing-page-container[2]/section/ing-dashboard/div/iron-pages/section[1]/ing-pay-anyone/ing-page-block/div/iron-pages/div[1]/ing-layout[4]/div/div/ing-layout/div/div/ing-input/div/ing-input-validator/ing-field/input'
        input_box15 = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath15)))
        input_box15.send_keys(str(transfer))
        time.sleep(1)
        x_arg = '//*[@id="transferButtonText"]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        time.sleep(1)
        x_arg = '//*[@id="confirmButton"]/span'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        time.sleep(8)
        x_arg = '//*[@id="tabPageReciept"]/ing-layout[2]/div/div/ing-content-block/div/ul[1]/li[3]/div[2]/span'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        newbal2 = driver.find_element(By.XPATH, '//*[@id="tabPageReciept"]/ing-layout[2]/div/div/ing-content-block/div/ul[1]/li[3]/div[2]/span').text
        newbal = newbal2.replace("$","")
        newbal = newbal.replace(",","")
        newbal = float(newbal)
        print(now,newbal)
        if len(newbal2) < 1:
            ing1 = ('transfer didnt work')
            print(now,ing1)
            start1=1
        else:
            ing1 = ("$"+str(transfer)+" transfered to UP, new balance of $"+str(newbal))
            print(now,ing1)
            start1=1

        #NOW TICTOC
        transfer = float(newbal - needed)
        x_arg5 = '//*[@id="mainMenuList"]/li[4]/div/div[2]/span'
        group_title5 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg5)))
        group_title5.click()
        time.sleep(1)
        x_arg6 = '//*[@id="navigation-transfer"]/li[3]/div'
        group_title6 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg6)))
        group_title6.click()
        time.sleep(1)
        x_arg7 = '//*[@id="from_targetInput"]'
        group_title7 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg7)))
        group_title7.click()
        time.sleep(2)
        x_arg8 = '//*[@id="from_listboxitem0"]/div[2]/div/div'
        group_title8 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg8)))
        group_title8.click()
        time.sleep(2)
        x_arg9 = '//*[@id="to_targetInput"]'
        group_title9 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg9)))
        group_title9.click()
        time.sleep(2)
        x_arg10 = '//*[@id="to_listboxitem2"]'
        group_title10 = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg10)))
        group_title10.click()
        time.sleep(2)
        x_arg = '//*[@id="amount"]/div'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        time.sleep(2)
        inp_xpath15 = '/html/body/ing-index/div/ing-pages/iron-pages/ing-page-container[2]/section/ing-dashboard/div/iron-pages/section[1]/ing-pay-anyone/ing-page-block/div/iron-pages/div[1]/ing-layout[4]/div/div/ing-layout/div/div/ing-input/div/ing-input-validator/ing-field/input'
        input_box15 = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath15)))
        input_box15.send_keys(str(transfer))
        time.sleep(1)
        x_arg = '//*[@id="transferButtonText"]'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        time.sleep(1)
        x_arg = '//*[@id="confirmButton"]/span'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        group_title.click()
        time.sleep(8)
        x_arg = '//*[@id="tabPageReciept"]/ing-layout[2]/div/div/ing-content-block/div/ul[1]/li[3]/div[2]/span'
        group_title = wait.until(EC.presence_of_element_located((
            By.XPATH, x_arg)))
        newbal2 = driver.find_element(By.XPATH, '//*[@id="tabPageReciept"]/ing-layout[2]/div/div/ing-content-block/div/ul[1]/li[3]/div[2]/span').text
        newbal = newbal2.replace("$","")
        newbal = newbal.replace(",","")
        newbal = float(newbal)
        print(now,newbal)
        if len(newbal2) < 1:
            ing1 = ('transfer didnt work')
            print(now,ing1)
            start1=1
        else:
            ing1 = ("$"+str(transfer)+" transfered to TicToc, new balance of $"+str(newbal))
            print(now,ing1)
            start1=1
        workouttimeran()
        timer11 = threading.Timer(tuesday, ing).start()
        tb = 0
        driver.close()
    except:
        driver.close()
        print(now,'ing error2- restarting')
        if tb > 2:
            timer10 = threading.Timer(2, ing).start()
            tb=tb+1
        else:
            workouttimeran()
            try:
                timer11 = threading.Timer(tuesday, ing).cancel()
            except:
                pass
            timer11 = threading.Timer(tuesday, ing).start()
        return

def newran():
    global pic,pic2,vid,picdate,pic2date,viddate,s1,w1
    list_pics = glob.glob('E://**/*.jpg' ,recursive = True) + glob.glob('E://**/*.jpeg' ,recursive = True)
    list_vids = glob.glob('E://**/*.mp4' ,recursive = True) + glob.glob('E://**/*.MOV' ,recursive = True)
    pic = random.choice(list_pics)
    pic2 = random.choice(list_pics)
    vid = random.choice(list_vids)
    vidsize = os.path.getsize(vid)
    while vidsize > 65000000:
        vid = random.choice(list_vids)
        vidsize = os.path.getsize(vid)
    try:
        picdate2 = Image.open(pic)._getexif()[36867]
        picdate = datetime.datetime.strptime(picdate2, '%Y:%m:%d %H:%M:%S').strftime('%d/%m/%Y %H:%M')
    except:
        picdate = 'Unknown Date'    
    try:
        pic2date2 = Image.open(pic2)._getexif()[36867]
        pic2date = datetime.datetime.strptime(pic2date2, '%Y:%m:%d %H:%M:%S').strftime('%d/%m/%Y %H:%M')
    except:
        pic2date = 'Unknown Date'    
    try:
        parser = createParser(vid)
        metadata = extractMetadata(parser)
        for line in metadata.exportPlaintext():
            if line.split(':')[0] == '- Creation date':
                viddate2 = line.split('- Creation date: ')[1]
        viddate = datetime.datetime.strptime(viddate2, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M')
        if viddate =='01/01/1904 00:00':
            viddate = 'Unknown Date'
        if len(viddate) < 5:
            viddate = 'Unknown Date'
    except:
        viddate = 'Unknown Date'
    w1=1

def newran2():
    global s1
    s1=1
    time.sleep(61)
    workouttimeran()
    timer5 = threading.Timer(delayran, newran2).start()

def cullovertime():
    global start12
    try:
        with open("overtime.txt", "r") as f:
            lines = f.readlines()
        with open("overtime.txt", "w") as f:
            for line in lines:
                try:
                    date = datetime.datetime.strptime(line[0:10], '%d/%m/%Y')
                except:
                    continue
                now5 = datetime.datetime.now()
                age2 = now5 - date
                age = age2.total_seconds() /3600
                if int(age) < int('382'):
                    f.write(line)                                                                        
        try:
            shutil.copy('overtime.txt', '//Desktop-il9uio1/p/overtime.txt')
        except IOError as e:
            pass
            #start12=1    #enable to see if jims pc is online
            #print(now,'error copying overtime.txt')
    except:
        return

def whatsappbot():
    global vite,rose,fpswitch,ing1,stop,pic,pic2,vid,picdate,pic2date,viddate,s1,w1,latest_file,start,start1,start2,start3,start4,start5,start6,start7,start8,start9,start10,start11,start12,start13,wnano,wbtc,wbanano,wcomsec,whatsappmsg,comsecclose,oz,oz2,nano,btc,xe,banano    
    ft,stop=0,0
    def quickmsg(string):
           global start13
           target2 = '"Trade"'
           wait = WebDriverWait(driver, 50) 
           inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'  #Main text input box
                        #//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1/p]
           try:
               input_box = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath)))
               for part in string.split('\n'):
                    input_box.send_keys(part)
                    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
               time.sleep(.3)
               input_box.send_keys(Keys.ENTER, Keys.ENTER)
               time.sleep(.5)
               if string == 'Robo going offline for a restart':
                   start13=0
                   print(now,'start13=0')
           except:
               stop=1
               print(now,'ERROR ERROR - WHATSAPP QUICKMSG FAILED')
               return
    
    def whatsapp(target, string):
            target2 = '"Trade"'
            wait = WebDriverWait(driver, 50) 
            x_arg = '//span[contains(@title,' + target + ')]'
            try:
                group_title = wait.until(EC.presence_of_element_located((
                  By.XPATH, x_arg)))
                group_title.click()
                time.sleep(2)
                inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]' #Main text input box
                             #//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p
                input_box = wait.until(EC.presence_of_element_located((
                  By.XPATH, inp_xpath)))
                time.sleep(2)
                if  'Ozbargain' in target:
                    input_box.send_keys(string)
                    time.sleep(4)
                else:
                     for part in string.split('\n'):
                         input_box.send_keys(part)
                         ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
                     time.sleep(2)
                input_box.send_keys(Keys.ENTER, Keys.ENTER)
                time.sleep(1)
                x_arg2 = '//span[contains(@title,' + target2 + ')]'
                group_title2 = wait.until(EC.presence_of_element_located((
                  By.XPATH, x_arg2)))
                group_title2.click()
                time.sleep(2)
            except:
                stop=1
                return
        
    def whatpic():
            global latest_file
            zr=0
            list_of_files = glob.glob('C://Blueiris/Alerts/*jpg')
            latest_file = max(list_of_files, key=os.path.getmtime)
            target2 = '"Trade"'
            wait = WebDriverWait(driver, 60)
            target = '"Robo"'   
            x_arg = '//span[contains(@title,' + target + ')]'
            try:
                group_title = wait.until(EC.presence_of_element_located((
                By.XPATH, x_arg)))
                #time.sleep(.5)
                group_title.click()
                inp_xpath = '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p'  #input text box on picture sending
                inp_xpath1 = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span' #Click paperclip
                inp_xpath2 = '/html/body/div[1]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'  #Send photo button                
                #time.sleep(.5)
                input_box1 = wait.until(EC.presence_of_element_located((
                By.XPATH, inp_xpath1)))
                #time.sleep(.5)
                input_box1.click()                                                      
                harry = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input') #Click on paperclip and search for camera to find photoinput
                harry.send_keys(latest_file)
                input_box = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath)))
                #time.sleep(.5)
                input_box.send_keys('Blueiris')
            except:                       
                stop=1
                print(now,"error blue iris")
                return
            try:
                input_box2 = wait.until(EC.presence_of_element_located((
                By.XPATH, inp_xpath2)))
                #time.sleep(.5)
                input_box2.click()    
                time.sleep(1)          
            except:
                while zr < 8:
                    try:
                        print(now,'trying to fix error whatpic')
                        time.sleep(20)
                        zr=zr+1                
                        input_box2 = wait.until(EC.presence_of_element_located((
                        By.XPATH, inp_xpath2)))
                        time.sleep(2)
                        input_box2.click()    
                        time.sleep(1)
                    except:
                        continue
                    print(now,'error fixed whatpic')
                    break                        
                stop=1
            try:                                                      
                home = '//span[contains(@title,' + target2 + ')]'
                group_home = wait.until(EC.presence_of_element_located((
                By.XPATH, home)))
                time.sleep(1)
                group_home.click()
                time.sleep(2)
            except:                       
                stop=1
                return
            
    def whatran():
            global w1,new,old,new2,newL
            zr,z=0,0
            try:
                
                while w1==0:
                    z=z+1
                    if z > 599:
                        stop=1
                        return
                    time.sleep(0.1)              
                w1=0
                target2 = '"Trade"'
                wait = WebDriverWait(driver, 60)
                target = '"Pic of the day"'   
                x_arg = '//span[contains(@title,' + target + ')]'
                try:
                    group_title = wait.until(EC.presence_of_element_located((
                        By.XPATH, x_arg)))
                    group_title.click()
                    inp_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p'  #input text box on picture sending
                    inp_xpath1 = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span' #Click paperclip
                    inp_xpath2 = '/html/body/div[1]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'  #Send photo button   
                    input_box1 = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath1)))
                    time.sleep(1)
                    input_box1.click()
                    time.sleep(1)
                    harry = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input') #Click on paperclip and search for camera to find photoinput
                    harry.send_keys(pic)
                    input_box = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath)))
                    time.sleep(1)
                    input_box.send_keys(picdate)
                    time.sleep(.5)
                except:                       
                    stop=1
                    return
                try:
                    input_box2 = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath2)))
                    time.sleep(1)
                    input_box2.click()        
                    time.sleep(1)
                except:
                    while zr < 8:
                        try:
                            print(now,'trying to fix error whatrann')
                            time.sleep(20)
                            zr=zr+1                
                            input_box2 = wait.until(EC.presence_of_element_located((
                            By.XPATH, inp_xpath2)))
                            time.sleep(1)
                            input_box2.click()    
                            time.sleep(1)
                        except:
                            continue
                        print(now,' error fixed whatrann')
                        break                        
                    stop=1
                try:
                    input_box1 = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath1)))
                    time.sleep(1)
                    input_box1.click()            
                    harry = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input') #Click on paperclip and search for camera to find photoinput
                    harry.send_keys(pic2)
                    input_box = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath)))
                    time.sleep(1)
                    input_box.send_keys(pic2date)
                    time.sleep(1)
                except:                       
                    stop=1
                    return
                try:
                    input_box2 = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath2)))
                    time.sleep(1)
                    input_box2.click()    
                    time.sleep(.5)
                except:
                    while zr < 8:
                        try:
                            print(now,'trying to fix error whatrann')
                            time.sleep(20)
                            zr=zr+1                
                            input_box2 = wait.until(EC.presence_of_element_located((
                            By.XPATH, inp_xpath2)))
                            time.sleep(1)
                            input_box2.click()    
                            time.sleep(1)
                        except:
                            continue
                        print(now,'error fixed whatrann')
                        break
                    stop=1
                try:
                    input_box1 = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath1)))
                    time.sleep(1)
                    input_box1.click()
                    harry = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input') #Click on paperclip and search for camera to find photoinput
                    harry.send_keys(vid)
                    inp_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]/p'  #Video Send input box
                    input_box = wait.until(EC.presence_of_element_located(( 
                    By.XPATH, inp_xpath)))
                    time.sleep(1)                            
                    input_box.send_keys(viddate)
                except:                       
                    stop=1
                    return
                try:
                    time.sleep(1)
                    input_box2 = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath2)))
                    time.sleep(1)
                    input_box2.click()
                    time.sleep(1)
                except:
                    while zr < 8:
                        try:
                            print(now,'trying to fix error whatrann')
                            time.sleep(20)
                            zr=zr+1                
                            input_box2 = wait.until(EC.presence_of_element_located((
                            By.XPATH, inp_xpath2)))
                            time.sleep(.5)
                            input_box2.click()    
                            time.sleep(1)
                        except:
                            continue
                        print(now,'error fixed whatrann')
                        break
                    stop=1
                try:
                    home = '//span[contains(@title,' + target2 + ')]'
                    group_home = wait.until(EC.presence_of_element_located((
                    By.XPATH, home)))
                    time.sleep(1)
                    group_home.click()
                    timer7 = threading.Timer(.001, newran).start()
                    time.sleep(2)
                except:                       
                    stop=1
                    return
            except:                       
                stop=1
                return

    def dickpic():
        global dpic
        print(now,'trying dickpic')
        try:
            wait = WebDriverWait(driver, 10)
            list_pics = glob.glob('D:/P/dp/*.jpg' ,recursive = True) + glob.glob('D:/P/dp/*.png' ,recursive = True) + glob.glob('D:/P/dp/*.gif' ,recursive = True)
            dpic = random.choice(list_pics)
            inp_xpath = '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p'  #input text box on picture sending
            inp_xpath1 = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span' #Click paperclip
            inp_xpath2 = '/html/body/div[1]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'  #Send photo button   
            input_box1 = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath1)))
            time.sleep(1)
            input_box1.click()
            time.sleep(1)
            harry = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input') #Click on paperclip and search for camera to find photoinput
            harry.send_keys(dpic)
            input_box = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath)))
            time.sleep(1)
            input_box.send_keys('Dickpic')
            time.sleep(.5)
            time.sleep(1)
            input_box2 = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath2)))
            time.sleep(1)
            input_box2.click()
            time.sleep(1)
        except:
            print('dickpick failed')
            stop=1
            return
    
    def robo():
        global f,robonew
        f,v=1,0         
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        data = soup.find_all("div", class_="copyable-text")
        new = []
        for each in data:
            new.append(each.text)
        del new[0:-11], new[-1]
        old = new.copy()
        while v < 30:
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"lxml")
            data = soup.find_all("div", class_="copyable-text")
            new = []
            for each in data:
                new.append(each.text)
            del new[0:-11], new[-1]
            if new == old:               
                time.sleep(1)
                v=v+1
                continue
            new2 = new.copy()
            for e in range(len(old)-5):
                del old[0],new2[-1]
                if new2 == old:
                    old = new.copy()
                    newL= new[-f:]
                    robonew= newL[-1]
                    f=1
                    return
                f=f+1
        quickmsg ("Timed out - Back to robot")
        robonew='N'
    def robofast():
        global f,robofastnew
        f,v=1,0         
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        data = soup.find_all("div", class_="copyable-text")
        new = []
        for each in data:
            new.append(each.text)
        del new[0:-11], new[-1]
        old = new.copy()
        while v < 10:
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"lxml")
            data = soup.find_all("div", class_="copyable-text")
            new = []
            for each in data:
                new.append(each.text)
            del new[0:-11], new[-1]
            if new == old:               
                time.sleep(1)
                v=v+1
                continue
            new2 = new.copy()
            for e in range(len(old)-5):
                del old[0],new2[-1]
                if new2 == old:
                    old = new.copy()
                    newL= new[-f:]
                    robofastnew= newL[-1]
                    f=1
                    return
                f=f+1
        quickmsg ("Timed out - Back to robot")
        robofastnew='N'
    def checkovertime():
        global robofastnew,robonew
        i=0
        try:            
            with open('overtime.txt', 'r') as reader:
                overtimetext=[]
                b=0
                for line in reader:
                    line = line.rstrip()
                    line= str(b)+'; '+line
                    overtimetext.append(line)
                    b=b+1
                quickmsg (str(overtimetext))
                quickmsg ("Do you want to delete any entries? Type 'Y' or 'N'")
                robofast()
                if robofastnew == 'Yes' or robofastnew == 'Y' or robofastnew == 'yes' or robofastnew == 'y':
                    quickmsg ("What number entry would you like to delete?")
                    robo()
                    try:
                        if int(robonew) > -1 and int(robonew) < 1000:
                            with open("overtime.txt", "r") as f:
                                lines = f.readlines()
                            with open("overtime.txt", "w") as f:
                                for line in lines:
                                    if str(i) != str(robonew):
                                        f.write(line)                                                                        
                                    i=i+1
                            try:
                                shutil.copy('overtime.txt', '//Desktop-il9uio1/p/overtime.txt')
                            except IOError as e:
                                pass
                            if int(robonew) > i:
                                quickmsg ("Entry does not exist")
                            else:
                                quickmsg ("Entry Deleted")
                    except:
                        quickmsg ("Number did not match up to an entry")
                        return
        except:
            quickmsg ('error')
            return
        
    f,bl,t=1,0,0
    tempwrit = "0"
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--user-data-dir=C:\\Users\\bluei\\AppData\\Local\\GoogleChrome\\User Data\\Profile 3")
    options.add_argument("--window-size=1920x1080")
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)
    target = '"Trade"'
    x_arg = '//span[contains(@title,' + target + ')]'
    time.sleep(1)
    group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
    time.sleep(1)
    group_title.click()
    inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'  #Main text inmput box
                
    input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
    time.sleep(1)
    old,new = [],[]
    while len(old)< 10:
        old = []
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        data = soup.find_all("div", class_="copyable-text")
        for each in data:
            pig = each.text
            if len(pig) > 8:
                if pig[-2:]=="am" or pig[-2:]=="pm":
                    pig = pig[:-7]
                    if pig[-1]== '1' :
                        pig = pig[:-1]                        
            old.append(pig)
        time.sleep(1)
        print(now,'waiting for 10',len(old))
        if (len(old)) < 9:
            time.sleep(1)
            ActionChains(driver).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).perform()
            ActionChains(driver).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).perform()
            time.sleep(1)
            ActionChains(driver).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_DOWN).perform()
            ActionChains(driver).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).perform()
    old = old[-10:]
    #START LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOP
    #LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOPSTART LONG LOOP
    while stop == 0:
        if s1==1:
            s1=0
            whatran()
        if start == 1:
            start= 0
            timer8 = threading.Timer(.001, fullloop).start()
        if start1 == 1:
            start1= 0
            quickmsg(ing1)            
        if start2 == 1:
            print(now,"-",oz)
            whatsapp('"Ozbargain"', oz)
            start2 =0
        if start3 == 1:
            start3=0
            comsecend()
        if start4 == 1:
            start4=0
            print (now,"-",wnano)
            whatsapp('"Trade"',wnano)
        if start5 == 1:
            start5=0
            print (now,"-",wbtc)
            whatsapp('"Trade"',wbtc)
        if start6 == 1:
            start6=0
            print (now),(wbanano)
            whatsapp('"Trade"',wbanano)
        if start7 == 1:
            start7=0
            print (now,'-',wcomsec)
            whatsapp('"Trade"', wcomsec)
        if start8 == 1:
            start8=0
            whatpic()
            print(now,'- Blueiris initiated')
        if start9 == 1:
            start9=0
            print (now,'-',whatsappmsg)
            whatsapp('"Banano"',whatsappmsg)
        if start10 == 1:
            start10=0
            print(now,'-',comsecclose)
            whatsapp('"Trade"',comsecclose)
        if start11 == 1:
            print(now,"-",oz2)
            whatsapp('"Ozbargain"', oz2)
            start11=0
        if start12 == 1:
            start12=0
            quickmsg('Jims PC is off, Can you please restart it annerie spencer')
        if start13 == 1:
            quickmsg('Robo going offline for a restart')
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        data = soup.find_all("div", class_="copyable-text")
        new = []
        for each in data:
            pig = each.text
            if len(pig) > 8:
                if pig[-2:]=="am" or pig[-2:]=="pm":
                    pig = pig[:-7]
                    if pig[-1]== '1' :
                        pig = pig[:-1]                        
            new.append(pig)
        new = new[-10:]
        if (len(new)) < 9:
            print(now,'loading more messages')
            time.sleep(.3)
            ActionChains(driver).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).perform()
            ActionChains(driver).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).perform()
            time.sleep(.3)
            ActionChains(driver).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_DOWN).perform()
            time.sleep(.3)
            ActionChains(driver).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).perform()
        if new == old:
            if ft == 0:
                print(now,'Bot Ready')
                #quickmsg('Robo back online')
                ft=1
            time.sleep(1)
            continue
        new2 = new.copy()
        for e in range(len(old)-5):
            del old[0],new2[-1]
            if new2 == old:
                old = new.copy()
                newL= new[-f:]
                f=1                
                while t < len(newL):
                    print(now,newL[t])
                    if newL[t] == 'Help' or newL[t]=='help':
                        quickmsg('Available Commands include: Doover, Aud, Blueiris, Pic, Price, Monoff, GetIng,Overtime,Checkovertime.')   
                    if newL[t] == 'Thedoover' or newL[t]=='Doover'or newL[t]=='Do over':
                        start=1
                        quickmsg('Do over initiated')
                    if newL[t] == 'Aud' or newL[t]=='AUD'or newL[t]=='Xe':
                        try:
                            aud=1/xe
                            quickmsg('Aussie dollar is - $'+ str(aud))
                        except:
                            print(now,'xe not ready yet')                      
                    if newL[t] == 'Dickpic' or newL[t]=='Dick pic':
                        dickpic()
                    if newL[t] == 'Blue' or newL[t]=='Iris'or newL[t]=='Blueiris'or newL[t]=='Blue iris':
                        start8=1
                    if newL[t] == 'pic' or newL[t]=='Pic':
                        quickmsg('Pic of the day initiated')
                        whatran()
                    if newL[t] == 'price' or newL[t]=='Price' or newL[t]=='Trade'or newL[t]=='trade':
                        print(now,'price recieved')
                        with open('banano.txt') as ff:
                            b1 = ff.readline()
                        with open('nano.txt') as ff:
                            b2 = float(ff.readline())
                        with open('ether.txt') as ff:
                            b30 = float(ff.readline())
                        b50= b2-721
                        b5 = b50+b30
                        finaltotal = int(b1)
                        bananototal= int(finaltotal*banano)
                        nanototal= int(float("3803") * nano)
                        nanototal2= int(float(b5) * nano)
                        vitetotal= int(float("1625625") * vite)
                        rose1= float(rose * .1)
                        if rose > 1:
                            rosetotal= int(float("2795") * rose1)
                        else:
                            rosetotal= int(float("279500000") * rose1)
                        audrose= int(rosetotal * xe)
                        audvite= int(vitetotal * xe)
                        audbanano= int(bananototal * xe)
                        audnano= int(nanototal * xe)
                        audnano2= int(nanototal2 * xe)
                        comsectotal=int(float("42000") * comsec)
                        viteprofit= audvite - int(2036)
                        roseprofit= audrose - int(2450)
                        mastertotal= int(audbanano+audnano+comsectotal+audnano2+audvite+audrose)
                        profit = mastertotal - int(40000)
                        if roseprofit > 0:
                            rosepro = ' - Profit: *$'
                        else:
                            rosepro = ' - Loss: *$'
                        if viteprofit > 0:
                            vitepro = ' - Profit: *$'
                        else:
                            vitepro = ' - Loss: *$'
                        if profit > 0:
                            pro = 'Profit: *$'
                        else:
                            pro = 'Loss: *$' 
                        quickmsg('Nano - $'+str(nano)+'\n'+'Bitcoin - $'+str(btc)+'\n'+'Floki - $'+str(rose)+str(rosepro)+str(roseprofit)+"*"+'\n'+'SHIBOKI - $'+str(vite)+str(vitepro)+str(viteprofit)+"*"+'\n'+'Banano - $'+str(banano)+'\n'+str(pro)+str(profit)+'*')
                    if newL[t] == 'monoff' or newL[t]=='Monoff' or newL[t]=='Mon off'or newL[t]=='mon off' or newL[t]=='Monitor off':
                        monoff()
                    if newL[t] == 'monon' or newL[t]=='Monon' or newL[t]=='Mon on'or newL[t]=='mon on' or newL[t]=='Monitor on':
                        monon()
                    if newL[t] == 'GetIng':
                        timer17 = threading.Timer(1, ing).start()
                    if newL[t] == 'Restart' or newL[t]=='restart':
                        timer22 = threading.Timer(1, restart).start()
                    if newL[t] == 'Overtime':
                        quickmsg('Expected format= Overtime xx/xx/xxxx x:xx or Checkovertime')
                    if newL[t] == 'Checkovertime' or newL[t] == 'Check':
                        checkovertime()

                    if 'Overtime ' in (newL[t][0:9]) or 'overtime ' in (newL[t][0:9]):
                        temp8= (newL[t][0:9])
                        temp7= (newL[t])
                        temp7= temp7.replace(temp8,"")
                        temp7= temp7.replace('.',":")
                        if '/' in temp7:
                            temp9= temp7.replace(' ',"-")                      
                        else:
                            temp9= now3+'-'+temp7
                        quickmsg(temp9+'\nIs this correct? Type "Y" or "N"')
                        robo()
                        if robonew == 'Yes' or robonew == 'Y' or robonew == 'yes' or robonew == 'y':
                            if len(temp9) > 13 and ':' in temp9:                           
                                    with open('overtime.txt', 'a+') as writer:
                                        writer.seek(0)
                                        overtimetxt=writer.read()
                                        r = "\n"+temp9
                                        writer.write(r)                            
                                        writer.close()                                                 
                                        try:
                                            shutil.copy('overtime.txt', '//Desktop-il9uio1/p/overtime.txt')
                                        except IOError as e:
                                            pass
                                    quickmsg('Your overtime has been logged '+temp9)
                            else:
                                quickmsg('Please check the format of your date, it has not been accepted')
                        elif robonew == 'No' or robonew == 'no' or robonew == 'N' or robonew == 'n':
                            quickmsg('Your overtime has NOT been saved')
                    t=t+1
                t=0
                
                break
            else:                f=f+1
        old = new.copy()
        time.sleep(1)
    driver.close()
    stop=2
    


def getuser():
   global users
   with open(localuser, 'r') as reader:
         q=(reader.read())
         r=q.splitlines()
         users=r

def getdata():
    global users,date,bans,wunits,points,i,firstdate,firstbans,datein,firstusers,firstwunits,firstwunits2,firstpoints2,firstdate2,firstpoints
    p=0
    date = []
    url = "https://www.monkey2monkey.com/fh-stats/?userid="+users[i]
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1366x768")
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(4)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        h4_tag = soup.h4
        data = soup.find_all('h4')
        mlist = []
        for each in data:
            mlist.append(each.text)        
        if (len(mlist)) < 3:
            mlist.append("5/3/2021 9:07 pm")
            mlist.append("0")
            mlist.append("0")
            mlist.append("0")
            data=["0","0","0","0"]
        w = slice(0,len(data),4)
        x = slice(1,len(data),4)
        y = slice(2,len(data),4)
        z = slice(3,len(data),4)
        date2 =(mlist[w])
        bans =(mlist[x])
        wunits=(mlist[y])
        points=(mlist[z])
        while not p == len(date2):
            datetime.datetime_object = datetime.datetime.strptime(date2[p], '%m/%d/%Y %I:%M %p')
            date.append(datetime.datetime_object)
            p=p+1        
        firstdate.append(date[0])
        firstbans.append(bans[0])
        firstwunits.append(wunits[0])
        firstpoints.append(points[0])
        driver.close()
    except:
        driver.close()
        print(now,'- Error getdata')

def addxl():
    global date,bans,wunits,points,users,url,address,i,checknet,localpath,netpath,netpathjim
    localpath="Excels/"+users[i]+".xlsx"
    netpath="//Desktop-mi103fq/c/Users/Public/Documents/Excels/"+users[i]+".xlsx"
    netpathjim="//Desktop-il9uio1/p/excels/"+users[i]+".xlsx"
    workbook = xlsxwriter.Workbook(localpath)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True, 'align': 'center'})
    center = workbook.add_format({'align': 'center'})
    worksheet.set_column(0, 0, 20)
    worksheet.set_column(1, 3, 11)
    worksheet.write('A1', 'Account - '+users[i], bold)
    worksheet.write('A2', 'Date', bold)
    worksheet.write('B2', 'Banano', bold)
    worksheet.write('C2', 'Work Units', bold)
    worksheet.write('D2', 'Points', bold)
    row, col = 2,0
    for date in (date):             
        worksheet.write(row, col, date.strftime('%d/%m/%Y %p'),center)
        row +=1
    row, col = 2,1
    for bans in (bans):
        worksheet.write(row, col, float(bans),center)
        row += 1
    worksheet.write(row, col, "=sum(B3:B"+str(row)+")", bold)
    row, col = 2,2
    for wunits in (wunits):
        worksheet.write(row, col, int(wunits),center)
        row += 1
    worksheet.write(row, col, "=sum(C3:C"+str(row)+")", bold)
    row, col = 2,3
    for points in (points):
        worksheet.write(row, col, int(points),center)
        row += 1
    worksheet.write(row, col, "=sum(D3:D"+str(row)+")", bold)
    worksheet.write(row, 0, "Totals -", bold)
    workbook.close()
    if os.path.exists(checknet):
      try:
          shutil.copy(localpath, netpath)
          shutil.copy(localpath, netpathjim)
      except IOError as e:
          pass

      

def latestxl():
    global date,bans,wunits,points,users,url,address,i,checknet,localpath2,netpath2,datei,jim    
    fdate2 = jim
    fdate = fdate2.replace("/","-").replace(" ","-")
    localpath2="Excels/latest/"+fdate+".xlsx"
    netpath2="//Desktop-mi103fq/c/Users/Public/Documents/Excels/latest/"+fdate+".xlsx"
    netpathjim2="//Desktop-il9uio1/p/excels/latest/"+fdate+".xlsx"
    workbook = xlsxwriter.Workbook(localpath2)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True, 'align': 'center'})
    center = workbook.add_format({'align': 'center'})
    worksheet.set_column(0, 0, 20)
    worksheet.set_column(1, 1, 15)
    worksheet.set_column(2, 4, 11)
    worksheet.write('A1', 'Latest Bananos', bold)
    worksheet.write('A2', 'Date', bold)
    worksheet.write('B2', 'Account', bold)
    worksheet.write('C2', 'Bananos', bold)
    worksheet.write('D2', 'Work Units', bold)
    worksheet.write('E2', 'Points', bold)
    row, col = 2,0
    for every in (firstdate):
        worksheet.write(row, col, (jim),center)
        row +=1
    row, col = 2,1
    for every in (users):
        worksheet.write(row, col, every,center)
        row += 1
    row, col = 2,2
    for every in (datein):
        worksheet.write(row, col, every,center)
        row += 1
    worksheet.write(row, col, "=sum(C3:C"+str(row)+")",bold)
    row, col = 2,3
    for every in (firstwunits2):
        worksheet.write(row, col, int(every))
        row += 1
        worksheet.write(row, col, "=sum(D3:D"+str(row)+")",bold)
    row, col = 2,4    
    for every in (firstpoints2):
        worksheet.write(row, col, int(every),center)
        row += 1
    worksheet.write(row, col, "=sum(E3:E"+str(row)+")",bold)
    worksheet.write(row, 1, "Totals -", bold)
    workbook.close()
    if os.path.exists(checknet):      
      try:
          shutil.copy(localpath2, netpath2)
          shutil.copy(localpath2, netpathjim2)
      except IOError as e:
          pass


def loop():
    global i,users
    i=0
    for u in trange(len(users), desc='Scraping BAN Info'):
        sleep(0.01)        
        getdata()
        addxl()
        i=i+1
        
    
def lastdate():
    global datein,firstuers,firstwunits,firstwunits2,firstpoints,firstpoints2,firstdate,firstdate2,u,jim
    p,u,=0,0
 
    jim = max(firstdate)
    jim = jim.strftime('%d/%m/%Y %p')
    while not p == (len(firstdate)):
        if firstdate[p].strftime('%d/%m/%Y %p') == jim:
            u = u+1
            datein.append(float(firstbans[p]))
            firstwunits2.append(firstwunits[p])
            firstpoints2.append(firstpoints[p])
            p=p+1
        else:
            datein.append(float("0"))
            firstwunits2.append("0")
            firstpoints2.append("0")
            p=p+1
    latestxl()

def getaccounts():
   global accounts,z
   with open(localaccounts, 'r') as reader:
         q=(reader.read())
         r=q.splitlines()
         accounts=r
   
def getdata2():
    global accounts,finaltotal,z,total,fpswitch
    url = "https://creeper.banano.cc/explorer/account/"+accounts[z]+"/history"
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1366x768")
    options.add_argument("--start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(2)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        h4_tag = soup.h4
        data = soup.find_all('h3')
        mlist = []
        mlist2 = []
        for each in data:
            mlist.append(each.text)
        if mlist == []:
           data = soup.find_all('h5')
           for each in data:
              mlist.append(each.text)
        total2 = mlist[0].replace(" BAN", "")
        total2 = total2.replace(",", "")
        total2 = float(total2)
        data = soup.find_all("p", class_="text-muted mb-0")
        for each in data:
           mlist2.append(each.text)
        y = [mlist2.index(q) for q in mlist2 if 'BAN pending' in q]
        pend=(mlist2[y[0]].replace(" BAN pending",""))
        pend = pend.replace(",", "")
        pend = float(pend)
        ftotal = total2+pend
        total.append(ftotal)
        driver.close()
    except:
        driver.close()
        print(now,'- Error getdata2')

def loop2():
    global z,accounts
    for r in trange(len(accounts), desc="Scraping BAN Total"):
        sleep(0.01)        
        getdata2()
        z=z+1
    z=0
def getoz():
    global oz,start2,xx,stop
    mlist, mlist2, mlist3,ldate,p,e,z = [],[],[],[],0,0,0
    if xx == 0:
        xx=1
        print(now,'- Getting Ozdata')
    url = "https://www.ozbargain.com.au/deals"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(1)
        ActionChains(driver).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).perform()
        ActionChains(driver).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        ActionChains(driver).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_UP).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        ActionChains(driver).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).perform()
        ActionChains(driver).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        ActionChains(driver).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).perform()
        ActionChains(driver).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).perform()
        time.sleep(1)
        ActionChains(driver).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).key_down(Keys.PAGE_DOWN).perform()
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        data = soup.find_all("span", class_="nvb voteup")
        for each in data:
           mlist.append(each.text)
        data2 = soup.find_all("h2", class_="title")
        data3 = soup.find("strong")
        data4 = data3.nextSibling
        if len(data4) > 2:
            data4 = data4.replace(" on ","").replace(" -","")
            mlist3.append(data4)
            for each in data2:
                j = str(each)
                h = j.find("id=")
                k = j[h+9:h+15]
                mlist2.append("https://www.ozbargain.com.au/node/"+k)
                try:
                    data3 = data3.findNext("strong")                      
                    data4 = data3.nextSibling
                    data4 = data4.replace(" on ","").replace(" -","")
                    if len(data4) > 6: 
                        mlist3.append(data4)
                except:
                    pass
        else:
            return
    except:
        driver.close()
        print(now,'- Error Ozbargain')
    while not p == len(mlist3):
        datetime.datetime_object = datetime.datetime.strptime(mlist3[p], '%d/%m/%Y %H:%M ')
        datetime.datetime_object = datetime.datetime_object - datetime.timedelta(hours=2)
        harry= datetime.datetime.now()
        barry = (harry - datetime.datetime_object) / 60
        ldate.append(barry.seconds)
        p=p+1
    while not e == len(ldate):
        while start2 == 1:
            print(now, '- waiting for ozbargain to post')
            z=z+1
            if z > 5:
                try:
                    Driver.quit()
                    stop=2
                except:
                    pass
            time.sleep(60)
        try:
            if int(mlist[e]) > 25:
                if ldate[e] > 1:
                    if int(mlist[e]) / ldate[e] > .20:
                        oz=(mlist2[e]+" - With "+mlist[e]+"Votes")
                        with open('oz.txt', 'a+') as writer:
                             writer.seek(0)
                             oztxt=writer.read()
                             if mlist2[e] in oztxt:
                                 pass
                             else:
                                 r = "\n"+ mlist2[e]
                                 writer.write(r)
                                 print(now,'-',mlist2[e])
                                 driver.get(mlist2[e])
                                 title2 = driver.title
                                 title = title2.replace("OzBargain","")
                                 oz= (title+oz)
                                 oz= oz.replace("https://","")
                                 start2=1
                                 time.sleep(5)
        except:
            try:
                driver.close()
            except:
                pass
            print(now,'- Error Ozbargain')
        e=e+1
    driver.close()

def getoz2():
    global oz2,start11
    mlist, mlist2, mlist3,ldate,p,e = [],[],[],[],0,0
    url = "https://www.ozbargain.com.au/deals/popular?days=1&noexpired=1"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver2 = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(1)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"lxml")
        data = soup.find_all("span", class_="nvb voteup")
        for each in data:
           mlist.append(each.text)
        data2 = soup.find_all("h2", class_="title")
        data3 = soup.find("strong")
        data4 = data3.nextSibling
        if len(data4) > 2:
            data4 = data4.replace(" on ","").replace(" -","")
            mlist3.append(data4)
            for each in data2:
                j = str(each)
                h = j.find("id=")
                k = j[h+9:h+15]
                mlist2.append("https://www.ozbargain.com.au/node/"+k)
                try:
                    data3 = data3.findNext("strong")                      
                    data4 = data3.nextSibling
                    data4 = data4.replace(" on ","").replace(" -","")
                    if len(data4) > 6: 
                        mlist3.append(data4)
                except:
                    pass
        else:
            return
    except:
        driver.close()
        print(now,'- Error Ozbargain')
    
    while not p == len(mlist3):
        datetime.datetime_object = datetime.datetime.strptime(mlist3[p], '%d/%m/%Y %H:%M ')
        datetime.datetime_object = datetime.datetime_object - datetime.timedelta(hours=2)
        harry= datetime.datetime.now()
        barry = (harry - datetime.datetime_object) / 60
        ldate.append(barry.seconds)
        p=p+1
    while not e == len(ldate):
        while start11==1:
            print(now, '- waiting for ozbargain to post')
            time.sleep(60)
        if ldate[e] > 1:
            if int(mlist[e]) / ldate[e] > .0001:
                if int(mlist[e]) > 100:
                    oz2=(mlist2[e]+" - With "+mlist[e]+"Votes")
                    with open('oz.txt', 'a+') as writer:
                         writer.seek(0)
                         oztxt=writer.read()
                         if mlist2[e] in oztxt:
                             pass
                         else:
                             r = "\n"+ mlist2[e]
                             writer.write(r)
                             print(now,'-',mlist2[e])
                             driver.get(mlist2[e])
                             title2 = driver.title
                             title = title2.replace("OzBargain","")
                             oz2= (title+oz2)
                             oz2= oz2.replace("https://","")
                             start11=1
                             time.sleep(5)
        e=e+1
    driver.close()
def loopoz():
    global start11
    time.sleep(2)
    getoz()
    getoz2()
    timer4 = threading.Timer(600, loopoz).start()    

def fullloop():
    global delay,whatsappmsg,final,i,firstdate,firstbans,datein,firstusers,firstwunits,firstpoints,firstwunits2,firstpoints2,firstdate2,total,whatsappmsg2,start,hcomsec,hnano,hbanano,xe,nano,banano,comsec,btc,hbtc,start9
    getuser()
    getaccounts()
    getnanos()
    #getether()
    #loop()  #banano loops
    #lastdate()
    #loop2()
    assets()
    final = int(sum(datein))
    finaltotal=int(sum(total))
    if finaltotal > 100 :
        with open('banano.txt', 'w') as f:
            f.write(str(finaltotal))
    else:
        with open('banano.txt') as ff:
            b1 = ff.readline()
            finaltotal = int(b1)
    with open('nano.txt') as ff:
        b2 = ff.readline()
    with open('ether.txt') as ff:
        b30 = float(ff.readline())
    b4 = float(b2)
    b3 = int(b4)
    b5= float(b4-721)
    b6 = int(b5)
    ether = round(b30,2)
    ethertotal = int(ether * nano)  
    bananototal= int(finaltotal*banano)
    nanototal= int(float("3803") * nano)
    nanototal2= int(float(b5) * nano)
    vitetotal= int(float("1625625") * vite)
    rose1= float(rose * .1)
    if rose > 1:
        rosetotal= int(float("2795") * rose1)
    else:
        rosetotal= int(float("279500000") * rose1)
    audether=int(ethertotal * xe)
    audrose= int(rosetotal * xe)
    audvite= int(vitetotal * xe)
    audbanano= int(bananototal * xe)
    audnano= int(nanototal * xe)
    audnano2= int(nanototal2 * xe)
    comsectotal=int(float("42000") * comsec)
    viteprofit= audvite - int(2036)
    roseprofit= audrose - int(2450)
    mastertotal= int(audbanano+audnano+comsectotal+audnano2+audvite+audrose+audether)
    profit = mastertotal - int(40000)
    if roseprofit > 0:
        rosepro = 'Pro: *$'
    else:
        rosepro = 'Loss: *$'
    if viteprofit > 0:
        vitepro = 'Pro: *$'
    else:
        vitepro = 'Loss: *$'
    if profit > 0:
        pro = 'Profit: *$'
    else:
        pro = 'Loss: *$'
    today = datetime.datetime.now()
    dnow = today.strftime('%d/%m/%Y %p')
    try:
        if jim == dnow:
            whatsappmsg1 = str(jim)+" - "+str(u)+"/"+str(len(users))+" earned "+str(final)+" BAN\n"
        else:
            whatsappmsg1 = ""
    except:
        whatsappmsg1 = ""
    whatsappmsg2 = "3803 NANO at $"+str(nano)+" = $"+str(nanototal)+" (AUD = $"+str(audnano)+")\n"+str(b6)+" NANO at $"+str(nano)+" = $"+str(nanototal2)+" (AUD = $"+str(audnano2)+")\n"+str(ether)+" NANO at $"\
                   +str(nano)+" = $"+str(ethertotal)+" (AUD = $"+str(audether)+")\n"+str(finaltotal)+" BAN at $"+str(banano)+" = $"+str(bananototal)+" (AUD = $"+str(audbanano)+")\n"\
                   "162M SHI at $"+str(vite)+" = (AUD = $"+str(audvite)+") - "+str(vitepro)+str(viteprofit)+"*\n"\
                   "28M FLO at $"+str(rose)+" = (AUD = $"+str(audrose)+") - "+str(rosepro)+str(roseprofit)+"*\n"\
                   "42000 JNO at $"+str(comsec)+" = $"+str(comsectotal)+"\nTotal AUD = $"+str(mastertotal)+" - "+str(pro)+str(profit)+"*\nRams = $"+str(rams)  
    whatsappmsg = whatsappmsg1 + whatsappmsg2
    start9 = 1                                                                                                                                                                 
    date, firstdate,firstbans,datein,firstusers,firstwunits,firstpoints,firstwunits2,firstpoints2,firstdate2,total= [],[],[],[],[],[],[],[],[],[],[]
    i=0
    workouttime()
    timer1 = threading.Timer(delay, fullactive).start()
    tradeloop()

def fullactive():
    global start
    start = 1

def zmq():
    global start2,start8,s1,start13
    while True:
        message = socket.recv()
        time.sleep(1)
        socket.send(b"Recieved")
        if message == b"Blueiris":            
            start8=1
        if message == b"cryptobot":
            print("cryptobot")
            start13=1
        if message == b"monoff":            
            monoff()
            print(now,'turning monitor off')
        if message == b"monon":            
            monon()
            print(now,'turning monitor on')
        if message == b"pic":            
            s1 = 1
            print(now,'- New pic of the day Initiated From menu')
                    
def tradeloop():
    global vite,hvite,rose,hrose,r1,wb,stop,now,now3,start4,start5,start6,bi,final,firstdate,firstbans,datein,firstusers,firstwunits,firstpoints,firstwunits2,firstpoints2,firstdate2,total,hcomsec,hnano,hbanano,xe,nano,banano,comsec,wcomsec,wbanano,wnano,stop,wbtc,btc,hbtc    
    getrose()
    getnano()
    getvite()
    time.sleep(1)
    now2 = datetime.datetime.now()
    now = (now2.strftime("%d-%m-%Y %H:%M"))
    now3 = (now2.strftime("%d/%m/%Y"))
    if stop == 2:
        r1=r1+1
        if r1 > 10:
            os.system("shutdown /r /t 0")
            time.sleep(20)
        stop=0
        print(now,'- Bot stopped attempting to restart')
        timer0 = threading.Timer(.001, whatsappbot).start()
    if wb == 700:
        wb=0
        stop=1
        print(now,'- Bot stopping')
    if nano < hnano*.95 or nano > hnano*1.05:
        wnano= "Nano has changed from $"+str(hnano)+" to $"+str(nano)
        hnano=nano
        start4=1
    if vite < hvite*.97 or vite > hvite*1.03:
        wnano= "Vite has changed from $"+str(hvite)+" to $"+str(vite)
        hvite=vite
        start4=1
    if rose < hrose*.90 or rose > hrose*1.10:
        wnano= "Floki has changed from $"+str(hrose)+" to $"+str(rose)
        hrose=rose
        start4=1
        
    getbtc()
    time.sleep(1)
    if btc < hbtc*.988 or btc> hbtc*1.012:
        wbtc= "Bitcoin has changed from $"+str(hbtc)+" to $"+str(btc)
        hbtc=btc
        start5=1
        
    bi=bi+1
    if bi ==120:
        cullovertime()
        getbanano()
        getxe()
        time.sleep(1)
        bi=0
        try:
             if banano < hbanano*.8 or banano> hbanano*1.2:
                wbanano= "Banano has changed from $"+str(hbanano)+" to $"+str(banano)
                hbanano=banano
                start6=1
        except:
            pass
        time.sleep(3)
        if delaycom < 21600:
             try:
                getcomsec()
                time.sleep(1)
                if comsec < hcomsec*.98 or comsec > hcomsec*1.02:
                    wcomsec= "JNO has changed from $"+str(hcomsec)+" to $"+str(comsec)
                    hcomsec=comsec
                    start7=1
             except:
                print(now, 'get comsec failed')
                pass
    wb=wb+1
    timer3 = threading.Timer(30, tradeloop).start()    

startup()
timer9 = threading.Timer(1, getnanos).start()
timer11 = threading.Timer(tuesday, ing).start()
timer9 = threading.Timer(.001, assets).start()
timer7 = threading.Timer(.001, newran).start()
timer0 = threading.Timer(.002, whatsappbot).start()
timer1 = threading.Timer(delay, fullactive).start()
timer2 = threading.Timer(delaycom, comstart).start()
timer4 = threading.Timer(90, loopoz).start()
timer5 = threading.Timer(delayran, newran2).start()
timer3 = threading.Timer(0.001, tradeloop).start()
timer8 = threading.Timer(1, zmq).start()
timer21 = threading.Timer(delayres, restart).start()







 


















