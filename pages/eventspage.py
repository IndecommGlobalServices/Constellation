__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from basepage import BasePage
from loginpage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import inspect

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
    _event_create_event = "//img[@ng-src='../images/icon_create_item_off.png']"
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
            return self.basepage.findElementsByXpath(self._event_list_event_name_black_color_locator)
        except Exception, err:
            raise type(err)("Black color in the list not available after insertion - searched XPATH - " \
                          + self._event_list_event_name_black_color_locator + err.message)

    @property
    def get_event_link_delete_text(self):
        try:
            return self.basepage.findElementByXpath(self._event_link_delete_text_xpath_locator)
        except Exception, err:
            raise type(err)("Delete option not present in the select action dropdown - searched XPATH - " \
                          + self._event_link_delete_text_xpath_locator + err.message)

    @property
    def get_event_list_first_check_box(self):
        try:
            return self.basepage.findElementByXpath(self._event_list_select_first_check_box_xpath_locator)
        except Exception, err:
            raise type(err)("Event table checkbox not available - searched XPATH - " \
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
        Description : This function should be called before any test to see the event page is displayed.
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
        events_checkbox = self.basepage.findElementsByXpath(self._event_list_check_box_locator)
        for event_checkbox in events_checkbox:
            event_checkbox.click()

        for event_checkbox in events_checkbox:
            event_checkbox.click()

    def get_total_row_count(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._event_select_action_delete_select_xpath_locator)))
        countText = (self.driver.find_element_by_id("eventsTable_info").text).encode('utf-8').split('\n')[2].strip()
        splitedText = countText.split(" ")
        totalCount = splitedText[5]
        return int(totalCount)

    def event_create_click(self):
        """
        Description : This function will click on Create Event Link.
        Revision:
        :return: None
        """
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._event_select_action_delete_select_xpath_locator)))
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, self._event_create_event))).click()

    def create_event(self):
        """
        Description : This function will enter event data.
        Revision:
        :return: None
        """

        # Click on Create Event Icon
        self.event_create_click()
        # Enter the values

