
# import os,sys
#
# current_directory = os.path.dirname(os.path.abspath(__file__))
#
# root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
#
# sys.path.append(root_path)


from selenium import webdriver
import time

# import sys,os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)


driver = webdriver.Chrome()
driver.get('gy1yinhe.fftechs.com:2086')
driver.maximize_window()
time.sleep(5)
driver.quit()