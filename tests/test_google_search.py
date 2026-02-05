from utils.driver_factory import create_driver
from pages.google_page import GooglePage

def test_google_search():
    driver = create_driver()
    page = GooglePage(driver)

    page.open("https://www.google.com")
    page.search("Selenium Python")

    assert "Selenium" in driver.title

    driver.quit()