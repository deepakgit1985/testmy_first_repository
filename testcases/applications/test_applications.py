import unittest
import pytest
import allure

from utilities.util import *
from pages.applications.application_page import CreateAPP
from testcases.test_config import *


@allure.parent_suite('Console Automation')
@allure.suite("Applications")
@pytest.mark.run(order=2)
class Applications(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.app = CreateAPP(self.driver)

    def test_001_click_security_requirements_external_link_sanity(self):
        """Verify clicking on the link open the url in the new tab."""
        self.app.verify_security_link_open_new_tab()

    def test_002_click_hosted_api_external_link(self):
        """Verify clicking on the link open the url in the new tab."""
        self.app.verify_hosted_api_link_open_new_tab()

    def test_003_click_add_application_button(self):
        """Verify add application button is clickable."""
        self.app.verify_clicking_add_application()

    def test_004_click_close_icon(self):
        """Verify clicking on the close icon close the model box"""
        self.app.verify_clicking_close_icon()

    def test_005_app_handle_min_charc_validation(self):
        """Verify app handle field return validation error when enter less than 3 characters"""
        self.app.create_app_flow(INTERNAL_APP_NAME, PUBLIC_APP_NAME, HANDLE_NAME_LESS_THAN_3_CHAR)
        self.app.verify_app_handle_field_validations(message="min")
        self.app.click_close_icon()

    def test_006_app_handle_special_char_validation(self):
        """Verify app handle field return validation error when enter less than special characters"""
        self.app.create_app_flow(INTERNAL_APP_NAME, PUBLIC_APP_NAME, HANDLE_NAME_SPECIAL_CHAR)
        self.app.verify_app_handle_field_validations(message="special_characters")
        self.app.click_close_icon()

    def test_007_create_ecdsa_app_sanity(self):
        """Verify user is able to create an app."""
        self.app.create_app_flow(INTERNAL_APP_NAME, PUBLIC_APP_NAME, APP_NAME)
        self.app.create_ecdsa_app()
        self.app.verify_app_created(process="ecdsa", app_handle_name=APP_NAME)

    def test_008_app_disable_functionality(self):
        """Verify user is able to disable the app"""
        self.app.verify_disable_app()

    def test_009_app_enable_functionality(self):
        """Verify user is able to enable the app"""
        self.app.verify_enable_app()

    def test_010_update_app_handle_min_charc_validation(self):
        """Verify user is not able to update the handle when characters are less than 3."""
        self.app.click_edit_button()
        self.app.enter_updated_app_handle(updated_handle_name=HANDLE_NAME_LESS_THAN_3_CHAR)
        self.app.verify_app_handle_field_validations(message="min")

    def test_011_update_app_handle_special_char_validation(self):
        """Verify user is not able to update the handle when characters are less than 3."""
        self.app.enter_updated_app_handle(updated_handle_name=HANDLE_NAME_SPECIAL_CHAR)
        self.app.verify_app_handle_field_validations(message="special_characters")

    def test_012_update_app_handle_sanity(self):
        """Verify user is able to update the app handle successfully."""
        self.app.click_edit_app_cancel()
        self.app.verify_update_app_handle(UPDATED_APP_NAME)

    def test_013_update_ecdsa_eth_address_sanity(self):
        """Verify user is able to generate new address"""
        self.app.verify_update_eth_address(process="ecdsa")
    #
    # def test_014_create_jwt_app(self):
    #     """Verify user is able to create a JWT App."""
    #     self.app.create_app_flow(INTERNAL_APP_NAME, PUBLIC_APP_NAME, HANDLE_NAME)
    #     self.app.create_access_token_app()
    #     self.app.verify_app_created(process="jwt", app_handle_name=APP_NAME)
    #
    # def test_015_update_jwt_app(self):
    #     """"""
    #     self.app.verify_update_eth_address()

    def test_016_delete_app_successfully_sanity(self):
        """Verify user is able to delete the app successfully."""
        self.app.verify_app_deleted()


