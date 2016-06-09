import json
import os
from time import sleep

__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from basepage import BasePage
from loginpage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import inspect
from selenium.webdriver.support import expected_conditions
cwd = os.getcwd()
os.chdir('..')
eventData = os.path.join(os.getcwd(), "data", "json_Eventdata.json")
os.chdir(cwd)

class EventsPage(BasePageClass, object):
    _app_events_appname_locator = "//span[contains(text(),'Events')]"
    _app_events_Type_dropdown_locator = "//div[@model='filter.value']//button[contains(text(), 'Type')]"
    _app_events_main_create_button_locator = "//img[@ng-src='../images/icon_create_item_off.png']"
    _event_link_delete_text_xpath_locator = ".//*[@id='event_actions_dropdown']/ul/li/a"
    # Events Delete related locators
    _event_select_action_delete_select_xpath_locator = ".//*[@id='event_actions_dropdown']/button[text()=" \
                                                       "'Select action']/following-sibling::button"
    _event_select_action_delete_click_xpath_locator = ".//*[@id='delete_event_modal']/descendant::button[text()=" \
                                                      "'Delete']"
    _event_list_select_first_check_box_xpath_locator = ".//*[@id='eventsTable']/tbody/tr[1]/td[1]/label/span/span[2]"
    _event_list_check_box_locator = ".//*[@id='eventsTable']/tbody/tr/td[1]/label/span/span[2]"
    _event_list_events_name_locator = "//*[@id='eventsTable']/tbody/tr/td[2]/a"
    _event_deleteevent_cancel_click_xpath_locator = ".//*[@id='delete_event_modal']/descendant::button[text()='Cancel']"
    # New Event creation related
    _event_create_event = "//img[@ng-src='../images/icon_create_item_off.png']"
    _event_link_locator = "Events"
    _event_list_event_name_black_color_locator = "//*[@id='eventsTable']/tbody/tr/td[2]"
    # Creating Events
    _event_create_click = "//img[@title='Create event']"
    _event_title = "//h4[contains(text(),'Event overview')]"
    _event_type_field_name_text_box_locator = "//*[@id='event_overview_edit_modal']/div/div/form/div[1]/div[1]/input"
    _event_type_field_Start_Date_text_box_locator = "//label[contains(text(),'Start Date')]/following-sibling::span" \
                                                    "/descendant::input[@ng-model='datetime_internal']"
    _event_type_field_End_Date_text_box_locator = "//label[contains(text(),'End Date')]/following-sibling::span" \
                                                  "/descendant::input[@ng-model='datetime_internal']"
    _event_type_field_Venue_text_box_locator = "//input[@placeholder='Venue']"
    _event_type_field_TAG_text_box_locator = "//input[@placeholder='Add a tag']"
    _event_type_field_TAG_button_locator = "//button[@ng-click='addEventTag()']"
    _event_type_field_CANCEL_button_locator = "//button[@ng-click='cancelEventOverviewEdit()']"
    _event_type_field_SAVE_button_locator = "//button[@ng-click='saveEventOverviewEdit()']"
    _event_type_field_type_drop_down_locator = "//button[contains(text(), 'Type')]"
    _event_type_field_type_text_box_locator = "//input[@placeholder='Enter new value']"
    _event_type_field_add_button_locator = "//*[@id='newItemButton']"
    # Event name on Breadcrumb
    _event_name_breadcrumb = "//*[@id='header']/div[1]/span[3]/span"
    _event_search_textbox_locator = "//input[@id='txt_search_events']"
    _event_table_createdcolumn_locator = "//*[@id='eventsTable']/thead/tr/th[3]"
    _event_list_background_locator = ".//*[@id='eventstable']/tbody/tr/td[2]"
    _event_type_Saved_label_locator = ".//*[@id='header']/div[contains(text(),'Saved')]"
    _event_overview_edit_link_locator = "//div[contains(text(),'Overview')]/div/img"
    # Event Details panel
    _event_details_edit_widget_locator = "//*[@id='widgets']/div[2]/div/div[1]"
    _event_detail_edit_link_locator = "//img[@ng-click = 'openEventDetailsEdit()']"
    _event_detail_edit_attendees_textbox_locator = "//input[@ng-model = 'event_edit.details.attendees']"
    _event_detail_edit_address1_textbox_locator = "//input[@ng-model = 'event_edit.details.address.address1']"
    _event_detail_edit_address2_textbox_locator = "//input[@ng-model = 'event_edit.details.address.address2']"
    _event_detail_edit_city_textbox_locator = "//input[@ng-model = 'event_edit.details.address.city']"
    _event_detail_edit_state_textbox_locator = "//input[@ng-model = 'event_edit.details.address.state']"
    _event_detail_edit_zip_textbox_locator = "//input[@ng-model = 'event_edit.details.address.zip']"
    _event_detail_edit_url_textbox_locator = "//input[@ng-model = 'event_edit.details.url']"
    _event_detail_edit_description_textbox_locator = "//textarea[@ng-model = 'event_edit.details.description']"
    _event_detail_edit_save_button_locator = "//button[@ng-click = 'saveEventDetailsEdit()']"
    _event_detail_edit_cancel_button_locator = "//button[@ng-click = 'cancelEventDetailsEdit()']"
    # Location related
    _event_location_map_id_locator = "map_control"
    _event_location_edit_icon_xpath_locator = ".//div[@id='map_control']/following-sibling::img[@class='widget_edit']"
    _event_location_title_id_locator = ".//*[@id='location_modal']/descendant::div[@class='modal-header']"
    _event_location_latitude_name_locator = "latitude"
    _event_location_latitude_error_xpath_locator = ".//*[@id='map_popup']/descendant::label[text()='Latitude']" \
                                                   "/following-sibling::span[@class='error']/small"
    _event_location_save_xpath_locator = ".//*[@id='location_modal']/div/div/form/div[2]/button[2]"
    _event_location_cancel_xpath_locator = ".//*[@id='location_modal']/descendant::button[text()='Cancel']"
    _event_location_longitude_name_locator = "longitude"
    _event_location_longitude_error_xpath_locator = ".//*[@id='map_popup']/descendant::label[text()='Longitude']" \
                                                    "/following-sibling::span[@class='error']/small"
    # _event_location_marker_avaliable_xpath_locator = ".//*[@id='map_control']/descendant::div" \
    #                                                  "[@class='leaflet-marker-pane']/img[contains(@class," \
    #                                                  "'leaflet-marker-icon')]"

    _event_location_marker_avaliable_xpath_locator = "//img[@src='/components/leaflet/images/new_item.png']"
    _event_location_event_name_xpath_locator = ".//*[@id='map_control']/div[1]/div[2]/div[4]/div/div[1]/div/b"
    # Point of Contacts related
    _event_points_of_contact_header_locator = "//div[contains(text(), 'Points of Contact')]"
    _events_points_of_contact_title_locator = ".//*[@id='event_contact_modal_title']"
    _event_point_of_contact_name_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Name']"
    _event_point_of_contact_title_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Title']"
    _event_point_of_contact_phone_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Phone']"
    _event_point_of_contact_email_tab_locator = "//*[@id='contacts_table']/thead/tr/th[text()='Email']"
    _event_point_of_contact_name_text_value_locator = "//table[@id='contacts_table']//tbody//tr/td//" \
                                                      "a[@class='showaslink showaslink-edit']"
    _event_point_of_contact_title_text_value_locator = "(//table[@id='contacts_table']//tbody//tr/td//" \
                                                       "a[@class='showaslink showaslink-edit'])/../" \
                                                       "following-sibling::td[1]"
    _event_point_of_contact_phone_text_value_locator = "(//table[@id='contacts_table']//tbody//tr/td//" \
                                                       "a[@class='showaslink showaslink-edit'])/../" \
                                                       "following-sibling::td[2]"
    _event_point_of_contact_email_text_value_locator = "(//table[@id='contacts_table']//tbody//tr/td//" \
                                                       "a[@class='showaslink showaslink-edit'])/../" \
                                                       "following-sibling::td[3]"



    #New Contact Window
    _event_main_contct_widget_locator = ".//*[@id='widgets']/descendant::div[@class='widget widget_contacts']" \
                                        "/div[@class='widgetheader']"
    _event_add_contact_button_locator = "btn_add_event_contact"
    _event_newcontact_firstname_textbox_locator = "first"
    _event_newcontact_lastname_textbox_locator = "last"
    _event_newcontact_prefix_textbox_locator = "//input[@placeholder='Prefix']"
    _event_newcontact_title_textbox_locator = "//input[@placeholder='Title']"
    _event_newcontact_phone_textbox_locator = "phone"
    _event_newcontact_email_textbox_locator = "email"
    _event_newcontact_address1_textbox_locator = "//input[@ng-model='contact_edit.address.address1']"
    _event_newcontact_address2_textbox_locator = "//input[@ng-model='contact_edit.address.address2']"
    _event_newcontact_city_textbox_locator = "//input[@ng-model='contact_edit.address.city']"
    _event_newcontact_state_textbox_locator = "//input[@ng-model='contact_edit.address.state']"
    _event_newcontact_zip_textbox_locator = "//input[@ng-model='contact_edit.address.zip']"
    _event_newcontact_save_button_locator = "//button[@ng-click='save_event_contact_edit()']"
    _event_newcontact_cancel_button_locator = "//button[@ng-click='cancel_event_contact_edit()']"
    _event_newcontact_delete_contact_icon_locator = ".//*[@id='contacts_table']/tbody/tr[1]/descendant::a/img"
    _event_newcontact_delete_contact_popup_delete_button_locator = ".//*[@id='event_delete_contact_modal']" \
                                                                   "/div/div/div[3]/button[2]"
    _event_newcontact_delete_contact_popup_cancel_button_locator = ".//*[@id='event_delete_contact_modal']" \
                                                                   "/div/div/div[3]/button[1]"
    _event_newcontact_window_popup_cross_button_locator = ".//*[@id='event_contact_modal']/descendant::" \
                                                          "button[@class='close fui-cross']"
    _event_newcontact_firstname_error_message_locator = "//*[@id='event_contact_error']/div[1]/small"
    _event_newcontact_lastname_error_message_locator = ".//*[@id='event_contact_error']/div[2]/small"
    _event_newcontact_email_error_message_locator = ".//*[@id='event_contact_error']/div[6]/small"
    _event_newcontact_state_error_message_locator = ".//div[contains(@ng-show,'form_contact_edit.state')]/small"
    _event_newcontact_zip_error_message_locator = ".//div[contains(@ng-show,'form_contact_edit.zip')]/small"
    _event_contact_first_last_name_value_text = "(//table[@id='contacts_table']//tbody//tr/td//a[" \
                                                "@class='showaslink showaslink-edit'])[1]"
    _event_contact_title_value_text_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[" \
                                              "@class='showaslink showaslink-edit'])[1]/../following-sibling::td[1]"
    _event_contact_phone_value_text_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[" \
                                              "@class='showaslink showaslink-edit'])[1]/../following-sibling::td[2]"
    _event_contact_email_value_text_locator = "(//table[@id='contacts_table']//tbody//tr/td//a[" \
                                              "@class='showaslink showaslink-edit'])[1]/../following-sibling::td[3]"
    _event_contact_new_contact_text_locator = "//table[@id='contacts_table']//tbody//tr"
    _event_main_contact_window_locator = ".//*[@id='form_main_contact']"
    _event_main_contact_name_locator = ".//*[@id='form_main_contact']/div[2]/table/tbody/tr[1]/td[2]"
    _event_header_save_text_locator = ".//*[@id='header']/div[contains(@class,'right ng-binding')]"

    # Scroll vertically
    _event_map_scroll = "//*[@id='page_content']"
    # Importance
    #
    # Click - //button[contains(text(),'Importance')]
    # Enter New Value - //input[@ng-model='itemInput']
    # Click - Add - //button[@id='newItemButton']
    #
    @property
    def get_events_app_name_label(self):
        return self.basepage.findElementByXpath(self._app_events_appname_locator)

    @property
    def get_Type_dropdown(self):
        try:
            return self.basepage.findElementByXpath(self._app_events_Type_dropdown_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._app_events_Type_dropdown_locator + err.message)

    @property
    def get_main_create_incident_button(self):
        try:
            return self.basepage.findElementByXpath(self._app_events_main_create_button_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._app_events_main_create_button_locator + err.message)

    @property
    def get_event_select_action_drop_down(self):
        try:
            return self.driver.find_element_by_xpath(self._event_select_action_delete_select_xpath_locator)
        except Exception, err:
            raise type(err)("Select Action drop down not available - searched XPATH - " \
                          + self._event_select_action_delete_select_xpath_locator + err.message)

    @property
    def get_event_name_list(self):
        try:
            return self.basepage.findElementsByXpath(self._event_list_event_name_black_color_locator)
        except Exception, err:
            raise type(err)("Black color in the list not available after insertion - searched XPATH - " \
                          + self._event_list_event_name_black_color_locator + err.message)

    @property
    def get_event_link_delete_text(self):
        try:
            return self.basepage.findElementByXpath(self._event_link_delete_text_xpath_locator)
        except Exception, err:
            raise type(err)("Delete option not present in the select action dropdown - searched XPATH - " \
                          + self._event_link_delete_text_xpath_locator + err.message)

    @property
    def get_event_list_first_check_box(self):
        try:
            return self.basepage.findElementByXpath(self._event_list_select_first_check_box_xpath_locator)
        except Exception, err:
            raise type(err)("Event table checkbox not available - searched XPATH - " \
                          + self._event_list_select_first_check_box_xpath_locator + err.message)

    @property
    def get_deleteevent_cancel_button(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH, self._event_deleteevent_cancel_click_xpath_locator)), "Cancel button not available")
            return self.driver.find_element_by_xpath(self._event_deleteevent_cancel_click_xpath_locator)
        except Exception, err:
            raise type(err)("Cancel button not available in Delete Events popup - searched XPATH - " \
                          + self._event_deleteevent_cancel_click_xpath_locator + err.message)

    @property
    def get_events_name_list(self):
        try:
            return self.driver.find_elements_by_xpath(self._event_list_events_name_locator)
        except Exception, err:
            raise type(err)("Event name column not available in the events table - searched XPATH - " \
                          + self._event_list_events_name_locator + err.message)


    def __init__(self, driver):
        super(EventsPage,self).__init__(driver)
        self.get_eventdata()
        self.basepage = BasePage(self.driver)

    def open_event_app(self):
        loginpage = LoginPage(self.driver)
        loginpage.loginDashboard()
        appicon = IconListPage(self.driver)
        appicon.click_events_icon()

    @property
    def get_event_create_event(self):
        try:
            self.driver.find_element_by_xpath(self._event_create_event)
        except:
            return False
        return True

    @property
    def get_event_delete_button(self):
        try:
            return self.basepage.findElementByXpath(self._event_select_action_delete_click_xpath_locator)
        except Exception, err:
            raise type(err)("Delete button not available in Delete Events popup - searched XPATH - " \
                          + self._event_select_action_delete_click_xpath_locator + err.message)

    @property
    def get_event_title_click(self):
        try:
            return self.basepage.findElementByXpath(self._event_title)
        except Exception, err:
            raise type(err)("Event title - searched XPATH - " \
                          + self._event_title + err.message)



    @property
    def enter_event_type_name(self):
        try:
            return self.driver.find_element_by_xpath(self._event_type_field_name_text_box_locator)
        except Exception, err:
            raise type(err)("Event name textbox not available - searched XPATH - " \
                          + self._event_type_field_name_text_box_locator + err.message)

    @property
    def enter_event_type_start_date(self):
        try:
            return self.driver.find_element_by_xpath(self._event_type_field_Start_Date_text_box_locator)
        except Exception, err:
            raise type(err)("Event Start Date textbox not available - searched XPATH - " \
                          + self._event_type_field_Start_Date_text_box_locator + err.message)

    @property
    def enter_event_type_end_date(self):
        try:
            return self.driver.find_element_by_xpath(self._event_type_field_End_Date_text_box_locator)
        except Exception, err:
            raise type(err)("Event End Date textbox not available - searched XPATH - " \
                          + self._event_type_field_End_Date_text_box_locator + err.message)

    @property
    def get_event_type_drop_down(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, self._event_type_field_type_drop_down_locator)))
            return self.driver.find_element_by_xpath(self._event_type_field_type_drop_down_locator)
        except Exception, err:
            raise type(err)("Event type dropdown not available - searched XPATH - " \
                          + self._event_type_field_type_drop_down_locator + err.message)

    @property
    def get_event_newtype_text_box(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, self._event_type_field_type_text_box_locator)))
            return self.driver.find_element_by_xpath(self._event_type_field_type_text_box_locator)
        except Exception, err:
            raise type(err)("Event Type textbox not available - searched XPATH - " \
                          + self._event_type_field_type_text_box_locator + err.message)

    @property
    def get_event_type_add_button(self):
        try:
            return self.driver.find_element_by_xpath(self._event_type_field_add_button_locator)
        except Exception, err:
            raise type(err)("Event Type Add button not available - searched XPATH - " \
                          + self._event_type_field_add_button_locator + err.message)


    @property
    def enter_event_type_venue(self):
        try:
            return self.driver.find_element_by_xpath(self._event_type_field_Venue_text_box_locator)
        except Exception, err:
            raise type(err)("Event Venue textbox not available - searched XPATH - " \
                          + self._event_type_field_Venue_text_box_locator + err.message)


    @property
    def enter_event_type_tag(self):
        try:
            return self.driver.find_element_by_xpath(self._event_type_field_TAG_text_box_locator)
        except Exception, err:
            raise type(err)("Event TAG textbox not available - searched XPATH - " \
                          + self._event_type_field_TAG_text_box_locator + err.message)

    @property
    def get_event_type_tag_add_button(self):
        try:
            return self.driver.find_element_by_xpath(self._event_type_field_TAG_button_locator)
        except Exception, err:
            raise type(err)("Event Type TAG Add button not available - searched XPATH - " \
                          + self._event_type_field_TAG_button_locator + err.message)

    @property
    def get_event_type_cancel_add_button(self):
        try:
            return self.driver.find_element_by_xpath(self._event_type_field_CANCEL_button_locator)
        except Exception, err:
            raise type(err)("Event Type CANCEL Add button not available - searched XPATH - " \
                          + self._event_type_field_CANCEL_button_locator + err.message)

    @property
    def get_event_type_save_add_button(self):
        try:
            return self.driver.find_element_by_xpath(self._event_type_field_SAVE_button_locator)
        except Exception, err:
            raise type(err)("Event Type SAVE Add button not available - searched XPATH - " \
                          + self._event_type_field_SAVE_button_locator + err.message)

    @property
    def get_event_name_breadcrumb(self):
        try:
            return self.driver.find_element_by_xpath(self._event_name_breadcrumb)
        except Exception, err:
            raise type(err)("Event name not available in breadcrumb - searched XPATH - " \
                          + self._event_name_breadcrumb + err.message)

    @property
    def get_eventtable_created_column(self):
        return self.driver.find_element_by_xpath(self._event_table_createdcolumn_locator)

    @property
    def get_event_list_background(self):
        return self.driver.find_elements_by_xpath(self._event_list_background_locator)

    # event overview related properties
    @property
    def get_event_overview_edit_link(self):
        try:
            WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(
                (By.XPATH , self._event_overview_edit_link_locator)))
            return self.basepage.findIfElementVisible(self._event_overview_edit_link_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_overview_edit_link_locator + err.message)

    @property
    def event_type_Saved_label(self):
        try:
            return self.basepage.findElementByXpath(self._event_type_Saved_label_locator)
        except Exception, err:
            raise type(err)("'Saved' label not available - searched XPATH - " \
                          + self._event_type_Saved_label_locator + err.message)

    # Events Details related properties
    @property
    def get_event_detail_edit_link(self):
        try:
            return self.driver.find_element_by_xpath(self._event_detail_edit_link_locator)
        except Exception, err:
            raise type(err)("Event Details Edit link not available - searched XPATH - " \
                          + self._event_detail_edit_link_locator + err.message)

    @property
    def get_event_detail_edit_attendees_text_box(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, self._event_detail_edit_attendees_textbox_locator)))
            return self.driver.find_element_by_xpath(self._event_detail_edit_attendees_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_detail_edit_attendees_textbox_locator + err.message)

    @property
    def get_event_detail_edit_address1_text_box(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, self._event_detail_edit_address1_textbox_locator)))
            return self.driver.find_element_by_xpath(self._event_detail_edit_address1_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_detail_edit_address1_textbox_locator + err.message)

    @property
    def get_event_detail_edit_address2_text_box(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, self._event_detail_edit_address2_textbox_locator)))
            return self.driver.find_element_by_xpath(self._event_detail_edit_address2_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_detail_edit_address2_textbox_locator + err.message)

    @property
    def get_event_detail_edit_city_text_box(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, self._event_detail_edit_city_textbox_locator)))
            return self.driver.find_element_by_xpath(self._event_detail_edit_city_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_detail_edit_city_textbox_locator + err.message)

    @property
    def get_event_detail_edit_state_text_box(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, self._event_detail_edit_state_textbox_locator)))
            return self.driver.find_element_by_xpath(self._event_detail_edit_state_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_detail_edit_state_textbox_locator + err.message)

    @property
    def get_event_detail_edit_zip_text_box(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, self._event_detail_edit_zip_textbox_locator)))
            return self.driver.find_element_by_xpath(self._event_detail_edit_zip_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_detail_edit_zip_textbox_locator + err.message)

    @property
    def get_event_detail_edit_url_text_box(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, self._event_detail_edit_url_textbox_locator)))
            return self.driver.find_element_by_xpath(self._event_detail_edit_url_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_detail_edit_url_textbox_locator + err.message)

    @property
    def get_event_detail_edit_description_text_box(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.XPATH, self._event_detail_edit_description_textbox_locator)))
            return self.driver.find_element_by_xpath(self._event_detail_edit_description_textbox_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_detail_edit_description_textbox_locator + err.message)

    @property
    def get_event_detail_edit_save_button(self):
        try:
            return self.driver.find_element_by_xpath(self._event_detail_edit_save_button_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_detail_edit_save_button_locator + err.message)

    @property
    def get_event_detail_edit_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._event_detail_edit_cancel_button_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_detail_edit_cancel_button_locator + err.message)

    # Location related properties
    @property
    def get_event_location_map(self):
        try:
            return self.driver.find_element_by_id(self._event_location_map_id_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_location_map_id_locator + err.message)

    @property
    def get_event_location_edit_icon(self):
        try:
            return self.driver.find_element_by_xpath(self._event_location_edit_icon_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_location_edit_icon_xpath_locator + err.message)

    @property
    def get_event_location_title(self):
        try:
            return self.driver.find_element_by_xpath(self._event_location_title_id_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_location_title_id_locator + err.message)

    @property
    def get_event_location_latitude_textbox(self):
        try:
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located(
                (By.NAME , self._event_location_latitude_name_locator)))
            return self.driver.find_element_by_name(self._event_location_latitude_name_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_location_latitude_name_locator + err.message)

    @property
    def get_event_location_latitude_error_text(self):
        try:
            return self.driver.find_element_by_xpath(self._event_location_latitude_error_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_location_latitude_error_xpath_locator + err.message)

    @property
    def get_event_location_save_button(self):
        try:
            return self.driver.find_element_by_xpath(self._event_location_save_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_location_save_xpath_locator + err.message)

    @property
    def get_event_location_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._event_location_cancel_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_location_cancel_xpath_locator + err.message)


    @property
    def get_event_location_longitude_textbox(self):
        try:
            return self.driver.find_element_by_name(self._event_location_longitude_name_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_location_longitude_name_locator + err.message)

    @property
    def get_event_location_longitude_error_text(self):
        try:
            return self.driver.find_element_by_xpath(self._event_location_longitude_error_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_location_longitude_error_xpath_locator + err.message)

    @property
    def get_event_location_marker_available_image(self):
        try:
             return self.basepage.findElementByXpath(self._event_location_marker_avaliable_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_location_marker_avaliable_xpath_locator + err.message)


    @property
    def get_event_location_event_name_text(self):
        try:
            return self.driver.find_element_by_xpath(self._event_location_event_name_xpath_locator)
        except Exception, err:
            raise type(err)(" - searched XPATH - " \
                          + self._event_location_event_name_xpath_locator + err.message)


    @property
    def get_event_points_of_contact_header(self):
        try:
            return self.driver.find_element_by_xpath(self._event_points_of_contact_header_locator)
        except Exception, err:
            raise type(err)("Points of Contact header not available - searched XPATH - " \
                          + self._event_points_of_contact_header_locator + err.message)

    @property
    def get_event_add_contact_button(self):
        try:
            return self.driver.find_element_by_id(self._event_add_contact_button_locator)
        except Exception, err:
            raise type(err)("Add contact button not available in Points of Contact- searched XPATH - " \
                          + self._event_add_contact_button_locator + err.message)

    @property
    def get_event_newcontact_firstname_textbox(self):
        try:
            return self.basepage.findElementByName(self._event_newcontact_firstname_textbox_locator)
        except Exception, err:
            raise type(err)("New contact first name textbox not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_firstname_textbox_locator + err.message)

    @property
    def get_event_newcontact_lastname_textbox(self):
        try:
            return self.driver.find_element_by_name(self._event_newcontact_lastname_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Last name textbox not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_lastname_textbox_locator + err.message)

    @property
    def get_event_newcontact_prefix_textbox(self):
        try:
            return self.basepage.findElementByXpath(self._event_newcontact_prefix_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Prefix textbox not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_prefix_textbox_locator + err.message)

    @property
    def get_event_newcontact_title_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._event_newcontact_title_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Title textbox not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_title_textbox_locator + err.message)

    @property
    def get_event_newcontact_phone_textbox(self):
        try:
            return self.driver.find_element_by_name(self._event_newcontact_phone_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Phone no textbox not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_phone_textbox_locator + err.message)

    @property
    def get_event_newcontact_email_textbox(self):
        try:
            return self.basepage.findElementByName(self._event_newcontact_email_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Email ID textbox not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_email_textbox_locator + err.message)

    @property
    def get_event_newcontact_address1_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._event_newcontact_address1_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Address1 textbox not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_address1_textbox_locator + err.message)

    @property
    def get_event_newcontact_address2_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._event_newcontact_address2_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Address2 textbox not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_address2_textbox_locator + err.message)

    @property
    def get_event_newcontact_city_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._event_newcontact_city_textbox_locator)
        except Exception, err:
            raise type(err)("New contact City textbox not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_city_textbox_locator + err.message)

    @property
    def get_event_newcontact_state_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._event_newcontact_state_textbox_locator)
        except Exception, err:
            raise type(err)("New contact State textbox not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_state_textbox_locator + err.message)

    @property
    def get_event_newcontact_zip_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._event_newcontact_zip_textbox_locator)
        except Exception, err:
            raise type(err)("New contact Zip textbox not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_zip_textbox_locator + err.message)

    @property
    def get_event_newcontact_save_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, self._event_newcontact_save_button_locator)))
            return self.driver.find_element_by_xpath(self._event_newcontact_save_button_locator)
        except Exception, err:
            raise type(err)("New contact Save button not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_save_button_locator + err.message)

    @property
    def get_event_newcontact_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._event_newcontact_cancel_button_locator)
        except Exception, err:
            raise type(err)("New contact Cancel button not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_cancel_button_locator + err.message)

    @property
    def get_event_newcontact_delete_icon(self):
        try:
            return self.driver.find_element_by_xpath(self._event_newcontact_delete_contact_icon_locator)
        except Exception, err:
            raise type(err)("New contact Delete Icon not available in Points of Contact- searched XPATH - " \
                          + self._event_newcontact_delete_contact_icon_locator + err.message)

    @property
    def get_event_newcontact_delete_popup_delete_button(self):
        try:
            return self.basepage.findElementByXpath(self._event_newcontact_delete_contact_popup_delete_button_locator)
        except Exception, err:
            raise type(err)("New contact Delete Button not available in Delete Contact popup- searched XPATH - " \
                          + self._event_newcontact_delete_contact_popup_delete_button_locator + err.message)

    @property
    def get_event_newcontact_delete_popup_cancel_button(self):
        try:
            return self.basepage.findElementByXpath(self._event_newcontact_delete_contact_popup_cancel_button_locator)
        except Exception, err:
            raise type(err)("New contact Cancel Button not available in Delete Contact popup- searched XPATH - " \
                          + self._event_newcontact_delete_contact_popup_cancel_button_locator + err.message)

    @property
    def get_event_newcontact_window_cross_button(self):
        try:
            return self.basepage.findElementByXpath(self._event_newcontact_window_popup_cross_button_locator)
        except Exception, err:
            raise type(err)("Cross Button not available in Delete Contact popup- searched XPATH - " \
                          + self._event_newcontact_window_popup_cross_button_locator + err.message)

    @property
    def get_event_newcontact_firstname_error_message(self):
        try:
            return self.basepage.findElementByXpath(self._event_newcontact_firstname_error_message_locator)
        except Exception, err:
            raise type(err)("Validation message for First name not available in contact information- searched XPATH - " \
                          + self._event_newcontact_firstname_error_message_locator + err.message)

    @property
    def get_event_newcontact_lastname_error_message(self):
        try:
            return self.basepage.findElementByXpath(self._event_newcontact_lastname_error_message_locator)
        except Exception, err:
            raise type(err)("Validation message for Last name not available in contact information- searched XPATH - " \
                          + self._event_newcontact_lastname_error_message_locator + err.message)

    @property
    def get_event_newcontact_email_error_message(self):
        try:
            return self.basepage.findElementByXpath(self._event_newcontact_email_error_message_locator)
        except Exception, err:
            raise type(err)("Validation message for Email ID not available in contact information  - searched XPATH - " \
                          + self._event_newcontact_email_error_message_locator + err.message)

    @property
    def get_event_contact_first_last_name_value_text(self):
        try:
            return self.basepage.findElementByXpath(self._event_contact_first_last_name_value_text)
        except Exception, err:
            raise type(err)("Contact Name not appearing in Points of contact widget  - searched XPATH - " \
                          + self._event_contact_first_last_name_value_text + err.message)

    @property
    def get_event_contact_title_value_text(self):
        try:
            return self.driver.find_element_by_xpath(self._event_contact_title_value_text_locator)
        except Exception, err:
            raise type(err)("Contact Title not appearing in Points of contact widget  - searched XPATH - " \
                          + self._event_contact_title_value_text_locator + err.message)

    @property
    def get_event_contact_phone_value_text(self):
        try:
            return self.driver.find_element_by_xpath(self._event_contact_phone_value_text_locator)
        except Exception, err:
            raise type(err)("Contact Phone no not appearing in Points of contact widget  - searched XPATH - " \
                          + self._event_contact_phone_value_text_locator + err.message)

    @property
    def get_event_contact_email_value_text(self):
        try:
            return self.driver.find_element_by_xpath(self._event_contact_email_value_text_locator)
        except Exception, err:
            raise type(err)("Contact Email ID not appearing in Points of contact widget - searched XPATH - " \
                          + self._event_contact_email_value_text_locator + err.message)

    @property
    def get_event_contact_new_contact_value_text(self):
        try:
            return self.driver.find_element_by_xpath(self._event_contact_new_contact_text_locator)
        except Exception, err:
            raise type(err)("No Contact appearing in Points of contact widget - searched XPATH - " \
                          + self._event_contact_new_contact_text_locator + err.message)

    @property
    def get_event_main_contact_window(self):
        try:
            return self.driver.find_element_by_xpath(self._event_main_contact_window_locator)
        except Exception, err:
            raise type(err)("Main Contact window title not available - searched XPATH - " \
                          + self._event_main_contact_window_locator + err.message)

    @property
    def get_event_main_contact_name_text(self):
        try:
            return self.driver.find_element_by_xpath(self._event_main_contact_name_locator)
        except Exception, err:
            raise type(err)("Main Contact name not available - searched XPATH - " \
                          + self._event_main_contact_name_locator + err.message)

    @property
    def get_event_point_of_contact_name_tab(self):
        try:
            return self.basepage.findElementByXpath(self._event_point_of_contact_name_tab_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget Name Tab not available - searched XPATH - " \
                          + self._event_point_of_contact_name_tab_locator + err.message)

    @property
    def get_event_point_of_contact_title_tab(self):
        try:
            return self.driver.find_element_by_xpath(self._event_point_of_contact_title_tab_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget Title Tab not available  - searched XPATH - " \
                          + self._event_point_of_contact_title_tab_locator + err.message)

    @property
    def get_event_point_of_contact_phone_tab(self):
        try:
            return self.driver.find_element_by_xpath(self._event_point_of_contact_phone_tab_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget Phone Tab not available  - searched XPATH - " \
                          + self._event_point_of_contact_phone_tab_locator + err.message)

    @property
    def get_event_point_of_contact_email_tab(self):
        try:
            return self.driver.find_element_by_xpath(self._event_point_of_contact_email_tab_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget Email Tab not available  - searched XPATH - " \
                          + self._event_point_of_contact_email_tab_locator + err.message)

    @property
    def get_event_point_of_contact_name_text_value(self):
        try:
            return self.basepage.findElementsByXpath(self._event_point_of_contact_name_text_value_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget contacts do not have Name Values - searched XPATH - " \
                          + self._event_point_of_contact_name_text_value_locator + err.message)

    @property
    def get_event_point_of_contact_title_text_value(self):
        try:
            return self.basepage.findElementsByXpath(self._event_point_of_contact_title_text_value_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget contacts do not have Title Values - searched XPATH - " \
                          + self._event_point_of_contact_title_text_value_locator + err.message)

    @property
    def get_event_point_of_contact_phone_text_value(self):
        try:
            return self.basepage.findElementsByXpath(self._event_point_of_contact_phone_text_value_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget contacts do not have Phone Values - searched XPATH - " \
                          + self._event_point_of_contact_phone_text_value_locator + err.message)

    @property
    def get_event_point_of_contact_email_text_value(self):
        try:
            return self.basepage.findElementsByXpath(self._event_point_of_contact_email_text_value_locator)
        except Exception, err:
            raise type(err)("In Point of Contact widget contacts do not have Email Values - searched XPATH - " \
                          + self._event_point_of_contact_email_text_value_locator + err.message)


    # Scroll
    @property
    def get_event_map_scroll(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._event_map_scroll)))
            return self.driver.find_element_by_xpath(self._event_map_scroll)
        except Exception, err:
            raise type(err)("Accordian main scroll bar - searched XPATH - " + self._event_map_scroll + err.message)


    def return_to_apps_main_page(self):
        """
        Description : This function will helps to go back to events page.
        Revision:
        :return: None
        """
        if not self.get_event_create_event:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                    (By.LINK_TEXT, self._event_link_locator))).click()
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self._event_create_event)))
            except:
                inspectstack = inspect.stack()[1][3]
                self.recoverapp(inspectstack)

    def recoverapp(self, inspectstack):
        """
        Description : This function helps to go back to events page. Inspect stack prints the test name from which
                                 this function is called.
        Revision:
        :return: None
        """
        print ("Application recovering called from " + inspectstack)
        basepage = BasePage(self.driver)
        basepage.accessURL()
        iconlistpage = IconListPage(self.driver)
        iconlistpage.click_events_icon()

    def app_sanity_check(self):
        """
        Description : This function should be called before any test to see the event page is displayed.
        Revision:
        :return: None
        """
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._event_create_event)))
        except:
            inspectstack = inspect.stack()[1][3]
            self.recoverapp(inspectstack)

    def get_select_checkbox_in_grid(self):
        """
        Description : This function will select the checkbox from the event list..
        Revision:
        :return: None
        """
        events_checkbox = self.basepage.findElementsByXpath(self._event_list_check_box_locator)
        for event_checkbox in events_checkbox:
            event_checkbox.click()

        for event_checkbox in events_checkbox:
            event_checkbox.click()

    def get_total_row_count(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._event_select_action_delete_select_xpath_locator)))
        countText = (self.driver.find_element_by_id("eventsTable_info").text).encode('utf-8').split('\n')[2].strip()
        splitedText = countText.split(" ")
        totalCount = splitedText[5]
        return int(totalCount)

    def event_create_click(self):
        """
        Description : This function will click on Create Event Link.
        Revision:
        :return: None
        """
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self._event_select_action_delete_select_xpath_locator)))
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, self._event_create_event))).click()

    def get_eventdata(self):
        with open(eventData) as data_file:
            for each in json.load(data_file):
                self.event_name = each["event_name"]
                self.event_start_date = each["event_start_date"]
                self.event_end_date = each["event_end_date"]
                self.event_type = each["event_type"]
                self.event_venue = each["event_venue"]
                self.event_tag = each["event_tag"]

    def create_event(self):
        """
        Description : This function will enter event data.
        Revision:
        :return: None
        """

        # Click on Create Event Icon
        self.event_create_click()

        # Click on Event title, so that the pop-up will disappear
        self.get_event_title_click.click()
        # Enter the values

        self.enter_event_type_name.send_keys(self.event_name)
        self.enter_event_type_start_date.send_keys(self.event_start_date)
        self.enter_event_type_end_date.send_keys(self.event_end_date)
        self.get_event_type_drop_down.click()
        self.get_event_newtype_text_box.send_keys(self.event_type)
        self.get_event_type_add_button.click()
        self.enter_event_type_venue.send_keys(self.event_venue)
        self.enter_event_type_tag.send_keys(self.event_tag)
        self.get_event_type_tag_add_button.click()
        self.get_event_type_save_add_button.click()

    def textbox_clear(self, textboxlocator):
        """
        Description : This function will clear search text box.
        Revision:
        :return: None
        """
        textboxlocator.clear()

    def event_search_eventname(self, name):
        """
        Description : This function will enter string in search text box.
        Revision:
        :return: None
        """
        search_textbox = self.basepage.findElementByXpath(self._event_search_textbox_locator)
        self.textbox_clear(search_textbox)
        search_textbox.send_keys(name)

    def select_event_type(self, event_type_name1):
        """
        Description : This function will select an event from event list.
        Revision:
        :return: None
        """
        try:
            self.event_search_eventname(event_type_name1)
            sleep(6)
            event_list = self.get_events_name_list
            if len(event_list)>=1:
                for i in event_list:
                    if i.text == event_type_name1:
                        i.click()
                        sleep(5)#Mandatory. event page is taking more time to load.
                        break
            else:
                sleep(4)
                self.event_search_eventname("")
                sleep(2)
                self.create_event()
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                        (By.XPATH, self._event_name_breadcrumb)))
        except Exception, err:
            raise type(err)("No event is existing or event Creation has been failed. "+err.message)

    def set_value_textbox(self, xpath, value):
        self.basepage.findElementByXpath(xpath).clear()
        self.basepage.findElementByXpath(xpath).send_keys(value)
    
    def delete_existing_contact(self):
        """
        Description : This function will delete existing contact.
        Revision:
        :return: None
        """
        try:
            while(self.get_event_newcontact_delete_icon.is_displayed()):
                self.get_event_newcontact_delete_icon.click()
                self.get_event_newcontact_delete_popup_delete_button.click()
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
        self.get_event_points_of_contact_header.click()
        self.get_event_add_contact_button.click()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element((By.XPATH,
                                                  self._events_points_of_contact_title_locator), "Contact information"))
        self.get_event_newcontact_firstname_textbox.clear()# Fill all fields.
        self.get_event_newcontact_firstname_textbox.send_keys(firstname)
        self.get_event_newcontact_lastname_textbox.clear()
        self.get_event_newcontact_lastname_textbox.send_keys(lastname)
        self.get_event_newcontact_prefix_textbox.clear()
        self.get_event_newcontact_prefix_textbox.send_keys(prefix)
        self.get_event_newcontact_title_textbox.clear()
        self.get_event_newcontact_title_textbox.send_keys(title)
        self.get_event_newcontact_address1_textbox.clear()
        self.get_event_newcontact_address1_textbox.send_keys(address1)
        self.get_event_newcontact_address2_textbox.clear()
        self.get_event_newcontact_address2_textbox.send_keys(address2)
        self.get_event_newcontact_city_textbox.clear()
        self.get_event_newcontact_city_textbox.send_keys(city)
        self.get_event_newcontact_state_textbox.clear()
        self.get_event_newcontact_state_textbox.send_keys(state)
        self.get_event_newcontact_zip_textbox.clear()
        self.get_event_newcontact_zip_textbox.send_keys(zip)
        self.get_event_newcontact_phone_textbox.clear()
        self.get_event_newcontact_phone_textbox.send_keys(phone)
        self.get_event_newcontact_email_textbox.clear()
        self.get_event_newcontact_email_textbox.send_keys(email)
        sleep(4)
        self.get_event_newcontact_save_button.click()#Click on Save Button.
        WebDriverWait(self.driver,100).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                        self._event_header_save_text_locator), "Saved"))

    def multiple_contact_create(self):
        """
        Description : This function will create multiple contacts.
        Revision:
        :return: None
        """
        self.delete_existing_contact()
        firstname = ['jkl','vwx','def','pqr']
        lastname = ['mno','abc','stu','ghi']
        phonelist = [r'661-111-1111',r'222-222-2222',r'433-333-3333',r'123-444-4444']
        emaillist = [r'stu@vwx',r'abc@def',r'mno@pqr',r'ghi@jkl']
        titlelist = ['HH','ZZ','CC','PP']
        for contact in range(4):
            self.create_new_contact(firstname[contact],lastname[contact],titlelist[contact],phonelist[contact],
                                    emaillist[contact])
            sleep(2) #required to update apps.
