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
    _ast_assessment_table_header_locator = ".//*[@id='tblAssessments']/thead/tr/th"
    _ast_staus_table_column_locator = ".//*[@id='tblAssessments']/tbody/tr/td[7]"

    #Asset grid locator
    _ast_asset_table_locator = ".//*[@id='assessmentManager_table']/tbody/tr[1]/td"
    _ast_asset_table_header_locator = ".//*[@id='assessmentManager_table']/thead/tr/th"

    # Assessment filter related locators
    _ast_status_filter_drop_down_locator = "//div[@label='Status']"
    _ast_type_filter_drop_down_locator = "//div[@label='Type']"
    _ast_filter_reset_button = ".//*[@id='span_filters']/button"

    # Assessment search related locators
    _ast_search_assessment_text_box_locator = ".//*[@id='search-assessments']"
    _ast_search_asset_text_box_locator = ".//*[@id='search-assessment-manager']"
    _ast_list_No_Matching_Records_Found_locator = ".//*[@id='tblAssessments']/tbody/tr/td"

    # Assessment delete related locators
    _ast_check_box_locator = ".//*[@id='tblAssessments']/tbody/tr/td[1]/label/span/span[2]"

    #Create Assessment related locators
    _ast_main_create_assessment_button_locator = ".//*[@id='page_content']/div[2]/img[1]"
    _ast_create_assessments_button_locator = ".//*[@id='assessmentManager']/div[1]/button"
    _ast_create_templatetype_dropdown_locator = ".//*[@id='assessmentManager']/div[2]/p[1]/span/div/button[2]"
    _ast_create_haystax_template_option_locator = ".//*[@id='assessmentManager']/div[2]/p[1]/span/div/ul/li/a"
    _ast_create_assignedto_text_box_locator = ".//*[@id='create_multi_assessment_assignedto']"
    _ast_create_start_date_text_box_locator = ".//*[@id='id']"
    _ast_create_end_date_text_box_locator = ".//*[@id='id']"


    def __init__(self, driver):
        super(AssessmentPage, self).__init__(driver)
        self.get_schooldata()
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
    def get_search_assessment_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_search_assessment_text_box_locator)

    @property
    def get_search_asset_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_search_asset_text_box_locator)

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
        return self.driver.find_elements_by_xpath(self._ast_create_start_date_text_box_locator)[0]

    @property
    def get_create_enddate_textbox(self):
        return self.driver.find_elements_by_xpath(self._ast_create_end_date_text_box_locator)[1]

    @property
    def get_create_templatetype_dropdown(self):
        return self.driver.find_element_by_xpath(self._ast_create_templatetype_dropdown_locator)

    @property
    def get_create_haystax_template_option(self):
        return self.driver.find_element_by_xpath(self._ast_create_haystax_template_option_locator)

    @property
    def get_status_table_column(self):
        return self.driver.find_elements_by_xpath(self._ast_staus_table_column_locator)

    @property
    def get_list_no_matching_records_found(self):
        return  self.driver.find_element_by_xpath(self._ast_list_No_Matching_Records_Found_locator)

    @property
    def get_action_dropdown(self):
        return self.driver.find_element_by_xpath(".//*[@id='assessment_actions_dropdown']/button[2]")

    @property
    def get_delete_assessment_delete_button(self):
        return self.driver.find_element_by_xpath(".//*[@id='delete_assessment_modal']/div/div/div[3]/button[2]")

    @property
    def get_delete_assessment_cancel_button(self):
        return self.driver.find_element_by_xpath(".//*[@id='delete_assessment_modal']/div/div/div[3]/button[1]")

    @property
    def get_action_delete_button(self):
        return self.driver.find_element_by_link_text("Delete")

    @property
    def get_action_assign_button(self):
        return self.driver.find_element_by_link_text("Assign")

    @property
    def get_ast_checkbox(self):
        return self.driver.find_elements_by_xpath(self._ast_check_box_locator)

    @property
    def get_ast_assignto_textbox(self):
        return self.driver.find_element_by_xpath(".//*[@id='txt_assessment_assignedto']")

    @property
    def get_ast_assignto_cancel_button(self):
        return self.driver.find_element_by_xpath(".//*[@id='assign_assessment_modal']/div/form/div[3]/button[1]")

    @property
    def get_ast_assignto_assign_button(self):
        return self.driver.find_element_by_xpath(".//*[@id='assign_assessment_modal']/div/form/div[3]/button[2]")

    @property
    def get_assessment_table_header_locator(self):
        return self.driver.find_elements_by_xpath(self._ast_assessment_table_header_locator)

    @property
    def get_asset_table_header_locator(self):
        return self.driver.find_elements_by_xpath(self._ast_asset_table_header_locator)

    def get_schooldata(self):
        cwd = os.getcwd()
        os.chdir('..')
        schooldatafile = os.path.join(os.getcwd(), "data\json_Schooldata.json")
        os.chdir(cwd)
        with open(schooldatafile) as data_file:
            school_data = json.load(data_file)
            for each in school_data:
                self.asset_school_name = each["asset_name"][0]


    def get_table_tr_index(self, tablelocator, heading):
        index = 1
        for item in tablelocator:
            if(item.text == heading):
                break
            index = index+1
        return index


    def get_assessment_table(self, heading):
        index = self.get_table_tr_index(self.get_assessment_table_header_locator, heading)
        xpath = ".//*[@id='tblAssessments']/tbody/tr/td["+str(index)+"]"
        return self.driver.find_elements_by_xpath(xpath)


    def get_asset_table(self, heading):
        index = self.get_table_tr_index(self.get_asset_table_header_locator, heading)
        xpath = ".//*[@id='assessmentManager_table']/tbody/tr/td["+str(index)+"]"
        return self.driver.find_elements_by_xpath(xpath)


    def get_total_row_count(self):
        countText = self.driver.find_element_by_id("tblAssessments_info").text
        splitedText = countText.split(" ")
        totalCount = splitedText[10]
        return totalCount


    def select_multiple_checkboxes(self, count):
        checks = self.get_ast_checkbox
        index=0
        for check in checks:
            check.click()
            index = index+1
            if index == count:
                break

    def deselect_checkboxes(self):
        checks = self.get_ast_checkbox



    def search_assessment_textbox(self, keyword):
        self.get_search_assessment_textbox.clear()
        self.get_search_assessment_textbox.send_keys(keyword)


    def search_asset_textbox(self, keyword):
        self.get_search_asset_textbox.clear()
        self.get_search_asset_textbox.send_keys(keyword)


    def select_assessment(self, asset_name):
        sleep(5)
        self.search_assessment_textbox(asset_name)
        sleep(6)
        assessment_list = self.get_assessment_table("Assessment")
        if len(assessment_list)>=1:
            assessment_list[0].click()
        else:
            self.get_search_assessment_textbox.clear()
            return False

    def select_asset(self, asset_name):
        sleep(5)
        #self.get_search_asset_textbox(asset_name)
        sleep(6)
        asset_list = self.get_asset_table("Asset")
        if len(asset_list)>=1:
            self.driver.find_element_by_xpath(".//*[@id='assessmentManager_table']/tbody/tr[1]/td[1]/label/span/span[2]").click()
        else:
            #self.get_search_asset_textbox.clear()
            return False

    def create_assessment_select_haystax_template(self):
        self.get_main_create_assessment_button.click()
        self.get_create_templatetype_dropdown.click()
        sleep(2)
        self.get_create_haystax_template_option.click()

    def create_assessment(self, assetname):
        self.create_assessment_select_haystax_template()
        self.select_asset(assetname)
        self.get_create_assignedto_textbox.clear()
        self.get_create_assignedto_textbox.send_keys("Dee@deep")
        self.get_create_startdate_textbox.clear()
        self.get_create_startdate_textbox.send_keys("2015-09-10")
        self.get_create_enddate_textbox.clear()
        self.get_create_enddate_textbox.send_keys("2015-09-11")
        sleep(2)
        self.get_create_assessments_button.click()
        sleep(5)




    #This function should be called before any test to see the assessmentt page is displayed
    def app_sanity_check(self):
        try:
            self.driver.find_element_by_xpath(self._ast_main_create_assessment_button_locator).is_displayed()
        except:
            print "Exception at sanity"


    def _validate_page(self, driver):
        pass