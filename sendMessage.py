from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 1000)
print("Waiting done...")

target = ' '

x_arg = '//span[@title="' + target + '"][@dir="auto"]'

friend = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
try:
    driver.find_element_by_xpath(x_arg).click()
    print("Found")
except NoSuchElementException:
    print("Not found")

inp_xpath = '//div[@class="selectable-text"][@data-tab="1"]'

try:
    driver.find_element_by_class_name("selectable-text")
    print("Found")
except NoSuchElementException:
    print("Not found")

n = 0
multiline_msg = ''' '''
lines = multiline_msg.split("\n")
for i in range(len(lines)):
    string = lines[n]
    input_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for letter in string:
        time.sleep(random.uniform(0, 2))
        input_box.send_keys(letter)
    input_box.send_keys(Keys.RETURN)
    n = n + 1
    time.sleep(1)
