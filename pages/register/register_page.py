import time
import allure

from base.selenium_driver import SeleniumDriver
from selenium.webdriver.common.action_chains import ActionChains
from testcases.locators import *
from testcases.message import *


class RegisterPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Selectors
    @allure.step("Get max length validation message")
    def get_max_length_validation_text(self):
        self.wait_for_element(get_validation_message)
        return self.get_text(get_validation_message)

    @allure.step("Get invalid phone validation message")
    def get_invalid_phone_text(self):
        return self.get_text(invalid_phone_validation)

    @allure.step("Get min password validation message")
    def get_min_password_validation_text(self):
        return self.get_text(password_min_length_validation)

    @allure.step("Get min password validation message")
    def get_max_password_validation_text(self):
        return self.get_text(password_max_length_validation)

    def get_password_mismatch_validation_text(self):
        return self.get_text(password_mismatch_validation)

    def get_password_look_alike_email_validation_text(self):
        return self.get_text(password_lookalike_email_validation)

    def get_invalid_email_text(self):
        self.wait_for_element(invalid_email)
        return self.get_text(invalid_email)

    def get_already_have_sila_account_text(self):
        return self.get_text(already_have_a_sila_account_text)

    def get_login_page_heading(self):
        self.wait_for_element(get_login_page_heading)
        return self.get_text(get_login_page_heading)

    def get_team_field_heading(self):
        self.wait_for_element(team_field_heading)
        return self.get_text(team_field_heading)

    def get_welcome_screen_text(self):
        self.wait_for_element(get_welcome_screen_heading)
        return self.get_text(get_welcome_screen_heading)

    # def getTeamFieldText(self):
    #     self.wait_for_element(add_team_name_field)
    #     self.element_click(add_team_name_field)
    #     return self.get_text(add_team_name_field)

    def get_team_name_validation_text(self):
        self.wait_for_element(get_validation_message)
        return self.get_text(get_validation_message)

    def get_team_invitation_sent_text(self):
        self.wait_for_element(invitation_sent_message, "css")
        return self.get_text(invitation_sent_message, "css")

    # Actions
    def click_sign_up_link(self):
        self.wait_for_element(sign_up_link)
        self.element_click(sign_up_link)

    def click_login_link(self):
        self.wait_for_element(login_link)
        self.element_click(login_link)

    def enter_first_name(self, first_name):
        self.wait_for_element(first_name_field)
        self.element_click(first_name_field)
        self.send_keys(clear_field, first_name_field)
        self.send_keys(first_name, first_name_field)
        self.log.info("Entered firstName: " + first_name)

    def enter_surname(self, surname):
        self.element_click(surname_field)
        self.send_keys(clear_field, surname_field)
        self.send_keys(surname, surname_field)
        self.log.info("Entered lastName: " + surname)

    def enter_company_name(self, company_name):
        self.element_click(company_name_field)
        self.send_keys(clear_field, company_name_field)
        self.send_keys(company_name, company_name_field)
        self.log.info("Entered companyName: " + company_name)
        time.sleep(1)
        self.select_company_name(Keys.ENTER)

    def select_company_name(self, press_enter):
        # comp_name = ActionChains(self.driver)
        # comp_name.send_keys(Keys.TAB)
        self.send_keys(press_enter, select_company_name)

    def enter_work_email(self, email):
        self.element_click(work_email_field)
        self.send_keys(clear_field, work_email_field)
        self.send_keys(email, work_email_field)
        self.log.info("Entered email: " + email)

    def enter_work_phone(self, phone):
        self.element_click(work_phone_field)
        self.send_keys(clear_field, work_phone_field)
        self.send_keys(phone, work_phone_field)
        self.log.info("Entered phone: " + phone)

    def enter_password(self, password):
        self.element_click(register_password_field)
        self.send_keys(clear_field, register_password_field)
        self.send_keys(password, register_password_field)
        self.log.info("Entered password: " + register_password_field)
        self.web_scroll("down")

    def enter_confirm_password(self, confirm_password):
        self.element_click(confirm_password_field)
        self.send_keys(clear_field, confirm_password_field)
        self.send_keys(confirm_password, confirm_password_field)
        self.log.info("Entered confirmPassword: " + confirm_password)

    def click_terms_checkbox(self):
        time.sleep(1)
        term_checkbox = self.get_element(terms_checkbox)
        hoverover = ActionChains(self.driver).move_to_element(term_checkbox).click().perform()
        self.log.info("Clicked on I agree checkbox")

    def click_confirm_account_button(self):
        self.element_click(create_account_button)
        self.log.info("Clicked on confirm account button")

    def click_email_validation_icon(self):
        self.wait_for_element(click_alert_icon)
        self.element_click(click_alert_icon)
        self.log.info("Clicked on email validation icon")

    def click_password_validation_icon(self):
        self.wait_for_element(password_icon, 'css')
        self.element_click(password_icon, 'css')
        self.log.info("Clicked on password validation icon")

    def click_confirm_password_validation_icon(self):
        self.wait_for_element(confirm_password_icon, 'css')
        self.element_click(confirm_password_icon, 'css')
        self.log.info("Clicked on confirm password validation icon")

    def click_phone_validation_icon(self):
        self.wait_for_element(phone_icon, 'css')
        self.element_click(phone_icon, 'css')
        self.log.info("Clicked on phone validation icon")

    def click_team_name(self):
        self.wait_for_element(add_team_name_field)
        self.element_click(add_team_name_field)
        self.send_keys(clear_field, add_team_name_field)

    def click_team_name_validation_icon(self):
        self.wait_for_element(click_alert_icon)
        self.element_click(click_alert_icon)

    def enter_team_member_email(self, email):
        self.element_click(add_team_mates_box)
        self.send_keys(clear_field, add_team_mates_box)
        time.sleep(0.5)
        self.send_keys(email, add_team_mates_box)

    def click_Send_invite_button(self):
        self.wait_for_element(send_invites_button)
        self.element_click(send_invites_button)

    def click_team_page_continue_button(self):
        self.element_click(click_continue_button)

    def click_skip_to_account_button(self):
        self.web_scroll('down')
        self.wait_for_element(skip_to_account_button)
        self.element_click(skip_to_account_button)

    # Methods
    def sign_up_form(self, first_name='', surname='', company_name='', email='', phone='',
                     password='', confirm_password=''):
        self.driver.refresh()
        self.web_scroll("up")
        time.sleep(3)
        self.enter_first_name(first_name)
        self.enter_surname(surname)
        if company_name == '':
            self.send_keys(clear_field, company_name_field)
        else:
            self.enter_company_name(company_name)
        self.enter_work_email(email)
        self.enter_work_phone(phone)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)

    # def registerUsers(self, firstName='', surName='', companyName='', email='', phone='',
    #                     password='', confirmPassword=''):
    #     self.driver.get(register_url)
    #     time.sleep(5)
    #     self.signUpForm()
    #     self.clickTermsCheckbox()
    #     self.clickConfirmAccountButton()

    def add_new_team(self, teamName):
        self.click_team_name()
        self.send_keys(teamName, add_team_name_field)
        time.sleep(2)

    def invite_team_member(self, email):
        self.enter_team_member_email(email)
        self.click_Send_invite_button()

    def welcome_screen_text(self):
        text = self.get_welcome_screen_text()
        self.verify_text_match(text, NEW_USER_WELCOME_SCREEN_TITLE)

    # Assertions
    def verify_page_title(self):
        time.sleep(5)
        title = self.get_title()
        self.verify_text_match(title, SIGN_UP_PAGE_TITLE)
        self.log.info("User is on signup page")

    def verify_confirm_button_disable(self):
        self.web_scroll('down')
        self.check_element_state(create_account_button, element_name='create account button')

    def verify_max_name_length_validation(self):
        text = self.get_max_length_validation_text()
        self.verify_text_match(text, MAX_LENGTH)

    def verify_phone_validation_message(self):
        self.click_phone_validation_icon()
        phone_validation_text = self.get_invalid_phone_text()
        self.verify_text_match(phone_validation_text, INVALID_PHONE_MESSAGE)

    def verify_email_validation_message(self, email_type=''):
        self.web_scroll('up')
        if email_type == "invalid":
            self.click_email_validation_icon()
            email_validation_text = self.get_invalid_email_text()
            self.verify_text_match(email_validation_text, INVALID_EMAIL_ADDRESS)
        else:
            self.click_email_validation_icon()
            email_validation_text = self.get_text(max_character_email)
            self.verify_text_match(email_validation_text, EMAIL_MORE_THAN_MAX_LENGTH)

    def verify_password_validation_message(self, val='mismatch'):
        time.sleep(2)
        if val == "min":
            self.click_password_validation_icon()
            actual_validation_message = self.get_min_password_validation_text()
            self.verify_text_match(actual_validation_message, PASSWORD_LESS_THAN_MIN_LENGTH)
        elif val == 'max':
            self.click_password_validation_icon()
            actual_validation_message = self.get_max_password_validation_text()
            self.verify_text_match(actual_validation_message, PASSWORD_MORE_THAN_MAX_LENGTH)
        elif val == "same_as_email":
            self.click_password_validation_icon()
            actual_validation_message = self.get_password_look_alike_email_validation_text()
            self.verify_text_match(actual_validation_message, PASSWORD_LOOKALIKE_MESSAGE)
        else:
            self.click_confirm_password_validation_icon()
            actual_validation_message = self.get_password_mismatch_validation_text()
            self.verify_text_match(actual_validation_message, PASSWORD_MISMATCH_MESSAGE)

    def verify_login_link(self):
        self.click_login_link()
        heading = self.get_login_page_heading()
        self.verify_text_match(heading, LOGIN_PAGE_HEADING)
        self.click_sign_up_link()

    def verify_privacy_policy_link(self):
        self.web_scroll('down')
        self.link_redirect(privacy_link, expected_text=PRIVACY_POLITY_PAGE_TITLE, name="title")

    def verify_terms_of_service_link(self):
        self.web_scroll('down')
        self.link_redirect(terms_of_service_link, expected_text=TERMS_PAGE_TITLE, name="title")

    def verify_sdk_agreement_link(self):
        self.web_scroll('down')
        self.link_redirect(sdk_license_agreement_link, expected_text=SDK_LICENSE_TITLE, name="title")

    def verify_ach_transfer_api_link(self):
        self.web_scroll('up')
        self.link_redirect(ach_transfer_link, redirect_ach_transfer_page_heading,
                           REDIRECTED_ACH_PAGE_HEADING)

    def verify_digital_wallet_api_link(self):
        self.link_redirect(digital_wallet_api_link, redirect_digital_wallet_page_heading,
                           REDIRECTED_DIGITAL_WALLET_API_PAGE_HEADING)

    def verify_bank_account_linking_api_link(self):
        self.link_redirect(bank_account_linking_api_link, redirect_bank_account_linking_page_heading,
                           REDIRECTED_ACCOUNT_LINKING_PAGE_HEADING)

    def verify_kyc_identity_verification_link(self):
        self.link_redirect(kyc_kyb_identity_verification_api_link,
                           redirect_kyb_kyc_verification_page_heading,
                           REDIRECTED_KYC_KYB_IDENTITY_VERIFICATION_PAGE_HEADING)

    def verify_already_have_sila_account_text(self):
        self.web_scroll('down')
        actual_text = self.get_already_have_sila_account_text()
        self.verify_text_contains(actual_text, ALREADY_HAVE_A_SILA_ACCOUNT)

    def verify_user_navigates_to_invite_team_screen(self):
        heading = self.get_team_field_heading()
        self.verify_text_match(heading, TEAM_HEADING)

    # def verifyTeamNameFieldNotEmpty(self, name):
    #     team_name = self.getTeamFieldText()
    #     self.verify_text_match(team_name, name)

    def verify_team_name_already_exists(self):
        self.web_scroll('up')
        time.sleep(2)
        self.click_team_name_validation_icon()
        text = self.get_team_name_validation_text()
        self.verify_text_match(text, TEAM_NAME_ALREADY_EXITS)

    def verify_continue_button_state(self, value=True):
        self.web_scroll('down')
        if not value:
            self.check_element_state(click_continue_button, element_name="continue button on team invite screen")
        else:
            self.check_element_state(click_continue_button, value=True,
                                     element_name="continue button on team invite screen")

    def verify_invite_already_registered_user_validation(self, alreadyRegisteredUserEmail):
        self.enter_team_member_email(alreadyRegisteredUserEmail)
        time.sleep(2)
        text = self.get_team_invitation_sent_text()
        self.verify_text_contains(text, EMAIL_ALREADY_REGISTERED)

    def verify_invite_user_with_invalid_email(self, email):
        self.enter_team_member_email(email)
        time.sleep(3)
        text = self.get_team_invitation_sent_text()
        self.verify_text_contains(text, INVALID_EMAIL_IN_INVITE_TEAM_MEMBER_BOX)

    def verify_team_member_invited_successfully(self, email):
        self.invite_team_member(email)
        time.sleep(3)
        text = self.get_team_invitation_sent_text()
        self.verify_text_match(text, INVITATION_SENT_SUCCESSFULLY)

    def verify_welcome_screen(self):
        self.click_team_page_continue_button()
        self.click_skip_to_account_button()
        self.welcome_screen_text()

    def verify_confirm_email(self, emailPrefix):
        self.log.info("Email verification started")
        get_url = self.verify_email_confirmation(emailPrefix, flow='register')
        get_url = self.driver.get(get_url)
        time.sleep(5)
        self.log.info(get_url)
        time.sleep(10)
        text = self.get_welcome_screen_text()
        self.verify_text_match(text, HOME_SCREEN_TITLE)
