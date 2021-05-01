# Authod: Kgyya
# Gitcrod: github.com/Kgyya
# Repo: github.com/Kgyya/sms
"""
Join Us:
t.me/tempatconfig
t.me/bebas_berinternet
"""



# pip install mechanize
# pip install requests
# pip install bs4
from bs4 import BeautifulSoup as bs
import mechanize
import datetime
import time
import sys
import os

waktu = datetime.datetime.now()
banner = """  ██████  ███▄ ▄███▓  ██████ 
▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒  
░ ▓██▄   ▓██    ▓██░░ ▓██▄   
  ▒   ██▒▒██    ▒██   ▒   ██▒
▒██████▒▒▒██▒   ░██▒▒██████▒▒
▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░ github.com/Kgyya
░  ░  ░  ░      ░   ░  ░  ░  
      ░         ░         ░  [V.1.0]"""
def sprint(s):
 for x in s + "\n":
  sys.stdout.write(x)
  sys.stdout.flush()
  time.sleep(00.09)

def mechan_wangy(kont,mmk):
 browser = mechanize.Browser()
 browser.set_handle_equiv(True)
 browser.set_handle_gzip(True)
 browser.set_handle_redirect(True)
 browser.set_handle_referer(True)
 browser.set_handle_robots(False)
 browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
 browser.addheaders=[('Connection','keep-alive'),('Pragma','no-cache'),('Cache-Control','no-cache'),('Origin','http://sms.payuterus.biz'),('Upgrade-Insecure-Requests','1'),('Content-Type','application/x-www-form-urlencoded'),('User-Agent','Opera/9.80 (Android; Opera Mini/8.0.1807/36.1609; U; en) Presto/2.12.423 Version/12.16'),('Accept','text/html,application/xhtml+xml,application/signed-exchange;v=b3'),('Referer','http://sms.payuterus.biz/alpha/'),('Accept-Encoding','gzip, deflate'),('Accept-Language','id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),('Cookie','_ga=GA1.2.131924726.1560439960; PHPSESSID=jjrqqaakmfcgfgbtjt8tve5595; _gid=GA1.2.1969561921.1561024035; _gat=1')]
 r = "https://sms.payuterus.biz/alpha/"
 l = []
 soup = bs(browser.open(r),features="html.parser")
 for y in soup.find_all("span"):
  l.append(y.text)
 cap = int(str(l)[2])+int(str(l)[6])
 browser.select_form(nr=0)
 browser.form["nohp"]=kont
 browser.form["pesan"]=mmk
 browser.form["captcha"]=str(cap)
 submit = browser.submit().read()
 if "SMS Gratis Telah Dikirim" in str(submit):
  print("\n\t[SUCCESS] > "+str(kont))
 elif "Mohon Tunggu" in str(submit):
  print("\n\t[WAITING] > "+str(kont))
 else:
  print("\n\t[ERROR] > "+str(kont))

def send():
 os.system("clear")
 time.sleep(1)
 print(banner) # Anjay So Ingris
 print("\n\tOnly Works In Indonesian Phone Numbers")
 print("\n\tGunakan Awalan 08xxxxxxxx")
 no = input("\tInput No      > ")
 print("\t[TIPS] Add '\\n' To Write New Lines.")
 mes = input("\tInput Message > ")
 sprint("\tProccessing...!")
 time.sleep(2)
 mechan_wangy(no,mes)
send()
