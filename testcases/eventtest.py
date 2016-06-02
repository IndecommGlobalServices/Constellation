from nose.plugins.skip import SkipTest
from selenium.webdriver.common.by import By
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
        Description : To verify delete functionality when no asset is selected. Delete button should be disabled.
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
        Description : To verify delete functionality. User selected asset should be deleted.
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
        self.assertEqual("Type", expectedAfterResetFilter)  # Checking "Asset Type" displayed after reset

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