import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pages.assetpage import AssetPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from time import sleep
import json, os, re
from selenium.webdriver.common.action_chains import ActionChains


class AssetPageTest(BaseTestCase):

    @attr(priority="high")
    #@SkipTest
    def test_AS_01(self):
        '''
        Description : To verify delete functionality when no assets are available. Delete button should be disabled.

        Revision:

        :return:
        '''
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.get_asset_select_action_drop_down.click()
        self.assertFalse(assetpage.get_asset_link_delete_text.is_enabled(),
                         "Delete must be disabled when no assets are available.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_02(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.get_select_checkbox_in_grid()
        assetpage.get_asset_select_action_drop_down.click()
        self.assertFalse(assetpage.get_asset_link_delete_text.is_enabled(),
                         "Delete must be disabled when no assets are selected.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_03(self):
        AssetPage(self.driver).get_asset_list_first_check_box.click()
        AssetPage(self.driver).get_asset_select_action_drop_down.click()
        AssetPage(self.driver).get_asset_link_delete_text.click()
        sleep(5)
        pcountText = self.driver.find_element_by_id("assetstable_info").text # get the current count
        print pcountText
        pparts = pcountText.split(" ")
        pvalue11 = pparts[10]
        print pvalue11
        sleep(5)
        AssetPage(self.driver).get_asset_delete_button.click() # Delete
        sleep(5)
        afterDeleteCount = self.driver.find_element_by_id("assetstable_info").text # count after delete
        print afterDeleteCount
        aparts = afterDeleteCount.split(" ")
        avalue11 = aparts[10]
        sleep(5)
        print("Record deleted successfully.")


    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_AS_04(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.get_asset_list_first_check_box.click()
        assetpage.get_asset_select_action_drop_down.click()
        assetpage.get_asset_link_delete_text.click()
        sleep(5)
        assetpage.get_deleteasset_cancel_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_06(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.asset_filter_based_on_place_and_school("Place")
        self.assertTrue(assetpage.get_asset_place_type_drop_down.is_displayed(), "Invalid filter")
        assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_07(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.asset_filter_based_on_place_and_school("School")
        self.assertTrue(assetpage.get_asset_school_district_drop_down.is_displayed(), "Invalid filter")
        assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_08(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.get_asset_school_district()
        for item in assetpage.select_asset_type_district_lists:
            self.assertEqual(assetpage.selecteddistrict, item.text)
        assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_09(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.get_asset_school_grade()
        for item in assetpage.select_asset_type_grade_lists:
            self.assertEqual(assetpage.selectedgrade, item.text)
        assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_10(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        AssetPage(self.driver).get_asset_reset_button.click()
        assetpage.get_asset_school_type()
        for item in assetpage.select_asset_type_type_lists:
            self.assertEqual(assetpage.selectedtype, item.text)
        assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_11(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.get_asset_reset_button.click()
        expectedAfterResetFilter = assetpage.get_asset_asset_type_text.text
        self.assertEqual("Asset Type",expectedAfterResetFilter)

    @attr(priority="high")
    #@SkipTest
    def test_AS_12(self):
        cwd = os.getcwd()
        os.chdir('..')
        searchasset_filepath = os.path.join(os.getcwd(), "data\json_searchAssets.json")
        os.chdir(cwd)
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        sleep(10)
        with open(searchasset_filepath) as data_file:
            data_SearchAsset_text = json.load(data_file)
            for each in data_SearchAsset_text:
                searchText = each["Search_name"]
                assetpage.select_asset_search_text_box.clear()
                assetpage.select_asset_search_text_box.send_keys(searchText)
                sleep(2)
                expectedAfterSearchFilter = assetpage.get_asset_list_no_matching_records_found.text
                searchNames = self.driver.find_elements_by_xpath(assetpage._asset_list_locator)
                print "Found " + str(len(searchNames)) + " by Name search."
                sleep(2)
                for searchName in searchNames:
                    if expectedAfterSearchFilter:
                        self.assertEqual("No matching records found", expectedAfterSearchFilter,
                                         "No records to find asset.")
                        sleep(2)
                    else:
                        print searchName.text
                        sleep(2)

    @attr(priority="high")
    #@SkipTest
    def test_AS_13(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.asset_search_assetname("{}")
        assetpage.asset_search_special_characters()
        sleep(2)
        assetpage.asset_search_assetname("")

    @attr(priority="high")
    #@SkipTest
    def test_AS_14_and_17(self):
        check = 0
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.create_asset("Place")
        sleep(10)
        #WebDriverWait(self.driver,20).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='header']/div[1]/span[3]/span")))
        self.assertEqual(assetpage.asset_place_name, assetpage.get_asset_name_breadcrumb.text)
        assetpage.retuntoappmainpage()
        sleep(5)
        assetpage.asset_search_assetname(assetpage.asset_place_name)
        sleep(5)
        for i in assetpage.get_asset_name_list_back_color:
            if (i.text  == assetpage.asset_place_name) and (i.value_of_css_property("background-color") \
                                                                == "rgba(255, 236, 158, 1)"):
                check = 1
                #self.assertEqual("rgba(255, 236, 158, 1)", i.value_of_css_property("background-color"))
                break
        assetpage.textbox_clear(self.driver.find_element_by_xpath(assetpage._asset_search_textbox_locator))
        self.assertFalse(check == 0, "Newly created asset is not appearing with yellow background")


    @attr(priority="high")
    #@SkipTest
    def test_AS_15(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.asset_create_click()
        assetpage.select_asset_template_type("Place")
        sleep(2)
        aname = ""
        assetpage.enter_asset_type_name.send_keys(aname)
        sleep(5)
        if aname == '':
            self.assertFalse(assetpage.get_asset_overview_save_button.is_enabled(), "Save button is not disabled.")
        assetpage.asset_overview_cancel_click()


    @attr(priority="high")
    #@SkipTest
    def test_AS_16(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.asset_create_click()
        assetpage.select_asset_template_type("Place")
        sleep(2)
        assetpage.enter_asset_type_phone.send_keys("123abc1234")
        assetpage.enter_asset_type_phone.send_keys(Keys.TAB)
        sleep(5)
        regex = re.compile(r'^\(?([0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([0-9]{4})$')
        self.assertRegexpMatches("123abc1234", regex, "Expected and actual value is not matching for EMAIL")
        assetpage.asset_overview_cancel_click()


    @attr(priority="high")
    #@SkipTest
    def test_AS_18(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        sleep(5)
        assetpage.asset_create_click()
        assetpage.asset_overview_cancel_click()
        expectedAfterResetFilter = assetpage.get_asset_asset_type_text.text
        self.assertEqual("Asset Type",expectedAfterResetFilter)# Checking "Asset Type" displayed after reset

    @attr(priority="high")
    #@SkipTest
    def test_AS_19(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        sleep(5)
        assetpage.asset_create_click()
        assetpage.create_place_asset()
        assetpage.asset_overview_cancel_click()
        expectedAfterResetFilter = assetpage.get_asset_asset_type_text.text
        self.assertEqual("Asset Type",expectedAfterResetFilter)# Checking "Asset Type" displayed after reset

    @attr(priority="high")
    #@SkipTest
    def test_AS_20(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)
        assetpage.get_asset_overview_edit_link.click()
        assetpage.set_place_overview_fields("kk address", "kk address 2", "kk city", "KA", "94821", "Indecomm")
        assetpage.asset_overview_save_click()# Click on Save
        self.assertTrue(assetpage.asset_type_Saved_label.is_displayed(), "Saved text is not displayed")
        assetpage.retuntoappmainpage()

    @attr(priority="high")
    #@SkipTest
    def test_AS_21(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)
        assetpage.get_asset_overview_edit_link.click()
        assetpage.set_place_overview_fields("kk address cancel", "kk address 2 cancel", "kk city", "KA", "94821",
                                            "Indecomm")
        assetpage.asset_overview_cancel_click()
        self.assertEqual(assetpage.asset_place_name, assetpage.get_asset_name_breadcrumb.text)
        assetpage.retuntoappmainpage()

    @attr(priority="high")
    #@SkipTest
    def test_AS_23(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(15)
        assetpage.get_asset_detail_edit_link.click()
        assetpage.set_place_details_fields("1234", "2017-05-16", "Description of School 3","", "ki22ran2.k@indecomm.net",
                                           "123-4567-892", "2015-02-23","", "6300", "http://www.haystax.com")
        assetpage.get_asset_detail_edit_save_button.click()
        sleep(10)
        self.assertTrue(assetpage.asset_type_Saved_label.is_displayed(), "Saved text is not displayed")
        assetpage.retuntoappmainpage()

    @attr(priority="high")
    #@SkipTest
    def test_AS_24(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(15)
        assetpage.get_asset_detail_edit_link.click()
        sleep(10)
        aemail = "test@email.com"
        assetpage.get_asset_detail_edit_email_text_box.clear()
        sleep(2)
        assetpage.get_asset_detail_edit_email_text_box.send_keys(aemail)
        sleep(2)
        assetpage.get_asset_detail_edit_email_text_box.send_keys(Keys.TAB)
        sleep(2)
        regex = re.compile(r'[\w.-]+@[\w.-]+')
        sleep(5)
        self.assertRegexpMatches(aemail, regex, "Expected and actual value is not matching for EMAIL")
        assetpage.get_asset_detail_edit_cancel_button.click()
        assetpage.retuntoappmainpage()

    @attr(priority="high")
    #@SkipTest
    def test_AS_25(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(15)
        assetpage.get_asset_detail_edit_link.click()# Click on Details panel
        sleep(10)
        assetpage.get_asset_detail_edit_detail_fax_text_box.clear()
        sleep(5)
        assetpage.get_asset_detail_edit_detail_fax_text_box.send_keys("123abc1234") #  Enter the value for FAX
        sleep(5)
        assetpage.get_asset_detail_edit_detail_fax_text_box.send_keys(Keys.TAB)
        sleep(5)
        regex = re.compile(r'^\(?([0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([0-9]{4})$')
        self.assertRegexpMatches("123abc1234", regex, "Expected and actual value is not matching for FAX")
        sleep(5)
        assetpage.get_asset_detail_edit_cancel_button.click()
        assetpage.retuntoappmainpage()

    @attr(priority="high")
    #@SkipTest
    def test_AS_26(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(15)
        assetpage.get_asset_detail_edit_link.click()
        sleep(10)
        assetpage.set_place_details_fields("4321", "2020-05-16", "Cancelled", "", "cancel@indecomm.net", "111-111-1111",
                                           "2017-02-23", "", "10001", "http://www.haystax.com")
        sleep(10)
        assetpage.get_asset_detail_edit_cancel_button.click()
        sleep(10)
        self.assertEqual(assetpage.asset_place_name, assetpage.get_asset_name_breadcrumb.text)
        assetpage.retuntoappmainpage()

    @attr(priority="high")
    #@SkipTest
    def test_AS_27(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(6)
        assetpage.delete_existing_contact() #delete existing contacts.
        assetpage.create_new_contact(firstname,lastname)#create new contact.
        act_new_contact_value = assetpage.get_asset_contact_new_contact_value_text.text
        exp_new_contact_value = lastname+", "+firstname+" Title "+"111-111-1111"+" test@test.com"
        assetpage.retuntoappmainpage()
        self.assertEqual(act_new_contact_value, exp_new_contact_value, "Expected and actual values for new contact are not matching.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_28(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(6)
        assetpage.delete_existing_contact()#delete existing contacts.
        assetpage.create_new_contact(firstname,lastname)#create new contact.
        try:
            if assetpage.get_asset_main_contact_window:
                act_name_value = assetpage.get_asset_main_contact_name_text.text
                exp_name_value = "Shri "+firstname+" "+lastname
                self.assertEqual(act_name_value,exp_name_value)#verify asset main contact first and last name value.
            assetpage.retuntoappmainpage()
        except NoSuchElementException:
            assetpage.retuntoappmainpage()
            self.assertFalse("No Main Contact exists.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_29(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)
        assetpage.delete_existing_contact()#delete existing contacts.
        assetpage.get_asset_points_of_contact_header.click()
        assetpage.get_asset_add_contact_button.click()#click on Add Contact button.
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        assetpage.get_asset_newcontact_firstname_textbox.clear()#clear first and last name.
        assetpage.get_asset_newcontact_lastname_textbox.clear()
        assetpage.get_asset_newcontact_prefix_textbox.clear()#clear Prefix filed.
        sleep(2)
        firstname_error = assetpage.get_asset_newcontact_firstname_error_message.is_displayed()#Verify Error messages.
        lastname_error = assetpage.get_asset_newcontact_lastname_error_message.is_displayed()
        sleep(2)
        assetpage.get_asset_newcontact_window_cross_button.click()#click on cross button to close window.
        sleep(2)
        assetpage.retuntoappmainpage()
        self.assertTrue(firstname_error, "Error message is not displayed for First Name.")
        self.assertTrue(lastname_error, "Error message is not displayed for Last Name.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_30(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)
        assetpage.delete_existing_contact()#delete existing contacts.
        assetpage.get_asset_points_of_contact_header.click()
        assetpage.get_asset_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        assetpage.get_asset_newcontact_firstname_textbox.clear()
        assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
        assetpage.get_asset_newcontact_lastname_textbox.clear()
        assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
        assetpage.get_asset_newcontact_phone_textbox.clear()
        assetpage.get_asset_newcontact_phone_textbox.send_keys(r"111-222-3343")
        assetpage.get_asset_newcontact_save_button.click()#click on save button.
        act_phone = assetpage.get_asset_contact_phone_value_text.text#reading act phone value.
        regex = re.compile(r'^\(?([A-Za-z0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([A-Za-z0-9]{4})$')
        assetpage.retuntoappmainpage()
        self.assertRegexpMatches(act_phone, regex, "Expected and actual phone value are not matching.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_31_1(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)
        assetpage.delete_existing_contact()#delete existing contacts.
        assetpage.get_asset_points_of_contact_header.click()
        assetpage.get_asset_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        assetpage.get_asset_newcontact_firstname_textbox.clear()
        assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
        assetpage.get_asset_newcontact_lastname_textbox.clear()
        assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
        assetpage.get_asset_newcontact_email_textbox.clear()
        assetpage.get_asset_newcontact_email_textbox.send_keys(r"test@test.com")
        assetpage.get_asset_newcontact_save_button.click()#click on save button.
        act_email = assetpage.get_asset_contact_email_value_text.text#reading actual email value.
        regex = re.compile(r'[\w.-]+@[\w.-]+')
        assetpage.retuntoappmainpage()
        self.assertRegexpMatches(act_email, regex, "Expected and actual value is not matching for EMAIL.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_31_2(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)
        assetpage.delete_existing_contact()#delete existing contacts.
        assetpage.get_asset_points_of_contact_header.click()
        assetpage.get_asset_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        assetpage.get_asset_newcontact_firstname_textbox.clear()
        assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
        assetpage.get_asset_newcontact_lastname_textbox.clear()
        assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
        assetpage.get_asset_newcontact_email_textbox.clear()
        assetpage.get_asset_newcontact_email_textbox.send_keys(r"testtest.com")
        sleep(2)
        assetpage.get_asset_newcontact_firstname_textbox.click()
        sleep(2)
        exp_error_message = assetpage.get_asset_newcontact_email_error_message.is_displayed()
        assetpage.get_asset_newcontact_window_cross_button.click()#Click on Cross button to close window.
        assetpage.retuntoappmainpage()
        self.assertTrue(exp_error_message, "Error message is not displayed for wrong EMAIL address.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_32(self):
        firstname = "FirstNameDel"
        lastname = "ZLastNameDel"
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)
        assetpage.delete_existing_contact()#delete existing contacts.
        assetpage.get_asset_points_of_contact_header.click()
        assetpage.get_asset_add_contact_button.click()#click on add contact button
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        assetpage.get_asset_newcontact_firstname_textbox.clear()
        assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
        assetpage.get_asset_newcontact_lastname_textbox.clear()
        assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
        assetpage.get_asset_newcontact_cancel_button.click()#click on cancel button.
        sleep(2)
        try:
            if assetpage.get_asset_contact_first_last_name_value_text.is_displayed():
                assetpage.retuntoappmainpage()
                self.assertFalse("Contact has been created. Cancel button is not working.")
        except:
            assetpage.retuntoappmainpage()
            self.assertTrue("New Contact is not created.")

    @attr(priority="high")
    def test_AS_33_1(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        assetpage.multiple_contact_create()#create multiple contacts.
        exp_name_ascending = r"stu, def, mno, jkl, ghi, pqr, abc, vwx"
        assetpage.get_asset_point_of_contact_name_tab.click()#click on contact name tab.
        sleep(2)
        act_name_list = assetpage.get_asset_point_of_contact_name_text_value#Reading all contact names.
        act_name_list_value = []
        for name in act_name_list:
            act_name_list_value.append(name.text)
        assetpage.retuntoappmainpage()
        self.assertEqual(exp_name_ascending, ", ".join(act_name_list_value))

    @attr(priority="high")
    def test_AS_33_2(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        assetpage.multiple_contact_create()#create multiple contacts.
        exp_name_descending = r"abc, vwx, ghi, pqr, mno, jkl, stu, def"
        assetpage.get_asset_point_of_contact_name_tab.click()#click on contact name tab.
        sleep(2)
        assetpage.get_asset_point_of_contact_name_tab.click()
        sleep(2)
        act_name_list = assetpage.get_asset_point_of_contact_name_text_value#Reading all contact's names.
        act_name_list_value =[]
        for name in act_name_list:
            act_name_list_value.append(name.text)
        assetpage.retuntoappmainpage()
        self.assertEqual(exp_name_descending, ", ".join(act_name_list_value))

    @attr(priority="high")
    def test_AS_33_3(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        assetpage.multiple_contact_create()#create multiple contacts.
        exp_title_ascending = r"CC, HH, PP, ZZ"
        assetpage.get_asset_point_of_contact_title_tab.click()#click on contact title tab.
        sleep(2)
        act_title_list = assetpage.get_asset_point_of_contact_title_text_value#Reading all contact's title values.
        act_title_list_value = []
        for title in act_title_list:
            act_title_list_value.append(title.text)
        self.assertEqual(exp_title_ascending, ", ".join(act_title_list_value))

    @attr(priority="high")
    def test_AS_33_4(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        assetpage.multiple_contact_create()#create multiple contacts.
        exp_title_descending = r"ZZ, PP, HH, CC"
        assetpage.get_asset_point_of_contact_title_tab.click()#click on contact title tab.
        sleep(1)
        assetpage.get_asset_point_of_contact_title_tab.click()
        sleep(2)
        act_title_list = assetpage.get_asset_point_of_contact_title_text_value#Reading all contact's title values.
        act_title_list_value = []
        for title in act_title_list:
            act_title_list_value.append(title.text)
        assetpage.retuntoappmainpage()
        self.assertEqual(exp_title_descending, ", ".join(act_title_list_value))

    @attr(priority="high")
    def test_AS_33_5(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        assetpage.multiple_contact_create()#create multiple contacts.
        exp_phone_ascending = r"123-444-4444, 222-222-2222, 433-333-3333, 661-111-1111"
        assetpage.get_asset_point_of_contact_phone_tab.click()#click on contact phone tab.
        sleep(2)
        act_phone_list = assetpage.get_asset_point_of_contact_phone_text_value#Reading all contact's phone values.
        act_phone_list_value = []
        for phone in act_phone_list:
            act_phone_list_value.append(phone.text)
        self.assertEqual(exp_phone_ascending, ", ".join(act_phone_list_value))

    @attr(priority="high")
    def test_AS_33_6(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        assetpage.multiple_contact_create()#create multiple contacts.
        exp_phone_descending = r"661-111-1111, 433-333-3333, 222-222-2222, 123-444-4444"
        assetpage.get_asset_point_of_contact_phone_tab.click()#click on contact phone tab.
        sleep(1)
        assetpage.get_asset_point_of_contact_phone_tab.click()
        sleep(2)
        act_phone_list = assetpage.get_asset_point_of_contact_phone_text_value#Reading all contact's phone values.
        act_phone_list_value = []
        for phone in act_phone_list:
            act_phone_list_value.append(phone.text)
        assetpage.retuntoappmainpage()
        self.assertEqual(exp_phone_descending, ", ".join(act_phone_list_value))

    @attr(priority="high")
    def test_AS_33_7(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        assetpage.multiple_contact_create()#create multiple contacts.
        exp_email_ascending = r"abc@def, ghi@jkl, mno@pqr, stu@vwx"
        assetpage.get_asset_point_of_contact_email_tab.click()  #click on contact email tab.
        sleep(2)
        act_email_list = assetpage.get_asset_point_of_contact_email_text_value#Reading all contact's email values.
        act_email_list_value = []
        for email in act_email_list:
            act_email_list_value.append(email.text)
        self.assertEqual(exp_email_ascending, ", ".join(act_email_list_value))

    @attr(priority="high")
    def test_AS_33_8(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(6)
        assetpage.multiple_contact_create()#create multiple contacts.
        exp_email_descending = r"stu@vwx, mno@pqr, ghi@jkl, abc@def"
        assetpage.get_asset_point_of_contact_email_tab.click()#click on contact email tab.
        sleep(1)
        assetpage.get_asset_point_of_contact_email_tab.click()
        sleep(2)
        act_email_list = assetpage.get_asset_point_of_contact_email_text_value#Reading all contact's email values.
        act_email_list_value = []
        for email in act_email_list:
            act_email_list_value.append(email.text)
        assetpage.retuntoappmainpage()
        self.assertEqual(exp_email_descending, ", ".join(act_email_list_value))

    @attr(priority="high")
    #@SkipTest
    def test_AS_34(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        assetpage.delete_existing_contact()#delete existing contacts.
        assetpage.get_asset_points_of_contact_header.click()
        assetpage.get_asset_add_contact_button.click()#click on add contact button.
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        assetpage.get_asset_newcontact_firstname_textbox.clear()
        assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
        assetpage.get_asset_newcontact_lastname_textbox.clear()
        assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
        assetpage.get_asset_newcontact_save_button.click()#click on save button.
        assetpage.delete_existing_contact()#delete existing contacts.
        try:
            if assetpage.get_asset_newcontact_delete_icon.is_displayed():
                sleep(2)
                self.assertFalse("New Contact is not Deleted")
        except NoSuchElementException:
            self.assertTrue("The Contact has been Deleted")

    @attr(priority="high")
    #@SkipTest
    def test_AS_35(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        assetpage.delete_existing_contact()#delete existing contacts.
        assetpage.get_asset_points_of_contact_header.click()
        assetpage.get_asset_add_contact_button.click()
        WebDriverWait(self.driver,30).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, assetpage._assets_points_of_contact_title_locator), r"Contact information"))
        assetpage.get_asset_newcontact_firstname_textbox.clear()
        assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
        assetpage.get_asset_newcontact_lastname_textbox.clear()
        assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
        assetpage.get_asset_newcontact_save_button.click()
        try:
            if assetpage.get_asset_newcontact_delete_icon.is_displayed():
                sleep(2)
                assetpage.get_asset_newcontact_delete_icon.click()
                sleep(2)
                assetpage.get_asset_newcontact_delete_popup_cancel_button.click()
                sleep(2)
                self.assertTrue("Pass. Cancel Button is working properly.")
        except NoSuchElementException:
            self.assertFalse("The Contact has been Deleted.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_36(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)
        WebDriverWait(self.driver,50).until(expected_conditions.presence_of_element_located((By.ID,"map_control")))
        locationEdit = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[4]/div/div[2]/div/img")
        locationEdit.click()
        sleep(5)
        locationTitle = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/div").text
        self.assertEqual("Asset location", locationTitle, "Location Title not displayed")
        sleep(5)
        lati = "550"
        latitudeValue = self.driver.find_element_by_name("latitude")
        latitudeValue.clear()
        latitudeValue.send_keys(lati)
        latitudeerrorMessage = self.driver.find_element_by_xpath(".//*[@id='map_popup']/div[1]/span/small").text
        self.assertEqual("Latitude must be a number between -90 and 90", latitudeerrorMessage, "Latitude error message"
                                                                                               " not displayed")
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        self.assertFalse(locationSave.is_enabled(), "Location Save button is not disabled")
        longi = "200"
        longitudeValue = self.driver.find_element_by_name("longitude")
        longitudeValue.clear()
        longitudeValue.send_keys(longi)
        longitudeerrorMessage = self.driver.find_element_by_xpath(".//*[@id='map_popup']/div[2]/span/small").text
        self.assertEqual("Longitude must be a number between -180 and 180", longitudeerrorMessage,
                         "Longitude error message not displayed")
        sleep(5)
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        self.assertFalse(locationSave.is_enabled(), "Location Save button is not disabled")
        self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[1]").click()
        assetpage.retuntoappmainpage()


    @attr(priority="high")
    #@SkipTest
    def test_AS_37(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)
        WebDriverWait(self.driver,50).until(expected_conditions.presence_of_element_located((By.ID,"map_control")))
        locationEdit = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[4]/div/div[2]/div/img")
        locationEdit.click()
        sleep(5)
        locationTitle = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/div").text
        self.assertEqual("Asset location", locationTitle, "Location Title not displayed")
        sleep(5)
        lati = "40.7127"
        latitudeValue = self.driver.find_element_by_name("latitude")
        latitudeValue.clear()
        latitudeValue.send_keys(lati)
        sleep(5)
        longi = "74.0059"
        longitudeValue = self.driver.find_element_by_name("longitude")
        longitudeValue.clear()
        longitudeValue.send_keys(longi)
        sleep(5)
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        self.assertTrue(locationSave.is_enabled(), "Location Save button is not disabled")
        locationSave.click()
        sleep(15)
        markerAvailable =  self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[2]/div[3]/img")
        self.assertTrue(markerAvailable.is_displayed(), "Marker not displayed on Map")
        assetpage.retuntoappmainpage()

    @attr(priority="high")
    #@SkipTest
    def test_AS_38(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)
        WebDriverWait(self.driver,50).until(expected_conditions.presence_of_element_located((By.ID,"map_control")))
        locationEdit = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[4]/div/div[2]/div/img")
        locationEdit.click()
        sleep(5)
        locationTitle = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/div").text
        self.assertEqual("Asset location", locationTitle, "Location Title not displayed")
        sleep(5)
        lati = "40.7127"
        latitudeValue = self.driver.find_element_by_name("latitude")
        latitudeValue.clear()
        latitudeValue.send_keys(lati)
        sleep(5)
        longi = "74.0059"
        longitudeValue = self.driver.find_element_by_name("longitude")
        longitudeValue.clear()
        longitudeValue.send_keys(longi)
        sleep(5)
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        self.assertTrue(locationSave.is_enabled(), "Location Save button is not disabled")
        locationSave.click()
        sleep(15)
        markerAvailable =  self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[2]/div[3]/img")
        self.assertTrue(markerAvailable.is_displayed(), "Marker not displayed on Map")
        sleep(5)
        markerAvailable.click()
        sleep(5)
        placeText = self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[2]/div[4]/div/div[1]/div/b").text
        self.assertEqual(assetpage.asset_place_name, placeText, "Marker name not displayed.")
        assetpage.retuntoappmainpage()


    @attr(priority="high")
    def test_AS_40(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        assetpage.delete_uploaded_files()#Delete all uploaded files.
        caption_val = "Test_Case_40"
        image_file_name = "Test_Case_40.jpg"
        assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
        image_count_after_file_upload = len(number_of_image_after_upload)
        try:
            caption_path = "//div//a[contains(text(),'"+caption_val+"')]//preceding-sibling::img" \
                                                                    "[@class='neutron_document_img']"
            image_icon = self.driver.find_element_by_xpath(caption_path)
            Hover = ActionChains(self.driver).move_to_element(image_icon)
            Hover.perform()
            delete_icon = self.driver.find_element_by_xpath(".//img[contains(@src,'delete_icon')]")
            delete_icon.click()
            sleep(2)
            self.driver.find_element_by_xpath("//div[@id='delete_document_modal']//button[contains(text(),"
                                              "'Delete')]").click()
            sleep(10)
        except NoSuchElementException:
            self.assertFalse(1,"File could not be deleted.")
        number_of_image_after_delete = assetpage.get_asset_photos_documents_header_text
        image_count_after_file_delete = len(number_of_image_after_delete)
        if (image_count_after_file_upload == image_count_after_file_delete+1):
            try:
                if (assetpage.get_asset_photos_documents_header_caption_text(caption_val).is_displayed()):
                    assetpage.retuntoappmainpage()
                    self.assertFalse("Test Case has been failed.")
            except NoSuchElementException:
                assetpage.retuntoappmainpage()
                self.assertTrue("Test Case 40 has been passed.")
        else:
            assetpage.retuntoappmainpage()
            self.assertFalse("Test Case 40 has been failed.")

    @attr(priority="high")
    def test_AS_41(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        assetpage.delete_uploaded_files()#Delete all uploaded files.
        number_of_image_before_upload = assetpage.get_asset_photos_documents_header_text
        image_count_before_file_upload = len(number_of_image_before_upload)
        assetpage.get_asset_photos_documents_upload_file_button.click()
        sleep(2)
        file_path = assetpage.file_path("Test_Case_41.jpg")
        assetpage.get_asset_photos_documents_attached_file_button.send_keys(file_path)
        sleep(3)
        caption_val = "Test_Case_41"
        assetpage.get_asset_photos_documents_caption_textbox.send_keys(caption_val)
        sleep(2)
        assetpage.get_asset_photos_documents_window_cancel_button.click()
        try:
            number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
            image_count_after_file_upload = len(number_of_image_after_upload)
            if (image_count_after_file_upload == image_count_before_file_upload):
                assetpage.retuntoappmainpage()
                self.assertTrue("Test Case 41 has been passed.")
            else:
                assetpage.retuntoappmainpage()
                self.assertFalse("Test Case 41 has been failed")
        except Exception, e:
            error = "Test Case no 41 has been failed. Error message is ::"+str(e)
            assetpage.retuntoappmainpage()
            self.assertFalse(1, error)

    @attr(priority="high")
    def test_AS_42(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(20)
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        assetpage.delete_uploaded_files()
        caption_val = "Test_Case_42"
        image_file_name = "Test_Case_42.jpg"
        assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
        header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)
        if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed()):
            assetpage.retuntoappmainpage()
            self.assertTrue("Test Case has been passed.")
        else:
            assetpage.retuntoappmainpage()
            self.assertFalse("Test Case has been failed. No Caption Displayed.")

    @attr(priority="high")
    def test_AS_43(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(15)
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        assetpage.delete_uploaded_files()
        caption_val = "Test_Case_43"
        image_file_name = "Test_Case_43.jpg"
        assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        try:
            WebDriverWait(self.driver, 200).until(expected_conditions.text_to_be_present_in_element(
                (By.XPATH, assetpage._asset_header_save_text_locator),r"415 - UNSUPPORTED MEDIA TYPE"))
        except:
            assetpage.retuntoappmainpage()
            self.assertFalse("Test Case has been failed. No Error message displayed for unsupported media size.")
        assetpage.retuntoappmainpage()
        self.assertTrue("Test Case has been passed.")

    @attr(priority="high")
    def test_AS_44_1(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(20)
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        assetpage.delete_uploaded_files()
        caption_val = "Test_Case_44_1"
        image_file_name = "Test_Case_44_1.pdf"
        assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
        header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)
        if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed() and
                                                        (assetpage.get_asset_header_save_text.text == r"Saved")):
            assetpage.retuntoappmainpage()
            self.assertTrue("Test Case has been passed.")
        else:
            assetpage.retuntoappmainpage()
            self.assertFalse("Test Case has been failed.")

    @attr(priority="high")
    def test_AS_44_2(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(20)
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        assetpage.delete_uploaded_files()
        caption_val = "Test_Case_44_2"
        image_file_name = "Test_Case_44_2.html"
        assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
        header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)
        if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed() and
                                                        (assetpage.get_asset_header_save_text.text == r"Saved")):
            assetpage.retuntoappmainpage()
            self.assertTrue("Test Case has been passed.")
        else:
            assetpage.retuntoappmainpage()
            self.assertFalse("Test Case has been failed.")

    @attr(priority="high")
    def test_AS_44_3(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(20)
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        assetpage.delete_uploaded_files()
        caption_val = "Test_Case_44_3"
        image_file_name = "Test_Case_44_3.txt"
        assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
        header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)
        if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed() and
                                                        (assetpage.get_asset_header_save_text.text == r"Saved")):
            assetpage.retuntoappmainpage()
            self.assertTrue("Test Case has been passed.")
        else:
            assetpage.retuntoappmainpage()
            self.assertFalse("Test Case has been failed.")

    @attr(priority="high")
    def test_AS_45(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        assetpage.delete_uploaded_files()
        number_of_image_before_upload = assetpage.get_asset_photos_documents_header_text
        image_count_before_file_upload = len(number_of_image_before_upload)
        caption_val = ["Test_Case_45_1", "Test_Case_45_2", "Test_Case_45_3"]
        image_file_name = ["Test_Case_45_1.jpg", "Test_Case_45_2.jpg", "Test_Case_45_3.jpg"]
        for num in range(3):
            assetpage.upload_a_file_with_caption(caption_val[num], image_file_name[num])
        number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
        image_count_after_file_upload = len(number_of_image_after_upload)
        if (image_count_after_file_upload == image_count_before_file_upload+3):
            assetpage.retuntoappmainpage()
            self.assertTrue("Test Case has been passed.")
        else:
            assetpage.retuntoappmainpage()
            self.assertFalse("Test Case has been failed.")

    @attr(priority="high")
    def test_AS_47(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        self.driver.execute_script("window.scrollTo(0, (document.body.scrollHeight)-100);")
        assetpage.delete_uploaded_files()
        number_of_image_before_upload = assetpage.get_asset_photos_documents_header_text
        image_count_before_file_upload = len(number_of_image_before_upload)
        caption_val = ""
        image_file_name = "Test_Case_47.jpg"
        assetpage.upload_a_file_with_caption(caption_val, image_file_name)
        number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
        image_count_after_file_upload = len(number_of_image_after_upload)
        header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(image_file_name)
        if (header_caption_text.is_displayed() and (image_count_after_file_upload == image_count_before_file_upload+1)):
            assetpage.retuntoappmainpage()
            self.assertTrue("Test Case has been passed")
        else:
            assetpage.retuntoappmainpage()
            self.assertFalse("Test Case has been failed")

    @attr(priority="high")
    def test_AS_48_1(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        exp_text_val = "This is Indecomm Testing. Groups."
        assetpage.delete_all_annotation()
        assetpage.get_asset_annotation_plus_image.click()
        assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)#Enter Annotation text.
        assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()#Select Annotation type.
        assetpage.get_asset_annotation_edit_window_dropdown_groups.click()
        assetpage.get_asset_annotation_edit_window_save_button.click()
        sleep(2)
        text_val = assetpage.get_asset_annotation_text_value.text#read annotation value.
        act_text_val = (text_val.split(' - '))[1].strip()
        assetpage.retuntoappmainpage()
        self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")

    @attr(priority="high")
    def test_AS_48_2(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        exp_text_val = "This is Indecomm Testing. Tenant."
        assetpage.delete_all_annotation()#delete All Annotation.
        assetpage.get_asset_annotation_plus_image.click()#Click on Annotation Plus image.
        assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)#Enter Annotation text.
        assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
        assetpage.get_asset_annotation_edit_window_dropdown_tenant.click()#Select Annotation type.
        assetpage.get_asset_annotation_edit_window_save_button.click()
        sleep(2)
        text_val = assetpage.get_asset_annotation_text_value.text#read annotation value.
        act_text_val = (text_val.split(' - '))[1].strip()
        assetpage.retuntoappmainpage()
        self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")

    @attr(priority="high")
    def test_AS_48_3(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        exp_text_val = "This is Indecomm Testing. Groups."
        assetpage.delete_all_annotation()#delete All Annotation.
        assetpage.get_asset_annotation_plus_image.click()#Click on Annotation Plus image.
        assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)#Enter Annotation text.
        assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
        assetpage.get_asset_annotation_edit_window_dropdown_user.click()#Select Annotation type.
        assetpage.get_asset_annotation_edit_window_save_button.click()
        sleep(2)
        text_val = assetpage.get_asset_annotation_text_value.text#read annotation value.
        act_text_val = (text_val.split(' - '))[1].strip()
        assetpage.retuntoappmainpage()
        self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")

    @attr(priority="high")
    def test_AS_48_4(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        exp_text_val = "This is Indecomm Testing. Gropus."
        assetpage.delete_all_annotation()#delete All Annotation.
        assetpage.get_asset_annotation_plus_image.click()#Click on Annotation Plus image.
        assetpage.get_asset_annotation_edit_window_text_area.send_keys("Random Text Value.")#Enter Annotation text.
        assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
        assetpage.get_asset_annotation_edit_window_dropdown_groups.click()#Select Annotation type.
        assetpage.get_asset_annotation_edit_window_save_button.click()
        sleep(2)
        assetpage.get_asset_annotation_edit_image.click()#click on annotation edit link.
        assetpage.get_asset_annotation_edit_window_text_area.clear()#clear annotation text.
        assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)#Enter new anootation text.
        assetpage.get_asset_annotation_edit_window_save_button.click()
        sleep(2)
        text_val = assetpage.get_asset_annotation_text_value.text
        act_text_val = (text_val.split(' - '))[1].strip()
        assetpage.retuntoappmainpage()
        self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")

    @attr(priotity = "high")
    @attr(status='smoke')
    def test_AS_49_50(self):
        flag = 0
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.create_asset("School")
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located \
                                            ((By.XPATH,"//*[@id='header']/div[1]/span[3]/span")))
        self.assertEqual(assetpage.asset_school_name[0], self.driver.find_element_by_xpath("//*[@id='header']"
                                                                                           "/div[1]/span[3]/span").text)
        assetpage.retuntoappmainpage()
        assetpage.asset_search_assetname(assetpage.asset_school_name[0])
        sleep(5)
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[2]"):
            if (i.text  == assetpage.asset_school_name[0]) and (i.value_of_css_property("background-color") ==
                                                                    "rgba(255, 236, 158, 1)"):
                flag = 1
                break
        assetpage.textbox_clear(self.driver.find_element_by_xpath(assetpage._asset_search_textbox_locator))
        assetpage.retuntoappmainpage()
        self.assertFalse(flag == 0, "Newly created asset is not appaering with yellow background")


    @attr(priority="high")
#    @SkipTest
    def test_AS_51(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.asset_create_click()
        assetpage.select_asset_template_type("School")
        self.assertFalse(assetpage.get_asset_overview_save_button.is_enabled())
        assetpage.get_asset_overview_cancel_button.click()
        sleep(5)
        self.assertTrue(self.driver.find_element_by_xpath(assetpage._asset_create_asset).is_displayed())

    @attr(priority="high")
#   @SkipTest
    def test_AS_53(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_create_click()
        assetpage.select_asset_template_type("School")
        assetpage.enter_asset_type_name.send_keys(assetpage.asset_school_name[0])
        assetpage.enter_school_district(assetpage.asset_school_district_grade_validation)
        assetpage.enter_school_grade(assetpage.asset_school_district_grade_validation)
        assetpage.asset_overview_save_click()
        self.assertEqual(assetpage.asset_school_district_grade_validation, assetpage.get_overview_district_text)
        self.assertEqual(assetpage.asset_school_district_grade_validation, assetpage.get_overview_grade_text)
        assetpage.retuntoappmainpage()

    @attr(priority="high")
    def test_AS_54(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.create_asset_cancel("School")
        self.assertTrue(self.driver.find_element_by_xpath(assetpage._asset_create_asset).is_displayed())

    @attr(priority="high")
    @SkipTest
    def test_AS_55(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.edit_asset("School")
        self.assertEqual(assetpage.asset_school_name[assetpage.editSchool], assetpage.
                         get_asset_overview_edit_name_text_box)
        self.assertEqual(assetpage.asset_school_district[1], assetpage.get_overview_district_text)
        self.assertEqual(assetpage.asset_school_grade[1], assetpage.get_overview_grade_text)

    @attr(priority="high")
    #@SkipTest
    def test_AS_56(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
        sleep(15)
        assetpage.get_asset_detail_edit_link.click()
        assetpage.set_place_details_fields("1234", "2017-05-16", "Description of School 3","2",
                                           "ki22ran2.k@indecomm.net", "123-4567-892", "2015-02-23", "3", "6300",
                                           "http://www.haystax.com")
        assetpage.get_asset_detail_edit_cancel_button.click()
        sleep(10)
        self.assertEqual(assetpage.asset_school_name[0], self.driver.find_element_by_xpath("//*[@id='header']/"
                                                                                           "div[1]/span[3]/span").text)
        assetpage.retuntoappmainpage()

    @attr(priority="high")
    #@SkipTest
    def test_AS_58(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
        sleep(15)
        assetpage.get_asset_detail_edit_link.click()
        assetpage.set_place_details_fields("1234", "2017-05-16", "Description of School 3","2",
                                           r"ki22ran2.k@indecomm.net", "123-4567-892", "2015-02-23", "3", "6300",
                                           "http://www.haystax.com")
        assetpage.get_asset_detail_edit_save_button.click()
        sleep(10)
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='header']/div[3]").is_displayed(),
                        "Saved text is not displayed")
        assetpage.retuntoappmainpage()

    @attr(priority="high")
    def test_AS_59_1(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
        sleep(10)
        assetpage.get_asset_detail_edit_link.click()
        WebDriverWait(self.driver,10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, assetpage._asset_detail_edit_title_locator), r"Asset details"))
        assetpage.get_asset_detail_edit_email_text_box.clear()
        assetpage.get_asset_detail_edit_email_text_box.send_keys("test@test")
        assetpage.get_asset_detail_edit_save_button.click()
        sleep(2)
        email = assetpage.get_asset_detail_email_value_text.text
        regex = re.compile(r'[\w.-]+@[\w.-]+')
        assetpage.retuntoappmainpage()
        self.assertRegexpMatches(email, regex, "Expected and actual value is not matching for EMAIL")

    @attr(priority="high")
    def test_AS_59_2(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
        sleep(8)
        assetpage.get_asset_detail_edit_link.click()
        WebDriverWait(self.driver,10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, assetpage._asset_detail_edit_title_locator), r"Asset details"))
        assetpage.get_asset_detail_edit_email_text_box.clear()
        assetpage.get_asset_detail_edit_email_text_box.send_keys("testtest")
        assetpage.get_asset_detail_edit_save_button.click()
        state = assetpage.get_asset_detail_edit_save_button.is_enabled()
        assetpage.get_asset_detail_edit_window_cross_button.click()
        sleep(2)
        assetpage.retuntoappmainpage()
        self.assertFalse(state, "Save Button is enabled even though EMAIL value is wrong")

    @attr(priority="high")
    #@SkipTest
    def test_AS_90(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        sleep(5)
        assetpage.get_asset_chart_dashboard_image.click()
        sleep(5)
        assetpage.charts_When_No_Asset_Type_Is_Selected()

    @attr(priority="high")
    #@SkipTest
    def test_AS_91(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        sleep(5)
        assetpage.asset_filter_based_on_place_and_school("Place")
        sleep(10)
        assetpage.place_related_charts_Place_Is_Selected()

    @attr(priority="high")
    #@SkipTest
    def test_AS_92(self):
        assetpage = AssetPage(self.driver)
        assetpage.app_sanity_check()
        sleep(5)
        assetpage.asset_filter_based_on_place_and_school("Place")
        sleep(10)
        assetpage.get_asset_place_type_drop_down.click()
        sleep(2)
        assetpage.get_asset_place_type_first_element.click()
        sleep(5)
        assetpage.place_related_charts_Place_And_Type_Is_Selected()

    @attr(priority="high")
    #@SkipTest
    def test_AS_93(self):
        assetpage = AssetPage(self.driver)
        sleep(5)
        assetpage.asset_filter_based_on_place_and_school("School")
        sleep(10)
        assetpage.school_related_charts_School_Is_Selected()

    @attr(priority="high")
    #@SkipTest
    def test_AS_94(self):
        assetpage = AssetPage(self.driver)
        sleep(5)
        assetpage.asset_filter_based_on_place_and_school("School")
        sleep(10)
        assetpage.get_asset_school_district_drop_down.click()
        sleep(2)
        assetpage.get_asset_school_district_first_element.click()
        sleep(2)
        assetpage.school_related_charts_School_And_District_Is_Selected()

    @attr(priority="high")
    #@SkipTest
    def test_AS_95(self):
        assetpage = AssetPage(self.driver)
        sleep(5)
        assetpage.asset_filter_based_on_place_and_school("School")
        sleep(10)
        assetpage.get_asset_school_grade_drop_down.click()
        sleep(2)
        assetpage.get_asset_school_grade_first_element.click()
        sleep(2)
        assetpage.school_related_charts_School_And_Grade_Is_Selected()

    @attr(priority="high")
    #@SkipTest
    def test_AS_96(self):
        assetpage = AssetPage(self.driver)
        sleep(5)
        assetpage.asset_filter_based_on_place_and_school("School")
        sleep(10)
        assetpage.get_asset_school_type_drop_down.click()
        sleep(2)
        assetpage.get_asset_school_type_first_element.click()
        sleep(2)
        assetpage.school_related_charts_School_And_Type_Is_Selected()

if __name__ =='__main__':
    unittest.main(verbosity=2)

