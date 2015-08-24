from lib.base import BasePage
from lib.base import InvalidPageException
from time import sleep
from faker import Factory
from selenium.webdriver.common.keys import Keys
import os,json

cwd = os.getcwd()
os.chdir('..')
L1 = os.path.join(os.getcwd(), "data\json_Schooldata.json")
os.chdir(cwd)

class AssetPage(BasePage):
    # Asset Delete related locators
    _select_action_delete_click_xpath_locator = ".//*[@id='asset_actions_dropdown']/button[2]"
    _click_delete_text_xpath_locator = ".//*[@id='asset_actions_dropdown']/ul/li/a"

    # Asset List related
    _asset_list_locator = "//tbody/tr/td/a"
    _asset_list_check_box_locator = ".//*[@id='assetstable']/tbody/tr/td[1]/label/span/span[2]"
    _asset_list_asset_name_locator = ".//*[@id='assetstable']/tbody/tr/td[2]/a"
    _asset_list_asset_type_locator = ".//*[@id='assetstable']/tbody/tr/td[3]"

    # Asset Filter related to place and school
    _asset_filter_drop_down_locator = "//*[@id='span_filters']/div/div/button[2]"
    #asset list is already specified above i,e _asset_list_locator
    # we need xpath for type column i,e place or school. locator is already defined above i,e _asset_list_asset_type_locator
    _asset_place_type_drop_down_locator = "//div[@label='Type']"
    _asset_school_district_drop_down_locator = "//div[@label= 'District']"

    # New Asset creation related
    _asset_create_asset = "//img[@alt='Create asset']"

    # Place and School - Creation mode related
    _asset_type_field_name_text_box_locator = "//input[@ng-model='model']"
    #_asset_type_field_name_text_box_locator = ".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/div[1]/typeahead/div/input"
    _asset_type_field_address_text_box_locator = "//input[@ng-model='asset_edit.address.address1']"
    _asset_type_field_address2_text_box_locator = "//input[@ng-model='asset_edit.address.address2']"
    _asset_type_field_city_text_box_locator = "//input[@ng-model='asset_edit.address.city']"
    _asset_type_field_state_text_box_locator = "//input[@ng-model='asset_edit.address.state']"
    _asset_type_field_zip_text_box_locator = "//input[@ng-model='asset_edit.address.zip']"
    _asset_type_field_owner_text_box_locator = "//input[@placeholder='Owner']"
    _asset_type_field_phone_text_box_locator = "//input[@ng-model='asset_edit.phone']"
    _asset_type_field_type_drop_down_locator = "(//div[@label='Type']//button[@data-toggle='dropdown'])[2]"
    _asset_type_field_district_drop_down_locator = "//div[@label='District']//button[@data-toggle='dropdown']"
    _asset_type_field_grade_drop_down_locator = "//div[@label='Grade']//button[@data-toggle='dropdown']"

    _asset_type_cancel_button_locator = "//div[@id='asset_overview_modal']/div/div/form/div[2]/button[1]"
    _asset_type_save_button_locator = "//div[@id='asset_overview_modal']/div/div/form/div[2]/button[2]"

    _asset_points_of_contact_locator = "//div[contains(text(), 'Points of Contact')]"
    _asset_add_contact_locator = "btn_add_asset_contact"
    _asset_newcontact_firstname_locator = "first_name"
    _asset_newcontact_lastname_locator = "last_name"
    _asset_newcontact_prefix_locator = "//input[@placeholder='Prefix']"
    _asset_newcontact_title_locator = "//input[@placeholder='Title']"
    _asset_newcontact_phone_locator = "phone"
    _asset_newcontact_email_locator = "email"
    _asset_newcontact_address1_locator = "address"
    _asset_newcontact_address2_locator = "*//input[@ng-model='contact_edit.address.address2']"
    _asset_newcontact_city_locator = "*//input[@placeholder='City']"
    _asset_newcontact_state_locator = "state"
    _asset_newcontact_zip_locator = "zip"
    _asset_newcontact_save_locator = ".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[2]"
    _asset_newcontact_cancel_locator = ".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[1]"
    _asset_newcontact_delete_contact_locator = ".//*[@id='contacts_table']/tbody/tr/td[5]/a/img"
    _asset_newcontact_delete_contact_popup_locator = ".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]"
    _asset_newcontact_window_popup_cross_button_locator = ".//*[@id='asset_contact_modal']/div/div/div/button"
    _asset_newcontact_firstname_error_message_locator = ".//*[@id='asset_contact_error']/div[1]/small"
    _asset_newcontact_lastname_error_message_locator = ".//*[@id='asset_contact_error']/div[2]/small"
    _asset_newcontact_email_error_message_locator = ".//*[@id='asset_contact_error']/div[6]/small"
    _asset_newcontact_state_error_message_locator = "//*[@id='asset_contact_error']/div[3]/small"
    _asset_newcontact_zip_error_message_locator = "//*[@id='asset_contact_error']/div[4]/small"

    _asset_detail_email_locator = "//input[@placeholder='Email']"
    _asset_detail_save_button_locator = ".//*[@id='asset_details_modal']/div/div/form/div[2]/button[2]"

    _asset_overview_edit_link_locator = "//div[contains(text(),'Overview')]/div/img"
    _asset_overview_edit_name_locator = "name"
    _asset_overview_window_popup_cross_button_locator = "//*[@id='asset_overview_modal']/div/div/div/button"

    _asset_count = 0
    _assets = {}


    def __init__(self, driver):
        super(AssetPage, self).__init__(driver)

        '''
        assets_results = self.driver.find_elements_by_xpath(self._asset_list_locator)
        for asset in assets_results:
            assetname = asset.find_elements_by_xpath(self._asset_list_asset_name_locator).text
            self._assets[assetname] = asset.find_element_by_xpath(self._asset_list_check_box_locator)
            self._assets[assetname] = asset.find_element_by_xpath(self._asset_list_asset_type_locator)
        '''


    @property
    def select_action_drop_down(self):
        return self.driver.find_element_by_xpath(self._select_action_delete_click_xpath_locator)

    @property
    def click_delete_text(self):
        return self.driver.find_element_by_xpath(self._click_delete_text_xpath_locator)

    @property
    def display_place_type_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_place_type_drop_down_locator)

    @property
    def display_school_district_drop_down(self):
        return self.driver.find_element_by_xpath(self._asset_school_district_drop_down_locator)


    @property
    def enter_asset_type_name(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_name_text_box_locator)

    @property
    def enter_asset_type_address(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_address_text_box_locator)

    @property
    def enter_asset_type_address2(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_address2_text_box_locator)

    @property
    def enter_asset_type_city(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_city_text_box_locator)

    @property
    def enter_asset_type_state(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_state_text_box_locator)

    @property
    def enter_asset_type_zip(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_zip_text_box_locator)

    @property
    def enter_asset_type_owner(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_owner_text_box_locator)

    @property
    def enter_asset_type_phone(self):
        return self.driver.find_element_by_css_selector(self._asset_type_field_phone_text_box_locator)

    @property
    def select_asset_type_type(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_type_drop_down_locator)

    @property
    def select_asset_type_district(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_district_drop_down_locator)

    @property
    def select_asset_type_grade(self):
        return self.driver.find_element_by_xpath(self._asset_type_field_grade_drop_down_locator)

    @property
    def click_asset_type_cancel(self):
        return self.driver.find_element_by_xpath(self._asset_type_cancel_button_locator)

    @property
    def click_asset_type_save(self):
        return self.driver.find_element_by_xpath(self._asset_type_save_button_locator)

    @property
    def select_asset_points_of_contact(self):
        return self.driver.find_element_by_xpath(self._asset_points_of_contact_locator)

    @property
    def select_asset_add_contact(self):
        return self.driver.find_element_by_id(self._asset_add_contact_locator)

    @property
    def select_asset_newcontact_firstname(self):
        return self.driver.find_element_by_name(self._asset_newcontact_firstname_locator)

    @property
    def select_asset_newcontact_lastname(self):
        return self.driver.find_element_by_name(self._asset_newcontact_lastname_locator)

    @property
    def select_asset_newcontact_prefix(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_prefix_locator)

    @property
    def select_asset_newcontact_title(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_title_locator)

    @property
    def select_asset_newcontact_phone(self):
        return self.driver.find_element_by_name(self._asset_newcontact_phone_locator)

    @property
    def select_asset_newcontact_email(self):
        return self.driver.find_element_by_name(self._asset_newcontact_email_locator)

    @property
    def select_asset_newcontact_address1(self):
        return self.driver.find_element_by_name(self._asset_newcontact_address1_locator)

    @property
    def select_asset_newcontact_address2(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_address2_locator)

    @property
    def select_asset_newcontact_city(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_city_locator)

    @property
    def select_asset_newcontact_state(self):
        return self.driver.find_element_by_name(self._asset_newcontact_state_locator)

    @property
    def select_asset_newcontact_zip(self):
        return self.driver.find_element_by_name(self._asset_newcontact_zip_locator)

    @property
    def select_asset_newcontact_save(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_save_locator)

    @property
    def select_asset_newcontact_cancel(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_cancel_locator)

    @property
    def select_asset_newcontact_delete_icon(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_delete_contact_locator)

    @property
    def select_asset_newcontact_delete_popup_window(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_delete_contact_popup_locator)

    @property
    def select_asset_newcontact_window_cross_button(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_window_popup_cross_button_locator)

    @property
    def check_asset_newcontact_firstname_error_message(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_firstname_error_message_locator)

    @property
    def check_asset_newcontact_lastname_error_message(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_lastname_error_message_locator)

    @property
    def check_asset_newcontact_state_error_message(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_state_error_message_locator)

    @property
    def check_asset_newcontact_zip_error_message(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_zip_error_message_locator)

    @property
    def check_asset_newcontact_email_error_message(self):
        return self.driver.find_element_by_xpath(self._asset_newcontact_email_error_message_locator)

    @property
    def select_asset_detail_edit_email_text_box(self):
        return self.driver.find_element_by_xpath(self._asset_detail_email_locator)

    @property
    def select_asset_detail_edit_save_button(self):
        return self.driver.find_element_by_xpath(self._asset_detail_save_button_locator)

    @property
    def select_asset_overview_edit_link(self):
        return self.driver.find_element_by_xpath(self._asset_overview_edit_link_locator)

    @property
    def select_asset_overview_edit_name_text_box(self):
        return self.driver.find_element_by_name(self._asset_overview_edit_name_locator)

    @property
    def select_asset_overview_window_cross_button(self):
        return self.driver.find_element_by_xpath(self._asset_overview_window_popup_cross_button_locator)


    def select_checkbox_in_grid(self):
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


    def asset_create(self):
        # Click on Create asset
        clickCreateAsset = self.driver.find_element_by_xpath(self._asset_create_asset)
        clickCreateAsset.click()
        sleep(10)
        # switch to new window
        self.driver.switch_to.active_element
        # Verify title "Asset overview" window
        self.driver.find_element_by_xpath("//div[@id='asset_overview_modal']/div/div/div/h4").text
        #sleep(2)
        #print("Asset overview", Create_Asset_Title)


    def get_schooldata(self):

        with open(L1) as data_file:
            school_data = json.load(data_file)

            for each in school_data:
                self.asset_name = each["asset_name"]
                self.asset_address = each["asset_address"]
                self.asset_address2 = each["asset_address2"]
                self.asset_city = each["asset_city"]
                self.asset_state = each["asset_state"]
                self.asset_zip = each["asset_zip"]
                self.asset_owner = each["asset_owner"]
                self.asset_type = each["asset_type"]
                self.asset_distrct = each["asset_district"]
                self.asset_grade = each["asset_grade"]


    def create_school_asset(self):
        # Select Place from the dropdown to create new place asset
        self.get_schooldata()
        self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[1]/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()
        sleep(4)

        self.enter_asset_type_name.send_keys(self.asset_name)
        self.enter_asset_type_name.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_address.send_keys(self.asset_address)
        self.enter_asset_type_address.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_address2.send_keys(self.asset_address2)
        self.enter_asset_type_address2.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_city.send_keys(self.asset_city)
        self.enter_asset_type_city.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_state.send_keys(self.asset_state)
        self.enter_asset_type_state.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_zip.send_keys(self.asset_zip)
        self.enter_asset_type_zip.send_keys(Keys.TAB)
        sleep(2)
        self.enter_asset_type_owner.send_keys(self.asset_owner)
        self.enter_asset_type_owner.send_keys(Keys.TAB)
        sleep(2)
        #self.select_asset_type_type.click()
        #sleep(2)

    def asset_save(self):
        self.click_asset_type_save.click()
        sleep(2)

    def asset_cancel(self):
        self.click_asset_type_cancel.click()
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




    def _validate_page(self, driver):
        try:
            driver.find_element_by_xpath(self._select_action_delete_click_xpath_locator)
        except:
            raise InvalidPageException("Select Action drop down not found.")

