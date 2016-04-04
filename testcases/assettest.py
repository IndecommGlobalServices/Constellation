import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from pages.assetpage import AssetPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from time import sleep
import json, os, re, inspect
from selenium.webdriver.common.action_chains import ActionChains
import ConfigParser
from lib.pagination import Pagination

class AssetpageTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(AssetpageTest, cls).setUpClass()
        cls.assetpage = AssetPage(cls.driver)
        cls.pagination = Pagination(cls.driver)
        cls.assetpage.open_asset_app()
        cls.section = 'Messages'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))

    def setUp(self):
        self.errors_and_failures = self.tally()
        WebDriverWait(self.driver, 50). until(EC.presence_of_element_located(
            (By.XPATH, self.assetpage._asset_select_action_delete_select_xpath_locator)))

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        self.assetpage.return_to_apps_main_page()

    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_asset_smoke(self):
        self.assertTrue(self.assetpage.get_asset_create_asset, "Create assest button not available")
        self.assertTrue(self.assetpage.get_filter_drop_down.is_displayed(), "Type filter dropdown not available")
        self.assertTrue(self.assetpage.get_asset_select_action_drop_down.is_displayed(), "Select action dropdown not available")
        self.assertTrue(self.assetpage.get_asset_reset_button.is_displayed(), "Reset button not available")
        self.assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_001(self):
        """
        Test : test_AS_01
        Description : To verify delete functionality when no assets are available. Delete button should be disabled.
        Revision:
        Author : Kiran
        :return: None
        """
        self.assetpage.get_asset_select_action_drop_down.click()
        if len(self.assetpage.get_asset_name_list)<= 0:
            self.assertFalse(self.assetpage.get_asset_link_delete_text.is_enabled(),
                             self.config.get(self.section, 'MESSAGE_WHEN_NO_ASSETS_AVAILABLE'))
        else:
            self.skipTest(self.config.get(self.section, 'MESSAGE_TEST_CAN_NOT_BE_VALIDATED'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_002(self):
        """
        Test : test_AS_02
        Description : To verify delete functionality when no asset is selected. Delete button should be disabled.
        Revision:
        Author : Kiran
        :return: None
        """
        self.assetpage.get_select_checkbox_in_grid()
        self.assetpage.get_asset_select_action_drop_down.click()
        state = self.assetpage.get_asset_link_delete_text.is_enabled()
        sleep(1)
        self.assetpage.get_asset_select_action_drop_down.click()
        self.assertFalse(state,
                         self.config.get(self.section, 'MESSAGE_WHEN_NO_ASSETS_AVAILABLE'))


    @attr(priority="high")
    #@SkipTest
    def test_AS_003(self):
        """
        Test : test_AS_03
        Description : To verify delete functionality. User selected asset should be deleted.
        Revision:
        Author : Kiran
        :return: None
        """
        countbeforedeletion = self.assetpage.get_total_row_count()
        self.assetpage.get_asset_list_first_check_box.click()
        self.assetpage.get_asset_select_action_drop_down.click()
        self.assetpage.get_asset_link_delete_text.click()
        self.assetpage.get_asset_delete_button.click() # Delete
        sleep(2)
        countafterdeletion = self.assetpage.get_total_row_count()
        sleep(2)
        self.assertEqual(int(countbeforedeletion), int(countafterdeletion)+1,
                         self.config.get(self.section, 'MESSAGE_COULD_NOT_DELETE_ASSET'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_004(self):
        """
        Test : test_AS_04
        Description : To verify delete window cancel button functionality.
        Revision:
        Author : Kiran
        :return: None
        """
        sleep(2)
        countbeforedeletion = self.assetpage.get_total_row_count()
        self.assetpage.get_asset_list_first_check_box.click()
        self.assetpage.get_asset_select_action_drop_down.click()
        self.assetpage.get_asset_link_delete_text.click()
        self.assetpage.get_deleteasset_cancel_button.click() # Cancel
        sleep(2)
        countafterdeletion = self.assetpage.get_total_row_count()
        sleep(2)
        self.assertEqual(int(countbeforedeletion), int(countafterdeletion),
                         self.config.get(self.section, 'MESSAGE_ASSET_DELETED_ON_CANCEL'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_006(self):
        """
        Test : test_AS_06
        Description : To verify filter functionality. Check whether type filter has 'Place' option or not.
        Revision:
        Author : Kiran
        :return: None
        """
        self.assetpage.asset_filter_based_on_place_and_school('Place')
        asset_filter_text = self.assetpage.get_asset_type_filter_text.text
        self.assertEqual('Place', str(asset_filter_text),self.config.get(self.section, 'MESSAGE_INVALID_FILTER') )
        self.assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_007(self):
        """
        Test : test_AS_07
        Description : To verify filter functionality. Check whether type filter has 'School' option or not.
        Revision:
        Author : Kiran
        :return: None
        """
        self.assetpage.asset_filter_based_on_place_and_school('School')
        asset_filter_text = self.assetpage.get_asset_type_filter_text.text
        self.assertEqual('School', str(asset_filter_text),self.config.get(self.section, 'MESSAGE_INVALID_FILTER') )
        self.assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_008(self):
        """
        Test : test_AS_08
        Description : To verify filter functionality. Select 'School/District' filter.
        Revision:
        Author : Kiran
        :return: None
        """
        self.assetpage.get_asset_school_district()
        for item in self.assetpage.select_asset_schooltype_district_column:
            district_text = self.assetpage.selecteddistrict
            self.assertEqual(str(district_text), item.text,
                             self.config.get(self.section, 'MESSAGE_INVALID_RESULT_ON_FILTER'))
        self.assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_009(self):
        """
        Test : test_AS_09
        Description : To verify filter functionality. Select 'School/Grade' filter.
        Revision:
        Author: Kiran
        :return: None
        """
        self.assetpage.get_asset_school_grade()
        for item in self.assetpage.select_asset_schooltype_grade_column:
            self.assertEqual(self.assetpage.selectedgrade, item.text,
                             self.config.get(self.section, 'MESSAGE_INVALID_RESULT_ON_FILTER'))
        self.assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_010(self):
        """
        Test : test_AS_10
        Description : To verify filter functionality. Select 'School/School Type' filter.
        Author: Kiran
        Revision:
        :return: None
        """
        self.assetpage.get_asset_reset_button.click()
        self.assetpage.get_asset_school_type()
        for item in self.assetpage.select_asset_schooltype_column:
            self.assertEqual(self.assetpage.selectedtype, item.text,
                             self.config.get(self.section, 'MESSAGE_INVALID_RESULT_ON_FILTER'))
        self.assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_011(self):
        """
        Test : test_AS_11
        Description : To verify Reset Filters buttons functionality. Select 'School/School Type' filter.
        Revision:
        Author : Kiran
        :return: None
        """
        self.assetpage.asset_filter_based_on_place_and_school('Place')
        asset_filter_text = self.assetpage.get_asset_type_filter_text.text
        self.assetpage.get_asset_reset_button.click()
        expectedAfterResetFilter = self.assetpage.get_asset_type_filter_text.text
        if str(asset_filter_text) == str(expectedAfterResetFilter):
            self.assertFalse(expectedAfterResetFilter, "Filters are not reset.")
        else:
            self.assertEqual('Asset type',expectedAfterResetFilter, "Filters are not reset.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_012(self):
        """
        Test : test_AS_12
        Description : To verify Search text box functionality. Enter multiple string.
        Revision:
        Author : Kiran
        :return: None
        """
        flag = 0
        cwd = os.getcwd()
        os.chdir('..')
        searchasset_filepath = os.path.join(os.getcwd(), "data", "json_SearchAssessments.json")
        os.chdir(cwd)
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(
            (By.XPATH, self.assetpage._asset_select_action_delete_select_xpath_locator)))
        with open(searchasset_filepath) as data_file:
            for each in json.load(data_file):
                searchText = each["Search_name"]
                self.assetpage.select_asset_search_text_box.clear()
                self.assetpage.select_asset_search_text_box.send_keys(searchText)
                sleep(5)
                if len(self.driver.find_elements_by_xpath(self.assetpage._asset_list_locator)) <= 0:
                    self.assertEqual("No matching records found", self.assetpage.get_asset_list_no_matching_records_found.text,
                                         self.config.get(self.section, 'MESSAGE_NO_ASSET_RECORDS'))
                    flag = 1
                else:
                    for searchName in self.driver.find_elements_by_xpath(self.assetpage._asset_list_locator):
                        if searchText in searchName.text:
                            flag = 1
                self.assertTrue(flag == 1, "The search result doesnt contain the text that is searched. "
                                           "Searched string is :" + searchText)
            self.assetpage.select_asset_search_text_box.clear()

    @attr(priority="high")
    #@SkipTest
    def test_AS_014_and_017(self):
        """
        Test : test_AS_14_and_17
        Description : To create place asset and verify that asset is created properly.
        Revision:
        Author : Kiran
        :return: None
        """
        check = 0
        self.assetpage.create_asset("Place")
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_name_breadcrumb), self.assetpage.get_asset_name_breadcrumb.text))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                    (By.LINK_TEXT, self.assetpage._asset_link_locator))).click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, self.assetpage._asset_select_action_delete_select_xpath_locator)))
        self.assetpage.asset_search_assetname(self.assetpage.asset_place_name)
        #sleep(5) # Necessary sleep to let the app search for the input string
        for item in self.assetpage.get_asset_list_background:
            if (item.text  == self.assetpage.asset_place_name) and (item.value_of_css_property("background-color")\
                                                                == "rgba(255, 236, 158, 1)"):
                check = 1
                break
        self.assetpage.textbox_clear(self.driver.find_element_by_xpath(self.assetpage._asset_search_textbox_locator))
        self.assertFalse(check == 0, self.config.get(self.section,'MESSAGE_NEW_ASSET_NOT_APPEARING_ON_YELLOW_BACKGROUND'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_015(self):
        """
        Test : test_AS_15
        Description : To verify New Asset Name field.
        Revision:
        :return: None
        """
        self.assetpage.asset_create_click()
        self.assetpage.select_asset_template_type("Place")
        self.assetpage.enter_asset_type_name.send_keys("")#Clear the text filed and leave it without any value
        self.assertFalse(self.assetpage.get_asset_overview_save_button.is_enabled(),
                         self.config.get(self.section,'MESSAGE_SAVE_BUTTON_IS_NOT_DISABLED'))
        self.assetpage.asset_overview_cancel_click()


    @attr(priority="high")
    #@SkipTest
    def test_AS_016(self):
        """
        Test : test_AS_16
        Description : To verify New Asset phone field.
        Revision:
        :return: None
        """
        self.assetpage.asset_create_click()
        self.assetpage.select_asset_template_type("Place")
        asset_phone = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH ,self.assetpage._asset_overview_phone_text_box_locator)))
        asset_phone.send_keys("123abc1234")
        asset_phone.send_keys(Keys.TAB)
        regex = re.compile(r'^\(?([0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([0-9]{4})$')
        self.assertRegexpMatches("123abc1234", regex,
                                 self.config.get(self.section, 'MESSAGE_PHONE_VALUE_NOT_MATCHING'))
        self.assetpage.asset_overview_cancel_click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_018(self):
        """
        Test : test_AS_18
        Description : To verify cancel button functionality of New asset window. Without any data entry.
        Revision:
        :return: None
        """
        self.assetpage.asset_create_click()
        self.assetpage.asset_overview_cancel_click()
        expectedAfterResetFilter = self.assetpage.get_asset_type_filter_text.text
        self.assertEqual("Asset type",expectedAfterResetFilter)# Checking "Asset Type" displayed after reset


    @attr(priority="high")
    #@SkipTest
    def test_AS_019(self):
        """
        Test : test_AS_19
        Description : To verify cancel button functionality of New asset window. With required date entry.
        Revision:
        Author : Kiran
        :return: None
        """
        self.assetpage.asset_create_click()
        self.assetpage.create_place_asset()
        self.assetpage.asset_overview_cancel_click()
        expectedAfterResetFilter = self.assetpage.get_asset_type_filter_text.text
        self.assertEqual("Asset type",expectedAfterResetFilter)# Checking "Asset Type" displayed after reset

    @attr(priority="high")
    #@SkipTest
    def test_AS_020(self):
        """
        Test : test_AS_20
        Description : To edit overview section. Enter all required fields info and click on save button.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_details_edit_widget_locator), r"Details"))
        self.assetpage.get_asset_overview_edit_link.click()
        self.assetpage.set_place_overview_fields(r"Ind address", r"Ind address 2", r"Ind city", r"KA", r"94821", r"Indecomm")
        self.assetpage.asset_overview_save_click()# Click on Save
        self.assertTrue(self.assetpage.asset_type_Saved_label.is_displayed(),
                        self.config.get(self.section, 'MESSAGE_SAVED_TEXT_NOT_DISPLAYED'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_021(self):
        """
        Test : test_AS_21
        Description : To edit overview section. Enter all required fields info and click on cancel button.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_details_edit_widget_locator), r"Details"))
        self.assetpage.get_asset_overview_edit_link.click()
        self.assetpage.set_place_overview_fields("indecomm address cancel", "indecomm address 2 cancel", "Indecomm city",
                                            "KA", "94821", "Indecomm_Cancel")
        self.assetpage.asset_overview_cancel_click()#click on Cancel
        self.assertEqual(self.assetpage.asset_place_name, self.assetpage.get_asset_name_breadcrumb.text)


    @attr(priority="high")
    #@SkipTest
    def test_AS_023(self):
        """
        Test : test_AS_23
        Description : To edit overview section. Enter all required fields info and click on save button.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_details_edit_widget_locator), r"Details"))
        self.assetpage.get_asset_detail_edit_link.click()
        self.assetpage.set_place_details_fields("1234", r"2017-05-16", r"Description of School 3",
                r"indecomm@indecomm.net", r"123-4567-892", r"2015-02-23",r"6300", r"http://www.haystax.com")
        self.assetpage.get_asset_detail_edit_save_button.click()
        self.assertTrue(self.assetpage.asset_type_Saved_label.is_displayed(),
                        self.config.get(self.section, 'MESSAGE_SAVED_TEXT_NOT_DISPLAYED'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_024(self):
        """
        Test : test_AS_24
        Description : To verify email field of the Detail section.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, 'Place')
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_details_edit_widget_locator), r"Details"))
        self.assetpage.get_asset_detail_edit_link.click()
        email_add = r"test@email.com"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self.assetpage._asset_detail_edit_email_textbox_locator))).clear()
        self.assetpage.get_asset_detail_edit_email_text_box.send_keys(email_add)
        self.assetpage.get_asset_detail_edit_email_text_box.send_keys(Keys.TAB)
        regex = re.compile(r'[\w.-]+@[\w.-]+')
        self.assertRegexpMatches(email_add, regex,
                                 self.config.get(self.section, 'MESSAGE_EMAIL_NOT_MATCHING'))
        self.assetpage.get_asset_detail_edit_cancel_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_025(self):
        """
        Test : test_AS_25
        Description : To verify FAX field of the Detail section.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_details_edit_widget_locator), r"Details"))
        self.assetpage.get_asset_detail_edit_link.click()#Click on Details panel
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located(
            (By.XPATH, self.assetpage._asset_detail_edit_title_locator)))
        self.assetpage.get_asset_detail_edit_detail_fax_text_box.clear()
        self.assetpage.get_asset_detail_edit_detail_fax_text_box.send_keys(r"123abc1234") #Enter the value for FAX
        self.assetpage.get_asset_detail_edit_detail_fax_text_box.send_keys(Keys.TAB)
        regex = re.compile(r'^\(?([0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([0-9]{4})$')
        self.assertRegexpMatches(r"123abc1234", regex,
                                 self.config.get(self.section, 'MESSAGE_FAX_NOT_MATCHING'))
        self.assetpage.get_asset_detail_edit_cancel_button.click()


    @attr(priority="high")
    #@SkipTest
    def test_AS_026(self):
        """
        Test : test_AS_26
        Description : To verify cancel button functionality of the Detail section.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_details_edit_widget_locator), r"Details"))
        self.assetpage.get_asset_detail_edit_link.click()
        self.assetpage.set_place_details_fields("4321", r"2020-05-16", r"Cancelled",r"cancel@indecomm.net",
                                                r"111-111-1111", r"2017-02-23", r"10001", r"http://www.haystax.com")
        self.assetpage.get_asset_detail_edit_cancel_button.click()
        self.assertEqual(self.assetpage.asset_place_name, self.assetpage.get_asset_name_breadcrumb.text)


    @attr(priority="high")
    #@SkipTest
    def test_AS_027(self):
        """
        Test : test_AS_27
        Description : To verify all mandatory fields in Contact Section.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.delete_existing_contact() #delete existing contacts.
        self.assetpage.create_new_contact("FirstName","ZLastName")#create new contact.
        act_new_contact_value = self.assetpage.get_asset_contact_new_contact_value_text.text
        exp_new_contact_value = "ZLastName, FirstName"+" Title "+r"111-111-1111 "+r"test@test.com"
        self.assertEqual(act_new_contact_value, exp_new_contact_value,
                                                        self.config.get(self.section, 'MESSAGE_CONTACTS_NOT_MATCHING'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_028(self):
        """
        Test : test_AS_28
        Description : To verify that main contact has same info as first contact.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.delete_existing_contact()#delete existing contacts.
        self.assetpage.create_new_contact("FirstName","ZLastName")#create new contact.
        try:
            if self.assetpage.get_asset_main_contact_window:
                act_name_value = self.assetpage.get_asset_main_contact_name_text.text
                exp_name_value = "Shri FirstName ZLastName"
                self.assertEqual(str(act_name_value), str(exp_name_value))#verify asset main contact first and last name value.
        except NoSuchElementException:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_NO_MAIN_CONTACTS'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_029(self):
        """
        Test : test_AS_29
        Description : To verify error message for first and last name.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.delete_existing_contact()#delete existing contacts.
        self.assetpage.get_asset_points_of_contact_header.click()
        self.assetpage.get_asset_add_contact_button.click()#click on Add Contact button.
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        self.assetpage.get_asset_newcontact_firstname_textbox.clear()#clear first and last name.
        self.assetpage.get_asset_newcontact_lastname_textbox.clear()
        self.assetpage.get_asset_newcontact_prefix_textbox.clear()#clear Prefix filed.
        #sleep(2) #required to check Error message.
        firstname_error = self.assetpage.get_asset_newcontact_firstname_error_message.is_displayed()#Verify Error messages.
        lastname_error = self.assetpage.get_asset_newcontact_lastname_error_message.is_displayed()
        #sleep(2) #required to check Error message.
        self.assetpage.get_asset_newcontact_window_cross_button.click()#click on cross button to close window.
        self.assertTrue(firstname_error, self.config.get(self.section, 'MESSAGE_ERROR_NOT_DISPLAYED_FOR_FIRST_NAME'))
        self.assertTrue(lastname_error, self.config.get(self.section, 'MESSAGE_ERROR_NOT_DISPLAYED_FOR_LAST_NAME'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_030(self):
        """
        Test : test_AS_30
        Description : To verify phone field of the Contact section.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.delete_existing_contact()#delete existing contacts.
        self.assetpage.get_asset_points_of_contact_header.click()
        self.assetpage.get_asset_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        self.assetpage.get_asset_newcontact_firstname_textbox.clear()
        self.assetpage.get_asset_newcontact_firstname_textbox.send_keys("FirstName")
        self.assetpage.get_asset_newcontact_lastname_textbox.clear()
        self.assetpage.get_asset_newcontact_lastname_textbox.send_keys("ZLastName")
        self.assetpage.get_asset_newcontact_phone_textbox.clear()
        self.assetpage.get_asset_newcontact_phone_textbox.send_keys(r"111-222-3343")
        self.assetpage.get_asset_newcontact_save_button.click()#click on save button.
        act_phone = self.assetpage.get_asset_contact_phone_value_text.text#reading act phone value.
        regex = re.compile(r'^\(?([A-Za-z0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([A-Za-z0-9]{4})$')
        self.assertRegexpMatches(str(act_phone), regex,
                                 self.config.get(self.section, 'MESSAGE_PHONE_VALUE_NOT_MATCHING'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_031_1(self):
        """
        Test : test_AS_31_1
        Description : To verify email field of the Contact section.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.delete_existing_contact()#delete existing contacts.
        self.assetpage.get_asset_points_of_contact_header.click()
        self.assetpage.get_asset_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        self.assetpage.get_asset_newcontact_firstname_textbox.clear()
        self.assetpage.get_asset_newcontact_firstname_textbox.send_keys("FirstName")
        self.assetpage.get_asset_newcontact_lastname_textbox.clear()
        self.assetpage.get_asset_newcontact_lastname_textbox.send_keys("ZLastName")
        self.assetpage.get_asset_newcontact_email_textbox.clear()
        self.assetpage.get_asset_newcontact_email_textbox.send_keys(r"test@test.com")
        self.assetpage.get_asset_newcontact_save_button.click() #click on save button.
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        act_email = self.assetpage.get_asset_contact_email_value_text.text #reading actual email value.
        regex = re.compile(r'[\w.-]+@[\w.-]+')
        self.assertRegexpMatches(str(act_email), regex,
                                 self.config.get(self.section, 'MESSAGE_EMAIL_NOT_MATCHING'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_031_2(self):
        """0
        Test : test_AS_31_2
        Description : To verify email field of the Contact section. Email address with wrong address.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.delete_existing_contact()#delete existing contacts.
        self.assetpage.get_asset_points_of_contact_header.click()
        self.assetpage.get_asset_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        self.assetpage.get_asset_newcontact_firstname_textbox.clear()
        self.assetpage.get_asset_newcontact_firstname_textbox.send_keys("FirstName")
        self.assetpage.get_asset_newcontact_lastname_textbox.clear()
        self.assetpage.get_asset_newcontact_lastname_textbox.send_keys("ZLastName")
        self.assetpage.get_asset_newcontact_email_textbox.clear()
        self.assetpage.get_asset_newcontact_email_textbox.send_keys(r"testtest.com")
        #sleep(2)
        self.assetpage.get_asset_newcontact_firstname_textbox.click()
        #sleep(2)
        exp_error_message = self.assetpage.get_asset_newcontact_email_error_message.is_displayed()
        self.assetpage.get_asset_newcontact_window_cross_button.click()#Click on Cross button to close window.
        self.assertTrue(exp_error_message,
                        self.config.get(self.section, 'MESSAGE_ERROR_NOT_DISPLAYED_FOR_WRONG_EMAIL'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_032(self):
        """
        Test : test_AS_32
        Description : To verify cancel button functionality of the Contact window.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.delete_existing_contact()#delete existing contacts.
        self.assetpage.get_asset_points_of_contact_header.click()
        self.assetpage.get_asset_add_contact_button.click()#click on add contact button
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        self.assetpage.get_asset_newcontact_firstname_textbox.clear()
        self.assetpage.get_asset_newcontact_firstname_textbox.send_keys("FirstNameDel")
        self.assetpage.get_asset_newcontact_lastname_textbox.clear()
        self.assetpage.get_asset_newcontact_lastname_textbox.send_keys("ZLastNameDel")
        self.assetpage.get_asset_newcontact_cancel_button.click()#click on cancel button.
        #sleep(2)
        try:
            if self.assetpage.get_asset_contact_first_last_name_value_text.is_displayed():
                self.assertFalse(True,
                                 self.config.get(self.section, 'MESSAGE_ERROR_CANCEL_NOT_WORKING_ON_CONTACT_CREATION'))
        except:
            self.assertTrue(True,self.config.get(self.section, 'MESSAGE_NEW_CONTACT_CREATED'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_033_1(self):
        """
        Test : test_AS_33_1
        Description : To verify contact name in ascending order.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver, 50).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.multiple_contact_create()#create multiple contacts.
        exp_name_ascending = r"stu, def, mno, jkl, ghi, pqr, abc, vwx"
        exp_name_descending = r"abc, vwx, ghi, pqr, mno, jkl, stu, def"
        self.assetpage.get_asset_point_of_contact_name_tab.click()#click on contact name tab.
        #sleep(2)
        act_name_list = self.assetpage.get_asset_point_of_contact_name_text_value#Reading all contact names.
        act_name_list_value = []
        for name in act_name_list:
            act_name_list_value.append(name.text)
        self.assertEqual(exp_name_ascending, ", ".join(act_name_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_NAMES_IN_ASCENDING_ORDER'))
        self.assetpage.get_asset_point_of_contact_name_tab.click()
        #sleep(2)
        act_name_list = self.assetpage.get_asset_point_of_contact_name_text_value#Reading all contact's names.
        act_name_list_value =[]
        for name in act_name_list:
            act_name_list_value.append(name.text)
        self.assertEqual(exp_name_descending, ", ".join(act_name_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_NAMES_IN_DESCENDING_ORDER'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_033_2(self):
        """
        Test : test_AS_33_2
        Description : To verify contact title's value in ascending order.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.multiple_contact_create()#create multiple contacts.
        exp_title_ascending = r"CC, HH, PP, ZZ"
        exp_title_descending = r"ZZ, PP, HH, CC"
        self.assetpage.get_asset_point_of_contact_title_tab.click()#click on contact title tab to sort ascendingly.
        #sleep(2)
        act_title_list = self.assetpage.get_asset_point_of_contact_title_text_value#Reading all contact's title values.
        act_title_list_value = []
        for title in act_title_list:
            act_title_list_value.append(title.text)
        self.assertEqual(exp_title_ascending, ", ".join(act_title_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_TITLES_NOT_IN_ASCENDING_ORDER'))
        self.assetpage.get_asset_point_of_contact_title_tab.click()#click on contact title tab to sort descendingly.
        #sleep(2)
        act_title_list = self.assetpage.get_asset_point_of_contact_title_text_value#Reading all contact's title values.
        act_title_list_value = []
        for title in act_title_list:
            act_title_list_value.append(title.text)
        self.assertEqual(exp_title_descending, ", ".join(act_title_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_TITLES_NOT_IN_DESCENDING_ORDER'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_033_3(self):
        """
        Test : test_AS_33_3
        Description : To verify contact phone's value in ascending order.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.multiple_contact_create()#create multiple contacts.
        exp_phone_ascending = r"123-444-4444, 222-222-2222, 433-333-3333, 661-111-1111"
        exp_phone_descending = r"661-111-1111, 433-333-3333, 222-222-2222, 123-444-4444"
        self.assetpage.get_asset_point_of_contact_phone_tab.click()#click on contact phone tab.
        #sleep(2)
        act_phone_list = self.assetpage.get_asset_point_of_contact_phone_text_value#Reading all contact's phone values.
        act_phone_list_value = []
        for phone in act_phone_list:
            act_phone_list_value.append(phone.text)
        self.assertEqual(exp_phone_ascending, ", ".join(act_phone_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_PHONE_NUMBERS_NOT_IN_ASCENDING_ORDER'))
        self.assetpage.get_asset_point_of_contact_phone_tab.click()
        #sleep(2)
        act_phone_list = self.assetpage.get_asset_point_of_contact_phone_text_value#Reading all contact's phone values.
        act_phone_list_value = []
        for phone in act_phone_list:
            act_phone_list_value.append(phone.text)
        self.assertEqual(exp_phone_descending, ", ".join(act_phone_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_PHONE_NUMBERS_NOT_IN_DESCENDING_ORDER'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_033_4(self):
        """
        Test : test_AS_33_4
        Description : To verify contact email's value in ascending order.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.multiple_contact_create()#create multiple contacts.
        exp_email_ascending = r"abc@def, ghi@jkl, mno@pqr, stu@vwx"
        exp_email_descending = r"stu@vwx, mno@pqr, ghi@jkl, abc@def"
        self.assetpage.get_asset_point_of_contact_email_tab.click()  #click on contact email tab.
        #sleep(2)
        act_email_list = self.assetpage.get_asset_point_of_contact_email_text_value#Reading all contact's email values.
        act_email_list_value = []
        for email in act_email_list:
            act_email_list_value.append(email.text)
        self.assertEqual(exp_email_ascending, ", ".join(act_email_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_EMAILS_NOT_IN_ASCENDING_ORDER'))
        self.assetpage.get_asset_point_of_contact_email_tab.click()
        #sleep(2)
        act_email_list = self.assetpage.get_asset_point_of_contact_email_text_value#Reading all contact's email values.
        act_email_list_value = []
        for email in act_email_list:
            act_email_list_value.append(email.text)
        self.assertEqual(exp_email_descending, ", ".join(act_email_list_value),
                         self.config.get(self.section, 'MESSAGE_CONTACT_EMAILS_NOT_IN_DESCENDING_ORDER'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_034(self):
        """
        Test : test_AS_34
        Description : To verify delete option of contact.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.delete_existing_contact()#delete existing contacts.
        self.assetpage.get_asset_points_of_contact_header.click()
        self.assetpage.get_asset_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        self.assetpage.get_asset_newcontact_firstname_textbox.clear()
        self.assetpage.get_asset_newcontact_firstname_textbox.send_keys("FirstName")
        self.assetpage.get_asset_newcontact_lastname_textbox.clear()
        self.assetpage.get_asset_newcontact_lastname_textbox.send_keys("ZLastName")
        self.assetpage.get_asset_newcontact_save_button.click()#click on save button.
        self.assetpage.delete_existing_contact()#delete existing contacts.
        try:
            if self.assetpage.get_asset_newcontact_delete_icon.is_displayed():
                #sleep(2)
                self.assertFalse(False, self.config.get(self.section, 'MESSAGE_NEW_CONTACT_NOT_DELETED'))
        except NoSuchElementException:
            self.assertTrue(True, self.config.get(self.section, 'MESSAGE_CONTACT_DELETED'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_035(self):
        """
        Test : test_AS_35
        Description : To verify delete window cancel button functionality.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_main_contct_widget_locator), r"Points of Contact"))
        self.assetpage.delete_existing_contact()#delete existing contacts.
        self.assetpage.get_asset_points_of_contact_header.click()
        self.assetpage.get_asset_add_contact_button.click()
        WebDriverWait(self.driver,30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        self.assetpage.get_asset_newcontact_firstname_textbox.clear()
        self.assetpage.get_asset_newcontact_firstname_textbox.send_keys("FirstName")
        self.assetpage.get_asset_newcontact_lastname_textbox.clear()
        self.assetpage.get_asset_newcontact_lastname_textbox.send_keys("ZLastName")
        self.assetpage.get_asset_newcontact_save_button.click()
        try:
            if self.assetpage.get_asset_newcontact_delete_icon.is_displayed():
                #sleep(2)
                self.assetpage.get_asset_newcontact_delete_icon.click()
                #sleep(2)
                self.assetpage.get_asset_newcontact_delete_popup_cancel_button.click()
                #sleep(2)
                self.assertTrue(True, self.config.get(self.section, 'MESSAGE_CANCEL_IS_WORKING'))
        except NoSuchElementException:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_CONTACT_DELETED'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_036(self):
        """
        Test : test_AS_36
        Description : To verify Latitude and Longitude boundary values.
        Revision:
        Author : Kiran
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.ID, "map_control")))
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(
            (By.XPATH,self.assetpage._asset_location_edit_icon_xpath_locator))).click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_location_title_id_locator), r"Asset location"),
            self.config.get(self.section, 'MESSAGE_LOCATION_POPUP_NOT_DISPLAYED'))
        lati = "550"
        self.assetpage.get_asset_location_latitude_textbox.clear()
        self.assetpage.get_asset_location_latitude_textbox.send_keys(lati)
        latitudeerrorMessage = self.assetpage.get_asset_location_latitude_error_text.text
        self.assertEqual(latitudeerrorMessage, self.config.get(self.section, 'MESSAGE_LATITUDE_NUMBER_RANGE'),
                         self.config.get(self.section, 'MESSAGE_ERROR_NOT_DISPLAYED_FOR_LATITUDE'))


        locationSave = self.assetpage.get_asset_location_save_button
        self.assertFalse(locationSave.is_enabled(), self.config.get(self.section, 'MESSAGE_LOCATION_SAVE_BUTTON_IS_NOT_DISABLED'))
        longi = "200"
        self.assetpage.get_asset_location_longitude_textbox.clear()
        self.assetpage.get_asset_location_longitude_textbox.send_keys(longi)
        longitudeerrorMessage = self.assetpage.get_asset_location_longitude_error_text.text
        self.assertEqual(self.config.get(self.section, 'MESSAGE_LONGITUDE_NUMBER_RANGE'), longitudeerrorMessage,
                         self.config.get(self.section, 'MESSAGE_ERROR_NOT_DISPLAYED_FOR_LONGITUDE'))
        locationSave = self.assetpage.get_asset_location_save_button
        self.assertFalse(locationSave.is_enabled(), self.config.get(self.section, 'MESSAGE_LOCATION_SAVE_BUTTON_NOT_DISABLED'))
        self.assetpage.get_asset_location_cancel_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_037(self):
        """
        Test : test_AS_37
        Description : To verify whether Marker is displayed on the map after_setting Latitude and Longitude values.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver,50).until(EC.presence_of_element_located((By.ID,"map_control")))
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(
            (By.XPATH,self.assetpage._asset_location_edit_icon_xpath_locator))).click()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_location_title_id_locator), r"Asset location"),
        self.config.get(self.section, 'MESSAGE_LOCATION_POPUP_NOT_DISPLAYED'))
        lati = "40.7127"
        self.assetpage.get_asset_location_latitude_textbox.clear()
        self.assetpage.get_asset_location_latitude_textbox.send_keys(lati)
        longi = "74.0059"
        self.assetpage.get_asset_location_longitude_textbox.clear()
        self.assetpage.get_asset_location_longitude_textbox.send_keys(longi)
        self.assetpage.get_asset_location_save_button.click()
        #self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        self.assertTrue(self.assetpage.get_asset_location_marker_available_image.is_displayed(),
                        self.config.get(self.section, 'MESSAGE_MARKER_NOT_DISPLAYED_ON_MAP'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_038(self):
        """
        Test : test_AS_38
        Description : To verify Place name once click on Marker.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID,"map_control")))
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(
            (By.XPATH,self.assetpage._asset_location_edit_icon_xpath_locator))).click()
        WebDriverWait(self.driver, 50).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_location_title_id_locator), r"Asset location"),
        self.config.get(self.section, 'MESSAGE_LOCATION_POPUP_NOT_DISPLAYED'))
        lati = "40.7127"
        self.assetpage.get_asset_location_latitude_textbox.clear()
        self.assetpage.get_asset_location_latitude_textbox.send_keys(lati)
        longi = "74.0059"
        self.assetpage.get_asset_location_longitude_textbox.clear()
        self.assetpage.get_asset_location_longitude_textbox.send_keys(longi)
        self.assetpage.get_asset_location_save_button.click()
        #self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-200);")
        self.assertTrue(self.assetpage.get_asset_location_marker_available_image.is_displayed(),
                        self.config.get(self.section, 'MESSAGE_MARKER_NOT_DISPLAYED_ON_MAP'))
        sleep(1)
        self.assetpage.get_asset_location_marker_available_image.click()
        placeText = self.assetpage.get_asset_location_place_name_text.text
        self.assertEqual(self.assetpage.asset_place_name, placeText,
                         self.config.get(self.section, 'MESSAGE_MARKER_NAME_NOT_DISPLAYED_ON_MAP'))

    @attr(priority="high")
    @SkipTest
    def test_AS_040(self):
        """
        Test : test_AS_40
        Description : To verify whether uploaded file deleted properly or not.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        self.assetpage.delete_uploaded_files()#Delete all uploaded files.
        caption_val = "Test_Case_40"
        image_file_name = "Test_Case_40.jpg"
        self.assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        number_of_image_after_upload = self.assetpage.get_asset_photos_documents_uploaded_file_count
        image_count_after_file_upload = len(number_of_image_after_upload)
        caption_path = "//a[contains(text(),'"+caption_val+"')]"
        image_icon = self.driver.find_element_by_xpath(caption_path)
        Hover = ActionChains(self.driver).move_to_element(image_icon)
        Hover.perform()
        #sleep(1) # required. so that Delete icon remain displayed.
        try:
            self.assetpage.get_asset_photos_documents_delete_icon_image.click()
            self.assetpage.get_asset_photos_documents_delete_window_delete_button.click()
            #sleep(3)  # required. Widget should be refreshed.
        except NoSuchElementException:
            self.assertFalse(True,
                             self.config.get(self.section, 'MESSAGE_DELETE_ICON_NOT_DISPLAYED_FILE_COULD_NOT_BE_DELETED'))
        except ElementNotVisibleException:
            self.assertFalse(True,
                             self.config.get(self.section, 'MESSAGE_DELETE_ICON_NOT_DISPLAYED_FILE_COULD_NOT_BE_DELETED'))
        number_of_image_after_delete = self.assetpage.get_asset_photos_documents_uploaded_file_count
        image_count_after_file_delete = len(number_of_image_after_delete)
        if (image_count_after_file_upload == image_count_after_file_delete+1):
            try:
                if (self.assetpage.get_asset_photos_documents_header_caption_text(caption_val).is_displayed()):
                    self.assertFalse(True, self.config.get(self.section, 'MESSAGE_UPLOADED_FILE_COULD_NOT_BE_DELETED'))
            except NoSuchElementException:
                self.assertTrue(True, self.config.get(self.section, 'MESSAGE_UPLOADED_FILE_DELETED'))
        else:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_FILES_BEFORE_AFTER_SAME_FILE_COULD_NOT_BE_DELETED'))

    @attr(priority="high")
    @SkipTest
    def test_AS_041(self):
        """
        Test : test_AS_41
        Description : To verify cancel button functionality of File upload window.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        self.assetpage.delete_uploaded_files()#Delete all uploaded files.
        number_of_image_before_upload = self.assetpage.get_asset_photos_documents_uploaded_file_count
        image_count_before_file_upload = len(number_of_image_before_upload)
        self.assetpage.get_asset_photos_documents_upload_file_button.click()
        #sleep(1)
        file_path = self.assetpage.file_path("Test_Case_41.jpg")
        self.assetpage.get_asset_photos_documents_attached_file_button.send_keys(file_path)
        #sleep(1)
        caption_val = "Test_Case_41"
        self.assetpage.get_asset_photos_documents_caption_textbox.send_keys(caption_val)
        #sleep(1)
        self.assetpage.get_asset_photos_documents_window_cancel_button.click()
        try:
            number_of_image_after_upload = self.assetpage.get_asset_photos_documents_uploaded_file_count
            image_count_after_file_upload = len(number_of_image_after_upload)
            if (image_count_after_file_upload == image_count_before_file_upload):
                self.assertTrue(True,"The Cancel Button is not workking. New file has been uploaded.")
        except Exception, e:
            error = "The Cancel Button is not workking. New file has been uploaded. ::"+str(e)
            self.assertFalse(True, error)

    @attr(priority="high")
    @SkipTest
    def test_AS_042(self):
        """
        Test : test_AS_42
        Description : To verify an image file with caption is uploaded properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        self.assetpage.delete_uploaded_files()
        caption_val = "Test_Case_42"
        image_file_name = "Test_Case_42.jpg"
        self.assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        image_caption_text = self.assetpage.get_asset_photos_documents_image_caption_text(caption_val)
        header_caption_text = self.assetpage.get_asset_photos_documents_header_caption_text(caption_val)
        if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed()):
            self.assertTrue(True,
                            self.config.get(self.section, 'MESSAGE_TEST_CASE_PASSED_CAPTION_DISPLAYED_IN_HEADER_FILE_WINDOW'))
        else:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_TEST_CASE_FAILED_FOR_NO_CAPTION'))

    @attr(priority="high")
    @SkipTest
    def test_AS_043(self):
        """
        Test : test_AS_43
        Description : To verify error message when file with more than 12 MB is uploaded.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        self.assetpage.delete_uploaded_files()
        caption_val = "Test_Case_43"
        image_file_name = "Test_Case_43.jpg"
        self.assetpage.get_asset_photos_documents_upload_file_button.click()
        file_path = self.assetpage.file_path(image_file_name)
        self.assetpage.get_asset_photos_documents_attached_file_button.send_keys(file_path)
        self.assetpage.get_asset_photos_documents_caption_textbox.send_keys(caption_val)
        self.assetpage.get_asset_photos_documents_window_upload_button.click()
        try:
            WebDriverWait(self.driver, 200).until(EC.text_to_be_present_in_element(
                (By.XPATH, self.assetpage._asset_header_save_text_locator),r"415 - UNSUPPORTED MEDIA TYPE"))
        except:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_NO_ERROR_MESSAGE_DISPLAYED_FOR_UNSUPPORTED_MEDIA_SIZE'))
        self.assertTrue(True, self.config.get(self.section, 'MESSAGE_TEST_CASE_PASSED'))

    @attr(priority="high")
    @SkipTest
    def test_AS_044_1(self):
        """
        Test : test_AS_44_1
        Description : To verify a pdf file with caption is uploaded properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        self.assetpage.delete_uploaded_files()
        caption_val = "Test_Case_44_1"
        image_file_name = "Test_Case_44_1.pdf"
        self.assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        image_caption_text = self.assetpage.get_asset_photos_documents_image_caption_text(caption_val)
        header_caption_text = self.assetpage.get_asset_photos_documents_header_caption_text(caption_val)
        if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed()):
            self.assertTrue(True, self.config.get(self.section, 'MESSAGE_TEST_CASE_PASSED'))
        else:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_PDF_FILE_NOT_UPLOADED'))

    @attr(priority="high")
    @SkipTest
    def test_AS_044_2(self):
        """
        Test : test_AS_44_2
        Description : To verify a html file with caption is uploaded properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        self.assetpage.delete_uploaded_files()
        caption_val = "Test_Case_44_2"
        image_file_name = "Test_Case_44_2.html"
        self.assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        image_caption_text = self.assetpage.get_asset_photos_documents_image_caption_text(caption_val)
        header_caption_text = self.assetpage.get_asset_photos_documents_header_caption_text(caption_val)
        if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed()):
            self.assertTrue(True, self.config.get(self.section, 'MESSAGE_TEST_CASE_PASSED'))
        else:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_HTML_FILE_NOT_UPLOADED'))

    @attr(priority="high")
    @SkipTest
    def test_AS_044_3(self):
        """
        Test : test_AS_44_3
        Description : To verify a text file with caption is uploaded properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        self.assetpage.delete_uploaded_files()
        caption_val = "Test_Case_44_3"
        image_file_name = "Test_Case_44_3.txt"
        self.assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        image_caption_text = self.assetpage.get_asset_photos_documents_image_caption_text(caption_val)
        header_caption_text = self.assetpage.get_asset_photos_documents_header_caption_text(caption_val)
        if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed() and
                                                        (self.assetpage.get_asset_header_save_text.text == r"Saved")):
            self.assertTrue(True, self.config.get(self.section, 'MESSAGE_TEST_CASE_PASSED'))
        else:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_TEXT_FILE_NOT_UPLOADED'))

    @attr(priority="high")
    @SkipTest
    def test_AS_045(self):
        """
        Test : test_AS_45
        Description : To verify whether multiple files has been uploaded properly or not.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        self.assetpage.delete_uploaded_files()
        image_count_before_file_upload = len(self.assetpage.get_asset_photos_documents_uploaded_file_count)
        caption_val = ["Test_Case_45_1", "Test_Case_45_2", "Test_Case_45_3"]
        image_file_name = ["Test_Case_45_1.jpg", "Test_Case_45_2.jpg", "Test_Case_45_3.jpg"]
        for num in range(3):
            self.assetpage.upload_a_file_with_caption(caption_val[num], image_file_name[num])
            #sleep(2) #required  to update image properly
        image_count_after_file_upload = len(self.assetpage.get_asset_photos_documents_uploaded_file_count)
        if (image_count_after_file_upload == image_count_before_file_upload+3):
            self.assertTrue(True, self.config.get(self.section, 'MESSAGE_TEST_CASE_PASSED'))
        else:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_MULTIPLE_FILES_COULD_NOT_BE_UPLOADED'))

    @attr(priority="high")
    @SkipTest
    def test_AS_047(self):
        """
        Test : test_AS_47
        Description : To verify an image file without caption is uploaded properly.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        self.assetpage.delete_uploaded_files()
        image_count_before_file_upload = len(self.assetpage.get_asset_photos_documents_uploaded_file_count)
        caption_val = ""
        image_file_name = "Test_Case_47.jpg"
        self.assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        image_count_after_file_upload = len(self.assetpage.get_asset_photos_documents_uploaded_file_count)
        header_caption_text = self.assetpage.get_asset_photos_documents_header_caption_text(image_file_name)
        if (header_caption_text.is_displayed() and (image_count_after_file_upload == image_count_before_file_upload+1)):
            self.assertTrue(True, self.config.get(self.section, 'MESSAGE_TEST_CASE_PASSED'))
        else:
            self.assertFalse(True, self.config.get(self.section, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_048_1(self):
        """
        Test : test_AS_48_1
        Description : To verify annotation groups text.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
                                            (By.XPATH, self.assetpage._asset_annotation_widget_locator), "Annotations"))
        exp_text_val = r"This is Indecomm Testing. Groups."
        self.assetpage.delete_all_annotation()
        self.assetpage.get_asset_annotation_plus_image.click()
        self.assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)#Enter Annotation text.
        self.assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()#Select Annotation type.
        self.assetpage.get_asset_annotation_edit_window_dropdown_groups.click()
        self.assetpage.get_asset_annotation_edit_window_save_button.click()
        #sleep(2)
        act_text_val = ((self.assetpage.get_asset_annotation_text_value.text).split(' - '))[1].strip()#read annotation value.
        self.assertEqual(str(act_text_val),str(exp_text_val), self.config.get(self.section, 'MESSAGE_ANNOTATIONS_NOT_MATCHING'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_048_2(self):
        """
        Test : test_AS_48_2
        Description : To verify annotation tenant text.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element
                                           ((By.XPATH, self.assetpage._asset_annotation_widget_locator), "Annotations"))
        exp_text_val = r"This is Indecomm Testing. Tenant."
        self.assetpage.delete_all_annotation()#delete All Annotation.
        self.assetpage.get_asset_annotation_plus_image.click()#Click on Annotation Plus image.
        self.assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)#Enter Annotation text.
        self.assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
        self.assetpage.get_asset_annotation_edit_window_dropdown_tenant.click()#Select Annotation type.
        self.assetpage.get_asset_annotation_edit_window_save_button.click()
        #sleep(2)
        text_val = self.assetpage.get_asset_annotation_text_value.text#read annotation value.
        act_text_val = (text_val.split(' - '))[1].strip()
        self.assertEqual(str(act_text_val),str(exp_text_val), self.config.get(self.section, 'MESSAGE_ANNOTATIONS_NOT_MATCHING'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_048_3(self):
        """
        Test : test_AS_48_3
        Description : To verify annotation users text.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element
                                           ((By.XPATH, self.assetpage._asset_annotation_widget_locator), "Annotations"))
        exp_text_val = r"This is Indecomm Testing. Groups."
        self.assetpage.delete_all_annotation()#delete All Annotation.
        self.assetpage.get_asset_annotation_plus_image.click()#Click on Annotation Plus image.
        self.assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)#Enter Annotation text.
        self.assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
        self.assetpage.get_asset_annotation_edit_window_dropdown_user.click()#Select Annotation type.
        self.assetpage.get_asset_annotation_edit_window_save_button.click()
        #sleep(2)
        text_val = self.assetpage.get_asset_annotation_text_value.text#read annotation value.
        act_text_val = (text_val.split(' - '))[1].strip()
        self.assertEqual(str(act_text_val),str(exp_text_val), self.config.get(self.section, 'MESSAGE_ANNOTATIONS_NOT_MATCHING'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_048_4(self):
        """
        Test : test_AS_48_4
        Description : To verify annotation edit functionality.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_place_name, "Place")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element
                                           ((By.XPATH, self.assetpage._asset_annotation_widget_locator), "Annotations"))
        exp_text_val = r"This is Indecomm Testing. Gropus."
        self.assetpage.delete_all_annotation()#delete All Annotation.
        self.assetpage.get_asset_annotation_plus_image.click()#Click on Annotation Plus image.
        self.assetpage.get_asset_annotation_edit_window_text_area.send_keys("Random Text Value.")#Enter Annotation text.
        self.assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
        self.assetpage.get_asset_annotation_edit_window_dropdown_groups.click()#Select Annotation type.
        self.assetpage.get_asset_annotation_edit_window_save_button.click()
        #sleep(2)
        self.assetpage.get_asset_annotation_edit_image.click()#click on annotation edit link.
        self.assetpage.get_asset_annotation_edit_window_text_area.clear()#clear annotation text.
        self.assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)#Enter new anootation text.
        self.assetpage.get_asset_annotation_edit_window_save_button.click()
        #sleep(2)
        text_val = self.assetpage.get_asset_annotation_text_value.text
        act_text_val = (text_val.split(' - '))[1].strip()
        self.assertEqual(str(act_text_val),str(exp_text_val), self.config.get(self.section, 'MESSAGE_ANNOTATIONS_NOT_MATCHING'))

    @attr(priotity = "high")
    #@SkipTest
    def test_AS_049_50(self):
        """
        Test : test_AS_49_50
        Description : To verify school asset creation and verify that created asset is displayed in the asset list.
        Revision:
        Author: Deepa Sivadas
        :return: None
        """
        flag = 0

        #self.assetpage.app_sanity_check()
        self.assetpage.create_asset("School")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_name_breadcrumb), self.assetpage.asset_school_name[0]))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                    (By.LINK_TEXT, self.assetpage._asset_link_locator))).click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, self.assetpage._asset_select_action_delete_select_xpath_locator)))
        self.assetpage.asset_search_assetname(self.assetpage.asset_school_name[0])
        sleep(5)#necessary sleep to let the app finish searching for the assetname
        for item in self.assetpage.get_asset_list_background:
            if (item.text  == self.assetpage.asset_school_name[0]) and \
                    (item.value_of_css_property("background-color") == "rgba(255, 236, 158, 1)"):
                flag = 1
                break
        self.assetpage.textbox_clear(self.driver.find_element_by_xpath(self.assetpage._asset_search_textbox_locator))
        self.assertFalse(flag == 0, self.config.get(self.section, 'MESSAGE_NEW_ASSET_NOT_APPEARING_ON_YELLOW_BACKGROUND'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_051(self):
        """
        Test : test_AS_51
        Description : To verify asset school Name field.
        Author: Deepa Sivadas
        Revision:
        :return: None
        """
        self.assetpage.asset_create_click()
        self.assetpage.select_asset_template_type("School")
        self.assertFalse(self.assetpage.get_asset_overview_save_button.is_enabled())
        self.assetpage.get_asset_overview_cancel_button.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self.assetpage._asset_create_asset)),
            self.config.get(self.section, 'MESSAGE_CREATE_ASSET_BUTTON_NOT_DISPALYED'))
        self.assertTrue(self.assetpage.get_asset_create_asset,
                        self.config.get(self.section, 'MESSAGE_CANCEL_FAILED_ON_CREATING_ASSET_DIALOGUE'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_053(self):
        """
        Test : test_AS_53
        Description : To verify asset school Grade and District fields.
        Author: Deepa Sivadas
        Revision:
        :return: None
        """

        self.assetpage.asset_create_click()
        self.assetpage.select_asset_template_type("School")
        self.assetpage.enter_asset_type_name.send_keys(self.assetpage.asset_school_name[0])
        self.assetpage.enter_school_district(self.assetpage.asset_school_district_grade_validation)
        self.assetpage.enter_school_grade(self.assetpage.asset_school_district_grade_validation)
        self.assetpage.asset_overview_save_click()
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_details_edit_widget_locator), "Details"))
        self.assertEqual(self.assetpage.asset_school_district_grade_validation, self.assetpage.get_overview_district_text)
        self.assertEqual(self.assetpage.asset_school_district_grade_validation, self.assetpage.get_overview_grade_text)


    @attr(priority="high")
    #@SkipTest
    def test_AS_054(self):
        """
        Test : test_AS_54
        Description : To verify Cancel Button functionality of Create Asset Window.
        Author: Deepa Sivadas
        Revision:
        :return: None
        """
        self.assetpage.create_asset_cancel("School")
        self.assertTrue(self.driver.find_element_by_xpath(self.assetpage._asset_create_asset).is_displayed())

    @attr(priority="high")
    #@SkipTest
    def test_AS_055(self):
        """
        Test : test_AS_55
        Description : To verify Asset edit functionality.
        Author: Deepa Sivadas
        Revision:
        :return: None
        """
        #self.assetpage.app_sanity_check()
        self.assetpage.edit_asset("School")
        self.assertEqual(self.assetpage.asset_school_name[1], self.assetpage.get_overview_name_text)
        self.assertEqual(self.assetpage.asset_school_district[1], self.assetpage.get_overview_district_text)
        self.assertEqual(self.assetpage.asset_school_grade[1], self.assetpage.get_overview_grade_text)

    @attr(priority="high")
    #@SkipTest
    def test_AS_056(self):
        """
        Test : test_AS_56
        Description : To verify cancel button functionality of Detail Window. Enter data in all required fields.
        Revision:
        :return: None
        """

        #self.assetpage.app_sanity_check()
        # Search and Click on Place in the List for EDIT mode
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_school_name[0], "School")
        #self.assetpage.wait_for_element_path(self.assetpage._asset_detail_edit_link_locator).click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_details_edit_widget_locator), "Details"))
        self.assetpage.get_asset_detail_edit_link.click()
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
                                         (By.XPATH, self.assetpage._asset_detail_edit_title_locator), r"Asset details"))
        self.assetpage.set_school_details_fields("1234", r"2017-05-16", r"Description of School 3", "2",
                       r"indecomm@indecomm.net", r"123-4567-892", r"2015-02-23", "3", "6300", r"http://www.haystax.com")
        self.assetpage.get_asset_detail_edit_cancel_button.click()
        textfrombreadcrumb = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (By.XPATH, self.assetpage._asset_name_breadcrumb))).text
        #self.assetpage.wait_for_element_path(self.assetpage._asset_create_asset).text

        self.assertEqual(self.assetpage.asset_school_name[0], textfrombreadcrumb, "")

    @attr(priority="high")
    #@SkipTest
    def test_AS_058(self):
        """
        Test : test_AS_58
        Description : To verify save button functionality of Detail Window.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_school_name[0], "School")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH,
                                                         self.assetpage._asset_details_edit_widget_locator), "Details"))
        self.assetpage.get_asset_detail_edit_link.click()
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
                                         (By.XPATH, self.assetpage._asset_detail_edit_title_locator), r"Asset details"))
        self.assetpage.set_school_details_fields("1234", "2017-05-16", "Description of School 3","2",
                                           r"ki22ran2.k@indecomm.net", "123-4567-892", "2015-02-23", "3", "6300",
                                           "http://www.haystax.com")
        self.assetpage.get_asset_detail_edit_save_button.click()
        #sleep(5)
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='header']/div[3]").is_displayed(),
                        self.config.get(self.section, 'MESSAGE_SAVED_TEXT_NOT_DISPLAYED'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_059_1(self):
        """
        Test : test_AS_59_1
        Description : To verify email text box functionality of Detail Window.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_school_name[0], "School")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
                                              (By.XPATH, self.assetpage._asset_details_edit_widget_locator), "Details"))
        self.assetpage.get_asset_detail_edit_link.click()
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
                                         (By.XPATH, self.assetpage._asset_detail_edit_title_locator), r"Asset details"))
        self.assetpage.get_asset_detail_edit_email_text_box.clear()
        self.assetpage.get_asset_detail_edit_email_text_box.send_keys("test@test")
        self.assetpage.get_asset_detail_edit_save_button.click()
        #sleep(2)
        email = self.assetpage.get_asset_detail_email_value_text.text
        regex = re.compile(r'[\w.-]+@[\w.-]+')
        self.assertRegexpMatches(str(email), regex, self.config.get(self.section, 'MESSAGE_EMAIL_NOT_MATCHING'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_059_2(self):
        """
        Test : test_AS_59_2
        Description : To verify email text box functionality of Detail Window. Invalid value. Verify error message.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_school_name[0], "School")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(
                                              (By.XPATH, self.assetpage._asset_details_edit_widget_locator), "Details"))

        self.assetpage.get_asset_detail_edit_link.click()

        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
                                         (By.XPATH, self.assetpage._asset_detail_edit_title_locator), r"Asset details"))
        self.assetpage.get_asset_detail_edit_email_text_box.clear()
        self.assetpage.get_asset_detail_edit_email_text_box.send_keys("testtest")
        self.assetpage.get_asset_detail_edit_save_button.click()
        state = self.assetpage.get_asset_detail_edit_save_button.is_enabled()
        self.assetpage.get_asset_detail_edit_window_cross_button.click()
        self.assertFalse(state, self.config.get(self.section, 'MESSAGE_SAVE_BUTTON_ENABLED_ON_WRONG_EMAIL_VALUE'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_086(self):
        """
        Test : test_AS_90
        Description : To verify chart when no asset is selected.
        Revision:
        :return: None
        """
        self.assetpage.get_asset_reset_button.click()
        self.assetpage.make_dashboard_on()
        countbeforefilter = self.assetpage.get_total_row_count()
        self.assetpage.charts_When_No_Asset_Type_Is_Selected()
        countafterfilter = self.assetpage.get_total_row_count_filter()
        if countafterfilter == countbeforefilter:
            self.assertEqual(int(countbeforefilter), int(countafterfilter),"No records to filter.")
        else:
            self.assertNotEquals(int(countbeforefilter), int(countafterfilter),"Count is matching.")
        #sleep(2)

    @attr(priority="high")
    #@SkipTest
    def test_AS_087(self):
        """
        Test : test_AS_91
        Description : To verify chart when place filter is selected.
        Revision:
        :return: None
        """
        self.assetpage.get_asset_reset_button.click()
        self.assetpage.make_dashboard_on()
        countbeforefilter = self.assetpage.get_total_row_count()
        self.assetpage.asset_filter_based_on_place_and_school("Place")
        self.assetpage.place_related_charts_Place_Is_Selected()
        countafterfilter = self.assetpage.get_total_row_count_filter()

        if countafterfilter == countbeforefilter:
            self.assertEqual(int(countbeforefilter), int(countafterfilter),"No records to filter.")
        else:
            self.assertNotEquals(int(countbeforefilter), int(countafterfilter),"Count is matching.")
        #sleep(2) # sleep is mandatory here otherwise it will fail

    @attr(priority="high")
    #@SkipTest
    def test_AS_088(self):
        """
        Test : test_AS_92
        Description : To verify chart when place and type filters are selected.
        Revision:
        :return: None
        """
        self.assetpage.get_asset_reset_button.click()
        self.assetpage.make_dashboard_on()
        countbeforefilter = self.assetpage.get_total_row_count()
        self.assetpage.asset_filter_based_on_place_and_school("Place")
        self.assetpage.get_asset_place_type_drop_down.click()
        self.assetpage.get_asset_place_type_first_element.click()
        self.assetpage.place_related_charts_Place_And_Type_Is_Selected()
        sleep(2)
        countafterfilter = self.assetpage.get_total_row_count_filter()
        if countafterfilter == countbeforefilter:
            self.assertEqual(int(countbeforefilter), int(countafterfilter),"No records to filter.")
        else:
            self.assertNotEquals(int(countbeforefilter), int(countafterfilter),"Count is matching.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_089(self):
        """
        Test : test_AS_93
        Description : To verify chart when school filter is selected.
        Revision:
        :return: None
        """
        self.assetpage.get_asset_reset_button.click()
        self.assetpage.make_dashboard_on()
        countbeforefilter = self.assetpage.get_total_row_count()
        self.assetpage.asset_filter_based_on_place_and_school("School")
        sleep(1)
        self.assetpage.school_related_charts_School_Is_Selected()
        countafterfilter = self.assetpage.get_total_row_count_filter()

        if countafterfilter == countbeforefilter:
            self.assertEqual(int(countbeforefilter), int(countafterfilter),"No records to filter.")
        else:
            self.assertNotEquals(int(countbeforefilter), int(countafterfilter),"Count is matching.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_090(self):
        """
        Test : test_AS_94
        Description : To verify chart when school and district filters are selected.
        Revision:
        :return: None
        """
        self.assetpage.get_asset_reset_button.click()
        self.assetpage.make_dashboard_on()
        countbeforefilter = self.assetpage.get_total_row_count()
        self.assetpage.asset_filter_based_on_place_and_school("School")
        self.assetpage.get_asset_school_district_drop_down.click()
        self.assetpage.get_asset_school_district_first_element.click()
        sleep(1)# sleep is mandatory here otherwise it will fail
        self.assetpage.school_related_charts_School_And_District_Is_Selected()
        countafterfilter = self.assetpage.get_total_row_count_filter()

        if countafterfilter == countbeforefilter:
            self.assertEqual(int(countbeforefilter), int(countafterfilter),"No records to filter.")
        else:
            self.assertNotEquals(int(countbeforefilter), int(countafterfilter),"Count is matching.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_091(self):
        """
        Test : test_AS_95
        Description : To verify chart when school and grade filters are selected.
        Revision:
        :return: None
        """
        self.assetpage.get_asset_reset_button.click()
        self.assetpage.make_dashboard_on()
        countbeforefilter = self.assetpage.get_total_row_count()
        self.assetpage.asset_filter_based_on_place_and_school("School")
        self.assetpage.get_asset_school_grade_drop_down.click()
        self.assetpage.get_asset_school_grade_first_element.click()
        sleep(1)# sleep is mandatory here otherwise it will fail
        self.assetpage.school_related_charts_School_And_Grade_Is_Selected()
        countafterfilter = self.assetpage.get_total_row_count_filter()
        if countafterfilter == countbeforefilter:
            self.assertEqual(int(countbeforefilter), int(countafterfilter),"No records to filter.")
        else:
            self.assertNotEquals(int(countbeforefilter), int(countafterfilter),"Count is matching.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_092(self):
        """
        Test : test_AS_96
        Description : To verify chart when school and type filters are selected.
        Revision:
        :return: None
        """
        self.assetpage.get_asset_reset_button.click()
        self.assetpage.make_dashboard_on()
        countbeforefilter = self.assetpage.get_total_row_count()
        self.assetpage.asset_filter_based_on_place_and_school("School")
        self.assetpage.get_asset_school_type_drop_down.click()
        self.assetpage.get_asset_school_type_first_element.click()
        sleep(1)# sleep is mandatory here otherwise it will fail
        self.assetpage.school_related_charts_School_And_Type_Is_Selected()
        countafterfilter = self.assetpage.get_total_row_count_filter()
        if countafterfilter == countbeforefilter:
            self.assertEqual(int(countbeforefilter), int(countafterfilter),"No records to filter.")
        else:
            self.assertNotEquals(int(countbeforefilter), int(countafterfilter),"Count is matching.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_093_to_test_pagination_next_button(self):
        """
        Test : test_AS_97
        Description :To Test pagination next button.
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
    def test_AS_094_to_test_pagination_next_button_disabled(self):
        """
        Test : test_AS_98
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
    def test_AS_095_to_test_pagination_previous_button(self):
        """
        Test : test_AS_99
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
    def test_AS_096_to_test_pagination_previous_button_disabled(self):
        """
        Test : test_AS_100
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
    def test_AS_097_to_test_pagination_page_group_select(self):
        """
        Test : test_AS_101
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
            last_page = (list_of_page_drop_down[-1].text.encode('utf-8')).split("-")[1]
            last_page_first = (list_of_page_drop_down[-1].text.encode('utf-8')).split("-")[0]
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
    def test_AS_098_to_test_direct_click_first_page(self):
        """
        Test : test_AS_102
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
    def test_AS_099_to_test_direct_click_last_page(self):
        """
        Test : test_AS_103
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
    def test_AS_100_to_test_search_asset_pagination(self):
        """
        Test : test_AS_104
        Description :To verify that if searched asset is not available than pagination should be disabled.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        self.assetpage.asset_search_assetname("123$%")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element
                       ((By.XPATH, self.assetpage._asset_search_no_matching_text_locator), "No matching records found"))
        if self.assetpage.get_asset_search_no_matching_text.is_displayed():
            list_of_nodes = self.pagination.get_pg_list_of_nodes
            node_length = len(list_of_nodes)
            previous_node_text = list_of_nodes[0].get_attribute("class")
            next_node_text = list_of_nodes[-1].get_attribute("class")
            sleep(2)
            if(previous_node_text == "previous disabled") and (next_node_text == "next disabled") and (node_length==3):
                self.assertTrue(True, "No Pages available but still next and previous button is enabled.")
            else:
                self.assertFalse(True, "No Pages available but still next and previous button is enabled.")


    @attr(priority="high")
    #@SkipTest
    def test_AS_101_and_102(self):
        """
        Test : test_AS_101_and_102
        Description : To create place asset and verify that asset is created properly.
        Revision:
        Author : Kiran
        :return: None
        """
        check = 0
        self.assetpage.create_asset("Person")
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_name_breadcrumb), self.assetpage.get_asset_name_breadcrumb.text))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                    (By.LINK_TEXT, self.assetpage._asset_link_locator))).click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, self.assetpage._asset_select_action_delete_select_xpath_locator)))
        self.assetpage.asset_search_assetname(self.assetpage.asset_person_name)
        sleep(10) # Necessary sleep to let the app search for the input string
        for item in self.assetpage.get_asset_list_background:
            if (item.text  == self.assetpage.asset_place_name) and (item.value_of_css_property("background-color")\
                                                                == "rgba(255, 236, 158, 1)"):
                check = 1
                break
        self.assetpage.textbox_clear(self.driver.find_element_by_xpath(self.assetpage._asset_search_textbox_locator))
        self.assertFalse(check == 0, self.config.get(self.section,'MESSAGE_NEW_ASSET_NOT_APPEARING_ON_YELLOW_BACKGROUND'))


    @attr(priority="high")
    #@SkipTest
    def test_AS_104(self):
        """
        Test : test_AS_16
        Description : To verify New Asset phone field.
        Revision:
        :return: None
        """
        self.assetpage.asset_create_click()
        self.assetpage.select_asset_template_type("Person")
        asset_phone = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH ,self.assetpage._asset_overview_phone_text_box_locator)))
        asset_phone.send_keys("123abc1234")
        asset_phone.send_keys(Keys.TAB)
        regex = re.compile(r'^\(?([0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([0-9]{4})$')
        self.assertRegexpMatches("123abc1234", regex,
                                 self.config.get(self.section, 'MESSAGE_PHONE_VALUE_NOT_MATCHING'))
        self.assetpage.asset_overview_cancel_click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_105(self):
        """
        Test : test_AS_20
        Description : To edit overview section. Enter all required fields info and click on save button.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_person_name, "Person")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_details_edit_widget_locator), r"Details"))
        self.assetpage.get_asset_overview_edit_link.click()
        self.assetpage.set_person_overview_fields(r"Ind address", r"Ind address 2", r"Ind city", r"KA", r"94821", r"98989898", r"pp@p.com")
        self.assetpage.asset_overview_save_click()# Click on Save
        self.assertTrue(self.assetpage.asset_type_Saved_label.is_displayed(),
                        self.config.get(self.section, 'MESSAGE_SAVED_TEXT_NOT_DISPLAYED'))

    @attr(priority="high")
    #@SkipTest
    def test_AS_106(self):
        """
        Test : test_AS_106
        Description : To edit overview section. Enter all required fields info and click on cancel button.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_person_name, "Person")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_details_edit_widget_locator), r"Details"))
        self.assetpage.get_asset_overview_edit_link.click()
        self.assetpage.set_person_overview_fields(r"Ind address", r"Ind address 2", r"Ind city", r"KA", r"94821", r"98989898", r"pp@p.com")
        self.assetpage.asset_overview_cancel_click()#click on Cancel
        self.assertEqual(self.assetpage.asset_person_name, self.assetpage.get_asset_name_breadcrumb.text)


    @attr(priority="high")
    #@SkipTest
    def test_AS_107(self):
        """
        Test : test_AS_107
        Description : To edit Details section. Enter all required fields info and click on save button.
        Revision:
        :return: None
        """
        self.assetpage.select_school_or_place_asset(self.assetpage.asset_person_name, "Person")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element(
            (By.XPATH, self.assetpage._asset_details_edit_widget_locator), r"Details"))
        self.assetpage.get_asset_detail_edit_link.click()
        self.assetpage.set_person_details_fields()
        self.assetpage.get_asset_detail_edit_save_button.click()
        self.assertTrue(self.assetpage.asset_type_Saved_label.is_displayed(),
                        self.config.get(self.section, 'MESSAGE_SAVED_TEXT_NOT_DISPLAYED'))
