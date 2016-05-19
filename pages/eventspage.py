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
    _event_select_action_delete_click_xpath_locator = ".//*[@id='delete_event_modal']/descendant::button[text()='Delete']"
    _event_list_select_first_check_box_xpath_locator = ".//*[@id='eventsTable']/tbody/tr[1]/td[1]/label/span/span[2]"
    _event_list_check_box_locator = ".//*[@id='eventsTable']/tbody/tr/td[1]/label/span/span[2]"
    _event_deleteevent_cancel_click_xpath_locator = ".//*[@id='delete_event_modal']/descendant::button[text()='Cancel']"

    # New Event creation related
    #_asset_create_asset = "//img[@alt='Create asset']"
    #_event_create_event = "//img[@ng-src='../images/icon_create_item_off.png']"

    _event_link_locator = "Events"

    _event_list_event_name_black_color_locator = "//*[@id='eventsTable']/tbody/tr/td[2]"

    # Creating Events
    _event_create_click = "//img[@title='Create event']"

    # Name - //input[@name='name']
    #
    # Start Date - //label[contains(text(),'Start Date')]/following-sibling::span/descendant::input[@ng-model='datetime_internal']
    #
    # Date - 2016-05-25 12:00 am
    #
    # End Date -
    #
    # //label[contains(text(),'End Date')]/following-sibling::span/descendant::input[@ng-model='datetime_internal']
    #
    # 2016-06-04 12:00 am
    #
    # Type
    #
    # Click - //button[contains(text(),'Type')]
    # Enter New Value - //input[@ng-model='itemInput']
    # Click - Add - //button[@id='newItemButton']
    #
    # Importance
    #
    # Click - //button[contains(text(),'Importance')]
    # Enter New Value - //input[@ng-model='itemInput']
    # Click - Add - //button[@id='newItemButton']
    #



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

    @property
    def get_event_list_first_check_box(self):
        try:
            #return self.driver.find_element_by_xpath(self._asset_list_select_first_check_box_xpath_locator)
            return self.basepage.findElementByXpath(self._event_list_select_first_check_box_xpath_locator)
        except Exception, err:
            raise type(err)("Asset table checkbox not available - searched XPATH - " \
                          + self._event_list_select_first_check_box_xpath_locator + err.message)


    @property
    def get_deleteevent_cancel_button(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, self._event_deleteevent_cancel_click_xpath_locator)), "Cancel button not available")
            return self.driver.find_element_by_xpath(self._event_deleteevent_cancel_click_xpath_locator)
        except Exception, err:
            raise type(err)("Cancel button not available in Delete Events popup - searched XPATH - " \
                          + self._event_deleteevent_cancel_click_xpath_locator + err.message)




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

    @property
    def get_event_delete_button(self):
        try:
            #return self.driver.find_element_by_xpath(self._asset_select_action_delete_click_xpath_locator)
            return self.basepage.findElementByXpath(self._event_select_action_delete_click_xpath_locator)
        except Exception, err:
            raise type(err)("Delete button not available in Delete Events popup - searched XPATH - " \
                          + self._event_select_action_delete_click_xpath_locator + err.message)

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

    def get_select_checkbox_in_grid(self):
        """
        Description : This function will select the checkbox from the event list..
        Revision:
        :return: None
        """
        #assets_checkbox = self.driver.find_elements_by_xpath(self._asset_list_check_box_locator)
        #sleep(2)
        events_checkbox = self.basepage.findElementsByXpath(self._event_list_check_box_locator)
        for event_checkbox in events_checkbox:
            #sleep(1)
            event_checkbox.click()

        for event_checkbox in events_checkbox:
            #sleep(1)
            event_checkbox.click()

    def get_total_row_count(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._event_select_action_delete_select_xpath_locator)))
        countText = (self.driver.find_element_by_id("eventsTable_info").text).encode('utf-8').split('\n')[2].strip()
        #print "count text:" + countText
        splitedText = countText.split(" ")
        totalCount = splitedText[5]
        # print "total count:" + totalCount
        return int(totalCount)

    def event_create_click(self):
        """
        Description : This function will click on Create Asset Link.
        Revision:
        :return: None
        """
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._event_select_action_delete_select_xpath_locator)))
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, self._event_create_asset))).click()

    def create_event(self):
        """
        Description : This function will enter event data.
        Revision:
        :return: None
        """

        # Click on Create Event Icon
        self.event_create_click()
        # Enter the values
        self.enter_asset_type_name.send_keys(self.asset_place_name)
        self.enter_asset_type_address.send_keys(self.asset_place_address)
        self.enter_asset_type_address2.send_keys(self.asset_place_address2)
        self.enter_asset_type_city.send_keys(self.asset_place_city)
        self.enter_asset_type_state.send_keys(self.asset_place_state)
        self.enter_asset_type_zip.send_keys(self.asset_place_zip)
        self.enter_asset_type_owner.send_keys(self.asset_place_owner)
        self.basepage.findElementByXpath(self._asset_overview_type_drop_down_locator).click()
        #sleep(2)
        self.get_overview_newtype_text_box.send_keys(self.asset_place_type)
        self.get_overview_place_type_add_button.click()
        # self.get_asset_overview_save_button.click()
