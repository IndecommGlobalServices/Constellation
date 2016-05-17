__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.basepage import BasePage
import sys
from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from basepage import BasePage
from time import sleep
from loginpage import LoginPage
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os, json, inspect
from selenium.webdriver.common.action_chains import ActionChains


class EventsPage(BasePageClass, object):


    _app_events_appname_locator = "//span[contains(text(),'Events')]"
    _app_events_Type_dropdown_locator = "//div[@model='filter.value']//button[contains(text(), 'Type')]"
    _app_events_main_create_button_locator = "//img[@ng-src='../images/icon_create_item_off.png']"
    _event_link_delete_text_xpath_locator = ".//*[@id='event_actions_dropdown']/ul/li/a"


    # Events Delete related locators
    _event_select_action_delete_select_xpath_locator = ".//*[@id='event_actions_dropdown']/button[text()='Select action']/following-sibling::button"

    # New Event creation related
    #_asset_create_asset = "//img[@alt='Create asset']"
    _event_create_event = "//img[@ng-src='../images/icon_create_item_off.png']"

    _event_link_locator = "Events"

    _event_list_event_name_black_color_locator = "//*[@id='eventsTable']/tbody/tr/td[2]"


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

    @property
    def get_event_select_action_drop_down(self):
        try:
            return self.driver.find_element_by_xpath(self._event_select_action_delete_select_xpath_locator)
        except Exception, err:
            raise type(err)("Select Action drop down not available - searched XPATH - " \
                          + self._event_select_action_delete_select_xpath_locator + err.message)

    @property
    def get_event_name_list(self):
        try:
            #return  self.driver.find_elements_by_xpath(self._asset_list_asset_name_black_color_locator)
            return self.basepage.findElementsByXpath(self._event_list_event_name_black_color_locator)
        except Exception, err:
            raise type(err)("Black color in the list not available after insertion - searched XPATH - " \
                          + self._event_list_event_name_black_color_locator + err.message)

    @property
    def get_event_link_delete_text(self):
        try:
            #return self.driver.find_element_by_xpath(self._asset_link_delete_text_xpath_locator)
            return self.basepage.findElementByXpath(self._event_link_delete_text_xpath_locator)
        except Exception, err:
            raise type(err)("Delete option not present in the select action dropdown - searched XPATH - " \
                          + self._event_link_delete_text_xpath_locator + err.message)


    def __init__(self, driver):
        super(EventsPage,self).__init__(driver)
        self.basepage = BasePage(self.driver)


    def open_event_app(self):
        loginpage = LoginPage(self.driver)
        loginpage.loginDashboard()
        appicon = IconListPage(self.driver)
        appicon.click_events_icon()

    @property
    def get_event_create_event(self):
        try:
            self.driver.find_element_by_xpath(self._event_create_event)
        except:
            return False
        return True


    def return_to_apps_main_page(self):
        """
        Description : This function will helps to go back to events page.
        Revision:
        :return: None
        """
        if not self.get_event_create_event:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                    (By.LINK_TEXT, self._event_link_locator))).click()
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self._event_create_event)))
            except:
                inspectstack = inspect.stack()[1][3]
                self.recoverapp(inspectstack)

    def recoverapp(self, inspectstack):
        """
        Description : This function helps to go back to events page. Inspect stack prints the test name from which
                                 this function is called.
        Revision:
        :return: None
        """
        print ("Application recovering called from " + inspectstack)
        basepage = BasePage(self.driver)
        basepage.accessURL()
        iconlistpage = IconListPage(self.driver)
        iconlistpage.click_events_icon()

    def app_sanity_check(self):
        """
        Description : This function should be called before any test to see the asset page is displayed.
        Revision:
        :return: None
        """
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._event_create_event)))
        except:
            inspectstack = inspect.stack()[1][3]
            self.recoverapp(inspectstack)
