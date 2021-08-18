import time, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
#import datetime
import pymysql
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime

def scroll_page_down():
    for x in range(5):
        time.sleep(random.randrange(1, 5, 1))
        jsCode = "var q=document.documentElement.scrollTop=100000"
        browser.execute_script(jsCode)
def db_open():
    # insert your own db address
    return ""
    
def login_facebook(usr,pwd):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-notifications")
    options.add_argument('--disable-gpu')
#    options.add_argument('--proxy-server={}'.format(proxy))
#    options.add_argument("user-agent={}".format(ua))
    global browser
#    browser = webdriver.Chrome('/usr/local/bin/chromedriver',options=options)
    browser = webdriver.Chrome("chrome_driver/chromedriver")
    browser.get("http://www.facebook.org")
    assert "Facebook" in browser.title
    elem = browser.find_element_by_name("email")
#    elem = browser.find_element_by_id("email")
    elem.send_keys(usr)
    elem = browser.find_element_by_name("pass")
    elem.send_keys(pwd)
    
    elem.send_keys(Keys.RETURN)
    
    WebDriverWait(browser,5)
    WebDriverWait(browser, 5)

def browse_state_page(url,table_name):
    db_open()
    browser.get(url)
    html = (browser.page_source).encode('utf-8')
    yahoo_soup = BeautifulSoup(html, 'html.parser')
    PUSH_NUM = ""
    FOLLOW_NUM =""
    for ya_s in yahoo_soup.findAll("div",{"class":"_1xnd"}):
    	for spare in ya_s.findAll("div",{"class":"_2pi9 _2pi2"}):
    		for str_ps in spare.findAll("div"):
    			if str_ps.get_text().find("人說這讚") != - 1 :
    				print("讚： " + str_ps.get_text())
    				str_push = str_ps.get_text().replace("人說這讚","")
    				PUSH_NUM = str_push.replace(" ","")
    				PUSH_NUM = str_push.replace(",","")
    			if str_ps.get_text().find("人在追蹤此地標") != - 1 :
    				print("讚： " + str_ps.get_text())
    				str_push = str_ps.get_text().replace("人在追蹤此地標","")
    				FLSTR = str_push.replace(" ","")
    				FLSTR = str_push.replace(",","")
    				FOLLOW_NUM = FLSTR
    UPDATETIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    state_list = [PUSH_NUM,FOLLOW_NUM,UPDATETIME]
    cursor.execute("INSERT INTO " + table_name + "(PUSH_NUM,FOLLOW_NUM,DT) VALUES(%s,%s,%s) ",state_list)
    db.commit()
    db.close()
    
