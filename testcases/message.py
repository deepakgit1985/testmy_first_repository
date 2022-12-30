from selenium.webdriver.common.keys import Keys

# keyboard keys
clear_field = Keys.CONTROL + "a" + Keys.DELETE

SIGN_UP_PAGE_TITLE = "Sign Up | Sila API"
LOGIN_PAGE_HEADING = "Log-in to the Console."
MFA_PAGE_TITLE = "Sila Console - Sign In::Two-factor authentication."
FORGOT_PASSWORD_PAGE_HEADING = "Forgot password?"
INVITE_TEAM_MEMBER_TITLE = "Sila Console - register::Invite Team Members"
QUESTIONNAIRE_PAGE_TITLE = "Sila Console - register::Questions"
INVALID_CODE_MESSAGE = "Could not verify this code. Please try again."
RESEND_CODE_MESSAGE = "A new code has been sent to your email address!"
REMEMBER_SCREEN_HEADING = "Would you like to remember this device for future login?"
HOME_SCREEN_TITLE = "Sila Console - Welcome Series"
NEW_USER_WELCOME_SCREEN_TITLE = "Welcome to the Sila Console"
INVALID_LOGIN_MESSAGE = "Your account will be temp"
WELCOME_SCREEN_HEADING = "Welcome to the Sila Console"
INVALID_EMAIL_ADDRESS = "Invalid email address"
FP_EMAIL_SENT = "An email has been sent!"
FP_HEADING = "Forgot password?"
NEW_PASSWORD_HEADING = "Create a new password."
LINK_EXPIRED_MESSAGE = "No unfrozen user account"
PASSWORD_UPDATED_MESSAGE = "Password has been updated"


# Applications::
REDIRECTED_SECURITY_LINK_HEADING = "Info Management & Security Requirements"
REDIRECTED_HOSTED_API_LINK_HEADING = "Choose Your Flow"
MIN_3_CHARACTERS_REQUIRED = "Minimum of 3 characters required."
SPECIAL_CHARACTER_VALIDATION = "Can't use spaces or special characters and must be at least 3 characters."
DISABLE_TEXT = "Disabled"
HANDLE_EXISTS = "Handle already exists."
APP_CREATED = "created"
APP_UPDATED_MESSAGE = "Your app has been updated!"
APP_DELETED_MESSAGE = "deleted!"
JWT_APP_UPDATED_MESSAGE = "The client has been updated"

MAX_LENGTH = "Maximum of 100 characters."
EMAIL_MORE_THAN_MAX_LENGTH = "Maximum of 254 characters."
PASSWORD_LESS_THAN_MIN_LENGTH = "Minimum of 8 characters required."
PASSWORD_MORE_THAN_MAX_LENGTH = "Provide a shorter password."
PASSWORD_MISMATCH_MESSAGE = "Re-enter your password confirmation so it matches your password."
PASSWORD_LOOKALIKE_MESSAGE = "Password can't contain your handle or email."
INVALID_PHONE_MESSAGE = "Invalid phone number"
TEAM_HEADING = "Give your team a name."
TEAM_NAME_ALREADY_EXITS = "This team name is already in use, please create a different name for your team."
ALREADY_HAVE_A_SILA_ACCOUNT = "Already have a Sila account?"
INVITATION_SENT_SUCCESSFULLY = "Invites successfully sent!"
EMAIL_ALREADY_REGISTERED = "This email is already registered:"
INVALID_EMAIL_IN_INVITE_TEAM_MEMBER_BOX = "At least one or more email addresses are invalid."
INVALID_LOGIN = "Invalid login, please try again."
INVALID_PASSWORD_ATTEMPT = "Your account will be temporarily locked after 4 more unsuccessful login attempts."


# login
EMPTY_USER_NAME = "Handle / Email Address is required"
EMPTY_PASSWORD_MESSAGE = "Password is required"

