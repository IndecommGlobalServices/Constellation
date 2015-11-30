import sys
from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from basepage import BasePage
from time import sleep
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os, json, inspect
from selenium.webdriver.common.action_chains import ActionChains

cwd = os.getcwd()
os.chdir('..')
L1 = os.path.join(os.getcwd(), "data", "json_Schooldata.json")
placeData = os.path.join(os.getcwd(), "data", "json_Placedata.json")
os.chdir(cwd)

class AssetPage(BasePageClass):

    selectedgrade = ""
    selecteddistrict = ""
    selectedtype = ""

    # Asset Delete related locators
    _asset_select_action_delete_select_xpath_locator = ".//*[@id='asset_actions_dropdown']/button[text()='Select action']/following-sibling::button"
    _asset_link_delete_text_xpath_locator = ".//*[@id='asset_actions_dropdown']/ul/li/a"
    _asset_list_select_first_check_box_xpath_locator = ".//*[@id='assetstable']/tbody/tr[1]/td[1]/label/span/span[2]"
    _asset_select_action_delete_click_xpath_locator = ".//*[@id='delete_asset_modal']/descendant::button[text()='Delete']"
    _asset_deleteasset_cancel_click_xpath_locator = ".//*[@id='delete_asset_modal']/descendant::button[text()='Cancel']"

    # Asset List related locators
    _asset_list_locator = "//tbody/tr/td/a"
    _asset_list_check_box_locator = ".//*[@id='assetstable']/tbody/tr/td[1]/label/span/span[2]"
    _asset_list_assets_name_locator = ".//*[@id='assetstable']/tbody/tr/td[2]/a"
    _asset_list_background_locator = ".//*[@id='assetstable']/tbody/tr/td[2]"
    _asset_list_asset_type_locator = ".//*[@id='assetstable']/tbody/tr/td[3]"
    _asset_list_No_Matching_Records_Found_locator = ".//*[@id='assetstable']/tbody/tr/td"
    _asset_list_asset_name_black_color_locator = ".//*[@id='assetstable']/tbody/tr/td[2]"

    # Asset name on Breadcrumb
    _asset_name_breadcrumb = "//*[@id='header']/div[1]/span[3]/span"

    # Asset Filter related to place and school
    _asset_filter_drop_down_locator = ".//*[@id='span_filters']/descendant::div[@label='Asset Type']/button[@data-toggle='dropdown']"
    _asset_place_type_drop_down_locator = ".//*[@id='span_filters']/descendant::div[@label='Type']/button[@data-toggle='dropdown']"
    _asset_place_type_drop_down_select_first_element_locator = ".//*[@id='span_filters']/div[2]/div/ul/li[1]/a"

    _asset_school_district_drop_down_firt_element_locator = ".//*[@id='span_filters']/div[2]/div/ul/li[1]/a"
    _asset_school_district_drop_down_locator = ".//*[@id='span_filters']/descendant::div[@label='District']/button[@data-toggle='dropdown']"
    _asset_school_district_lists_locator = ".//*[@id='assetstable']/tbody/tr/td[4]"

    _asset_school_grade_drop_down_locator = ".//*[@id='span_filters']/descendant::div[@label='Grade Level']/button[@data-toggle='dropdown']"
    _asset_school_grade_drop_down_select_first_element_locator = ".//*[@id='span_filters']/div[3]/div/ul/li[1]/a"
    _asset_school_grade_lists_locator = ".//*[@id='assetstable']/tbody/tr/td[5]"

    _asset_school_type_drop_down_locator = ".//*[@id='span_filters']/descendant::div[@label='School Type']/button[@data-toggle='dropdown']"
    _asset_school_type_drop_down_select_first_element_locator = ".//*[@id='span_filters']/div[4]/div/ul/li[1]/a"
    _asset_school_type_lists_locator = ".//*[@id='assetstable']/tbody/tr/td[6]"

    #asset search textbox
    _asset_search_textbox_locator = ".//*[@id='txt_search_assets']"

    # New Asset creation related
    #_asset_create_asset = "//img[@alt='Create asset']"
    _asset_create_asset = "//img[@ng-src='../images/icon_create_item_off.png']"

    # Reset filter related
    _asset_filter_reset_button_locator = ".//*[@id='span_filters']/button"
    _asset_filter_asset_type_text_locator = ".//*[@id='span_filters']/div/div/button[1]"

    # Place and School - Creation mode related
    _asset_type_field_name_text_box_locator = "//input[@ng-model='model']"
    _asset_type_field_address_text_box_locator = "//input[@ng-model='asset_edit.address.address1']"
    _asset_type_field_address2_text_box_locator = "//input[@ng-model='asset_edit.address.address2']"
    _asset_type_field_city_text_box_locator = "//input[@ng-model='asset_edit.address.city']"
    _asset_type_field_state_text_box_locator = "//input[@ng-model='asset_edit.address.state']"
    _asset_type_field_zip_text_box_locator = "//input[@ng-model='asset_edit.address.zip']"
    _asset_type_field_owner_text_box_locator = "//input[@placeholder='Owner']"
    _asset_type_field_phone_text_box_locator = "//input[@ng-model='asset_edit.phone']"
    _asset_type_Saved_label_locator = ".//*[@id='header']/div[contains(text(),'Saved')]"

    # Overview panel related
    #Asset Overview dialouge locators
    _asset_overview_templatetype_dropdown_locator = "(//div[@label='Type']//button[@data-toggle='dropdown'])"
    _asset_overview_name_text_box_locator = "//input[@placeholder='Name']"
    _asset_overview_address_text_box_locator = ".//*[@id='asset_overview_modal']/descendant::input[@placeholder='Address']"
    _asset_overview_address2_text_box_locator = "//input[@ng-model='asset_edit.address.address2']"
    _asset_overview_city_text_box_locator = "//input[@ng-model='asset_edit.address.city']"
    _asset_overview_state_text_box_locator = "//input[@ng-model='asset_edit.address.state']"
    _asset_overview_zip_text_box_locator = "//input[@ng-model='asset_edit.address.zip']"
    _asset_overview_owner_text_box_locator = "//input[@placeholder='Owner']"
    _asset_overview_phone_text_box_locator = ".//*[@id='asset_overview_modal']/descendant::input[@name='phone']"
    _asset_overview_type_text_box_locator = "//input[@placeholder='Enter new value']"
    _asset_overview_district_text_box_locator = ".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li/input"
    _asset_overview_grade_text_box_locator = ".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li/input"

    _asset_overview_type_drop_down_locator = "//div[@class='forminputfields']//div[@label='Type']//button[@data-toggle='dropdown']"
    # "(//div[@label='Type']//button[@data-toggle='dropdown'])[2]"
    _asset_overview_district_drop_down_locator = "//div[@class='forminputfields']//div[@label= 'District']/button[@data-toggle='dropdown']"
    _asset_overview_grade_drop_down_locator = "//div[@class='forminputfields']//div[@label= 'Grade']/button[@data-toggle='dropdown']"
    _asset_overview_add_button_locator = ".//*[@id='newItemButton']"
    _asset_overview_cancel_button_locator = ".//div[@id='asset_overview_modal']/descendant::button[text()='Cancel']"
    _asset_overview_save_button_locator = ".//div[@id='asset_overview_modal']/descendant::button[@type='submit' and text()='Save']"
    _asset_overview_panel_name_text = ".//*[@id='widgets']/descendant::div[@class='widgetheader']/following-sibling::div[@class='widgetcontent']/descendant::td[span[text()='Name']]/following-sibling::td"
    _asset_overview_panel_address_text = ".//*[@id='widgets']/descendant::div[@class='widgetheader']/following-sibling::div[@class='widgetcontent']/descendant::td[span[text()='Address']]/following-sibling::td"
    _asset_overview_panel_owner_text = ".//*[@id='widgets']/descendant::div[@class='widgetheader']/following-sibling::div[@class='widgetcontent']/descendant::td[span[text()='Owner']]/following-sibling::td"
    _asset_overview_panel_district_text = ".//*[@id='widgets']/descendant::div[@class='widgetheader']/following-sibling::div[@class='widgetcontent']/descendant::td[span[text()='District']]/following-sibling::td"
    _asset_overview_panel_grade_text = ".//*[@id='widgets']/descendant::div[@class='widgetheader']/following-sibling::div[@class='widgetcontent']/descendant::td[span[text()='Grade']]/following-sibling::td"
    _asset_overview_edit_link_locator = "//div[contains(text(),'Overview')]/div/img"
    _asset_overview_edit_name_textbox_locator = "name"
    _asset_overview_window_popup_cross_button_locator = "//*[@id='asset_overview_modal']/div/div/div/button"

    _asset_type_cancel_button_locator = "//div[@id='asset_overview_modal']/div/div/form/div[2]/button[1]"
    _asset_type_save_button_locator = "//div[@id='asset_overview_modal']/div/div/form/div[2]/button[2]"

    # Point of Contacts related
    _asset_points_of_contact_header_locator = "//div[contains(text(), 'Points of Contact')]"
    _assets_points_of_contact_title_locator = ".//*[@id='asset_contact_modal_title']"
    _asset_point_of_contact_name_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Name']"
    _asset_point_of_contact_title_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Title']"
    _asset_point_of_contact_phone_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Phone']"
    _asset_point_of_contact_email_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Email']"
    _asset_point_of_contact_name_text_value_locator = "//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit']"
    _asset_point_of_contact_title_text_value_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])/../following-sibling::td[1]"
    _asset_point_of_contact_phone_text_value_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])/../following-sibling::td[2]"
    _asset_point_of_contact_email_text_value_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])/../following-sibling::td[3]"

    #New Contact Window
    _asset_main_contct_widget_locator = ".//*[@id='widgets']/descendant::div[@class='widget widget_contacts']/div[@class='widgetheader']"
    _asset_add_contact_button_locator = "btn_add_asset_contact"
    _asset_newcontact_firstname_textbox_locator = "first_name"
    _asset_newcontact_lastname_textbox_locator = "last_name"
    _asset_newcontact_prefix_textbox_locator = "//input[@placeholder='Prefix']"
    _asset_newcontact_title_textbox_locator = "//input[@placeholder='Title']"
    _asset_newcontact_phone_textbox_locator = "phone"
    _asset_newcontact_email_textbox_locator = "email"
    _asset_newcontact_address1_textbox_locator = "address"
    _asset_newcontact_address2_textbox_locator = "*//input[@ng-model='contact_edit.address.address2']"
    _asset_newcontact_city_textbox_locator = "*//input[@placeholder='City']"
    _asset_newcontact_state_textbox_locator = "state"
    _asset_newcontact_zip_textbox_locator = "zip"
    _asset_newcontact_save_button_locator = "//form[@name='form_contact_edit']//div//button[@type='submit' and text()='Save']"
    _asset_newcontact_cancel_button_locator = "//form[@name='form_contact_edit']//div//button[@type='button' and text()='Cancel']"
    _asset_newcontact_delete_contact_icon_locator = ".//*[@id='contacts_table']/tbody/tr[1]/descendant::a/img"
    _asset_newcontact_delete_contact_popup_delete_button_locator = ".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]"
    _asset_newcontact_delete_contact_popup_cancel_button_locator = ".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[1]"
    _asset_newcontact_window_popup_cross_button_locator = ".//*[@id='asset_contact_modal']/descendant::button[@class='close fui-cross']"
    _asset_newcontact_firstname_error_message_locator = ".//div[contains(@ng-show,'form_contact_edit.first_name')]/small"
    _asset_newcontact_lastname_error_message_locator = ".//div[contains(@ng-show,'form_contact_edit.last_name')]/small"
    _asset_newcontact_email_error_message_locator = ".//div[contains(@ng-show,'form_contact_edit.email')]/small"
    _asset_newcontact_state_error_message_locator = ".//div[contains(@ng-show,'form_contact_edit.state')]/small"
    _asset_newcontact_zip_error_message_locator = ".//div[contains(@ng-show,'form_contact_edit.zip')]/small"
    _asset_contact_first_last_name_value_text = "(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])[1]"
    _asset_contact_title_value_text_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])[1]/../following-sibling::td[1]"
    _asset_contact_phone_value_text_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])[1]/../following-sibling::td[2]"
    _asset_contact_email_value_text_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])[1]/../following-sibling::td[3]"
    _asset_contact_new_contact_text_locator = "//table[@id='contacts_table']//tbody//tr"
    _asset_main_contact_window_locator = ".//*[@id='form_main_contact']"
    _asset_main_contact_name_locator = ".//*[@id='form_main_contact']/div[2]/table/tbody/tr[1]/td[2]"

    _asset_link_locator = "Assets"
    _asset_header_save_text_locator = ".//*[@id='header']/div[contains(@class,'right ng-binding')]"

    # Asset Detail panel related
    _asset_detail_edit_link_locator = ".//*[@id='widgets']/div[5]/div/div[1]/div/img"
    _asset_details_edit_widget_locator = ".//*[@id='widgets']/div[5]/div/div[1]"
    _asset_detail_edit_title_locator = ".//h4[@id='H2']"
    _asset_detail_edit_capacity_textbox_locator = "//input[@placeholder='Capacity']"
    _asset_detail_edit_closed_textbox_locator = ".//*[@id='datetimepicker']/div/input"
    _asset_detail_edit_description_textbox_locator = ".//*[@id='asset_details_description_edit']"
    _asset_detail_edit_detail_district_number_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[4]/div/span/input"
    _asset_detail_edit_fax_textbox_locator = "//input[@placeholder='Fax, e.g. 555-555-5555']"
    _asset_detail_edit_opened_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[6]/div/span/input"
    _asset_detail_edit_school_number_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[8]/div/span/input"
    _asset_detail_edit_place_size_textbox_locator = "//input[@placeholder='size (sq ft)']"
    _asset_detail_edit_school_size_textbox_locator = "//input[@placeholder='Size_sqfeet']"
    _asset_detail_edit_email_textbox_locator = "//input[@placeholder='Email']"
    _asset_detail_email_value_text_locator = ".//span[text()='Email']/../following-sibling::td"
    _asset_detail_edit_website_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[8]/div/span/input"
    _asset_detail_edit_save_button_locator = ".//*[@id='asset_details_modal']/descendant::div[@class='modal-footer']/button[text()='Save']"
    _asset_detail_edit_cancel_button_locator = ".//*[@id='asset_details_modal']/descendant::div[@class='modal-footer']/button[text()='Cancel']"
    _asset_detail_edit_window_popup_cross_button_locator = ".//*[@id='asset_details_modal']/descendant::button[@class='close fui-cross']"

    # Asset Photo/Document Upload Panel
    _asset_photos_documents_header_locator = "//div[contains(text(),'Photos / Documents')]"
    _asset_photos_documents_uploaded_file_locator = "//div[contains(@label,'Photos / Documents')]/div[@class='formLayout']/div/div[@class='widgetcontent']/div/div"
    _asset_photos_documents_upload_file_button_locator = "//button[contains(text(), 'Upload file')]"
    _asset_photos_documents_attached_file_button_locator = "file_upload"
    _asset_photos_documents_caption_textbox_locator = "file_title"
    _asset_photos_documents_window_upload_button_locator = ".//*[@id='fileEditModal']/descendant::button[contains(text(),'Upload')]"
    _asset_photos_documents_window_cancel_button_locator = ".//*[@id='fileEditModal']/descendant::button[contains(text(),'Cancel')]"
    _asset_photos_documents_delete_window_delete_locator = "//div[@id='fileDeleteModal']//button[contains(text(),'Delete')]"
    _asset_photos_documents_window_title_locator = ".//*[@id='fileEditModal']"
    _asset_photos_documents_delete_icon_locator = "//img[@class='neutron_file_delete_icon']"

    # Asset Annotation Panel
    _asset_annotation_widget_locator = ".//*[@id='widgets']/descendant::div[@class='widgetheader' and contains(text(),'Annotations')]"
    _asset_annotation_plus_image_locator = "//div[contains(text(),'Annotations')]//img"
    _asset_annotation_edit_window_text_area_locator = "//label[text()='Annotation']//following-sibling::textarea"
    _asset_annotation_edit_window_visibility_dropdown_locator = "//label[text()='Visibility']//following-sibling::div//button[@data-toggle='dropdown']"
    _asset_annotation_edit_window_dropdown_groups_locator = "//label[text()='Visibility']//following-sibling::div//ul//li[1]//a"
    _asset_annotation_edit_window_dropdown_tenant_locator = "//label[text()='Visibility']//following-sibling::div//ul//li[2]//a"
    _asset_annotation_edit_window_dropdown_user_locator = "//label[text()='Visibility']//following-sibling::div//ul//li[3]//a"
    _asset_annotation_edit_window_save_button_locator = "//*[@id='asset_annotation_modal']/descendant::button[text()='Save']"
    _asset_annotation_edit_window_cancel_button_locator = "//*[@id='asset_annotation_modal']/descendant::button[text()='Cancel']"
    _asset_annotation_text_value_locator = "//div[contains(text(),'Annotations')]//following-sibling::div/div"
    _asset_annotation_delete_image_locator = "//div[contains(text(),'Annotations')]//following-sibling::div/div/div/a[contains(@ng-click,'deleteItem')]"
    _asset_annotation_edit_image_locator = "//div[contains(text(),'Annotations')]//following-sibling::div/div/div/a[contains(@ng-click,'editItem')]"

    # Location related
    _asset_location_map_id_locator = "map_control"
    _asset_location_edit_icon_xpath_locator = ".//div[@id='map_control']/following-sibling::img[@class='widget_edit']"
    _asset_location_title_id_locator = ".//*[@id='location_modal']/descendant::div[@class='modal-header']"
    _asset_location_latitude_name_locator = "latitude"
    _asset_location_latitude_error_xpath_locator = ".//*[@id='map_popup']/descendant::label[text()='Latitude']/following-sibling::span[@class='error']/small"
    _asset_location_save_xpath_locator = ".//*[@id='location_modal']/div/div/form/div[2]/button[2]"
    _asset_location_cancel_xpath_locator = ".//*[@id='location_modal']/descendant::button[text()='Cancel']"
    _asset_location_longitude_name_locator = "longitude"
    _asset_location_longitude_error_xpath_locator = ".//*[@id='map_popup']/descendant::label[text()='Longitude']/following-sibling::span[@class='error']/small"
    _asset_location_marker_avaliable_xpath_locator = ".//*[@id='map_control']/descendant::div[@class='leaflet-marker-pane']/img[contains(@class,'leaflet-marker-icon')]"
    _asset_location_place_name_xpath_locator = ".//*[@id='map_control']/div[1]/div[2]/div[4]/div/div[1]/div/b"

    # Charts related
    _asset_chart_total_Graph_In_Container_xpath_locator = ".//*[@id='graphs_frame']/div/div/div/div[1]"
    #Chart dashboard
    _asset_chart_dashboard_img_xpath_locator = "//img[@title='Dashboard']"
    #_asset_chart_dashboard_img_off_xpath_locator = ".//*[@id='page_content']/div[2]/img[2]"
    _asset_chart_dashboard_img_off_xpath_locator = ".//*[@id='page_content']/descendant::img[@title='Dashboard' and contains(@class,'dashboard')]"
    _asset_count = 0
    _assets = {}


    def __init__(self, driver):
        super(AssetPage, self).__init__(driver)
        self.get_schooldata()
        self.get_placedata()

    def open_asset_app(self):
        appicon = IconListPage(self.driver)
        appicon.click_asset_icon()

    @property
    def get_asset_name_breadcrumb(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_name_breadcrumb)
        except Exception, err:
            raise type(err)("Asset name not available in breadcrumb - searched XPATH - " \
                          + self._asset_name_breadcrumb + err.message)

    @property
    def get_assets_name_list(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_list_assets_name_locator)
        except Exception, err:
            raise type(err)("Asset name column not available in the assets table - searched XPATH - " \
                          + self._asset_list_assets_name_locator + err.message)

    @property
    def get_asset_list_background(self):
        return self.driver.find_elements_by_xpath(self._asset_list_background_locator)

    @property
    def get_filter_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_filter_drop_down_locator)

    @property
    def get_asset_select_action_drop_down(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_select_action_delete_select_xpath_locator)
        except Exception, err:
            raise type(err)("Select Action drop down not available - searched XPATH - " \
                          + self._asset_select_action_delete_select_xpath_locator + err.message)

    @property
    def get_asset_link_delete_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_link_delete_text_xpath_locator)
        except Exception, err:
            raise type(err)("Delete option not present in the select action dropdown - searched XPATH - " \
                          + self._asset_link_delete_text_xpath_locator + err.message)

    @property
    def get_asset_delete_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_select_action_delete_click_xpath_locator)
        except Exception, err:
            raise type(err)("Delete button not available in Delete Assets popup - searched XPATH - " \
                          + self._asset_select_action_delete_click_xpath_locator + err.message)

    @property
    def get_deleteasset_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_deleteasset_cancel_click_xpath_locator)
        except Exception, err:
            raise type(err)("Cancel button not available in Delete Assets popup - searched XPATH - " \
                          + self._asset_deleteasset_cancel_click_xpath_locator + err.message)

    @property
    def get_asset_reset_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_filter_reset_button_locator)
        except Exception, err:
            raise type(err)("Reset filter button not available - searched XPATH - " \
                          + self._asset_filter_reset_button_locator + err.message)

    @property
    def get_overview_templatetype_drop_down(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_templatetype_dropdown_locator)
        except Exception, err:
            raise type(err)("Template type dropdown not available - searched XPATH - " \
                          + self._asset_overview_templatetype_dropdown_locator + err.message)

    @property
    def get_overview_type_drop_down(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, self._asset_overview_type_drop_down_locator)))
            return self.driver.find_element_by_xpath(self._asset_overview_type_drop_down_locator)
        except Exception, err:
            raise type(err)("Asset type dropdown not available - searched XPATH - " \
                          + self._asset_overview_type_drop_down_locator + err.message)

    @property
    def get_overview_district_drop_down(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_district_drop_down_locator)
        except Exception, err:
            raise type(err)("District dropdown not available - searched XPATH - " \
                          + self._asset_overview_district_drop_down_locator + err.message)

    @property
    def get_overview_grade_drop_down(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_grade_drop_down_locator)
        except Exception, err:
            raise type(err)("Grade dropdown not available - searched XPATH - " \
                          + self._asset_overview_grade_drop_down_locator + err.message)

    @property
    def get_asset_asset_type_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_filter_asset_type_text_locator)
        except Exception, err:
            raise type(err)("Asset type dropdown not available - searched XPATH - " \
                          + self._asset_filter_asset_type_text_locator + err.message)

    @property
    def get_asset_list_first_check_box(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_list_select_first_check_box_xpath_locator)
        except Exception, err:
            raise type(err)("Asset table checkbox not available - searched XPATH - " \
                          + self._asset_list_select_first_check_box_xpath_locator + err.message)

    @property
    def get_asset_place_type_drop_down(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_place_type_drop_down_locator)
        except Exception, err:
            raise type(err)("Place type dropdown not available - searched XPATH - " \
                          + self._asset_place_type_drop_down_locator + err.message)

    @property
    def get_asset_place_type_first_element(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_place_type_drop_down_select_first_element_locator)
        except Exception, err:
            raise type(err)("Place type dropdown list not available - searched XPATH - " \
                          + self._asset_place_type_drop_down_select_first_element_locator + err.message)

    @property
    def get_asset_school_district_drop_down(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_school_district_drop_down_locator)
        except Exception, err:
            raise type(err)("District dropdown not available - searched XPATH - " \
                          + self._asset_school_district_drop_down_locator + err.message)

    @property
    def get_asset_school_district_first_element(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_school_district_drop_down_firt_element_locator)
        except Exception, err:
            raise type(err)("District dropdown list not available - searched XPATH - " \
                          + self._asset_school_district_drop_down_firt_element_locator + err.message)

    @property
    def get_asset_school_grade_drop_down(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_school_grade_drop_down_locator)
        except Exception, err:
            raise type(err)("Grade dropdown not available - searched XPATH - " \
                          + self._asset_school_grade_drop_down_locator + err.message)

    @property
    def get_asset_school_grade_first_element(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_school_grade_drop_down_select_first_element_locator)
        except Exception, err:
            raise type(err)("Grade dropdown list not available - searched XPATH - " \
                          + self._asset_school_grade_drop_down_select_first_element_locator + err.message)
    @property
    def get_asset_school_type_drop_down(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_school_type_drop_down_locator)
        except Exception, err:
            raise type(err)("School type dropdown not available - searched XPATH - " \
                          + self._asset_school_type_drop_down_locator + err.message)
    @property
    def get_asset_school_type_first_element(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_school_type_drop_down_select_first_element_locator)
        except Exception, err:
            raise type(err)("School type dropdown list not available - searched XPATH - " \
                          + self._asset_school_type_drop_down_select_first_element_locator + err.message)

    @property
    def get_asset_list_no_matching_records_found(self):
        try:
            return  self.driver.find_element_by_xpath(self._asset_list_No_Matching_Records_Found_locator)
        except Exception, err:
            raise type(err)("No Matching Records Found message not available - searched XPATH - " \
                          + self._asset_list_No_Matching_Records_Found_locator + err.message)

    @property
    def get_asset_name_list(self):
        try:
            return  self.driver.find_elements_by_xpath(self._asset_list_asset_name_black_color_locator)
        except Exception, err:
            raise type(err)("Black color in the list not available after insertion - searched XPATH - " \
                          + self._asset_list_asset_name_black_color_locator + err.message)

    @property
    def enter_asset_type_name(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_name_text_box_locator)
        except Exception, err:
            raise type(err)("Asset name textbox not available - searched XPATH - " \
                          + self._asset_overview_name_text_box_locator + err.message)

    @property
    def enter_asset_type_address(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_address_text_box_locator)
        except Exception, err:
            raise type(err)("Asset Address textbox not available - searched XPATH - " \
                          + self._asset_overview_address_text_box_locator + err.message)

    @property
    def enter_asset_type_address2(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_address2_text_box_locator)
        except Exception, err:
            raise type(err)("Asset Address2 textbox not available - searched XPATH - " \
                          + self._asset_overview_address2_text_box_locator + err.message)

    @property
    def enter_asset_type_city(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_city_text_box_locator)
        except Exception, err:
            raise type(err)("Asset City textbox not available - searched XPATH - " \
                          + self._asset_overview_city_text_box_locator + err.message)
    @property
    def enter_asset_type_state(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_state_text_box_locator)
        except Exception, err:
            raise type(err)("Asset State textbox not available - searched XPATH - " \
                          + self._asset_overview_state_text_box_locator + err.message)

    @property
    def enter_asset_type_zip(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_zip_text_box_locator)
        except Exception, err:
            raise type(err)("Asset Zip textbox not available - searched XPATH - " \
                          + self._asset_overview_zip_text_box_locator + err.message)

    @property
    def enter_asset_type_owner(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_owner_text_box_locator)
        except Exception, err:
            raise type(err)("Asset Owner textbox not available - searched XPATH - " \
                          + self._asset_overview_owner_text_box_locator + err.message)

    @property
    def enter_asset_type_phone(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_phone_text_box_locator)
        except Exception, err:
            raise type(err)("Asset Phone no textbox not available - searched XPATH - " \
                          + self._asset_overview_phone_text_box_locator + err.message)

    @property
    def asset_type_Saved_label(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_type_Saved_label_locator)
        except Exception, err:
            raise type(err)("'Saved' label not available - searched XPATH - " \
                          + self._asset_type_Saved_label_locator + err.message)

    @property
    def select_asset_schooltype_column(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_school_type_lists_locator)
        except Exception, err:
            raise type(err)("School Type column not available - searched XPATH - " \
                          + self._asset_school_type_lists_locator + err.message)

    @property
    def select_asset_schooltype_district_column(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_school_district_lists_locator)
        except Exception, err:
            raise type(err)("School District column not available - searched XPATH - " \
                          + self._asset_school_district_lists_locator + err.message)

    @property
    def select_asset_schooltype_grade_column(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_school_grade_lists_locator)
        except Exception, err:
            raise type(err)("School Grade column not available - searched XPATH - " \
                          + self._asset_school_grade_lists_locator + err.message)

    @property
    def get_overview_editname_text_box(self):
        try:
            return self.driver.find_element_by_name("name")
        except Exception, err:
            raise type(err)("Asset Name textbox not found with element name 'name' - searched XPATH - " \
                          + err.message)

    @property
    def get_overview_newdistrict_text_box(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, self._asset_overview_district_text_box_locator)))
            return self.driver.find_element_by_xpath(self._asset_overview_district_text_box_locator)
        except Exception, err:
            raise type(err)("School District textbox not available - searched XPATH - " \
                          + self._asset_overview_district_text_box_locator + err.message)

    @property
    def get_overview_newgrade_text_box(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, self._asset_overview_grade_text_box_locator)))
            return self.driver.find_element_by_xpath(self._asset_overview_grade_text_box_locator)
        except Exception, err:
            raise type(err)("School Grade textbox not available - searched XPATH - " \
                          + self._asset_overview_grade_text_box_locator + err.message)

    @property
    def get_overview_newtype_text_box(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, self._asset_overview_type_text_box_locator)))
            return self.driver.find_element_by_xpath(self._asset_overview_type_text_box_locator)
        except Exception, err:
            raise type(err)("Asset Type textbox not available - searched XPATH - " \
                          + self._asset_overview_type_text_box_locator + err.message)

    @property
    def get_overview_school_newtype_text_box(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_overview_type_text_box_locator)[2]
        except Exception, err:
            raise type(err)("Asset Type textbox not available - searched XPATH - " \
                          + self._asset_overview_type_text_box_locator + err.message)

    @property
    def get_overview_district_add_button(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_overview_add_button_locator)[0]
        except Exception, err:
            raise type(err)("School District textbox not available - searched XPATH - " \
                          + self._asset_overview_add_button_locator + err.message)

    @property
    def get_overview_grade_add_button(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_overview_add_button_locator)[1]
        except Exception, err:
            err.msg = "School Grade Add button not available - " + err.msg
            raise type(err)("School Grade Add button not available - searched XPATH - " \
                          + self._asset_overview_add_button_locator + err.message)

    @property
    def get_overview_type_add_button(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_overview_add_button_locator)[2]
        except Exception, err:
            raise type(err)("Asset Type Add button not available - searched XPATH - " \
                          + self._asset_overview_add_button_locator + err.message)

    @property
    def get_overview_place_type_add_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_add_button_locator)
        except Exception, err:
            raise type(err)("Asset Type Add button not available - searched XPATH - " \
                          + self._asset_overview_add_button_locator + err.message)

    @property
    def get_overview_name_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_panel_name_text)
        except Exception, err:
            raise type(err)("Asset name not available in overview panel - searched XPATH - " \
                          + self._asset_overview_panel_name_text + err.message)

    @property
    def get_overview_address1_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_panel_address_text).text
        except Exception, err:
            raise type(err)("Asset Address not available in overview panel - searched XPATH - " \
                          + self._asset_overview_panel_address_text + err.message)

    @property
    def get_overview_district_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_panel_district_text).text
        except Exception, err:
            raise type(err)("District not available in overview panel - searched XPATH - " \
                          + self._asset_overview_panel_district_text + err.message)

    @property
    def get_overview_grade_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_panel_grade_text).text
        except Exception, err:
            raise type(err)("Grade not available in overview panel - searched XPATH - " \
                          + self._asset_overview_panel_grade_text + err.message)

    @property
    def get_asset_overview_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_cancel_button_locator)
        except Exception, err:
            raise type(err)("Cancel button not available in overview dialog - searched XPATH - " \
                          + self._asset_overview_cancel_button_locator + err.message)

    @property
    def get_asset_overview_save_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_save_button_locator)
        except Exception, err:
            raise type(err)("Save button not available in overview dialog - searched XPATH - " \
                          + self._asset_overview_save_button_locator + err.message)

    @property
    def get_asset_points_of_contact_header(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_points_of_contact_header_locator)
        except Exception, err:
            raise type(err)("Points of Contact header not available - searched XPATH - " \
                          + self._asset_points_of_contact_header_locator + err.message)

    @property
    def get_asset_add_contact_button(self):
        try:
            return self.driver.find_element_by_id(self._asset_add_contact_button_locator)
        except Exception, err:
            raise type(err)("Add contact button not available in Points of Contact- searched XPATH - " \
                          + self._asset_add_contact_button_locator + err.message)

    @property
    def get_asset_newcontact_firstname_textbox(self):
        try:
            return self.driver.find_element_by_name(self._asset_newcontact_firstname_textbox_locator)
        except Exception, err:
            raise type(err)("New contact first name textbox not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_firstname_textbox_locator + err.message)

    @property
    def get_asset_newcontact_lastname_textbox(self):
        try:
            return self.driver.find_element_by_name(self._asset_newcontact_lastname_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Last name textbox not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_lastname_textbox_locator + err.message)

    @property
    def get_asset_newcontact_prefix_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_prefix_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Prefix textbox not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_prefix_textbox_locator + err.message)

    @property
    def get_asset_newcontact_title_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_title_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Title textbox not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_title_textbox_locator + err.message)

    @property
    def get_asset_newcontact_phone_textbox(self):
        try:
            return self.driver.find_element_by_name(self._asset_newcontact_phone_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Phone no textbox not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_phone_textbox_locator + err.message)

    @property
    def get_asset_newcontact_email_textbox(self):
        try:
            return self.driver.find_element_by_name(self._asset_newcontact_email_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Email ID textbox not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_email_textbox_locator + err.message)

    @property
    def get_asset_newcontact_address1_textbox(self):
        try:
            return self.driver.find_element_by_name(self._asset_newcontact_address1_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Address1 textbox not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_address1_textbox_locator + err.message)

    @property
    def get_asset_newcontact_address2_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_address2_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Address2 textbox not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_address2_textbox_locator + err.message)

    @property
    def get_asset_newcontact_city_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_city_textbox_locator)
        except Exception, err:
            raise type(err)("New contact City textbox not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_city_textbox_locator + err.message)

    @property
    def get_asset_newcontact_state_textbox(self):
        try:
            return self.driver.find_element_by_name(self._asset_newcontact_state_textbox_locator)
        except Exception, err:
            raise type(err)("New contact State textbox not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_state_textbox_locator + err.message)

    @property
    def get_asset_newcontact_zip_textbox(self):
        try:
            return self.driver.find_element_by_name(self._asset_newcontact_zip_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Zip textbox not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_zip_textbox_locator + err.message)

    @property
    def get_asset_newcontact_save_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_save_button_locator)
        except Exception, err:
            raise type(err)("New contact Save button not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_save_button_locator + err.message)

    @property
    def get_asset_newcontact_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_cancel_button_locator)
        except Exception, err:
            raise type(err)("New contact Cancel button not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_cancel_button_locator + err.message)

    @property
    def get_asset_newcontact_delete_icon(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_delete_contact_icon_locator)
        except Exception, err:
            raise type(err)("New contact Delete Icon not available in Points of Contact- searched XPATH - " \
                          + self._asset_newcontact_delete_contact_icon_locator + err.message)

    @property
    def get_asset_newcontact_delete_popup_delete_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_delete_contact_popup_delete_button_locator)
        except Exception, err:
            raise type(err)("New contact Delete Button not available in Delete Contact popup- searched XPATH - " \
                          + self._asset_newcontact_delete_contact_popup_delete_button_locator + err.message)

    @property
    def get_asset_newcontact_delete_popup_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_delete_contact_popup_cancel_button_locator)
        except Exception, err:
            raise type(err)("New contact Cancel Button not available in Delete Contact popup- searched XPATH - " \
                          + self._asset_newcontact_delete_contact_popup_cancel_button_locator + err.message)

    @property
    def get_asset_newcontact_window_cross_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_window_popup_cross_button_locator)
        except Exception, err:
            raise type(err)("Cross Button not available in Delete Contact popup- searched XPATH - " \
                          + self._asset_newcontact_window_popup_cross_button_locator + err.message)

    @property
    def get_asset_newcontact_firstname_error_message(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_firstname_error_message_locator)
        except Exception, err:
            raise type(err)("Validation message for First name not available in contact information- searched XPATH - " \
                          + self._asset_newcontact_firstname_error_message_locator + err.message)

    @property
    def get_asset_newcontact_lastname_error_message(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_lastname_error_message_locator)
        except Exception, err:
            raise type(err)("Validation message for Last name not available in contact information- searched XPATH - " \
                          + self._asset_newcontact_lastname_error_message_locator + err.message)

    @property
    def get_asset_newcontact_email_error_message(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_newcontact_email_error_message_locator)
        except Exception, err:
            raise type(err)("Validation message for Email ID not available in contact information  - searched XPATH - " \
                          + self._asset_newcontact_email_error_message_locator + err.message)

    @property
    def get_asset_contact_first_last_name_value_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_contact_first_last_name_value_text)
        except Exception, err:
            raise type(err)("Contact Name not appearing in Points of contact widget  - searched XPATH - " \
                          + self._asset_contact_first_last_name_value_text + err.message)

    @property
    def get_asset_contact_title_value_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_contact_title_value_text_locator)
        except Exception, err:
            raise type(err)("Contact Title not appearing in Points of contact widget  - searched XPATH - " \
                          + self._asset_contact_title_value_text_locator + err.message)

    @property
    def get_asset_contact_phone_value_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_contact_phone_value_text_locator)
        except Exception, err:
            raise type(err)("Contact Phone no not appearing in Points of contact widget  - searched XPATH - " \
                          + self._asset_contact_phone_value_text_locator + err.message)

    @property
    def get_asset_contact_email_value_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_contact_email_value_text_locator)
        except Exception, err:
            raise type(err)("Contact Email ID not appearing in Points of contact widget - searched XPATH - " \
                          + self._asset_contact_email_value_text_locator + err.message)

    @property
    def get_asset_contact_new_contact_value_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_contact_new_contact_text_locator)
        except Exception, err:
            raise type(err)("No Contact appearing in Points of contact widget - searched XPATH - " \
                          + self._asset_contact_new_contact_text_locator + err.message)

    @property
    def get_asset_main_contact_window(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_main_contact_window_locator)
        except Exception, err:
            raise type(err)("Main Contact window title not available - searched XPATH - " \
                          + self._asset_main_contact_window_locator + err.message)

    @property
    def get_asset_main_contact_name_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_main_contact_name_locator)
        except Exception, err:
            raise type(err)("Main Contact name not available - searched XPATH - " \
                          + self._asset_main_contact_name_locator + err.message)

    @property
    def get_asset_point_of_contact_name_tab(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_point_of_contact_name_tab_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget Name Tab not available - searched XPATH - " \
                          + self._asset_point_of_contact_name_tab_locator + err.message)

    @property
    def get_asset_point_of_contact_title_tab(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_point_of_contact_title_tab_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget Title Tab not available  - searched XPATH - " \
                          + self._asset_point_of_contact_title_tab_locator + err.message)

    @property
    def get_asset_point_of_contact_phone_tab(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_point_of_contact_phone_tab_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget Phone Tab not available  - searched XPATH - " \
                          + self._asset_point_of_contact_phone_tab_locator + err.message)

    @property
    def get_asset_point_of_contact_email_tab(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_point_of_contact_email_tab_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget Email Tab not available  - searched XPATH - " \
                          + self._asset_point_of_contact_email_tab_locator + err.message)

    @property
    def get_asset_point_of_contact_name_text_value(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_point_of_contact_name_text_value_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget contacts do not have Name Values - searched XPATH - " \
                          + self._asset_point_of_contact_name_text_value_locator + err.message)

    @property
    def get_asset_point_of_contact_title_text_value(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_point_of_contact_title_text_value_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget contacts do not have Title Values - searched XPATH - " \
                          + self._asset_point_of_contact_title_text_value_locator + err.message)

    @property
    def get_asset_point_of_contact_phone_text_value(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_point_of_contact_phone_text_value_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget contacts do not have Phone Values - searched XPATH - " \
                          + self._asset_point_of_contact_phone_text_value_locator + err.message)


    @property
    def get_asset_point_of_contact_email_text_value(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_point_of_contact_email_text_value_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget contacts do not have Email Values - searched XPATH - " \
                          + self._asset_point_of_contact_email_text_value_locator + err.message)

    # Asset Details related properties
    @property
    def get_asset_detail_edit_link(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_link_locator)
        except Exception, err:
            raise type(err)("Asset Details Edit link not available - searched XPATH - " \
                          + self._asset_detail_edit_link_locator + err.message)

    @property
    def get_asset_detail_edit_capacity_text_box(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, self._asset_detail_edit_capacity_textbox_locator)))
            return self.driver.find_element_by_xpath(self._asset_detail_edit_capacity_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_capacity_textbox_locator + err.message)

    @property
    def get_asset_detail_edit_closed_text_box(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_detail_edit_closed_textbox_locator)[0]
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_closed_textbox_locator + err.message)

    @property
    def get_asset_detail_edit_detail_opened_number_text_box(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_detail_edit_closed_textbox_locator)[1]
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_closed_textbox_locator + err.message)

    @property
    def get_asset_detail_edit_description_text_box(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_description_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_description_textbox_locator + err.message)

    @property
    def get_asset_detail_edit_detail_district_number_text_box(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_detail_district_number_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_detail_district_number_textbox_locator + err.message)

    @property
    def get_asset_detail_edit_detail_fax_text_box(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_fax_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_fax_textbox_locator + err.message)

    @property
    def get_asset_detail_edit_detail_school_number_text_box(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_school_number_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_school_number_textbox_locator + err.message)

    @property
    def get_asset_detail_edit_detail_place_size_text_box(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_place_size_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_place_size_textbox_locator + err.message)

    @property
    def get_asset_detail_edit_detail_school_size_text_box(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_school_size_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_school_size_textbox_locator + err.message)

    @property
    def get_asset_detail_edit_detail_website_text_box(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_website_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_website_textbox_locator + err.message)

    @property
    def get_asset_detail_edit_email_text_box(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_email_textbox_locator)
        except Exception, err:
            raise type(err)("Asset Details Edit window's email text box not available. - searched XPATH - " \
                          + self._asset_detail_edit_email_textbox_locator + err.message)

    @property
    def get_asset_detail_email_value_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_email_value_text_locator)
        except Exception, err:
            raise type(err)("Asset Details email value text box not available. - searched XPATH - " \
                          + self._asset_detail_email_value_text_locator + err.message)

    @property
    def get_asset_detail_edit_save_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_save_button_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_save_button_locator + err.message)

    @property
    def get_asset_detail_edit_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_cancel_button_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_cancel_button_locator + err.message)

    @property
    def get_asset_detail_edit_window_cross_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_detail_edit_window_popup_cross_button_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_detail_edit_window_popup_cross_button_locator + err.message)

    # Asset overview related properties
    @property
    def get_asset_overview_edit_link(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_edit_link_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_overview_edit_link_locator + err.message)

    @property
    def get_asset_overview_edit_name_text_box(self):
        try:
            return self.driver.find_element_by_name(self._asset_overview_edit_name_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_overview_edit_name_textbox_locator + err.message)

    @property
    def get_asset_overview_window_cross_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_overview_window_popup_cross_button_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_overview_window_popup_cross_button_locator + err.message)

    @property
    def click_on_asset_link(self):
        try:
            return self.driver.find_element_by_link_text(self._asset_link_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_link_locator + err.message)

    @property
    def get_asset_header_save_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_header_save_text_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_header_save_text_locator + err.message)

    @property
    def select_asset_search_text_box(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_search_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_search_textbox_locator + err.message)

    @property
    def get_asset_photos_documents_header_text(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_photos_documents_header_locator)
        except Exception, err:
            raise type(err)("Photos / Documents widget header not available - searched XPATH - " \
                          + self._asset_photos_documents_header_locator + err.message)

    @property
    def get_asset_photos_documents_uploaded_file_count(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_photos_documents_uploaded_file_locator)
        except Exception, err:
            raise type(err)("In Photos / Documents widget, No file uploaded - searched XPATH - " \
                          + self._asset_photos_documents_uploaded_file_locator + err.message)

    @property
    def get_asset_photos_documents_upload_file_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_photos_documents_upload_file_button_locator)
        except Exception, err:
            raise type(err)("File Upload button not available - searched XPATH - " \
                          + self._asset_photos_documents_upload_file_button_locator + err.message)

    @property
    def get_asset_photos_documents_attached_file_button(self):
        try:
            return self.driver.find_element_by_id(self._asset_photos_documents_attached_file_button_locator)
        except Exception, err:
            raise type(err)("In File Upload window Attach File button is not available - searched XPATH - " \
                          + self._asset_photos_documents_attached_file_button_locator + err.message)

    @property
    def get_asset_photos_documents_caption_textbox(self):
        try:
            return self.driver.find_element_by_id(self._asset_photos_documents_caption_textbox_locator)
        except Exception, err:
            raise type(err)("In File Upload window Caption Text Box is not available - searched XPATH - " \
                          + self._asset_photos_documents_caption_textbox_locator + err.message)

    @property
    def get_asset_photos_documents_window_upload_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_photos_documents_window_upload_button_locator)
        except Exception, err:
            raise type(err)("In File Upload window Upload button is not available - searched XPATH - " \
                          + self._asset_photos_documents_window_upload_button_locator + err.message)

    @property
    def get_asset_photos_documents_window_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_photos_documents_window_cancel_button_locator)
        except Exception, err:
            raise type(err)("In File Upload window Cancel button is not available - searched XPATH - " \
                          + self._asset_photos_documents_window_cancel_button_locator + err.message)

    @property
    def get_asset_photos_documents_delete_icon_image(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_photos_documents_delete_icon_locator)
        except Exception, err:
            raise type(err)("Delete icon is not displayed - search XPATH - " \
                          + self._asset_photos_documents_delete_icon_locator + err.message)

    @property
    def get_asset_photos_documents_delete_window_delete_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_photos_documents_delete_window_delete_locator)
        except Exception, err:
            raise type(err)("In File Delete Window Delete button is not available - searched XPATH - " \
                          + self._asset_photos_documents_delete_window_delete_locator + err.message)

    @property
    def get_asset_annotation_plus_image(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_annotation_plus_image_locator)
        except Exception, err:
            raise type(err)("In Annotation widget Edit/Plus image not available - searched XPATH - " \
                          + self._asset_annotation_plus_image_locator + err.message)

    @property
    def get_asset_annotation_edit_window_text_area(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_text_area_locator)
        except Exception, err:
            raise type(err)("In Annotation edit window text are is not available - searched XPATH - " \
                          + self._asset_annotation_edit_window_text_area_locator + err.message)

    @property
    def get_asset_annotation_edit_window_visibility_dropdown(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_visibility_dropdown_locator)
        except Exception, err:
            raise type(err)("In Annotation edit window visibility drop down is not available - searched XPATH - " \
                          + self._asset_annotation_edit_window_visibility_dropdown_locator + err.message)

    @property
    def get_asset_annotation_edit_window_dropdown_groups(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_dropdown_groups_locator)
        except Exception, err:
            raise type(err)("In Annotation edit window visibility groups option is not available - searched XPATH - " \
                          + self._asset_annotation_edit_window_dropdown_groups_locator + err.message)

    @property
    def get_asset_annotation_edit_window_dropdown_tenant(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_dropdown_tenant_locator)
        except Exception, err:
            raise type(err)("In Annotation edit window visibility tenant option is not available - searched XPATH - " \
                          + self._asset_annotation_edit_window_dropdown_tenant_locator + err.message)

    @property
    def get_asset_annotation_edit_window_dropdown_user(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_dropdown_user_locator)
        except Exception, err:
            raise type(err)("In Annotation edit window visibility user option is not available - searched XPATH - " \
                          + self._asset_annotation_edit_window_dropdown_user_locator + err.message)

    @property
    def get_asset_annotation_edit_window_save_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_save_button_locator)
        except Exception, err:
            raise type(err)("In Annotation edit window save button is not available - searched XPATH - " \
                          + self._asset_annotation_edit_window_save_button_locator + err.message)

    @property
    def get_asset_annotation_edit_window_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_cancel_button_locator)
        except Exception, err:
            raise type(err)("In Annotation edit window cancel button is not available - searched XPATH - " \
                          + self._asset_annotation_edit_window_cancel_button_locator + err.message)

    @property
    def get_asset_annotation_text_value(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_annotation_text_value_locator)
        except Exception, err:
            raise type(err)("In Annotation widget no annotation available - searched XPATH - " \
                          + self._asset_annotation_text_value_locator + err.message)

    @property
    def get_asset_annotation_delete_image(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_annotation_delete_image_locator)
        except Exception, err:
            raise type(err)("Annotation text delete link is not available - searched XPATH - " \
                          + self._asset_annotation_delete_image_locator + err.message)
    @property
    def get_asset_annotation_edit_image(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_annotation_edit_image_locator)
        except Exception, err:
            raise type(err)("Annotation text edit link is not available - searched XPATH - " \
                          + self._asset_annotation_edit_image_locator + err.message)
    # Location related properties
    @property
    def get_asset_location_map(self):
        try:
            return self.driver.find_element_by_id(self._asset_location_map_id_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_location_map_id_locator + err.message)

    @property
    def get_asset_location_edit_icon(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_location_edit_icon_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_location_edit_icon_xpath_locator + err.message)

    @property
    def get_asset_location_title(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_location_title_id_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_location_title_id_locator + err.message)

    @property
    def get_asset_location_latitude_textbox(self):
        try:
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located(
                (By.NAME , self._asset_location_latitude_name_locator)))
            return self.driver.find_element_by_name(self._asset_location_latitude_name_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_location_latitude_name_locator + err.message)

    @property
    def get_asset_location_latitude_error_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_location_latitude_error_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_location_latitude_error_xpath_locator + err.message)

    @property
    def get_asset_location_save_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_location_save_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_location_save_xpath_locator + err.message)

    @property
    def get_asset_location_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_location_cancel_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_location_cancel_xpath_locator + err.message)


    @property
    def get_asset_location_longitude_textbox(self):
        try:
            return self.driver.find_element_by_name(self._asset_location_longitude_name_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_location_longitude_name_locator + err.message)

    @property
    def get_asset_location_longitude_error_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_location_longitude_error_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_location_longitude_error_xpath_locator + err.message)

    @property
    def get_asset_location_marker_available_image(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_location_marker_avaliable_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_location_marker_avaliable_xpath_locator + err.message)


    @property
    def get_asset_location_place_name_text(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_location_place_name_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._asset_location_place_name_xpath_locator + err.message)



    # Charts related
    @property
    def get_asset_chart_dashboard_image(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_chart_dashboard_img_xpath_locator)
        except Exception, err:
            raise type(err)(" - search XPATH - " \
                          + self._asset_chart_dashboard_img_xpath_locator + err.message)

    @property
    def get_asset_chart_dashboard_image_off(self):
        try:
            return self.driver.find_element_by_xpath(self._asset_chart_dashboard_img_off_xpath_locator)
        except Exception, err:
            raise type(err)(" - search XPATH - " \
                          + self._asset_chart_dashboard_img_off_xpath_locator + err.message)

    @property
    def get_asset_chart_total_graph(self):
        try:
            return self.driver.find_elements_by_xpath(self._asset_chart_total_Graph_In_Container_xpath_locator)
        except Exception, err:
            raise type(err)(" - search XPATH - " \
                          + self._asset_chart_total_Graph_In_Container_xpath_locator + err.message)

    def get_asset_photos_documents_image_caption_text(self, caption_val):
        caption_xpath = " //div[contains(@ng-repeat,'file in files')]//div[contains(text(),'"+caption_val+"')]"
        try:
            return self.driver.find_element_by_xpath(caption_xpath)
        except Exception, err:
            raise type(err)("Image caption for uploaded file in new window is not available - search XPATH - " \
                          + caption_xpath + err.message)

    def get_asset_photos_documents_header_caption_text(self, caption_val):
        caption_xpath = "//a[contains(text(),'"+caption_val+"')]"
        try:
            return self.driver.find_element_by_xpath(caption_xpath)
        except Exception, err:
            raise type(err)("In Photos / Documents widget Image Caption/File Name is not available - search XPATH - " \
                          + caption_xpath + err.message)

    def get_select_checkbox_in_grid(self):
        """
        Description : This function will select the checkbox from the asset list..
        Revision:
        :return: None
        """
        assets_checkbox = self.driver.find_elements_by_xpath(self._asset_list_check_box_locator)
        sleep(2)
        for asset_checkbox in assets_checkbox:
            sleep(1)
            asset_checkbox.click()

        for asset_checkbox in assets_checkbox:
            sleep(1)
            asset_checkbox.click()

    def asset_filter_based_on_place_and_school(self, assetType):
        """
        Description : This function will select the checkbox from the asset list.
        Revision:
        :return: None
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, self._asset_filter_drop_down_locator))).click()
        self.driver.find_element_by_link_text(assetType).click()

    def get_asset_school_district(self):
        """
        Description : This function will click on school district drop down menu and will select a value.
        Revision:
        :return: None
        """
        self.asset_filter_based_on_place_and_school("School")
        self.driver.find_element_by_xpath(self._asset_school_district_drop_down_locator).click()
        chkDistrictDropDownValuesExists = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div[2]/div/ul")
        items = chkDistrictDropDownValuesExists.find_elements_by_tag_name("li")
        sleep(5)
        if len(items) > 1:
            self.selecteddistrict = self.get_asset_school_district_first_element.text
            self.get_asset_school_district_first_element.click()
        else:
            print "No items to select in District drop down."
        sleep(2)

    def get_asset_school_grade(self):
        """
        Description : This function will click on school grade drop down menu and will select a value.
        Revision:
        :return: None
        """
        self.asset_filter_based_on_place_and_school("School")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(
            (By.XPATH, self._asset_school_grade_drop_down_locator))).click()
        sleep(2)
        chkGradeDropDownValuesExists = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div[3]/div/ul")
        items = chkGradeDropDownValuesExists.find_elements_by_tag_name("li")
        sleep(5)

        if len(items) > 1:
            firstelement =self.driver.find_element_by_xpath\
                (self._asset_school_grade_drop_down_select_first_element_locator)
            self.selectedgrade = firstelement.text
            firstelement.click()
        else:
            print "No items to select in Grade drop down."
        sleep(2)

    def get_asset_school_type(self):
        """
        Description : This function will click on school type drop down menu and will select a value.
        Revision:
        :return: None
        """
        self.asset_filter_based_on_place_and_school("School")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(
            (By.XPATH, self._asset_school_type_drop_down_locator))).click()
        sleep(2)
        #chkSchoolTypeDropDownValuesExists = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div[4]/div/ul")
        chkSchoolTypeDropDownValuesExists = self.driver.find_element_by_xpath(".//*[@id='span_filters']/descendant::div[@label='School Type']/ul")
        items = chkSchoolTypeDropDownValuesExists.find_elements_by_tag_name("li")
        sleep(5)
        if len(items) > 1:
            firstelemet = self.driver.find_element_by_xpath(self._asset_school_type_drop_down_select_first_element_locator)
            self.selectedtype = firstelemet.text
            firstelemet.click()
        else:
            print "No items to select in Type drop down."
        sleep(2)


    def textbox_clear(self, textboxlocator):
        """
        Description : This function will clear search text box.
        Revision:
        :return: None
        """
        textboxlocator.clear()

    def asset_search_assetname(self, name):
        """
        Description : This function will enter string in search text box.
        Revision:
        :return: None
        """
        search_textbox = WebDriverWait(self.driver,20).until(EC.presence_of_element_located(
            (By.XPATH, self._asset_search_textbox_locator)))
        self.textbox_clear(search_textbox)
        search_textbox.send_keys(name)

    def asset_search_special_characters(self):
        """
        Description : This function will enter special characters in search text box.
        Revision:
        :return: None
        """
        searchNames = self.driver.find_elements_by_xpath(AssetPage(self.driver)._asset_list_locator)
        print len(searchNames)
        if len(searchNames) > 0:
            for searchname in searchNames:
                print searchname.text
        else:
            print "No records found."

    @property
    def get_asset_create_asset(self):
        try:
            self.driver.find_element_by_xpath(self._asset_create_asset)
        except:
            return False
        return True

    def return_to_apps_main_page(self):
        """
        Description : This function will helps to go back to assets page.
        Revision:
        :return: None
        """
        if not self.get_asset_create_asset:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                    (By.LINK_TEXT, self._asset_link_locator))).click()
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self._asset_create_asset)))
            except:
                inspectstack = inspect.stack()[1][3]
                self.recoverapp(inspectstack)

    def recoverapp(self, inspectstack):
        """
        Description : This function helps to go back to assets page. Inspect stack prints the test name from which
                                 this function is called.
        Revision:
        :return: None
        """
        print ("Application recovering called from " + inspectstack)
        basepage = BasePage(self.driver)
        basepage.accessURL()
        iconlistpage = IconListPage(self.driver)
        iconlistpage.click_asset_icon()

    def app_sanity_check(self):
        """
        Description : This function should be called before any test to see the asset page is displayed.
        Revision:
        :return: None
        """
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._asset_create_asset)))
        except:
            inspectstack = inspect.stack()[1][3]
            self.recoverapp(inspectstack)

    def asset_create_click(self):
        """
        Description : This function will click on Create Asset Link.
        Revision:
        :return: None
        """
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._asset_select_action_delete_select_xpath_locator)))
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, self._asset_create_asset))).click()

    def select_asset_template_type(self, template):
        # Select Place from the dropdown to create new place asset
        self.get_overview_templatetype_drop_down.click()
        self.driver.find_element_by_link_text(template).click()

    def get_placedata(self):
        with open(placeData) as data_file:
            for each in json.load(data_file):
                self.asset_place_name = each["asset_name"]
                self.asset_place_address = each["asset_address"]
                self.asset_place_address2 = each["asset_address2"]
                self.asset_place_city = each["asset_city"]
                self.asset_place_state = each["asset_state"]
                self.asset_place_zip = each["asset_zip"]
                self.asset_place_owner = each["asset_owner"]
                self.asset_place_type = each["asset_type"]

    def create_place_asset(self):
        """
        Description : This function will enter place data in asset template.
        Revision:
        :return: None
        """
        self.select_asset_template_type("Place")
        self.enter_asset_type_name.send_keys(self.asset_place_name)
        self.enter_asset_type_address.send_keys(self.asset_place_address)
        self.enter_asset_type_address2.send_keys(self.asset_place_address2)
        self.enter_asset_type_city.send_keys(self.asset_place_city)
        self.enter_asset_type_state.send_keys(self.asset_place_state)
        self.enter_asset_type_zip.send_keys(self.asset_place_zip)
        self.enter_asset_type_owner.send_keys(self.asset_place_owner)
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(
            (By.XPATH, self._asset_overview_type_drop_down_locator))).click()
        sleep(2)
        self.get_overview_newtype_text_box.send_keys(self.asset_place_type)
        self.get_overview_place_type_add_button.click()
        self.get_asset_overview_save_button.click()


    def get_schooldata(self):
        """
        Description : This function will read school data from json file.
        Revision:
        :return: None
        """
        with open(L1) as data_file:
            for each in json.load(data_file):
                self.asset_school_name = each["asset_name"]
                self.asset_school_address = each["asset_address"]
                self.asset_school_address2 = each["asset_address2"]
                self.asset_school_city = each["asset_city"]
                self.asset_school_state = each["asset_state"]
                self.asset_school_zip = each["asset_zip"]
                self.asset_school_owner = each["asset_owner"]
                self.asset_school_type = each["asset_type"]
                self.asset_school_district = each["asset_district"]
                self.asset_school_grade = each["asset_grade"]
                self.asset_school_district_grade_validation = each["asset_dist_grade_validation"]
                self.asset_contact_firstname = each["contact_firstname"]
                self.asset_contact_lastname = each["contact_firstname"]


    def create_school_asset(self, index, schoolname):
        """
        Description : This function will enter school data in asset template.
        Revision:
        :return: None
        """
        if(index == 0):
            self.enter_asset_type_name.send_keys(schoolname)
        else:
            self.get_overview_editname_text_box.clear()
            self.get_overview_editname_text_box.send_keys(schoolname)
        self.enter_asset_type_address.clear()
        self.enter_asset_type_address.send_keys(self.asset_school_address[index])
        self.enter_asset_type_address2.clear()
        self.enter_asset_type_address2.send_keys(self.asset_school_address2[index])
        self.enter_asset_type_city.clear()
        self.enter_asset_type_city.send_keys(self.asset_school_city[index])
        self.enter_asset_type_state.clear()
        self.enter_asset_type_state.send_keys(self.asset_school_state[index])
        self.enter_asset_type_zip.clear()
        self.enter_asset_type_zip.send_keys(self.asset_school_zip[index])
        self.enter_asset_type_owner.clear()
        self.enter_asset_type_owner.send_keys(self.asset_school_owner[index])
        self.enter_school_district(self.asset_school_district[index])
        self.enter_school_grade(self.asset_school_grade[index])
        self.enter_asset_type(self.asset_school_type[index])
        self.get_asset_overview_save_button.click()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self._asset_name_breadcrumb), self.get_asset_name_breadcrumb.text))

    def enter_school_district(self, value):
        """
        Description : This function will enter school district info in the text box.
        Revision:
        :return: None
        """
        sleep(2)
        self.get_overview_district_drop_down.click()
        sleep(2)
        self.get_overview_newdistrict_text_box.send_keys(value)
        self.get_overview_district_add_button.click()

    def enter_school_grade(self, value):
        """
        Description : This function will enter school grade info in the text box.
        Revision:
        :return: None
        """
        sleep(2)
        self.get_overview_grade_drop_down.click()
        sleep(2)
        self.get_overview_newgrade_text_box.send_keys(value)
        self.get_overview_grade_add_button.click()

    def enter_asset_type(self, value):
        """
        Description : This function will enter school type info in the text box.
        Revision:
        :return: None
        """
        sleep(2)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, self._asset_overview_type_drop_down_locator))).click()
        self.get_overview_school_newtype_text_box.send_keys(value)
        self.get_overview_type_add_button.click()
        #self.get_overview_type_drop_down.send_keys(Keys.TAB, value, Keys.TAB, Keys.ENTER)

    def asset_overview_save_click(self):
        """
        Description : This function will click on save button of overview window.
        Revision:
        :return: None
        """
        self.get_asset_overview_save_button.click()
        sleep(2)

    def asset_overview_cancel_click(self):
        """
        Description : This function will click on cancel button of overview window.
        Revision:
        :return: None
        """
        self.get_asset_overview_cancel_button.click()
        sleep(2)
        '''
        # check all fields are enabled
        self.assertTrue(place_name.is_enabled()
                        and place_address.is_enabled()
                        and place_address2.is_enabled()
                        and place_city.is_enabled()
                        and place_state.is_enabled()
                        and place_zip.is_enabled()
                        and place_owner.is_enabled()
                        and place_phone.is_enabled()
                        and place_type.is_enabled()
                        and place_cancel.is_enabled()
                        and place_save.is_enabled())
        '''
    newSchool = 0
    editSchool = 1

    def create_asset(self, type):
        """
        Description : This function will create asset Place/School.
        Revision:
        :return: None
        """
        self.asset_create_click()
        if type == "School":
            self.select_asset_template_type("School")
            self.create_school_asset(self.newSchool, self.asset_school_name[self.newSchool])
        elif type == "Place":
            self.create_place_asset()


    def create_school_asset_for_assessmentapp(self, schoolname):
        self.recoverapp(inspect.stack()[1][3])
        self.asset_create_click()
        self.select_asset_template_type("School")
        self.create_school_asset(self.newSchool, schoolname)

    def edit_asset(self, type):
        """
        Description : This function will edit asset Place/School.
        Revision:
        :return: None
        """
        self.select_school_or_place_asset(self.asset_school_name[0], type)
        if type == "School":
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self._asset_details_edit_widget_locator), "Details"))
            self.get_asset_overview_edit_link.click()
            self.create_school_asset(self.editSchool, self.asset_school_name[self.editSchool])
        elif type == "Place":
            self.create_place_asset()
        self.asset_overview_save_click()

    def create_asset_cancel(self, type):
        """
        Description : This function will cancel asset creation.
        Revision:
        :return: None
        """
        self.asset_create_click()
        if type == "School":
            self.select_asset_template_type("School")
            self.create_school_asset(self.newSchool, self.asset_school_name[self.newSchool])
        elif type == "Place":
            self.create_place_asset()
        self.asset_overview_cancel_click()

    def select_school_or_place_asset(self, asset_name1,asset_type):
        """
        Description : This function will select an asset from asset list.
        Revision:
        :return: None
        """
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._asset_select_action_delete_select_xpath_locator)))
        try:
            self.asset_search_assetname(asset_name1)
            sleep(6)
            asset_list = self.get_assets_name_list
            if len(asset_list)>=1:
                for i in asset_list:
                    if i.text == asset_name1:
                        i.click()
                        break
            else:
                sleep(4)
                self.asset_search_assetname("")
                sleep(2)
                self.create_asset(asset_type)
                sleep(2)
        except Exception, err:
            raise type(err)("No Asset is existing or Asset Creation has been failed. "+err.message)


    def set_place_overview_fields(self,paddress, paddress1, pcity, pstate, pzip, powner):
        """
        Description : This function will enter data in all fields of Overview Edit Window.
        Revision:
        :return: None
        """
        self.enter_asset_type_address.clear()
        self.enter_asset_type_address.send_keys(paddress)
        self.enter_asset_type_address.send_keys(Keys.TAB)
        self.enter_asset_type_address2.clear()
        self.enter_asset_type_address2.send_keys(paddress1)
        self.enter_asset_type_address2.send_keys(Keys.TAB)
        self.enter_asset_type_city.clear()
        self.enter_asset_type_city.send_keys(pcity)
        self.enter_asset_type_city.send_keys(Keys.TAB)
        self.enter_asset_type_state.clear()
        self.enter_asset_type_state.send_keys(pstate)
        self.enter_asset_type_state.send_keys(Keys.TAB)
        self.enter_asset_type_zip.clear()
        self.enter_asset_type_zip.send_keys(pzip)
        self.enter_asset_type_zip.send_keys(Keys.TAB)
        self.enter_asset_type_phone.send_keys(Keys.TAB)
        self.enter_asset_type_owner.clear()
        self.enter_asset_type_owner.send_keys(powner)
        self.enter_asset_type_owner.send_keys(Keys.TAB)

    def set_place_details_fields(self, pcapacity, pclosed, pdescription, pemail, pfax, popened, psize, pwebsite):
        # fill out the fields

        self.get_asset_detail_edit_capacity_text_box.clear()
        self.get_asset_detail_edit_capacity_text_box.send_keys(pcapacity)
        self.get_asset_detail_edit_capacity_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_closed_text_box.clear()
        self.get_asset_detail_edit_closed_text_box.send_keys(pclosed)
        self.get_asset_detail_edit_closed_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_description_text_box.clear()
        self.get_asset_detail_edit_description_text_box.send_keys(pdescription)
        self.get_asset_detail_edit_description_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_email_text_box.clear()
        self.get_asset_detail_edit_email_text_box.send_keys(pemail)
        self.get_asset_detail_edit_email_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_detail_fax_text_box.clear()
        self.get_asset_detail_edit_detail_fax_text_box.send_keys(pfax)
        self.get_asset_detail_edit_detail_fax_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_detail_opened_number_text_box.clear()
        self.get_asset_detail_edit_detail_opened_number_text_box.send_keys(popened)
        self.get_asset_detail_edit_detail_opened_number_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_detail_place_size_text_box.clear()
        self.get_asset_detail_edit_detail_place_size_text_box.send_keys(psize)
        self.get_asset_detail_edit_detail_place_size_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_detail_website_text_box.clear()
        self.get_asset_detail_edit_detail_website_text_box.send_keys(pwebsite)
        self.get_asset_detail_edit_detail_website_text_box.send_keys(Keys.TAB)

    def set_school_details_fields(self, pcapacity, pclosed, pdescription, pdistrict, pemail, pfax, popened, pschoolnumber, ssize, pwebsite):
        # fill out the fields
        #WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, self._asset_detail_edit_capacity_textbox_locator)))
        self.get_asset_detail_edit_capacity_text_box.clear()
        self.get_asset_detail_edit_capacity_text_box.send_keys(pcapacity)
        self.get_asset_detail_edit_capacity_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_closed_text_box.clear()
        self.get_asset_detail_edit_closed_text_box.send_keys(pclosed)
        self.get_asset_detail_edit_closed_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_description_text_box.clear()
        self.get_asset_detail_edit_description_text_box.send_keys(pdescription)
        self.get_asset_detail_edit_description_text_box.send_keys(Keys.TAB)
        if pdistrict is not None:
            self.get_asset_detail_edit_detail_district_number_text_box.send_keys("")
            self.get_asset_detail_edit_detail_district_number_text_box.send_keys(pdistrict)
            self.get_asset_detail_edit_detail_district_number_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_email_text_box.clear()
        self.get_asset_detail_edit_email_text_box.send_keys(pemail)
        self.get_asset_detail_edit_email_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_detail_fax_text_box.clear()
        self.get_asset_detail_edit_detail_fax_text_box.send_keys(pfax)
        self.get_asset_detail_edit_detail_fax_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_detail_opened_number_text_box.clear()
        self.get_asset_detail_edit_detail_opened_number_text_box.send_keys(popened)
        self.get_asset_detail_edit_detail_opened_number_text_box.send_keys(Keys.TAB)
        if pschoolnumber is not None:
            self.get_asset_detail_edit_detail_school_number_text_box.send_keys("")
            self.get_asset_detail_edit_detail_school_number_text_box.send_keys(pschoolnumber)
            self.get_asset_detail_edit_detail_school_number_text_box.send_keys(Keys.TAB)
        if ssize is not None:
            self.get_asset_detail_edit_detail_school_size_text_box.send_keys("")
            self.get_asset_detail_edit_detail_school_size_text_box.send_keys(ssize)
            self.get_asset_detail_edit_detail_school_size_text_box.send_keys(Keys.TAB)
        self.get_asset_detail_edit_detail_website_text_box.clear()
        self.get_asset_detail_edit_detail_website_text_box.send_keys(pwebsite)
        self.get_asset_detail_edit_detail_website_text_box.send_keys(Keys.TAB)

    def delete_existing_contact(self):
        """
        Description : This function will delete existing contact.
        Revision:
        :return: None
        """
        try:
            while(self.get_asset_newcontact_delete_icon.is_displayed()):
                sleep(2)
                self.get_asset_newcontact_delete_icon.click()
                sleep(1)
                self.get_asset_newcontact_delete_popup_delete_button.click()
        except Exception, err:
            pass

    def create_new_contact(self, firstname, lastname, title="Title", phone=r"111-111-1111", email=r"test@test.com",
                                        prefix="Shri", address1="Indecomm", address2=r"Brigade South Parade",
                                        city="Bangalore", state="KA", zip="56001"):
        """
        Description : This function will create new contact.
        Revision:
        :return: None
        """
        self.get_asset_points_of_contact_header.click()
        self.get_asset_add_contact_button.click()
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element((By.XPATH,
                                                  self._assets_points_of_contact_title_locator), "Contact information"))
        self.get_asset_newcontact_firstname_textbox.clear()# Fill all fields.
        self.get_asset_newcontact_firstname_textbox.send_keys(firstname)
        self.get_asset_newcontact_lastname_textbox.clear()
        self.get_asset_newcontact_lastname_textbox.send_keys(lastname)
        self.get_asset_newcontact_prefix_textbox.clear()
        self.get_asset_newcontact_prefix_textbox.send_keys(prefix)
        self.get_asset_newcontact_title_textbox.clear()
        self.get_asset_newcontact_title_textbox.send_keys(title)
        self.get_asset_newcontact_address1_textbox.clear()
        self.get_asset_newcontact_address1_textbox.send_keys(address1)
        self.get_asset_newcontact_address2_textbox.clear()
        self.get_asset_newcontact_address2_textbox.send_keys(address2)
        self.get_asset_newcontact_city_textbox.clear()
        self.get_asset_newcontact_city_textbox.send_keys(city)
        self.get_asset_newcontact_state_textbox.clear()
        self.get_asset_newcontact_state_textbox.send_keys(state)
        self.get_asset_newcontact_zip_textbox.clear()
        self.get_asset_newcontact_zip_textbox.send_keys(zip)
        self.get_asset_newcontact_phone_textbox.clear()
        self.get_asset_newcontact_phone_textbox.send_keys(phone)
        self.get_asset_newcontact_email_textbox.clear()
        self.get_asset_newcontact_email_textbox.send_keys(email)
        sleep(2)
        self.get_asset_newcontact_save_button.click()#Click on Save Button.
        WebDriverWait(self.driver,100).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                        self._asset_header_save_text_locator), "Saved"))

    def multiple_contact_create(self):
        """
        Description : This function will create multiple contacts.
        Revision:
        :return: None
        """
        sleep(2)
        #delete existing contacts.
        self.delete_existing_contact()
        sleep(2)
        firstname = ['jkl','vwx','def','pqr']
        lastname = ['mno','abc','stu','ghi']
        phonelist = [r'661-111-1111',r'222-222-2222',r'433-333-3333',r'123-444-4444']
        emaillist = [r'stu@vwx',r'abc@def',r'mno@pqr',r'ghi@jkl']
        titlelist = ['HH','ZZ','CC','PP']
        for contact in range(4):
            self.create_new_contact(firstname[contact],lastname[contact],titlelist[contact],phonelist[contact],
                                    emaillist[contact])
            sleep(2)

    def file_path(self, image_file_name):
        """
        Description : This function will generate absolute path and return path.
        Revision:
        :return: Absolute path of the file.
        """
        cur_dir = os.getcwd()
        os.chdir("..")
        complete_file_path = os.path.join(os.getcwd(), "image_file", image_file_name)
        os.chdir(cur_dir)
        return complete_file_path

    def delete_uploaded_files(self):
        """
        Description : This function will existing uploaded files.
        Revision:
        :return:
        """
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
        (By.XPATH, self._asset_photos_documents_header_locator), r"Photos / Documents"))
        self.driver.find_element_by_xpath(self._asset_photos_documents_header_locator).click()
        sleep(2)
        image_icons = self.driver.find_elements_by_xpath("//div[@class='overview']//div//a")
        num_of_files = len(image_icons)
        if num_of_files >= 1:
            sleep(2)
            for count in range(num_of_files, 0, -1):
                index = count
                xpath = r"(//img[@class='neutron_file_delete_icon'])"+"["+str(index)+"]"
                image_icon_xpath =  self.driver.find_element_by_xpath\
                    ("(//img[@class='file_list_img'])[" + str(index)+ "]")
                Hover = ActionChains(self.driver).move_to_element(image_icon_xpath)
                Hover.perform()
                self.driver.find_element_by_xpath(xpath).click()
                self.get_asset_photos_documents_delete_window_delete_button.click()
                WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,
                                                        self._asset_photos_documents_upload_file_button_locator)))
                sleep(3)

    def upload_a_file_with_caption(self, image_caption, image_file_name):
        """
        Description : This function will upload a file with caption.
        Revision:
        :return:
        """
        # Click on Photo/Document panel - File Upload button
        self.get_asset_photos_documents_upload_file_button.click()
        # Click on Attach file button and attached the file path with the send_keys
        file_path = self.file_path(image_file_name)
        self.get_asset_photos_documents_attached_file_button.send_keys(file_path)
        # Enter Caption
        caption_val = image_caption
        self.get_asset_photos_documents_caption_textbox.send_keys(caption_val)
        # Click Upload.
        self.get_asset_photos_documents_window_upload_button.click()
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,self._asset_photos_documents_header_locator)))
        try:
            WebDriverWait(self.driver,100).until(EC.text_to_be_present_in_element((By.XPATH, self._asset_header_save_text_locator), "Saved"))
        except Exception, err:
            print type(err)("File could not be uploaded or Saved text does not appear."+err.message)

    def delete_all_annotation(self):
        """
        Description : This function will delete all annotation texts.
        Revision:
        :return:
        """
        try:
            sleep(2)
            while(self.get_asset_annotation_delete_image.is_displayed()):
                sleep(2)
                self.get_asset_annotation_delete_image.click()
                sleep(2)
        except Exception, err:
            pass

    # Charts related functions
    svg_path_1=r"//*[name()='svg' and namespace-uri()='http://www.w3.org/2000/svg']"
    svg_path_2=r"/*[name()='text']"

    def charts_When_No_Asset_Type_Is_Selected(self):
        """
        Description : This function will display available chart names in the container when no asset is selected.
        Revision:
        :return:
        """
        chart_xpath = r"//div[starts-with(@id,'asset_graph-0')]"+self.svg_path_1+self.svg_path_2
        totalGraphInContainer = self.get_asset_chart_total_graph
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                if totalGraph.text == "Asset Type":
                    assets = self.driver.find_elements_by_xpath(str(chart_xpath))
                    for asset in assets:
                        print asset.text
        else :
            print "No chart found at place level."

    def place_related_charts_Place_Is_Selected(self):
        """
        Description : This function will display available chart names in the container when place is selected.
        Revision:
        :return:
        """
        chart_xpath = r"//div[starts-with(@id,'asset_graph-0')]"+self.svg_path_1+self.svg_path_2
        totalGraphInContainer = self.get_asset_chart_total_graph
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."
                assets = self.driver.find_elements_by_xpath(str(chart_xpath))
                for asset in assets:
                    print asset.text
        else :
            print "No chart found at place level."


    def place_related_charts_Place_And_Type_Is_Selected(self):
        """
        Description: This function will display available chart names in the container when place and type are selected.
        Revision:
        :return:
        """
        chart_xpath = self.svg_path_1+self.svg_path_2+r"/*[name()='tspan']"
        totalGraphInContainer = self.get_asset_chart_total_graph
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."
                if totalGraph.text == "Type":
                    assets = totalGraph.find_elements_by_xpath(str(chart_xpath))
                    for asset in assets:
                        print asset.text
        else :
            print "No chart found at place and type level."

    def school_related_charts_School_Is_Selected(self):
        """
        Description: This function will display available chart names in the container when school is selected.
        Revision:
        :return:
        """
        chart_xpath_1 = "//div[starts-with(@id,'asset_graph-0')]"+self.svg_path_1+self.svg_path_2
        chart_xpath_2 = "//div[starts-with(@id,'asset_graph-1')]"+self.svg_path_1+self.svg_path_2
        chart_xpath_3 = "//div[starts-with(@id,'asset_graph-2')]"+self.svg_path_1+self.svg_path_2
        totalGraphInContainer = self.get_asset_chart_total_graph
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."
                if totalGraph.text == "District":
                    sleep(2)
                    assets = self.driver.find_elements_by_xpath(str(chart_xpath_1))
                    for asset in assets:
                        print asset.text
                elif totalGraph.text == "Grade Level":
                    sleep(2)
                    assets = self.driver.find_elements_by_xpath(str(chart_xpath_2))
                    for asset in assets:
                        print asset.text
                elif totalGraph.text == "School Type":
                    sleep(2)
                    assets = self.driver.find_elements_by_xpath(str(chart_xpath_3))
                    for asset in assets:
                        print asset.text
        else :
            print "No chart found at school level."


    def school_related_charts_School_And_District_Is_Selected(self):
        """
        Description: This function will display available chart names in the container when school and district are
                        selected.
        Revision:
        :return:
        """
        chart_xpath_1 = "//div[starts-with(@id,'asset_graph-0')]"+self.svg_path_1+self.svg_path_2
        chart_xpath_2 = "//div[starts-with(@id,'asset_graph-1')]"+self.svg_path_1+self.svg_path_2
        totalGraphInContainer = self.get_asset_chart_total_graph
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."
                if totalGraph.text == "Grade Level":
                    assets = self.driver.find_elements_by_xpath(str(chart_xpath_1))
                    for asset in assets:
                        print asset.text
                elif totalGraph.text == "School Type":
                    assets = self.driver.find_elements_by_xpath(str(chart_xpath_2))
                    for asset in assets:
                        print asset.text
        else :
            print "No chart found at school and district level."

    def school_related_charts_School_And_Grade_Is_Selected(self):
        """
        Description: This function will display available chart names in the container when school and grade are
                        selected.
        Revision:
        :return:
        """
        chart_xpath_1 = "//div[starts-with(@id,'asset_graph-0')]"+self.svg_path_1+self.svg_path_2
        chart_xpath_2 = "//div[starts-with(@id,'asset_graph-1')]"+self.svg_path_1+self.svg_path_2
        totalGraphInContainer = self.get_asset_chart_total_graph
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."
                if totalGraph.text == "District":
                    assets = self.driver.find_elements_by_xpath(str(chart_xpath_1))
                    for asset in assets:
                        print asset.text
                elif totalGraph.text == "School Type":
                    assets = self.driver.find_elements_by_xpath(str(chart_xpath_2))
                    for asset in assets:
                        print asset.text
        else :
            print "No chart found at school and grade level."

    def school_related_charts_School_And_Type_Is_Selected(self):
        """
        Description: This function will display available chart names in the container when school and type are
                        selected.
        Revision:
        :return:
        """
        chart_xpath_1 = "//div[starts-with(@id,'asset_graph-0')]"+self.svg_path_1+self.svg_path_2
        chart_xpath_2 = "//div[starts-with(@id,'asset_graph-1')]"+self.svg_path_1+self.svg_path_2
        totalGraphInContainer = self.get_asset_chart_total_graph
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."
                if totalGraph.text == "District":
                    assets = self.driver.find_elements_by_xpath(str(chart_xpath_1))
                    for asset in assets:
                        print asset.text
                elif totalGraph.text == "Grade Level":
                    assets = self.driver.find_elements_by_xpath(str(chart_xpath_2))
                    for asset in assets:
                        print asset.text
        else :
            print "No chart found at school and type level."

    def get_total_row_count(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._asset_select_action_delete_select_xpath_locator)))
        countText = self.driver.find_element_by_id("assetstable_info").text
        splitedText = countText.split("of")
        while '' in splitedText:
            splitedText.remove('')
        totalCount = splitedText[1].replace(" entries", "")
        return int(totalCount)

    def get_total_row_count_filter(self):
        countText = self.driver.find_element_by_id("assetstable_info").text
        splitedText = countText.split(" ")
        totalCount = splitedText[6]
        return int(totalCount)

    def _validate_page(self, driver):
        pass
