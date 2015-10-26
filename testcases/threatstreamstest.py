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
    @attr(status='smoke')
    def test_threat_steams(self):
        #tstream = ThreatStreamPage(self.driver)
        # WebDriverWait(self.driver,20).until(EC.presence_of_element_located(By.XPATH, tstream._ts_app_name_text))
        self.assertEqual(self.tstream.get_ts_app_name.text, "Threat Streams")

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
    def test_TS_13(self):
        """
        Test : test_TS_04
        Description : To verify that filter type is selected as Trending Last Hour.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.tstream.get_ts_threat_dropdown_filter.click()