import time

import pytest
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage


# combined
class TestSearchByFilter:
    @pytest.mark.filter
    def test_filter_by_name(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        search_name = driver.find_elements(By.TAG_NAME, value="Option")
        time.sleep(2)

        search_name[1].click()
        time.sleep(5)

    @pytest.mark.filter
    def test_filter_by_price(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.execute_login("standard_user", "secret_sauce")

        search_name = driver.find_elements(By.TAG_NAME, value="Option")
        time.sleep(2)

        search_name[2].click()
        time.sleep(5)
