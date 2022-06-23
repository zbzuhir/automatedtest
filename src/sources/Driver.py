from optparse import Option
from ssl import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

global driver
#driver = webdriver.Chrome('/Users/nurkhairunnisa.alies/Serunai/VH Smart/Automation/chromedriver/chromedriver')
s = Service('/Users/Asus/Downloads/Folder/chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
