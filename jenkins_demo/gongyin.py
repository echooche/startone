from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('gy1yinhe.fftechs.com:2086')
driver.maximize_window()
time.sleep(5)
driver.quit()