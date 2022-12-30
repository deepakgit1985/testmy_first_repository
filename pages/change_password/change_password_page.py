import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver
from testcases.message import *
from utilities.util import *
from testcases.locators import *


class Change_Password_Page(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utility = Util()

    def click_to_profile(self):
        self.wait_for_element(Profile_icon)
        self.element_click(Profile_icon)
        time.sleep(5)
        self.element_click(change_password_dropdown)
        time.sleep(2)
        get_change_password_text = self.get_text(change_password_screen_heading)
        self.verify_text_match(get_change_password_text, change_password_screen_title)

    def set_password_disable_check(self):
        self.check_element_state(locator=set_password_button, element_name=set_password_button)

    def set_password_enable_check(self):
        self.check_element_state(locator=set_password_button, element_name=set_password_button, value=True)

    def click_to_cancel(self):
        time.sleep(2)
        self.click_to_profile()
        time.sleep(2)
        self.element_click(cancel_button)
        time.sleep(2)
        home_page_title = self.get_title()
        self.verify_text_match(home_page_title, HOME_SCREEN_TITLE)
        time.sleep(5)

    def Wrong_current_password(self, password):
        self.send_keys(password, current_password_text_field)
        self.element_click(change_password_screen_heading)
        # self.keyboard_tab()
        time.sleep(2)
        current_password_actual_text = self.driver.execute_script("return document.getElementById('setPasswordForm.currentPassword').getAttribute('error');")
        self.verify_text_match(current_password_actual_text, current_password_error_message)
        self.set_password_disable_check()
        time.sleep(3)

    def enter_password_less_than_8_characters(self, PASSWORD, LESS_THAN_8_CHARACTERS):
        self.send_keys(clear_field, current_password_text_field)
        time.sleep(2)
        self.send_keys(PASSWORD, current_password_text_field)
        time.sleep(2)
        self.send_keys(clear_field, password_text_field)
        self.send_keys(LESS_THAN_8_CHARACTERS, password_text_field)
        time.sleep(2)
        Password_less_than_8_char_text = self.driver.execute_script("return document.getElementById('setPasswordForm.password').getAttribute('error');")
        self.verify_text_match(Password_less_than_8_char_text, password_less_than_8_char_error_message)
        self.set_password_disable_check()
        time.sleep(10)

    def blank_current_password_validation(self):
        self.wait_for_element(current_password_text_field)
        self.element_click(current_password_text_field)
        self.element_click(change_password_screen_heading)
        current_password_actual_text = self.driver.execute_script("return document.getElementById('setPasswordForm.currentPassword').getAttribute('error');")
        self.verify_text_match(current_password_actual_text, blank_current_password_error_message)
        self.set_password_disable_check()

    def blank_password_validation(self):
        self.wait_for_element(password_text_field)
        self.element_click(password_text_field)
        self.element_click(change_password_screen_heading)
        current_password_actual_text = self.driver.execute_script("return document.getElementById('setPasswordForm.password').getAttribute('error');")
        self.verify_text_match(current_password_actual_text, blank_password_error_message)
        self.set_password_disable_check()

    def blank_retype_password_validation(self):
        self.wait_for_element(retype_password_text_field)
        self.element_click(retype_password_text_field)
        self.element_click(change_password_screen_heading)
        current_password_actual_text = self.driver.execute_script("return document.getElementById('setPasswordForm.confirmPassword').getAttribute('error');")
        self.verify_text_match(current_password_actual_text, blank_retype_error_message)
        self.set_password_disable_check()

    def wrong_confirm_password(self,currentpassword, password, confirmpassword):
        self.send_keys(clear_field, current_password_text_field)
        self.send_keys(currentpassword, current_password_text_field)
        self.send_keys(clear_field, password_text_field)
        self.send_keys(password, password_text_field)
        self.send_keys(clear_field, retype_password_text_field)
        self.send_keys(confirmpassword, retype_password_text_field)
        current_password_actual_text = self.driver.execute_script("return document.getElementById('setPasswordForm.confirmPassword').getAttribute('error');")
        self.verify_text_match(current_password_actual_text, wrong_retype_error_message)
        self.set_password_disable_check()

    def verify_change_password_successfully(self, currentpassword, password, confirmpassword):
        self.send_keys(clear_field, current_password_text_field)
        self.send_keys(currentpassword, current_password_text_field)
        self.send_keys(clear_field, password_text_field)
        self.send_keys(password, password_text_field)
        self.send_keys(clear_field, retype_password_text_field)
        self.send_keys(confirmpassword, retype_password_text_field)
        self.element_click(set_password_button)
        time.sleep(2)
        home_page_title = self.get_title()
        self.verify_text_match(home_page_title, HOME_SCREEN_TITLE)








