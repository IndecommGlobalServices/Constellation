from lib.base import BasePage
from lib.base import InvalidPageException

class LoginPage(BasePage):
    _email_input_id_locator     = "inputusername"
    _password_input_id_locator  = "inputpassword"
    _login_click_xpath_locator  = "//form[@id='login_form']/li[3]/button"

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


    def _validate_page(cls, driver):
        try:
            driver.find_element_by_id(cls._email_input_id_locator)
        except:
            raise InvalidPageException("Login page not loaded")
