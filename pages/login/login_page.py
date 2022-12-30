import time

import pytest
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver
from testcases.message import *
from utilities.util import *
from testcases.locators import *


@pytest.mark.run(order=1)
class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utility = Util()

    @allure.step("Get login page heading")
    def get_login_page_text(self):
        self.wait_for_element(get_login_page_heading)
        return self.get_text(get_login_page_heading)

    @allure.step("Enter user handle")
    def enter_email(self, user_handle):
        self.wait_for_element(email_field)
        self.element_click(email_field)
        self.send_keys(clear_field, email_field)
        self.send_keys(user_handle, email_field)

    @allure.step("Enter password")
    def enter_password(self, user_password):
        self.wait_for_element(password_field)
        self.element_click(password_field)
        self.send_keys(clear_field, password_field)
        self.send_keys(user_password, password_field)

    @allure.step("Click login button")
    def click_login_button(self):
        self.wait_for_element(click_login_button)
        self.web_scroll('down')
        self.element_click(click_login_button)

    # Method
    @allure.description("Verify Login Flow")
    def login(self, user_handle, user_password):
        time.sleep(3)
        self.enter_email(user_handle)
        self.enter_password(user_password)
        self.click_login_button()

    # Assertions
    @allure.link("https://sila.testrail.io/index.php?/suites/view/31&group_by=cases:section_id&group_order=asc"
                 "&display_deleted_cases=0&group_id=400")
    def verify_login_field_displayed(self):
        self.wait_for_element(email_field)
        self.is_element_displayed(email_field)

    @allure.step("verify password field present on the login screen")
    def verify_password_field_displayed(self):
        self.is_element_displayed(password_field)

    @allure.step("verify forgot password link present on the login screen")
    def verify_forgot_password_link_displayed(self):
        self.is_element_displayed(click_forgot_password_link)

    @allure.step("verify sign up link present on the login screen")
    def verify_sign_up_link_displayed(self):
        self.is_element_displayed(sign_up_link)

    @allure.step("verify user lands on login screen:: " + LOGIN_PAGE_HEADING)
    def verify_login_page(self):
        get_text = self.get_login_page_text()
        self.verify_text_match(get_text, LOGIN_PAGE_HEADING)

    @allure.step("Verify login button disable")
    def verify_login_button_disable(self):
        element = self.get_element(click_login_button)
        print(element.is_enabled())
        assert element.is_enabled() is False, ("Login Button is not disabled " + click_login_button)

    @allure.step("Verify not able to login with invalid credentials:: " + INVALID_LOGIN_MESSAGE)
    def verify_validation_with_invalid_credentials(self):
        get_text = self.get_text(get_alert_message)
        self.verify_text_contains(get_text, INVALID_LOGIN_MESSAGE)

    def verify_empty_handle_validation(self):
        get_text = self.get_text(get_validation_message)
        self.verify_text_contains(get_text, EMPTY_USER_NAME)

    def verify_empty_password_validation(self):
        get_text = self.get_text(get_validation_message)
        self.verify_text_contains(get_text, EMPTY_PASSWORD_MESSAGE)

    def verify_user_handle_min_length_validation(self):
        get_text = self.get_text(get_validation_message)
        self.verify_text_contains(get_text, SPECIAL_CHARACTER_VALIDATION)

    @allure.step("Verify user navigates to MFA screen:: " + MFA_PAGE_TITLE)
    def verify_login_successfully(self):
        time.sleep(10)
        page_title = self.get_title()
        self.verify_text_match(page_title, MFA_PAGE_TITLE)

    @allure.step("Verify validation when enter invalid MFA code")
    def verify_invalid_mfa_code(self, invalid_code):
        self.wait_for_element(enter_mfa_code)
        self.send_keys(invalid_code, enter_mfa_code)

    @allure.step("Verify resend code link resend the new code:: "+ RESEND_CODE_MESSAGE)
    def verify_resend_code_link(self):
        self.wait_for_element(click_resend_code_link)
        self.element_click(click_resend_code_link)
        get_text = self.get_text(enter_invalid_error)
        self.verify_text_match(get_text, RESEND_CODE_MESSAGE)

    @allure.step("Verify MFA Message")
    def verify_messages(self, message_name):
        """
        type> message_name: invalid_code, resend_code
        """
        if message_name == "invalid_code":
            self.element_click(click_submit_button)
            self.wait_for_element(enter_invalid_error)
            get_text = self.get_text(enter_invalid_error)
            self.verify_text_match(get_text, INVALID_CODE_MESSAGE)
        elif message_name == "resend_code":
            time.sleep(5)
            self.element_click(click_resend_code_link)
            time.sleep(5)
            get_text = self.get_text(enter_invalid_error)
            self.verify_text_match(get_text, RESEND_CODE_MESSAGE)

    @allure.step("Verify entering valida mfa, navigates user to remember screen:: "+ REMEMBER_SCREEN_HEADING)
    def verify_valid_mfa(self):
        time.sleep(15)
        get_code = self.get_mfa_code("silaqaautomation")
        self.element_click(enter_mfa_code)
        self.send_keys(get_code, enter_mfa_code)
        self.element_click(click_submit_button)
        self.wait_for_element(get_remember_screen_heading)
        get_text = self.get_text(get_remember_screen_heading)
        self.verify_text_match(get_text, REMEMBER_SCREEN_HEADING)

    @allure.step("Verify selecting remember me navigates user to home screen:: " + WELCOME_SCREEN_HEADING)
    def verify_remember_me(self):
        self.element_click(click_remember_me_on_device)
        self.element_click(click_continue_button)
        get_text = self.get_text(get_welcome_screen_heading)
        self.verify_text_match(get_text, WELCOME_SCREEN_HEADING)
        time.sleep(2)

    #
    # def getUserNameValidationMessage(self):
    #     self.wait_for_element(self._username_field_validation_icon, 'css')
    #     self.element_click(self._username_field_validation_icon, 'css')
    #     time.sleep(1)
    #     return self.get_text(self._username_min_character_validation_message)
    #
    # def getPasswordEmptyFieldText(self):
    #     self.wait_for_element(self._password_field_validation_icon, 'css')
    #     self.element_click(self._password_field_validation_icon, 'css')
    #     return self.get_text(self._password_empty_field_validation)
    #
    # def getInvalidUserNameOrPasswordErrorMessage(self):
    #     self.wait_for_element(self._flex_error_message, 'css')
    #     return self.get_text(self._flex_error_message, 'css')

    # def clickForgotPasswordPageCancelButton(self):
    #     self.wait_for_element(self._forgot_password_page_cancel_button)
    #     self.element_click(self._forgot_password_page_cancel_button)
    #
    # def clickForgotPasswordLink(self):
    #     self.wait_for_element(self._forgot_password_link)
    #     self.element_click(self._forgot_password_link)

