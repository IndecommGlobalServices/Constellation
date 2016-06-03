from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.fieldinterviewspage import FieldInterviewsPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from time import sleep
import ConfigParser
from lib.pagination import Pagination

class FieldinterviewsTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(FieldinterviewsTest, cls).setUpClass()
        cls.fieldinterviewspage = FieldInterviewsPage(cls.driver)
        cls.pagination = Pagination(cls.driver)
        cls.fieldinterviewspage.open_field_interviews_app()
        cls.section = 'FieldInterviewsMessages'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))

    def setUp(self):
        self.errors_and_failures = self.tally()
        WebDriverWait(self.driver, 50). until(EC.presence_of_element_located(
            (By.XPATH, self.fieldinterviewspage._fi_select_action_drop_down_locator)))

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        self.fieldinterviewspage.return_to_apps_main_page()

    @attr(priority="high")
    #@SkipTest
    def test_FI_001(self):
        """
        Test : test_FI_01
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.fieldinterviewspage.get_field_interviews_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                         self.fieldinterviewspage._fi_settings_window_heading_locator)))

        before_click = self.fieldinterviewspage.get_fi_settings_window_periodic_refresh_checkbox.get_attribute("class")
        self.fieldinterviewspage.get_fi_settings_window_periodic_refresh_checkbox.click()
        sleep(2)#Required for check box info update
        self.fieldinterviewspage.get_fi_settings_window_save_button.click()
        sleep(2)#Required for apps update
        self.fieldinterviewspage.get_field_interviews_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                         self.fieldinterviewspage._fi_settings_window_heading_locator)))
        after_click = self.fieldinterviewspage.get_fi_settings_window_periodic_refresh_checkbox.get_attribute("class")
        sleep(2)#Required for apps update
        self.fieldinterviewspage.get_fi_settings_window_close_button.click()
        self.assertNotEqual(before_click, after_click, "The Click is not happened for Periodic Refresh check box.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_002(self):
        """
        Test : test_FI_002
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """
        self.fieldinterviewspage.get_field_interviews_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                         self.fieldinterviewspage._fi_settings_window_heading_locator)))
        before_click = self.fieldinterviewspage.get_fi_settings_window_alert_on_new_fi_checkbox.get_attribute("class")
        self.fieldinterviewspage.get_fi_settings_window_alert_on_new_fi_checkbox.click()
        sleep(2)#Required for check box info update
        self.fieldinterviewspage.get_fi_settings_window_save_button.click()
        sleep(2)#Required for apps update
        self.fieldinterviewspage.get_field_interviews_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                         self.fieldinterviewspage._fi_settings_window_heading_locator)))
        after_click = self.fieldinterviewspage.get_fi_settings_window_alert_on_new_fi_checkbox.get_attribute("class")
        sleep(2)#Required for apps update
        self.fieldinterviewspage.get_fi_settings_window_close_button.click()
        self.assertNotEqual(before_click, after_click, "The Click is not happened for Alert on new FI check box.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_003(self):
        """
        Test : test_FI_003
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """
        text_value = "200"
        self.fieldinterviewspage.get_field_interviews_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                         self.fieldinterviewspage._fi_settings_window_heading_locator)))
        sleep(2)
        self.fieldinterviewspage.get_fi_settings_window_badge_number_textbox.clear()
        self.fieldinterviewspage.get_fi_settings_window_badge_number_textbox.send_keys(text_value)
        self.fieldinterviewspage.get_fi_settings_window_save_button.click()
        sleep(2)
        self.fieldinterviewspage.get_field_interviews_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                         self.fieldinterviewspage._fi_settings_window_heading_locator)))
        act_text_value = self.fieldinterviewspage.get_fi_settings_window_badge_number_textbox.get_attribute("value")
        self.fieldinterviewspage.get_fi_settings_window_close_button.click()
        self.assertEqual(text_value, act_text_value, "Entered text and actual text values are not matching.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_004(self):
        """
        Test : test_FI_004
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """
        text_value = "500"
        self.fieldinterviewspage.get_field_interviews_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                         self.fieldinterviewspage._fi_settings_window_heading_locator)))
        sleep(2)
        self.fieldinterviewspage.get_fi_settings_window_rank_textbox.clear()
        self.fieldinterviewspage.get_fi_settings_window_rank_textbox.send_keys(text_value)
        self.fieldinterviewspage.get_fi_settings_window_save_button.click()
        sleep(2)
        self.fieldinterviewspage.get_field_interviews_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                         self.fieldinterviewspage._fi_settings_window_heading_locator)))
        act_text_value = self.fieldinterviewspage.get_fi_settings_window_rank_textbox.get_attribute("value")
        self.fieldinterviewspage.get_fi_settings_window_close_button.click()
        self.assertEqual(text_value, act_text_value, "Entered text and actual text values are not matching.")


    @attr(priority="high")
    #@SkipTest
    def test_FI_005(self):
        """
        Test : test_FI_004
        Description : .
        Revision:
        Author : Bijesh
        :return: None
        """
        text_value = "700"
        self.fieldinterviewspage.get_field_interviews_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                         self.fieldinterviewspage._fi_settings_window_heading_locator)))
        sleep(2)
        self.fieldinterviewspage.get_fi_settings_window_rank_textbox.clear()
        self.fieldinterviewspage.get_fi_settings_window_rank_textbox.send_keys(text_value)
        self.fieldinterviewspage.get_fi_settings_window_close_button.click()
        sleep(2)
        self.fieldinterviewspage.get_field_interviews_settings_link.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                         self.fieldinterviewspage._fi_settings_window_heading_locator)))
        act_text_value = self.fieldinterviewspage.get_fi_settings_window_rank_textbox.get_attribute("value")
        self.fieldinterviewspage.get_fi_settings_window_close_button.click()
        self.assertNotEqual(text_value, act_text_value, "Entered text and actual text values are matching.")