def browse_post_page(url,article_name):
    browser.get(url)
    time.sleep(1)
    ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    scroll_page_down()
    time.sleep(random.randrange(1, 3, 1))
    
    html = (browser.page_source).encode('utf-8')
    global fb_soup, pieces
    fb_soup = BeautifulSoup(html, 'html.parser')
    pieces = fb_soup.findAll("div", {"class": "_5pcr userContentWrapper"})
    for piece in pieces:
        top = piece.find("div", {"class": "v_ymowr4dzu f_ymowq-b_j clearfix"})
        time_info = top.find("abbr", {"class": "_5ptz"})
        po_ppl_info = top.find("a", {"class": "profileLink"})
        global DT
        DT = time_info['title']
        dateFormatter = '%Y/%m/%d %H:%M'
        if '上午' in DT:
            DT = DT.replace("上午","")
            if len(DT) == 13:
                DT = datetime.strptime(DT, dateFormatter)
                print(DT)
            elif len(DT) == 14:
                if int(DT[-5:-3]) == 12:
                    change = int(DT[-5:-3]) - 12
                    DT = DT[:-5] + str(change) + DT[-3:]
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
                else:
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
            elif len(DT) == 15:
                if int(DT[-5:-3]) == 12:
                    change = int(DT[-5:-3]) - 12
                    DT = DT[:-5] + str(change) + DT[-3:]
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
                else:
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
            elif len(DT) == 16:
                if int(DT[-5:-3]) == 12:
                    change = int(DT[-5:-3]) - 12
                    DT = DT[:-5] + str(change) + DT[-3:]
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
                else:
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)            
        elif '下午' in DT:
            DT = DT.replace("下午","")
            if len(DT) == 13:
                change = int(DT[-5:-3]) + 12
                DT = DT[:-4] + str(change) + DT[-3:]
                DT = datetime.strptime(DT, dateFormatter)
                print(DT)
            elif len(DT) == 14:
                if DT[-5:-3] == "12":
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
                elif DT[-5:-3] == "11" or DT[-5:-3] == "10":
                    change = int(DT[-5:-3]) + 12
                    DT = DT[:-5] + str(change) + DT[-3:]
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
                else:
                    change = int(DT[-4:-3]) + 12
                    DT = DT[:-4] + str(change) + DT[-3:]
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
            elif len(DT) == 15:
                if DT[-5:-3] == "12":
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
                elif DT[-5:-3] == "11" or DT[-5:-3] == "10":
                    change = int(DT[-5:-3]) + 12
                    DT = DT[:-5] + str(change) + DT[-3:]
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
                else:
                    change = int(DT[-4:-3]) + 12
                    DT = DT[:-4] + str(change) + DT[-3:]
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
            elif len(DT) == 16:
                if DT[-5:-3] == "12":
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
                elif DT[-5:-3] == "11" or DT[-5:-3] == "10":
                    change = int(DT[-5:-3]) + 12
                    DT = DT[:-5] + str(change) + DT[-3:]
                    DT = datetime.strptime(DT, dateFormatter)
                    print(DT)
    #    print(DT)
        global URL
        URL = time_info['data-utime']
        global FROM_URL
        try:    
            FROM_URL = po_ppl_info['href']
        except:
            po_ppl_info = top.find('a')
            FROM_URL = po_ppl_info['href']
            
        
        global CONTEXT
        CONTEXT = ""
        for middle in piece.findAll("div", {"class": "_5pbx userContent _3576"}):
            CONTEXT = middle.text
            print(CONTEXT)
        for middle in piece.findAll("div", {"class": "_5pbx userContent _3ds9 _3576"}):
            CONTEXT = middle.text
            print(CONTEXT)
        for middle in piece.findAll("div", {"class": "_yd0 _5pbx userContent _3577"}):
            CONTEXT = middle.text
            print(CONTEXT)
        if CONTEXT == "":
            for share_post_content in piece.findAll("div", {"class": "mtm _5pco"}):
                CONTEXT = share_post_content.text
                print(CONTEXT)
            for share_post_content in piece.findAll("div", {"class": "mtm _5pco _2zpv"}):
                CONTEXT = share_post_content.find("p")
                CONTEXT = CONTEXT.text
                print(CONTEXT)
    
        
        for bottom in piece.findAll("form", {"class": "commentable_item"}):
            # 留言數與分享數 + PUSH_URL
            msg_share_info = bottom.find("div", {"class": "_4vn1"})
            print(msg_share_info)
            
            global PUSH_NUM, SHARE_NUM, PUSH_URL
            
            # 如果 (沒留言 and 沒分享)
            if msg_share_info == None:
                print("沒留言也沒分享")
                PUSH_NUM,SHARE_NUM = 0,0
                PUSH_URL= ""
            else:
                print("有留言或有分享")
                try:
                    msg_info = msg_share_info.find("a", {"class": "_3hg- _42ft"})
                    PUSH_NUM = msg_info.text
                    PUSH_NUM = PUSH_NUM.strip(' 則留言')
                    PUSH_NUM = int(PUSH_NUM.replace(',',''))
                    print(PUSH_NUM)
                    PUSH_URL = msg_info['href']
                    print(PUSH_URL)
                except:
                    PUSH_NUM = 0
                    PUSH_URL = ""
                    print(PUSH_NUM)
                    print(PUSH_URL)
                    
                try:
                    share_info = msg_share_info.find("a", {"class": "_3rwx _42ft"})
                    SHARE_NUM = share_info.text
                    SHARE_NUM = SHARE_NUM.strip('次分享')
                    SHARE_NUM = int(SHARE_NUM.replace(',',''))
                    print(SHARE_NUM)
                except:
                    SHARE_NUM = 0
                    print(SHARE_NUM)
                
    #            -------------------
                
                
            # 鄉民留言
            comments_info = bottom.find("ul", {"class": "_7791"})
            try:
                print("留言區: ")
                for comments in comments_info.findAll("span", {"class": "_3l3x"}):
                    global COMMENT
                    COMMENT = comments.text
                    print(COMMENT)
            except AttributeError:
                print("AttributeError")
    
    
    
            # 總讚數
            global PUSH_TAG_ALL,PUSH_TAG1,PUSH_TAG2,PUSH_TAG3,PUSH_TAG4,PUSH_TAG5,PUSH_TAG6
            PUSH_TAG1,PUSH_TAG2,PUSH_TAG3,PUSH_TAG4,PUSH_TAG5,PUSH_TAG6 = 0,0,0,0,0,0
            PUSH_TAG_ALL = 0
            
            likes_info = bottom.find("div", {"class": "_66lg"})
            try:
                total_like = likes_info.find("span", {"class": "_3dlh"})
                PUSH_TAG_ALL = total_like.text
                PUSH_TAG_ALL = PUSH_TAG_ALL.replace(',','')
                PUSH_TAG_ALL = PUSH_TAG_ALL.replace('萬','')
                PUSH_TAG_ALL = PUSH_TAG_ALL.replace(u"\xa0",'')
                if "." in PUSH_TAG_ALL:
                    PUSH_TAG_ALL = PUSH_TAG_ALL.replace('.', '')
                    PUSH_TAG_ALL = PUSH_TAG_ALL + "000"
                    PUSH_TAG_ALL = int(PUSH_TAG_ALL)
                else:
                    PUSH_TAG_ALL = int(PUSH_TAG_ALL)
                print(PUSH_TAG_ALL)                
            except:
                PUSH_TAG_ALL = 0
                print(PUSH_TAG_ALL)
            
           
            if PUSH_TAG_ALL != 0:
                #分別讚數
                for at in likes_info.findAll("a", {"class": "_1n9l"}):
                    if '讚' in at['aria-label']:
                        PUSH_TAG1 = at['aria-label'][:-1]
                        PUSH_TAG1 = PUSH_TAG1.replace(',','')
                        PUSH_TAG1 = PUSH_TAG1.replace('萬','')
                        PUSH_TAG1 = PUSH_TAG1.replace(u"\xa0","")
                        if "." in PUSH_TAG1:
                            PUSH_TAG1 = PUSH_TAG1.replace('.', '')
                            PUSH_TAG1 = PUSH_TAG1 + "000"
                            PUSH_TAG1 = int(PUSH_TAG1)
                        else:
                            PUSH_TAG1 = int(PUSH_TAG1)
                        print(str(PUSH_TAG1) + '讚')
                    if '大心' in at['aria-label']:
                        PUSH_TAG2 = at['aria-label'][:-2]
                        PUSH_TAG2 = PUSH_TAG2.replace(',','')
                        PUSH_TAG2 = PUSH_TAG2.replace('萬','')
                        PUSH_TAG2 = PUSH_TAG2.replace(u"\xa0",'')
                        if "." in PUSH_TAG2:
                            PUSH_TAG2 = PUSH_TAG2.replace('.', '')
                            PUSH_TAG2 = PUSH_TAG2 + "000"
                            PUSH_TAG2 = int(PUSH_TAG2)
                        else:
                            PUSH_TAG2 = int(PUSH_TAG2)
                        print(str(PUSH_TAG2) + '大心')
                    if '哈' in at['aria-label']:
                        PUSH_TAG3 = at['aria-label'][:-1]
                        PUSH_TAG3 = PUSH_TAG3.replace(',','')
                        PUSH_TAG3 = PUSH_TAG3.replace('萬','')
                        PUSH_TAG3 = PUSH_TAG3.replace(u"\xa0",'')
                        if "." in PUSH_TAG3:
                            PUSH_TAG3 = PUSH_TAG3.replace('.', '')
                            PUSH_TAG3 = PUSH_TAG3 + "000"
                            PUSH_TAG3 = int(PUSH_TAG3)
                        else:
                            PUSH_TAG3 = int(PUSH_TAG3)
                        print(str(PUSH_TAG3) + '哈')
                    if '哇' in at['aria-label']:
                        PUSH_TAG4 = at['aria-label'][:-1]
                        PUSH_TAG4 = PUSH_TAG4.replace(',','')
                        PUSH_TAG4 = PUSH_TAG4.replace('萬','')
                        PUSH_TAG4 = PUSH_TAG4.replace(u"\xa0",'')
                        if "." in PUSH_TAG4:
                            PUSH_TAG4 = PUSH_TAG4.replace('.', '')
                            PUSH_TAG4 = PUSH_TAG4 + "000"
                            PUSH_TAG4 = int(PUSH_TAG4)
                        else:
                            PUSH_TAG4 = int(PUSH_TAG4)
                        print(str(PUSH_TAG4) + '哇')
                    if '嗚' in at['aria-label']:
                        PUSH_TAG5 = at['aria-label'][:-1]
                        PUSH_TAG5 = PUSH_TAG5.replace(',','')
                        PUSH_TAG5 = PUSH_TAG5.replace('萬','')
                        PUSH_TAG5 = PUSH_TAG5.replace(u"\xa0",'')
                        if "." in PUSH_TAG5:
                            PUSH_TAG5 = PUSH_TAG5.replace('.', '')
                            PUSH_TAG5 = PUSH_TAG5 + "000"
                            PUSH_TAG5 = int(PUSH_TAG5)
                        else:
                            PUSH_TAG5 = int(PUSH_TAG5)
                        print(str(PUSH_TAG5) + '嗚')
                    if '怒' in at['aria-label']:
                        PUSH_TAG6 = at['aria-label'][:-1]
                        PUSH_TAG6 = PUSH_TAG6.replace(',','')
                        PUSH_TAG6 = PUSH_TAG6.replace('萬','')
                        PUSH_TAG6 = PUSH_TAG6.replace(u"\xa0",'')
                        if "." in PUSH_TAG6:
                            PUSH_TAG6 = PUSH_TAG6.replace('.', '')
                            PUSH_TAG6 = PUSH_TAG6 + "000"
                            PUSH_TAG6 = int(PUSH_TAG6)
                        else:
                            PUSH_TAG6 = int(PUSH_TAG6)
                        print(str(PUSH_TAG6) + '怒')
        db_open()
        
        UPDATETIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        str_list = [CONTEXT,UPDATETIME,PUSH_TAG1,PUSH_TAG2,PUSH_TAG3,PUSH_TAG4,PUSH_TAG5,PUSH_TAG6,PUSH_TAG_ALL,PUSH_NUM,SHARE_NUM,URL,PUSH_URL,DT,FROM_URL]
        print(str_list)
        cursor.execute("INSERT INTO " + article_name + "(CONTEXT,UPDATETIME,PUSH_TAG1,PUSH_TAG2,PUSH_TAG3,PUSH_TAG4,PUSH_TAG5,PUSH_TAG6,PUSH_TAG_ALL,PUSH_NUM,SHARE_NUM,URL,PUSH_URL,DT,FROM_URL) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",str_list)
        db.commit()
        db.close()
#    browser.quit()
    
def close_browser():
    browser.quit()
    
    
    
    
    
    
    
    