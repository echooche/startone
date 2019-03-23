from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def getEle(driver,time,xpath,describe):
    ele =WebDriverWait(driver,time).until(lambda d:driver.find_element_by_xpath(xpath))
    return ele



url = 'http://gy3yinhe.fftechs.com:2086'
username = 'caipiao03'
password = 'caipiao03'


driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# 登陆

login_btn = getEle(driver,10,'//*[@id="header"]/div/div[3]/div[1]/span[2]','登陆')
login_btn.click()

username_inp = getEle(driver,10,'//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[1]/div/input','用户名')
pwd_inp = getEle(driver,10,'//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[2]/div/input','密码')
username_inp.send_keys(username)
pwd_inp.send_keys(password)

instant_login = getEle(driver,10,'//*[@id="content"]/div[2]/div[2]/div/div/div[1]/div/div[3]/div[7]/span','立即登陆')
instant_login.click()

# 点击彩票--通过js方法中的click点击
js = "var  q = document.querySelector('#header > div > div.main-menu > ul > li:nth-child(4) > a').click()"
driver.execute_script(js)


# 滚动界面
# driver.execute_script("window.scrollBy(0,2000)")


# # 时时彩进入游戏
shishi = getEle(driver,20,'//*[@id="lotteryinfo"]/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/span','时时彩进入游戏')
driver.execute_script("arguments[0].scrollIntoView(false);", shishi) #拖动到可见的元素去
assert shishi.text == '进入游戏'
shishi.click()
import time
time.sleep(100)


# driver.quit()