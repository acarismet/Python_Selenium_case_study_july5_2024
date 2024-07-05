import os
from time import sleep
import pytest
import pyperclip
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages import page_1_login
from utilities import Driver
from utilities import Constants as const
from utilities import ConfigReader as cr
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class TestProfile:

    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_1_login.LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def click_element(self, element):
        """
        Some elements unexpectedly accept a click pattern that other elements don't and
        don't allow to execute the other pattern, so this method will solve this problem in one line.
        Attempts to click on the given element. If the conventional click fails,
        Performs a click operation with JavaScript.

        To call:
        self.click_element(element)
        """
        try:
            element.click()
            print("Element clicked successfully.")
        except NoSuchElementException:
            print("Element not found.")
        except WebDriverException as e:
            print(f"Normal click failed: {e}. JavaScript will try clicking.")
            try:
                self.driver.execute_script("arguments[0].click()", element)
                print("Clicking with JavaScript was successful.")
            except Exception as js_e:
                print(f"The JavaScript click also failed: {js_e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_new_url(self):
        self.new_url = self.driver.current_url
        print(self.new_url)

    def login(self):
        self.page.login_info()
        # self.page.email.send_keys(const.valid_email)
        self.page.password.send_keys(const.valid_password)
        self.page.submit_button()
        self.driver.execute_script("arguments[0].click();", self.page.login_button)

    def close_all_campaign_pop_ups(self):

        try:
            self.page.find_campaign_pop_up_x()
            self.click_element(self.page.campaign_pop_x)
        except (TimeoutException, NoSuchElementException):
            pass

        try:
            self.page.find_campaign_pop_up_skip()
            self.click_element(self.page.campaign_pop_skip)
            try:
                self.page.find_campaign_pop_up_confirm_skip()
                self.click_element(self.page.campaign_pop_confirm_skip)
            except (TimeoutException, NoSuchElementException):
                pass
        except (TimeoutException, NoSuchElementException):
            pass

    def navigate_safes_pages(self):
        self.login()
        sleep(1)
        self.page.find_side_menu_money()
        self.click_element(self.page.side_menu_money)
        sleep(1)
        self.page.find_side_menu_safes()
        self.click_element(self.page.side_menu_safes)

    def navigate_main_safe_edit(self):
        self.navigate_safes_pages()
        self.page.find_edit_main_safe_button()
        self.click_element(self.page.edit_main_safe_button)
        sleep(3)

    def selecting_currency(self): # Website doesn't allow to change it for safe opening. So try this for other edits
        self.page.find_dropdown_main_safe_currency()
        self.click_element(self.page.dropdown_main_safe_currency)
        self.page.find_usd_option_dropdown_main_safe()
        self.click_element(self.page.usd_option_dropdown_main_safe)

    def enter_main_safe_balance(self):
        self.page.find_input_opening_main_safe_balance()
        self.page.input_opening_main_safe_balance.send_keys(const.main_safe_opening_balance)

    def test_successful_login(self):
        self.login()
        sleep(2)
        Driver.screenshot(self.driver, "../screenshots/screenshots_1_login", "test_1_1_login_success.png")
        self.close_all_campaign_pop_ups()
        sleep(4)
        Driver.screenshot(self.driver, "../screenshots/screenshots_1_login", "test_1_2_login_success.png")
        self.get_new_url()
        assert self.new_url == const.url_main_page, "Login Failed"
        print("Login Successful")

    def test_successful_first_edit_main_safe(self):
        self.navigate_main_safe_edit()
        sleep(1)
        Driver.screenshot(self.driver, "../screenshots/screenshots_1_login", "test_2_1_edit_safe_success.png")
        sleep(1)
        self.enter_main_safe_balance()
        sleep(3)
        Driver.screenshot(self.driver, "../screenshots/screenshots_1_login", "test_2_2_edit_safe_success.png")
        self.page.find_button_submit_main_safe_edit()
        self.click_element(self.page.button_submit_main_safe_edit)
        sleep(3)
        Driver.screenshot(self.driver, "../screenshots/screenshots_1_login", "test_2_3_edit_safe_success.png")
        self.page.find_td_main_safe_balance_amount()
        assert self.page.td_main_safe_balance_amount == const.main_safe_opening_balance, "Amounts matching failed"
        print("Balance amounts matched successfully")

