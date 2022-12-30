import logging
import time
import unittest
import pytest

from pages.change_password.change_password_page import Change_Password_Page
from utilities.util import *
from testcases.test_config import *


@pytest.mark.run(order=4)
class Change_Password(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cp = Change_Password_Page(self.driver)#SAGAR

    def test_001_verify_change_password_is_clicked_sanity(self):
        self.cp.click_to_profile()

    def test_002_verify_set_password_button_is_enabled(self):
        self.cp.set_password_disable_check()

    def test_003_verify_blank_current_password_validation(self):
        self.cp.blank_current_password_validation()
    #
    # def test_004_verify_blank_password_validation(self):
    #     self.cp.blank_password_validation()
    #
    # def test_005_verify_blank_retype_password_validation(self):
    #     self.cp.blank_retype_password_validation()
    #
    # def test_006_verify_wrong_current_password(self):
    #     self.cp.Wrong_current_password(INVALID_PASSWORD)
    #
    # def test_007_verify_message_user_entered_password_less_than_8_character(self):
    #     self.cp.enter_password_less_than_8_characters(PASSWORD, LESS_THAN_8_CHARACTERS)
    #
    # def test_008_verify_mismatch_confirm_password(self):
    #     self.cp.wrong_confirm_password(PASSWORD, NEW_PASSWORD, NEW_CONFIRM_PASSWORD)
    #
    # def test_009_verify_password_change_functionality(self):
    #     self.cp.verify_change_password_successfully(PASSWORD, NEW_PASSWORD, NEW_PASSWORD)
    #
    # def test_010_verify_cancel_button_functionality(self):
    #     time.sleep(5)
    #     self.cp.click_to_cancel()
    #

