from lib.base import BasePageClass
from lib.base import InvalidPageException
import json, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.homepage import HomePage
from pages.IconListPage import IconListPage
import inspect
from basepage import BasePage


cwd = os.getcwd()
os.chdir('..')
json_path= "data"+os.sep+"json_login.json"
L1 = os.path.join(os.getcwd(),"data","json_login.json")
os.chdir(cwd)

class LoginPage(BasePageClass):
    _login_big_logo_id_locator = "largelogo"
    _email_input_id_locator     = "inputusername"
    _password_input_id_locator  = "inputpassword"
    _login_click_xpath_locator  = "//*[@id='li-buttons']/button[1]" #"//form[@id='login_form']/li[3]/button"
    _login_main_register_id_locator = "buttonregister"

    _login_error_id_locator = "loginerrorspan"


    # Register
    _register_username_email_input_id_locator = "inputregusername"
    _register_first_name_input_id_locator = "inputregfirstname"
    _register_last_name_input_id_locator = "inputreglastname"
    _register_password_1_input_id_locator = "inputregpassword1"
    _register_password_2_input_id_locator = "inputregpassword2" # inputregpassword2
    _register_13_year_check_box_xpath_locator = ".//*[@id='inputregageli']/label/span/span[2]"
    _register_agree_service_terms_check_box_xpath_locator = ".//*[@id='inputusepolicyli']/label/span/span[2]"
    _register_register_button_id_locator = "buttonregisterregister" #"registerbuttonsli"
    _register_cancel_button_id_locator = "buttonregistercancel"
    _register_error_id_locator = "registererrorspan"
    _register_error_xpath_locator = ".//*[@id='registererror']/p[2]"

    # Forgot password
    _forgot_pwd_reset_password_id_locator = "buttonresetpassword"
    _forgot_pwd_input_username_id_locator = "inputforgotusername"
    _forgot_pwd_reset_id_locator = "buttonforgotsubmit"
    _forgot_pwd_error_id_locator = "forgotnoticespan"

    usernameText = ""

    def __init__(cls,driver):
        super(LoginPage,cls).__init__(driver)

    @property
    def get_big_logo(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._login_big_logo_id_locator)))
            return cls.driver.find_element_by_id(cls._login_big_logo_id_locator)
        except Exception, err:
            raise type(err)("Big Logo - searched ID - "
                            + cls._login_big_logo_id_locator + err.message)

    @property
    def email(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._email_input_id_locator)))
            return cls.driver.find_element_by_id(cls._email_input_id_locator)
        except Exception, err:
            raise type(err)("login email - searched ID - "
                            + cls._email_input_id_locator + err.message)

    @property
    def password(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._password_input_id_locator)))
            return cls.driver.find_element_by_id(cls._password_input_id_locator)
        except Exception, err:
            raise type(err)("login password - searched ID - "
                            + cls._password_input_id_locator + err.message)

    @property
    def login(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, cls._login_click_xpath_locator)))
            return cls.driver.find_element_by_xpath(cls._login_click_xpath_locator)
        except Exception, err:
            raise type(err)("login button - searched XPATH - "
                            + cls._login_click_xpath_locator + err.message)

    @property
    def loginerror(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._login_error_id_locator)))
            return cls.driver.find_element_by_id(cls._login_error_id_locator)
        except Exception, err:
            raise type(err)("login error status message - searched ID - "
                            + cls._login_error_id_locator + err.message)
    # _login_main_register_id_locator

    @property
    def get_login_main_register(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._login_main_register_id_locator)))
            return cls.driver.find_element_by_id(cls._login_main_register_id_locator)
        except Exception, err:
            raise type(err)("Main Register button - searched ID - "
                            + cls._login_main_register_id_locator + err.message)

    # Register related
    @property
    def get_register_username_email(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._register_username_email_input_id_locator)))
            return cls.driver.find_element_by_id(cls._register_username_email_input_id_locator)
        except Exception, err:
            raise type(err)("register username - searched ID - "
                            + cls._register_username_email_input_id_locator + err.message)

    @property
    def get_register_first_name(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._register_first_name_input_id_locator)))
            return cls.driver.find_element_by_id(cls._register_first_name_input_id_locator)
        except Exception, err:
            raise type(err)("register first name - searched ID - "
                            + cls._register_first_name_input_id_locator + err.message)

    @property
    def get_register_last_name(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._register_last_name_input_id_locator)))
            return cls.driver.find_element_by_id(cls._register_last_name_input_id_locator)
        except Exception, err:
            raise type(err)("register last name - searched ID - "
                            + cls._register_last_name_input_id_locator + err.message)

    @property
    def get_register_password_1(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._register_password_1_input_id_locator)))
            return cls.driver.find_element_by_id(cls._register_password_1_input_id_locator)
        except Exception, err:
            raise type(err)("register password 1 - searched ID - "
                            + cls._register_password_1_input_id_locator + err.message)

    @property
    def get_register_password_2(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._register_password_2_input_id_locator)))
            return cls.driver.find_element_by_id(cls._register_password_2_input_id_locator)
        except Exception, err:
            raise type(err)("register password 2 - searched ID - "
                            + cls._register_password_2_input_id_locator + err.message)

    @property
    def get_register_13_year(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, cls._register_13_year_check_box_xpath_locator)))
            return cls.driver.find_element_by_xpath(cls._register_13_year_check_box_xpath_locator)
        except Exception, err:
            raise type(err)("I am 13 years or older - searched XPATH - "
                            + cls._register_13_year_check_box_xpath_locator + err.message)

    @property
    def get_register_agree_service_terms(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, cls._register_agree_service_terms_check_box_xpath_locator)))
            return cls.driver.find_element_by_xpath(cls._register_agree_service_terms_check_box_xpath_locator)
        except Exception, err:
            raise type(err)("I agree to the terms of service policy - searched XPATH - "
                            + cls._register_agree_service_terms_check_box_xpath_locator + err.message)
    
    @property
    def get_register_register(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._register_register_button_id_locator)))
            return cls.driver.find_element_by_id(cls._register_register_button_id_locator)
        except Exception, err:
            raise type(err)("register button - searched ID - "
                            + cls._register_register_button_id_locator + err.message)
    
    @property
    def get_register_cancel(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._register_cancel_button_id_locator)))
            return cls.driver.find_element_by_id(cls._register_cancel_button_id_locator)
        except Exception, err:
            raise type(err)("cancel button - searched ID - "
                            + cls._register_cancel_button_id_locator + err.message)
    
    @property
    def get_register_error_status_message(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._register_error_id_locator)))
            return cls.driver.find_element_by_id(cls._register_error_id_locator)
        except Exception, err:
            raise type(err)("Register error status message - searched ID - "
                            + cls._register_error_id_locator + err.message)

    @property
    def get_register_error_password_status_message(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, cls._register_error_xpath_locator)))
            return cls.driver.find_element_by_xpath(cls._register_error_xpath_locator)
        except Exception, err:
            raise type(err)("Register error password status message - searched class name - "
                            + cls._register_error_xpath_locator + err.message)

    #
    @property
    def get_reset_password(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._forgot_pwd_reset_password_id_locator)))
            return cls.driver.find_element_by_id(cls._forgot_pwd_reset_password_id_locator)
        except Exception, err:
            raise type(err)("Reset password button - searched ID - "
                            + cls._forgot_pwd_reset_password_id_locator + err.message)

    #
    @property
    def get_forgot_pwd_username(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._forgot_pwd_input_username_id_locator)))
            return cls.driver.find_element_by_id(cls._forgot_pwd_input_username_id_locator)
        except Exception, err:
            raise type(err)("Forgot password user email - searched ID - "
                            + cls._forgot_pwd_input_username_id_locator + err.message)

    @property
    def get_forgot_pwd_reset(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._forgot_pwd_reset_id_locator)))
            return cls.driver.find_element_by_id(cls._forgot_pwd_reset_id_locator)
        except Exception, err:
            raise type(err)("Forgot password reset button - searched ID - "
                            + cls._forgot_pwd_reset_id_locator + err.message)

    @property
    def get_forgot_pwd_error_status_message(cls):
        try:
            WebDriverWait(cls.driver,10).until(expected_conditions.presence_of_element_located(
                (By.ID, cls._forgot_pwd_error_id_locator)))
            return cls.driver.find_element_by_id(cls._forgot_pwd_error_id_locator)
        except Exception, err:
            raise type(err)("Forgot password error status message - searched ID - "
                            + cls._forgot_pwd_error_id_locator + err.message)


    def loginDashboard(cls):
        with open(L1) as data_file:
            data_text = json.load(data_file)
            for each in data_text:
                cls.usernameText = each["username"]
                passwordText = each["password"]
                sleep(5)
                cls.email.clear()
                sleep(5)
                cls.email.send_keys(cls.usernameText)
                sleep(5)
                cls.password.clear()
                sleep(5)
                cls.password.send_keys(passwordText)
                sleep(5)
                cls.login.click()

    def clearallfields(cls):
        cls.get_register_username_email.clear()
        cls.get_register_first_name.clear()
        cls.get_register_last_name.clear()
        cls.get_register_password_1.clear()
        cls.get_register_password_2.clear()

    def _validate_page(cls, driver):
        try:
            WebDriverWait(driver, 20).until(expected_conditions.presence_of_all_elements_located(
                (By.ID, cls._email_input_id_locator)))
        except:
            try:
                HomePage(driver)._validate_page(driver)
                HomePage(driver).loginlink.click()
            except:
                raise InvalidPageException("Login page not loaded")

    def return_to_apps_main_page(self):
        """
        Description : This function will helps to go back to assets page.
        Revision:
        :return: None
        """
        #if not self.email:
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, self.login))).click()

            #WebDriverWait(self.driver, 50).until(expected_conditions.presence_of_element_located(
            #    (By.XPATH, IconListPage(self.driver)._app_map_icon_locator)),"Map Icon")

        except:
            inspectstack = inspect.stack()[1][3]
            self.recoverapp(inspectstack)


    def recoverapp(self, inspectstack):
        """
        Description : This function helps to go back to assets page. Inspect stack prints the test name from which
                                 this function is called.
        Revision:
        :return: None
        """
        print ("Application recovering called from " + inspectstack)
        basepage = BasePage(self.driver)
        basepage.loginURL()
        #iconlistpage = IconListPage(self.driver)
        #iconlistpage.get_loggedin_username.click()
        #iconlistpage.get_logout.click()
