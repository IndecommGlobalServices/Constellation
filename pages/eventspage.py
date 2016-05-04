__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.basepage import BasePage


class EventsPage(BasePageClass, object):


    _app_events_appname_locator = ".//*[@id='header']/span[2]/span"
    _app_events_Type_dropdown_locator = "//div[@model='filter.value']//button[contains(text(), 'Type')]"
    _app_events_main_create_button_locator = "//img[@ng-src='../images/icon_create_item_off.png']"

    @property
    def get_events_app_name_label(self):
        return self.basepage.findElementByXpath(self._app_events_appname_locator)

    @property
    def get_Type_dropdown(self):
        try:
            return self.basepage.findElementByXpath(self._app_events_Type_dropdown_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._app_events_Type_dropdown_locator + err.message)

    @property
    def get_main_create_incident_button(self):
        try:
            return self.basepage.findElementByXpath(self._app_events_main_create_button_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._app_events_main_create_button_locator + err.message)

    def __init__(self, driver):
        super(EventsPage,self).__init__(driver)
        self.basepage = BasePage(self.driver)


