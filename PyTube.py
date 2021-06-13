from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os

browser = webdriver.Firefox()
browser.get('https://www.youtube.com')

print("You are accessing :",browser.title)

def menu_fn():
    while True:
        print("\n\t-----------The PyTube----------\n\n1 > Search\n2 > Exit\n")
        try:
            n = int(input("-->"))
        except:
            print("\nSorry, invalid input")
            continue
        if not n in [1,2]:
            print("\nSorry, invalid input")
            continue
        return(n)
 
def search_option_fn():
    while True:
        print("\nSearch >>> ", end='')
        try:
            search_option = input()
        except:
            print("\nSorry, invalid input")
            continue
        return(search_option)

n = menu_fn()

search_bar = browser.find_element_by_name("search_query")

while n == 1:
    while True:
        try:
            search_option = search_option_fn()
            
            search_bar.clear()            
            search_bar.send_keys(search_option)
            search_bar.send_keys(Keys.RETURN)

            n = menu_fn()
        except:         #If the user unexpectedly closed the browser
            print("Sorry, the browser is closed. Restarting...")
            browser = webdriver.Firefox()
            browser.get('https://www.youtube.com')
            continue
else:
    if n == 2:
        browser.quit()
        exit()
    else:
        print("\nSorry, invalid input")
        n = menu_fn()