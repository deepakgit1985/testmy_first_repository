import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.selenium_driver import SeleniumDriver
from testcases.message import *
from utilities.util import *
from testcases.locators import *


class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.utility = Util()

    @allure.link("https://sila.testrail.io/index.php?/cases/view/4690")
    def verify_virtual_account_link_is_clicked(self):
        self.wait_for_element(virtual_account_link)
        self.link_redirect(locator=virtual_account_link, name='title', expected_text=virtual_account_page_title)

    @allure.link("https://sila.testrail.io/index.php?/cases/view/4691")
    def verify_instant_settlement_link_is_clicked(self):
        self.wait_for_element(Instant_Settlement_link)
        self.link_redirect(locator=Instant_Settlement_link, name='title', expected_text=instant_settlement_page_title)

    @allure.description("When new user click more unhappy path mocking link")
    def verify_more_unhappy_path_mocking_link_is_clicked(self):
        self.wait_for_element(More_Unhappy_Path_Mocking)
        self.link_redirect(locator=More_Unhappy_Path_Mocking, name='title', expected_text=More_Unhappy_Path_Mocking_title)

    @allure.description("When new user click on get payment method link")
    def verify_get_payment_method_link_is_clicked(self):
        self.wait_for_element(get_payment_methods_link)
        self.link_redirect(locator=get_payment_methods_link, name='title', expected_text=get_payment_methods_title)

    @allure.description("When new user click on invite now button")
    def verify_invite_now_button_clicked(self):
        self.element_click(invite_now)
        get_team_member_text = self.get_text(team_member_pop_up)
        self.verify_text_match(get_team_member_text, team_member_message)
        time.sleep(2)
        self.driver.back()

    @allure.description("When new user click on learn how button")
    def learn_how_button_clicked(self):
        self.wait_for_element(learn_how)
        self.link_redirect(locator=learn_how, name='title', expected_text=learn_how_message)

    @allure.description("When new user click on view docs button")
    def view_docs_button_clicked(self):
        self.wait_for_element(view_docs)
        self.link_redirect(locator=view_docs, name='title', expected_text=view_docs_message)

    @allure.description("When new user click on save my spot button")
    def view_save_my_spot_button_clicked(self):
        self.wait_for_element(save_my_spot)
        self.link_redirect(locator=save_my_spot, name='title', expected_text=save_my_spot_message)

    @allure.description("When new user click on send message button")
    def send_message_button_clicked(self):
        self.element_click(send_message)
        time.sleep(2)
        self.move_to_frame()
        time.sleep(4)

    @allure.description("When new user click on confirm your email ")
    def confirm_your_email(self):
        self.element_click(confirm_your_email)
        confirm_emailed = self.get_text(confirm_email_locator)
        self.verify_text_match(confirm_emailed, confirmed_email_message)

    @allure.description("When new user click on add team member button")
    def add_team_members(self):
        self.element_click(add_team_members)
        self.element_click(add_team_members_button)
        get_team_member_text = self.get_text(team_member_pop_up)
        self.verify_text_match(get_team_member_text, team_member_message)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    @allure.description("When new user click on get pre qualified")
    def get_pre_qualified(self):
        time.sleep(3)
        self.wait_for_element(get_pre_qualified)
        self.element_click(get_pre_qualified)
        self.element_click(ask_sales_button)
        self.move_to_frame()
        time.sleep(2)

    @allure.description("When new user click on understand security requirements")
    def understand_security_requirements(self):
        self.wait_for_element(understand_security_requirements)
        self.element_click(understand_security_requirements)
        self.link_redirect(locator=read_requirements, name='title' , expected_text=understand_security_requirements_message)
        time.sleep(2)

    def click_to_create_your_app(self):
        self.wait_for_element(create_your_app)
        self.element_click(create_your_app)

    @allure.description("When new user click on create your app button")
    def create_your_app(self):
        self.click_to_create_your_app()
        time.sleep(2)
        self.element_click(create_app_button)
        Application_page_heading_text = self.get_text(application_page_heading)
        self.verify_text_match(Application_page_heading_text, application_page_heading_message)
        time.sleep(2)
        self.driver.back()

    @allure.description("When new user click on hosted api explorer link")
    def hosted_api_explorer(self):
        self.click_to_create_your_app()
        time.sleep(2)
        self.link_redirect(locator=hosted_api_explorer, name='title', expected_text=hosted_api_explorer_message)

    @allure.description("When new user click on run a local instance link")
    def run_a_local_instance(self):
        self.click_to_create_your_app()
        time.sleep(2)
        self.link_redirect(locator=run_a_local_instance, name='title', expected_text=run_a_local_instance_message)

    @allure.description("When new user click on postman collection link")
    def postman_collection(self):
        self.click_to_create_your_app()
        time.sleep(2)
        self.link_redirect(locator=postman_collection, name='title', expected_text=postman_collection_message)

    @allure.description("When new user click on try sila extensions link")
    def try_sila_extensions(self):
        self.wait_for_element(try_sila_extensions)
        self.element_click(try_sila_extensions)
        self.link_redirect(locator=view_sila_marketplace_button, name='title', expected_text=view_sila_marketplace_message)

    @allure.description("When new user click on manage your apps button")
    def manage_your_apps_button(self):
        self.element_click(manage_your_apps_button)
        Application_page_heading_text = self.get_text(application_page_heading)
        self.verify_text_match(Application_page_heading_text, application_page_heading_message)
        time.sleep(2)
        self.driver.back()

    @allure.description("When new user click on create your app button")
    def create_your_app_button(self):
        self.wait_for_element(create_your_app_button)
        time.sleep(2)
        self.element_click(create_your_app_button)
        time.sleep(2)
        Application_page_heading = self.get_text(application_page_heading)
        self.verify_text_match(Application_page_heading, application_page_heading_message)
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

    @allure.description("When new user click on request access button")
    def request_access_button(self):
        self.wait_for_element(request_access_button)
        self.element_click(request_access_button)
        time.sleep(2)
        self.move_to_frame()
        time.sleep(2)

    @allure.description("When new user click on Get Started : create app button")
    def get_started_create_app_button(self):
        self.wait_for_element(get_started_create_app_button)
        self.element_click(get_started_create_app_button)
        time.sleep(2)
        Application_page_heading = self.get_text(application_page_heading)
        self.verify_text_match(Application_page_heading, application_page_heading_message)
        time.sleep(2)
        self.driver.back()

    @allure.description("When new user click on resend email button")
    def resend_email_button(self):
        self.wait_for_element(confirm_your_email)
        self.element_click(confirm_your_email)
        time.sleep(2)
        self.element_click(resend_email_button)
        resend_email_verify = self.get_text(resend_email_header)
        self.verify_text_contains(resend_email_verify, resend_email_message)
        time.sleep(10)





