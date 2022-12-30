# Register Page Locators ::

# Login::
email_field = "//input[@id='loginForm.handle']"
password_field = "//input[@id='loginForm.password']"
click_login_button = "//button[contains(text(),'Login')]"
get_login_page_heading = "//h2[contains(text(),'Log-in to the Console.')]"
click_forgot_password_link = "//a[contains(text(),'Forgot password?')]"
sign_up_link = "//span[contains(text(),'Sign up')]"
enter_mfa_code = "//input[@aria-label='Please enter verification code. Digit 1']"
click_resend_code_link = "//button[contains(text(),'Re-send code.')]"
enter_invalid_error = "//p[@class='text-info d-flex align-items-center mb-0']"
click_remember_me_on_device = "//input[@id='loginForm.mfa_device_remember_yes']"
get_remember_screen_heading = "//h2[contains(text(),'Would you like to remember this device for future ')]"
click_submit_button = "//button[@type='submit']"
get_alert_message = "//div[@role='alert']"
click_alert_icon = "//i[@class='fas fa-exclamation']"
click_continue_button = "//button[contains(text(),'Continue')]"
get_welcome_screen_heading = '''//h1[contains(text(),'Welcome to the Sila Console')]'''

# Forgot password::
user_email_field = "//input[@id='forgotPasswordForm.email']"
email_field_validation_icon = ".ml-2"
email_address_required_validation_message = "//div[contains(text(),'Email Address is required')]"
click_cancel_button = "//a[contains(text(),'Cancel')]"
get_forgot_password_heading = "//h2[contains(text(),'Forgot password?')]"
fp_email_sent_successfully = "//h2[contains(text(),'An email has been sent!')]"

# Create new password::
new_password_field = '//*[@id="setPasswordForm.password"]'
retype_new_password_field = "//input[@id='setPasswordForm.confirmPassword']"
click_reset_button = "//button[contains(text(),'Reset')]"
get_new_password_heading = "//h2[contains(text(),'Create a new password.')]"


# Home screen::
click_manage_your_apps_button = "//a[contains(text(),'Manage Your Apps')]"


# Application screen::
navigate_application_screen_link = "//i[@class='sila-icon apps']"
click_add_application_button = "//button[normalize-space()='Add Application']"
click_security_req_link = "//a[contains(text(),'security requirements')]"
security_link_new_tab_heading = "//h1[contains(text(),'Info Management & Security Requirements')]"
click_hosted_api_link = "//a[contains(text(),'hosted API explorer')]"
hosted_api_new_tab_heading = "//h1[contains(text(),'Choose Your Flow')]"
internal_app_name_field = "//input[@id='createAppForm.name']"
public_facing_app_name_field = "//input[@id='createAppForm.brand_name']"
application_close_icon = "//header/button[1]/i[1]"
enter_internal_app_name = "//input[@id='createAppForm.name']"
enter_public_app_name = "//input[@id='createAppForm.brand_name']"
enter_app_handle_name = "//input[@id='createAppForm.handle']"
click_generate_button = "//button[normalize-space()='Generate']"
authenticate_with_access_token = "//input[@id='createAppForm.authentication.jwt']"
authenticate_with_ECDSA = "//input[@id='createAppForm.authentication.wallet']"
get_validation_message = "//div[@class='tooltip-inner']"
check_app_handle_name = "//div[1]/article[1]/form[1]/div[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]"
request_support_button = "//article[contains(@class,'first app mb-3 mb-md-5')]//button[contains(@type,'button')][" \
                         "normalize-space()='Request Support']"
statement_information_button = "//div//article[1]/form[1]//div[1]/button[2]"
disable_button = "//div//article[1]/form[1]//div[1]/button[3]"
edit_button = "//div//article[1]/form[1]//div[1]/button[4]"
app_disabled_text = "//p[contains(text(),'Disabled')]"
update_public_facing_app_name = "//div[@class='brand-name loaded m-0 form-group']//input[" \
                                "@id='editAppForm.442.brand_name']"
update_internal_app_name = "//div[@class='name loaded m-0 form-group']//input[@id='editAppForm.442.name']"
update_app_handle_field = '''//div[@class='h-100 flex-nowrap input-group']//input[@name="handle" and @tabindex=3]'''
enter_current_password = "//input[@id='confirmPasswordForm.password']"
delete_app_button = "//article[contains(@class,'first app mb-3 mb-md-5')]//button[contains(@type,'button')][" \
                    "normalize-space()='Delete']"
confirm_delete_button = "//button[normalize-space()='Delete']"
regenerate_confirm_button = "//button[@class='btn btn-primary']"
confirm_and_download_button = "//button[normalize-space()='Confirm and Download']"
edit_app_cancel_button = "//button[normalize-space()='Cancel']"


