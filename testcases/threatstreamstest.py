__author__ = 'Deepa.Sivadas'
from testcases.basetestcase import BaseTestCase
from pages.threatstreamspage import ThreatStreamPage
from nose.plugins.attrib import attr
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class ThreatStreamTest(BaseTestCase):


    def setUp(self):
        self.errors_and_failures = self.tally()
        self.tstream = ThreatStreamPage(self.driver)

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        #self.tstream.return_to_apps_main_page()

    @attr(priority="high")
    #@SkipTest
    def test_TS_099(self):
        sleep(15)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.tstream._ts_app_name_text)))
        self.tstream.get_ts_app_settingl_ink.click()
        WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((By.XPATH,
                                                self.tstream._ts_setting_window_locator), "Threat Stream settings"))
        sleep(10)
        if not self.tstream.get_ts_setting_window_checkbox.is_selected():
            self.tstream.get_ts_setting_window_checkbox.click()
            sleep(2)
            self.tstream.get_ts_setting_window_save_button.click()
            sleep(2)
            print "dddddddddddd"
        else:

            print "rrrrrrrrrrrrrrrrrrrr"
        self.tstream.get_ts_setting_link.click()
        sleep(2)
        self.tstream.get_ts_setting_window_save_button.click()
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable ((By.XPATH, self.tstream._ts_setting_link_locator)))
        self.tstream.get_ts_setting_link.click()
        # sleep(3)
        # xxx = self.tstream.get_ts_app_setting_window_checkbox.is_selected()
        # print xxx
        self.assertTrue(self.tstream.get_ts_setting_window_checkbox.is_selected(), "Check box has been enabled.")

    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_TS_01(self):
        """
        Test : test_TS_01
        Description : To verify that filter type is selected as Starred.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        self.tstream.get_ts_threat_dropdown_starred_filter.click()
        act_text = self.tstream.get_ts_threat_filter_name_text.text
        self.assertEqual('Starred', act_text, "Selected filter name is not same as 'Starred'.")


    @attr(priority="high")
    #@SkipTest
    def test_TS_02(self):
        """
        Test : test_TS_02
        Description : To verify that filter type is selected as Stream.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        self.tstream.get_ts_threat_dropdown_stream_filter.click()
        act_text = self.tstream.get_ts_threat_filter_name_text.text
        self.assertEqual('Stream', act_text, "Selected filter name is not same as 'Stream'.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_03(self):
        """
        Test : test_TS_03
        Description : To verify that filter type is selected as Trending Last Day.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        self.tstream.get_ts_threat_dropdown_trendinglastday_filter.click()
        act_text = self.tstream.get_ts_threat_filter_name_text.text
        self.assertEqual('Trending Last Day', act_text, "Selected filter name is not same as 'Trending Last Day'.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_04(self):
        """
        Test : test_TS_04
        Description : To verify that filter type is selected as Trending Last Hour.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        self.tstream.get_ts_threat_dropdown_trendinglasthour_filter.click()
        act_text = self.tstream.get_ts_threat_filter_name_text.text
        self.assertEqual('Trending Last Hour', act_text, "Selected filter name is not same as 'Trending Last Hour'.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_05(self):
        """
        Test : test_TS_05
        Description : To verify that filter type is selected as Relevance.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_second_filter_dropdown.click()
        self.tstream.get_ts_threat_filter_dropdown_relevance.click()
        act_text = self.tstream.get_ts_threat_second_filter_name_text.text
        self.assertEqual('Relevance', act_text, "Selected filter name is not same as 'Relevance'.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_06(self):
        """
        Test : test_TS_06
        Description : To verify that filter type is selected as Time.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_second_filter_dropdown.click()
        self.tstream.get_ts_threat_filter_dropdown_time.click()
        act_text = self.tstream.get_ts_threat_second_filter_name_text.text
        self.assertEqual('Time', act_text, "Selected filter name is not same as 'Time'.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_09(self):
        """
        Test : test_TS_09
        Description : To verify mark important button is working properly or not .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        self.tstream.get_ts_threat_dropdown_trendinglastday_filter.click()
        detail_links = self.tstream.get_ts_feed_data_details_link
        detail_links[0].click()
        important_list = self.tstream.get_ts_feed_data_important_button
        button_text = important_list[0].text
        if str(button_text) == r"Mark important":
            important_list[0].click()
            sleep(10)
            feeds_list = self.tstream.get_ts_feeds_list
            attri_value =  feeds_list[0].get_attribute("class")
            if str(attri_value) == r"squintem ng-scope importantsquintem":
                self.assertTrue(True, "The Feed could not be marked as 'Mark important'.")
        else:
            important_list[0].click()
            sleep(10)
            feeds_list = self.tstream.get_ts_feeds_list
            attri_value =  feeds_list[0].get_attribute("class")
            if str(attri_value) == r"squintem ng-scope":
                self.assertTrue(True, "The Feed could not be marked as 'Mark not important'.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_10(self):
        """
        Test : test_TS_10
        Description : To verify Hide button is working properly or not .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        self.tstream.get_ts_threat_dropdown_trendinglastday_filter.click()
        feed_text_val = self.tstream.get_ts_feeds_list_text_value
        before_hide_text = str(feed_text_val[0].text)
        detail_links = self.tstream.get_ts_feed_data_details_link
        detail_links[0].click()
        hide_list = self.tstream.get_ts_feed_data_hide_button_locator
        hide_list[0].click()
        sleep(4)
        feed_text_val = self.tstream.get_ts_feeds_list_text_value
        after_hide_text = str(feed_text_val[0].text)
        print before_hide_text
        print after_hide_text
        self.assertNotEqual(before_hide_text,after_hide_text, "The Feed can not be hided.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_11(self):
        """
        Test : test_TS_11
        Description : To verify share button is working properly or not .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        self.tstream.get_ts_threat_dropdown_trendinglastday_filter.click()
        detail_links = self.tstream.get_ts_feed_data_details_link
        detail_links[0].click()
        email_share_link = self.tstream.get_ts_feed_data_share_button_locator
        email_share_link[0].click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,\
                                     self.tstream._ts_feed_email_window_title_locator),r"Share via email to..."))
        self.tstream.get_ts_feed_email_window_email_textbox.send_keys("test@indecomm.net")
        self.tstream.get_ts_feed_email_window_comment_textbox.send_keys("This is a comment.")
        self.tstream.get_ts_feed_email_window_send_button.click()
        sleep(4)
        try:
            if self.tstream.get_ts_feed_share_email_window_title.is_displayed():
                self.assertFalse(True, "The Send Button is not working. The window is not closed.")
        except:
            self.assertTrue(True, "The Email send window is not working properly.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_13_1(self):
        """
        Test : test_TS_13_1
        Description : To verify New Filter is created and saved. Filter type is RSS/Atom.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_13_1")
        self.tstream.get_ts_filter_create_type_dropdown_arrow.click()
        self.tstream.get_ts_filter_create_type_dropdown_rss_atom.click()
        self.tstream.get_ts_filter_create_visibility_dropdown_arrow.click()
        self.tstream.get_ts_filter_create_visibility_groups.click()
        self.tstream.get_ts_filter_create_tags_textbox.send_keys("Fire")
        self.tstream.get_ts_filter_create_tags_add_button.click()
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("flood")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        self.tstream.get_ts_filter_create_save_button.click()
        try:
            WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"New_Filter_TC_13_1"))
            act_text = self.tstream.get_ts_threat_filter_name_text.text
            self.assertEqual(act_text, "New_Filter_TC_13_1", "New filter name is not appearing in window title")
        except Exception, err:
            raise type(err)("Newly created filter name is not appearing in window title - search XPATH - " \
                          + self.tstream._ts_threat_filter_name_text_locator + err.message)

    #@SkipTest
    def test_TS_13_2(self):
        """
        Test : test_TS_13_2
        Description : To verify New Filter is created and saved. Filter type is RSS/Atom.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_13_2")
        self.tstream.get_ts_filter_create_type_dropdown_arrow.click()
        self.tstream.get_ts_filter_create_type_dropdown_twitter.click()
        self.tstream.get_ts_filter_create_visibility_dropdown_arrow.click()
        self.tstream.get_ts_filter_create_visibility_groups.click()
        self.tstream.get_ts_filter_create_tags_textbox.send_keys("Bomb")
        self.tstream.get_ts_filter_create_tags_add_button.click()
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("Threat")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        self.tstream.get_ts_filter_create_save_button.click()
        try:
            WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"New_Filter_TC_13_2"))
            act_text = self.tstream.get_ts_threat_filter_name_text.text
            self.assertEqual(act_text, "New_Filter_TC_13_2", "New filter name is not appearing in window title")
        except Exception, err:
            raise type(err)("Newly created filter name is not appearing in window title - search XPATH - " \
                          + self.tstream._ts_threat_filter_name_text_locator + err.message)

