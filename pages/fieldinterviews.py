__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.basepage import BasePage


class FieldInterviewsPage(BasePageClass, object):


    _app_fieldinterviews_appname_locator = ".//*[@id='header']/span[2]/span"
    _app_fieldinterviews_Contacttype_dropdown_locator = "//div[@model='filter.value']//button[contains(text(), 'Contact type')]"

    @property
    def get_fieldinterviews_app_name_label(self):
        return self.basepage.findElementByXpath(self._app_fieldinterviews_appname_locator)

    @property
    def get_Contacttype_dropdown(self):
        try:
            return self.basepage.findElementByXpath(self._app_fieldinterviews_Contacttype_dropdown_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._app_fieldinterviews_Contacttype_dropdown_locator + err.message)


    def __init__(self, driver):
        super(FieldInterviewsPage,self).__init__(driver)
        self.basepage = BasePage(self.driver)


