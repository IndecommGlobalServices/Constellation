from selenium.webdriver.common.keys import Keys
from lib.base import BasePageClass
from lib.base import InvalidPageException
from pages.IconListPage import IconListPage
from basepage import BasePage
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os, json


class AssessmentPage(BasePageClass):

    ast_status_Inprogress = "In Progress"
    ast_status_Not_Started = "Not Started"
    ast_status_Submitted = "Submitted"


    #Assessment app name locator
    _ast_name_text = ".//*[@id='header']/span[2]/span"

    #Assessment grid locators
    _ast_main_table_locator = ".//*[@id='tblAssessments']/tbody/tr/td"
    _ast_main_table_header_locator = ".//*[@id='tblAssessments']/thead/tr/th"
    _ast_staus_table_column_locator = ".//*[@id='tblAssessments']/tbody/tr/td[7]"

    # Assessment filter related locators
    _ast_status_filter_drop_down_locator = "//div[@label='Status']"
    _ast_type_filter_drop_down_locator = "//div[@label='Type']"
    _ast_filter_reset_button = ".//*[@id='span_filters']/button"

    # Assessment search related locators
    _ast_search_text_box_locator = ".//*[@id='search-assessments']"

    #Create Assessment related locators
    _ast_main_create_assessment_button_locator = "//img[@alt='Create assessment']"
    _ast_create_assessments_button_locator = "//img[@alt='Create assessments']"
    _ast_create_templatetype_dropdown_locator = ".//*[@id='assessmentManager']/div[2]/p[1]/span/div/button[2]"
    _ast_create_haystax_template_option_locator = ".//*[@id='assessmentManager']/div[2]/p[1]/span/div/ul/li/a"
    _ast_create_assignedto_text_box_locator = ".//*[@id='create_multi_assessment_assignedto']"
    _ast_create_start_date_text_box_locator = ".//*[@id='create_multi_assessment_datepicker-01']"
    _ast_create_end_date_text_box_locator = ".//*[@id='create_multi_assessment_datepicker-02']"


    def __init__(self, driver):
        super(AssessmentPage, self).__init__(driver)
        appicon = IconListPage(self.driver)
        appicon.click_assessments_icon()


    @property
    def get_ast_app_name(self):
        return self.driver.find_element_by_xpath(self._ast_name_text)

    @property
    def get_ast_statusfilter_dropdown(self):
        return self.driver.find_element_by_xpath(self._ast_status_filter_drop_down_locator)

    @property
    def get_ast_typefilter_dropdown(self):
        return self.driver.find_element_by_xpath(self._ast_type_filter_drop_down_locator)

    @property
    def get_statusfilter_InProgress_link(self):
        return self.driver.find_element_by_link_text(self.ast_status_Inprogress)

    @property
    def get_statusfilter_NotStarted_link(self):
        return self.driver.find_element_by_link_text(self.ast_status_Not_Started)

    @property
    def get_statusfilter_Submitted_link(self):
        return self.driver.find_element_by_link_text(self.ast_status_Submitted)

    @property
    def get_typefilter_haystax_link(self):
        return self.driver.find_element_by_link_text("Haystax School Safety")

    @property
    def get_resetfilter_button(self):
        return self.driver.find_element_by_xpath(self._ast_filter_reset_button)

    @property
    def get_search_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_search_text_box_locator)

    @property
    def get_main_create_assessment_button(self):
        return self.driver.find_element_by_xpath(self._ast_main_create_assessment_button_locator)

    @property
    def get_create_assessments_button(self):
        return self.driver.find_element_by_xpath(self._ast_create_assessments_button_locator)

    @property
    def get_create_assignedto_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_create_assignedto_text_box_locator)

    @property
    def get_create_startdate_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_create_start_date_text_box_locator)

    @property
    def get_create_enddate_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_create_end_date_text_box_locator)

    @property
    def get_create_templatetype_dropdown(self):
        return self.driver.find_element_by_xpath(self._ast_create_templatetype_dropdown_locator)

    @property
    def get_create_haystax_template_option(self):
        return self.driver.find_element_by_xpath(self._ast_create_haystax_template_option_locator)

    @property
    def get_status_table_column(self):
        return self.driver.find_elements_by_xpath(self._ast_staus_table_column_locator)


    def get_table_tr_index(self, heading):
        index = 1
        for item in self.driver.find_elements_by_xpath(self._ast_main_table_header_locator):
            if(item.text == heading):
                break
            index = index+1
        return index

    def get_xpath(self, index):
        xpath = ".//*[@id='tblAssessments']/tbody/tr/td["+str(index)+"]"
        return self.driver.find_elements_by_xpath(xpath)


    def _validate_page(self, driver):
        pass