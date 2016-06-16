from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.fieldinterviewspage import FieldInterviewsPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from time import sleep
import ConfigParser
from lib.pagination import Pagination
from selenium.webdriver.common.keys import Keys
from nose.plugins.skip import SkipTest

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
    def test_FI_001_to_test_periodic_refresh_checkbox(self):
        """
        Test : test_FI_01
        Description : This test will check periodic refresh check box functionality.
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
    def test_FI_002_to_test_alert_on_new_fi_checkbox(self):
        """
        Test : test_FI_002
        Description : This test will check alert on new FI check box functionality.
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
    def test_FI_003_to_test_settings_window_badge_number_textbox(self):
        """
        Test : test_FI_003
        Description : This test will check Settings window Badge Number text box functionality.
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
    def test_FI_004_to_test_settings_window_rank_textbox(self):
        """
        Test : test_FI_004
        Description : This test will check Settings window Rank text box functionality..
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
    def test_FI_005_to_test_settings_window_cancel_button(self):
        """
        Test : test_FI_005
        Description : This test will check Settings window Cancel button functionality.
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

    @attr(priority="high")
    #@SkipTest
    def test_FI_006_to_test_contact_type_gang_activity_option(self):
        """
        Test : test_FI_006
        Description : This test will check Gang Activity option of Contact Type drop down menu functionality.
        Revision:
        Author : Bijesh
        :return: None
        """
        filter_text = r"Gang Activity"
        self.fieldinterviewspage.get_contact_type_drop_down.click()
        sleep(1)
        self.fieldinterviewspage.get_contact_type_gang_option.click()
        sleep(5)
        selected_filter_text = self.fieldinterviewspage.get_selected_filter_button_text.text
        filters_name_list = self.fieldinterviewspage.get_selected_filter_column_text
        sleep(1)
        if selected_filter_text == filter_text:
            for name in filters_name_list:
                column_text = name.text
                if column_text != filter_text:
                    self.fieldinterviewspage.get_fi_reset_filters_button.click()
                    self.assertFalse(filter_text, "Gang Activity filter is not selected properly.")
                    break
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertTrue(filter_text, "Gang Activity filter is not selected properly.")
        else:
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertFalse(filter_text, "Gang Activity filter is not selected properly.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_007_to_test_contact_type_suspicious_circumstances_activity_option(self):
        """
        Test : test_FI_007
        Description : This test will check Suspicious Circumstances option of Contact Type drop down menu functionality.
        Revision:
        Author : Bijesh
        :return: None
        """
        filter_text = r"Suspicious Circumstances"
        self.fieldinterviewspage.get_contact_type_drop_down.click()
        sleep(1)
        self.fieldinterviewspage.get_contact_type_circumstances_option.click()
        sleep(5)
        selected_filter_text = self.fieldinterviewspage.get_selected_filter_button_text.text
        filters_name_list = self.fieldinterviewspage.get_selected_filter_column_text
        sleep(1)
        if selected_filter_text == filter_text:
            for name in filters_name_list:
                column_text = name.text
                if column_text != filter_text:
                    self.fieldinterviewspage.get_fi_reset_filters_button.click()
                    self.assertFalse(filter_text, "Suspicious Circumstances filter is not selected properly.")
                    break
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertTrue(filter_text, "Suspicious Circumstances filter is not selected properly.")
        else:
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertFalse(filter_text, "Suspicious Circumstances filter is not selected properly.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_008_to_test_contact_type_probation_option(self):
        """
        Test : test_FI_008
        Description : This test will check Probation option of Contact Type drop down menu functionality.
        Revision:
        Author : Bijesh
        :return: None
        """
        filter_text = r"Probation"
        self.fieldinterviewspage.get_contact_type_drop_down.click()
        sleep(1)
        self.fieldinterviewspage.get_contact_type_probation_option.click()
        sleep(5)
        selected_filter_text = self.fieldinterviewspage.get_selected_filter_button_text.text
        filters_name_list = self.fieldinterviewspage.get_selected_filter_column_text
        sleep(1)
        if selected_filter_text == filter_text:
            for name in filters_name_list:
                column_text = name.text
                if column_text != filter_text:
                    self.fieldinterviewspage.get_fi_reset_filters_button.click()
                    self.assertFalse(filter_text, "Probation filter is not selected properly.")
                    break
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertTrue(filter_text, "Probation filter is not selected properly.")
        else:
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertFalse(filter_text, "Probation filter is not selected properly.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_009_to_test_contact_type_suspicious_person_option(self):
        """
        Test : test_FI_009
        Description : This test will check Suspicious Person option of Contact Type drop down menu functionality.
        Revision:
        Author : Bijesh
        :return: None
        """
        filter_text = r"Suspicious Person"
        self.fieldinterviewspage.get_contact_type_drop_down.click()
        sleep(1)
        self.fieldinterviewspage.get_contact_type_person_option.click()
        sleep(5)
        selected_filter_text = self.fieldinterviewspage.get_selected_filter_button_text.text
        filters_name_list = self.fieldinterviewspage.get_selected_filter_column_text
        sleep(1)
        if selected_filter_text == filter_text:
            for name in filters_name_list:
                column_text = name.text
                if column_text != filter_text:
                    self.fieldinterviewspage.get_fi_reset_filters_button.click()
                    self.assertFalse(filter_text, "Suspicious Person filter is not selected properly.")
                    break
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertTrue(filter_text, "Suspicious Person filter is not selected properly.")
        else:
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertFalse(filter_text, "Suspicious Person filter is not selected properly.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_010_to_test_contact_type_suspicious_vehicle_option(self):
        """
        Test : test_FI_010
        Description : This test will check Suspicious Vehicle option of Contact Type drop down menu functionality.
        Revision:
        Author : Bijesh
        :return: None
        """
        filter_text = r"Suspicious Vehicle"
        self.fieldinterviewspage.get_contact_type_drop_down.click()
        sleep(1)
        self.fieldinterviewspage.get_contact_type_vehicle_option.click()
        sleep(5)
        selected_filter_text = self.fieldinterviewspage.get_selected_filter_button_text.text
        filters_name_list = self.fieldinterviewspage.get_selected_filter_column_text
        sleep(1)
        if selected_filter_text == filter_text:
            for name in filters_name_list:
                column_text = name.text
                if column_text != filter_text:
                    self.fieldinterviewspage.get_fi_reset_filters_button.click()
                    self.assertFalse(filter_text, "Suspicious Vehicle filter is not selected properly.")
                    break
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertTrue(filter_text, "Suspicious Vehicle filter is not selected properly.")
        else:
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertFalse(filter_text, "Suspicious Vehicle filter is not selected properly.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_011_to_test_contact_type_traffic_stop_option(self):
        """
        Test : test_FI_011
        Description : This test will check Traffic Stop option of Contact Type drop down menu functionality.
        Revision:
        Author : Bijesh
        :return: None
        """
        filter_text = r"Traffic Stop"
        self.fieldinterviewspage.get_contact_type_drop_down.click()
        sleep(1)
        self.fieldinterviewspage.get_contact_type_traffic_option.click()
        sleep(5)
        selected_filter_text = self.fieldinterviewspage.get_selected_filter_button_text.text
        filters_name_list = self.fieldinterviewspage.get_selected_filter_column_text
        sleep(1)
        if selected_filter_text == filter_text:
            for name in filters_name_list:
                column_text = name.text
                if column_text != filter_text:
                    self.fieldinterviewspage.get_fi_reset_filters_button.click()
                    self.assertFalse(filter_text, "Traffic Stop filter is not selected properly.")
                    break
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertTrue(filter_text, "Traffic Stop filter is not selected properly.")
        else:
            self.fieldinterviewspage.get_fi_reset_filters_button.click()
            self.assertFalse(filter_text, "Traffic Stop filter is not selected properly.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_012_to_test_reset_button(self):
        """
        Test : test_FI_012
        Description : This test will check Reset Button functionality.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.fieldinterviewspage.get_contact_type_drop_down.click()
        sleep(1)
        self.fieldinterviewspage.get_contact_type_traffic_option.click()
        sleep(3)
        filter_text_before = self.fieldinterviewspage.get_selected_filter_button_text.text
        self.fieldinterviewspage.get_fi_reset_filters_button.click()
        sleep(2)
        filter_text_after = self.fieldinterviewspage.get_selected_filter_button_text.text
        if filter_text_after == r"Contact type" and filter_text_after != filter_text_before:
            self.assertTrue(filter_text_after, "Filter could not be reset.")
        else:
            self.assertFalse(filter_text_after, "Filter could not be reset.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_013_to_test_search_textbox_with_valid_string(self):
        """
        Test : test_FI_013
        Description : This test will check Search Text box functionality with valid search string.
        Revision:
        Author : Bijesh
        :return: None
        """
        search_text = r"Traffic Stop"
        self.fieldinterviewspage.get_fi_search_textbox.send_keys(search_text)
        self.fieldinterviewspage.get_fi_search_textbox.send_keys(Keys.ENTER)
        sleep(5)
        filters_name_list = self.fieldinterviewspage.get_selected_filter_column_text
        sleep(1)
        for name in filters_name_list:
            column_text = name.text
            if column_text != search_text:
                self.fieldinterviewspage.get_fi_search_textbox.clear()
                self.fieldinterviewspage.get_fi_search_textbox.send_keys("")
                sleep(2)
                self.assertFalse(search_text, "Searched text is not appearing in the field interviews list.")
                break
        self.fieldinterviewspage.get_fi_search_textbox.clear()
        self.fieldinterviewspage.get_fi_search_textbox.send_keys("")
        sleep(2)
        self.assertTrue(search_text, "Searched text is not appearing in the field interviews list.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_014_to_test_search_textbox_with_invalid_string(self):
        """
        Test : test_FI_014
        Description : This test will check Search Text box functionality with invalid search string.
        Revision:
        Author : Bijesh
        :return: None
        """
        search_text = r"qwertyuiop1()_"
        self.fieldinterviewspage.get_fi_search_textbox.send_keys(search_text)
        self.fieldinterviewspage.get_fi_search_textbox.send_keys(Keys.ENTER)
        sleep(5)
        error_message = self.fieldinterviewspage.get_fi_search_error_message.text
        if error_message == r"No matching records found":
            self.fieldinterviewspage.get_fi_search_textbox.send_keys(Keys.CONTROL+'a')
            self.fieldinterviewspage.get_fi_search_textbox.send_keys(Keys.DELETE)
            sleep(3)
            self.assertTrue(error_message, "Either error message is not appears or wrong Error message.")
        else:
            self.fieldinterviewspage.get_fi_search_textbox.send_keys(Keys.CONTROL+'a')
            self.fieldinterviewspage.get_fi_search_textbox.send_keys(Keys.DELETE)
            sleep(3)
            self.assertFalse(error_message, "Either error message is not appears or wrong Error message.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_015_to_test_delete_window_cancel_button(self):
        """
        Test : test_FI_015
        Description : This test will check Search Text box functionality with invalid search string.
        Revision:
        Author : Bijesh
        :return: None
        """
        fi_count_before = self.fieldinterviewspage.field_interviews_count()
        check_boxes = self.fieldinterviewspage.get_field_interviews_checkboxes
        if check_boxes[0].get_attribute("class") == "checkbox":
            check_boxes[0].click()
            sleep(1)
        self.fieldinterviewspage.get_field_interviews_select_action_drop_down.click()
        self.fieldinterviewspage.get_field_interviews_select_action_delete_option.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                    self.fieldinterviewspage._fi_delete_window_heading_text_locator)))
        self.fieldinterviewspage.get_fi_delete_window_cancel_button.click()
        sleep(1)
        fi_count_after = self.fieldinterviewspage.field_interviews_count()
        if fi_count_after == fi_count_before:
            self.assertTrue(True, "In Delete Confirmation window cancel button is not working.")
        else:
            self.assertFalse(True, "In Delete Confirmation window cancel button is not working.")

    @attr(priority="high")
    @SkipTest
    def test_FI_016_to_test_delete_window_delete_button(self):
        """
        Test : test_FI_016
        Description :  This test will check Search Text box functionality with invalid search string.
        Revision:
        Author : Bijesh
        :return: None
        """
        fi_count_before = self.fieldinterviewspage.field_interviews_count()
        check_boxes = self.fieldinterviewspage.get_field_interviews_checkboxes
        if check_boxes[0].get_attribute("class") == "checkbox":
            check_boxes[0].click()
            sleep(1)
        self.fieldinterviewspage.get_field_interviews_select_action_drop_down.click()
        self.fieldinterviewspage.get_field_interviews_select_action_delete_option.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                    self.fieldinterviewspage._fi_delete_window_heading_text_locator)))

        self.fieldinterviewspage.get_fi_delete_window_delete_button.click()
        sleep(4)
        fi_count_after = self.fieldinterviewspage.field_interviews_count()
        if fi_count_after+1 == fi_count_before:
            self.assertTrue(True, "In Delete Confirmation window Delete button is not working.")
        else:
            self.assertFalse(True, "In Delete Confirmation window Delete button is not working.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_017_to_test_pagination_next_button(self):
        """
        Test : test_FI_017
        Description : To Test pagination next button.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        self.pagination.pagination_previous()
        sleep(2)
        current_page_num = self.pagination.pagination_active_page()
        self.pagination.pagination_next()
        sleep(2)
        next_page_num = self.pagination.pagination_active_page()
        self.assertEqual(next_page_num, current_page_num + 1,"The next button click is not working.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_018_to_test_pagination_next_button_disabled(self):
        """
        Test : test_FI_018
        Description :To Test pagination next button. Last Page is active.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        self.pagination.pagination_drop_down_click(-1)
        sleep(2)
        current_page_num = self.pagination.pagination_active_page()
        total_pages = self.pagination.pagination_total_pages()
        flag = 1
        while flag:
            if int(current_page_num) == int(total_pages):
                flag = 0
            else:
                self.pagination.pagination_next()
                current_page_num = self.pagination.pagination_active_page()
        next_page_num = self.pagination.pagination_active_page()
        self.assertEqual(current_page_num, next_page_num, "Next Arrow button is not disabled.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_019_to_test_pagination_previous_button(self):
        """
        Test : test_FI_019
        Description :To Test pagination previous button.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        self.pagination.pagination_next()
        current_page_num = self.pagination.pagination_active_page()
        self.pagination.pagination_previous()
        sleep(2)
        previous_page_num = self.pagination.pagination_active_page()
        self.assertEqual(previous_page_num, current_page_num - 1, "The Previous button click is not working.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_020_to_test_pagination_previous_button_disabled(self):
        """
        Test : test_FI_020
        Description :To Test pagination previous button. First page is active.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        self.pagination.pagination_drop_down_click(0)
        sleep(2)
        current_page_num = self.pagination.pagination_active_page()
        flag = 1
        while flag:
            if int(current_page_num) == int(1):
                flag = 0
            else:
                self.pagination.pagination_previous()
                current_page_num = self.pagination.pagination_active_page()
        previous_page_num = self.pagination.pagination_active_page()
        self.assertEqual(current_page_num, previous_page_num, "Previous Arrow button is not disabled.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_021_to_test_pagination_page_group_select(self):
        """
        Test : test_FI_021
        Description :To verify that page group is selected from drop down menu
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        self.pagination.get_pg_drop_down_arrow.click()
        sleep(1)
        list_of_page_drop_down = self.pagination.get_pg_list_of_page_groups
        sleep(1)
        self.pagination.get_pg_drop_down_arrow.click()
        sleep(1)
        if len(list_of_page_drop_down)>=1:
            self.pagination.pagination_drop_down_click(-1)
            self.pagination.get_pg_drop_down_arrow.click()
            sleep(1)
            list_of_page_drop_down = self.pagination.get_pg_list_of_page_groups
            sleep(1)
            self.pagination.get_pg_drop_down_arrow.click()
            page_list = ((list_of_page_drop_down[-1]).text.encode('utf-8')).split("-")
            last_page = int(page_list[-1])
            last_page_first = int(page_list[0])
            self.pagination.get_pg_drop_down_arrow.click()
            if int(last_page) >= 5:
                first_page = int(last_page)-4
            else:
                first_page = last_page_first
            start_value, end_value = self.pagination.pagination_start_end_node_value()
            actual_group = [str(start_value), str(end_value)]
            expected_group = [str(first_page), str(last_page)]
            self.assertListEqual(actual_group, expected_group, "Selected Group value is not matching with Actual.")
        else:
            self.skipTest("There is only one page available.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_022_to_test_direct_click_first_page(self):
        """
        Test : test_FI_022
        Description :To verify that first page is selected directly and previous button is disabled.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        page_count = self.pagination.pagination_total_pages()
        list_of_nodes = self.pagination.get_pg_list_of_nodes
        if str(page_count) == str(1):
            previous_node_value = list_of_nodes[0].get_attribute("class")
            next_node_value = list_of_nodes[-1].get_attribute("class")
            if (previous_node_value == "previous disabled") and (next_node_value == "next disabled"):
                self.assertTrue(True, "There is only one page and next/previous button is enabled.")
            else:
                self.assertFalse(True, "There is only one page and next/previous button is enabled.")

        elif str(page_count) > str(1):
            self.pagination.pagination_drop_down_click(0)
            sleep(2)
            list_of_nodes = self.pagination.get_pg_list_of_nodes
            sleep(2)
            list_of_nodes[1].click()
            sleep(2)
            if list_of_nodes[0].get_attribute("class") == "previous disabled":
                self.assertTrue(True, "Current Page number is One but previous button is enabled.")
            else:
                self.assertFalse(True, "Current Page number is One but previous button is enabled.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_023_to_test_direct_click_last_page(self):
        """
        Test : test_FI_023
        Description :To verify that last page is selected directly and next button is disabled.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        page_count = self.pagination.pagination_total_pages()
        list_of_nodes = self.pagination.get_pg_list_of_nodes
        if str(page_count) == str(1):
            previous_node_value = list_of_nodes[0].get_attribute("class")
            next_node_value = list_of_nodes[-1].get_attribute("class")
            if (previous_node_value == "previous disabled") and (next_node_value == "next disabled"):
                self.assertTrue(True, "There is only one page and next/previous button is enabled.")
            else:
                self.assertFalse(True, "There is only one page and next/previous button is enabled.")
        elif str(page_count) > str(1):
            self.pagination.pagination_drop_down_click(-1)
            sleep(2)
            list_of_nodes = self.pagination.get_pg_list_of_nodes
            list_of_nodes[-3].click()
            self.pagination.pagination_next()
            sleep(2)
            if list_of_nodes[-1].get_attribute("class") == "next disabled":
                self.assertTrue(True, "Displayed Page is last page but next button is enabled.")
            else:
                self.assertFalse(True, "Displayed Page is last page but next button is enabled.")

    @attr(priority="high")
    #@SkipTest
    def test_FI_024_to_test_search_field_interviews_pagination(self):
        """
        Test : test_FI_024
        Description :To verify that if searched field interviews is not available than pagination should be disabled.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        self.fieldinterviewspage.get_fi_search_textbox.send_keys("1qwertyuiop*^!+")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element
                   ((By.XPATH, self.fieldinterviewspage._fi_search_error_message_locator), "No matching records found"))
        if self.fieldinterviewspage.get_fi_search_error_message.is_displayed():
            list_of_nodes = self.pagination.get_pg_list_of_nodes
            node_length = len(list_of_nodes)
            previous_node_text = list_of_nodes[0].get_attribute("class")
            next_node_text = list_of_nodes[-1].get_attribute("class")
            sleep(2)
            if(previous_node_text == "previous disabled") and (next_node_text == "next disabled") and (node_length==3):
                self.assertTrue(True, "No Pages available but still next and previous button is enabled.")
            else:
                self.assertFalse(True, "No Pages available but still next and previous button is enabled.")

