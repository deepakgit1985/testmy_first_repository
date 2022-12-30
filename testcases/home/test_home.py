import logging
import time
import unittest
import pytest

from pages.home.home_page import HomePage
from utilities.util import *
from testcases.test_config import *


@pytest.mark.run(order=2)
class Home(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.home = HomePage(self.driver)

    def test_001_verify_virtual_account_link_clicked_sanity(self):
        """Verify when user click link under virtual account section of what's new"""
        self.home.verify_virtual_account_link_is_clicked()

    def test_002_verify_instant_settlement_link_clicked_sanity(self):
        """Verify when user click link under instant settlement section of what's new"""
        self.home.verify_instant_settlement_link_is_clicked()

    def test_003_verify_more_unhappy_path_mocking_link_clicked_sanity(self):
        """Verify when user click link under more_unhappy_path_mocking section of what's new"""
        self.home.verify_more_unhappy_path_mocking_link_is_clicked()

    def test_004_verify_get_payment_method_link_clicked_sanity(self):
        """Verify when user click link under /get_payment_methods section of what's new"""
        self.home.verify_get_payment_method_link_is_clicked()

    def test_005_verify_manage_your_app_button_is_clicked_sanity(self):
        """Verify when user click Manage your apps button"""
        self.home.manage_your_apps_button()

    def test_006_verify_confirm_your_email_button_is_clicked_sanity(self):
        """Verify when user click on confirm your email option under let's get started section"""
        self.home.confirm_your_email()

    def test_007_verify_add_team_member_button_is_clicked_sanity(self):
        """Verify when user click on Add team members option under let's get started section"""
        self.home.add_team_members()

    def test_008_verify_get_pre_qualified_button_is_clicked_sanity(self):
        """Verify when user click on get pre-qualified option under let's get started section"""
        self.home.get_pre_qualified()

    def test_009_verify_understand_security_requirements_is_clicked_sanity(self):
        """Verify when user click on Understand Security Requirements option under let's get started section"""
        self.home.understand_security_requirements()

    def test_010_verify_create_your_app_button_is_clicked_sanity(self):
        """Verify when user click on Create your app option under let's get started section"""
        self.home.create_your_app()

    def test_011_verify_click_to_hosted_api_explorer_link_sanity(self):
        """Verify when user click on hosted api explorer under let's get started > Create your app section"""
        self.home.hosted_api_explorer()

    def test_012_verify_click_to_run_a_local_instance_link_sanity(self):
        """Verify when user click on run a local instance under let's get started > Create your app section"""
        self.home.run_a_local_instance()

    def test_013_verify_click_to_postman_collection_link_sanity(self):
        """Verify when user click on postman collection under let's get started > Create your app section"""
        self.home.postman_collection()

    def test_014_verify_try_sila_extensions_button_is_clicked_sanity(self):
        """Verify when user click on Try Sila Extensions option under let's get started section"""
        self.home.try_sila_extensions()

    def test_015_verify_invite_now_button_is_clicked_sanity(self):
        """Verify when user click on invite now button"""
        self.home.verify_invite_now_button_clicked()

    def test_016_verify_learn_now_button_is_clicked_sanity(self):
        """Verify when user click on learn now button"""
        self.home.learn_how_button_clicked()

    def test_017_verify_view_docs_button_is_clicked_sanity(self):
        """Verify when user click on view docs button"""
        self.home.view_docs_button_clicked()

    def test_018_verify_save_my_spot_button_is_clicked_sanity(self):
        """Verify when user click on save my spot button"""
        self.home.view_save_my_spot_button_clicked()

    def test_019_verify_send_message_button_is_clicked_sanity(self):
        """Verify when user click on send message button"""
        self.home.send_message_button_clicked()


@pytest.mark.run(order=3)
class Home_new_user(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, sign_up_test):
        self.home = HomePage(self.driver)

    def test_001_verify_create_your_app_button_sanity(self):
        self.home.create_your_app_button()

    def test_002_verify_request_access_button_sanity(self):
        self.home.request_access_button()

    def test_003_verify_get_started_create_app_button_sanity(self):
        self.home.get_started_create_app_button()

    def test_004_verify_resend_email_button_is_clicked_sanity(self):
        self.home.resend_email_button()




