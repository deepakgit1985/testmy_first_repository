import unittest
import pytest
import allure

from utilities.util import *
from pages.login.login_page import LoginPage
from testcases.test_config import *


@allure.parent_suite('Console Automation')
@allure.suite("Login")
@pytest.mark.run(order=1)
class Login(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTest):
        self.login = LoginPage(self.driver)

    def test_001_handle_field_available(self):
        """Verify handle field is available."""
        self.login.verify_login_field_displayed()

    def test_002_password_field_available(self):
        """Verify password field is available."""
        self.login.verify_password_field_displayed()

    def test_003_forgot_password_field_available(self):
        """Verify forgot password link is available."""
        self.login.verify_forgot_password_link_displayed()

    def test_004_sign_up_link_available(self):
        """Verify signup link is available."""
        self.login.verify_sign_up_link_displayed()

    def test_005_verify_login_button_disable(self):
        """Verify login button disable for the first time."""
        self.login.verify_login_button_disable()

    def test_006_verify_with_invalid_credentials(self):
        """Verify user is not able to login when enter invalid credentials."""
        self.login.login(USER_HANDLE, INVALID_PASSWORD)
        self.login.verify_validation_with_invalid_credentials()

    def test_007_login_when_user_name_is_empty(self):
        """Verify user is not able to login when username field is empty."""
        self.login.enter_email("")
        self.login.enter_password(PASSWORD)
        self.login.verify_empty_handle_validation()

    def test_008_login_when_user_name_is_less_than_min_characters(self):
        """Verify user is not able to login when username field is less than 3 characters."""
        self.login.enter_email(HANDLE_NAME_LESS_THAN_3_CHAR)
        self.login.enter_password(PASSWORD)
        self.login.verify_user_handle_min_length_validation()

    def test_009_login_when_password_field_is_empty(self):
        """Verify user is not able to login when password field is empty."""
        self.login.enter_email(USER_HANDLE)
        self.login.enter_password("")
        self.login.verify_empty_password_validation()

    def test_010_verify_login_successfully_sanity(self):
        """Verify user is able to login with valid credentials."""
        self.login.login(USER_HANDLE, PASSWORD)
        self.login.verify_login_successfully()

    def test_011_verify_entering_invalid_mfa_code(self):
        """Verify user is not able to proceed to home page when entering invalid MFA."""
        self.login.verify_invalid_mfa_code(INVALID_CODE)
        self.login.verify_messages(message_name="invalid_code")

    def test_012_verify_resend_code_functionality_sanity(self):
        """Verify resend code sent the new code to the email."""
        self.login.verify_messages(message_name="resend_code")

    def test_013_verify_mfa_success_flow_sanity(self):
        """Verify entering the valid mfa navigate user to remember screen."""
        self.login.verify_valid_mfa()

    def test_014_select_remember_me_sanity(self):
        """Verify user is able to click on the remember me"""
        self.login.verify_remember_me()
