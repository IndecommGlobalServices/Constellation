__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.basepage import BasePage


class TimelinePage(BasePageClass, object):


    _app_timeline_appname_locator = ".//*[@id='header']/div[1]/span[2]/span"

    @property
    def get_timeline_app_name_label(self):
        try:
            return self.basepage.findElementByXpath(self._app_timeline_appname_locator)
        except Exception, err:
            raise type(err)("Timeline app name label is not found " \
                          + err.message)


    def __init__(self, driver):
        super(TimelinePage,self).__init__(driver)
        self.basepage = BasePage(self.driver)


