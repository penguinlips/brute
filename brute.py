from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(200)
driver.get("file:///home/anonymous/Desktop/login/login-page.html")

user = driver.find_element_by_id("uname")
psw = driver.find_element_by_id("pass")
sub = driver.find_element_by_id("ok")
clr = driver.find_element_by_id("clear")
file = open("pass.txt")
while True:
    line = file.readline()
    if not line:
        break
    user.send_keys("keralacybermentor")
    psw.send_keys(line)
    sub.click()
    clr.click()
file.close()
