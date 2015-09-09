from selenium.webdriver.common.keys import Keys
from lib.base import BasePageClass
from lib.base import InvalidPageException
from pages.IconListPage import IconListPage
from basepage import BasePage
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os, json


class AssessmentPage(BasePageClass):

    _app = ".//*[@id='header']/span[2]/span"

    def __init__(self, driver):
        super(AssessmentPage, self).__init__(driver)
        appicon = IconListPage(self)
        appicon.click_assessments_icon()

    @property
    def get_app(self):
        return self.driver.find_element_by_id(self._app)

    def _validate_page(self, driver):
        pass