from lib.base import BasePageClass
from lib.base import InvalidPageException
from selenium.webdriver.common.keys import Keys
from pages.IconListPage import IconListPage
from basepage import BasePage
from loginpage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import inspect, os, json
from time import sleep
__author__ = 'Bijesh.gupta'

cwd = os.getcwd()
os.chdir('..')
eventData = os.path.join(os.getcwd(), "data", "json_time_line.json")
os.chdir(cwd)

class TimelinePage(BasePageClass, object):

    _tl_app_link_locator = "Timeline"
    _tl_app_name_locator = ".//span[text()='Timeline']"
    _tl_settings_link_locator = "//img[@title='Settings']"
    _tl_settings_window_header_locator = "//h4[contains(text(),'Timeline settings')]"
    _tl_now_link_locator = "//button[contains(text(),'Now')]"
    _tl_settings_start_date_locator = "//label[contains(text(),'Start Date')]/following-sibling::span//input"
    _tl_settings_end_date_locator = "//label[contains(text(),'End Date')]/following-sibling::span//input"
    _tl_settings_tags_textbox_locator = "//label[text()='Tags']/following-sibling::input"
    _tl_settings_tags_add_button_locator = "//button[text()='Add']"
    _tl_settings_tags_delete_link_locator = "//a[contains(@class,'delete-item showaslink')]/img"
    _tl_settings_assessments_checkbox_locator = "//label[contains(text(),'Assessments')]"
    _tl_settings_events_checkbox_locator = "//label[contains(text(),'Events')]"
    _tl_settings_field_interviews_checkbox_locator = "//label[contains(text(),'Field Interviews')]"
    _tl_settings_incidents_checkbox_locator = "//label[contains(text(),'Incidents')]"
    _tl_settings_close_button_locator = "//*[@id='timeline_settings_modal']//button[text()='Close']"
    _tl_settings_save_button_locator = "//*[@id='timeline_settings_modal']//button[text()='Save']"
    _tl_settings_date_error_message_locaator = ".//*[@id='timeline_settings_modal']//span[@class='error']"
    _tl_time_line_all_images_locator = ".//*[@id='calendarcontainer']//img"
    _tl_time_line_assessments_images_locator = "//img[contains(@src,'app_icon_assessments.png')]"
    _tl_time_line_assessments_links_locator = ".//*[@id='calendarcontainer']//a[contains(text(),'Assessment')]"
    _tl_time_line_events_images_locator = "//img[contains(@src,'app_icon_events.png')]"
    _tl_time_line_events_links_locator = ".//*[@id='calendarcontainer']//a[contains(text(),'Event')]"
    _tl_time_line_incidents_images_locator = "//img[contains(@src,'app_icon_incidents.png')]"
    _tl_time_line_incidents_links_locator = ".//*[@id='calendarcontainer']//a[contains(text(),'Incident')]"
    _tl_time_line_field_interviews_images_locator = "//img[contains(@src,'app_icon_field_interviews.png')]"
    _tl_time_line_field_interviews_links_locator = ".//*[@id='calendarcontainer']//a[contains(text(),'Field')]"


    @property
    def get_time_line_header(self):
        try:
            self.driver.find_element_by_xpath(self._tl_app_name_locator)
        except:
            return False
        return True

    @property
    def get_time_line_app_name_label(self):
        try:
            return self.basepage.findElementByXpath(self._tl_app_name_locator)
        except Exception, err:
            raise type(err)("Time line app name label is not found -" + self._tl_app_name_locator + err.message)

    @property
    def get_time_line_settings_link(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_link_locator)
        except Exception, err:
            raise type(err)("Time line Settings link is not available - searched XPATH - "\
                          + self._tl_settings_link_locator + err.message)

    @property
    def get_tl_settings_window_heading(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_window_header_locator)
        except Exception, err:
            raise type(err)("Time line Settings window heading is not available - searched XPATH - "\
                          + self._tl_settings_window_header_locator + err.message)

    @property
    def get_tl_settings_window_start_date_textbox(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_start_date_locator)
        except Exception, err:
            raise type(err)("Settings window start date textbox is not available - searched XPATH - "\
                          + self._tl_settings_start_date_locator + err.message)

    @property
    def get_tl_settings_window_end_date_textbox(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_end_date_locator)
        except Exception, err:
            raise type(err)("Settings window end date textbox is not available - searched XPATH - "\
                          + self._tl_settings_end_date_locator + err.message)

    @property
    def get_tl_settings_window_tags_textbox(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_tags_textbox_locator)
        except Exception, err:
            raise type(err)("Settings window tags textbox is not available - searched XPATH - "\
                          + self._tl_settings_tags_textbox_locator + err.message)

    @property
    def get_tl_settings_window_tags_add_button(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_tags_add_button_locator)
        except Exception, err:
            raise type(err)("Settings window tags add button is not available - searched XPATH - "\
                          + self._tl_settings_tags_add_button_locator + err.message)

    @property
    def get_tl_settings_window_tags_delete_link(self):
        try:
            return self.basepage.findElementsByXpath(self._tl_settings_tags_delete_link_locator)
        except Exception, err:
            raise type(err)("Settings window tags delete link is not available - searched XPATH - "\
                          + self._tl_settings_tags_delete_link_locator + err.message)

    @property
    def get_tl_settings_window_assessments_checkbox(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_assessments_checkbox_locator)
        except Exception, err:
            raise type(err)("Settings window assessments checkbox is not available - searched XPATH - "\
                          + self._tl_settings_assessments_checkbox_locator + err.message)

    @property
    def get_tl_settings_window_events_checkbox(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_events_checkbox_locator)
        except Exception, err:
            raise type(err)("Settings window events checkbox is not available - searched XPATH - "\
                          + self._tl_settings_events_checkbox_locator + err.message)

    @property
    def get_tl_settings_window_incidents_checkbox(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_incidents_checkbox_locator)
        except Exception, err:
            raise type(err)("Settings window incidents checkbox is not available - searched XPATH - "\
                          + self._tl_settings_incidents_checkbox_locator + err.message)

    @property
    def get_tl_settings_window_field_interviews_checkbox(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_field_interviews_checkbox_locator)
        except Exception, err:
            raise type(err)("Settings window incidents checkbox is not available - searched XPATH - "\
                          + self._tl_settings_field_interviews_checkbox_locator + err.message)

    @property
    def get_tl_settings_window_close_button(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_close_button_locator)
        except Exception, err:
            raise type(err)("Settings window close button is not available - searched XPATH - "\
                          + self._tl_settings_close_button_locator + err.message)

    @property
    def get_tl_settings_window_save_button(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_save_button_locator)
        except Exception, err:
            raise type(err)("Settings window save button is not available - searched XPATH - "\
                          + self._tl_settings_save_button_locator + err.message)
    @property
    def get_tl_settings_date_error_message(self):
        try:
            return self.basepage.findElementByXpath(self._tl_settings_date_error_message_locaator)
        except Exception, err:
            raise type(err)("Settings window date error message is not available - searched XPATH - "\
                          + self._tl_settings_date_error_message_locaator + err.message)

    @property
    def get_time_line_now_link(self):
        try:
            return self.basepage.findElementByXpath(self._tl_now_link_locator)
        except Exception, err:
            raise type(err)("Time line Now link is not available - searched XPATH - "\
                          + self._tl_now_link_locator + err.message)

    @property
    def get_time_line_all_images(self):
        try:
            return self.basepage.findElementsByXpath(self._tl_time_line_all_images_locator)
        except Exception, err:
            raise type(err)("Time line all images are not available - searched XPATH - "\
                          + self._tl_time_line_all_images_locator + err.message)

    @property
    def get_time_line_assessments_images(self):
        try:
            return self.basepage.findElementsByXpath(self._tl_time_line_assessments_images_locator)
        except Exception, err:
            raise type(err)("Time line assessments images are not available - searched XPATH - "\
                          + self._tl_time_line_assessments_images_locator + err.message)

    @property
    def get_time_line_assessments_links(self):
        try:
            return self.basepage.findElementsByXpath(self._tl_time_line_assessments_links_locator)
        except Exception, err:
            raise type(err)("Time line assessments links are not available - searched XPATH - "\
                          + self._tl_time_line_assessments_links_locator + err.message)

    @property
    def get_time_line_events_images(self):
        try:
            return self.basepage.findElementsByXpath(self._tl_time_line_events_images_locator)
        except Exception, err:
            raise type(err)("Time line events images are not available - searched XPATH - "\
                          + self._tl_time_line_events_images_locator + err.message)

    @property
    def get_time_line_events_links(self):
        try:
            return self.basepage.findElementsByXpath(self._tl_time_line_events_links_locator)
        except Exception, err:
            raise type(err)("Time line events links are not available - searched XPATH - "\
                          + self._tl_time_line_events_links_locator + err.message)

    @property
    def get_time_line_incidents_images(self):
        try:
            return self.basepage.findElementsByXpath(self._tl_time_line_incidents_images_locator)
        except Exception, err:
            raise type(err)("Time line incidents images are not available - searched XPATH - "\
                          + self._tl_time_line_incidents_images_locator + err.message)

    @property
    def get_time_line_incidents_links(self):
        try:
            return self.basepage.findElementsByXpath(self._tl_time_line_incidents_links_locator)
        except Exception, err:
            raise type(err)("Time line incidents links are not available - searched XPATH - "\
                          + self._tl_time_line_incidents_links_locator + err.message)

    @property
    def get_time_line_field_interviews_images(self):
        try:
            return self.basepage.findElementsByXpath(self._tl_time_line_field_interviews_images_locator)
        except Exception, err:
            raise type(err)("Time line field interviews images are not available - searched XPATH - "\
                          + self._tl_time_line_field_interviews_images_locator + err.message)

    @property
    def get_time_line_field_interviews_links(self):
        try:
            return self.basepage.findElementsByXpath(self._tl_time_line_field_interviews_links_locator)
        except Exception, err:
            raise type(err)("Time line field interviews links are not available - searched XPATH - "\
                          + self._tl_time_line_field_interviews_links_locator + err.message)


    def open_timeline_app(self):
        loginpage = LoginPage(self.driver)
        loginpage.loginDashboard()
        appicon = IconListPage(self.driver)
        appicon.click_timeline_icon()

    def return_to_apps_main_page(self):
        """
        Description : This function will helps to go back to Time line page.
        Revision:
        :return: None
        """
        if not self.get_time_line_header:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                    (By.LINK_TEXT, self._tl_app_link_locator))).click()
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located \
                                                               ((By.XPATH,self._tl_app_name_locator)))
            except:
                inspectstack = inspect.stack()[1][3]
                self.recoverapp(inspectstack)

    def recoverapp(self, inspectstack):
        """
        Description : This function helps to go back to Time Line page. Inspect stack prints the test name from
                      which this function is called.
        Revision:
        :return: None
        """
        print ("Application recovering called from " + inspectstack)
        basepage = BasePage(self.driver)
        basepage.accessURL()
        iconlistpage = IconListPage(self.driver)
        iconlistpage.click_timeline_icon()

    def get_time_line_data(self):
        with open(eventData) as data_file:
            for each in json.load(data_file):
                self.time_line_start_date = each["timeline_start_date"]
                self.time_line_end_date = each["timeline_end_date"]
                self.time_line_tag_1 = each["timeline_tag_1"]
                self.time_line_tag_2 = each["timeline_tag_2"]

    def delete_all_tags(self):
        tag_list = self.get_tl_settings_window_tags_delete_link
        if len(tag_list)>=1:
            for count in range(len(tag_list), 0, -1):
                tag_list[count-1].click()
        sleep(2)

    def check_box_enable(self, checkbox_name):
        if checkbox_name == "assessments":
            if self.get_tl_settings_window_assessments_checkbox.get_attribute("class") == "checkbox":
                self.get_tl_settings_window_assessments_checkbox.click()
        elif checkbox_name == "events":
            if self.get_tl_settings_window_events_checkbox.get_attribute("class") == "checkbox":
                self.get_tl_settings_window_events_checkbox.click()
        elif checkbox_name == "incidents":
            if self.get_tl_settings_window_incidents_checkbox.get_attribute("class") == "checkbox":
                self.get_tl_settings_window_incidents_checkbox.click()
        elif checkbox_name == "field_interviews":
            if self.get_tl_settings_window_field_interviews_checkbox.get_attribute("class") == "checkbox":
                self.get_tl_settings_window_field_interviews_checkbox.click()
                sleep(2)

    def check_box_disable(self, checkbox_name):
        if checkbox_name == "assessments":
            if "checkbox checked" in self.get_tl_settings_window_assessments_checkbox.get_attribute("class"):
                self.get_tl_settings_window_assessments_checkbox.click()
        elif checkbox_name == "events":
            if "checkbox checked" in self.get_tl_settings_window_events_checkbox.get_attribute("class"):
                self.get_tl_settings_window_events_checkbox.click()
        elif checkbox_name == "incidents":
            if "checkbox checked" in self.get_tl_settings_window_incidents_checkbox.get_attribute("class"):
                self.get_tl_settings_window_incidents_checkbox.click()
                sleep(1)
        elif checkbox_name == r"field_interviews":
            if "checkbox checked" in self.get_tl_settings_window_field_interviews_checkbox.get_attribute("class"):
                self.get_tl_settings_window_field_interviews_checkbox.click()
                sleep(2)

    def __init__(self, driver):
        super(TimelinePage,self).__init__(driver)
        self.basepage = BasePage(self.driver)
        self.get_time_line_data()


