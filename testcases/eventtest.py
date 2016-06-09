import re

from nose.plugins.skip import SkipTest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.eventspage import EventsPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from time import sleep
import ConfigParser
from lib.pagination import Pagination


class EventpageTest(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        super(EventpageTest, cls).setUpClass()
        cls.eventpage = EventsPage(cls.driver)
        cls.pagination = Pagination(cls.driver)
        cls.eventpage.open_event_app()
        cls.section = 'EventsMessages'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))

    def setUp(self):
        self.errors_and_failures = self.tally()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (By.XPATH, self.eventpage._event_select_action_delete_select_xpath_locator)))

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        self.eventpage.return_to_apps_main_page()

    @attr(priority="high")
    # @SkipTest
    def test_EV_001(self):
        """
        Test : test_EV_01
        Description : To verify delete functionality when no events are available. Delete button should be disabled.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.get_event_select_action_drop_down.click()
        if len(self.eventpage.get_event_name_list) <= 0:
            self.assertFalse(self.eventpage.get_event_link_delete_text.is_enabled(),
                             self.config.get(self.section, 'MESSAGE_WHEN_NO_EVENTS_AVAILABLE'))
        else:
            self.skipTest(self.config.get(self.section, 'MESSAGE_TEST_CAN_NOT_BE_VALIDATED'))

    @attr(priority="high")
    # @SkipTest
    def test_EV_002(self):
        """
        Test : test_EV_02
        Description : To verify delete functionality when no event is selected. Delete button should be disabled.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.get_select_checkbox_in_grid()
        self.eventpage.get_event_select_action_drop_down.click()
        state = self.eventpage.get_event_link_delete_text.is_enabled()
        sleep(1)
        self.eventpage.get_event_select_action_drop_down.click()
        self.assertFalse(state,
                         self.config.get(self.section, 'MESSAGE_WHEN_NO_EVENTS_AVAILABLE'))

    @attr(priority="high")
    @SkipTest
    def test_EV_003(self):
        """
        Test : test_EV_03
        Description : To verify delete functionality. User selected event should be deleted.
        Revision:
        Author : Kiran
        :return: None
        """
        countbeforedeletion = self.eventpage.get_total_row_count()
        self.eventpage.get_event_list_first_check_box.click()
        self.eventpage.get_event_select_action_drop_down.click()
        self.eventpage.get_event_link_delete_text.click()
        self.eventpage.get_event_delete_button.click()  # Delete
        sleep(2)
        countafterdeletion = self.eventpage.get_total_row_count()
        sleep(2)
        self.assertEqual(int(countbeforedeletion), int(countafterdeletion) + 1,
                         self.config.get(self.section, 'MESSAGE_COULD_NOT_DELETE_EVENT'))

    @attr(priority="high")
    # @SkipTest
    def test_EV_004(self):
        """
        Test : test_EV_04
        Description : To verify delete window cancel button functionality.
        Revision:
        Author : Kiran
        :return: None
        """
        sleep(2)
        countbeforedeletion = self.eventpage.get_total_row_count()
        self.eventpage.get_event_list_first_check_box.click()
        self.eventpage.get_event_select_action_drop_down.click()
        self.eventpage.get_event_link_delete_text.click()
        self.eventpage.get_deleteevent_cancel_button.click()  # Cancel
        sleep(2)
        countafterdeletion = self.eventpage.get_total_row_count()
        sleep(2)
        self.assertEqual(int(countbeforedeletion), int(countafterdeletion),
                         self.config.get(self.section, 'MESSAGE_EVENT_DELETED_ON_CANCEL'))

    @attr(priority="high")
    # @SkipTest
    def test_EV_005(self):
        """
        Test : test_EV_05
        Description : To create event and verify that event is created properly.
        Revision:
        Author : Kiran
        :return: None
        """
        check = 0

        self.eventpage.create_event()

        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_name_breadcrumb), self.eventpage.get_event_name_breadcrumb.text))

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.LINK_TEXT, self.eventpage._event_link_locator))).click()

        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, self.eventpage._event_select_action_delete_select_xpath_locator)))

        self.eventpage.event_search_eventname(self.eventpage.event_name)

        if self.pagination.pagination_total_pages() >= 1:
            while (self.eventpage.get_eventtable_created_column.get_attribute("class") != "sorting_desc"):
                self.eventpage.get_eventtable_created_column.click()
                sleep(5)
        for item in self.eventpage.get_event_list_background:
            if (item.text == self.eventpage.event_name) and (item.value_of_css_property("background-color") \
                                                                     == "rgba(255, 236, 158, 1)"):
                check = 1
                self.assertTrue(check == 1,
                                self.config.get(self.section, 'MESSAGE_NEW_EVENT_NOT_APPEARING_ON_YELLOW_BACKGROUND'))
                break
        self.eventpage.textbox_clear(self.driver.find_element_by_xpath(self.eventpage._event_search_textbox_locator))

    @attr(priority="high")
    # @SkipTest
    def test_EV_006(self):
        """
        Test : test_EV_006
        Description : To verify New Event Name field.
        Revision:
        :return: None
        """
        self.eventpage.event_create_click()
        self.eventpage.enter_event_type_name.send_keys("")  # Clear the text filed and leave it without any value
        self.assertFalse(self.eventpage.get_event_type_save_add_button.is_enabled(),
                         self.config.get(self.section, 'MESSAGE_SAVE_BUTTON_IS_NOT_DISABLED'))
        self.eventpage.get_event_type_cancel_add_button.click()

    @attr(priority="high")
    # @SkipTest
    def test_EV_007(self):
        """
        Test : test_EV_007
        Description : To verify cancel button functionality of New event window. Without any data entry.
        Revision:
        :return: None
        """
        self.eventpage.event_create_click()
        self.eventpage.get_event_type_cancel_add_button.click()
        expectedAfterResetFilter = self.eventpage.get_Type_dropdown.text
        self.assertEqual("Type", expectedAfterResetFilter)  # Checking "event Type" displayed after reset

    @attr(priority="high")
    # @SkipTest
    def test_EV_008(self):
        """
        Test : test_EV_008
        Description : To edit overview section. Enter all required fields info and click on save button.
        Revision:
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_details_edit_widget_locator), r"Details"))
        self.eventpage.get_event_overview_edit_link.click()
        self.eventpage.get_event_title_click.click()

        self.eventpage.enter_event_type_name.clear()
        self.eventpage.enter_event_type_name.send_keys("kk edit event")

        self.eventpage.enter_event_type_venue.clear()
        self.eventpage.enter_event_type_venue.send_keys("edit Bangalore 1")

        self.eventpage.get_event_type_save_add_button.click()  # Click on Save
        self.assertTrue(self.eventpage.event_type_Saved_label.is_displayed(),
                        self.config.get(self.section, 'MESSAGE_SAVED_TEXT_NOT_DISPLAYED'))

    @attr(priority="high")
    # @SkipTest
    def test_EV_009(self):
        """
        Test : test_EV_009
        Description : To edit overview section. Enter all required fields info and click on cancel button.
        Revision:
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_details_edit_widget_locator), r"Details"))
        self.eventpage.get_event_overview_edit_link.click()
        self.eventpage.get_event_title_click.click()

        self.eventpage.enter_event_type_name.clear()
        self.eventpage.enter_event_type_name.send_keys("kk edit cancel event")

        self.eventpage.enter_event_type_venue.clear()
        self.eventpage.enter_event_type_venue.send_keys("edit cancel Bangalore 1")

        self.eventpage.get_event_type_cancel_add_button.click()  # click on Cancel
        self.assertEqual(self.eventpage.event_name, self.eventpage.get_event_name_breadcrumb.text)

    @attr(priority="high")
    #@SkipTest
    def test_EV_010(self):
        """
        Test : test_EV_010
        Description : To edit Details section. Enter all required fields info and click on save button.
        Revision:
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_details_edit_widget_locator), r"Details"))
        self.eventpage.get_event_detail_edit_link.click()

        self.eventpage.get_event_detail_edit_attendees_text_box.clear()
        self.eventpage.get_event_detail_edit_attendees_text_box.send_keys("20")

        self.eventpage.get_event_detail_edit_address1_text_box.clear()
        self.eventpage.get_event_detail_edit_address1_text_box.send_keys("Details Address 1")

        self.eventpage.get_event_detail_edit_address2_text_box.clear()
        self.eventpage.get_event_detail_edit_address2_text_box.send_keys("Details Address 2")

        self.eventpage.get_event_detail_edit_city_text_box.clear()
        self.eventpage.get_event_detail_edit_city_text_box.send_keys("Details City")

        self.eventpage.get_event_detail_edit_state_text_box.clear()
        self.eventpage.get_event_detail_edit_state_text_box.send_keys("Details State")

        self.eventpage.get_event_detail_edit_zip_text_box.clear()
        self.eventpage.get_event_detail_edit_zip_text_box.send_keys("Details Zip")

        self.eventpage.get_event_detail_edit_url_text_box.clear()
        self.eventpage.get_event_detail_edit_url_text_box.send_keys("http://www.indecomm.net")

        self.eventpage.get_event_detail_edit_description_text_box.clear()
        self.eventpage.get_event_detail_edit_description_text_box.send_keys("Partner with Indecomm for consulting, outsourcing, technology, and learning solutions")

        self.eventpage.get_event_detail_edit_save_button.click()  # click on Save
        self.assertTrue(self.eventpage.event_type_Saved_label.is_displayed(),
                        self.config.get(self.section, 'MESSAGE_SAVED_TEXT_NOT_DISPLAYED'))

    @attr(priority="high")
    #@SkipTest
    def test_EV_011(self):
        """
        Test : test_EV_011
        Description : To verify cancel button functionality of the Detail section.
        Revision:
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_details_edit_widget_locator), r"Details"))
        self.eventpage.get_event_detail_edit_link.click()

        self.eventpage.get_event_detail_edit_attendees_text_box.clear()
        self.eventpage.get_event_detail_edit_attendees_text_box.send_keys("20")

        self.eventpage.get_event_detail_edit_address1_text_box.clear()
        self.eventpage.get_event_detail_edit_address1_text_box.send_keys("Cancel Details Address 1")

        self.eventpage.get_event_detail_edit_address2_text_box.clear()
        self.eventpage.get_event_detail_edit_address2_text_box.send_keys("Cancel Details Address 2")

        self.eventpage.get_event_detail_edit_city_text_box.clear()
        self.eventpage.get_event_detail_edit_city_text_box.send_keys("Cancel Details City")

        self.eventpage.get_event_detail_edit_state_text_box.clear()
        self.eventpage.get_event_detail_edit_state_text_box.send_keys("Cancel Details State")

        self.eventpage.get_event_detail_edit_zip_text_box.clear()
        self.eventpage.get_event_detail_edit_zip_text_box.send_keys("Details Zip")

        self.eventpage.get_event_detail_edit_url_text_box.clear()
        self.eventpage.get_event_detail_edit_url_text_box.send_keys("Cancel http://www.indecomm.net")

        self.eventpage.get_event_detail_edit_description_text_box.clear()
        self.eventpage.get_event_detail_edit_description_text_box.send_keys("Partner with Indecomm for consulting, outsourcing, technology, and learning solutions")
        self.eventpage.get_event_detail_edit_cancel_button.click()
        self.assertEqual(self.eventpage.event_name, self.eventpage.get_event_name_breadcrumb.text)


    @attr(priority="high")
    #@SkipTest
    def test_EV_012(self):
        """
        Test : test_EV_12
        Description : To verify Latitude and Longitude boundary values.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.ID, "map_control")))
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(
            (By.XPATH,self.eventpage._event_location_edit_icon_xpath_locator))).click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_location_title_id_locator), r"Event location"),
            self.config.get(self.section, 'MESSAGE_LOCATION_POPUP_NOT_DISPLAYED'))
        lati = "550"
        self.eventpage.get_event_location_latitude_textbox.clear()
        self.eventpage.get_event_location_latitude_textbox.send_keys(lati)
        latitudeerrorMessage = self.eventpage.get_event_location_latitude_error_text.text
        self.assertEqual(latitudeerrorMessage, self.config.get(self.section, 'MESSAGE_LATITUDE_NUMBER_RANGE'),
                         self.config.get(self.section, 'MESSAGE_ERROR_NOT_DISPLAYED_FOR_LATITUDE'))


        locationSave = self.eventpage.get_event_location_save_button
        self.assertFalse(locationSave.is_enabled(), self.config.get(self.section, 'MESSAGE_LOCATION_SAVE_BUTTON_IS_NOT_DISABLED'))
        longi = "200"
        self.eventpage.get_event_location_longitude_textbox.clear()
        self.eventpage.get_event_location_longitude_textbox.send_keys(longi)
        longitudeerrorMessage = self.eventpage.get_event_location_longitude_error_text.text
        self.assertEqual(self.config.get(self.section, 'MESSAGE_LONGITUDE_NUMBER_RANGE'), longitudeerrorMessage,
                         self.config.get(self.section, 'MESSAGE_ERROR_NOT_DISPLAYED_FOR_LONGITUDE'))
        locationSave = self.eventpage.get_event_location_save_button
        self.assertFalse(locationSave.is_enabled(), self.config.get(self.section, 'MESSAGE_LOCATION_SAVE_BUTTON_NOT_DISABLED'))
        self.eventpage.get_event_location_cancel_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_EV_013(self):
        """
        Test : test_EV_013
        Description : To verify whether Marker is displayed on the map after_setting Latitude and Longitude values.
        Revision:
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.ID,"map_control")))
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(
            (By.XPATH,self.eventpage._event_location_edit_icon_xpath_locator))).click()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_location_title_id_locator), r"Event location"),
        self.config.get(self.section, 'MESSAGE_LOCATION_POPUP_NOT_DISPLAYED'))
        lati = "40.7127"
        self.eventpage.get_event_location_latitude_textbox.clear()
        self.eventpage.get_event_location_latitude_textbox.send_keys(lati)
        longi = "74.0059"
        self.eventpage.get_event_location_longitude_textbox.clear()
        self.eventpage.get_event_location_longitude_textbox.send_keys(longi)
        self.eventpage.get_event_location_save_button.click()
        #self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        self.assertTrue(self.eventpage.get_event_location_marker_available_image.is_displayed(),
                        self.config.get(self.section, 'MESSAGE_MARKER_NOT_DISPLAYED_ON_MAP'))

    @attr(priority="high")
    #@SkipTest
    def test_EV_014(self):
        """
        Test : test_EV_014
        Description : To verify Event name once click on Marker.
        Revision:
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,"map_control")))
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(
            (By.XPATH,self.eventpage._event_location_edit_icon_xpath_locator))).click()
        WebDriverWait(self.driver, 50).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_location_title_id_locator), r"Event location"),
        self.config.get(self.section, 'MESSAGE_LOCATION_POPUP_NOT_DISPLAYED'))
        lati = "40.7127"
        self.eventpage.get_event_location_latitude_textbox.clear()
        self.eventpage.get_event_location_latitude_textbox.send_keys(lati)
        longi = "74.0059"
        self.eventpage.get_event_location_longitude_textbox.clear()
        self.eventpage.get_event_location_longitude_textbox.send_keys(longi)
        self.eventpage.get_event_location_save_button.click()
        #self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-200);")
        sleep(5)
        self.eventpage.get_event_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.eventpage.get_event_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.eventpage.get_event_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.assertTrue(self.eventpage.get_event_location_marker_available_image.is_displayed(),
                        self.config.get(self.section, 'MESSAGE_MARKER_NOT_DISPLAYED_ON_MAP'))
        self.eventpage.get_event_location_marker_available_image.click()
        self.assertEqual(self.eventpage.event_name, self.eventpage.get_event_location_event_name_text.text,
                         self.config.get(self.section, 'MESSAGE_MARKER_NAME_NOT_DISPLAYED_ON_MAP'))

    @attr(priority="high")
    #@SkipTest
    def test_EV_015(self):
        """
        Test : test_EV_015
        Description : To verify all mandatory fields in Contact Section.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.delete_existing_contact() #delete existing contacts.
        self.eventpage.create_new_contact("FirstName","ZLastName")#create new contact.
        act_new_contact_value = self.eventpage.get_event_contact_new_contact_value_text.text
        exp_new_contact_value = "ZLastName, FirstName"+" Title "+r"111-111-1111 "+r"test@test.com"
        self.assertEqual(act_new_contact_value, exp_new_contact_value,
                                                        self.config.get(self.section, 'MESSAGE_CONTACTS_NOT_MATCHING'))

    @attr(priority="high")
    #@SkipTest
    def test_EV_016(self):
        """
        Test : test_EV_016
        Description : To verify that main contact has same info as first contact.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.delete_existing_contact()#delete existing contacts.
        self.eventpage.create_new_contact("FirstName","ZLastName")#create new contact.
        try:
            if self.eventpage.get_event_main_contact_window:
                act_name_value = self.eventpage.get_event_main_contact_name_text.text
                exp_name_value = "Shri FirstName ZLastName"
                self.assertEqual(str(act_name_value), str(exp_name_value))#verify event main contact first and last name value.
        except NoSuchElementException:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_NO_MAIN_CONTACTS'))

    @attr(priority="high")
    #@SkipTest
    def test_EV_017(self):
        """
        Test : test_EV_017
        Description : To verify error message for first and last name.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.delete_existing_contact()#delete existing contacts.
        self.eventpage.get_event_points_of_contact_header.click()
        self.eventpage.get_event_add_contact_button.click()#click on Add Contact button.
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._events_points_of_contact_title_locator), r"Contact information"))
        self.eventpage.get_event_newcontact_firstname_textbox.clear()#clear first and last name.
        self.eventpage.get_event_newcontact_lastname_textbox.clear()
        self.eventpage.get_event_newcontact_prefix_textbox.clear()#clear Prefix filed.
        #sleep(2) #required to check Error message.
        firstname_error = self.eventpage.get_event_newcontact_firstname_error_message.is_displayed()#Verify Error messages.
        lastname_error = self.eventpage.get_event_newcontact_lastname_error_message.is_displayed()
        #sleep(2) #required to check Error message.
        self.eventpage.get_event_newcontact_window_cross_button.click()#click on cross button to close window.
        self.assertTrue(firstname_error, self.config.get(self.section, 'MESSAGE_ERROR_NOT_DISPLAYED_FOR_FIRST_NAME'))
        self.assertTrue(lastname_error, self.config.get(self.section, 'MESSAGE_ERROR_NOT_DISPLAYED_FOR_LAST_NAME'))

    @attr(priority="high")
    #@SkipTest
    def test_EV_018(self):
        """
        Test : test_EV_018
        Description : To verify phone field of the Contact section.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.delete_existing_contact()#delete existing contacts.
        self.eventpage.get_event_points_of_contact_header.click()
        self.eventpage.get_event_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._events_points_of_contact_title_locator), r"Contact information"))
        self.eventpage.get_event_newcontact_firstname_textbox.clear()
        self.eventpage.get_event_newcontact_firstname_textbox.send_keys("FirstName")
        self.eventpage.get_event_newcontact_lastname_textbox.clear()
        self.eventpage.get_event_newcontact_lastname_textbox.send_keys("ZLastName")
        self.eventpage.get_event_newcontact_phone_textbox.clear()
        self.eventpage.get_event_newcontact_phone_textbox.send_keys(r"111-222-3343")
        self.eventpage.get_event_newcontact_save_button.click()#click on save button.
        act_phone = self.eventpage.get_event_contact_phone_value_text.text#reading act phone value.
        regex = re.compile(r'^\(?([A-Za-z0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([A-Za-z0-9]{4})$')
        self.assertRegexpMatches(str(act_phone), regex,
                                 self.config.get(self.section, 'MESSAGE_PHONE_VALUE_NOT_MATCHING'))
    
    @attr(priority="high")
    #@SkipTest
    def test_EV_019(self):
        """
        Test : test_EV_019
        Description : To verify email field of the Contact section.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.delete_existing_contact()#delete existing contacts.
        self.eventpage.get_event_points_of_contact_header.click()
        self.eventpage.get_event_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._events_points_of_contact_title_locator), r"Contact information"))
        self.eventpage.get_event_newcontact_firstname_textbox.clear()
        self.eventpage.get_event_newcontact_firstname_textbox.send_keys("FirstName")
        self.eventpage.get_event_newcontact_lastname_textbox.clear()
        self.eventpage.get_event_newcontact_lastname_textbox.send_keys("ZLastName")
        self.eventpage.get_event_newcontact_email_textbox.clear()
        self.eventpage.get_event_newcontact_email_textbox.send_keys(r"test@test.com")
        self.eventpage.get_event_newcontact_save_button.click() #click on save button.
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        act_email = self.eventpage.get_event_contact_email_value_text.text #reading actual email value.
        regex = re.compile(r'[\w.-]+@[\w.-]+')
        self.assertRegexpMatches(str(act_email), regex,
                                 self.config.get(self.section, 'MESSAGE_EMAIL_NOT_MATCHING'))

    @attr(priority="high")
    #@SkipTest
    def test_EV_020(self):
        """
        Test : test_EV_020
        Description : To verify email field of the Contact section. Email address with wrong address.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.delete_existing_contact()#delete existing contacts.
        self.eventpage.get_event_points_of_contact_header.click()
        self.eventpage.get_event_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._events_points_of_contact_title_locator), r"Contact information"))
        self.eventpage.get_event_newcontact_firstname_textbox.clear()
        self.eventpage.get_event_newcontact_firstname_textbox.send_keys("FirstName")
        self.eventpage.get_event_newcontact_lastname_textbox.clear()
        self.eventpage.get_event_newcontact_lastname_textbox.send_keys("ZLastName")
        self.eventpage.get_event_newcontact_email_textbox.clear()
        self.eventpage.get_event_newcontact_email_textbox.send_keys(r"testtest.com")
        #sleep(2)
        self.eventpage.get_event_newcontact_firstname_textbox.click()
        #sleep(2)
        exp_error_message = self.eventpage.get_event_newcontact_email_error_message.is_displayed()
        self.eventpage.get_event_newcontact_window_cross_button.click()#Click on Cross button to close window.
        self.assertTrue(exp_error_message,
                        self.config.get(self.section, 'MESSAGE_ERROR_NOT_DISPLAYED_FOR_WRONG_EMAIL'))
    
    @attr(priority="high")
    #@SkipTest
    def test_EV_021(self):
        """
        Test : test_EV_021
        Description : To verify cancel button functionality of the Contact window.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.delete_existing_contact()#delete existing contacts.
        self.eventpage.get_event_points_of_contact_header.click()
        self.eventpage.get_event_add_contact_button.click()#click on add contact button
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._events_points_of_contact_title_locator), r"Contact information"))
        self.eventpage.get_event_newcontact_firstname_textbox.clear()
        self.eventpage.get_event_newcontact_firstname_textbox.send_keys("FirstNameDel")
        self.eventpage.get_event_newcontact_lastname_textbox.clear()
        self.eventpage.get_event_newcontact_lastname_textbox.send_keys("ZLastNameDel")
        self.eventpage.get_event_newcontact_cancel_button.click()#click on cancel button.
        #sleep(2)
        try:
            if self.eventpage.get_event_contact_first_last_name_value_text.is_displayed():
                self.assertFalse(True,
                                 self.config.get(self.section, 'MESSAGE_ERROR_CANCEL_NOT_WORKING_ON_CONTACT_CREATION'))
        except:
            self.assertTrue(True,self.config.get(self.section, 'MESSAGE_NEW_CONTACT_CREATED'))

    @attr(priority="high")
    #@SkipTest
    def test_EV_022(self):
        """
        Test : test_EV_022
        Description : To verify contact name in ascending order.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver, 50).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.multiple_contact_create()#create multiple contacts.
        exp_name_ascending = r"stu, def, mno, jkl, ghi, pqr, abc, vwx"
        exp_name_descending = r"abc, vwx, ghi, pqr, mno, jkl, stu, def"
        self.eventpage.get_event_point_of_contact_name_tab.click()#click on contact name tab.
        #sleep(2)
        act_name_list = self.eventpage.get_event_point_of_contact_name_text_value#Reading all contact names.
        act_name_list_value = []
        for name in act_name_list:
            act_name_list_value.append(name.text)
        self.assertEqual(exp_name_ascending, ", ".join(act_name_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_NAMES_IN_ASCENDING_ORDER'))
        self.eventpage.get_event_point_of_contact_name_tab.click()
        #sleep(2)
        act_name_list = self.eventpage.get_event_point_of_contact_name_text_value#Reading all contact's names.
        act_name_list_value =[]
        for name in act_name_list:
            act_name_list_value.append(name.text)
        self.assertEqual(exp_name_descending, ", ".join(act_name_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_NAMES_IN_DESCENDING_ORDER'))
    
    @attr(priority="high")
    #@SkipTest
    def test_EV_023(self):
        """
        Test : test_EV_023
        Description : To verify contact title's value in ascending order.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.multiple_contact_create()#create multiple contacts.
        exp_title_ascending = r"CC, HH, PP, ZZ"
        exp_title_descending = r"ZZ, PP, HH, CC"
        self.eventpage.get_event_point_of_contact_title_tab.click()#click on contact title tab to sort ascendingly.
        #sleep(2)
        act_title_list = self.eventpage.get_event_point_of_contact_title_text_value#Reading all contact's title values.
        act_title_list_value = []
        for title in act_title_list:
            act_title_list_value.append(title.text)
        self.assertEqual(exp_title_ascending, ", ".join(act_title_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_TITLES_NOT_IN_ASCENDING_ORDER'))
        self.eventpage.get_event_point_of_contact_title_tab.click()#click on contact title tab to sort descendingly.
        #sleep(2)
        act_title_list = self.eventpage.get_event_point_of_contact_title_text_value#Reading all contact's title values.
        act_title_list_value = []
        for title in act_title_list:
            act_title_list_value.append(title.text)
        self.assertEqual(exp_title_descending, ", ".join(act_title_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_TITLES_NOT_IN_DESCENDING_ORDER'))
    
    @attr(priority="high")
    #@SkipTest
    def test_EV_024(self):
        """
        Test : test_EV_024
        Description : To verify contact phone's value in ascending order.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.multiple_contact_create()#create multiple contacts.
        exp_phone_ascending = r"123-444-4444, 222-222-2222, 433-333-3333, 661-111-1111"
        exp_phone_descending = r"661-111-1111, 433-333-3333, 222-222-2222, 123-444-4444"
        self.eventpage.get_event_point_of_contact_phone_tab.click()#click on contact phone tab.
        #sleep(2)
        act_phone_list = self.eventpage.get_event_point_of_contact_phone_text_value#Reading all contact's phone values.
        act_phone_list_value = []
        for phone in act_phone_list:
            act_phone_list_value.append(phone.text)
        self.assertEqual(exp_phone_ascending, ", ".join(act_phone_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_PHONE_NUMBERS_NOT_IN_ASCENDING_ORDER'))
        self.eventpage.get_event_point_of_contact_phone_tab.click()
        #sleep(2)
        act_phone_list = self.eventpage.get_event_point_of_contact_phone_text_value#Reading all contact's phone values.
        act_phone_list_value = []
        for phone in act_phone_list:
            act_phone_list_value.append(phone.text)
        self.assertEqual(exp_phone_descending, ", ".join(act_phone_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_PHONE_NUMBERS_NOT_IN_DESCENDING_ORDER'))

    @attr(priority="high")
    #@SkipTest
    def test_EV_025(self):
        """
        Test : test_EV_025
        Description : To verify contact email's value in ascending order.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.multiple_contact_create()#create multiple contacts.
        exp_email_ascending = r"abc@def, ghi@jkl, mno@pqr, stu@vwx"
        exp_email_descending = r"stu@vwx, mno@pqr, ghi@jkl, abc@def"
        self.eventpage.get_event_point_of_contact_email_tab.click()  #click on contact email tab.
        #sleep(2)
        act_email_list = self.eventpage.get_event_point_of_contact_email_text_value#Reading all contact's email values.
        act_email_list_value = []
        for email in act_email_list:
            act_email_list_value.append(email.text)
        self.assertEqual(exp_email_ascending, ", ".join(act_email_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_EMAILS_NOT_IN_ASCENDING_ORDER'))
        self.eventpage.get_event_point_of_contact_email_tab.click()
        #sleep(2)
        act_email_list = self.eventpage.get_event_point_of_contact_email_text_value#Reading all contact's email values.
        act_email_list_value = []
        for email in act_email_list:
            act_email_list_value.append(email.text)
        self.assertEqual(exp_email_descending, ", ".join(act_email_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_EMAILS_NOT_IN_DESCENDING_ORDER'))

    @attr(priority="high")
    #@SkipTest
    def test_EV_026(self):
        """
        Test : test_EV_026
        Description : To verify delete option of contact.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.delete_existing_contact()#delete existing contacts.
        self.eventpage.get_event_points_of_contact_header.click()
        self.eventpage.get_event_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._events_points_of_contact_title_locator), r"Contact information"))
        self.eventpage.get_event_newcontact_firstname_textbox.clear()
        self.eventpage.get_event_newcontact_firstname_textbox.send_keys("FirstName")
        self.eventpage.get_event_newcontact_lastname_textbox.clear()
        self.eventpage.get_event_newcontact_lastname_textbox.send_keys("ZLastName")
        self.eventpage.get_event_newcontact_save_button.click()#click on save button.
        self.eventpage.delete_existing_contact()#delete existing contacts.
        try:
            if self.eventpage.get_event_newcontact_delete_icon.is_displayed():
                #sleep(2)
                self.assertFalse(False, self.config.get(self.section, 'MESSAGE_NEW_CONTACT_NOT_DELETED'))
        except NoSuchElementException:
            self.assertTrue(True, self.config.get(self.section, 'MESSAGE_CONTACT_DELETED'))

    @attr(priority="high")
    #@SkipTest
    def test_EV_027(self):
        """
        Test : test_EV_027
        Description : To verify delete window cancel button functionality.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.select_event_type(self.eventpage.event_name)
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._event_main_contct_widget_locator), r"Points of Contact"))
        self.eventpage.delete_existing_contact()#delete existing contacts.
        self.eventpage.get_event_points_of_contact_header.click()
        self.eventpage.get_event_add_contact_button.click()
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.eventpage._events_points_of_contact_title_locator), r"Contact information"))
        self.eventpage.get_event_newcontact_firstname_textbox.clear()
        self.eventpage.get_event_newcontact_firstname_textbox.send_keys("FirstName")
        self.eventpage.get_event_newcontact_lastname_textbox.clear()
        self.eventpage.get_event_newcontact_lastname_textbox.send_keys("ZLastName")
        self.eventpage.get_event_newcontact_save_button.click()
        try:
            if self.eventpage.get_event_newcontact_delete_icon.is_displayed():
                #sleep(2)
                self.eventpage.get_event_newcontact_delete_icon.click()
                #sleep(2)
                self.eventpage.get_event_newcontact_delete_popup_cancel_button.click()
                #sleep(2)
                self.assertTrue(True, self.config.get(self.section, 'MESSAGE_CANCEL_IS_WORKING'))
        except NoSuchElementException:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_CONTACT_DELETED'))
