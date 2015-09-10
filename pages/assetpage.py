from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from basepage import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os, json

cwd = os.getcwd()
os.chdir('..')
L1 = os.path.join(os.getcwd(), "data\json_Schooldata.json")
placeData = os.path.join(os.getcwd(), "data\json_place_asset.json")
os.chdir(cwd)

class AssetPage(BasePageClass):

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

    # Asset Filter related to place and school
    _asset_filter_drop_down_locator = "//*[@id='span_filters']/div/div/button[2]"

    _asset_place_type_drop_down_locator = "//div[@label='Type']"
    #_asset_school_district_drop_down_locator = "//div[@label= 'District']"
    #_asset_school_district_drop_down_select_first_element_locator = ".//*[@id='span_filters']/div[2]/div/ul/li[1]/a"
    #_asset_school_district_drop_down_locator = "//div[@label= 'District']"
    _asset_school_district_drop_down_locator = ".//*[@id='span_filters']/div[2]/div/button[2]"
    _asset_school_district_drop_down_select_first_element_locator = ".//*[@id='span_filters']/div[2]/div/ul/li[1]/a"

    _asset_school_grade_drop_down_locator = ".//*[@id='span_filters']/div[3]/div/button[2]"
    _asset_school_grade_drop_down_select_first_element_locator = ".//*[@id='span_filters']/div[3]/div/ul/li[1]/a"

    _asset_school_type_drop_down_locator = ".//*[@id='span_filters']/div[4]/div/button[2]"
    _asset_school_type_drop_down_select_first_element_locator = ".//*[@id='span_filters']/div[4]/div/ul/li[1]/a"

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

    # Overview panel related


    #Asset Overview dialouge locators
    #_asset_overview_templatetype_dropdown_locator = "//*[@id='asset_overview_modal']/div/div/form/div[1]/div/div/button[2]"
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
    #_asset_overview_type_drop_down_locator = ".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/button[1]"
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
    _asset_point_of_contact_name_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Name']"
    _asset_point_of_contact_title_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Title']"
    _asset_point_of_contact_phone_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Phone']"
    _asset_point_of_contact_email_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Email']"
    _asset_point_of_contact_name_text_value_locator = "//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit']"
    _asset_point_of_contact_title_text_value_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])/../following-sibling::td[1]"
    _asset_point_of_contact_phone_text_value_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])/../following-sibling::td[2]"
    _asset_point_of_contact_email_text_value_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])/../following-sibling::td[3]"

    #_asset_detail_edit_link_locator = ".//div[contains(text(),'Details')]/div/img"
    #_asset_detail_edit_email_textbox_locator = "//input[@placeholder='Email']"
    #_asset_detail_email_value_text_locator = ".//span[text()='Email']/../following-sibling::td"
    #_asset_detail_edit_save_button_locator = ".//*[@id='asset_details_modal']/div/div/form/div[2]/button[2]"
    #_asset_detail_edit_window_popup_cross_button_locator = ".//*[@id='asset_details_modal']/div/div/div/button"


    _asset_link_locator = "Assets"
    _asset_header_save_text_locator = ".//*[@id='header']/div[contains(@class,'right ng-binding')]"

    # Asset Detail panel related

    _asset_detail_edit_link_locator = ".//*[@id='widgets']/div[5]/div/div[1]/div/img"
    _asset_detail_edit_capacity_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[1]/div/span/input"
    _asset_detail_edit_closed_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[2]/div/span/input"
    _asset_detail_edit_description_textbox_locator = ".//*[@id='asset_details_description_edit']"
    _asset_detail_edit_detail_district_number_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[4]/div/span/input"
    _asset_detail_edit_fax_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[5]/div/span/input"
    _asset_detail_edit_opened_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[6]/div/span/input"
    _asset_detail_edit_school_number_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[8]/div/span/input"
    _asset_detail_edit_size_textbox_locator = ".//*[@id='asset_details_modal']/div/div/form/div[1]/span[7]/div/span/input"
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


    _asset_count = 0
    _assets = {}


    def __init__(self, driver):
        super(AssetPage, self).__init__(driver)
        self.get_schooldata()
        self.get_placedata()
        appicon = IconListPage(self.driver)
        appicon.click_asset_icon()

        '''
        assets_results = self.driver.find_elements_by_xpath(self._asset_list_locator)
        for asset in assets_results:
            assetname = asset.find_elements_by_xpath(self._asset_list_asset_name_locator).text
            self._assets[assetname] = asset.find_element_by_xpath(self._asset_list_check_box_locator)
            self._assets[assetname] = asset.find_element_by_xpath(self._asset_list_asset_type_locator)
        '''

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
    def get_asset_school_district_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_school_district_drop_down_locator)


    @property
    def get_asset_list_no_matching_records_found(self):
        return  self.driver.find_element_by_xpath(self._asset_list_No_Matching_Records_Found_locator)

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

    '''
    @property
    def select_asset_type_type(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_type_drop_down_locator)

    @property
    def select_asset_type_district(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_district_drop_down_locator)

    @property
    def select_asset_type_grade(self):
        return self.driver.find_element_by_xpath(self._asset_school_grade_drop_down_locator)
        return self.driver.find_element_by_xpath(self._asset_type_field_grade_drop_down_locator)'''

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
        return self.driver.find_element_by_xpath(self._asset_detail_edit_closed_textbox_locator)

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
    def get_asset_detail_edit_detail_opened_number_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_detail_edit_opened_textbox_locator)

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

    def get_asset_photos_documents_image_caption_text(self, caption_val):
        caption_xpath = "//div[contains(text(),'Photos / Documents')]//following-sibling::div//ul//li[contains(text(),'"+caption_val+"')]"
        return self.driver.find_element_by_xpath(caption_xpath)

    def get_asset_photos_documents_header_caption_text(self, caption_val):
        caption_xpath = "//div[contains(text(),'Photos / Documents')]//following-sibling::div//a[contains(text(),'"+caption_val+"')]"
        return self.driver.find_element_by_xpath(caption_xpath)

    def get_select_checkbox_in_grid(self):
        assets_checkbox = self.driver.find_elements_by_xpath(self._asset_list_check_box_locator)
        sleep(2)
        for asset_checkbox in assets_checkbox:
            sleep(1)
            asset_checkbox.click()

        for asset_checkbox in assets_checkbox:
            sleep(1)
            asset_checkbox.click()
    '''
    def display_asset_names_in_grid(self):
        assets_name = self.driver.find_elements_by_xpath(self._asset_list_asset_name_locator)
        sleep(2)
        for asset_name in assets_name:
    '''

    def asset_filter_based_on_place_and_school(self, assetType):

        self.driver.find_element_by_xpath(self._asset_filter_drop_down_locator).click()
        self.driver.find_element_by_link_text(assetType).click()

        assetsType = self.driver.find_elements_by_xpath(self._asset_list_locator)
        print "Found " + str(len(assetsType)) + " - " + assetType + " Asset Types"

    # This function is to select the school district
    def get_asset_school_district(self):
        sleep(5)
        self.driver.find_element_by_xpath(self._asset_filter_drop_down_locator).click()
        self.driver.find_element_by_link_text("School").click()

        # Click on District dropdown
        self.driver.find_element_by_xpath(self._asset_school_district_drop_down_locator).click()

        # Check the values exists inside District dropdown
        chkDistrictDropDownValuesExists = self.driver.find_elements_by_xpath(".//*[@id='span_filters']/div[2]/div/ul")
        sleep(5)

        try:

            # If value exists inside Grade dropdown
            if len(chkDistrictDropDownValuesExists) > 1:
                # Click on the First link inside District dropdown
                self.driver.find_element_by_xpath(self._asset_school_district_drop_down_select_first_element_locator).click()

                # Count the no of schools displayed in the list after filtering by Grade dropdown
                districtNames = self.driver.find_elements_by_xpath(self._asset_list_locator)

                # Print the School names based on District dropdown
                if len(districtNames) > 0:
                    for districtname in districtNames:
                        print districtname.text
                else:
                    print "No school records found."
            else:
                print "No value to select inside School District dropdown."
        except:
            self.driver.get_asset_reset_button.click()


    # This function is to select the school grade
    def get_asset_school_grade(self):
        sleep(5)
        self.driver.find_element_by_xpath(self._asset_filter_drop_down_locator).click()
        self.driver.find_element_by_link_text("School").click()
        sleep(10)

        # Click on Grade dropdown
        self.driver.find_element_by_xpath(self._asset_school_grade_drop_down_locator).click()
        sleep(5)

        # Check the values exists inside Grade dropdown
        chkGradeDropDownValuesExists = self.driver.find_elements_by_xpath(".//*[@id='span_filters']/div[3]/div/ul")
        sleep(5)
        try:

            # If value exists inside Grade dropdown
            if len(chkGradeDropDownValuesExists) > 1:
                # Click on the First link inside Grade dropdown
                self.driver.find_element_by_xpath(self._asset_school_grade_drop_down_select_first_element_locator).click()

                # Count the no of schools displayed in the list after filtering by Grade dropdown
                gradeNames = self.driver.find_elements_by_xpath(self._asset_list_locator)

                # Print the School names based on Grade dropdown
                if len(gradeNames) > 0:
                    for gradename in gradeNames:
                        print gradename.text
                else:
                    print "No school records found."
            else:
                print "No value to select inside School Grade dropdown."
        except:
            self.driver.get_asset_reset_button.click()




    # This function is to select the school type
    def get_asset_school_type(self):
        sleep(5)
        self.driver.find_element_by_xpath(self._asset_filter_drop_down_locator).click()
        self.driver.find_element_by_link_text("School").click()
        sleep(10)

        # Check the values exists inside School dropdown
        self.driver.find_element_by_xpath(self._asset_school_type_drop_down_locator).click()
        sleep(5)

        # Check the values exists inside School dropdown
        self.driver.find_element_by_xpath(self._asset_school_type_drop_down_select_first_element_locator).click()
        #schoolassetsType = self.driver.find_elements_by_xpath(self._asset_list_locator)

         # Check the values exists inside School dropdown
        chkSchoolDropDownValuesExists = self.driver.find_elements_by_xpath(".//*[@id='span_filters']/div[4]/div/ul")
        sleep(5)
        try:

            # If value exists inside Grade dropdown
            if len(chkSchoolDropDownValuesExists) > 1:
                # Click on the First link inside Grade dropdown
                self.driver.find_element_by_xpath(self._asset_school_type_drop_down_select_first_element_locator).click()

                # Count the no of schools displayed in the list after filtering by Grade dropdown
                typeNames = self.driver.find_elements_by_xpath(self._asset_list_locator)

                # Print the School names based on Grade dropdown
                if len(typeNames) > 0:
                    for typename in typeNames:
                        print typename.text
                else:
                    print "No school records found."
            else:
                print "No value to select inside School Type dropdown."
        except:
            self.driver.get_asset_reset_button.click()


    def textbox_clear(self, textboxlocator):
        textboxlocator.clear()

    def asset_search_assetname(self, name):
        sleep(4)
        search_textbox = self.driver.find_element_by_xpath(self._asset_search_textbox_locator)
        self.textbox_clear(search_textbox)
        search_textbox.send_keys(name)

    def asset_search_special_characters(self):
        sleep(5)
        searchNames = self.driver.find_elements_by_xpath(self._asset_list_locator)
        print len(searchNames)
        sleep(5)
        if len(searchNames) > 0:
            for searchname in searchNames:
                print searchname.text
        else:
            print "No records found."

    def asset_create_click(self):
        try:
            self.driver.find_element_by_xpath(self._asset_create_asset).is_displayed()
        except:
            print ("Application recovering")
            basepage = BasePage(self.driver)
            basepage.accessURL()
            iconlistpage = IconListPage(self.driver)
            iconlistpage.click_asset_Icon()

        # Click on Create asset
        sleep(5)
        self.driver.find_element_by_xpath(self._asset_create_asset).click()
        sleep(10)
        # switch to new window
        self.driver.switch_to.active_element
        # Verify title "Asset overview" window
        #self.driver.find_element_by_xpath("//div[@id='asset_overview_modal']/div/div/div/h4").text
        #sleep(2)
        #print("Asset overview", Create_Asset_Title)

    # This function is based on selecting the Template either by Place or School.
    # We need to pass the parameter from the Testcase
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
        # Select Place from the dropdown to create new place asset
        sleep(10)
        #self.get_placedata()
        self.select_asset_template_type("Place")
        sleep(10)
        self.enter_asset_type_name.send_keys(self.asset_place_name)
        self.enter_asset_type_name.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_address.send_keys(self.asset_place_address)
        self.enter_asset_type_address.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_address2.send_keys(self.asset_place_address2)
        self.enter_asset_type_address2.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_city.send_keys(self.asset_place_city)
        self.enter_asset_type_city.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_state.send_keys(self.asset_place_state)
        self.enter_asset_type_state.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_zip.send_keys(self.asset_place_zip)
        self.enter_asset_type_zip.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_owner.send_keys(self.asset_place_owner)
        self.enter_asset_type_owner.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type(self.asset_place_type)


    def get_schooldata(self):

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
        # Select School from the dropdown to create new School asset
        #self.get_schooldata()

        sleep(4)
        if(index == 0):
            self.enter_asset_type_name.send_keys(self.asset_school_name[index])
            self.enter_asset_type_name.send_keys(Keys.TAB)
        else:
            self.get_overview_editname_text_box.clear()
            self.get_overview_editname_text_box.send_keys(self.asset_school_name[index])
            self.get_overview_editname_text_box.send_keys(Keys.TAB)

        self.enter_asset_type_address.clear()
        self.enter_asset_type_address.send_keys(self.asset_school_address[index])
        self.enter_asset_type_address.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_address2.clear()
        self.enter_asset_type_address2.send_keys(self.asset_school_address2[index])
        self.enter_asset_type_address2.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_city.clear()
        self.enter_asset_type_city.send_keys(self.asset_school_city[index])
        self.enter_asset_type_city.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_state.clear
        self.enter_asset_type_state.send_keys(self.asset_school_state[index])
        self.enter_asset_type_state.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_zip.clear()
        self.enter_asset_type_zip.send_keys(self.asset_school_zip[index])
        self.enter_asset_type_zip.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_owner.clear()
        self.enter_asset_type_owner.send_keys(self.asset_school_owner[index])
        self.enter_asset_type_owner.send_keys(Keys.TAB)
        sleep(2)
        self.enter_school_district(self.asset_school_district[index])
        sleep(2)
        self.enter_school_grade(self.asset_school_grade[index])
        sleep(2)
        self.enter_asset_type(self.asset_school_type[index])


    def enter_school_district(self, value):
         self.get_overview_district_drop_down.click()
         self.get_overview_newdistrict_text_box.send_keys(value)
         self.get_overview_district_add_button.click()

    def enter_school_grade(self, value):
         self.get_overview_grade_drop_down.click()
         self.get_overview_newgrade_text_box.send_keys(value)
         self.get_overview_grade_add_button.click()

    def enter_asset_type(self, value):
         self.get_overview_type_drop_down.click()
         self.get_overview_type_drop_down.send_keys(Keys.TAB, value, Keys.TAB, Keys.ENTER)
        # self.get_overview_type_add_button.click()

    def asset_overview_save_click(self):
        self.get_asset_overview_save_button.click()
        sleep(2)

    def asset_overview_cancel_click(self):
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
        self.asset_create_click()
        if type == "School":
            self.select_asset_template_type("School")
            self.create_school_asset(self.newSchool)
        elif type == "Place":
            self.create_place_asset()
        self.asset_overview_save_click()

    def edit_asset(self, type):
        self.select_school_or_place_asset(self.asset_school_name[0], type)
        if type == "School":
            sleep(10)
            self.get_asset_overview_edit_link.click()
            self.create_school_asset(self.editSchool)
        elif type == "Place":
            self.create_place_asset()
        self.asset_overview_save_click()

    def create_asset_cancel(self, type):
        self.asset_create_click()
        if type == "School":
            self.select_asset_template_type("School")
            self.create_school_asset(self.newSchool)
        elif type == "Place":
            self.create_place_asset()
        self.asset_overview_cancel_click()

    def select_school_or_place_asset(self, asset_name1,asset_type):
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

    # Place Edit mode - Overview panel
    def set_place_overview_fields(self,paddress, paddress1, pcity, pstate, pzip, powner):
        '''
        sleep(5)
        self.get_asset_overview_edit_name_text_box.send_keys("")
        sleep(2)
        self.get_asset_overview_edit_name_text_box.send_keys(pname)
        '''
        #self.get_asset_overview_edit_name_text_box.send_keys(Keys.TAB)
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
        #self.select_asset_type_type.click()
        #sleep(2)

    def set_place_details_fields(self, pcapacity, pclosed, pdescription, pemail, pfax, popened, psize, pwebsite):
        # fill out the fields

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

        #self.get_asset_detail_edit_detail_district_number_text_box.send_keys("")
        #self.get_asset_detail_edit_detail_district_number_text_box.send_keys(pdistrict)
        #self.get_asset_detail_edit_detail_district_number_text_box.send_keys(Keys.TAB)

        #sleep(2)

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

        #self.get_asset_detail_edit_detail_school_number_text_box.send_keys("")
        #self.get_asset_detail_edit_detail_school_number_text_box.send_keys(pschoolnumber)
        #self.get_asset_detail_edit_detail_school_number_text_box.send_keys(Keys.TAB)

        #sleep(2)

        self.get_asset_detail_edit_detail_size_text_box.clear()
        self.get_asset_detail_edit_detail_size_text_box.send_keys(psize)
        self.get_asset_detail_edit_detail_size_text_box.send_keys(Keys.TAB)

        sleep(2)

        self.get_asset_detail_edit_detail_website_text_box.clear()
        self.get_asset_detail_edit_detail_website_text_box.send_keys(pwebsite)
        self.get_asset_detail_edit_detail_website_text_box.send_keys(Keys.TAB)

        sleep(2)


    def delete_existing_contact(self):
        try:
            while( self.get_asset_newcontact_delete_icon.is_displayed()):
                sleep(2)
                self.get_asset_newcontact_delete_icon.click()
                sleep(1)
                self.get_asset_newcontact_delete_popup_delete_button.click()
        except NoSuchElementException:
            pass

    def create_new_contact(self, firstname, lastname, title="Title", phone="111-111-1111", email="test@test.com", prefix="Shri", address1="Indecomm", address2="Brigade South Parade", city="Bangalore", state="KA", zip="56001"):
        self.get_asset_points_of_contact_header.click()
        self.get_asset_add_contact_button.click()
        sleep(4)
        self.get_asset_newcontact_firstname_textbox.clear()
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
        self.get_asset_newcontact_save_button.click()
        sleep(2)

    def multiple_contact_create(self):
        try:
            sleep(2)
            self.delete_existing_contact()
            sleep(2)
            firstname = ['jkl','vwx', 'def', 'pqr']
            lastname = ['mno', 'abc','stu', 'ghi']
            phonelist = ['661-111-1111','222-222-2222', '433-333-3333', '123-444-4444']
            emaillist = ['stu@vwx', 'abc@def', 'mno@pqr', 'ghi@jkl']
            titlelist = ['HH', 'ZZ', 'CC', 'PP']
            for contact in range(4):
                self.create_new_contact(firstname[contact],lastname[contact],titlelist[contact],phonelist[contact],emaillist[contact])
                sleep(2)
            sleep(2)
        except:
            print "multiple file creation has been failed"

    def file_path(self, image_file_name):
        cur_dir = os.getcwd()
        os.chdir("..")
        file_path = "image_file\\"+image_file_name
        complete_file_path = os.path.join(os.getcwd(),file_path)
        os.chdir(cur_dir)
        return complete_file_path

    def delete_uploaded_files(self):
        try:
            self.driver.find_element_by_xpath("(//div[contains(text(),'Photos / Documents')])[1]").click()
            sleep(2)
            image_icons = self.driver.find_elements_by_xpath(".//img[@class='neutron_document_img']")
            num_of_files = len(image_icons)
            if num_of_files>= 1:
                sleep(2)
                for count in range(num_of_files, 0, -1):
                    sleep(5)
                    index = count
                    xpath = r"(.//img[contains(@src,'delete_icon')])"+"["+str(index)+"]"
                    image_icons[count-1].click()
                    sleep(3)
                    delete_icon = self.driver.find_element_by_xpath(xpath)
                    delete_icon.click()
                    sleep(3)
                    self.driver.find_element_by_xpath("//div[@id='delete_document_modal']//button[contains(text(),'Delete')]").click()
                    sleep(10)
        except :
            print "File deletion not done properly"


    def upload_a_file_with_caption(self, image_caption, image_file_name):
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
            sleep(2)
        except:
            print "File uploads failed."

    def _validate_page(self, driver):
        '''
        try:
            driver.find_element_by_xpath(self._select_action_delete_click_xpath_locator)
        except:
            raise InvalidPageException("Select Action drop down not found.")
        '''
        pass
