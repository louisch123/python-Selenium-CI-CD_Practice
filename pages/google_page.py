from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class GooglePage(BasePage):
    SEARCH_BOX = (By.NAME, "q")

    def search(self, text):
        box = self.driver.find_element(*self.SEARCH_BOX)
        box.send_keys(text)
        box.submit()