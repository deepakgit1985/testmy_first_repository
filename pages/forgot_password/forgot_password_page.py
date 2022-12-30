import time
import allure

from base.selenium_driver import SeleniumDriver
from pages.register.register_page import RegisterPage
from pages.login.login_page import LoginPage
from testcases.message import *
from testcases.locators import *


class ForgotPassword(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.register = RegisterPage(driver)
        self.login = LoginPage(driver)

    @allure.step("Get Forgot password screen heading")
    def get_forgot_password_screen_heading(self):
        self.wait_for_element(get_forgot_password_heading)
        return self.get_text(get_forgot_password_heading)

    @allure.step("Get validation text when email field is empty")
    def get_empty_email_validation(self):
        self.wait_for_element(email_field_validation_icon)
        self.element_click(email_field_validation_icon)
        return self.get_text(email_address_required_validation_message)

    @allure.step("Enter email")
    def enter_email(self, email):
        self.wait_for_element(user_email_field)
        self.element_click(user_email_field)
        self.send_keys(clear_field, user_email_field)
        self.send_keys(email, user_email_field)

    @allure.step("Click on the forgot password link")
    def click_forgot_password_link(self):
        self.wait_for_element(click_forgot_password_link)
        self.element_click(click_forgot_password_link)

    @allure.step("Enter new password")
    def enter_new_password(self, enter_new_password):
        self.wait_for_element(new_password_field)
        self.element_click(new_password_field)
        self.send_keys(clear_field, new_password_field)
        self.send_keys(enter_new_password, new_password_field)

    @allure.step("Enter retype password")
    def enter_retype_new_password(self, retype_new_password):
        self.wait_for_element(retype_new_password_field)
        self.element_click(retype_new_password_field)
        self.send_keys(clear_field, retype_new_password_field)
        self.send_keys(retype_new_password, retype_new_password_field)

    @allure.step("Click on the reset button")
    def click_reset_button(self):
        self.element_click(click_reset_button)

    # Method
    @allure.step("Verify forgot password flow.")
    def forgot_password(self, email):
        self.enter_email(email)
        self.element_click(click_submit_button)

    @allure.step("Set new password")
    def set_new_password(self, enter_new_password, retype_new_password):
        self.enter_new_password(enter_new_password)
        self.enter_retype_new_password(retype_new_password)
        self.click_reset_button()

    @allure.step("Get new reset link from the gmail")
    def get_link(self, name=""):
        time.sleep(15)
        get_reset_link = self.verify_email_confirmation(name=name, flow="reset_password")
        self.driver.get(get_reset_link)

    # Assertions
    @allure.step("Verify Forgot password screen heading:: " + FP_HEADING)
    def verify_fp_heading(self):
        self.click_forgot_password_link()
        page_heading = self.get_forgot_password_screen_heading()
        self.verify_text_match(page_heading, FP_HEADING)

    @allure.step("Verify clicking on the cancel button navigates user to home screen")
    def verify_clicking_cancel_button(self):
        self.wait_for_element(click_cancel_button)
        self.element_click(click_cancel_button)
        self.login.verify_login_page()

    @allure.step("Verify forgot password screen contains email field.")
    def verify_email_field_present(self):
        self.element_click(click_forgot_password_link)
        self.wait_for_element(user_email_field)
        self.is_element_displayed(user_email_field)

    @allure.step("Verify user gets an error when email field is empty:: " + EMAIL_ADDRESS_REQUIRED_MESSAGE)
    def verify_validation_when_email_empty(self):
        self.element_click(user_email_field)
        time.sleep(1)
        self.element_click(get_forgot_password_heading)
        text = self.get_empty_email_validation()
        self.verify_text_match(text, EMAIL_ADDRESS_REQUIRED_MESSAGE)

    @allure.step("Verify user gets an error when email field is invalid")
    def verify_invalid_email_validation(self, email):
        self.element_click(user_email_field)
        self.forgot_password(email)
        self.register.verify_email_validation_message(email_type="invalid")

    @allure.step("Verify user is able to forgot password successfully:: " + FP_EMAIL_SENT)
    def verify_forgot_password_successfully(self, email):
        self.element_click(user_email_field)
        self.forgot_password(email)
        time.sleep(2)
        get_text = self.get_text(fp_email_sent_successfully)
        self.verify_text_contains(get_text, FP_EMAIL_SENT)

    @allure.step("Verify user gets an email on email :: " + NEW_PASSWORD_HEADING)
    def verify_fp_email_received(self):
        self.wait_for_element(get_new_password_heading)
        get_heading = self.get_text(get_new_password_heading)
        self.verify_text_match(get_heading, NEW_PASSWORD_HEADING)

    @allure.step("Verify reset button disable after resetting the password")
    def verify_reset_button_disable(self):
        self.wait_for_element(click_reset_button)
        self.check_element_state(click_reset_button, element_name="click_reset_button")

    @allure.step("Verify cancel button")
    def verify_cancel_button_functionality(self):
        self.element_click(click_cancel_button)
        self.verify_fp_heading()

    @allure.step("Verify password update message :: " + PASSWORD_UPDATED_MESSAGE)
    def verify_password_updated_message(self):
        get_message = self.get_text(get_alert_message)
        self.verify_text_contains(get_message, PASSWORD_UPDATED_MESSAGE)

    @allure.step("Verify link should be expired once password reset:: " + LINK_EXPIRED_MESSAGE)
    def verify_link_expires_after_resetting_password(self):
        time.sleep(2)
        get_message = self.get_text(get_alert_message)
        self.verify_text_contains(get_message, LINK_EXPIRED_MESSAGE)

