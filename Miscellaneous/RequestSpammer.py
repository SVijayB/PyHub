# Spam rogue requests to a webpage to test how well it can handle multiple requests. Add in more threads for faster testing.

from selenium import webdriver
import time
from threading import Thread


def one():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="D:\chromedriver", options=chrome_options)

    for i in range(200):
        driver.get("https://www.google.com/")
    print("Done")


t1 = Thread(target=one).start()
t2 = Thread(target=one).start()