# User Profile :: Your information screen

your_info_first_name = "//input[@id='userForm.first_name']"
your_info_last_name = "//input[@id='userForm.surname']"

# Logout
click_user_menu = "//a[@id='user-menu-toggle']"
menu_logout_link = "//a[normalize-space()='Logout']"
popup_text = '''//p[contains(text(),'Select "Logout" below if you are ready to end your')]'''
popup_title = "//h3[@id='logout-modal-title']"
logout_model_close_icon = "//body/div[6]/div[1]/div[1]/div[1]/button[1]"
logout_popup_cancel_button = "//button[normalize-space()='Cancel']"
logout_button = "//button[normalize-space()='Logout']"

# Register::
sila_main_logo = "//*[@id='main-logo']"
signup_to_move_money_heading = "//h1[contains(text(),'Sign up to move money with Sila.')]"
ach_transfer_link = "//a[contains(text(),'ACH Transfer API')]"
redirect_ach_transfer_page_heading = "//p[contains(text(),'Transfer money and initiate ACH transfers fast usi')]"
digital_wallet_api_link = "//a[contains(text(),'Digital Wallet API')]"
redirect_digital_wallet_page_heading = "//p[contains(text(),'Our Wallet API links any U.S. bank account via API')]"
bank_account_linking_api_link = "//a[contains(text(),'Bank Account Linking API')]"
redirect_bank_account_linking_page_heading = "//p[contains(text(),'Link bank accounts and transfer money fast " \
                                              "using t')] "
kyc_kyb_identity_verification_api_link = "//a[contains(text(),'KYC & KYB Identity Verification API')]"
redirect_kyb_kyc_verification_page_heading = "//p[contains(text(),'Banking, Digital Wallet & ACH Payments API " \
                                              "for Sof')] "
already_have_a_sila_account_text = "//p[contains(text(),'Already have a Sila account?')]"
login_link = "//span[contains(text(),'Login')]"
privacy_link = "//a[contains(text(),'Privacy Policy')]"
redirect_privacy_page_heading = "//h1[contains(text(),'Privacy Policy')]"
terms_of_service_link = "//a[contains(text(),'Terms of Service')]"
redirect_terms_page_heading = "//h1[contains(text(),'Terms of Service')]"
sdk_license_agreement_link = "//a[contains(text(),'SDK License Agreement')]"
redirect_sdk_page_heading = "//h1[contains(text(),'SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT')]"
first_name_field = "//input[@id='registerForm.first_name']"
surname_field = "//input[@id='registerForm.surname']"
company_name_field = "//input[@role='combobox']"
after_adding_company_name = "//input[@id='registerForm.company_name']"
select_company_name = "//a[@id='registerForm.company_name-item-1']"
work_email_field = "//input[@id='registerForm.email']"
work_phone_field = "//input[@id='registerForm.phone']"
register_password_field = "//input[@id='registerPasswordForm.password']"
confirm_password_field = "//input[@id='registerPasswordForm.confirmPassword']"
terms_checkbox = "//input[@name='privacy']"
create_account_button = "//button[contains(text(),'Create Account')]"
email_icon = ".email .fas"
invalid_email = "//div[contains(text(),'Invalid email address')]"
max_character_email = "//div[contains(text(),'Maximum of 254 characters.')]"
phone_icon = ".phone:nth-child(4) .fas"
invalid_phone_validation = "//div[contains(text(),'Invalid phone number')]"
password_icon = ".password:nth-child(5) .fas"
confirm_password_icon = ".password:nth-child(6) .fas"
password_min_length_validation = "//div[contains(text(),'Minimum of 8 characters required.')]"
password_max_length_validation = "//div[contains(text(),'Provide a shorter password.')]"
password_mismatch_validation = "//div[contains(text(),'Re-enter your password confirmation so it matches ')]"
password_lookalike_email_validation = '''//div[contains(text(),"Password can't contain your handle or email.")]'''
team_field_heading = "//h2[contains(text(),'Give your team a name.')]"
team_field_label = "//label[contains(text(),'Team Name')]"
add_team_name_field = "//input[@id='InviteTeamMembers.team_name']"
team_name_validation_icon = ".fas"
team_name_already_exists_validation = "//div[contains(text(),'Team name already exists.')]"
add_team_mates_box = "//textarea[@id='InviteTeamMembers.emails']"
send_invites_button = "//button[contains(text(),'Send Invites')]"
invitation_sent_message = ".text-info.d-flex.mb-0.px-4"

