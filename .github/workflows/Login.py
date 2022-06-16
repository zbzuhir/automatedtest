from selenium.webdriver.common.keys import Keys
import Driver

def login():
    Driver.driver.get('https://vhsmartqsrtest.azurewebsites.net/') # Go to VH Smart website login
    Driver.driver.fullscreen_window()
    try:
        username_box = Driver.driver.find_element_by_xpath('//*[@id="Input_Email"]')
        password_box = Driver.driver.find_element_by_xpath('//*[@id="Input_Password"]')

        username = "admin@qsrbrands.com.my"
        password = "p@ssw0rd1234"

        # 1. Login into VH SMART
        username_box.send_keys(username)
        password_box.send_keys(password)
        password_box.send_keys(Keys.ENTER)

        print('TEST PASSED! Able to login to VH Smart')
    except Exception as e:
        print('TEST FAILED! Unable to login to VH Smart. Error', e)
