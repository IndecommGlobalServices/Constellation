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

class AssessmentPage(BasePageClass):

    schoolnames = 'SchoolNames'
    config = ConfigParser.ConfigParser()
    config.readfp(open('baseconfig.cfg'))

    ast_status_Inprogress = "In Progress"
    ast_status_Not_Started = "Not Started"
    ast_status_Submitted = "Submitted"

    #Assessment app name locator
    _ast_assessment_link_locator = "Assessments"
    _ast_assessment_header_locator = ".//*[@id='header']/div[1]/span[2]/span/a"
    _ast_name_text = ".//*[@id='header']/span[2]/span"

    #Assessment grid locators
    _ast_main_table_locator = ".//*[@id='tblAssessments']/tbody/tr/td"
    _ast_assessment_table_header_locator = ".//*[@id='tblAssessments']/thead/tr/th"
    _ast_staus_table_column_locator = ".//*[@id='tblAssessments']/tbody/tr/td[7]"

    #Asset grid locator
    _ast_asset_table_locator = ".//*[@id='assessmentManager_table']/tbody/tr[1]/td"
    _ast_asset_table_header_locator = ".//*[@id='assessmentManager_table']/thead/tr/th"
    _ast_assetlist_No_Matching_Records_Found_locator=".//*[@id='assessmentManager_table']/tbody/tr/td"

    #Assessment actions locator
    _ast_action_dropdown_loactor = "(//div[@id='assessment_actions_dropdown']//button[@data-toggle='dropdown'])"
        #"//div[@id = 'assessment_actions_dropdown']//button[contains(text(), 'Select action')]"

    # Assessment filter related locators
    _ast_status_filter_drop_down_locator = "//div[@label='Status']"
    _ast_type_filter_drop_down_locator = "//div[@label='Type']"
    _ast_filter_reset_button = "//button[contains(text(), 'Reset filters')]"


    # Assessment search related locators
    _ast_search_assessment_text_box_locator = ".//*[@id='search-assessments']"
    _ast_search_asset_text_box_locator = ".//*[@id='search-assessment-manager']"
    _ast_assessmentlist_No_Matching_Records_Found_locator = ".//*[@id='tblAssessments']//td[@class='dataTables_empty']"

    # Assessment delete related locators
    _ast_check_box_locator = ".//*[@id='tblAssessments']/tbody/tr/td[1]/label/span/span[2]"

    #Create Assessment related locators
    _ast_main_create_assessment_button_locator = "//img[@ng-src='../images/icon_create_item_off.png']"
    _ast_main_create_assessment_button_on_locator = "//img[@ng-src='../images/icon_create_item_on.png']"
    _ast_create_templatetype_dropdown_locator = "(//div[@id='assessment_create_modal']//button[@data-toggle='dropdown'])"
    _ast_create_haystax_template_option_locator = ".//*[@id='assessment_create_modal']/div/div/form/div[1]/div[1]/div/ul/li/a"
    _ast_create_start_date_text_box_locator = ".//*[@id='datetimepicker']//div//input[@id='create_multi_assessment_datepicker-01']"
    _ast_create_end_date_text_box_locator = ".//*[@id='datetimepicker']//div//input[@id='create_multi_assessment_datepicker-02']"
    _ast_create_assignedto_text_box_locator = "//span//input[contains(@placeholder,'Email address')]"
    _ast_create_assignedto_button_locator = "//button[contains(text(), 'Assign')]"
    _ast_create_asset_text_box_locator = "//input[@placeholder= 'Name']"
    _ast_create_asset_add_button_locator = "//button[contains(text(), 'Add')]"
    _ast_create_assessments_cancel_button_locator = "//div[@id='assessment_create_modal']/descendant::button[contains(text(), 'Cancel')]"
    _ast_create_assessments_save_button_locator = "//div[@id='assessment_create_modal']/descendant::button[contains(text(), 'Save')]"


    #_ast_create_assessments_button_locator = ".//*[@id='assessmentManager']/div[1]/button"
    #_ast_create_templatetype_dropdown_locator = "(//div[@model='template']//button[@data-toggle='dropdown'])"
    #_ast_create_haystax_template_option_locator = ".//*[@id='assessmentManager']/div[2]/p[1]/span/div/ul/li/a"
    #_ast_create_assignedto_text_box_locator = ".//*[@id='create_multi_assessment_assignedto']"


    #Assessment Overview related locators
    _ast_overview_button_locator = "//button[@title='Overview']"
    _ast_breadcrumb_text_locator = ".//*[@id='header']/div[1]/span[3]/span"
    _ast_overview_text = ".//*[@id='overview']/div[1]"
    _ast_overview_notes_textbox_locator = "assessment_notes"
    _ast_overview_save_button_locator = "//div[@id='header']//button[contains(text(),'Save')]"
    _ast_overview_start_date_textbox_locator = "//span[@name= 'started_picker']//input[@type = 'text']"
    _ast_overview_end_date_textbox_locator="//span[@name= 'ended_picker']//input[@type = 'text']"
    _ast_saved_text_locator = ".//*[@id='header']/div[4]"

    #Assessment Overview Upload related locator
    _ast_photos_documents_header_locator = "//div[contains(text(),'Photos / Documents')]"
    _ast_photos_documents_upload_file_button_locator = "//button[contains(text(), 'Upload file')]"
    _ast_photos_documents_attach_file_button_locator = "file_upload"
    _ast_photos_documents_caption_textbox_locator = "file_title"
    _ast_photos_documents_window_upload_button_locator = ".//*[@id='fileEditModal']/div/div/div//button[contains(text(),'Upload')]"
    _ast_photos_documents_window_cancel_button_locator = ".//*[@id='fileEditModal']/div/div/div//button[contains(text(),'Cancel')]"
    _ast_photos_documents_window_delete_button_locator = "//div[@id='fileDeleteModal']//button[contains(text(),'Delete')]"

    #Assessment edit caption locators
    _ast_file_edit_caption_text_box_locator = "//div[@class='forminputfields']//input[@id='question_photo_caption']"
    _ast_file_edit_caption_save_button_locator = "//div[@id='modal_edit_photo']//button[text()='Save']"
    _ast_file_edit_caption_cancel_button_locator = "//div[@id='modal_edit_photo']//button[text()='Cancel']"

    #Assessment school data related locators
    _ast_schooldata_button_locator = "//button[@title='School Data']"
    _ast_schooldata_schooltype_radio_button_locator = ".//*[@id='assessment_section']/div[3]/div[2]/span/label"
    _ast_schooldata_gradelevel_checkbox_locator = ".//*[@id='assessment_section']/div[3]/div[3]/span/span/label"
    _ast_schooldata_schoolhours_text_are_locator = "//div[contains(text(),'School hours')]//input[@ng-model='question.answer.text']"
    _ast_schooldata_numberofstudents_text_are_locator = "//div[contains(text(),'Number of students')]//input[@ng-model='question.answer.text']"
    _ast_schooldata_specialneedsstudents_text_area_locator = "//div[contains(text(),'Does the student body " \
                                                        "include students with special needs? If yes, how " \
                                                        "many students with special needs are enrolled')]" \
                                                        "//input[@ng-model='question.answer.text']"
    _ast_schooldata_numberofstaff_text_area_locator = "//div[contains(text(),'Number of staff')]//input[@ng-model='question.answer.text']"
    _ast_schooldata_numberofvisitors_text_area_locator = "//div[contains(text(),'Average number of visitors (non student/staff) per day')]" \
                                                         "//input[@ng-model='question.answer.text']"
    _ast_schooldata_lawenforcement_yes_radio_button_loactor = "//div[contains(text(),'Is there a certified law enforcement officer on campus?')]//label[@label='Yes']"
    _ast_schooldata_lawenforcement_no_radio_button_loactor = "//div[contains(text(),'Is there a certified law enforcement officer on campus?')]//label[@label='No']"

    #Assessment school Infrastructure related locators
    _ast_schoolInfrastructure_button_locator = "//button[@title='School Infrastructure']"

    #Assessment physical security related locators
    _ast_physicalsecurity_button_locator = "//button[@title='Physical Security']"

    #Assessment physical security related locators
    _ast_policiesandplanning_button_locator = "//button[@title='Policies & Planning']"

    #Assessment trainning and exercises related locators
    _ast_trainningandexercises_button_locator = "//button[@title='Training & Exercises']"

    # Scroll
    _assessment_scroll = ".//*[@id='main_content']"


    #Dashboard
    _ast_dashboard_on_icon = "//img[@ng-src = '../images/icon_pie_chart_on.png']"
    _ast_dashboard_off_icon = "//img[@ng-src = '../images/icon_pie_chart_off.png']"

    def __init__(self, driver):
        super(AssessmentPage, self).__init__(driver)
        # self.get_schooldata()
        self.basepage = BasePage(self.driver)
        loginpage = LoginPage(self.driver)
        loginpage.loginDashboard()
        self.username = loginpage.usernameText
        self.get_assessment_app()

    def get_assessment_app(self):
        appicon = IconListPage(self.driver)
        appicon.click_assessments_icon()

    @property
    def click_on_assessment_link(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
                (By.LINK_TEXT, self._ast_assessment_link_locator )))
            return self.driver.find_element_by_link_text(self._ast_assessment_link_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._ast_assessment_link_locator + err.message)

    @property
    def click_on_assessment_header(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self._ast_assessment_header_locator )))
            return self.driver.find_element_by_xpath(self._ast_assessment_header_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._ast_assessment_header_locator + err.message)

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
        return self.driver.find_element_by_xpath(".//*[@id='span_filters']/div[2]/div/ul/li/a")

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
        try:
            WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(
                        (By.XPATH, self._ast_main_create_assessment_button_locator)))
            return self.driver.find_element_by_xpath(self._ast_main_create_assessment_button_locator)
        except Exception, err:
            raise type(err)("Create assessment button not available - search XPATH - " \
                          + self._ast_main_create_assessment_button_locator + err.message)

    @property
    def get_main_create_assessment_red_button(self):
        try:
            return  self.driver.find_element_by_xpath(self._ast_main_create_assessment_button_on_locator)
        except Exception, err:
            raise type(err)("Create assessment button not available - searched XPATH - " \
                          + self._ast_main_create_assessment_button_on_locator + err.message)
    # @property
    # def get_create_assessments_button(self):
    #     try:
    #         return self.driver.find_element_by_xpath(self._ast_create_assessments_button_locator)
    #     except Exception, err:
    #         raise type(err)("Create assessment button not available - searched XPATH - " \
    #                       + self._ast_create_assessments_button_locator + err.message)
    @property
    def get_create_assignedto_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_create_assignedto_text_box_locator)

    @property
    def get_create_assignedto_button(self):
        return self.driver.find_element_by_xpath(self._ast_create_assignedto_button_locator)

    @property
    def get_create_assets_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_create_asset_text_box_locator)

    @property
    def get_create_assets_add_button(self):
        return self.driver.find_element_by_xpath(self._ast_create_asset_add_button_locator)

    @property
    def get_create_assessment_cancel_button(self):
        return self.driver.find_element_by_xpath(self._ast_create_assessments_cancel_button_locator)

    @property
    def get_create_assessment_save_button(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, self._ast_create_assessments_save_button_locator)), "Save button not visible")
            return self.driver.find_element_by_xpath(self._ast_create_assessments_save_button_locator)
        except Exception, err:
            raise type(err)("Create assessment Save button not available - searched XPATH - " \
                          + self._ast_create_assessments_save_button_locator + err.message)


    @property
    def get_create_startdate_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_create_start_date_text_box_locator)

    @property
    def get_create_enddate_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_create_end_date_text_box_locator)

    @property
    def get_create_templatetype_dropdown(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, self._ast_create_templatetype_dropdown_locator)))
            return self.driver.find_element_by_xpath(self._ast_create_templatetype_dropdown_locator)
        except:
            raise

    @property
    def get_create_haystax_template_option(self):
        return self.driver.find_element_by_xpath(self._ast_create_haystax_template_option_locator)

    @property
    def get_status_table_column(self):
        return self.driver.find_elements_by_xpath(self._ast_staus_table_column_locator)

    @property
    def get_assessmentlist_no_matching_records_found(self):
        return  self.driver.find_element_by_xpath(self._ast_assessmentlist_No_Matching_Records_Found_locator)

    @property
    def get_assetlist_no_matching_records_found(self):
        return  self.driver.find_element_by_xpath(self._ast_assetlist_No_Matching_Records_Found_locator)

    @property
    def get_action_dropdown(self):
        return self.driver.find_element_by_xpath(self._ast_action_dropdown_loactor)

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
        return self.basepage.findElementByLinkText("Assign")
        # return self.driver.find_element_by_link_text("Assign")

    @property
    def get_ast_checkbox(self):
        return self.driver.find_elements_by_xpath(self._ast_check_box_locator)

    @property
    def get_ast_assignto_textbox(self):
        try:
            return self.driver.find_element_by_xpath(".//*[@id='txt_assessment_assignedto']")
        except Exception, err:
            raise type(err)("Assigned to text box not available - searched XPATH - " \
                          + ".//*[@id='txt_assessment_assignedto']" + err.message)

    @property
    def get_ast_assignto_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(".//*[@id='assign_assessment_modal']/div/form/div[3]/button[1]")
        except Exception, err:
            raise type(err)("Cancel button not available - searched XPATH - " \
                          + ".//*[@id='assign_assessment_modal']/div/form/div[3]/button[1]" + err.message)

    @property
    def get_ast_assignto_assign_button(self):
        return self.driver.find_element_by_xpath(".//*[@id='assign_assessment_modal']/div/form/div[3]/button[2]")

    @property
    def get_assessment_table_header_locator(self):
        return self.driver.find_elements_by_xpath(self._ast_assessment_table_header_locator)

    @property
    def get_asset_table_header_locator(self):
        try:
            return self.driver.find_elements_by_xpath(self._ast_asset_table_header_locator)
        except Exception, err:
            raise

    @property
    def get_ast_overview_text(self):
        return self.driver.find_element_by_xpath(self._ast_overview_text)

    @property
    def get_overview_startdate_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_overview_start_date_textbox_locator)

    @property
    def get_overview_enddate_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_overview_end_date_textbox_locator)

    @property
    def get_overview_notes_textbox(self):
        return self.driver.find_element_by_id(self._ast_overview_notes_textbox_locator)

    @property
    def get_overview_save_button(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(
                (By.XPATH, self._ast_overview_save_button_locator)))
            return self.driver.find_element_by_xpath(self._ast_overview_save_button_locator)
        except Exception, err:
            raise type(err)(" Save button not available - searched XPATH - " \
                          + self._ast_overview_save_button_locator + err.message)

    @property
    def get_breadcrumb_assessmentname_text(self):
        return self.driver.find_element_by_xpath(self._ast_breadcrumb_text_locator)

    @property
    def get_photos_documents_header_text(self):
        return self.driver.find_elements_by_xpath(self._ast_photos_documents_header_locator)

    @property
    def get_file_upload_button(self):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._ast_photos_documents_upload_file_button_locator )))
            return self.driver.find_element_by_xpath(self._ast_photos_documents_upload_file_button_locator)
        except Exception, err:
            raise type(err)("Upload file button not visible - searched XPATH - " \
                          + self._ast_photos_documents_upload_file_button_locator + err.message)

    @property
    def get_file_attach_file_button(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                (By.ID, self._ast_photos_documents_attach_file_button_locator )))
            return self.driver.find_element_by_id(self._ast_photos_documents_attach_file_button_locator)
        except Exception, err:
            raise type(err)("Upload file button not visible - searched XPATH - " \
                          + self._ast_photos_documents_attach_file_button_locator + err.message)

    @property
    def get_fileupload_caption_textbox(self):
        return self.driver.find_element_by_id(self._ast_photos_documents_caption_textbox_locator)

    @property
    def get_fileupload_window_upload_button(self):
        return self.driver.find_element_by_xpath(self._ast_photos_documents_window_upload_button_locator)

    @property
    def get_fileupload_window_cancel_button(self):
        return self.driver.find_element_by_xpath(self._ast_photos_documents_window_cancel_button_locator)

    @property
    def get_fileupload_delete_button(self):
        return self.driver.find_element_by_xpath(self._ast_photos_documents_window_delete_button_locator)

    @property
    def get_overview_button(self):
        return self.driver.find_element_by_xpath(self._ast_overview_button_locator)

    @property
    def get_file_edit_caption_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_file_edit_caption_text_box_locator)

    @property
    def get_file_edit_caption_save_button(self):
        return self.driver.find_element_by_xpath(self._ast_file_edit_caption_save_button_locator)

    @property
    def get_file_edit_caption_cancel_button(self):
        return self.driver.find_element_by_xpath(self._ast_file_edit_caption_cancel_button_locator)

    @property
    def get_schooldata_button(self):
        WebDriverWait(self.driver, 50).until(expected_conditions.presence_of_all_elements_located(
            (By.XPATH, self._ast_schooldata_button_locator)), "Timeout")
        return self.driver.find_element_by_xpath(self._ast_schooldata_button_locator)

    @property
    def get_schooldata_schooltype_radiobuttons(self):
        return self.driver.find_elements_by_xpath(self._ast_schooldata_schooltype_radio_button_locator)

    @property
    def get_schooldata_gradelevel_checkbox(self):
        return self.driver.find_elements_by_xpath(self._ast_schooldata_gradelevel_checkbox_locator)

    @property
    def get_schooldata_schoolhours_textarea(self):
        return self.driver.find_element_by_xpath(self._ast_schooldata_schoolhours_text_are_locator)

    @property
    def get_schooldata_noofstudents_textarea(self):
        return self.driver.find_element_by_xpath(self._ast_schooldata_numberofstudents_text_are_locator)

    @property
    def get_schooldata_specialneedsstudents_textarea(self):
        return self.driver.find_element_by_xpath(self._ast_schooldata_specialneedsstudents_text_area_locator)

    @property
    def get_schooldata_noofstaff_textarea(self):
        return self.driver.find_element_by_xpath(self._ast_schooldata_numberofstaff_text_area_locator)

    @property
    def get_schooldata_noofvisitors_textarea(self):
        return self.driver.find_element_by_xpath(self._ast_schooldata_numberofvisitors_text_area_locator)

    @property
    def get_schooldata_lawenforcement_Yes_radiobutton(self):
        return self.driver.find_element_by_xpath(self._ast_schooldata_lawenforcement_yes_radio_button_loactor)

    @property
    def get_schooldata_lawenforcement_No_radiobutton(self):
        return self.driver.find_element_by_xpath(self._ast_schooldata_lawenforcement_no_radio_button_loactor)

    ####################School Infrastucture############################################################################
    @property
    def get_schoolinfrastructure_button(self):
        return self.driver.find_element_by_xpath(self._ast_schoolInfrastructure_button_locator)

    ####################School Physical Security########################################################################
    @property
    def get_school_physicalsecurity_button(self):
        return self.driver.find_element_by_xpath(self._ast_physicalsecurity_button_locator)

    ####################School Policies and Planning####################################################################
    @property
    def get_school_policiesandplanning_button(self):
        return self.driver.find_element_by_xpath(self._ast_policiesandplanning_button_locator)

    ####################School Training and Exercises####################################################################
    @property
    def get_school_trainningandexercises_button(self):
        return self.driver.find_element_by_xpath(self._ast_trainningandexercises_button_locator)



    def get_create_assets_option(self, assetname):
        return self.driver.find_element_by_xpath("//li[contains(text(), '"+assetname+"')]")

    def get_school_name(self, relevance):
        with open(schooldatafile) as data_file:
            school_data = json.load(data_file)
            for each in school_data:
                if relevance == "":
                    self.asset_school_name = each["asset_name"][0]
                elif relevance == 'schooldata':
                    self.asset_school_name = each["asset_name"][int(self.config.get(self.schoolnames, "SCHOOL_DATA"))]
                elif relevance == 'overview':
                    self.asset_school_name = each["asset_name"][int(self.config.get(self.schoolnames, "OVERVIEW_SCHOOL"))]
                elif relevance == 'infrastructure':
                     self.asset_school_name = each["asset_name"][int(self.config.get(self.schoolnames, "INFRASTRUCUTURE_SCHOOL"))]
                elif relevance == 'security':
                     self.asset_school_name = each["asset_name"][int(self.config.get(self.schoolnames, "PHYSICAL_School"))]
                elif relevance == 'policies':
                     self.asset_school_name = each["asset_name"][int(self.config.get(self.schoolnames, "POLICIES_School"))]
                elif relevance == 'training':
                     self.asset_school_name = each["asset_name"][int(self.config.get(self.schoolnames, "TRAINING_School"))]



    def get_table_tr_index(self, tablelocator, heading):
        index = 1
        for item in tablelocator:
            if(item.text == heading):
                break
            index = index+1
        return index

    def get_assessment_table(self, heading):
        index = self.get_table_tr_index(self.get_assessment_table_header_locator, heading)
        if heading == "Assessment":
            xpath = ".//*[@id='tblAssessments']/tbody/tr/td["+str(index)+"]"+"/a"
        else:
            xpath = ".//*[@id='tblAssessments']/tbody/tr/td["+str(index)+"]"
        return self.driver.find_elements_by_xpath(xpath)

    def get_assessment_table_row_values(self, row, heading):
        index = self.get_table_tr_index(self.get_assessment_table_header_locator, heading)
        xpath = ".//*[@id='tblAssessments']/tbody/tr["+str(row)+"]/td["+str(index)+"]"
        return self.driver.find_element_by_xpath(xpath)

    def get_asset_table(self, heading):
        index = self.get_table_tr_index(self.get_asset_table_header_locator, heading)
        xpath = ".//*[@id='assessmentManager_table']/tbody/tr/td["+str(index)+"]"
        return self.driver.find_elements_by_xpath(xpath)

    def get_asset_table_column_header(self, heading):
        index = self.get_table_tr_index(self.get_asset_table_header_locator, heading)
        xpath = ".//*[@id='assessmentManager_table']/thead/tr/th["+str(index)+"]"
        return self.driver.find_element_by_xpath(xpath)

    def get_total_row_count(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self._ast_action_dropdown_loactor)))
        countText = self.driver.find_element_by_id("tblAssessments_info").text.encode('utf-8').split('\n')[2].strip()
        splitedText = countText.split(" ")
        totalCount = splitedText[5]
        # print "total count:" + totalCount
        return int(totalCount)

    def select_multiple_checkboxes(self, count):
        checks = self.get_ast_checkbox
        index=0
        for check in checks:
            check.click()
            index = index+1
            if index == count:
                break

    def deselect_checkboxes(self):
        checks = self.driver.find_elements_by_xpath("//label[@class = 'checkbox checked']")
        for check in checks:
            check.click()

    def search_assessment_textbox(self, keyword):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, self._ast_search_assessment_text_box_locator)), "Assessment search text box not available")
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located(
            (By.XPATH, self._ast_action_dropdown_loactor)))
        self.get_search_assessment_textbox.clear()
        self.get_search_assessment_textbox.send_keys(keyword)

    def search_asset_textbox(self, keyword):
        self.get_search_asset_textbox.clear()
        self.get_search_asset_textbox.send_keys(keyword)

    def select_assessment(self, asset_name):
        sleep(5)
        WebDriverWait(self.driver, 50).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self._ast_action_dropdown_loactor)))
        self.search_assessment_textbox(asset_name)
        sleep(6)
        assessment_list = self.get_assessment_table("Assessment")
        if len(assessment_list)<=0:
            start_date = datetime.today().date()
            end_date = start_date + timedelta(days=31)
            self.create_assessment(str(start_date), str(end_date), "dee@dee")
        assessment_list = self.get_assessment_table("Assessment")
        assessment_list[0].click()

    def create_assessment_select_haystax_template(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self._ast_action_dropdown_loactor)))
        sleep(1)
        self.get_main_create_assessment_button.click()
        self.get_create_templatetype_dropdown.click()
        self.get_create_haystax_template_option.click()

    def get_asset_avilability(self, relevance):
        self.get_school_name(relevance)
        self.create_assessment_select_haystax_template()
        self.get_create_assets_textbox.send_keys(self.asset_school_name)
        try:
            self.driver.find_element_by_xpath("//li[contains(text(), '"+self.asset_school_name+"')]")
            self.get_create_assessment_cancel_button.click()
        except NoSuchElementException:
            AssetPage(self.driver).create_school_asset_for_assessmentapp(self.asset_school_name)
            BasePage(self.driver).accessURL()
            self.get_assessment_app()


    def delete_existing_assessments(self):
        self.search_assessment_textbox(self.asset_school_name)
        sleep(2)
        if len(self.get_assessment_table("Asset")) > 0:
            self.select_multiple_checkboxes(self.get_total_row_count())
            self.get_action_dropdown.click()
            self.get_action_delete_button.click()
            self.get_delete_assessment_delete_button.click()
        self.get_search_assessment_textbox.clear()
        self.get_search_assessment_textbox.send_keys(Keys.BACKSPACE)
        sleep(1)


    def create_assessment(self, startdate, enddate, assignedto):
        self.create_assessment_select_haystax_template()
        self.get_create_startdate_textbox.send_keys(startdate)
        self.get_create_enddate_textbox.send_keys(enddate)
        self.get_create_assignedto_textbox.clear()
        self.get_create_assignedto_textbox.send_keys(assignedto)
        self.get_create_assets_textbox.clear()
        self.get_create_assets_textbox.send_keys(self.asset_school_name)
        sleep(5)
        try:
            self.driver.find_element_by_xpath("//li[contains(text(), '"+self.asset_school_name+"')]").click()
        except Exception, err:
            self.get_create_assessment_cancel_button.click()
            raise type(err)("Searched asset name is not populated"  + err.message)
        self.get_create_assets_add_button.click()
        self.get_create_assessment_save_button.click()


    # def validate_email_textbox(self, textbox):
    #     emailid = ['Email', 'Email.', 'email.com', 'email@']
    #     textbox.clear()
    #     for item in emailid:
    #         textbox.send_keys(item)
    #         textbox.send_keys(Keys.TAB)
    #         sleep(5)
    #         self.assertEqual("rgba(192, 57, 43, 1)", textbox.value_of_css_property("border-bottom-color"),  "Email ID validation error in create assessment")
    #         textbox.clear()

    def get_assessment_name_from_breadcrumb(self):
        return (self.get_breadcrumb_assessmentname_text.text.split(' - '))[0].strip()

    def get_caption_path(self, caption):
        try:
            return self.driver.find_element_by_xpath("//div[@class = 'file_list_container showaslink ng-scope']"
                                                     "//a[contains(text(),'"+caption+"')]")
        except Exception, err:
             raise type(err)("File caption not visible - searched XPATH - " \
                          + "//div[@class = 'file_list_container showaslink ng-scope']"
                                                     "//a[contains(text(),'"+caption+"')]" + err.message)

    def get_file_header_path(self, filename):
        path = "//div[contains(text(), '" + filename + "')]"
        return path

    def get_file_caption_text(self, caption):
        caption_xpath = "//div[contains(text(),'Photos / Documents')]//following-sibling::div//ul//li[contains(text(),'"+caption+"')]"
        return self.driver.find_element_by_xpath(caption_xpath)

    def get_file_caption_text_path(self, caption):
        caption_xpath = "//div[contains(text(),'Photos / Documents')]//following-sibling::div//ul//li[contains(text(),'"+caption+"')]"
        return caption_xpath

    def file_path(self, image_file_name):
        cur_dir = os.getcwd()
        os.chdir("..")
        file_path = "image_file\\"+image_file_name
        complete_file_path = os.path.join(os.getcwd(), file_path)
        os.chdir(cur_dir)
        return complete_file_path

    def upload_a_file(self, image_caption, image_file_name):
        sleep(2)
        self.get_file_upload_button.click()# Click on Photo/Document panel - File Upload button
        # Click on Attach file button and attached the file path with the send_keys
        file_path = self.file_path(image_file_name)
        self.get_file_attach_file_button.send_keys(file_path)
        sleep(3)
        # Enter Caption
        if not image_caption == "":
            caption_val = image_caption
            self.get_fileupload_caption_textbox.send_keys(caption_val)
            sleep(2)
        # Click Upload.
        self.get_fileupload_window_upload_button.click()
        sleep(5)
        try:
            WebDriverWait(self.driver, 100).until(expected_conditions.text_to_be_present_in_element(
                (By.XPATH, self._ast_saved_text_locator), "Saved"),  self.driver.find_element_by_xpath(self._ast_saved_text_locator).text)
        except Exception, err:
            raise type(err)("File upload failed- Message displayed is -  " + self.driver.find_element_by_xpath(
                self._ast_saved_text_locator).text + err.message)


    def upload_a_file_cancel(self, image_caption, image_file_name):
         # Click on Photo/Document panel - File Upload button
        self.get_file_upload_button.click()
        sleep(2)
        # Click on Attach file button and attached the file path with the send_keys
        file_path = self.file_path(image_file_name)
        self.get_file_attach_file_button.send_keys(file_path)
        sleep(3)
        # Enter Caption
        caption_val = image_caption
        self.get_fileupload_caption_textbox.send_keys(caption_val)
        sleep(2)
        # Click Upload.
        self.get_fileupload_window_cancel_button.click()

    def delete_uploaded_files(self):
        """
        Description : This function will existing uploaded files.
        Revision:
        :return:
        """
        image_icons = self.driver.find_elements_by_xpath(".//img[@class='file_list_img']")
        num_of_files = len(image_icons)
        if num_of_files >= 1:
            sleep(2)
            for count in range(num_of_files, 0, -1):
                index = count
                xpath = r"(.//img[contains(@src,'delete_icon')])"+"["+str(index)+"]"
                image_icon_xpath =  self.driver.find_element_by_xpath\
                    (".//*[@id='widgets']/div[4]/div[1]/div/div[2]/div/div[" + str(index)+ "]")
                Hover = ActionChains(self.driver).move_to_element(image_icon_xpath)
                Hover.perform()
                self.driver.find_element_by_xpath(xpath).click()
                self.get_fileupload_delete_button.click()
                sleep(5)

    def delete_uploaded_files_assessmentpage(self, section, subsection, assessmentsection):
        """
        Description : This function will existing uploaded files.
        Revision:
        :return:
        """
        for deleteicon in self.get_schooldata_image_delete_button(section, subsection):
                deleteicon.click()
        self.get_schooldata_camera_image(section, subsection).click()
        self.save_editeddata(assessmentsection)

    def save_editeddata(self, mainsection):
        WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(
                    (By.XPATH, self._ast_overview_save_button_locator)),"Save button is disabled or not available").click()
        try:
            WebDriverWait(self.driver, 150).until(expected_conditions.text_to_be_present_in_element(
                (By.XPATH, self._ast_saved_text_locator), "Saved"))
        except Exception, err:
            raise type(err)("Save failed and the message displayed is - " \
                          + self.driver.find_element_by_xpath(self._ast_saved_text_locator).text + err.message)
        self.get_overview_button.click()
        if mainsection == "schooldata":
            self.get_schooldata_button.click()
        elif mainsection == "infrastructure":
            self.get_schoolinfrastructure_button.click()
        elif mainsection == "security":
            self.get_school_physicalsecurity_button.click()
        elif mainsection == "policies":
            self.get_school_policiesandplanning_button.click()
        elif mainsection == "training":
            self.get_school_trainningandexercises_button.click()

    def delete_attchedimage(self, subsection):
        if self.is_all_attachphoto_button_visible(subsection):
            for delete_button in self.get_all_schooldata_image_delete_button(subsection):
                delete_button.click()
            self.get_all_schooldata_camera_image(subsection).click()

    def get_assessment_availablity(self):
        if not self.select_assessment(self.asset_school_name):
            start_date = datetime.today().date()
            end_date = start_date + timedelta(days=31)
            self.create_assessment(str(start_date), str(end_date), "dee@dee")

    def open_overview_page(self):
        self.select_assessment(self.asset_school_name)
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located(
            (By.CLASS_NAME, "widgetcontent")))

    def open_main_section(self, mainsection):
        self.select_assessment(self.asset_school_name)
        if mainsection == "schooldata":
            self.get_schooldata_button.click()
        elif mainsection == "infrastructure":
            self.get_schoolinfrastructure_button.click()
        elif mainsection == "security":
            self.get_school_physicalsecurity_button.click()
        elif mainsection == "policies":
            self.get_school_policiesandplanning_button.click()
        elif mainsection == "training":
            self.get_school_trainningandexercises_button.click()

    def return_to_assessment_main_page(self):
        self.click_on_assessment_header.click()
        try:
            WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
                        (By.XPATH,self._ast_main_create_assessment_button_locator)))
        except:
            self.open_assessment_app()

    def open_assessment_app(self):
            BasePage(self.driver).accessURL()
            IconListPage(self.driver).click_assessments_icon()

    def get_schooldata_comment_image(self, section, subsection):
        return self.driver.find_element_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                                "[contains(text(),'"+subsection+"')]//img[@src='../images/comment.png']")

    def get_schooldata_comment_textbox(self, section, subsection):
        return self.driver.find_element_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                                "[contains(text(), '"+subsection+"')]//textarea[@placeholder='Comments']")

    def get_schooldata_comment_textbox_locator(self, section, subsection):
        return "//div[contains(text(), '"+section+"')]/following-sibling::div[contains(text(),'"+subsection+"')]//textarea[@placeholder='Comments']"

    def get_schooldata_comment_image_locator(self, section, subsection):
        return "//div[contains(text(), '"+section+"')]/following-sibling::div[contains(text(),'"+subsection+"')]//img[@src='../images/comment.png']"

    def get_schooldata_camera_image(self, section, subsection):
        return  self.driver.find_element_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                                "[contains(text(),'"+subsection+"')]//img[@src='../images/camera.png']")

    def get_all_schooldata_camera_image(self, subsection):
        return  self.driver.find_element_by_xpath("//div[contains(text(),'"+subsection+"')]//img[@src='../images/camera.png']")

    def get_schooldata_camera_image_locator(self, section, subsection):
        return "//div[contains(text(), '"+section+"')]/following-sibling::div" \
                                                  "[contains(text(),'"+subsection+"')]//img[@src='../images/camera.png']"

    def get_schooldata_attachphoto_button(self, section, subsection):
        return self.driver.find_element_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                                            "[contains(text(),'"+subsection+"')]" \
                                                           "//div[@ng-show='question.show_photo_upload']" \
                                                           "//div[@ng-show='assessmentEditable()']" \
                                                           "//input[@id='upload_document_file_upload']")


    def is_attachphoto_button_visible(self, section, subsection):
        return self.driver.find_element_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                                 "[contains(text(),'"+subsection+"')]"
                                                 "//div[@ng-show='question.show_photo_upload']"
                                                 "//div[@ng-show='assessmentEditable()']"
                                                 "//span[@class = 'fileinput-new']").is_displayed()

    def is_all_attachphoto_button_visible(self, subsection):
        return self.driver.find_element_by_xpath("//div[contains(text(),'"+subsection+"')]"
                                                 "//div[@ng-show='question.show_photo_upload']"
                                                 "//div[@ng-show='assessmentEditable()']"
                                                 "//span[@class = 'fileinput-new']").is_displayed()

    def get_schooldata_attachphoto_button_locator(self, section):
        return "//div[contains(text(),'"+section+"')]//div[@ng-show='question.show_photo_upload']" \
                                                 "//div[@ng-show='assessmentEditable()']" \
                                                           "//input[@id='upload_document_file_upload']"

    def get_schooldata_image(self, section, subsection):
        return self.driver.find_elements_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                                                        "[contains(text(),'"+subsection+"')]" \
                                                            "//div[@ng-show='question.show_photo_upload']" \
                                                            "//div[@class= 'assessment_photo_span ng-scope']"
                                                            "//img[@class= 'assessment_photo showaslink']")

    def get_schooldata_image_locator(self, section, subsection):
        return "//div[contains(text(), '"+section+"')]/following-sibling::div" \
                                        "[contains(text(),'"+subsection+"')]//div[@ng-show='question.show_photo_upload']" \
                                                            "//div[@class= 'assessment_photo_span ng-scope']"

    def get_schooldata_image_delete_button(self, section, subsection):
        return self.driver.find_elements_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                                                "[contains(text(),'"+subsection+"')]" \
                                                             "//div[@ng-show='question.show_photo_upload']" \
                                                             "//div[@class= 'assessment_photo_span ng-scope']" \
                                                             "//img[@src='../images/delete_icon.png']")

    def get_all_schooldata_image_delete_button(self, subsection):
        return self.driver.find_elements_by_xpath("//div[contains(text(),'"+subsection+"')]" \
                                                             "//div[@ng-show='question.show_photo_upload']" \
                                                             "//div[@class= 'assessment_photo_span ng-scope']" \
                                                             "//img[@src='../images/delete_icon.png']")
    def get_schooldata_image_delete_button_locator(self, section, subsection):
        return "//div[contains(text(), '"+section+"')]/following-sibling::div" \
                                    "[contains(text(),'"+subsection+"')]//div[@ng-show='question.show_photo_upload']" \
                                                 "//div[@class= 'assessment_photo_span ng-scope']" \
                                                             "//img[@src='../images/delete_icon.png']"

    def get_schooldata_image_caption(self, section, subsection):
        return self.driver.find_elements_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                                            "[contains(text(),'"+subsection+"')]" \
                                                      "//div[@ng-show='question.show_photo_upload']" \
                                                        "//div[@class= 'assessment_photo_span ng-scope']" \
                                                      "//div[@class = 'assessment_photo_caption ng-binding']")

    def get_schooldata_image_caption_locator(self, section):
        return "//div[contains(text(),'"+section+"')]//div[@ng-show='question.show_photo_upload']" \
                                                        "//div[@class= 'assessment_photo_span ng-scope']" \
                                                      "//div[@class = 'assessment_photo_caption ng-binding']"

    def schooldata_upload_file(self, section, subsection, assessmentsection):
        if not self.is_attachphoto_button_visible(section, subsection):
            self.get_schooldata_camera_image(section, subsection).click()
        file = self.file_path("Test_Case_40.jpg")
        self.get_schooldata_attachphoto_button(section, subsection).send_keys(file)
        self.save_editeddata(assessmentsection)

    def schooldata_edit_caption_image(self, section, subsection, assessmentsection):
        if not self.is_attachphoto_button_visible(section, subsection):
            self.get_schooldata_camera_image(section, subsection).click()
        file = self.file_path("Test_Case_40.jpg")
        self.get_schooldata_attachphoto_button(section, subsection).send_keys(file)
        WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(
                    (By.XPATH, self._ast_overview_save_button_locator)),"Save button is disabled").click()
        try:
            WebDriverWait(self.driver, 150).until(expected_conditions.text_to_be_present_in_element(
                (By.XPATH, self._ast_saved_text_locator), "Saved"))
        except Exception, err:
            raise type(err)("Save failed and the message displayed is - " \
                          + self.driver.find_element_by_xpath(self._ast_saved_text_locator).text + err.message)
        self.get_schooldata_image(section, subsection)[0].click()
        self.get_file_edit_caption_textbox.send_keys("Hello")
        self.get_file_edit_caption_save_button.click()
        self.save_editeddata(assessmentsection)

    @property
    def get_assessment_scroll(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._assessment_scroll)))
            return self.driver.find_element_by_xpath(self._assessment_scroll)
        except Exception, err:
            raise type(err)("Accordian main scroll bar - searched XPATH - " + self._assessment_scroll + err.message)

    def schooldata_edit_comment(self, section, subsection, assessmentsection):
        if not self.get_schooldata_comment_textbox(section, subsection).is_displayed():
            self.get_schooldata_comment_image(section, subsection).click()
        self.get_assessment_scroll.send_keys(Keys.ARROW_UP)
        self.get_assessment_scroll.send_keys(Keys.ARROW_UP)
        self.get_schooldata_comment_textbox(section, subsection).clear()
        self.get_schooldata_comment_textbox(section, subsection).send_keys("Comment")
        self.save_editeddata(assessmentsection)
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.get_schooldata_comment_textbox_locator(section, subsection))))

    def schooldata_delete_comment(self, section, subsection):
        if self.get_schooldata_comment_textbox(section, subsection).is_displayed():
            self.get_schooldata_comment_textbox(section, subsection).clear()
            self.get_schooldata_comment_image(section, subsection).click()
            WebDriverWait(self.driver, 50).until(expected_conditions.element_to_be_clickable(
                    (By.XPATH, self._ast_overview_save_button_locator)),"Save button is disabled").click()
            try:
                WebDriverWait(self.driver, 100).until(expected_conditions.text_to_be_present_in_element(
                    (By.XPATH, self._ast_saved_text_locator), "Saved"))
            except Exception, err:
                raise type(err)("Save failed and the message displayed is - " \
                              + self.driver.find_element_by_xpath(self._ast_saved_text_locator).text + err.message)

    def get_schooldata_radiobutton(self, section, subsectionsection):
        return self.driver.find_elements_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                "[contains(text(),'"+subsectionsection+"')]//label[@model='question.answer.text']")

    def get_schooldata_textarea(self, section, subsectionsection):
        return  self.driver.find_element_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                             "[contains(text(),'"+subsectionsection+"')]//textarea[@ng-model='question.answer.text']")

    def get_schooldata_textarea_locator(self, section, subsectionsection):
        return "//div[contains(text(), '"+section+"')]/following-sibling::div" \
                                "[contains(text(),'"+subsectionsection+"')]//textarea[@ng-model='question.answer.text']"

    def get_schooldata_textbox(self, section, subsectionsection):
        return self.driver.find_element_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                        "[contains(text(),'"+subsectionsection+"')]//input[@name = 'integer_input']")

    def get_schooldata_textbox_textinput(self, section, subsectionsection):
        return self.driver.find_element_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                        "[contains(text(),'"+subsectionsection+"')]//input[@type = 'text']")
    def get_schooldata_textbox_textinput_locator(self, section, subsectionsection):
        return ("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                        "[contains(text(),'"+subsectionsection+"')]//input[@type = 'text']")

    def get_schooldata_textbox_error(self, section, subsectionsection):
        return self.driver.find_element_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                                 "[contains(text(),'"+subsectionsection+"')]//span[@class = 'error']")

    def get_schooldata_textbox_error_locator(self, section, subsectionsection):
        return "//div[contains(text(), '"+section+"')]/following-sibling::div" \
                                                  "[contains(text(),'"+subsectionsection+"')]//span[@class = 'error']"

    def get_schooldata_textbox_locator(self, section, subsectionsection):
        return ("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                         "[contains(text(),'"+subsectionsection+"')]//input[@name = 'integer_input']")

    def get_schooldata_checkbox(self, section, subsectionsection):
        return self.driver.find_elements_by_xpath("//div[contains(text(), '"+section+"')]/following-sibling::div"
                                                                "[contains(text(),'"+subsectionsection+"')] //label")

    def get_schooldata_checkbox_locator(self, section, subsectionsection):
        return ("//div[contains(text(), '"+section+"')]/following-sibling::div[contains(text(),'"+subsectionsection+"')] //label")

    @property
    def get_assessment_scroll(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._assessment_scroll)))
            return self.driver.find_element_by_xpath(self._assessment_scroll)
        except Exception, err:
            raise type(err)("Accordian main scroll bar - searched XPATH - " + self._assessment_scroll + err.message)


    def _validate_page(self, driver):
        pass