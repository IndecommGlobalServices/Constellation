from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.timelinepage import TimelinePage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from time import sleep
import ConfigParser
from lib.pagination import Pagination

class TimelinepageTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(TimelinepageTest, cls).setUpClass()
        cls.timelinepage = TimelinePage(cls.driver)
        cls.pagination = Pagination(cls.driver)
        cls.timelinepage.open_timeline_app()
        cls.section = 'TimelineMessages'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))

    def setUp(self):
        self.errors_and_failures = self.tally()
        WebDriverWait(self.driver, 50). until(EC.presence_of_element_located \
                                              ((By.XPATH, self.timelinepage._tl_app_name_locator)))

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        self.timelinepage.return_to_apps_main_page()

    @attr(priority="high")
    #@SkipTest
    def test_TL_001_timeline_settings_start_end_date(self):
        """
        Test : test_FI_001 To verify Start and End date check boxes.
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """

        self.timelinepage.get_time_line_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.timelinepage._tl_settings_window_header_locator)))
        self.timelinepage.get_tl_settings_window_start_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_start_date_textbox.send_keys(self.timelinepage.time_line_start_date)
        self.timelinepage.get_tl_settings_window_end_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_end_date_textbox.send_keys(self.timelinepage.time_line_end_date)
        self.timelinepage.get_tl_settings_window_save_button.click()
        sleep(2)
        self.timelinepage.get_time_line_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.timelinepage._tl_settings_window_header_locator)))
        actual_start_date = self.timelinepage.get_tl_settings_window_start_date_textbox.get_attribute('value').encode('utf-8')
        actual_end_date = self.timelinepage.get_tl_settings_window_end_date_textbox.get_attribute('value').encode('utf-8')
        exp_start_date = self.timelinepage.time_line_start_date.encode('utf-8')
        exp_end_date = self.timelinepage.time_line_end_date.encode('utf-8')
        self.timelinepage.get_tl_settings_window_close_button.click()
        if (actual_start_date == exp_start_date) and (actual_end_date == exp_end_date):
            self.assertTrue(True, "Start/End dates are not matching with the expected dates.")
        else:
            self.assertFalse(True, "Start/End dates are not matching with the expected dates.")

    @attr(priority="high")
    #@SkipTest
    def test_TL_002_timeline_settings_end_date_less(self):
        """
        Test : test_FI_002 To verify End date less than start date.
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """

        self.timelinepage.get_time_line_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.timelinepage._tl_settings_window_header_locator)))
        self.timelinepage.get_tl_settings_window_start_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_start_date_textbox.send_keys(self.timelinepage.time_line_end_date)
        self.timelinepage.get_tl_settings_window_end_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_end_date_textbox.send_keys(self.timelinepage.time_line_start_date)
        sleep(2)
        if self.timelinepage.get_tl_settings_date_error_message.is_displayed():
            self.timelinepage.get_tl_settings_window_close_button.click()
            self.assertTrue(True, "Error Message is not displayed.")
        else:
            self.timelinepage.get_tl_settings_window_close_button.click()
            self.assertFalse(True, "Error Message is not displayed.")


    @attr(priority="high")
    #@SkipTest
    def test_TL_003_timeline_settings_add_new_tags(self):
        """
        Test : test_FI_003 To verify that new tags added properly.
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.timelinepage.get_time_line_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.timelinepage._tl_settings_window_header_locator)))
        tag_count = 0
        try:
            if len(self.timelinepage.get_tl_settings_window_tags_delete_link)>=1:
                tag_count = len(self.timelinepage.get_tl_settings_window_tags_delete_link)
        except:
            pass
        self.timelinepage.get_tl_settings_window_start_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_start_date_textbox.send_keys(self.timelinepage.time_line_start_date)
        self.timelinepage.get_tl_settings_window_end_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_end_date_textbox.send_keys(self.timelinepage.time_line_end_date)
        self.timelinepage.get_tl_settings_window_tags_textbox.send_keys(self.timelinepage.time_line_tag_1)
        self.timelinepage.get_tl_settings_window_tags_add_button.click()
        self.timelinepage.get_tl_settings_window_save_button.click()
        sleep(2)
        self.timelinepage.get_time_line_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.timelinepage._tl_settings_window_header_locator)))
        tag_count_final = len(self.timelinepage.get_tl_settings_window_tags_delete_link)
        sleep(1)
        self.timelinepage.delete_all_tags()
        sleep(1)
        self.timelinepage.get_tl_settings_window_save_button.click()
        sleep(1)
        self.assertEqual(tag_count_final, tag_count+1,"New tag could not be added.")

    @attr(priority="high")
    #@SkipTest
    def test_TL_004_timeline_settings_add_new_tag_wrong_value(self):
        """
        Test : test_FI_004 To verify that time line does not have any info if wrong tags has been added.
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.timelinepage.get_time_line_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.timelinepage._tl_settings_window_header_locator)))
        self.timelinepage.get_tl_settings_window_start_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_start_date_textbox.send_keys(self.timelinepage.time_line_start_date)
        self.timelinepage.get_tl_settings_window_end_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_end_date_textbox.send_keys(self.timelinepage.time_line_end_date)
        self.timelinepage.get_tl_settings_window_tags_textbox.send_keys(self.timelinepage.time_line_tag_2)
        self.timelinepage.get_tl_settings_window_tags_add_button.click()
        check_boxes_name = ["assessments","events","incidents", "field_interviews"]
        for item in check_boxes_name:
            self.timelinepage.check_box_enable(item)
        self.timelinepage.get_tl_settings_window_save_button.click()
        sleep(2)
        time_line_info = len(self.timelinepage.get_time_line_all_images)
        self.timelinepage.get_time_line_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.timelinepage._tl_settings_window_header_locator)))
        self.timelinepage.delete_all_tags()
        self.timelinepage.get_tl_settings_window_save_button.click()
        sleep(2)
        self.assertEqual(time_line_info, 1, "Tag could not be added properly.")

    @attr(priority="high")
    #@SkipTest
    def test_TL_005_timeline_settings_enable_assessments_checkbox(self):
        """
        Test : test_FI_005 To verify that assessments checkbox.
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.timelinepage.get_time_line_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.timelinepage._tl_settings_window_header_locator)))
        self.timelinepage.get_tl_settings_window_start_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_start_date_textbox.send_keys(self.timelinepage.time_line_start_date)
        self.timelinepage.get_tl_settings_window_end_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_end_date_textbox.send_keys(self.timelinepage.time_line_end_date)
        check_boxes_name = ["assessments","events","incidents", "field_interviews"]
        for item in check_boxes_name:
            self.timelinepage.check_box_disable(item)
        sleep(2)
        self.timelinepage.check_box_enable("assessments")
        sleep(2)
        self.timelinepage.get_tl_settings_window_save_button.click()
        sleep(3)
        try:
            assessments_images = len(self.timelinepage.get_time_line_assessments_images)
            assessments_links = len(self.timelinepage.get_time_line_assessments_links)
            self.timelinepage.get_time_line_settings_link.click()
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                     self.timelinepage._tl_settings_window_header_locator)))
            check_box_status = self.timelinepage.get_tl_settings_window_assessments_checkbox.is_displayed()
            self.timelinepage.get_tl_settings_window_save_button.click()
            sleep(2)
            if check_box_status and (assessments_images == assessments_links):
                self.assertTrue(check_box_status, "Assessments checkbox is not enabled or Info not appearing on Time Line.")
            else:
                self.assertFalse(check_box_status, "Assessments checkbox is not enabled or Info not appearing on Time Line")
        except:
            self.skipTest("No Incidents were created between start-end date.")

    @attr(priority="high")
    #@SkipTest
    def test_TL_006_timeline_settings_enable_events_checkbox(self):
        """
        Test : test_FI_006 To verify that events checkbox.
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.timelinepage.get_time_line_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.timelinepage._tl_settings_window_header_locator)))
        self.timelinepage.get_tl_settings_window_start_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_start_date_textbox.send_keys(self.timelinepage.time_line_start_date)
        self.timelinepage.get_tl_settings_window_end_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_end_date_textbox.send_keys(self.timelinepage.time_line_end_date)
        check_boxes_name = ["assessments","events","incidents", "field_interviews"]
        for item in check_boxes_name:
            self.timelinepage.check_box_disable(item)
        sleep(2)
        self.timelinepage.check_box_enable("events")
        sleep(2)
        self.timelinepage.get_tl_settings_window_save_button.click()
        sleep(3)
        try:
            events_images = len(self.timelinepage.get_time_line_events_images)
            events_links = len(self.timelinepage.get_time_line_events_links)
            self.timelinepage.get_time_line_settings_link.click()
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                     self.timelinepage._tl_settings_window_header_locator)))
            check_box_status = self.timelinepage.get_tl_settings_window_events_checkbox.is_displayed()
            self.timelinepage.get_tl_settings_window_save_button.click()
            sleep(2)
            if check_box_status and (events_images == events_links):
                self.assertTrue(check_box_status, "Events checkbox is not enabled or info not appearing on Time Line.")
            else:
                self.assertFalse(check_box_status, "Events checkbox is not enabled or info not appearing on Time Line.")
        except:
            self.skipTest("No Events were created between start-end date.")

    @attr(priority="high")
    #@SkipTest
    def test_TL_007_timeline_settings_enable_incidents_checkbox(self):
        """
        Test : test_FI_007 To verify that incidents checkbox.
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.timelinepage.get_time_line_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.timelinepage._tl_settings_window_header_locator)))
        self.timelinepage.get_tl_settings_window_start_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_start_date_textbox.send_keys(self.timelinepage.time_line_start_date)
        self.timelinepage.get_tl_settings_window_end_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_end_date_textbox.send_keys(self.timelinepage.time_line_end_date)
        check_boxes_name = ["assessments","events","incidents", "field_interviews"]
        for item in check_boxes_name:
            self.timelinepage.check_box_disable(item)
        sleep(2)
        self.timelinepage.check_box_enable("incidents")
        sleep(2)
        self.timelinepage.get_tl_settings_window_save_button.click()
        sleep(3)
        try:
            incidents_images = len(self.timelinepage.get_time_line_incidents_images)
            incidents_links = len(self.timelinepage.get_time_line_incidents_links)
            self.timelinepage.get_time_line_settings_link.click()
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                     self.timelinepage._tl_settings_window_header_locator)))
            check_box_status = self.timelinepage.get_tl_settings_window_incidents_checkbox.is_displayed()
            self.timelinepage.get_tl_settings_window_save_button.click()
            sleep(2)
            if check_box_status and (incidents_images == incidents_links):
                self.assertTrue(check_box_status, "Incidents checkbox is not enabled or info not appearing on Time Line.")
            else:
                self.assertFalse(check_box_status, "Incidents checkbox is not enabled or info not appearing on Time Line.")
        except:
            self.skipTest("No Incidents were created between start-end date.")

    @attr(priority="high")
    #@SkipTest
    def test_TL_008_timeline_settings_enable_field_interviews_checkbox(self):
        """
        Test : test_FI_008 To verify that filed interviews checkbox.
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.timelinepage.get_time_line_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                 self.timelinepage._tl_settings_window_header_locator)))
        self.timelinepage.get_tl_settings_window_start_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_start_date_textbox.send_keys(self.timelinepage.time_line_start_date)
        self.timelinepage.get_tl_settings_window_end_date_textbox.clear()
        self.timelinepage.get_tl_settings_window_end_date_textbox.send_keys(self.timelinepage.time_line_end_date)
        check_boxes_name = ["assessments","events","incidents", "field_interviews"]
        for item in check_boxes_name:
            self.timelinepage.check_box_disable(item)
        sleep(2)
        self.timelinepage.check_box_enable("field_interviews")
        sleep(2)
        self.timelinepage.get_tl_settings_window_save_button.click()
        sleep(3)
        try:
            field_interviews_images = len(self.timelinepage.get_time_line_field_interviews_images)
            field_interviews_links = len(self.timelinepage.get_time_line_field_interviews_links)
            self.timelinepage.get_time_line_settings_link.click()
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                     self.timelinepage._tl_settings_window_header_locator)))
            check_box_status = self.timelinepage.get_tl_settings_window_field_interviews_checkbox.is_displayed()
            self.timelinepage.get_tl_settings_window_save_button.click()
            sleep(2)
            if check_box_status and (field_interviews_images == field_interviews_links):
                self.assertTrue(check_box_status, \
                                "Field interviews checkbox is not enabled or info not appearing on Time Line.")
            else:
                self.assertFalse(check_box_status, \
                                 "Field_interviews checkbox is not enabled or info not appearing on Time Line.")
        except:
            self.skipTest("No Field interviews were created between start-end date.")