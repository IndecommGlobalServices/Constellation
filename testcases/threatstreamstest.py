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
import ConfigParser, re

class ThreatStreamTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(ThreatStreamTest, cls).setUpClass()
        cls.tstream = ThreatStreamPage(cls.driver)
        cls.section = 'Messages'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))

    def setUp(self):
        self.errors_and_failures = self.tally()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        #self.tstream.return_to_apps_main_page()

    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_threatsstream_smoke(self):
        self.assertTrue(self.tstream.get_ts_threat_dropdown_filter.is_displayed(), "Dropdown filter not available")


    @attr(priority="high")
    #@SkipTest
    def test_TS_01_To_Verify_Starred_Filter_Is_Selected(self):
        """
        Test : test_TS_01
        Description : To verify that filter type is selected as Starred.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_starred_filter.click()
        act_text = self.tstream.get_ts_threat_filter_name_text.text
        self.assertEqual('Starred', act_text, "Selected filter name is not same as 'Starred'.")


    @attr(priority="high")
    #@SkipTest
    def test_TS_02_To_Verify_Stream_Filter_Is_Selected(self):
        """
        Test : test_TS_02
        Description : To verify that filter type is selected as Stream.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_stream_filter.click()
        act_text = self.tstream.get_ts_threat_filter_name_text.text
        self.assertEqual('Stream', act_text, "Selected filter name is not same as 'Stream'.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_03_To_Verify_Trending_Last_Day_Filter_Is_Selected(self):
        """
        Test : test_TS_03
        Description : To verify that filter type is selected as Trending Last Day.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_trendinglastday_filter.click()
        act_text = self.tstream.get_ts_threat_filter_name_text.text
        self.assertEqual('Trending Last Day', act_text, "Selected filter name is not same as 'Trending Last Day'.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_04_To_Verify_Trending_Last_Hour_Filter_Is_Selected(self):
        """
        Test : test_TS_04
        Description : To verify that filter type is selected as Trending Last Hour.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_trendinglasthour_filter.click()
        act_text = self.tstream.get_ts_threat_filter_name_text.text
        self.assertEqual('Trending Last Hour', act_text, "Selected filter name is not same as 'Trending Last Hour'.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_05_To_Verify_Selected_Filter_Type_Is_Relevance(self):
        """
        Test : test_TS_05
        Description : To verify that filter type is selected as Relevance.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_second_filter_dropdown.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_filter_dropdown_relevance.click()
        act_text = self.tstream.get_ts_threat_second_filter_name_text.text
        self.assertEqual('Relevance', act_text, "Selected filter name is not same as 'Relevance'.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_06_To_Verify_Selected_Filter_Type_Is_Time(self):
        """
        Test : test_TS_06
        Description : To verify that filter type is selected as Time.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_second_filter_dropdown.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_filter_dropdown_time.click()
        act_text = self.tstream.get_ts_threat_second_filter_name_text.text
        self.assertEqual('Time', act_text, "Selected filter name is not same as 'Time'.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_09_To_Test_Mark_Important_Button(self):
        """
        Test : test_TS_09
        Description : To verify mark important button is working properly or not .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_trendinglastday_filter.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"Trending Last Day"))
        detail_links = self.tstream.get_ts_feed_data_details_link
        if len(detail_links) >= 1:
            detail_links[0].click()
            important_list = self.tstream.get_ts_feed_data_important_button
            button_text = (important_list[0].text).encode('utf-8')
            if str(button_text) == r"Mark important":
                important_list[0].click()
                sleep(10)
                feeds_list = self.tstream.get_ts_feeds_list
                attri_value =  feeds_list[0].get_attribute("class")
                self.tstream.get_ts_threat_dropdown_filter.click()
                self.tstream.get_ts_threat_dropdown_stream_filter.click()
                if str(attri_value) == r"squintem ng-scope importantsquintem":
                    self.assertTrue(True, "The Feed could not be marked as 'Mark important'.")
            else:
                important_list[0].click()
                sleep(10)
                feeds_list = self.tstream.get_ts_feeds_list
                attri_value =  feeds_list[0].get_attribute("class")
                self.tstream.get_ts_threat_dropdown_filter.click()
                self.tstream.get_ts_threat_dropdown_stream_filter.click()
                if str(attri_value) == r"squintem ng-scope":
                    self.assertTrue(True, "The Feed could not be marked as 'Mark not important'.")
        else:
            self.skipTest("Trending Last Day filter does not have any feeds. Mark Important Button could not be tested")

    @attr(priority="high")
    #@SkipTest
    def test_TS_10_To_Test_Hide_Button(self):
        """
        Test : test_TS_10
        Description : To verify Hide button is working properly or not .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_trendinglastday_filter.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"Trending Last Day"))
        sleep(2)
        feed_text_val = self.tstream.get_ts_feeds_list_text_value
        if len(feed_text_val)>=1:
            before_hide_text = (feed_text_val[0].text).encode('utf-8')
            detail_links = self.tstream.get_ts_feed_data_details_link
            detail_links[0].click()
            hide_list = self.tstream.get_ts_feed_data_hide_button_locator
            hide_list[0].click()
            sleep(4)#Required to update feeds in window
            feed_text_val = self.tstream.get_ts_feeds_list_text_value
            after_hide_text = (feed_text_val[0].text).encode('utf-8')
            self.assertNotEqual(before_hide_text,after_hide_text, "The Feed can not be hided.")
        else:
            self.skipTest("Trending Last Day filter does not have any feeds. Hide Button could not be tested.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_11_To_Test_Share_Button_With_Valid_Email_ID(self):
        """
        Test : test_TS_11
        Description : To verify share button is working properly or not.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_trendinglastday_filter.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"Trending Last Day"))
        detail_links = self.tstream.get_ts_feed_data_details_link
        if len(detail_links)>=1:
            detail_links[0].click()
            email_share_link = self.tstream.get_ts_feed_data_share_button_locator
            email_share_link[0].click()
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,\
                                         self.tstream._ts_feed_email_window_title_locator),r"Share via email to..."))
            self.tstream.get_ts_feed_email_window_email_textbox.send_keys("test@indecomm.net")
            self.tstream.get_ts_feed_email_window_comment_textbox.send_keys("This is a comment.")
            self.tstream.get_ts_feed_email_window_send_button.click()
            sleep(2)#Required to update feeds window
            self.tstream.get_ts_threat_dropdown_filter.click()
            sleep(2)#required to update dropdown menu
            self.tstream.get_ts_threat_dropdown_stream_filter.click()
            try:
                if self.tstream.get_ts_feed_share_email_window_title.is_displayed():
                    self.assertFalse(True, "The Send Button is not working. The window is not closed.")
            except:
                self.assertTrue(True, "In the Email window Save button is not working properly.")
        else:
            self.skipTest("Trending Last Day filter does not have any feeds. Share Button could not be tested.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_12_To_Test_Share_Button_With_Invalid_Email_ID(self):
        """
        Test : test_TS_12
        Description : To verify share button is working properly or not. Wrong Email value.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_trendinglastday_filter.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"Trending Last Day"))
        detail_links = self.tstream.get_ts_feed_data_details_link
        if len(detail_links)>=1:
            detail_links[0].click()
            email_share_link = self.tstream.get_ts_feed_data_share_button_locator
            email_share_link[0].click()
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH,\
                                         self.tstream._ts_feed_email_window_title_locator),r"Share via email to..."))
            self.tstream.get_ts_feed_email_window_email_textbox.send_keys("test#indecomm.net")
            self.tstream.get_ts_feed_email_window_comment_textbox.send_keys("This is a comment.")
            send_button_state = self.tstream.get_ts_feed_email_window_send_button.is_enabled()
            if send_button_state:
                self.assertFalse(send_button_state, "Email address is invalid but SEND button is enabled.")
            self.tstream.get_ts_feed_email_window_cancel_button.click()
            sleep(2)#required to update feeds window
            self.tstream.get_ts_threat_dropdown_filter.click()
            sleep(2)#required to update dropdown menu
            self.tstream.get_ts_threat_dropdown_stream_filter.click()
            try:
                if self.tstream.get_ts_feed_share_email_window_title.is_displayed():
                    self.assertFalse(True, "The Cancel Button is not working. The window is not closed.")
            except:
                self.assertTrue(True, "In the Email window Cancel button is not working properly.")
        else:
            self.skipTest("Trending Last Day filter does not have any feeds. Share Button could not be tested.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_13_1_To_Verify_New_RSS_Filter_Type_Appears_On_Window_Title(self):
        """
        Test : test_TS_13_1
        Description : To verify New Filter is created. Newly created filter name appears on Title window.
                        Filter type is RSS/Atom.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_13_1")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_type_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_type_dropdown_rss_atom.click()
        sleep(2) #required to load option properly.
        self.tstream.get_ts_filter_create_visibility_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
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
            self.tstream.delete_created_filter("New_Filter_TC_13_1")
            self.assertEqual(act_text, "New_Filter_TC_13_1", "New filter name is not appearing in window title")
        except Exception, err:
            raise type(err)("Newly created filter name is not appearing in window title"+ err.message)

    @attr(priority="high")
    #@SkipTest
    def test_TS_13_2_To_Verify_New_Twitter_Filter_Type_Appears_On_Window_Title(self):
        """
        Test : test_TS_13_2
        Description : To verify New Filter is created. Newly created filter name appears on Title window.
                        Filter type is Twitter.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_13_2")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_type_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_type_dropdown_twitter.click()
        sleep(2) #required to load option properly.
        self.tstream.get_ts_filter_create_visibility_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_visibility_groups.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_tags_textbox.send_keys("Bomb")
        self.tstream.get_ts_filter_create_tags_add_button.click()
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("Threat")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        self.tstream.get_ts_filter_create_save_button.click()
        try:
            WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"New_Filter_TC_13_2"))
            act_text = self.tstream.get_ts_threat_filter_name_text.text
            self.tstream.delete_created_filter("New_Filter_TC_13_2")
            self.assertEqual(act_text, "New_Filter_TC_13_2", "New filter name is not appearing in window title")
        except Exception, err:
            raise type(err)("Newly created filter name is not appearing in window title" + err.message)

    @attr(priority="high")
    #@SkipTest
    def test_TS_14_To_Verify_New_Twitter_Filter_Type_Appears_In_Filter_Dropdown_Menu(self):
        """
        Test : test_TS_14
        Description : To verify New Filter is created. Newly created filter name appears as one of menu item.
                        Filter type is Twitter.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_14")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_type_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_type_dropdown_twitter.click()
        sleep(2) #required to load option properly.
        self.tstream.get_ts_filter_create_visibility_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_visibility_groups.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_tags_textbox.send_keys("Bomb")
        self.tstream.get_ts_filter_create_tags_add_button.click()
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("bomb")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        self.tstream.get_ts_filter_create_save_button.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"New_Filter_TC_14"))
        self.tstream.get_ts_threat_dropdown_filter.click()
        try:
            if self.tstream.get_ts_new_filter_name("New_Filter_TC_14").is_displayed():
                state = self.tstream.get_ts_new_filter_name("New_Filter_TC_14").is_displayed()
                self.tstream.get_ts_threat_dropdown_filter.click()
                self.tstream.delete_created_filter("New_Filter_TC_14")
                self.assertTrue(state, "New filter name is not appearing in the dropdown menu.")
            else:
                self.assertFalse(True, "New filter is not created or it is not appearing in the dropdown menu.")
        except Exception, err:
            raise type(err)("Newly created filter name is not appearing in dropdown menu item list."+ err.message)

    @attr(priority="high")
    #@SkipTest
    def test_TS_15_To_Verify_Phrases_Appears_In_New_Filter_Feeds(self):
        """
        Test : test_TS_15
        Description : To verify more than one phrases has been added in newly created filter.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_15")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("gun")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        sleep(2)
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("love")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        sleep(2)
        self.tstream.get_ts_filter_create_save_button.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"New_Filter_TC_15"))
        sleep(20) #Required to update feeds in new filter window.
        feed_text_val = self.tstream.get_ts_feeds_list_text_value
        counter1 = counter2 = 0
        if len(feed_text_val)>10:
            loop_count = 10
        else:
            loop_count = len(feed_text_val)
        for num in range(loop_count):
            if 'gun' in (feed_text_val[num].text).encode('utf-8'):
               counter1 = counter1+1
            elif "love" in (feed_text_val[num].text).encode('utf-8'):
                counter2 = counter2+1
        if counter1>=1 and counter2>=1:
            self.tstream.delete_created_filter("New_Filter_TC_15")
            self.assertTrue(True, "The phrases are not appearing in the feeds.")
        else:
            self.tstream.delete_created_filter("New_Filter_TC_15")
            self.assertFalse(True,"The phrases are not appearing in the feeds." )

    @attr(priority="high")
    #@SkipTest
    def test_TS_16_To_Test_New_Filter_Menu_Save_Buton(self):
        """
        Test : test_TS_16
        Description : To verify Name text box of Create New filter window. No Value has been entered.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("")
        sleep(3)
        #self.tstream.get_ts_filter_create_save_button.click()
        #sleep(2)
        state = self.tstream.get_ts_filter_create_save_button.is_enabled()
        self.tstream.get_ts_filter_create_cancel_button.click()
        if state:
            self.assertFalse(True, "The Save button is enabled even though no value entered in Name text box.")
        else:
            self.assertTrue(True, "The Save button is enabled even though no value entered in Name text box." )


    @attr(priority="high")
    #@SkipTest
    def test_TS_17_To_Verify_Phrase_Deleted_Properly(self):
        """
        Test : test_TS_17
        Description : To verify that added phrase has been deleted properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_17")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("gun")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        sleep(2)
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("love")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        sleep(2)
        phrases_count = self.tstream.get_ts_filter_create_phrases_delete_icon
        count_before_delete = len(phrases_count)
        phrases_count[0].click()
        sleep(2)
        phrases_count = self.tstream.get_ts_filter_create_phrases_delete_icon
        count_after_delete = len(phrases_count)
        self.tstream.get_ts_filter_create_cancel_button.click()
        self.assertEqual(count_before_delete, count_after_delete+1, "Phrase could not be deleted.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_18_To_Verify_Multiple_Phrases_Deleted_Properly(self):
        """
        Test : test_TS_18
        Description : To verify that added phrases has been deleted properly. Multiple phrases.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_18")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("test1")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("test2")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("test3")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("test4")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        phrases_count = self.tstream.get_ts_filter_create_phrases_delete_icon
        count_before_delete = len(phrases_count)
        sleep(5)
        for item in phrases_count[::-1]:
            item.click()
            sleep(2)
        phrases_count = self.tstream.get_ts_filter_create_phrases_delete_icon
        count_after_delete = len(phrases_count)
        self.tstream.get_ts_filter_create_cancel_button.click()
        self.assertEqual(count_before_delete, count_after_delete+count_before_delete, "Phrases could not be deleted.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_19_To_Test_New_Filter_Window_Reset_Button(self):
        """
        Test : test_TS_19
        Description : To verify Type Reset button functionality.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_19")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_type_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_type_dropdown_twitter.click()
        sleep(2) #required to load option properly.
        text_before_refresh = self.tstream.get_ts_filter_create_type_text.text
        sleep(2)
        self.tstream.get_ts_filter_create_type_refresh_button.click()
        sleep(2)#required to update type text
        text_after_refresh = self.tstream.get_ts_filter_create_type_text.text
        self.tstream.get_ts_filter_create_cancel_button.click()
        if (text_after_refresh == "Type") and (text_after_refresh != text_before_refresh):
            self.assertTrue(text_after_refresh, "The Type value has not been reset.")
        else:
            self.assertFalse(True, "The Type value has not been reset." )

    @attr(priority="high")
    #@SkipTest
    def test_TS_20_To_Test_New_Filter_Window_Map_Icon(self):
        """
        Test : test_TS_20
        Description : To verify Type Map icon functionality.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_20")
        self.tstream.show_advance_info()
        self.tstream.show_location_options()
        status = self.tstream.get_ts_filter_create_location_latitude_textbox.is_displayed()
        self.tstream.get_ts_filter_create_cancel_button.click()
        sleep(2)
        if status:
            self.assertTrue(status, "Location Icon is disabled.")
        else:
            self.assertFalse(status, "Location Icon is disabled." )


    @attr(priority="high")
    #@SkipTest
    def test_TS_21_To_Test_New_Filter_Window_Cancel_Button(self):
        """
        Test : test_TS_21
        Description : To verify that Cancel button is working properly in New filter create window.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_21")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_type_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_type_dropdown_twitter.click()
        sleep(2) #required to load option properly.
        self.tstream.get_ts_filter_create_visibility_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_visibility_groups.click()
        self.tstream.get_ts_filter_create_tags_textbox.send_keys("and")
        self.tstream.get_ts_filter_create_tags_add_button.click()
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("you")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        self.tstream.get_ts_filter_create_cancel_button.click()
        sleep(2)
        self.tstream.get_ts_threat_dropdown_filter.click()
        try:
            if self.tstream.get_ts_new_filter_name("New_Filter_TC_21").is_displayed():
                self.tstream.get_ts_threat_dropdown_filter.click()
                self.assertFalse(True, "New filter has been created and Cancel button is not working.")
        except:
            self.tstream.get_ts_threat_dropdown_filter.click()
            self.assertTrue(True, "New filter has been created and Cancel button is not working.")


    @attr(priority="high")
    #@SkipTest
    def test_TS_23_To_Verify_Edit_Window_Of_New_Filter(self):
        """
        Test : test_TS_23
        Description : To verify that new filter edit window is working.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_23")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_save_button.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"New_Filter_TC_23"))
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_new_filter_name("New_Filter_TC_23").click()
        self.tstream.get_ts_threat_filter_edit_cog_wheel.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.clear()
        sleep(2)#required to clear textbox
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_23_edit_name")
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("love")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        self.tstream.get_ts_filter_create_save_button.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                        self.tstream._ts_threat_filter_name_text_locator),"New_Filter_TC_23_edit_name"))
        try:
            act_text = self.tstream.get_ts_threat_filter_name_text.text
            self.tstream.delete_created_filter("New_Filter_TC_23_edit_name")
            self.assertEqual(act_text, "New_Filter_TC_23_edit_name", "Edited name of filter is not appearing in window title")
        except Exception, err:
            raise type(err)("Edited name of filter is not appearing in window title" + err.message)

    @attr(priority="high")
    #@SkipTest
    def test_TS_24_1_To_Verify_New_Filter_Deleted_Properly(self):
        """
        Test : test_TS_24_1
        Description : To verify that new filter has been deleted properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_24_1")
        self.tstream.get_ts_filter_create_save_button.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"New_Filter_TC_24_1"))
        self.tstream.delete_created_filter("New_Filter_TC_24_1")
        self.tstream.get_ts_threat_dropdown_filter.click()
        try:
            if self.tstream.get_ts_new_filter_name("New_Filter_TC_24_1").is_displayed():
                state = self.tstream.get_ts_new_filter_name("New_Filter_TC_24_1").is_displayed()
                self.tstream.get_ts_threat_dropdown_filter.click()
                self.assertFalse(state, "Newly created filter could not be deleted.")
        except Exception:
            self.tstream.get_ts_threat_dropdown_filter.click()
            self.assertTrue(True, "Newly created filter could not be deleted.")


    @attr(priority="high")
    #@SkipTest
    def test_TS_24_2_To_Test_Cancel_Button_In_Delete_Fileter_Window(self):
        """
        Test : test_TS_24_2
        Description : To verify that in new filter edit window Delete Cancel button working properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(3)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_24_2")
        self.tstream.get_ts_filter_create_save_button.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"New_Filter_TC_24_2"))
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(4)#required to update dropdown menu
        self.tstream.get_ts_new_filter_name("New_Filter_TC_24_2").click()
        sleep(4)#required to display filter name on title.
        self.tstream.get_ts_threat_filter_edit_cog_wheel.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_delete_button.click()
        sleep(3)#required to display confirm delete popup
        self.tstream.get_ts_filter_create_confirm_cancel_button.click()
        sleep(3)
        self.tstream.get_ts_filter_create_cancel_button.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"New_Filter_TC_24_2"))
        self.tstream.get_ts_threat_dropdown_filter.click()
        try:
            if self.tstream.get_ts_new_filter_name("New_Filter_TC_24_2").is_displayed():
                state = self.tstream.get_ts_new_filter_name("New_Filter_TC_24_2").is_displayed()
                self.tstream.get_ts_threat_dropdown_filter.click()
                self.tstream.delete_created_filter("New_Filter_TC_24_2")
                self.assertTrue(state, "In edit filter window Confirm Cancel button is not working.")
        except Exception:
            self.tstream.get_ts_threat_dropdown_filter.click()
            self.tstream.delete_created_filter("New_Filter_TC_24_2")
            self.assertFalse(True, "In edit filter window Confirm Cancel button is not working.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_25_To_Test_Cancel_Button_Of_Filter_Edit_Window(self):
        """
        Test : test_TS_25
        Description : To verify that in new filter edit window Cancel button working properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_25")
        self.tstream.get_ts_filter_create_save_button.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self.tstream._ts_threat_filter_name_text_locator),"New_Filter_TC_25"))
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_new_filter_name("New_Filter_TC_25").click()
        self.tstream.get_ts_threat_filter_edit_cog_wheel.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.clear()
        sleep(2)#required to update text box
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_25_edit_name")
        self.tstream.get_ts_filter_create_phrases_textbox.send_keys("love")
        self.tstream.get_ts_filter_create_phrases_add_button.click()
        self.tstream.get_ts_filter_create_cancel_button.click()
        sleep(2)#required to update threat stream app.
        act_text = self.tstream.get_ts_threat_filter_name_text.text
        self.tstream.delete_created_filter("New_Filter_TC_25")
        self.assertNotEqual(act_text, "New_Filter_TC_25_edit_name", "In Edit Filter window Cancel button is not Working.")


    @attr(priority="high")
    #@SkipTest
    def test_TS_26_To_Test_New_Filter_Visibility_User_Option(self):
        """
        Test : test_TS_26
        Description : To verify that visibility as User has been selected properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_26")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_visibility_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_visibility_user.click()
        sleep(2)
        visibility_type = self.tstream.get_ts_filter_create_visibility_text.text
        self.tstream.get_ts_filter_create_cancel_button.click()
        self.assertEqual(visibility_type, "User", "Visibility type is not equal to 'User'")

    @attr(priority="high")
    #@SkipTest
    def test_TS_27_To_Test_New_Filter_Visibility_Tenant_Option(self):
        """
        Test : test_TS_27
        Description : To verify that visibility as Tenant has been selected properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_27")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_visibility_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_visibility_tenant.click()
        sleep(2)
        visibility_type = self.tstream.get_ts_filter_create_visibility_text.text
        self.tstream.get_ts_filter_create_cancel_button.click()
        self.assertEqual(visibility_type, "Tenant", "Visibility type is not equal to 'Tenant'")

    @attr(priority="high")
    #@SkipTest
    def test_TS_28_To_Test_New_Filter_Visibility_Groups_Option(self):
        """
        Test : test_TS_28
        Description : To verify that visibility as Groups has been selected properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_28")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_visibility_dropdown_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_filter_create_visibility_groups.click()
        sleep(2)
        visibility_type = self.tstream.get_ts_filter_create_visibility_text.text
        self.tstream.get_ts_filter_create_cancel_button.click()
        self.assertEqual(visibility_type, "Groups", "Visibility type is not equal to 'Groups'")

    @attr(priority="high")
    #@SkipTest
    def test_TS_29_To_Test_New_Filter_Add_Tag(self):
        """
        Test : test_TS_29
        Description : To verify that new tag added properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_29")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_tags_textbox.send_keys("Bomb")
        self.tstream.get_ts_filter_create_tags_add_button.click()
        list = self.tstream.get_ts_filter_create_tags_delete_icon
        if list[0].is_displayed():
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertTrue(True, "New Tag could not be added.")
        else:
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertFalse(True, "New Tag could not be added.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_30_To_Test_New_Filter_Delete_Tag(self):
        """
        Test : test_TS_30
        Description : To verify that new tag has been deleted properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_30")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_tags_textbox.send_keys("Bomb")
        self.tstream.get_ts_filter_create_tags_add_button.click()
        list = self.tstream.get_ts_filter_create_tags_delete_icon
        list[0].click()
        sleep(5)
        list = self.tstream.get_ts_filter_create_tags_delete_icon
        if len(list)>=1:
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertFalse(True, "New Tag could not be deleted.")
        else:
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertTrue(True, "New Tag could not be deleted.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_31_To_Test_Manage_Feeds_Rss_Atom_Filter(self):
        """
        Test : test_TS_31
        Description : To verify that In manage feeds window Rss/Atom Filter is selected.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_manage_feeds_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                       self.tstream._ts_manage_feeds_app_text_locator)))
        self.tstream.get_ts_manage_feeds_filter_type_drop_down_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_manage_feeds_type_dropdown_rss_atom_menu_item.click()
        sleep(2)#Required for selected filter to update
        text = self.tstream.get_ts_manage_feeds_filter_type_text.text
        self.tstream.get_ts_threat_streams_link.click()
        self.assertEqual(text, "Rss/atom", "Selected feeds filter type is not equal to Rss/atom")

    @attr(priority="high")
    #@SkipTest
    def test_TS_32_To_Test_Manage_Feeds_Rss_Atom_Off_Filter(self):
        """
        Test : test_TS_32
        Description : To verify that In manage feeds window Rss/Atom-Off Filter is selected.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_manage_feeds_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                       self.tstream._ts_manage_feeds_app_text_locator)))
        self.tstream.get_ts_manage_feeds_filter_type_drop_down_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_manage_feeds_type_dropdown_rss_atom_off_menu_item.click()
        sleep(2)#Required for selected filter to update
        text = self.tstream.get_ts_manage_feeds_filter_type_text.text
        self.tstream.get_ts_threat_streams_link.click()
        self.assertEqual(text, "Rss/atom-OFF", "Selected feeds filter type is not equal to Rss/atom-OFF")

    @attr(priority="high")
    #@SkipTest
    def test_TS_33_To_Test_Manage_Feeds_Twitter_Filter(self):
        """
        Test : test_TS_33
        Description : To verify that In manage feeds window Twitter Filter is selected.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_manage_feeds_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                       self.tstream._ts_manage_feeds_app_text_locator)))
        self.tstream.get_ts_manage_feeds_filter_type_drop_down_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_manage_feeds_type_dropdown_twitter_menu_item.click()
        sleep(2)#Required for selected filter to update
        text = self.tstream.get_ts_manage_feeds_filter_type_text.text
        self.tstream.get_ts_threat_streams_link.click()
        self.assertEqual(text, "Twitter", "Selected feeds filter type is not equal to Twitter")

    @attr(priority="high")
    #@SkipTest
    def test_TS_34_To_Test_Manage_Feeds_Reset_Filter(self):
        """
        Test : test_TS_34
        Description : To verify that In manage feeds Reset Feeds filter.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_manage_feeds_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                       self.tstream._ts_manage_feeds_app_text_locator)))
        self.tstream.get_ts_manage_feeds_filter_type_drop_down_arrow.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_manage_feeds_type_dropdown_twitter_menu_item.click()
        sleep(2)#Required for selected filter to update
        text1 = self.tstream.get_ts_manage_feeds_filter_type_text.text
        self.tstream.get_ts_manage_feeds_reset_filter.click()
        sleep(2)#Wait to reset filter
        text2 = self.tstream.get_ts_manage_feeds_filter_type_text.text
        sleep(2)#required to update filter text
        if (text1 != text2) and (text2 == 'Type'):
            self.tstream.get_ts_threat_streams_link.click()
            self.assertTrue(text2, "Filter Could not reset.")
        else:
            self.tstream.get_ts_threat_streams_link.click()
            self.assertFalse(True, "Filter Could not reset.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_35_To_Test_Manage_Feeds_Search_Textbox(self):
        """
        Test : test_TS_35
        Description : To verify that search feeds text box is working properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_manage_feeds_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                       self.tstream._ts_manage_feeds_app_text_locator)))
        self.tstream.get_ts_manage_feeds_search_feeds_textbox.clear()
        self.tstream.get_ts_manage_feeds_search_feeds_textbox.send_keys("Latest")
        sleep(5)#Required to update filter list.
        feeds_list = self.tstream.get_ts_manage_feeds_texts_list
        word_count = 0
        for text in feeds_list:
            if "Latest" in text.text.encode('utf-8'):
                word_count = word_count+1
        if word_count>=1:
            self.tstream.get_ts_threat_streams_link.click()
            self.assertTrue(word_count, "Feeds does not have searched word.")
        else:
            self.tstream.get_ts_threat_streams_link.click()
            self.assertFalse(True,"Feeds does not have searched word.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_36_To_Test_Setting_Compact_View_Save_Button(self):
        """
        Test : test_TS_36
        Description : To verify that Compact View Check Box.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_setting_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                        self.tstream._ts_setting_window_title_locator)))
        before_click = self.tstream.get_ts_setting_window_checkbox.get_attribute("class")
        self.tstream.get_ts_setting_window_checkbox.click()
        sleep(2)#Required for check box info update
        self.tstream.get_ts_setting_window_save_button.click()
        sleep(2)#Required for apps update
        self.tstream.get_ts_setting_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                        self.tstream._ts_setting_window_title_locator)))
        after_click = self.tstream.get_ts_setting_window_checkbox.get_attribute("class")
        self.tstream.get_ts_setting_window_save_button.click()
        sleep(3)#Required to make settings link enable
        self.assertNotEqual(before_click, after_click, "The Click is not happened for Compact View check box.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_37_To_Test_Setting_Compact_View_Cancel_Button(self):
        """
        Test : test_TS_37
        Description : To verify that Settings window cancel button.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_setting_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                        self.tstream._ts_setting_window_title_locator)))
        before_click = self.tstream.get_ts_setting_window_checkbox.get_attribute("class")
        self.tstream.get_ts_setting_window_checkbox.click()
        sleep(2)#Required for check box info update
        self.tstream.get_ts_setting_window_close_button.click()
        sleep(2)#Required to make settings link enable
        self.tstream.get_ts_setting_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                        self.tstream._ts_setting_window_title_locator)))
        after_click = self.tstream.get_ts_setting_window_checkbox.get_attribute("class")
        self.tstream.get_ts_setting_window_close_button.click()
        self.assertEqual(before_click, after_click, "Cancel button is not working properly.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_38_To_Test_New_Filter_Assets_Name_Add(self):
        """
        Test : test_TS_30
        Description : To verify Asset name added properly or not.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_38")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_assets_textbox.send_keys("Haystax School")
        sleep(2)
        assets_list = self.tstream.get_ts_filter_create_assets_name_list
        assets_list[0].click()
        sleep(2)
        self.tstream.get_ts_filter_create_assets_add_button.click()
        icon_list = self.tstream.get_ts_filter_create_assets_delete_icon
        if icon_list[0].is_displayed():
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertTrue(True, "Asset could not be added.")
        else:
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertFalse(True, "Asset Tag could not be added.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_39_To_Test_New_Filter_Assets_Delete(self):
        """
        Test : test_TS_39
        Description : To verify Asset name has beed deleted properly or not.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_39")
        self.tstream.show_advance_info()
        self.tstream.get_ts_filter_create_assets_textbox.send_keys("Haystax School")
        sleep(2)
        assets_list = self.tstream.get_ts_filter_create_assets_name_list
        assets_list[0].click()
        sleep(2)
        self.tstream.get_ts_filter_create_assets_add_button.click()
        icon_list = self.tstream.get_ts_filter_create_assets_delete_icon
        icon_count_before_delete = len(icon_list)
        icon_list[0].click()
        icon_list = self.tstream.get_ts_filter_create_assets_delete_icon
        icon_count_after_delete = len(icon_list)
        self.tstream.get_ts_filter_create_cancel_button.click()
        self.assertEqual(icon_count_before_delete, icon_count_after_delete+1, "Asset could not be deleted.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_40_To_Verify_Multiple_Assets_Deleted_Properly(self):
        """
        Test : test_TS_40
        Description : To verify that added assets has been deleted properly. Multiple Assets.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_40")
        self.tstream.show_advance_info()
        for num in range(3):
            self.tstream.get_ts_filter_create_assets_textbox.send_keys("Haystax School")
            sleep(1)
            assets_list = self.tstream.get_ts_filter_create_assets_name_list
            assets_list[0].click()
            sleep(1)
            self.tstream.get_ts_filter_create_assets_add_button.click()
            sleep(2)
        icon_list = self.tstream.get_ts_filter_create_assets_delete_icon
        icon_count_before_delete = len(icon_list)
        for item in icon_list[::-1]:
            item.click()
            sleep(2)
        icon_list = self.tstream.get_ts_filter_create_assets_delete_icon
        icon_count_after_delete = len(icon_list)
        self.tstream.get_ts_filter_create_cancel_button.click()
        self.assertEqual(icon_count_before_delete, icon_count_after_delete+icon_count_before_delete, "Assets could not be deleted.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_41_To_Verify_Locations_Options(self):
        """
        Test : test_TS_41
        Description : To verify that locations options(Latitude, Longitude and Radius) has been added.
        Revision:
        Author : Bijesh
        :return: None
        """
        location_value = "77"
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_41")
        self.tstream.show_advance_info()
        self.tstream.show_location_options()
        sleep(1)
        self.tstream.get_ts_filter_create_location_latitude_textbox.send_keys(location_value)
        self.tstream.get_ts_filter_create_location_longitude_textbox.send_keys(location_value)
        self.tstream.get_ts_filter_create_location_radius_textbox.send_keys(location_value)
        sleep(1)
        location_text_actual = self.tstream.get_ts_filter_create_location_text.text
        location_text_expected = 'Lat long: ['+ location_value+', '+location_value+'], radius: '+location_value+' miles'
        self.tstream.get_ts_filter_create_cancel_button.click()
        self.assertEqual(location_text_actual, location_text_expected, "Location text are not matching.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_42_To_Verify_Locations_Latitude_With_Invalid_Value(self):
        """
        Test : test_TS_42
        Description : To verify that error message for invalid value of Location Latitude.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_42")
        self.tstream.show_advance_info()
        self.tstream.show_location_options()
        sleep(1)
        self.tstream.get_ts_filter_create_location_latitude_textbox.send_keys("100")
        sleep(1)
        if self.tstream.get_ts_filter_create_location_latitude_error_message.is_displayed():
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertTrue(True, "Error message is not displayed.")
        else:
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertFalse(True, "Error message is not displayed.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_43_To_Verify_Locations_Longitude_With_Invalid_Value(self):
        """
        Test : test_TS_43
        Description : To verify that error message for invalid value of Location Longitude.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_43")
        self.tstream.show_advance_info()
        self.tstream.show_location_options()
        sleep(1)
        self.tstream.get_ts_filter_create_location_longitude_textbox.send_keys("200")
        sleep(1)
        if self.tstream.get_ts_filter_create_location_longitude_error_message.is_displayed():
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertTrue(True, "Error message is not displayed.")
        else:
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertFalse(True, "Error message is not displayed.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_44_To_Verify_Locations_Radius_With_Invalid_Value(self):
        """
        Test : test_TS_44
        Description : To verify that error message for invalid value of Location Radius.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_44")
        self.tstream.show_advance_info()
        self.tstream.show_location_options()
        sleep(1)
        self.tstream.get_ts_filter_create_location_radius_textbox.send_keys("abc")
        sleep(1)
        if self.tstream.get_ts_filter_create_location_radius_error_message.is_displayed():
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertTrue(True, "Error message is not displayed.")
        else:
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertFalse(True, "Error message is not displayed.")

    @attr(priority="high")
    #@SkipTest
    def test_TS_45_To_Verify_New_Filter_Advance_Link(self):
        """
        Test : test_TS_45
        Description : To verify that Advance link is working.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()
        sleep(2)#required to update dropdown menu
        self.tstream.get_ts_threat_dropdown_addnew_filter.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self.tstream._ts_filter_create_title_locator)))
        self.tstream.get_ts_filter_create_name_textbox.send_keys("New_Filter_TC_45")
        self.tstream.show_advance_info()
        visibility_display_status = self.tstream.get_ts_filter_create_visibility_dropdown_arrow.is_displayed()
        location_display_status = self.tstream.get_ts_filter_create_location_icon.is_displayed()
        if visibility_display_status and location_display_status:
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertTrue(True, "Advance Link is not working.")
        else:
            self.tstream.get_ts_filter_create_cancel_button.click()
            self.assertFalse(False, "Advance Link is not working.")


    @attr(priority="high")
    #@SkipTest
    def test_TS_46_To_Verify_Dashboard_Link(self):
        """
        Test : test_TS_45
        Description : To verify that Dashboard link is working.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.show_dashboard_info()
        sleep(1)
        document_graph_status = self.tstream.get_ts_dashboard_document_graph.is_displayed()
        rss_graph_status = self.tstream.get_ts_dashboard_rss_graph.is_displayed()
        twitter_graph_status = self.tstream.get_ts_dashboard_twitter_graph.is_displayed()
        if document_graph_status and rss_graph_status and twitter_graph_status:
            self.assertTrue(True, "Dashboard does not displays all graphs.")
        else:
            self.assertFalse(True, "Dashboard does not displays all graphs.")
