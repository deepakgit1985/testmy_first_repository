import time
import unittest
import pytest
import allure

from utilities.util import *
from pages.forgot_password.forgot_password_page import ForgotPassword
from testcases.test_config import *


@allure.parent_suite('Console Automation')
@allure.suite("ForgotPassword")
@pytest.mark.run(order=3)
class ForgotPasswords(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTest):
        self.fp = ForgotPassword(self.driver)

    def test_001_verify_page_heading_sanity(self):
        """Verify page heading"""
        self.fp.verify_fp_heading()
        time.sleep(5)

    def test_002_verify_clicking_cancel_button(self):
        """Verify user navigates to login screen."""
        self.fp.verify_clicking_cancel_button()

    def test_003_verify_email_field_present(self):
        """Verify email field should be present on the forgot password screen"""
        self.fp.verify_email_field_present()

    def test_004_verify_empty_email_validation(self):
        """Verify user get an validation error when field is empty."""
        self.fp.verify_validation_when_email_empty()

    def test_005_verify_invalid_email_validation(self):
        """Verify user should get an error when email field is invalid."""
        self.fp.verify_invalid_email_validation(email=INCORRECT_EMAIL)

    def test_006_verify_forgot_password_functionality_successfully_sanity(self):
        """Verify user is able to forgot there password successfully."""
        self.fp.verify_forgot_password_successfully(email=USER_HANDLE)

    def test_007_verify_user_gets_email_sanity(self):
        """Verify user gets an email on there email id"""
        self.fp.get_link(name=HANDLE)
        self.fp.verify_fp_email_received()

    def test_008_verify_reset_button(self):
        """Verify reset button is in disable state"""
        self.fp.verify_reset_button_disable()

    def test_009_verify_cancel_button_navigates_to_login(self):
        """Verify when user click on the cancel button it navigates user to login screen."""
        self.fp.verify_cancel_button_functionality()

    def test_009_verify_user_change_password_successfully_sanity(self):
        """Verify user is able to update the new password successfully."""
        self.fp.get_link(name=HANDLE)
        self.fp.verify_fp_email_received()
        self.fp.set_new_password(enter_new_password="Arcgate1!", retype_new_password="Arcgate1!")
        self.fp.verify_password_updated_message()

    def test_010_verify_link_expire_after_reset_password_sanity(self):
        """Verify user is not able to change the password from the old link"""
        self.fp.get_link(name=HANDLE)
        self.fp.verify_link_expires_after_resetting_password()