invite_your_team_and_collaborate_heading = "//h3[contains(text(),'Invite your team and collaborate.')]"
listing__text_1 = "//li[contains(text(),'Save time with faster onboarding')]"
listing__text_2 = "//li[contains(text(),'Stay up to date with the latest features')]"
listing_text_3 = "//li[contains(text(),'Organize communication with the Sila team')]"
add_team_box_placeholder_text = "//label[contains(text(),'Add teammates by email address and use commas to s')]"
skip_to_account_button = "// button[contains(text(), 'Skip to account creation')]"
flex_validation_message = "//div[@class='d-flex my-auto p-0 container']"

# Home screen with old user :::::::
# What's new
virtual_account_link = "//a[@href='https://docs.silamoney.com/docs/virtual-accounts-beta']"
Instant_Settlement_link = "//a[@href='https://docs.silamoney.com/docs/instant-settlement-beta']"
More_Unhappy_Path_Mocking = "//a[@href='https://docs.silamoney.com/docs/register']"
get_payment_methods_link = "//a[@href='https://docs.silamoney.com/docs/get_payment_methods']"
manage_your_apps_button = "//a[contains(text(),'Manage Your Apps')]"
# bottom section
invite_now = "//a[text()='Invite Now']"
learn_how = "//a[text()='Learn How']"
view_docs = "//a[text()='View Docs']"
save_my_spot = "//button[text()='Save my spot']"
send_message = "//button[text()='Send Message']"
team_member_pop_up = "//h3[@id='member-modal-title']"
iframe_path = "//*[@id='intercom-container']/div/div[1]"
# Let's get started
confirm_your_email = "//*[@id='sila-app']/div/div/div/main/section/div/div[2]/div/div[2]/div/a[1]"
add_team_members = "//*[@id='sila-app']/div/div/div/main/section/div/div[2]/div/div[2]/div/a[2]"
get_pre_qualified = "//*[@id='sila-app']/div/div/div/main/section/div/div[2]/div/div[2]/div/a[3]"
understand_security_requirements = "//*[@id='sila-app']/div/div/div/main/section/div/div[2]/div/div[2]/div/a[4]"
create_your_app = "//*[@id='sila-app']/div/div/div/main/section/div/div[2]/div/div[2]/div/a[5]"
try_sila_extensions = "//a[contains(text(),'Try Sila Extensions')]"
add_team_members_button = "//button[text()='Add team members']"
ask_sales_button = "//button[text()='Ask Sales']"
intercom_icon = "//*[@id='intercom-container']/div/div/div[2]"
read_requirements = "//button[text()='Read Requirements']"
hosted_api_explorer = "//*[@id='sila-app']/div/div/div/main/section/div/div[2]/div/div[3]/div/div[5]/p/a[1]"
run_a_local_instance = "//*[@id='sila-app']/div/div/div/main/section/div/div[2]/div/div[3]/div/div[5]/p/a[2]"
postman_collection = "//*[@id='sila-app']/div/div/div/main/section/div/div[2]/div/div[3]/div/div[5]/p/a[3]"
create_app_button = "//*[@id='sila-app']/div/div/div/main/section/div/div[2]/div/div[3]/div/div[5]/a"
application_page_heading = "//h1/span[contains(text(),'Application Detail')]"
view_sila_marketplace_button = "//button[text()='Visit Sila Marketplace']"
sila_icon = "//div[@class='d-flex align-items-center my-auto']"

# Home screen with new user :::::::
create_your_app_button = "//a[contains(text(),'Create Your App')]"
request_access_button = "//button[contains(text(),'Request Access')]"
get_started_create_app_button = "//*[@id='sila-app']/div/div/div/main/section/div/div[3]/div[3]/a"
resend_email_button = "//button[text()='Resend Email']"
confirm_email_locator= "//p[text()='All set! Your email is confirmed.']"
resend_email_header = "//*[@id='sila-app']/ul/li/div/div"

# Change password
Profile_icon = "//*[@id='user-menu-toggle']/span/span[2]"
change_password_dropdown = "//*[@id='user-menu']/div/a[2]/span[2]"
change_password_screen_heading = "//form/h2[text()='Set a new password']"
set_password_button = "//button[@type='submit']"
cancel_button = "//button[contains(text(),'Cancel')]"
current_password_text_field = "//input[@id='setPasswordForm.currentPassword']"
password_text_field = "//input[@id='setPasswordForm.password']"
retype_password_text_field = "//input[@id='setPasswordForm.confirmPassword']"

# SIDE MENU::
navigate_home_screen = "//i[@class='sila-icon home']"
navigate_account_admin_screen = "//i[@class='sila-icon settings']"
navigate_developer_screen = "//i[@class='sila-icon developers']"

# Application with new user
confirm_email_locator_app_page = "//p[contains(text(),'confirm your email')]"

