from selenium.webdriver.common.keys import Keys
from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from basepage import BasePage
from time import sleep, time
import os, json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from datetime import date, timedelta, datetime

filepath = "data" + os.sep + "json_Schooldata.json"
cwd = os.getcwd()
os.chdir('..')
schooldatafile = os.path.join(os.getcwd(), filepath)
os.chdir(cwd)

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
    _ast_create_templatetype_dropdown_locator = "(//div[@model='template']//button[@data-toggle='dropdown'])"
    _ast_create_haystax_template_option_locator = ".//*[@id='assessmentManager']/div[2]/p[1]/span/div/ul/li/a"
    _ast_create_assignedto_text_box_locator = ".//*[@id='create_multi_assessment_assignedto']"
    _ast_create_start_date_text_box_locator = ".//*[@id='datetimepicker']//div//input[@id='create_multi_assessment_datepicker-01']"
    _ast_create_end_date_text_box_locator = ".//*[@id='datetimepicker']//div//input[@id='create_multi_assessment_datepicker-02']"

    #Assessment Overview related locators
    _ast_overview_button_locator = "//button[@title='Overview']"
    _ast_breadcrumb_text_locator = ".//*[@id='header']/div[1]/span[3]/span"
    _ast_overview_text = ".//*[@id='overview']/div[1]"
    _ast_overview_notes_textbox_locator = "//*[@id='assessment_notes']"
    # "//textarea[@placeholder='Notes']"
    _ast_overview_save_button_locator = ".//*[@id='header']/div[4]/button"
    _ast_overview_dates_textbox_locator = ".//*[@id='datetimepicker']/div/input"
    _ast_saved_text_locator = ".//*[@id='header']/div[4]"

    #Assessment Overview Upload related locator
    _ast_photos_documents_header_locator = "//div[contains(text(),'Photos / Documents')]"
    _ast_photos_documents_upload_file_button_locator = "//button[contains(text(), 'Upload file')]"
    _ast_photos_documents_attach_file_button_locator = "upload_document_file_upload"
    _ast_photos_documents_caption_textbox_locator = "upload_document_caption"
    _ast_photos_documents_window_upload_button_locator = ".//*[@id='widget_attach_document_modal']/div/div/div//button[contains(text(),'Upload')]"
    _ast_photos_documents_window_cancel_button_locator = ".//*[@id='widget_attach_document_modal']/div/div/div//button[contains(text(),'Cancel')]"

    #Assessment school data related locators
    _ast_schooldata_button_locator = "//button[@title='School Data']"
    _ast_schooldata_schooltyple_radio_button_locator = ".//*[@id='assessment_section']/div[3]/div[2]/span/label/span/span[2]"

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

    @property
    def get_ast_overview_text(self):
        return self.driver.find_element_by_xpath(self._ast_overview_text)

    @property
    def get_overview_startdate_textbox(self):
        return self.driver.find_elements_by_xpath(self._ast_overview_dates_textbox_locator)[0]

    @property
    def get_overview_enddate_textbox(self):
        return self.driver.find_elements_by_xpath(self._ast_overview_dates_textbox_locator)[1]

    @property
    def get_overview_notes_textbox(self):
        return self.driver.find_element_by_xpath(self._ast_overview_notes_textbox_locator)

    @property
    def get_overview_save_button(self):
        return self.driver.find_element_by_xpath(self._ast_overview_save_button_locator)

    @property
    def get_breadcrumb_assessmentname_text(self):
        return self.driver.find_element_by_xpath(self._ast_breadcrumb_text_locator)

    @property
    def get_photos_documents_header_text(self):
        return self.driver.find_elements_by_xpath(self._ast_photos_documents_header_locator)

    @property
    def get_file_upload_button(self):
        return self.driver.find_element_by_xpath(self._ast_photos_documents_upload_file_button_locator)

    @property
    def get_file_attach_file_button(self):
        return self.driver.find_element_by_id(self._ast_photos_documents_attach_file_button_locator)

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
    def get_overview_button(self):
        return self.driver.find_element_by_xpath(self._ast_overview_button_locator)
    @property
    def get_schooldata_button(self):
        return self.driver.find_element_by_xpath(self._ast_schooldata_button_locator)

    @property
    def get_schooldata_schooltype_radiobuttons(self):
        return self.driver.find_elements_by_xpath(self._ast_schooldata_schooltyple_radio_button_locator)


    def get_schooldata(self):

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
        countText = self.driver.find_element_by_id("tblAssessments_info").text
        splitedText = countText.split(" ")
        totalCount = splitedText[10]
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
        checks = self.driver.find_elements_by_xpath(".//*[@id='tblAssessments']/tbody/tr/td[1]/label")
        for checkbox in checks:
            if checkbox.get_attribute("class") == "checkbox checked":
                sleep(2)
                print "Uncheck"
                checkbox.click()
                sleep(1)

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
            return True
        else:
            self.get_search_assessment_textbox.clear()
            return False

    def select_asset(self, asset_name):
        sleep(5)
        self.get_search_asset_textbox.send_keys(asset_name)
        sleep(6)
        asset_list = self.get_asset_table("Asset")
        if len(asset_list)>=1:
            self.driver.find_element_by_xpath(".//*[@id='assessmentManager_table']/tbody/tr[1]/td[1]/label/span/span[2]").click()
        else:
            self.get_search_asset_textbox.clear()
            return False

    def select_first_asset(self):
        sleep(5)
        asset_list = self.get_asset_table("Asset")
        if len(asset_list)>=1:
            self.driver.find_element_by_xpath(".//*[@id='assessmentManager_table']/tbody/tr[1]/td[1]/label/span/span[2]").click()
        else:
            print "No Assets added yet"
            return False

    def wait_for_element(self, element):
        timeout = time() + 60*5
        print timeout
        while True:
            if element.is_displayed() or time() > 0:
                element.select()
                print "elemtn found"
                break

    def create_assessment_select_haystax_template(self):
        if not self.get_create_assessments_button.is_displayed():
            sleep(10)
            self.get_main_create_assessment_button.click()
            self.get_create_templatetype_dropdown.click()
            sleep(2)
            self.get_create_haystax_template_option.click()
            sleep(2)

    def create_assessment(self, assetname):
        self.create_assessment_select_haystax_template()
        start_date = datetime.today().date()
        end_date = start_date + timedelta(days=1)
        self.get_create_assignedto_textbox.clear()
        self.get_create_assignedto_textbox.send_keys("Dee@deep")
        sleep(2)
        self.get_create_startdate_textbox.clear()
        self.get_create_startdate_textbox.send_keys(str(start_date))
        sleep(1)
        self.get_create_enddate_textbox.clear()
        self.get_create_enddate_textbox.send_keys(str(end_date))
        if self.select_asset(assetname) == False:
            print "Asset not created yet"
            return False
        else:
            sleep(5)
            self.get_search_asset_textbox.clear()
            self.get_create_assessments_button.click()
            sleep(10)
            #self.get_main_create_assessment_button.click()

    def validate_email_textbox(self, textbox):
        emailid = ['Email', 'Email.', 'email.com', 'email@']
        textbox.clear()
        for item in emailid:
            textbox.send_keys(item)
            textbox.send_keys(Keys.TAB)
            sleep(5)
            self.assertEqual("rgba(192, 57, 43, 1)", textbox.value_of_css_property("border-bottom-color"),  "Email ID validation error in create assessment")
            textbox.clear()

    def get_assessment_name_from_breadcrumb(self):
        return (self.get_breadcrumb_assessmentname_text.text.split(' - '))[0].strip()

    def get_caption_path(self, caption):
        return self.driver.find_element_by_xpath("//div//a[contains(text(),'"+caption+"')]")

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
        file_path = "image_file"+ os.sep + image_file_name
        complete_file_path = os.path.join(os.getcwd(), file_path)
        os.chdir(cur_dir)
        return complete_file_path

    def upload_a_file(self, image_caption, image_file_name):
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
        self.get_fileupload_window_upload_button.click()
        sleep(5)
        # try:
        #     WebDriverWait(self.driver,100).until(expected_conditions.text_to_be_present_in_element((By.XPATH, self._ast_saved_text_locator), "Saved"))
        # except:
        #     pass

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

    def recoverapp(self):
        basepage = BasePage(self.driver)
        basepage.accessURL()
        iconlistpage = IconListPage(self.driver)
        iconlistpage.click_assessments_icon()

    #This function should be called before any test to see the assessmentt page is displayed
    def app_sanity_check(self):
        try:
            self.driver.find_element_by_xpath(self._ast_main_create_assessment_button_locator).is_displayed()
        except:
            print "Exception at sanity"

    def _validate_page(self, driver):
        pass