from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
driver_path = r"E:\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://www.baidu.com/')
# input_tag = driver.find_element_by_id('kw')

# input_tag = driver.find_element_by_xpath('//input[@id="kw"]')
#
# submit_tag = driver.find_element_by_xpath('//input[@id="su"]')
#
# for cookie in driver.get_cookies():
#     print(cookie)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'su'))
)
submitButton = driver.find_element_by_id('su')
print(type(submitButton))
driver.close()
