from lib.base import BasePageClass
from lib.base import InvalidPageException
import json, os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.homepage import HomePage

cwd = os.getcwd()
os.chdir('..')
json_path= "data"+os.sep+"json_login.json"
L1 = os.path.join(os.getcwd(),"data","json_login.json")
os.chdir(cwd)

class LoginPage(BasePageClass):
    _email_input_id_locator     = "inputusername"
    _password_input_id_locator  = "inputpassword"
    _login_click_xpath_locator  = "//form[@id='login_form']/li[3]/button"
    usernameText = ""

    def __init__(cls,driver):
        super(LoginPage,cls).__init__(driver)

    @property
    def email(cls):
        return cls.driver.find_element_by_id(cls._email_input_id_locator)

    @property
    def password(cls):
        return cls.driver.find_element_by_id(cls._password_input_id_locator)

    @property
    def login(cls):
        return cls.driver.find_element_by_xpath(cls._login_click_xpath_locator)


    def loginDashboard(self):
        with open(L1) as data_file:
            data_text = json.load(data_file)
            for each in data_text:
                self.usernameText = each["username"]
                passwordText = each["password"]
                self.email.send_keys(self.usernameText)
                self.password.send_keys(passwordText)
                self.login.click()


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
