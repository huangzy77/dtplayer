# coding = utf-8

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.ssegou.com/page/testss.html')

print driver.page_source

driver.quit()