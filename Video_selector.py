from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os

browser = webdriver.Firefox()
browser.get('https://www.youtube.com/results?search_query=sreeragamo')

print("You are accessing :",browser.title)


thumbnail_element = browser.find_elements_by_id("thumbnail")
first = thumbnail_element[0]
first.send_keys(Keys.RETURN)

views = browser.find_elements_by_tag_name(" views")
print(views)