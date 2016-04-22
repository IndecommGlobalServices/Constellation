import inspect
from pages.assetpage import AssetPage
from selenium.webdriver.common.keys import Keys
from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from basepage import BasePage
from time import sleep, time
import os, json
from loginpage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from datetime import date, timedelta, datetime
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import ConfigParser

cwd = os.getcwd()
os.chdir('..')
schooldatafile = os.path.join(os.getcwd(), "data", "json_Schooldata.json")
os.chdir(cwd)

class IncidentsPage(BasePageClass):

    config = ConfigParser.ConfigParser()
    config.readfp(open('baseconfig.cfg'))

    incident_status_Inprogress = "In Progress"
    incident_status_Not_Started = "Not Started"
    incident_status_Submitted = "Submitted"

    #Assessment app name locator
    _ast_assessment_link_locator = "Assessments"
    _ast_assessment_header_locator = ".//*[@id='header']/div[1]/span[2]/span/a"
    _ast_name_text = ".//*[@id='header']/span[2]/span"

    #Incidents create locators
    _incident_main_create_assessment_button_locator = "//img[@ng-src='../images/icon_create_item_off.png']"
    _incident_setttings_button_locator = "//img[@src='../images/icon_settings.png']"
    _incident_Type_dropdown_locator = "//div[@model='filter.value']//button[contains(text(), 'Type')]"
    _incident_Status_dropdown_locator = "//div[@model='filter.value']//button[contains(text(), 'Status')]"
    _incident_close_button_locator = "//div[@id='incident_settings_modal']//button[contains(text(), 'Close')]"


    def __init__(self, driver):
        super(IncidentsPage, self).__init__(driver)
        # self.get_schooldata()

    def logintoapp(self):
        self.basepage = BasePage(self.driver)
        loginpage = LoginPage(self.driver)
        loginpage.loginDashboard()
        self.username = loginpage.usernameText
        self.get_incidents_app()

    def get_incidents_app(self):
        appicon = IconListPage(self.driver)
        appicon.click_incidents_icon()

    @property
    def get_main_create_incident_button(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, self._incident_main_create_assessment_button_locator )))
            return self.driver.find_element_by_xpath(self._incident_main_create_assessment_button_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._incident_main_create_assessment_button_locator + err.message)

    @property
    def get_setings_button(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, self._incident_setttings_button_locator )))
            return self.driver.find_element_by_xpath(self._incident_setttings_button_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._incident_setttings_button_locator + err.message)

    @property
    def get_Type_dropdown(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, self._incident_Type_dropdown_locator )))
            return self.driver.find_element_by_xpath(self._incident_Type_dropdown_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._incident_Type_dropdown_locator + err.message)

    @property
    def get_status_dropdown(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, self._incident_Status_dropdown_locator )))
            return self.driver.find_element_by_xpath(self._incident_Status_dropdown_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._incident_Status_dropdown_locator + err.message)

    @property
    def get_close_button(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, self._incident_close_button_locator )))
            return self.driver.find_element_by_xpath(self._incident_close_button_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._incident_close_button_locator + err.message)

    def _validate_page(self, driver):
        pass