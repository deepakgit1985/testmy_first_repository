import datetime
import os
import logging
import pickle
import time

import allure
from allure_commons.types import AttachmentType
import base64

from selenium.webdriver import ActionChains, Keys

import utilities.custom_logger as cl
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from testcases.locators import *


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver


    def get_screenshot(self, result_message):
        """
        Takes screenshot of the current open web page
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred when taking screenshot")

    def get_title(self):
        """Get title of the page"""
        try:
            return self.driver.title
        except:
            self.log.info("Title not found")
            raise

    def get_by_type(self, locator_type):
        """Get element by its type."""
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type +
                          " not correct/supported")
        return False

    def get_element(self, locator, locator_type="xpath"):
        """
        Get element name
        locator: "It can be id, xpath, css_selector etc.."
        locator_type: by default its xpath.
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        return element

    def get_element_list(self, locator, locator_type="xpath"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and locator_type: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and locator_type: " + locator_type)
        return element

    def element_click(self, locator="", locator_type="xpath", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
                assert element is not None, (
                        "Locator not found. Cannot click on the element with locator: " + locator +
                        "locator_type: " + locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locator_type: " + locator_type)
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(locator + ' ' + 'not found ')
            raise
        except:
            self.log.info("Locator not found. Cannot click on the element with locator: " + locator +
                          "locator_type: " + locator_type)

    def send_keys(self, data, locator="", locator_type="xpath", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
                assert element is not None, (
                        "locator not found. Cannot send data on the element with locator: " + locator +
                        " locator_type: " + locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locator_type: " + locator_type)
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(element + ' ' + 'not found')
            raise
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locator_type: " + locator_type)
            raise

    def clear_field(self, locator="", locator_type="xpath"):
        """
        Clear an element field
        """
        element = self.get_element(locator, locator_type)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locator_type: " + locator_type)

    def get_text(self, locator="", locator_type="xpath", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
                assert element is not None, ("Locator not found. Failed to get text on element " + info)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(element + ' ' + 'not found ')
            raise
        except:
            self.log.error("Failed to get text on element " + info)
            text = None
        return text

    def is_element_present(self, locator="", locator_type="xpath", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
                assert element is None, ("Locator not found. Element not present with locator: " + locator +
                                         " locator_type: " + locator_type)
                return False
            else:
                self.log.info("Element present with locator: " + locator +
                              " locator_type: " + locator_type)
                return True
        except AssertionError as msg:
            self.log.info(msg)
            raise
        except:
            self.log.info("Element not found")
            return False

    def is_element_displayed(self, locator="", locator_type="xpath", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                assert element.is_displayed() == True, "Element is not displaying on the page."
            # else:
            #     self.log.info("Element not displayed")
            # return isDisplayed
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(element + ' ' + 'not found')
            raise

    def element_presence_check(self, locator, by_type="xpath"):
        """
        Check if element is present
        """
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locator_type: " + str(by_type))
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locator_type: " + str(by_type))
                return False
        except:
            self.log.info("Element not found")

    def wait_for_element(self, locator, locator_type="xpath",
                         timeout=30, poll_frequency=1):
        element = None
        try:
            byType = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            assert element is not None, ("Element not present with locator: " + locator +
                                         " locator_type: " + locator_type)
            self.log.info("Element appeared on the web page")
        except AssertionError as msg:
            self.log.info(msg)
            raise
        except:
            self.log.info("Element not appeared on the web page")
        return element

    def web_scroll(self, direction="up"):
        """
        To scroll the web page up and down
        """
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string

        Parameters:
            expected_text: Expected Text
            actual_text: Actual Text
        """
        try:
            self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
            self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
            assert expected_text.lower() in actual_text.lower(), (
                    f"Actual text mismatched with the expected text." + '' + "Expected text = "
                    + str(expected_text) + ' ' + " and Actual text = " + str(actual_text))
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(expected_text + ' ' + 'not matching ')
            raise
        else:
            self.log.info("### VERIFICATION CONTAINS !!! Actual text contain expected text.")

    def verify_text_match(self, actual_text, expected_text):
        """
        Verify actual text match with the expected text.

        Parameters:
            expected_text: Expected Text
            actual_text: Actual Text
        """
        try:
            self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
            self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
            assert expected_text.lower() == actual_text.lower(), (
                    f"Actual text mismatched with the expected text." + '' + "Expected text = "
                    + str(expected_text) + ' ' + " and Actual text = " + str(actual_text))
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(expected_text + ' ' + 'not matching ')
            raise
        else:
            self.log.info("### VERIFICATION CONTAINS !!! Actual text matched with the expected text.")

    def verify_email_confirmation(self, name, flow):
        """
        Call gmail api to fetch Gmail inbox to get registered email.
        Parameters:
            name: name after plus in the registered user email
            :param flow: it defines user is validating email from which flow.

        """
        # SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
        # store = file.Storage('token.json')
        # creds = store.get()
        # path = os.path.abspath("./credentials.json")
        # if not creds or creds.invalid:
        #     flow = client.flow_from_clientsecrets(path,
        #                                           SCOPES)
        #     creds = tools.run_flow(flow, store)
        # service = build('gmail', 'v1', http=creds.authorize(Http()))
        #
        # creds = None
        #
        # # The file token.pickle contains the user access token.
        # # Check if it exists
        # if os.path.exists('token.pickle'):
        #     # Read the token from the file and store it in the variable creds
        #     with open('token.pickle', 'rb') as token:
        #         creds = pickle.load(token)
        #
        # # If credentials are not available or are invalid, ask the user to log in.
        # if not creds or not creds.valid:
        #     if creds and creds.expired and creds.refresh_token:
        #         creds.refresh(Request())
        #     else:
        #         flow = InstalledAppFlow.from_client_secrets_file('./credentials.json', SCOPES)
        #         creds = flow.run_local_server(port=0)
        #
        #     # Save the access token in token.pickle file for the next run
        #     with open('token.pickle', 'wb') as token:
        #         pickle.dump(creds, token)
        # service = build('gmail', 'v1', credentials=creds)
        SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
        # store = file.Storage('token.json')
        # creds = store.get()
        # path = os.path.abspath("./credentials.json")
        # if not creds or creds.invalid:
        #     flow = client.flow_from_clientsecrets(path,
        #                                           SCOPES)
        #     creds = tools.run_flow(flow, store)
        # service = build('gmail', 'v1', http=creds.authorize(Http()))
        creds = None
        # The file token.pickle contains the user access token.
        # Check if it exists
        if os.path.exists('token.pickle'):
            # Read the token from the file and store it in the variable creds
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If credentials are not available or are invalid, ask the user to log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('./credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the access token in token.pickle file for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('gmail', 'v1', credentials=creds)

        # Call the Gmail API to fetch INBOX
        if flow == 'register':
            subject_line = "Confirm Sila Account"
        elif flow == 'reset_password':
            subject_line = "Sila Password Reset"
        else:
            subject_line = "Sila Invitation"
        search = 'to:' + name + ',subject:' + subject_line
        results = service.users().messages().list(userId='me', q=search,
                                                  labelIds=['INBOX']).execute()
        print(results)
        messages = results.get('messages', [])

        if not messages:
            print("No messages found.")
        else:
            print("Message snippets:")
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                data = msg['payload']['body']['data']
                decoded_data = base64.urlsafe_b64decode(data)
                decoded_data = decoded_data.decode('utf-8')
                print(msg['snippet'])
                print(decoded_data)
                url = (re.findall("(?P<url>https?://[^\s]+)", decoded_data))
                if flow == 'register':
                    console = "account/confirm/"
                    strings_with_substring = [string for string in url if console in string]
                    strings_with_substring = strings_with_substring[0]
                    return strings_with_substring
                elif flow == 'reset_password':
                    console = "/account/reset_password/"
                    strings_with_substring = [string for string in url if console in string]
                    strings_with_substring = strings_with_substring[0]
                    print(strings_with_substring)
                    return strings_with_substring
                elif flow == "invitation":
                    console = "/invitation/"
                    strings_with_substring = [string for string in url if console in string]
                    strings_with_substring = strings_with_substring[0]
                    return strings_with_substring

    def get_mfa_code(self, name):
        """
        Call gmail api to fetch Gmail inbox to get registered email.
        Parameters:
            name: name after plus in the registered user email
            :param flow: it defines user is validating email from which flow.

        """
        SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
        # store = file.Storage('token.json')
        # creds = store.get()
        # path = os.path.abspath("./credentials.json")
        # if not creds or creds.invalid:
        #     flow = client.flow_from_clientsecrets(path,
        #                                           SCOPES)
        #     creds = tools.run_flow(flow, store)
        # service = build('gmail', 'v1', http=creds.authorize(Http()))
        creds = None
        # The file token.pickle contains the user access token.
        # Check if it exists
        if os.path.exists('token.pickle'):
            # Read the token from the file and store it in the variable creds
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If credentials are not available or are invalid, ask the user to log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('./credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the access token in token.pickle file for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('gmail', 'v1', credentials=creds)
        # Call the Gmail API to fetch INBOX
        search = 'to:' + name + ',subject:Sila Console Verification Code'
        results = service.users().messages().list(maxResults=1, userId='me', q=search,
                                                  labelIds=['INBOX']).execute()
        messages = results.get('messages', [])
        if not messages:
            print("No messages found.")
        else:
            print("Message snippets:")
            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                message = (msg['snippet'])
                print(message)
                mfa_code = re.split('[!]', message)
                mfa_code = mfa_code[1]
                mfa_code = mfa_code[1:7]
                print(mfa_code)
                return mfa_code

    def check_element_state(self, locator="", locator_type="xpath", value=False, element_name=''):
        """
        Check whether element is in disable state or not
        Click on an element -> Either provide element or a combination of locator and locator_type
        :param
            value : boolean value, default is false i.e element is in disable state.
            element_name : it could be either button name  or anything
        """
        try:
            if locator:  # This means if locator is not empty
                time.sleep(2)
                element = self.get_element(locator, locator_type)
                assert element.is_enabled() == value, (element_name + " is not in a disable state")
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(element_name + ' ' + 'is not in a disable state')
            raise
        except:
            self.log.info("Locator not found. Cannot click on the element with locator: " + locator +
                          "locator_type: " + locator_type)

    def link_redirect(self, locator="", locator1='', expected_text='', name='', locator_type="xpath"):
        try:
            if locator:  # This means if locator is not empty
                time.sleep(2)
                window_before = self.driver.window_handles[0]
                element = self.element_click(locator, locator_type)
                assert element is None, ("Locator not found. Element not present with locator: " + locator +
                                         " locator_type: " + locator_type)
                window_after = self.driver.window_handles[1]
                # switch on to new child window
                self.driver.switch_to.window(window_after)
                time.sleep(1)

                if name == "title":
                    title = self.get_title()
                    if title != "404 Not Found":
                        print("--------------------")
                        self.verify_text_match(title, expected_text)
                        time.sleep(1)
                        self.driver.close()
                        self.driver.switch_to.window(window_before)
                    else:
                        time.sleep(1)
                        # self.verify_text_match(title, expected_text)
                        self.driver.close()
                        self.driver.switch_to.window(window_before)
                else:
                    element = self.get_element(locator1, locator_type)
                    assert element is not None, ("Failed to get locator on new window", self.driver.close(),
                                                 self.driver.switch_to.window(window_before))
                    text = self.get_text(locator1, locator_type)
                    self.verify_text_match(text, expected_text)
                    self.driver.close()
                    self.driver.switch_to.window(window_before)
                    time.sleep(1)
                # if element == None:
                #     self.driver.close()
                #     self.driver.switch_to.window(window_before)
                # else:
                #     text = self.get_text(locator1, locator_type)
                #     self.verify_text_match(text, expected_text)
                #     self.driver.close()
                #     self.driver.switch_to.window(window_before)
                #     time.sleep(1)
        except AssertionError as msg:
            self.log.info(msg)
            name = datetime.datetime.today().strftime('%Y-%m-%d-%M-%S')
            allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)
            self.get_screenshot(locator + ' ' + 'not found')
            raise
        except:
            self.log.info("Locator not found. Cannot click on the element with locator: " + locator +
                          "locator_type: " + locator_type)

    def move_to_frame(self):
        """move to frames"""
        try:
            time.sleep(2)
            frame = ActionChains(self.driver)
            frame.move_to_element(self.driver.find_element(By.XPATH, iframe_path)).send_keys(" amit").perform()
            time.sleep(2)
            frame.send_keys(Keys.ESCAPE).perform()
        except:
            self.log.info("frame not found")
            raise
    #
    # def keyboard_tab(self):
    #     try:
    #         time.sleep(2)
    #         tab = ActionChains(self.driver)
    #         tab.send_keys(Keys.TAB).perform()
    #         time.sleep(2)
    #         # tab.send_keys(Keys.SHIFT+Keys.TAB).perform()
    #     except:
    #         self.log.info("Tab is not working")
    #         raise
    #






