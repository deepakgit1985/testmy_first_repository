import unittest

import allure
import pytest

from utilities.util import *
from pages.register.register_page import RegisterPage
from testcases.test_config import *


@pytest.mark.run(order=1)
@pytest.mark.usefixtures('setUp')
class RegisterTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTest):
        self.register = RegisterPage(self.driver)

    def test_001_verify_register_page(self):
        """Verify user is on the register page."""
        self.register.click_sign_up_link()
        self.register.verify_page_title()

    def test_002_register_when_first_name_empty(self):
        """Verify user is not able to register when first_name field is empty."""
        self.register.sign_up_form('', SURNAME, COMPANY_NAME, RANDOM_EMAIL, PHONE, PASSWORD,
                                   CONFIRM_PASSWORD)
        self.register.click_terms_checkbox()
        self.register.verify_confirm_button_disable()

    def test_003_register_when_surname_empty(self):
        """Verify user is not able to register when surname field is empty."""
        self.register.enter_surname('')
        self.register.verify_confirm_button_disable()

    def test_004_register_when_company_name_empty(self):
        """Verify user is not able to register when company_name field is empty."""
        self.register.sign_up_form(FIRST_NAME, SURNAME, '', RANDOM_EMAIL, PHONE, PASSWORD,
                                   CONFIRM_PASSWORD)
        self.register.verify_confirm_button_disable()

    def test_005_register_when_work_email_empty(self):
        """Verify user is not able to register when work email field is empty."""
        self.register.sign_up_form(FIRST_NAME, SURNAME, COMPANY_NAME, '', PHONE, PASSWORD,
                                   CONFIRM_PASSWORD)
        self.register.verify_confirm_button_disable()

    def test_006_register_when_phone_empty(self):
        """Verify user is not able to register when work_phone field is empty."""
        self.register.sign_up_form(FIRST_NAME, SURNAME, COMPANY_NAME, RANDOM_EMAIL, '', PASSWORD,
                                   CONFIRM_PASSWORD)
        self.register.verify_confirm_button_disable()

    def test_007_register_when_password_empty(self):
        """Verify user is not able to register when password field is empty."""
        self.register.sign_up_form(FIRST_NAME, SURNAME, COMPANY_NAME, RANDOM_EMAIL, PHONE, '',
                                   CONFIRM_PASSWORD)
        self.register.verify_confirm_button_disable()

    def test_008_register_when_confirm_password_empty(self):
        """Verify user is not able to register when confirm_password field is empty."""
        self.register.sign_up_form(FIRST_NAME, SURNAME, COMPANY_NAME, RANDOM_EMAIL, PHONE, PASSWORD, ' ')
        self.register.verify_confirm_button_disable()

    def test_009_register_with_more_than_100_characters_first_name(self):
        """Verify user is not able to register when first_name is more than 100 characters."""
        self.driver.refresh()
        self.register.enter_first_name(MORE_THAN_100_CHARACTERS)
        self.register.enter_surname(SURNAME)
        self.register.verify_max_name_length_validation()

    def test_010_register_with_more_than_100_characters_sur_name(self):
        """Verify user is not able to register when surname is more than 100 characters."""
        self.driver.refresh()
        self.register.enter_surname(MORE_THAN_100_CHARACTERS)
        self.register.enter_first_name(FIRST_NAME)
        self.register.verify_max_name_length_validation()

    def test_011_register_when_terms_checkbox_empty(self):
        """Verify user is not able to register when confirm_password field is empty."""
        self.register.sign_up_form(FIRST_NAME, SURNAME, COMPANY_NAME, RANDOM_EMAIL, PHONE, PASSWORD,
                                   CONFIRM_PASSWORD)
        self.register.verify_confirm_button_disable()

    def test_012_register_when_email_invalid(self):
        """Verify user is not able to register when email is invalid."""
        self.driver.refresh()
        self.register.enter_work_email(email=INVALID_EMAIL)
        time.sleep(2)
        self.register.verify_email_validation_message("invalid")

    def test_013_register_when_email_is_more_than_255_characters(self):
        """Verify user is not able to register when email is more than 255 characters."""
        self.register.enter_work_email(email=EMAIL_MORE_THAN_254_CHARACTERS)
        self.register.verify_email_validation_message()

    def test_014_register_when_password_is_less_than_8_characters(self):
        """Verify user is not able to register when password is less than 8 characters."""
        self.register.enter_password(password=LESS_THAN_8_CHARACTERS)
        self.register.verify_password_validation_message("min")

    def test_015_register_when_password_is_more_than_100_characters(self):
        """Verify user is not able to register when password is more than 100 characters."""
        self.driver.refresh()
        self.register.enter_password(password=MORE_THAN_100_CHARACTERS)
        self.register.enter_work_phone(PHONE)
        self.register.verify_password_validation_message('max')

    def test_016_register_when_password_and_confirm_password_mismatch(self):
        """Verify user is not able to register when password and confirm password mismatch."""
        self.register.enter_password(password=PASSWORD)
        self.register.enter_confirm_password(confirm_password=MISMATCH_CONFIRM_PASSWORD)
        self.register.enter_work_phone(PHONE)
        self.register.verify_password_validation_message('mismatch')

    # def test_017_register_when_password_same_as_email(self):
    #     """Verify user is not able to register when password is similar to email."""
    #     self.register.enter_work_email(email=user_email)
    #     self.register.enter_password(password=PASSWORD_LOOKALIKE_EMAIL)
    #     self.register.enter_work_phone(PHONE)
    #     self.register.verify_password_validation_message("same_as_email")

    def test_018_register_when_phone_number_is_invalid(self):
        """Verify user is not able to register when entered invalid phone number."""
        self.driver.refresh()
        self.register.enter_work_phone(phone=INVALID_PHONE_NUM)
        self.register.enter_surname(SURNAME)
        self.register.verify_phone_validation_message()

    def test_019_verify_privacy_policy(self):
        """Verify privacy policy link navigates user to privacy policy page.."""
        self.register.verify_privacy_policy_link()

    def test_020_verify_terms_of_service_link(self):
        """Verify terms of service link navigates user to terms and services page."""
        self.register.verify_terms_of_service_link()

    def test_021_verify_already_have_account_text(self):
        """Verify page contains already have a sila account text."""
        self.register.verify_already_have_sila_account_text()

    def test_022_verify_login_link(self):
        """Verify user is able to navigates to login page."""
        self.register.verify_login_link()

    def test_023_verify_user_navigates_to_invite_team_screen(self):
        """Verify user is able to navigate from register screen to invite team screen."""
        self.driver.refresh()
        time.sleep(2)
        self.register.sign_up_form(owner_first_name, SURNAME, COMPANY_NAME, user_email, PHONE, PASSWORD,
                                   CONFIRM_PASSWORD)
        self.register.click_terms_checkbox()
        self.register.click_confirm_account_button()
        # utility.insert_data(user_email)
        self.register.verify_user_navigates_to_invite_team_screen()

    def test_024_verify_team_screen_text(self):
        """Verify heading and paragraph on invite team member screen."""
        self.register.verify_continue_button_state(False)

    def test_025_verify_team_name_already_exists_validation(self):
        """Verify team name already exist validation error"""
        self.register.verify_team_name_already_exists()

    def test_030_add_new_team_name(self):
        """Verify user is able to add new team."""
        self.register.add_new_team(team_name)
        self.register.verify_continue_button_state(True)
    #
    # def test_032_invite_already_registered_user_to_team(self):
    #     """Verify user is not able to invite already registered member."""
    #     self.register.verify_invite_already_registered_user_validation("test@gmail.com")

    def test_033_invite_user_with_invalid_email(self):
        """Verify user is not able to invite team member when email is invalid."""
        self.register.verify_invite_user_with_invalid_email(email=INVALID_EMAIL)
        self.register.verify_continue_button_state(False)

    def test_034_invite_team_member_successfully(self):
        """Verify user is able to invite team member from add team box."""
        self.register.verify_team_member_invited_successfully(email=RANDOM_EMAIL)

    def test_035_register_user_successfully(self):
        """Verify user navigates to welcome screen successfully."""
        self.register.verify_welcome_screen()

    def test_036_register_user_from_email_confirmation_link(self):
        """Verify user should redirect to home screen after clicking on email confirmation link"""
        self.register.verify_confirm_email(admin)
        time.sleep(10)

    # def test_035_register_user_for_owner_role(self):
    #     """Verify user is able to register user as owner role."""
    #     self.register.registerUsers(owner_first_name, surname, company_name, owner_email, phone, password,
    #                                 confirm_password)
    #     utility.insert_data(owner_email)
    #     self.register.verifyConfirmEmail(owner)
    #
    # def test_036_register_user_for_manager_role(self):
    #     """Verify user is able to register user as manager role."""
    #     self.register.registerUsers(manager_first_name, surname, company_name, manager_email, phone, password,
    #                                 confirm_password)
    #     utility.insert_data(manager_email)
    #     self.register.verifyConfirmEmail(manager)
    #
    # def test_037_register_user_for_developer_role(self):
    #     """Verify user is able to register user as developer role."""
    #     self.register.registerUsers(developer_first_name, surname, company_name, developer_email, phone, password,
    #                                 confirm_password)
    #     utility.insert_data(developer_email)
    #     self.register.verifyConfirmEmail(developer)
    #
    # def test_038_register_user_for_contractor_role(self):
    #     """Verify user is able to register user as contractor role."""
    #     self.register.registerUsers(contractor_first_name, surname, company_name, contractor_email, phone, password,
    #                                 confirm_password)
    #     utility.insert_data(contractor_email)
    #     self.register.verifyConfirmEmail(contractor)
    # def test_021_verify_sdk_agreement_link(self):
    #     """Verify sdk agreement link navigates user to sdk agreement page."""
    #     self.register.verify_sdk_agreement_link()
    #
    # def test_022_verify_ACH_transfer_link(self):
    #     """Verify ACH transfer api link navigates user to ach transfer page."""
    #     self.register.verify_ach_transfer_api_link()
    #
    # def test_023_verify_digital_wallet_api_link(self):
    #     """Verify digital wallet api link navigates user to digital wallet page."""
    #     self.register.verify_digital_wallet_api_link()
    #
    # def test_024_verify_bank_account_link(self):
    #     """Verify bank account linking api navigates user to bank account link page"""
    #     self.register.verify_bank_account_linking_api_link()
    #
    # def test_025_verify_kyc_kyb_identity_verification_link(self):
    #     """Verify user navigates to kyb kyc verification page."""
    #     self.register.verify_kyc_identity_verification_link()