# logout
LOGOUT_POPUP_TEXT = 'Select "Logout" below if you are ready to end your current session.'
LOGOUT_POPUP_TITLE = "Ready to Leave?"

# forgot password
EMAIL_ADDRESS_REQUIRED_MESSAGE = "Email Address is required"

#  Heading after page redirect by clicking on links
PRIVACY_POLITY_PAGE_TITLE = "Sila Privacy Policy • Sila Money"
TERMS_PAGE_TITLE = "Terms of Service • Sila Money"
SDK_LICENSE_TITLE = "SDK License Agreement • Sila Money"
REDIRECTED_PRIVACY_PAGE_HEADING = "Privacy Policy"
REDIRECTED_TERMS_PAGE_HEADING = "Terms of Service"
REDIRECTED_SDK_AGREEMENT_PAGE_HEADING = "SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT"
REDIRECTED_ACH_PAGE_HEADING = "Transfer money and initiate ACH transfers fast using the Sila API"
REDIRECTED_DIGITAL_WALLET_API_PAGE_HEADING = "Our Wallet API links any U.S. bank account via API for in-app payments."
REDIRECTED_ACCOUNT_LINKING_PAGE_HEADING = "Link bank accounts and transfer money fast using the Sila API"
REDIRECTED_KYC_KYB_IDENTITY_VERIFICATION_PAGE_HEADING = "Banking, Digital Wallet & ACH Payments API for Software Teams"

# Teams
TEAM_MODAL_BOX_TITLE = "Create new team"

# Application
APPLICATION_HEADING = "Application Detail"
NO_APP_YET_MESSAGE = "You do not have any apps yet."
STEP1_HEADING = "App Pending"
STEP1_SUB_HEADING = "Create an internal and public name for your app."
STEP1_DESCRIPTION = "The internal app name will be what you see within this console and is what Sila uses to identify" \
                    " your activity for support. The publicly facing app name will be used for services like Plaid" \
                    " and in other instances where the app name is shown to the end-user."
STEP2_HEADING = "Give your app a handle."
STEP3_HEADING = "Generate a public Ethereum address, or provide us with one below."
STEP3_DESCRIPTION = "A private key will also be generated for you. Download and store both of these keys in order to" \
                    " access your app. It’s very important that you store these keys in a safe place and do not" \
                    " lose them!"

# home
team_member_message = "Invite a team member"
learn_how_message = "Native SDKs"
view_docs_message = "Introduction"
save_my_spot_message = "Live Demo • Sila • The Money API for Fintech"
understand_security_requirements_message = "Info Management & Security Requirements"
hosted_api_explorer_message = "Sila API Demo (Node SDK)"
run_a_local_instance_message = "Running the Sila Demo (local)"
postman_collection_message = "GitHub - Sila-Money/sila-postman-signer: Lightweight local server to sign requests with ECDSA and forward requests to desired host. Includes a Postman collection for the Sila API that works with this server."
application_page_heading_message = "Application Detail"
view_sila_marketplace_message = "Fintech Marketplace - Sila"
virtual_account_page_title = "Sila API Docs | Sila Banking and Payments API"
instant_settlement_page_title = "Instant Settlement (BETA)"
More_Unhappy_Path_Mocking_title = "/register"
get_payment_methods_title = "/get_payment_methods"
resend_email_message = "You have registered for the Sila Console. Please check your email"
confirmed_email_message = "All set! Your email is confirmed."

# Change password
change_password_screen_title = "Set a new password"
current_password_error_message = "Re-enter your current password so it matches your current settings."
password_less_than_8_char_error_message = "Minimum of 8 characters required."
blank_current_password_error_message = "Current password is required"
blank_password_error_message = "Password is required"
blank_retype_error_message = "Retype password is required"
wrong_retype_error_message = "Re-enter your password confirmation so it matches your password."

# Application with new user
confirm_email_message_app_page = "Please confirm your email to create an app."
