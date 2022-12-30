import time
import allure

from base.selenium_driver import SeleniumDriver
from testcases.message import *
from testcases.locators import *


class CreateAPP(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Click on the add application button")
    def click_add_application_button(self):
        self.wait_for_element(click_add_application_button)
        self.element_click(click_add_application_button)

    @allure.step("Verify on the close icon of new app creation flow")
    def click_close_icon(self):
        self.element_click(application_close_icon)

    @allure.step("Click on the generate button to generate the address")
    def click_generate_button(self):
        self.wait_for_element(click_generate_button)
        self.element_click(click_generate_button)

    # unable when select option available in the front end.
    # def select_ecdsa_option(self):
    #     self.element_click(authenticate_with_ECDSA)

    # def select_authentic_token(self):
    #     self.element_click(authenticate_with_access_token)

    @allure.step("Enter internal app name")
    def enter_internal_app_name(self, internal_app_name):
        self.wait_for_element(enter_internal_app_name)
        self.element_click(enter_internal_app_name)
        self.send_keys(clear_field, enter_internal_app_name)
        self.send_keys(internal_app_name, enter_internal_app_name)

    @allure.step("Enter Public app name")
    def enter_public_app_name(self, public_app_name):
        self.wait_for_element(enter_public_app_name)
        self.element_click(enter_public_app_name)
        self.send_keys(clear_field, enter_public_app_name)
        self.send_keys(public_app_name, enter_public_app_name)

    @allure.step("Enter app handle")
    def enter_app_handle(self, handle_name):
        self.wait_for_element(enter_app_handle_name)
        self.element_click(enter_app_handle_name)
        self.send_keys(clear_field, enter_app_handle_name)
        self.send_keys(handle_name, enter_app_handle_name)

    @allure.step("Create app flow")
    def create_app_flow(self, internal_app_name, public_app_name, handle_name):
        self.click_add_application_button()
        self.enter_internal_app_name(internal_app_name)
        self.enter_public_app_name(public_app_name)
        self.element_click(click_submit_button)
        self.enter_app_handle(handle_name)
        self.element_click(click_submit_button)

    @allure.step("Create ECDSA APP")
    def create_ecdsa_app(self):
        # self.select_ecdsa_option()  # this feature is removed in console 2.13 release.
        self.click_generate_button()
        self.element_click(click_submit_button)
        self.element_click(confirm_and_download_button)

    @allure.step("Create JWT App")
    def create_access_token_app(self):
        # self.select_authentic_token()   # this feature is removed in console 2.13 release.
        self.element_click(click_submit_button)

    @allure.step("Click on the edit button to edit the app")
    def click_edit_button(self):
        self.wait_for_element(edit_button)
        self.element_click(edit_button)

    @allure.step("Update app handle")
    def enter_updated_app_handle(self, updated_handle_name):
        self.wait_for_element(update_app_handle_field)
        self.element_click(update_app_handle_field)
        self.send_keys(clear_field, update_app_handle_field)
        self.send_keys(updated_handle_name, update_app_handle_field)

    @allure.step("Delete the app")
    def click_delete_button(self):
        self.wait_for_element(delete_app_button)
        self.element_click(delete_app_button)

    @allure.step("Enter Current password to update the app details.")
    def enter_current_password(self, enter_current_pass):
        self.wait_for_element(enter_current_password)
        self.element_click(enter_current_password)
        self.send_keys(enter_current_pass, enter_current_password)

    @allure.step("Click on the cancel button to cancel the edit on the app.")
    def click_edit_app_cancel(self):
        self.element_click(edit_app_cancel_button)

    # Assertions::
    @allure.step("Verify link open in new tab :: " + REDIRECTED_SECURITY_LINK_HEADING)
    def verify_security_link_open_new_tab(self):
        self.element_click(navigate_application_screen_link)
        self.wait_for_element(click_security_req_link)
        self.link_redirect(locator=click_security_req_link, locator1=security_link_new_tab_heading,
                           expected_text=REDIRECTED_SECURITY_LINK_HEADING)

    @allure.step("Verify link open in new tab :: " + REDIRECTED_HOSTED_API_LINK_HEADING)
    def verify_hosted_api_link_open_new_tab(self):
        self.link_redirect(locator=click_hosted_api_link, locator1=hosted_api_new_tab_heading,
                           expected_text=REDIRECTED_HOSTED_API_LINK_HEADING)

    @allure.step("Verify clicking on the add application should open the app creation flow")
    def verify_clicking_add_application(self):
        self.click_add_application_button()
        self.is_element_present(internal_app_name_field)
        self.is_element_present(public_facing_app_name_field)

    @allure.step("Verify clicking on the close icon close the app creation flow")
    def verify_clicking_close_icon(self):
        self.click_close_icon()
        self.is_element_displayed(click_add_application_button)

    @allure.step("Verify app handle validations")
    def verify_app_handle_field_validations(self, message):
        """
        :param message: it should be either min or special characters
        """
        self.wait_for_element(click_alert_icon)
        self.element_click(click_alert_icon)
        text = self.get_text(get_validation_message)
        if message == "min":
            self.verify_text_match(text, MIN_3_CHARACTERS_REQUIRED)
        elif message == "special_characters":
            self.verify_text_match(text, SPECIAL_CHARACTER_VALIDATION)
        else:
            self.verify_text_match(text, HANDLE_EXISTS)

    @allure.step("Verify app creation successfully.")
    def verify_app_created(self, process, app_handle_name):
        """
        :param process: it will be either JWT OR ecdsa
        :param app_handle_name: new app created name
        """
        if process == "ecdsa":
            self.wait_for_element(check_app_handle_name)
            text = self.get_text(check_app_handle_name)
            self.verify_text_contains(text, app_handle_name)
        elif process == "jwt":
            self.wait_for_element(check_app_handle_name)
            text = self.get_text(check_app_handle_name)
            self.verify_text_match(text, app_handle_name)

    @allure.step("Verify disable button should disable the app")
    def verify_disable_app(self):
        time.sleep(5)
        self.element_click(disable_button)
        self.wait_for_element(app_disabled_text)
        text = self.get_text(app_disabled_text)
        self.verify_text_match(text, DISABLE_TEXT)

    @allure.step("Verify clicking on the enable button, enables the app")
    def verify_enable_app(self):
        time.sleep(5)
        self.element_click(disable_button)
        text = self.get_text(disable_button)
        self.verify_text_match(text, "Disable")

    @allure.step("Verify app handle updated successfully :: " + APP_UPDATED_MESSAGE)
    def verify_update_app_handle(self, updated_handle_name):
        self.click_edit_button()
        self.enter_updated_app_handle(updated_handle_name)
        time.sleep(5)
        self.element_click(click_submit_button)
        text = self.get_text(get_alert_message)
        self.verify_text_match(text, APP_UPDATED_MESSAGE)

    @allure.step("Verify ETH address update successfully")
    def verify_update_eth_address(self, process=""):
        self.click_edit_button()
        # self.wait_for_element(click_generate_button)
        # self.element_click(click_generate_button)
        if process == "ecdsa":
            self.create_ecdsa_app()
            time.sleep(5)
            text = self.get_text(get_alert_message)
            self.verify_text_match(text, APP_UPDATED_MESSAGE)
        else:
            self.enter_current_password(enter_current_pass="")
            self.wait_for_element(regenerate_confirm_button)
            self.element_click(regenerate_confirm_button)
            text = self.get_text(get_alert_message)
            self.verify_text_match(text, JWT_APP_UPDATED_MESSAGE)

    @allure.step("Verify app deleted successfully :: " + APP_DELETED_MESSAGE)
    def verify_app_deleted(self):
        self.click_edit_button()
        self.click_delete_button()
        self.element_click(confirm_delete_button)
        time.sleep(5)
        text = self.get_text(get_alert_message)
        self.verify_text_contains(text, APP_DELETED_MESSAGE)
