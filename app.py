from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from userInfo import *
from time import sleep
import pyfiglet

def banner():
    result = pyfiglet.figlet_format("ERN AKKC")   
    os.system('cls')
    print( "\033[92m"+result +"\n\nBuradan işlemleri takip etmeyi unutmayınız !!") 


driver_path = Service(driver_path)
app = webdriver.Chrome(service=driver_path)
banner()


app.get("https://www.instagram.com")
sleep(3)


banner()
try:
    usernameInput = app.find_element(By.NAME, "username")
    passwordInput = app.find_element(By.NAME, "password")
    usernameInput.send_keys(username)
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.ENTER)
    app.find_element(By.XPATH, "(//div[@role='button'])[1]").click()
    app.find_element(By.XPATH, " //button[contains(text(),'Şimdi Değil')]").click()
except:
    pass
a = '\033[96m'+ "Giriş başarıyla tamamlandı... \033[92m"
print(a)

sleep(5)

banner()
print(a)
# Hesaba git
takipKAdi = str(input("Takipçilerini takip etmek istediğiniz instagram hesabını başında '@' olmadan giriniz:  "))
takipSayi = int(input("Kaç hesabı takip etmek istiyorsunuz:   "))
app.get(f"https://instagram.com/{takipKAdi}/followers/")

sleep(5)


print('\033[96m' + "Kullanıcı adları çekiliyor lütfen bekleyiniz." + "\033[92m")
# Takipçiler
action = webdriver.ActionChains(app)
for _ in range(takipSayi*5):
    action.key_down(Keys.TAB).key_up(Keys.TAB).perform()
    sleep(0.2)
fallowers = app.find_element(*(By.XPATH,"(//div[@class='x1ja2u2z x1afcbsf x1a2a7pz x6ikm8r x10wlt62 x71s49j x6s0dn4 x78zum5 xdt5ytf xl56j7k x1n2onr6'])[1]"))
fusernames = fallowers.find_elements(*(By.XPATH,"(//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x6s0dn4 xozqiw3 x1q0g3np'])"))
fallowers = []
for i in fusernames:
    fallowers.append(str(i.text))
liste = []
fallowers.pop(0)
for i in fallowers:
    liste.append(i.split('\n')[0])
while len(liste) > takipSayi:
    liste.pop(0)
print("\033[94m Takipçilerin kullanıcı adları çekildi\nTakip etme işlemi başlıyor...\nHer takip edilen kişinin hesap linki aşağıda verilecektir...")
# Takipçi k.adları çekildi.

for kullanıcı in liste:
    link = f"https://instagram.com/{kullanıcı}"
    print(link)
    app.get(link)
    sleep(3)
    app.find_element(By.XPATH,"(//button[@type='button'])[1]").click()
    sleep(10)

print('\033[93m'+"İŞLEM TAMAMLANDI !")
