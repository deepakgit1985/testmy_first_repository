import logging
import unittest

import pytest

from pages.application_new_user.application_new_user_page import ApplicationNewUser
from utilities.util import *


@pytest.mark.run(order=3)
class App_new_user(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, sign_up_test):
        self.app_new_user = ApplicationNewUser(self.driver)

    def test_001_verify_message_while_no_email_is_confirmed(self):
        self.app_new_user.verify_message_when_email_is_not_confirmed()