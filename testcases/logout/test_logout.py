import unittest
import pytest
import allure

from utilities.util import *
from pages.logout.logout_page import LogoutPage


@allure.parent_suite('Console Automation')
@allure.suite("Logout")
@pytest.mark.run(order=2)
@pytest.mark.usefixtures("oneTimeSetUp")
class LogoutTest(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.logout = LogoutPage(self.driver)

    def test_001_verify_logout_popup_title(self):
        """Verify logout popup title"""
        self.logout.verify_logout_popup_title()

    def test_002_verify_logout_popup_text(self):
        """Verify logout popup text."""
        self.logout.verify_logout_popup_text()

    def test_003_verify_cancel_button_functionality(self):
        """Verify clicking on cancel button close the logout popup"""
        self.logout.verify_cancel_button_close_popup()

    def test_004_logout_successfully_sanity(self):
        """Verify user is able to logout successfully."""
        self.logout.verify_logout_flow()
