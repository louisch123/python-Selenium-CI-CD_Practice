from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def create_driver():
    service = Service(r'C:\Users\louis\.wdm\drivers\chromedriver\win64\144.0.7559.133\chromedriver-win32\chromedriver.exe')
    options = webdriver.ChromeOptions()
    # your options here
    driver = webdriver.Chrome(service=service, options=options)
    return driver