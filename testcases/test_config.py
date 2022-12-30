from utilities.util import Util

# get unique name
utility = Util()
name = utility.get_unique_name(15)

# environments
dev_url = 'https://devconsole.silamoney.com/login'
stage_url = 'https://devconsole.silamoney.com/login'
production_url = "https://devconsole.silamoney.com/login"


# Login
USER_HANDLE = "silaqaautomation@gmail.com"
PASSWORD = "Arcgate1!"
HANDLE = "silaqaautomation"
INVALID_PASSWORD = "55455265123"

INVALID_CODE = "985635"
INCORRECT_EMAIL = "testsa"
NEW_USER_EMAIL = "testautomation@mailinator.com"
APP_NAME = "esdca_auto_" + name
UPDATED_APP_NAME = "auto_update_" + name

HANDLE_NAME_LESS_THAN_3_CHAR = "aa"
HANDLE_NAME_SPECIAL_CHAR = "@@"
INTERNAL_APP_NAME = "sila_autom" + name
PUBLIC_APP_NAME = "public_autom" + name
HANDLE_NAME = "jwt_app" + name

# register form data
FIRST_NAME = "Automation"
SURNAME = "User"
COMPANY_NAME = "ArcGate"
UPDATED_COMPANY_NAME = "Arcgate"
PHONE = "9874585855"
CONFIRM_PASSWORD = "Arcgate1!"
RANDOM_EMAIL = name + "@mailiantor.com"

# admin user
admin_first_name = "Sila_Admin"
admin = admin_first_name + name
user_email = "silaqaautomation+" + admin + "@gmail.com"
# admin_email = "testqa+" + admin + "@mailinator.com"

# owner user
owner_first_name = "Owner"
owner = owner_first_name + name
owner_email = "silaqaautomation+" + owner + "@gmail.com"

# manager user
manager_first_name = "manager"
manager = manager_first_name + name
manager_email = "silaqaautomation+" + manager + "@gmail.com"

# developer user
developer_first_name = "developer"
developer = developer_first_name + name
developer_email = "silaqaautomation+" + developer + "@gmail.com"

# contractor user
contractor_first_name = "contractor"
contractor = contractor_first_name + name
contractor_email = "silaqaautomation+" + contractor + "@gmail.com"

# Create team name
team_name = "team_" + name

# register invalid and mix and max data
MORE_THAN_100_CHARACTERS = "testuserforsignuptestuserforsignuptestuserforsignuptestuserforsignuptestuserforsignuptestuserforsisss"
LESS_THAN_8_CHARACTERS = "1234567"
EMAIL_MORE_THAN_254_CHARACTERS = "fakedsadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdsadassadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdsadasssadasdasddsadasdasdasdasdasdasdasdasdasdasdasdasdasdgsadadasdasdasdasdasdasdsadasdasdasdasdasdasdasdasdasdasd@gmail.com"
MISMATCH_CONFIRM_PASSWORD = "Arcgate12!"
PASSWORD_LOOKALIKE_EMAIL = user_email
INVALID_EMAIL = "test@"
INVALID_PHONE_NUM = "dadas"
INVALID_USER_NAME = "fdd@g"


# Change password
NEW_PASSWORD = "Arcgate1!"
NEW_CONFIRM_PASSWORD = "ArcGat"

