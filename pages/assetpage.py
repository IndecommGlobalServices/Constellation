from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from basepage import BasePage
from time import sleep, time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import os, json, inspect
from selenium.webdriver.common.action_chains import ActionChains

filepathschool = "data" + os.sep + "json_Schooldata.json"
filepathplace = "data" + os.sep + "json_Placedata.json"
cwd = os.getcwd()
os.chdir('..')
L1 = os.path.join(os.getcwd(), filepathschool)
placeData = os.path.join(os.getcwd(), filepathplace)
os.chdir(cwd)

class AssetPage(BasePageClass):

    selectedgrade = ""
    selecteddistrict = ""
    selectedtype = ""

    # Asset Delete related locators
    _asset_select_action_delete_select_xpath_locator = ".//*[@id='asset_actions_dropdown']/button[2]"
    _asset_link_delete_text_xpath_locator = ".//*[@id='asset_actions_dropdown']/ul/li/a"
    _asset_list_select_first_check_box_xpath_locator = ".//*[@id='assetstable']/tbody/tr[1]/td[1]/label/span/span[2]"
    _asset_select_action_delete_click_xpath_locator = ".//*[@id='delete_asset_modal']/div/div/div[3]/button[2]"
    _asset_deleteasset_cancel_click_xpath_locator = ".//*[@id='delete_asset_modal']/div/div/div[3]/button[1]"

    # Asset List related locators
    _asset_list_locator = "//tbody/tr/td/a"
    _asset_list_check_box_locator = ".//*[@id='assetstable']/tbody/tr/td[1]/label/span/span[2]"
    _asset_list_assets_name_locator = ".//*[@id='assetstable']/tbody/tr/td[2]/a"
    _asset_list_asset_type_locator = ".//*[@id='assetstable']/tbody/tr/td[3]"
    _asset_list_No_Matching_Records_Found_locator = ".//*[@id='assetstable']/tbody/tr/td"
    _asset_list_asset_name_back_color_locator = ".//*[@id='assetstable']/tbody/tr/td[2]"

    # Asset name on Breadcrumb
    _asset_name_breadcrumb = "//*[@id='header']/div[1]/span[3]/span"

    # Asset Filter related to place and school
    _asset_filter_drop_down_locator = "//*[@id='span_filters']/div/div/button[2]"
    _asset_place_type_drop_down_locator = ".//*[@id='span_filters']/div[2]/div/button[2]"
    _asset_place_type_drop_down_select_first_element_locator = ".//*[@id='span_filters']/div[2]/div/ul/li[1]/a"
    _asset_school_district_drop_down_locator = ".//*[@id='span_filters']/div[2]/div/button[2]"
    _asset_school_district_drop_down_select_first_element_locator = ".//*[@id='span_filters']/div[2]/div/ul/li[1]/a"
    _asset_school_district_lists_locator = ".//*[@id='assetstable']/tbody/tr/td[4]"

    _asset_school_grade_drop_down_locator = ".//*[@id='span_filters']/div[3]/div/button[2]"
    _asset_school_grade_drop_down_select_first_element_locator = ".//*[@id='span_filters']/div[3]/div/ul/li[1]/a"
    _asset_school_grade_lists_locator = ".//*[@id='assetstable']/tbody/tr/td[5]"

    _asset_school_type_drop_down_locator = ".//*[@id='span_filters']/div[4]/div/button[2]"
    _asset_school_type_drop_down_select_first_element_locator = ".//*[@id='span_filters']/div[4]/div/ul/li[1]/a"
    _asset_school_type_lists_locator = ".//*[@id='assetstable']/tbody/tr/td[6]"

    #asset search textbox
    _asset_search_textbox_locator = ".//*[@id='txt_search_assets']"

    # New Asset creation related
    _asset_create_asset = "//img[@alt='Create asset']"

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
    _asset_type_Saved_label_locator = ".//*[@id='header']/div[3]"

    # Overview panel related
    #Asset Overview dialouge locators
    _asset_overview_templatetype_dropdown_locator = "(//div[@label='Type']//button[@data-toggle='dropdown'])"
    _asset_overview_name_text_box_locator = "//input[@ng-model='model']"
    _asset_overview_address_text_box_locator = "//input[@ng-model='asset_edit.address.address1']"
    _asset_overview_address2_text_box_locator = "//input[@ng-model='asset_edit.address.address2']"
    _asset_overview_city_text_box_locator = "//input[@ng-model='asset_edit.address.city']"
    _asset_overview_state_text_box_locator = "//input[@ng-model='asset_edit.address.state']"
    _asset_overview_zip_text_box_locator = "//input[@ng-model='asset_edit.address.zip']"
    _asset_overview_owner_text_box_locator = "//input[@placeholder='Owner']"
    _asset_overview_phone_text_box_locator = "//input[@ng-model='asset_edit.phone']"
    _asset_overview_type_text_box_locator = ".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/ul/li/input"
    _asset_overview_district_text_box_locator = ".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li/input"
    _asset_overview_grade_text_box_locator = ".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li/input"

    _asset_overview_type_drop_down_locator = ".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/button[1]"
    _asset_overview_type_drop_down_locator = "(//div[@label='Type']//button[@data-toggle='dropdown'])[2]"
    _asset_overview_district_drop_down_locator = "//div[@label= 'District']"
    _asset_overview_grade_drop_down_locator = "//div[@label= 'Grade']"
    _asset_overview_add_button_locator = ".//*[@id='newItemButton']"
    _asset_overview_cancel_button_locator = "//div[@id='asset_overview_modal']/div/div/form/div[2]/button[1]"
    _asset_overview_save_button_locator = "//div[@id='asset_overview_modal']/div/div/form/div[2]/button[2]"
    _asset_overview_panel_name_text = ".//*[@id='widgets']/div[1]/div/div[2]/table/tbody/tr[1]/td[2]"
    _asset_overview_panel_address_text = ".//*[@id='widgets']/div[1]/div/div[2]/table/tbody/tr[2]/td[2]"
    _asset_overview_panel_owner_text = ".//*[@id='widgets']/div[1]/div/div[2]/table/tbody/tr[6]/td[2]"
    _asset_overview_panel_district_text = ".//*[@id='widgets']/div[1]/div/div[2]/table/tbody/tr[4]/td[2]"
    _asset_overview_panel_grade_text = ".//*[@id='widgets']/div[1]/div/div[2]/table/tbody/tr[5]/td[2]"
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
    _asset_newcontact_delete_contact_icon_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])[1]/../following-sibling::td[4]//a//img"
    _asset_newcontact_delete_contact_popup_delete_button_locator = ".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]"
    _asset_newcontact_delete_contact_popup_cancel_button_locator = ".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[1]"
    _asset_newcontact_window_popup_cross_button_locator = ".//*[@id='asset_contact_modal']/div/div/div/button"
    _asset_newcontact_firstname_error_message_locator = ".//*[@id='asset_contact_error']/div[1]/small"
    _asset_newcontact_lastname_error_message_locator = ".//*[@id='asset_contact_error']/div[2]/small"
    _asset_newcontact_email_error_message_locator = ".//*[@id='asset_contact_error']/div[6]/small"
    _asset_newcontact_state_error_message_locator = "//*[@id='asset_contact_error']/div[3]/small"
    _asset_newcontact_zip_error_message_locator = "//*[@id='asset_contact_error']/div[4]/small"
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
    _asset_detail_edit_title_locator = ".//*[@id='H2']"
    _asset_detail_edit_capacity_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[1]/div/span/input"
    _asset_detail_edit_closed_textbox_locator = ".//*[@id='datetimepicker']/div/input"
    _asset_detail_edit_description_textbox_locator = ".//*[@id='asset_details_description_edit']"
    _asset_detail_edit_detail_district_number_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[4]/div/span/input"
    _asset_detail_edit_fax_textbox_locator = "//input[@placeholder='Fax, e.g. 555-555-5555']"
    _asset_detail_edit_opened_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[6]/div/span/input"
    _asset_detail_edit_school_number_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[8]/div/span/input"
    _asset_detail_edit_size_textbox_locator = "//input[@placeholder='size (sq ft)']"
    _asset_detail_edit_email_textbox_locator = "//input[@placeholder='Email']"
    _asset_detail_email_value_text_locator = ".//span[text()='Email']/../following-sibling::td"
    _asset_detail_edit_website_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[8]/div/span/input"
    _asset_detail_edit_save_button_locator = ".//*[@id='asset_details_modal']/div/div/form/div[2]/button[2]"
    _asset_detail_edit_cancel_button_locator = ".//*[@id='asset_details_modal']/div/div/form/div[2]/button[1]"
    _asset_detail_edit_window_popup_cross_button_locator = ".//*[@id='asset_details_modal']/div/div/div/button"


    # Asset Photo/Document Upload Panel
    _asset_photos_documents_header_locator = "//div[contains(text(),'Photos / Documents')]"
    _asset_photos_documents_upload_file_button_locator = "//button[contains(text(), 'Upload file')]"
    _asset_photos_documents_attached_file_button_locator = "upload_document_file_upload"
    _asset_photos_documents_caption_textbox_locator = "upload_document_caption"
    _asset_photos_documents_window_upload_button_locator = ".//*[@id='widget_attach_document_modal']/div/div/div//button[contains(text(),'Upload')]"
    _asset_photos_documents_window_cancel_button_locator = ".//*[@id='widget_attach_document_modal']/div/div/div//button[contains(text(),'Cancel')]"

    # Asset Annotation Panel
    _asset_annotation_plus_image_locator = "//div[contains(text(),'Annotations')]//img"
    _asset_annotation_edit_window_text_area_locator = "//label[text()='Annotation']//following-sibling::textarea"
    _asset_annotation_edit_window_visibility_dropdown_locator = "//label[text()='Visibility']//following-sibling::div//button[@data-toggle='dropdown']"
    _asset_annotation_edit_window_dropdown_groups_locator = "//label[text()='Visibility']//following-sibling::div//ul//li[1]//a"
    _asset_annotation_edit_window_dropdown_tenant_locator = "//label[text()='Visibility']//following-sibling::div//ul//li[2]//a"
    _asset_annotation_edit_window_dropdown_user_locator = "//label[text()='Visibility']//following-sibling::div//ul//li[3]//a"
    _asset_annotation_edit_window_save_button_locator = "//*[@id='asset_annotation_modal']//div//button[text()='Save']"
    _asset_annotation_edit_window_cancel_button_locator = "//*[@id='asset_annotation_modal']//div//button[text()='Cancel']"
    _asset_annotation_text_value_locator = "//div[contains(text(),'Annotations')]//following-sibling::div/div"
    _asset_annotation_delete_image_locator = "//div[contains(text(),'Annotations')]//following-sibling::div/div/div/a[contains(@ng-click,'deleteItem')]"
    _asset_annotation_edit_image_locator = "//div[contains(text(),'Annotations')]//following-sibling::div/div/div/a[contains(@ng-click,'editItem')]"
    # Location related
    _asset_location_map_id_locator = "map_control"
    _asset_location_edit_icon_css_locator = "img.widget_edit"
    _asset_location_title_id_locator = "(H1)[1]"
    _asset_location_latitude_name_locator = "latitude"
    _asset_location_latitude_error_css_locator = "small"
    _asset_location_save_xpath_locator = "(//button[@type='submit'])[2]"
    _asset_location_longitude_name_locator = "longitude"
    _asset_location_longitude_error_xpath_locator = "//div[2]/span/small"

    # Charts related
    _asset_chart_total_Graph_In_Container_xpath_locator = ".//*[@id='graphs_frame']/div/div/div/div[1]"
    #Chart dashboard
    _asset_chart_dashboard_img_xpath_locator = "//img[@title='Dashboard']"

    _asset_count = 0
    _assets = {}


    def __init__(self, driver):
        super(AssetPage, self).__init__(driver)
        self.get_schooldata()
        self.get_placedata()
        appicon = IconListPage(self.driver)
        appicon.click_asset_icon()

    @property
    def get_asset_name_breadcrumb(self):
        return self.driver.find_element_by_xpath(self._asset_name_breadcrumb)

    @property
    def get_assets_name_list(self):
        return self.driver.find_elements_by_xpath(self._asset_list_assets_name_locator)

    @property
    def get_asset_select_action_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_select_action_delete_select_xpath_locator)

    @property
    def get_asset_link_delete_text(self):
        return self.driver.find_element_by_xpath(self._asset_link_delete_text_xpath_locator)

    @property
    def get_asset_delete_button(self):
        return self.driver.find_element_by_xpath(self._asset_select_action_delete_click_xpath_locator)

    @property
    def get_deleteasset_cancel_button(self):
        return self.driver.find_element_by_xpath(self._asset_deleteasset_cancel_click_xpath_locator)

    @property
    def get_asset_reset_button(self):
        return self.driver.find_element_by_xpath(self._asset_filter_reset_button_locator)

    @property
    def get_overview_templatetype_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_overview_templatetype_dropdown_locator)

    @property
    def get_overview_type_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_overview_type_drop_down_locator)

    @property
    def get_overview_district_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_overview_district_drop_down_locator)

    @property
    def get_overview_grade_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_overview_grade_drop_down_locator)

    @property
    def get_asset_asset_type_text(self):
        return self.driver.find_element_by_xpath(self._asset_filter_asset_type_text_locator)

    @property
    def get_asset_list_first_check_box(self):
        return self.driver.find_element_by_xpath(self._asset_list_select_first_check_box_xpath_locator)

    @property
    def get_asset_place_type_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_place_type_drop_down_locator)

    @property
    def get_asset_place_type_first_element(self):
        return self.driver.find_element_by_xpath(self._asset_place_type_drop_down_select_first_element_locator)

    @property
    def get_asset_school_district_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_school_district_drop_down_locator)

    @property
    def get_asset_school_district_first_element(self):
        return self.driver.find_element_by_xpath(self._asset_school_district_drop_down_select_first_element_locator)

    @property
    def get_asset_school_grade_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_school_grade_drop_down_locator)

    @property
    def get_asset_school_grade_first_element(self):
        return self.driver.find_element_by_xpath(self._asset_school_grade_drop_down_select_first_element_locator)

    @property
    def get_asset_school_type_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_school_type_drop_down_locator)

    @property
    def get_asset_school_type_first_element(self):
        return self.driver.find_element_by_xpath(self._asset_school_type_drop_down_select_first_element_locator)

    @property
    def get_asset_list_no_matching_records_found(self):
        return  self.driver.find_element_by_xpath(self._asset_list_No_Matching_Records_Found_locator)

    #_asset_list_asset_name_back_color_locator
    @property
    def get_asset_name_list(self):
        return  self.driver.find_elements_by_xpath(self._asset_list_asset_name_back_color_locator)

    @property
    def enter_asset_type_name(self):
        return self.driver.find_element_by_xpath(self._asset_overview_name_text_box_locator)

    @property
    def enter_asset_type_address(self):
        return self.driver.find_element_by_xpath(self._asset_overview_address_text_box_locator)

    @property
    def enter_asset_type_address2(self):
        return self.driver.find_element_by_xpath(self._asset_overview_address2_text_box_locator)

    @property
    def enter_asset_type_city(self):
        return self.driver.find_element_by_xpath(self._asset_overview_city_text_box_locator)

    @property
    def enter_asset_type_state(self):
        return self.driver.find_element_by_xpath(self._asset_overview_state_text_box_locator)

    @property
    def enter_asset_type_zip(self):
        return self.driver.find_element_by_xpath(self._asset_overview_zip_text_box_locator)

    @property
    def enter_asset_type_owner(self):
        return self.driver.find_element_by_xpath(self._asset_overview_owner_text_box_locator)

    @property
    def enter_asset_type_phone(self):
        return self.driver.find_element_by_xpath(self._asset_overview_phone_text_box_locator)

    #_asset_type_Saved_label_locator
    @property
    def asset_type_Saved_label(self):
        return self.driver.find_element_by_xpath(self._asset_type_Saved_label_locator)

    @property
    def select_asset_type_type_lists(self):
        return self.driver.find_elements_by_xpath(self._asset_school_type_lists_locator)

    @property
    def select_asset_type_district_lists(self):
        return self.driver.find_elements_by_xpath(self._asset_school_district_lists_locator)

    @property
    def select_asset_type_grade_lists(self):
        return self.driver.find_elements_by_xpath(self._asset_school_grade_lists_locator)

    @property
    def get_overview_editname_text_box(self):
        return self.driver.find_element_by_name("name")

    @property
    def get_overview_newdistrict_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_overview_district_text_box_locator)

    @property
    def get_overview_newgrade_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_overview_grade_text_box_locator)

    @property
    def get_overview_newtype_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_overview_type_text_box_locator)

    @property
    def get_overview_district_add_button(self):
        return self.driver.find_elements_by_xpath(self._asset_overview_add_button_locator)[0]

    @property
    def get_overview_grade_add_button(self):
        return self.driver.find_elements_by_xpath(self._asset_overview_add_button_locator)[1]

    @property
    def get_overview_type_add_button(self):
        return self.driver.find_elements_by_xpath(self._asset_overview_add_button_locator)[2]

    @property
    def get_overview_name_text(self):
        return self.driver.find_element_by_xpath(self._asset_overview_panel_name_text)

    @property
    def get_overview_address1_text(self):
        return self.driver.find_element_by_xpath(self._asset_overview_panel_address_text).text

    @property
    def get_overview_district_text(self):
        return self.driver.find_element_by_xpath(self._asset_overview_panel_district_text).text

    @property
    def get_overview_grade_text(self):
        return self.driver.find_element_by_xpath(self._asset_overview_panel_grade_text).text

    @property
    def get_asset_overview_cancel_button(self):
        return self.driver.find_element_by_xpath(self._asset_overview_cancel_button_locator)

    @property
    def get_asset_overview_save_button(self):
        return self.driver.find_element_by_xpath(self._asset_overview_save_button_locator)

    @property
    def get_asset_points_of_contact_header(self):
        return self.driver.find_element_by_xpath(self._asset_points_of_contact_header_locator)

    @property
    def get_asset_add_contact_button(self):
        return self.driver.find_element_by_id(self._asset_add_contact_button_locator)

    @property
    def get_asset_newcontact_firstname_textbox(self):
        return self.driver.find_element_by_name(self._asset_newcontact_firstname_textbox_locator)

    @property
    def get_asset_newcontact_lastname_textbox(self):
        return self.driver.find_element_by_name(self._asset_newcontact_lastname_textbox_locator)

    @property
    def get_asset_newcontact_prefix_textbox(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_prefix_textbox_locator)

    @property
    def get_asset_newcontact_title_textbox(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_title_textbox_locator)

    @property
    def get_asset_newcontact_phone_textbox(self):
        return self.driver.find_element_by_name(self._asset_newcontact_phone_textbox_locator)

    @property
    def get_asset_newcontact_email_textbox(self):
        return self.driver.find_element_by_name(self._asset_newcontact_email_textbox_locator)

    @property
    def get_asset_newcontact_address1_textbox(self):
        return self.driver.find_element_by_name(self._asset_newcontact_address1_textbox_locator)

    @property
    def get_asset_newcontact_address2_textbox(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_address2_textbox_locator)

    @property
    def get_asset_newcontact_city_textbox(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_city_textbox_locator)

    @property
    def get_asset_newcontact_state_textbox(self):
        return self.driver.find_element_by_name(self._asset_newcontact_state_textbox_locator)

    @property
    def get_asset_newcontact_zip_textbox(self):
        return self.driver.find_element_by_name(self._asset_newcontact_zip_textbox_locator)

    @property
    def get_asset_newcontact_save_button(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_save_button_locator)

    @property
    def get_asset_newcontact_cancel_button(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_cancel_button_locator)

    @property
    def get_asset_newcontact_delete_icon(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_delete_contact_icon_locator)

    @property
    def get_asset_newcontact_delete_popup_delete_button(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_delete_contact_popup_delete_button_locator)

    @property
    def get_asset_newcontact_delete_popup_cancel_button(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_delete_contact_popup_cancel_button_locator)

    @property
    def get_asset_newcontact_window_cross_button(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_window_popup_cross_button_locator)

    @property
    def get_asset_newcontact_firstname_error_message(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_firstname_error_message_locator)

    @property
    def get_asset_newcontact_lastname_error_message(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_lastname_error_message_locator)

    @property
    def get_asset_newcontact_state_error_message(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_state_error_message_locator)

    @property
    def get_asset_newcontact_zip_error_message(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_zip_error_message_locator)

    @property
    def get_asset_newcontact_email_error_message(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_email_error_message_locator)

    @property
    def get_asset_contact_first_last_name_value_text(self):
        return self.driver.find_element_by_xpath(self._asset_contact_first_last_name_value_text)

    @property
    def get_asset_contact_title_value_text(self):
        return self.driver.find_element_by_xpath(self._asset_contact_title_value_text_locator)

    @property
    def get_asset_contact_phone_value_text(self):
        return self.driver.find_element_by_xpath(self._asset_contact_phone_value_text_locator)

    @property
    def get_asset_contact_email_value_text(self):
        return self.driver.find_element_by_xpath(self._asset_contact_email_value_text_locator)

    @property
    def get_asset_contact_new_contact_value_text(self):
        return self.driver.find_element_by_xpath(self._asset_contact_new_contact_text_locator)

    @property
    def get_asset_main_contact_window(self):
        return self.driver.find_element_by_xpath(self._asset_main_contact_window_locator)

    @property
    def get_asset_main_contact_name_text(self):
        return self.driver.find_element_by_xpath(self._asset_main_contact_name_locator)

    @property
    def get_asset_point_of_contact_name_tab(self):
        return self.driver.find_element_by_xpath(self._asset_point_of_contact_name_tab_locator)

    @property
    def get_asset_point_of_contact_title_tab(self):
        return self.driver.find_element_by_xpath(self._asset_point_of_contact_title_tab_locator)

    @property
    def get_asset_point_of_contact_phone_tab(self):
        return self.driver.find_element_by_xpath(self._asset_point_of_contact_phone_tab_locator)

    @property
    def get_asset_point_of_contact_email_tab(self):
        return self.driver.find_element_by_xpath(self._asset_point_of_contact_email_tab_locator)

    @property
    def get_asset_point_of_contact_name_text_value(self):
        return self.driver.find_elements_by_xpath(self._asset_point_of_contact_name_text_value_locator)

    @property
    def get_asset_point_of_contact_title_text_value(self):
        return self.driver.find_elements_by_xpath(self._asset_point_of_contact_title_text_value_locator)

    @property
    def get_asset_point_of_contact_phone_text_value(self):
        return self.driver.find_elements_by_xpath(self._asset_point_of_contact_phone_text_value_locator)

    @property
    def get_asset_point_of_contact_email_text_value(self):
        return self.driver.find_elements_by_xpath(self._asset_point_of_contact_email_text_value_locator)

    # Asset Details related properties
    @property
    def get_asset_detail_edit_link(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_link_locator)

    @property
    def get_asset_detail_edit_capacity_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_capacity_textbox_locator)

    @property
    def get_asset_detail_edit_closed_text_box(self):
        return self.driver.find_elements_by_xpath(self._asset_detail_edit_closed_textbox_locator)[0]

    @property
    def get_asset_detail_edit_detail_opened_number_text_box(self):
        return self.driver.find_elements_by_xpath(self._asset_detail_edit_closed_textbox_locator)[1]

    @property
    def get_asset_detail_edit_description_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_description_textbox_locator)

    @property
    def get_asset_detail_edit_detail_district_number_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_detail_district_number_textbox_locator)

    @property
    def get_asset_detail_edit_detail_fax_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_fax_textbox_locator)

    @property
    def get_asset_detail_edit_detail_school_number_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_school_number_textbox_locator)

    @property
    def get_asset_detail_edit_detail_size_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_size_textbox_locator)

    @property
    def get_asset_detail_edit_detail_website_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_website_textbox_locator)

    @property
    def get_asset_detail_edit_email_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_email_textbox_locator)

    @property
    def get_asset_detail_email_value_text(self):
        return self.driver.find_element_by_xpath(self._asset_detail_email_value_text_locator)

    @property
    def get_asset_detail_edit_save_button(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_save_button_locator)

    @property
    def get_asset_detail_edit_cancel_button(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_cancel_button_locator)

    @property
    def get_asset_detail_edit_window_cross_button(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_window_popup_cross_button_locator)

    # Asset overview related properties
    @property
    def get_asset_overview_edit_link(self):
        return self.driver.find_element_by_xpath(self._asset_overview_edit_link_locator)

    @property
    def get_asset_overview_edit_name_text_box(self):
        return self.driver.find_element_by_name(self._asset_overview_edit_name_textbox_locator)

    @property
    def get_asset_overview_window_cross_button(self):
        return self.driver.find_element_by_xpath(self._asset_overview_window_popup_cross_button_locator)

    @property
    def click_on_asset_link(self):
        return self.driver.find_element_by_link_text(self._asset_link_locator)

    @property
    def get_asset_header_save_text(self):
        return self.driver.find_element_by_xpath(self._asset_header_save_text_locator)

    @property
    def select_asset_search_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_search_textbox_locator)

    @property
    def get_asset_photos_documents_header_text(self):
        return self.driver.find_elements_by_xpath(self._asset_photos_documents_header_locator)

    @property
    def get_asset_photos_documents_upload_file_button(self):
        return self.driver.find_element_by_xpath(self._asset_photos_documents_upload_file_button_locator)

    @property
    def get_asset_photos_documents_attached_file_button(self):
        return self.driver.find_element_by_id(self._asset_photos_documents_attached_file_button_locator)

    @property
    def get_asset_photos_documents_caption_textbox(self):
        return self.driver.find_element_by_id(self._asset_photos_documents_caption_textbox_locator)

    @property
    def get_asset_photos_documents_window_upload_button(self):
        return self.driver.find_element_by_xpath(self._asset_photos_documents_window_upload_button_locator)

    @property
    def get_asset_photos_documents_window_cancel_button(self):
        return self.driver.find_element_by_xpath(self._asset_photos_documents_window_cancel_button_locator)

    @property
    def get_asset_annotation_plus_image(self):
        return self.driver.find_element_by_xpath(self._asset_annotation_plus_image_locator)

    @property
    def get_asset_annotation_edit_window_text_area(self):
        return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_text_area_locator)

    @property
    def get_asset_annotation_edit_window_visibility_dropdown(self):
        return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_visibility_dropdown_locator)

    @property
    def get_asset_annotation_edit_window_dropdown_groups(self):
        return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_dropdown_groups_locator)

    @property
    def get_asset_annotation_edit_window_dropdown_tenant(self):
        return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_dropdown_tenant_locator)

    @property
    def get_asset_annotation_edit_window_dropdown_user(self):
        return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_dropdown_user_locator)

    @property
    def get_asset_annotation_edit_window_save_button(self):
        return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_save_button_locator)

    @property
    def get_asset_annotation_edit_window_cancel_button(self):
        return self.driver.find_element_by_xpath(self._asset_annotation_edit_window_cancel_button_locator)

    @property
    def get_asset_annotation_text_value(self):
        return self.driver.find_element_by_xpath(self._asset_annotation_text_value_locator)

    @property
    def get_asset_annotation_delete_image(self):
        return self.driver.find_element_by_xpath(self._asset_annotation_delete_image_locator)

    @property
    def get_asset_annotation_edit_image(self):
        return self.driver.find_element_by_xpath(self._asset_annotation_edit_image_locator)

    # Location related properties
    @property
    def get_asset_location_map(self):
        return self.driver.find_element_by_id(self._asset_location_map_id_locator)

    @property
    def get_asset_location_edit_icon(self):
        return self.driver.find_element_by_css_selector(self._asset_location_edit_icon_css_locator)

    @property
    def get_asset_location_title(self):
        return self.driver.find_elements_by_xpath(self._asset_location_title_id_locator)

    @property
    def get_asset_location_latitude_textbox(self):
        return self.driver.find_element_by_name(self._asset_location_latitude_name_locator)

    @property
    def get_asset_location_latitude_error_text(self):
        return self.driver.find_element_by_css_selector(self._asset_location_latitude_error_css_locator)

    @property
    def get_asset_location_save_button(self):
        return self.driver.find_element_by_xpath(self._asset_location_save_xpath_locator)

    @property
    def get_asset_location_longitude_textbox(self):
        return self.driver.find_element_by_name(self._asset_location_longitude_name_locator)

    @property
    def get_asset_location_longitude_error_text(self):
        return self.driver.find_element_by_xpath_selector(self._asset_location_longitude_error_xpath_locator)

    @property
    def get_asset_chart_dashboard_image(self):
        return self.driver.find_element_by_xpath(self._asset_chart_dashboard_img_xpath_locator)

    def get_asset_photos_documents_image_caption_text(self, caption_val):
        caption_xpath = "//div[contains(text(),'Photos / Documents')]//following-sibling::div//ul//li[contains(text(),'"+caption_val+"')]"
        return self.driver.find_element_by_xpath(caption_xpath)

    def get_asset_photos_documents_header_caption_text(self, caption_val):
        caption_xpath = "//div[contains(text(),'Photos / Documents')]//following-sibling::div//a[contains(text(),'"+caption_val+"')]"
        return self.driver.find_element_by_xpath(caption_xpath)

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
        self.driver.find_element_by_xpath(self._asset_filter_drop_down_locator).click()
        self.driver.find_element_by_link_text(assetType).click()

    def get_asset_school_district(self):
        """
        Description : This function will click on school district drop down menu and will select a value.
        Revision:
        :return: None
        """
        sleep(5)
        self.asset_filter_based_on_place_and_school("School")
        self.driver.find_element_by_xpath(self._asset_school_district_drop_down_locator).click()
        chkDistrictDropDownValuesExists = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div[2]/div/ul")
        items = chkDistrictDropDownValuesExists.find_elements_by_tag_name("li")
        sleep(10)
        if len(items) > 1:
            firstelemet =self.driver.find_element_by_xpath\
                (self._asset_school_district_drop_down_select_first_element_locator)
            self.selecteddistrict = firstelemet.text
            firstelemet.click()
        else:
            print "No items to select in District drop down."
        sleep(2)

    def get_asset_school_grade(self):
        """
        Description : This function will click on school grade drop down menu and will select a value.
        Revision:
        :return: None
        """
        sleep(5)
        self.asset_filter_based_on_place_and_school("School")
        sleep(10)
        self.driver.find_element_by_xpath(self._asset_school_grade_drop_down_locator).click()
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
        sleep(5)
        self.asset_filter_based_on_place_and_school("School")
        sleep(10)
        self.driver.find_element_by_xpath(self._asset_school_type_drop_down_locator).click()
        sleep(2)
        chkSchoolTypeDropDownValuesExists = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div[4]/div/ul")
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
        sleep(4)
        search_textbox = self.driver.find_element_by_xpath(self._asset_search_textbox_locator)
        self.textbox_clear(search_textbox)
        search_textbox.send_keys(name)

    def asset_search_special_characters(self):
        """
        Description : This function will enter special characters in search text box.
        Revision:
        :return: None
        """
        sleep(5)
        searchNames = self.driver.find_elements_by_xpath(self._asset_list_locator)
        print len(searchNames)
        sleep(5)
        if len(searchNames) > 0:
            for searchname in searchNames:
                print searchname.text
        else:
            print "No records found."

    def return_to_apps_main_page(self):
        """
        Description : This function will helps to go back to assets page.
        Revision:
        :return: None
        """
        try:
            sleep(2)
            self.click_on_asset_link.click()
            WebDriverWait(self.driver,30).until(expected_conditions.presence_of_element_located((By.XPATH, self._asset_create_asset)))
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
            # self.driver.find_element_by_xpath(self._asset_create_asset).is_displayed()
            self.wait_for_element(self._asset_create_asset)
        except:
            inspectstack = inspect.stack()[1][3]
            self.recoverapp(inspectstack)

    def asset_create_click(self):
        """
        Description : This function will click on Create Asset Link.
        Revision:
        :return: None
        """
        self.app_sanity_check()
        sleep(5)
        self.driver.find_element_by_xpath(self._asset_create_asset).click()
        sleep(10)
        self.driver.switch_to.active_element


    def select_asset_template_type(self, template):
        # Select Place from the dropdown to create new place asset
        self.get_overview_templatetype_drop_down.click()
        self.driver.find_element_by_link_text(template).click()
        sleep(4)
    '''
    def select_school_asset_template_type(self):
        # Select Place from the dropdown to create new place asset
        self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[1]/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()
        sleep(4)
    '''
    def get_placedata(self):

        with open(placeData) as data_file:
            place_data = json.load(data_file)

            for each in place_data:
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
        sleep(10)
        self.select_asset_template_type("Place")
        sleep(10)
        self.enter_asset_type_name.send_keys(self.asset_place_name)
        sleep(2)
        self.enter_asset_type_address.send_keys(self.asset_place_address)
        sleep(2)
        self.enter_asset_type_address2.send_keys(self.asset_place_address2)
        sleep(2)
        self.enter_asset_type_city.send_keys(self.asset_place_city)
        sleep(2)
        self.enter_asset_type_state.send_keys(self.asset_place_state)
        sleep(2)
        self.enter_asset_type_zip.send_keys(self.asset_place_zip)
        sleep(2)
        self.enter_asset_type_owner.send_keys(self.asset_place_owner)
        sleep(2)
        self.enter_asset_type(self.asset_place_type)


    def get_schooldata(self):
        """
        Description : This function will read school data from json file.
        Revision:
        :return: None
        """
        with open(L1) as data_file:
            school_data = json.load(data_file)
            for each in school_data:
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


    def create_school_asset(self, index):
        """
        Description : This function will enter school data in asset template.
        Revision:
        :return: None
        """
        sleep(4)
        if(index == 0):
            self.enter_asset_type_name.send_keys(self.asset_school_name[index])
        else:
            self.get_overview_editname_text_box.clear()
            self.get_overview_editname_text_box.send_keys(self.asset_school_name[index])

        self.enter_asset_type_address.clear()
        self.enter_asset_type_address.send_keys(self.asset_school_address[index])
        sleep(2)
        self.enter_asset_type_address2.clear()
        self.enter_asset_type_address2.send_keys(self.asset_school_address2[index])
        sleep(2)
        self.enter_asset_type_city.clear()
        self.enter_asset_type_city.send_keys(self.asset_school_city[index])
        sleep(2)
        self.enter_asset_type_state.clear
        self.enter_asset_type_state.send_keys(self.asset_school_state[index])
        sleep(2)
        self.enter_asset_type_zip.clear()
        self.enter_asset_type_zip.send_keys(self.asset_school_zip[index])
        sleep(2)
        self.enter_asset_type_owner.clear()
        self.enter_asset_type_owner.send_keys(self.asset_school_owner[index])
        sleep(2)
        self.enter_school_district(self.asset_school_district[index])
        sleep(2)
        self.enter_school_grade(self.asset_school_grade[index])
        sleep(2)
        self.enter_asset_type(self.asset_school_type[index])


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
        self.get_overview_type_drop_down.click()
        sleep(2)
        self.get_overview_type_drop_down.send_keys(Keys.TAB, value, Keys.TAB, Keys.ENTER)

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
            self.create_school_asset(self.newSchool)
        elif type == "Place":
            self.create_place_asset()

        self.asset_overview_save_click()

    def edit_asset(self, type):
        """
        Description : This function will edit asset Place/School.
        Revision:
        :return: None
        """
        self.select_school_or_place_asset(self.asset_school_name[0], type)
        if type == "School":
            sleep(10)
            self.get_asset_overview_edit_link.click()
            self.create_school_asset(self.editSchool)
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
            self.create_school_asset(self.newSchool)
        elif type == "Place":
            self.create_place_asset()
        self.asset_overview_cancel_click()

    def select_school_or_place_asset(self, asset_name1,asset_type):
        """
        Description : This function will select an asset from asset list.
        Revision:
        :return: None
        """
        sleep(5)
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
        except:
            print "No Asset is existing or Asset Creation has been failed."


    def set_place_overview_fields(self,paddress, paddress1, pcity, pstate, pzip, powner):
        """
        Description : This function will enter data in all fields of Overview Edit Window.
        Revision:
        :return: None
        """
        sleep(5)
        self.enter_asset_type_address.clear()
        self.enter_asset_type_address.send_keys(paddress)
        self.enter_asset_type_address.send_keys(Keys.TAB)
        sleep(5)
        self.enter_asset_type_address2.clear()
        self.enter_asset_type_address2.send_keys(paddress1)
        self.enter_asset_type_address2.send_keys(Keys.TAB)
        sleep(5)
        self.enter_asset_type_city.clear()
        self.enter_asset_type_city.send_keys(pcity)
        self.enter_asset_type_city.send_keys(Keys.TAB)
        sleep(5)
        self.enter_asset_type_state.clear()
        self.enter_asset_type_state.send_keys(pstate)
        self.enter_asset_type_state.send_keys(Keys.TAB)
        sleep(5)
        self.enter_asset_type_zip.clear()
        self.enter_asset_type_zip.send_keys(pzip)
        self.enter_asset_type_zip.send_keys(Keys.TAB)
        sleep(5)
        self.enter_asset_type_phone.send_keys(Keys.TAB)
        sleep(5)
        self.enter_asset_type_owner.clear()
        self.enter_asset_type_owner.send_keys(powner)
        self.enter_asset_type_owner.send_keys(Keys.TAB)
        sleep(5)


    def set_place_details_fields(self, pcapacity, pclosed, pdescription, pdistrict, pemail, pfax, popened,
                                 pschoolnumber, psize, pwebsite):
        """
        Description : This function will enter data in all fields of Detail Edit Window.
        Revision:
        :return: None
        """
        self.get_asset_detail_edit_capacity_text_box.clear()
        self.get_asset_detail_edit_capacity_text_box.send_keys(pcapacity)
        self.get_asset_detail_edit_capacity_text_box.send_keys(Keys.TAB)

        sleep(2)

        self.get_asset_detail_edit_closed_text_box.clear()
        self.get_asset_detail_edit_closed_text_box.send_keys(pclosed)
        self.get_asset_detail_edit_closed_text_box.send_keys(Keys.TAB)

        sleep(2)

        self.get_asset_detail_edit_description_text_box.clear()
        self.get_asset_detail_edit_description_text_box.send_keys(pdescription)
        self.get_asset_detail_edit_description_text_box.send_keys(Keys.TAB)
        sleep(2)
        if pdistrict is not None:
            self.get_asset_detail_edit_detail_district_number_text_box.send_keys("")
            self.get_asset_detail_edit_detail_district_number_text_box.send_keys(pdistrict)
            self.get_asset_detail_edit_detail_district_number_text_box.send_keys(Keys.TAB)
            sleep(2)
        self.get_asset_detail_edit_email_text_box.clear()
        self.get_asset_detail_edit_email_text_box.send_keys(pemail)
        self.get_asset_detail_edit_email_text_box.send_keys(Keys.TAB)
        sleep(2)
        self.get_asset_detail_edit_detail_fax_text_box.clear()
        self.get_asset_detail_edit_detail_fax_text_box.send_keys(pfax)
        self.get_asset_detail_edit_detail_fax_text_box.send_keys(Keys.TAB)
        sleep(2)
        self.get_asset_detail_edit_detail_opened_number_text_box.clear()
        self.get_asset_detail_edit_detail_opened_number_text_box.send_keys(popened)
        self.get_asset_detail_edit_detail_opened_number_text_box.send_keys(Keys.TAB)
        sleep(2)
        if pschoolnumber is not None:
            self.get_asset_detail_edit_detail_school_number_text_box.send_keys("")
            self.get_asset_detail_edit_detail_school_number_text_box.send_keys(pschoolnumber)
            self.get_asset_detail_edit_detail_school_number_text_box.send_keys(Keys.TAB)
            sleep(2)
        self.get_asset_detail_edit_detail_size_text_box.clear()
        self.get_asset_detail_edit_detail_size_text_box.send_keys(psize)
        self.get_asset_detail_edit_detail_size_text_box.send_keys(Keys.TAB)
        sleep(2)
        self.get_asset_detail_edit_detail_website_text_box.clear()
        self.get_asset_detail_edit_detail_website_text_box.send_keys(pwebsite)
        self.get_asset_detail_edit_detail_website_text_box.send_keys(Keys.TAB)
        sleep(2)


    def delete_existing_contact(self):
        """
        Description : This function will delete existing contact.
        Revision:
        :return: None
        """
        try:
            while( self.get_asset_newcontact_delete_icon.is_displayed()):
                sleep(2)
                self.get_asset_newcontact_delete_icon.click()
                sleep(1)
                self.get_asset_newcontact_delete_popup_delete_button.click()
        except NoSuchElementException, ElementNotVisibleException:
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
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element((By.XPATH,
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
        WebDriverWait(self.driver,100).until(expected_conditions.text_to_be_present_in_element((By.XPATH,
                                                                        self._asset_header_save_text_locator), "Saved"))

    def multiple_contact_create(self):
        """
        Description : This function will create multiple contacts.
        Revision:
        :return: None
        """
        try:
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
            sleep(2)
        except:
            print "multiple file creation has been failed"

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
        try:
            self.driver.find_element_by_xpath("(//div[contains(text(),'Photos / Documents')])[1]").click()
            sleep(2)
            image_icons = self.driver.find_elements_by_xpath(".//img[@class='neutron_document_img']")
            num_of_files = len(image_icons)
            if num_of_files >= 1:
                sleep(2)
                for count in range(num_of_files, 0, -1):
                    index = count
                    xpath = r"(.//img[contains(@src,'delete_icon')])"+"["+str(index)+"]"
                    image_icon_xpath =  self.driver.find_element_by_xpath\
                        (".//*[@id='widgets']/div[6]/div[1]/div/div[2]/div/div[" + str(index)+ "]")
                    Hover = ActionChains(self.driver).move_to_element(image_icon_xpath)
                    Hover.perform()
                    delete_icon = self.driver.find_element_by_xpath(xpath)
                    delete_icon.click()
                    self.driver.find_element_by_xpath\
                        ("//div[@id='delete_document_modal']//button[contains(text(),'Delete')]").click()
                    sleep(10)
        except :
            print "File deletion not done properly or some files could not be deleted."


    def upload_a_file_with_caption(self, image_caption, image_file_name):
        """
        Description : This function will upload a file with caption.
        Revision:
        :return:
        """
        try:
            # Click on Photo/Document panel - File Upload button
            self.get_asset_photos_documents_upload_file_button.click()
            sleep(2)

            # Click on Attach file button and attached the file path with the send_keys
            file_path = self.file_path(image_file_name)
            self.get_asset_photos_documents_attached_file_button.send_keys(file_path)
            sleep(3)
            # Enter Caption
            caption_val = image_caption
            self.get_asset_photos_documents_caption_textbox.send_keys(caption_val)
            sleep(2)
            # Click Upload.
            self.get_asset_photos_documents_window_upload_button.click()
            try:
                WebDriverWait(self.driver,200).until(expected_conditions.text_to_be_present_in_element((By.XPATH, self._asset_header_save_text_locator), "Saved"))
            except:
                pass
        except:
            print "File uploads failed."


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
        except:
            print "Annotation text coulld not deleted or no annotation text is available."

    def charts_When_No_Asset_Type_Is_Selected(self):
        # Display available chart names in the container
        totalGraphInContainer = self.driver.find_elements_by_xpath(".//*[@id='graphs_frame']/div/div/div/div[1]")
        sleep(10)
        print len(totalGraphInContainer)
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."
                if totalGraph.text == "Asset Type":
                    assets = self.driver.find_elements_by_xpath(chart_xpath)
                    for asset in assets:
                        print asset.text
                        sleep(10)
        else :

            print "No chart found at place level."


    def place_related_charts_Place_Is_Selected(self):
        """
        Description : This function will display available chart names in the container when place is selected.
        Revision:
        :return:
        """
        chart_xpath = r"//div[starts-with(@id,'asset_graph-0')]"+self.svg_path_1+self.svg_path_2
        totalGraphInContainer = self.driver.find_elements_by_xpath(".//*[@id='graphs_frame']/div/div/div/div[1]")
        sleep(10)
        print len(totalGraphInContainer)
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."
                if totalGraph.text == "Type":
                    assets = self.driver.find_elements_by_xpath(chart_xpath)
                    for asset in assets:
                        print asset.text
                        sleep(10)
        else :
            print "No chart found at place level."


    def place_related_charts_Place_And_Type_Is_Selected(self):
        """
        Description: This function will display available chart names in the container when place and type are selected.
        Revision:
        :return:
        """
        chart_xpath = self.svg_path_1+self.svg_path_2+r"/*[name()='tspan']"
        totalGraphInContainer = self.driver.find_elements_by_xpath(".//*[@id='graphs_frame']/div/div/div/div[1]")
        sleep(10)
        print len(totalGraphInContainer)
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text

                print "Printing according to the chart wise data..."
                assets = totalGraph.find_elements_by_xpath(chart_xpath)
                for asset in assets:
                    print asset.text
                    sleep(10)

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
        totalGraphInContainer = self.driver.find_elements_by_xpath(".//*[@id='graphs_frame']/div/div/div/div[1]")
        sleep(10)
        print len(totalGraphInContainer)
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."
                if totalGraph.text == "District":
                    assets = self.driver.find_elements_by_xpath(chart_xpath_1)
                    for asset in assets:
                        print asset.text
                        sleep(10)
                elif totalGraph.text == "Grade Level":
                    assets = self.driver.find_elements_by_xpath(chart_xpath_2)
                    for asset in assets:
                        print asset.text
                        sleep(10)
                elif totalGraph.text == "School Type":
                    assets = self.driver.find_elements_by_xpath(chart_xpath_3)
                    for asset in assets:
                        print asset.text
                        sleep(10)
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
        totalGraphInContainer = self.driver.find_elements_by_xpath(".//*[@id='graphs_frame']/div/div/div/div[1]")
        sleep(10)
        print len(totalGraphInContainer)
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."

                if totalGraph.text == "Grade Level":
                    assets = self.driver.find_elements_by_xpath(chart_xpath_1)
                    for asset in assets:
                        print asset.text
                        sleep(10)
                elif totalGraph.text == "School Type":
                    assets = self.driver.find_elements_by_xpath(chart_xpath_2)
                    for asset in assets:
                        print asset.text
                        sleep(10)
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
        totalGraphInContainer = self.driver.find_elements_by_xpath(".//*[@id='graphs_frame']/div/div/div/div[1]")
        sleep(10)
        print len(totalGraphInContainer)
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."
                #assets = self.driver.find_elements_by_xpath("//*[name()='svg' and namespace-uri()='http://www.w3.org/2000/svg']/*[name()='text']/*[name()='tspan']")

                if totalGraph.text == "District":
                    assets = self.driver.find_elements_by_xpath("//div[starts-with(@id,'asset_graph-0')]//*[name()='svg' and namespace-uri()='http://www.w3.org/2000/svg']/*[name()='text']")
                    for asset in assets:
                        print asset.text
                        sleep(10)
                elif totalGraph.text == "School Type":
                    assets = self.driver.find_elements_by_xpath(chart_xpath_2)
                    for asset in assets:
                        print asset.text
                        sleep(10)
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
        totalGraphInContainer = self.driver.find_elements_by_xpath(".//*[@id='graphs_frame']/div/div/div/div[1]")
        sleep(10)
        print len(totalGraphInContainer)
        if len(totalGraphInContainer) >= 1:
            print "Printing chart names..."
            for totalGraph in totalGraphInContainer:
                print totalGraph.text
                print "Printing according to the chart wise data..."

                if totalGraph.text == "District":
                    assets = self.driver.find_elements_by_xpath(chart_xpath_1)
                    for asset in assets:
                        print asset.text
                        sleep(10)
                elif totalGraph.text == "Grade Level":
                    assets = self.driver.find_elements_by_xpath(chart_xpath_2)
                    for asset in assets:
                        print asset.text
                        sleep(10)
        else :
            print "No chart found at school and type level."

    def wait_for_element_path(self, locator):
        limit = 10   # waiting limit in seconds
        inc = 1   # in seconds; sleep for 500ms
        c = 0
        while (c < limit):
            try:
                return self.driver.find_element_by_xpath(locator)  # Success
            except:
                sleep(inc)
                c = c + inc
        raise Exception # Failure

    def wait_for_list_element_path(self, locator):
        limit = 20   # waiting limit in seconds
        inc = 1   # in seconds; sleep for 500ms
        c = 0
        while (c < limit):
            try:
                return self.driver.find_elements_by_xpath(locator)  # Success
            except:
                sleep(inc)
                c = c + inc
        raise Exception # Failure

    def wait_for_element(self, locator):
        limit = 10   # waiting limit in seconds
        inc = 1   # in seconds; sleep for 500ms
        c = 0
        while (c < limit):
            try:
                self.driver.find_element_by_xpath(locator)  # Success
                return True
            except:
                sleep(inc)
                c = c + inc
        return False# Failure

    def _validate_page(self, driver):
        pass
