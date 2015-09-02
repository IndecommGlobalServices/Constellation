__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException

class BasePage(BasePageClass):
    _home_page_landing_logo_locator = "//*[@id='page_content']/div[1]/div[1]/span"

    def __init__(cls, driver):
        super(BasePage,cls).__init__(driver)

    def accessURL(self):
        self.driver.get("https://constellation-qa.haystax.com/#/")
