from lib.base import BasePageClass
from lib.base import InvalidPageException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class HomePage(BasePageClass):
    _home_page_landing_logo_locator = "//*[@id='page_content']/div[1]/div[1]/span"
    _home_page_login_link_locator = "Or log in"

    def __init__(cls, driver):
        super(HomePage,cls).__init__(driver)

    @property
    def loginlink(cls):
        WebDriverWait(cls.driver, 20).until(EC.presence_of_element_located(
            (By.LINK_TEXT, cls._home_page_login_link_locator )))
        return cls.driver.find_element_by_link_text(cls._home_page_login_link_locator)

    def _validate_page(cls, driver):
        try:
            driver.find_element_by_xpath(cls._home_page_landing_logo_locator)
        except:
            raise InvalidPageException("Home Page not loaded")