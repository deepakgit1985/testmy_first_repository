import time
import allure

from base.selenium_driver import SeleniumDriver
from testcases.locators import *
from testcases.message import *


class LogoutPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Get logout model box title")
    def get_popup_title(self):
        self.wait_for_element(popup_title)
        return self.get_text(popup_title)

    @allure.step("Get logout model box text")
    def get_popup_text(self):
        self.wait_for_element(popup_text)
        return self.get_text(popup_text)

    # def click_popup_close_icon(self):
    #     time.sleep(5)
    #     self.wait_for_element(logout_model_close_icon)
    #     self.element_click(logout_model_close_icon)

    @allure.step("Click on the model box cancel button")
    def click_popup_cancel_button(self):
        time.sleep(2)
        self.wait_for_element(logout_popup_cancel_button)
        self.element_click(logout_popup_cancel_button)

    @allure.step("Click on the logout link from home screen menu")
    def click_logout_link_from_home_menu(self):
        self.element_click(click_user_menu)
        time.sleep(5)
        self.wait_for_element(menu_logout_link)
        self.element_click(menu_logout_link)

    @allure.step("Click on the model box logout button")
    def click_popup_logout_button(self):
        self.wait_for_element(logout_button)
        self.element_click(logout_button)

    @allure.step("Logout flow")
    def logout(self):
        self.click_logout_link_from_home_menu()
        self.click_popup_logout_button()

    # Assertions
    @allure.step("Validate logout model box Title:: " + LOGOUT_POPUP_TITLE)
    def verify_logout_popup_title(self):
        self.click_logout_link_from_home_menu()
        text = self.get_popup_title()
        self.verify_text_match(text, LOGOUT_POPUP_TITLE)

    @allure.step("Validate logout model box Text:: " + LOGOUT_POPUP_TEXT)
    def verify_logout_popup_text(self):
        text = self.get_popup_text()
        self.verify_text_match(text, LOGOUT_POPUP_TEXT)

    # def verify_close_icon_close_popup(self):
    #     self.click_popup_close_icon()
    #     get_text = self.get_text(get_welcome_screen_heading)
    #     self.verify_text_match(get_text, WELCOME_SCREEN_HEADING)

    @allure.step("Validate cancel button navigates back to home screen")
    def verify_cancel_button_close_popup(self):
        # self.click_logout_link_from_home_menu()
        self.click_popup_cancel_button()

    @allure.step("Validate user logout successfully:: " + LOGIN_PAGE_HEADING)
    def verify_logout_flow(self):
        self.logout()
        time.sleep(5)
        text = self.get_text(get_login_page_heading)
        self.verify_text_match(text, LOGIN_PAGE_HEADING)
