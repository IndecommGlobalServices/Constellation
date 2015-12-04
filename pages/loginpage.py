from lib.base import BasePageClass
from lib.base import InvalidPageException
import json, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


cwd = os.getcwd()
os.chdir('..')
json_path= "data"+os.sep+"json_login.json"
L1 = os.path.join(os.getcwd(),"data","json_login.json")
os.chdir(cwd)

class LoginPage(BasePageClass):
    _login_big_logo_id_locator = "largelogo"
    _email_input_id_locator     = "inputusername"
    _password_input_id_locator  = "inputpassword"
    _login_click_xpath_locator  = "//form[@id='login_form']/li[3]/button"
    _login_main_register_id_locator = "buttonregister"

    _login_error_id_locator = "loginerrorspan"


    # Register
    _register_username_email_input_id_locator = "inputregusername"
    _register_first_name_input_id_locator = "inputregfirstname"
    _register_last_name_input_id_locator = "inputreglastname"
    _register_password_1_input_id_locator = "inputregpassword1"
    _register_password_2_input_id_locator = "inputregpassword2"
    _register_13_year_check_box_xpath_locator = ".//*[@id='inputregageli']/label/span/span[2]"
    _register_agree_service_terms_check_box_xpath_locator = ".//*[@id='inputusepolicyli']/label/span/span[2]"
    _register_register_button_id_locator = "buttonregisterregister"
    _register_cancel_button_id_locator = "buttonregistercancel"
    _register_error_id_locator = "registererrorspan"
    _register_error_xpath_locator = ".//*[@id='registererror']/p[2]"

    # Forgot password
    _forgot_pwd_reset_password_id_locator = "buttonresetpassword"
    _forgot_pwd_input_username_id_locator = "inputforgotusername"
    _forgot_pwd_reset_id_locator = "buttonforgotsubmit"
    _forgot_pwd_error_id_locator = "forgotnoticespan"

    usernameText = ""

    def __init__(self,driver):
        super(LoginPage,self).__init__(driver)

    # _login_big_logo_id_locator

    @property
    def get_big_logo(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._login_big_logo_id_locator)))
            return self.driver.find_element_by_id(self._login_big_logo_id_locator)
        except Exception, err:
            raise type(err)("Big Logo - searched ID - "
                            + self._login_big_logo_id_locator + err.message)

    @property
    def email(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._email_input_id_locator)))
            return self.driver.find_element_by_id(self._email_input_id_locator)
        except Exception, err:
            raise type(err)("login email - searched ID - "
                            + self._email_input_id_locator + err.message)

    @property
    def password(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._password_input_id_locator)))
            return self.driver.find_element_by_id(self._password_input_id_locator)
        except Exception, err:
            raise type(err)("login password - searched ID - "
                            + self._password_input_id_locator + err.message)

    @property
    def login(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._login_click_xpath_locator)))
            return self.driver.find_element_by_xpath(self._login_click_xpath_locator)
        except Exception, err:
            raise type(err)("login button - searched XPATH - "
                            + self._login_click_xpath_locator + err.message)

    @property
    def loginerror(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._login_error_id_locator)))
            return self.driver.find_element_by_id(self._login_error_id_locator)
        except Exception, err:
            raise type(err)("login error status message - searched ID - "
                            + self._login_error_id_locator + err.message)
    # _login_main_register_id_locator

    @property
    def get_login_main_register(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._login_main_register_id_locator)))
            return self.driver.find_element_by_id(self._login_main_register_id_locator)
        except Exception, err:
            raise type(err)("Main Register button - searched ID - "
                            + self._login_main_register_id_locator + err.message)

    # Register related
    @property
    def get_register_username_email(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._register_username_email_input_id_locator)))
            return self.driver.find_element_by_id(self._register_username_email_input_id_locator)
        except Exception, err:
            raise type(err)("register username - searched ID - "
                            + self._register_username_email_input_id_locator + err.message)

    @property
    def get_register_first_name(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._register_first_name_input_id_locator)))
            return self.driver.find_element_by_id(self._register_first_name_input_id_locator)
        except Exception, err:
            raise type(err)("register first name - searched ID - "
                            + self._register_first_name_input_id_locator + err.message)

    @property
    def get_register_last_name(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._register_last_name_input_id_locator)))
            return self.driver.find_element_by_id(self._register_last_name_input_id_locator)
        except Exception, err:
            raise type(err)("register last name - searched ID - "
                            + self._register_last_name_input_id_locator + err.message)

    @property
    def get_register_password_1(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._register_password_1_input_id_locator)))
            return self.driver.find_element_by_id(self._register_password_1_input_id_locator)
        except Exception, err:
            raise type(err)("register password 1 - searched ID - "
                            + self._register_password_1_input_id_locator + err.message)

    @property
    def get_register_password_2(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._register_password_2_input_id_locator)))
            return self.driver.find_element_by_id(self._register_password_2_input_id_locator)
        except Exception, err:
            raise type(err)("register password 2 - searched ID - "
                            + self._register_password_2_input_id_locator + err.message)

    @property
    def get_register_13_year(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._register_13_year_check_box_xpath_locator)))
            return self.driver.find_element_by_xpath(self._register_13_year_check_box_xpath_locator)
        except Exception, err:
            raise type(err)("I am 13 years or older - searched XPATH - "
                            + self._register_13_year_check_box_xpath_locator + err.message)

    @property
    def get_register_agree_service_terms(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._register_agree_service_terms_check_box_xpath_locator)))
            return self.driver.find_element_by_xpath(self._register_agree_service_terms_check_box_xpath_locator)
        except Exception, err:
            raise type(err)("I agree to the terms of service policy - searched XPATH - "
                            + self._register_agree_service_terms_check_box_xpath_locator + err.message)
    
    @property
    def get_register_register(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._register_register_button_id_locator)))
            return self.driver.find_element_by_id(self._register_register_button_id_locator)
        except Exception, err:
            raise type(err)("register button - searched ID - "
                            + self._register_register_button_id_locator + err.message)
    
    @property
    def get_register_cancel(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._register_cancel_button_id_locator)))
            return self.driver.find_element_by_id(self._register_cancel_button_id_locator)
        except Exception, err:
            raise type(err)("cancel button - searched ID - "
                            + self._register_cancel_button_id_locator + err.message)
    
    @property
    def get_register_error_status_message(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._register_error_id_locator)))
            return self.driver.find_element_by_id(self._register_error_id_locator)
        except Exception, err:
            raise type(err)("Register error status message - searched ID - "
                            + self._register_error_id_locator + err.message)

    @property
    def get_register_error_password_status_message(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._register_error_xpath_locator)))
            return self.driver.find_element_by_xpath(self._register_error_xpath_locator)
        except Exception, err:
            raise type(err)("Register error password status message - searched class name - "
                            + self._register_error_xpath_locator + err.message)

    #
    @property
    def get_reset_password(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._forgot_pwd_reset_password_id_locator)))
            return self.driver.find_element_by_id(self._forgot_pwd_reset_password_id_locator)
        except Exception, err:
            raise type(err)("Reset password button - searched ID - "
                            + self._forgot_pwd_reset_password_id_locator + err.message)

    #
    @property
    def get_forgot_pwd_username(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._forgot_pwd_input_username_id_locator)))
            return self.driver.find_element_by_id(self._forgot_pwd_input_username_id_locator)
        except Exception, err:
            raise type(err)("Forgot password user email - searched ID - "
                            + self._forgot_pwd_input_username_id_locator + err.message)

    @property
    def get_forgot_pwd_reset(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._forgot_pwd_reset_id_locator)))
            return self.driver.find_element_by_id(self._forgot_pwd_reset_id_locator)
        except Exception, err:
            raise type(err)("Forgot password reset button - searched ID - "
                            + self._forgot_pwd_reset_id_locator + err.message)

    @property
    def get_forgot_pwd_error_status_message(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, self._forgot_pwd_error_id_locator)))
            return self.driver.find_element_by_id(self._forgot_pwd_error_id_locator)
        except Exception, err:
            raise type(err)("Forgot password error status message - searched ID - "
                            + self._forgot_pwd_error_id_locator + err.message)


    def loginDashboard(self):
        with open(L1) as data_file:
            data_text = json.load(data_file)
            for each in data_text:
                self.usernameText = each["username"]
                passwordText = each["password"]
                self.email.clear()
                self.email.send_keys(self.usernameText)
                self.password.clear()
                self.password.send_keys(passwordText)
                self.login.click()

    def clearallfields(self):
        self.get_register_username_email.clear()
        self.get_register_first_name.clear()
        self.get_register_last_name.clear()
        self.get_register_password_1.clear()
        self.get_register_password_2.clear()

    def _validate_page(self, driver):
        try:
            driver.find_element_by_id(self._email_input_id_locator)
        except:
            raise InvalidPageException("Login page not loaded")
