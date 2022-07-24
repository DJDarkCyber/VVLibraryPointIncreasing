#!/usr/bin/env python3

import getpass
import requests
import threading

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

class vvLibraryPointIncreaser:
    def __init__(self):
        print(GREEN)
        print("+--------------------------------------+")
        print("| VV library auto point increasing BOT |")
        print("+--------------------------------------+")
        print(END)
        self.count = 1
        self.url = "http://lib.vvcoe.org/wp-admin/admin-ajax.php"
        self.startMenu()
    def startMenu(self):
        print(CYAN)
        self.userName = str(input("Enter your rollNo   >_ ")).upper()
        self.passWord = str(getpass.getpass("Enter your Password >_ "))
        self.userAPIs = str(input("Enter you API       >_ ")).lower()
        self.rounds   = int(input("Enter number of rounds >_ "))
        print(PURPLE)
        print("[*] Logging in")
        insider_page = requests.get("http://lib.vvcoe.org/wp-login.php")
        login_page_cookies = ""
        for r in insider_page.cookies:
            login_page_cookies += r.name + "=" + r.value + "; "
        login_page_cookies += login_page_cookies[0:len(login_page_cookies)-2]
        login_headers = {
            "POST": "/wp-login.php HTTP/1.1",
            "Host": "lib.vvcoe.org",
            "User-Agent": "Mozilla/6.0 (Linux x86_64) Gecko/20123 Firefox/92",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Content-Length": "80",
            "Origin": "http://lib.vvcoe.org",
            "DNT": "1",
            "Connection": "close",
            "Referer": "http://lib.vvcoe.org/wp-login.php",
            "Cookie": login_page_cookies,
            "Upgrade-Insecure-Requests": "1"
        }
        myData = {
        "log":self.userName,
        "pwd":self.passWord,
        "wp-submit": "Log+in+to+VVLibrary",
        "redirect_to": "",
        "testcookie": "1"
        }
        session = requests.Session()
        logined_page = session.post("http://lib.vvcoe.org/wp-login.php", headers=login_headers, data=myData)
        if "Invalid username" in str(logined_page.content):
            print(RED)
            print("[-] Invalid Username")
            print(END)
            exit()
        if "The password you entered for the username" in str(logined_page.content):
            print(RED)
            print("[-] Invalid Password")
            print(END)
            exit()
        logged_cookies = session.cookies.get_dict()
        
        self.myLoggedCookies = ""

        for heading, value in logged_cookies.items():
            self.myLoggedCookies += heading + "=" + value + "; "
            
        self.myLoggedCookies = self.myLoggedCookies[0:len(self.myLoggedCookies)-2]
        
        self.myHeader = {
            "Host": "lib.vvcoe.org",
            "User-Agent": "Mozilla/6.0 (Linux x86_64) Gecko/20123 Firefox/92",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": "151",
            "Origin": "http://lib.vvcoe.org",
            "Connection": "close",
            "Referer": "http://lib.vvcoe.org/?searchby=title&searchbox&weblib_orderby=barcode&weblib_order=DESC&barcode=BB3336",
            "Cookie": self.myLoggedCookies
        }
        self.myDataCmt = {
            "action" : "new_activity_comment",
            "cookie" : "bp-activity-oldestpage%253D1",
            "_wpnonce_new_activity_comment": self.userAPIs,
            "comment_id" : "44499",
            "form_id" : "44499",
            "content" : "437" ,
        }
        self.reqThread(500, self.rounds)
    def webReq(self):
        try:
            print("\rRequested --> "+str(self.count),end="")
            self.count+=1
            # req = requests.post(self.url, data=self.myDataCmt, headers=self.myHeader, proxies={"http": "http://" + self.proxies[random.randint(0, len(self.proxies)-1)], "https": "https://" + self.proxies[random.randint(0, len(self.proxies)-1)]})
            req = requests.post(self.url, data=self.myDataCmt, headers=self.myHeader)
        except Exception:
            pass
    
    def reqThread(self, threadLen, rounds):
        for i in range(0, rounds):
            threads = list()
            for i in range(0, threadLen):
                x = threading.Thread(target=self.webReq)
                threads.append(x)
                x.start()

            for i, thread in enumerate(threads):
                thread.join()
    
vvLibraryPointIncreaser()
