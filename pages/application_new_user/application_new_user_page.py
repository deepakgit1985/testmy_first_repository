from base.selenium_driver import SeleniumDriver
from testcases.locators import *
from testcases.message import *
from utilities.util import *


class ApplicationNewUser(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utility = Util()

    def verify_message_when_email_is_not_confirmed(self):
        self.element_click(navigate_application_screen_link)
        self.wait_for_element(confirm_email_locator_app_page)
        get_text = self.get_text(confirm_email_locator_app_page)
        self.verify_text_match(get_text, confirm_email_message_app_page)

