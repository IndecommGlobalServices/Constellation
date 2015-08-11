from lib.base import BasePage
from lib.base import InvalidPageException
import csv
from ddt import ddt, data, unpack
from lib import loginData

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


    def get_data(file_name):
        # create an empty list to store rows
        rows = []

        # open the CSV file
        data_file = open(file_name, "rb")

        # create a CSV Reader from CSV file
        reader = csv.reader(data_file)

        # skip the headers
        next(reader, None)

        # add rows from reader to list
        for row in reader:
            rows.append(row)
        return rows
    '''
    @ddt
    @data(loginData.get_data("D:\Project\Constellation\data\loginData1.csv"))
    @unpack
    def test_Login(self, username, password):
    '''



    def _validate_page(cls, driver):
        try:
            driver.find_element_by_id(cls._email_input_id_locator)
        except:
            raise InvalidPageException("Login page not loaded")
