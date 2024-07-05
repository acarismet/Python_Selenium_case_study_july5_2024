from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities import Driver


class LoginPage:
    # Login page elements
    email = None
    password = None
    login_button = None

    # Main page elements

        # Pop closing elements
    campaign_pop_x = None
    campaign_pop_skip = None
    campaign_pop_confirm_skip = None

        # Annual Summary Cash Flow table headers
    header_first_in_annual_cash_flow = None  # Gelirlerim ve Varlıklarım
    header_second__in_annual_cash_flow = None  # Ödemelerim
    header_third_in_annual_cash_flow = None  # Toplam Nakit Akışı

        # side menu elements
    side_menu_overview = None  # Genel Bakış
    side_menu_sales = None  # Satışlar
    side_menu_acquisitions = None  # Alışlar
    side_menu_expenses = None  # Giderler
    side_menu_money = None  # Para
    side_menu_cash_status = None  # Nakit Durumu
    side_menu_safes = None  # Kasalar

    # safes page elements
    edit_main_safe_button = None  # Merkez Kasa Edit Butonu

        # main safe edit elements
    input_main_safe_name = None
    dropdown_main_safe_currency = None
    usd_option_dropdown_main_safe = None
    input_opening_main_safe_balance = None
    input_opening_main_safe_date = None
    button_submit_main_safe_edit = None

        # main safe table elements
    td_main_safe_balance_amount = None
    td_main_safe_balance_currency = None



    def __init__(self, driver):
        self.driver = driver

    def login_info(self):
        self.email = Driver.wait(self.driver, By.XPATH, "//input[@name=\"email\"]")
        self.password = Driver.wait(self.driver, By.XPATH, '//input[@name="password"]', "click", 5)

    def submit_button(self):
        self.login_button = Driver.wait(self.driver, By.XPATH, '//button[@id="m_login_signin_submit"]', "click", 50)

    def find_campaign_pop_up_x(self):
        self.campaign_pop_x = Driver.wait(self.driver, By.XPATH, '/html/body/div[5]/div/button', "click", 5)

    def find_campaign_pop_up_skip(self):
        self.campaign_pop_skip = Driver.wait(self.driver, By.XPATH, '/html/body/div[6]/div/div[10]/button[2]', "click", 5)

    def find_campaign_pop_up_confirm_skip(self):
        self.campaign_pop_confirm_skip = Driver.wait(self.driver, By.XPATH, '/html/body/div[7]/div/div[10]/button[1]', "click", 5)

    def find_first_header_in_annual_cash_flow(self):
        self.header_first_in_annual_cash_flow = Driver.wait(self.driver, By.XPATH, '//*[@id="trIncomeAssets"]/td[1]', "click", 5)

    def find_second_header_in_annual_cash_flow(self):
        self.header_second__in_annual_cash_flow = Driver.wait(self.driver, By.XPATH, '//*[@id="trPayment"]/td[1]', "click", 5)

    def find_third_header_in_annual_cash_flow(self):
        self.header_third_in_annual_cash_flow = Driver.wait(self.driver, By.XPATH, '//*[@id="cashFlow"]/table/tbody/tr[23]/td[1]', "click", 5)

    def find_side_menu_overview(self):
        self.side_menu_overview = Driver.wait(self.driver, By.XPATH, '//*[@id="dashboard"]/span', "click", 5)

    def find_side_menu_sales(self):
        self.side_menu_sales = Driver.wait(self.driver, By.XPATH, '//*[@id="m_5c931df8509159455a8a136e"]/a/h4', "click", 5)

    def find_side_menu_acquisitions(self):
        self.side_menu_acquisitions = Driver.wait(self.driver, By.XPATH, '//*[@id="m_5d48339fa89bd919aa541b29"]/a/h4', "click", 5)

    def find_side_menu_expenses(self):
        self.side_menu_expenses = Driver.wait(self.driver, By.XPATH, '//*[@id="m_5bfcfe64a8212551671f9062"]/a/span', "click", 5)

    def find_side_menu_money(self):
        self.side_menu_money = Driver.wait(self.driver, By.XPATH, '//*[@id="m_5bfcfe64a8212551671f9066"]/a/h4', "click", 5)

    def find_side_menu_cash_status(self):
        self.side_menu_cash_status = Driver.wait(self.driver, By.XPATH, '//*[@id="m_5bfcffaca8212551671f9069"]/a/span', "click", 10)

    def find_side_menu_safes(self):
        self.side_menu_safes = Driver.wait(self.driver, By.XPATH, "//span[contains(.,'Kasalar')]", "click", 10)

    def find_edit_main_safe_button(self):
        self.edit_main_safe_button = Driver.wait(self.driver, By.XPATH, '//*[@id="safeList"]/div[2]/table/tbody/tr/td[1]/a[1]', "click", 5)

    def find_input_main_safe_name(self):
        self.input_main_safe_name = Driver.wait(self.driver, By.CSS_SELECTOR, "[name='name']", "visit", 5)

    def find_dropdown_main_safe_currency(self):
        self.dropdown_main_safe_currency = Driver.wait(self.driver, By.XPATH, '//*[@id="tabSafeCommon"]/form/div/div[1]/div[2]/div/button', "click", 5)

    def find_usd_option_dropdown_main_safe(self):
        self.usd_option_dropdown_main_safe = Driver.wait(self.driver, By.XPATH, '//*[@id="tabSafeCommon"]/form/div/div[1]/div[2]/div/div/ul/li[2]/a', "click", 5)

    def find_input_opening_main_safe_balance(self):
        self.input_opening_main_safe_balance = Driver.wait(self.driver, By.XPATH, '//*[@id="tabSafeCommon"]/form/div/div[2]/div[1]/span/span/input[1]', "visit", 5)

    def find_input_opening_main_safe_date(self):
        self.input_opening_main_safe_date = Driver.wait(self.driver, By.XPATH, '//*[@id="tabSafeCommon"]/form/div/div[2]/div[1]/span/span/input[1]', "click", 5)

    def find_button_submit_main_safe_edit(self):
        self.button_submit_main_safe_edit = Driver.wait(self.driver, By.XPATH, '//*[@id="safeEditWindow"]/div/div/div[3]/button[2]', "click", 5)

    def find_td_main_safe_balance_amount(self):
        self.td_main_safe_balance_amount = Driver.wait(self.driver, By.XPATH, '//*[@id="safeList"]/div[2]/table/tbody/tr/td[3]/div', "visit", 5).text

    def find_td_main_safe_balance_currency(self):
        self.td_main_safe_balance_currency = Driver.wait(self.driver, By.XPATH, '//*[@id="safeList"]/div[2]/table/tbody/tr/td[4]/div', "visit", 5).text
