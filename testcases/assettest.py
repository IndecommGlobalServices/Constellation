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
import selenium.webdriver as webdriver


cwd = os.getcwd()
os.chdir('..')
searchasset_filepath = os.path.join(os.getcwd(), "data\json_searchAssets.json")
os.chdir(cwd)



class AssetPageTest(BaseTestCase):

    @attr(priority="high")
    #@SkipTest
    def test_AS_01_To_Verify_Delete_When_No_Assets_Are_Available(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.get_asset_select_action_drop_down.click()
        self.assertTrue(assetpage.get_asset_link_delete_text.is_enabled(), "Delete must be disabled.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_02_To_Verify_Delete_Deselect_All_Assets(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.get_select_checkbox_in_grid()
        assetpage.get_asset_select_action_drop_down.click()
        self.assertTrue(assetpage.get_asset_link_delete_text.is_enabled(), "Delete must be disabled.")

   
    @attr(priority="high")
    @SkipTest
    def test_AS_03_To_Verify_Delete_Asset_Should_Be_Deleted(self):
        AssetPage(self.driver).get_asset_list_first_check_box.click()
        AssetPage(self.driver).get_asset_select_action_drop_down.click()
        AssetPage(self.driver).get_asset_link_delete_text.click()
        sleep(5)
        AssetPage(self.driver).get_asset_delete_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_04_To_Verify_Delete_Asset_Cancel(self):
        AssetPage(self.driver).get_asset_list_first_check_box.click()
        AssetPage(self.driver).get_asset_select_action_drop_down.click()
        AssetPage(self.driver).get_asset_link_delete_text.click()
        sleep(5)
        AssetPage(self.driver).get_deleteasset_cancel_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_06_To_Verify_The_Filter_Function_Filter_By_Place(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_filter_based_on_place_and_school("Place")
        self.assertTrue(assetpage.get_asset_place_type_drop_down.is_displayed(), "Invalid filter")

    @attr(priority="high")
    #@SkipTest
    def test_AS_07_To_Verify_The_Filter_Function_Filter_By_School(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_filter_based_on_place_and_school("School")
        self.assertTrue(assetpage.get_asset_school_district_drop_down.is_displayed(), "Invalid filter")

    @attr(priority="high")
    #@SkipTest
    def test_AS_08_To_Verify_The_Filter_Function_Filter_By_School_District(self):
        assetpage = AssetPage(self.driver)
        assetpage.get_asset_school_district()
        for item in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[4]"):
            self.assertEqual(assetpage.selecteddistrict, item.text)
        assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_09_To_Verify_The_Filter_Function_Filter_By_School_Grade(self):
        assetpage = AssetPage(self.driver)
        assetpage.get_asset_school_grade()
        for item in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[5]"):
            self.assertEqual(assetpage.selectedgrade, item.text)
        assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_10_To_Verify_The_Filter_Function_Filter_By_School_Type(self):
        assetpage = AssetPage(self.driver)
        AssetPage(self.driver).get_asset_reset_button.click()
        assetpage.get_asset_school_type()
        for item in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[6]"):
            self.assertEqual(assetpage.selectedtype, item.text)
        assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_11_To_Verify_The_Reset_Filter_Function(self):
        assetpage = AssetPage(self.driver)
        assetpage.get_asset_reset_button.click()
        expectedAfterResetFilter = assetpage.get_asset_asset_type_text.text
        self.assertEqual("Asset Type",expectedAfterResetFilter)

    # Need to re-visit
    @attr(priority="high")
    #@SkipTest
    def test_AS_12_To_Verify_The_Search_For_Asset_Function_Search_By_Name(self):
        assetpage = AssetPage(self.driver)
        with open(searchasset_filepath) as data_file:
            data_SearchAsset_text = json.load(data_file)

            for each in data_SearchAsset_text:
                searchText = each["Search_name"]

                assetpage.select_asset_search_text_box.send_keys(searchText)
                sleep(2)
                assetpage.select_asset_search_text_box.send_keys(Keys.CONTROL,"a",Keys.DELETE)
                sleep(5)
                expectedAfterSearchFilter = assetpage.get_asset_list_no_matching_records_found.text
                searchNames = self.driver.find_elements_by_xpath(assetpage._asset_list_locator)
                print "Found " + str(len(searchNames)) + " by Name search."
                sleep(2)
                for searchName in searchNames:
                    if expectedAfterSearchFilter:
                        self.assertEqual("No matching records found", expectedAfterSearchFilter, "No records to find asset.")
                        sleep(2)
                    else:
                        print searchName.text
                        sleep(2)

    @attr(priority="high")
    #@SkipTest
    def test_AS_13_To_Verify_The_Search_For_Asset_Function_Search_By_Special_Characters(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_search_assetname("{}")
        assetpage.asset_search_special_characters()
        sleep(2)
        assetpage.asset_search_assetname("")

    @attr(priority="high")
    #@SkipTest
    def test_AS_14_17_To_Verify_Create_Asset_Function_Create_Place_Asset(self):
        check = 0
        assetpage = AssetPage(self.driver)
        assetpage.create_asset("Place")
        sleep(10)
        #WebDriverWait(self.driver,20).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='header']/div[1]/span[3]/span")))
        self.assertEqual(assetpage.asset_place_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        assetpage.retuntoappmainpage()
        sleep(5)
        assetpage.asset_search_assetname(assetpage.asset_place_name)
        sleep(5)
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[2]"):
            if (i.text  == assetpage.asset_place_name) and (i.value_of_css_property("background-color") == "rgba(255, 236, 158, 1)"):
                check = 1
                #self.assertEqual("rgba(255, 236, 158, 1)", i.value_of_css_property("background-color"))
                break
        assetpage.textbox_clear(self.driver.find_element_by_xpath(assetpage._asset_search_textbox_locator))
        self.assertFalse(check == 0, "Newly created asset is not appearing with yellow background")


    #This test case should always follow AS_14
    @attr(priority="high")
    @SkipTest
    def test_AS_17_To_Verify_That_Created_Asset_Displayed_In_The_List(self):
        check =0
        assetpage = AssetPage(self.driver)
        sleep(10)
        assetpage.asset_search_assetname(assetpage.asset_place_name)
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[2]"):
            if (i.text  == assetpage.asset_place_name) and (i.value_of_css_property("background-color") == "rgba(255, 236, 158, 1)"):
                check = 1
                #self.assertEqual("rgba(255, 236, 158, 1)", i.value_of_css_property("background-color"))
                break
        assetpage.textbox_clear(self.driver.find_element_by_xpath(assetpage._asset_search_textbox_locator))
        self.assertFalse(check == 0, "Newly created asset is not appearing with yellow background")

    @attr(priority="high")
    #@SkipTest
    def test_AS_15_To_Verify_Validation_Of_Name_Field(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_create_click()
        assetpage.select_asset_template_type("Place")
        sleep(2)
        aname = ""
        assetpage.enter_asset_type_name.send_keys(aname)
        #assetpage.enter_asset_type_name.send_keys(Keys.TAB)
        sleep(5)
        if aname == '':
            self.assertFalse(assetpage.get_asset_overview_save_button.is_enabled(), "Save button is not disabled.")
        assetpage.asset_overview_cancel_click()


    @attr(priority="high")
    #@SkipTest
    def test_AS_16_To_Verify_Validation_Of_Phone_Field(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_create_click()
        assetpage.select_asset_template_type("Place")
        sleep(2)
        aphone = "123abc1234"
        assetpage.enter_asset_type_phone.send_keys(aphone)
        assetpage.enter_asset_type_phone.send_keys(Keys.TAB)

        sleep(5)
        regex = re.compile(r'^\(?([0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([0-9]{4})$')
        self.assertRegexpMatches(aphone, regex, "Expected and actual value is not matching for EMAIL")
        assetpage.asset_overview_cancel_click()


    @attr(priority="high")
    #@SkipTest
    def test_AS_18_To_Verify_Create_Asset_Function_Cancel_Place_Asset(self):
        assetpage = AssetPage(self.driver)
        sleep(5)
        assetpage.asset_create_click()
        assetpage.asset_overview_cancel_click()
        expectedAfterResetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div/div/button[1]").text
        self.assertEqual("Asset Type",expectedAfterResetFilter)

    @attr(priority="high")
    #@SkipTest
    def test_AS_19_To_Verify_Create_Asset_Function_Cancel_Place_Asset(self):
        assetpage = AssetPage(self.driver)
        sleep(5)
        assetpage.asset_create_click()
        assetpage.create_place_asset()
        assetpage.asset_overview_cancel_click()
        expectedAfterResetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div/div/button[1]").text
        self.assertEqual("Asset Type",expectedAfterResetFilter)

    @attr(priority="high")
    #@SkipTest
    def test_AS_20_To_Verify_That_The_Asset_In_Overview_Panel_Edit_Mode_Is_Saved_Successfully(self):
        assetpage = AssetPage(self.driver)

    # Search and Click on Place in the List for EDIT mode
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)

    # Click on Overview panel
        assetpage.get_asset_overview_edit_link.click()

    # Modify the values
        assetpage.set_place_overview_fields("kk address", "kk address 2", "kk city", "KA", "94821", "Indecomm")

    # Click on Save
        assetpage.asset_overview_save_click()

    # Assert on Saved text is displayed
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='header']/div[3]").is_displayed(), "Saved text is not displayed")
        assetpage.retuntoappmainpage()


    @attr(priority="high")
    #@SkipTest
    def test_AS_21_To_Verify_That_The_Asset_In_Overview_Panel_Edit_Mode_Is_Cancelled_Successfully(self):
        assetpage = AssetPage(self.driver)

    # Search and Click on Place in the List for EDIT mode
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)

    # Click on Overview panel
        assetpage.get_asset_overview_edit_link.click()

    # Modify the values
        assetpage.set_place_overview_fields("kk address cancel", "kk address 2 cancel", "kk city", "KA", "94821", "Indecomm")

    # Click on Cancel
        assetpage.asset_overview_cancel_click()

    # Assert on Asset name is displayed in the breadcrumb
        self.assertEqual(assetpage.asset_place_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        assetpage.retuntoappmainpage()


    @attr(priority="high")
    #@SkipTest
    def test_AS_23_To_Verify_That_The_Asset_In_Details_Panel_Edit_Mode_Is_Saved_Successfully(self):
        assetpage = AssetPage(self.driver)

    # Search and Click on Place in the List for EDIT mode
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(15)

    # Click on Details panel
        assetpage.get_asset_detail_edit_link.click()

    # Modify the values
        assetpage.set_place_details_fields("1234", "2017-05-16", "Description of School 3","", "ki22ran2.k@indecomm.net", "123-4567-892", "2015-02-23","", "6300", "http://www.haystax.com")
        # pcapacity, pclosed, pdescription, pdistrict, pemail, pfax, popened, pschoolnumber, psize, pwebsite
    # Click on Save
        assetpage.get_asset_detail_edit_save_button.click()
        sleep(10)

    # Assert on Saved text is displayed
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='header']/div[3]").is_displayed(), "Saved text is not displayed")
        assetpage.retuntoappmainpage()

    @attr(priority="high")
    #@SkipTest
    def test_AS_24_To_Verify_The_Validation_Of_Email_Field(self):
        assetpage = AssetPage(self.driver)

    # Search and Click on Place in the List for EDIT mode
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(15)

    # Click on Details panel
        assetpage.get_asset_detail_edit_link.click()
        sleep(10)

    #  Enter the value for Email - Valid

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
    def test_AS_25_To_Verify_The_Validation_Of_Fax_Field(self):
        assetpage = AssetPage(self.driver)

    # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(15)

    # Click on Details panel
        assetpage.get_asset_detail_edit_link.click()
        sleep(10)

    #  Enter the value for FAX

        afax = "123abc1234"
        assetpage.get_asset_detail_edit_detail_fax_text_box.clear()
        sleep(5)
        assetpage.get_asset_detail_edit_detail_fax_text_box.send_keys(afax)
        sleep(5)
        assetpage.get_asset_detail_edit_detail_fax_text_box.send_keys(Keys.TAB)
        sleep(5)
        regex = re.compile(r'^\(?([0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([0-9]{4})$')
        self.assertRegexpMatches(afax, regex, "Expected and actual value is not matching for FAX")
        sleep(5)
        assetpage.get_asset_detail_edit_cancel_button.click()
        assetpage.click_on_asset_link.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_26_To_Verify_That_The_Asset_In_Details_Panel_Edit_Mode_Is_Cancelled_Successfully(self):
        assetpage = AssetPage(self.driver)

    # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(15)

    # Click on Details panel
        assetpage.get_asset_detail_edit_link.click()
        sleep(10)
    # Modify the values
        assetpage.set_place_details_fields("4321", "2020-05-16", "Cancelled", "", "cancel@indecomm.net", "111-111-1111", "2017-02-23", "", "10001", "http://www.haystax.com")
        # pcapacity, pclosed, pdescription, pdistrict, pemail, pfax, popened, pschoolnumber, psize, pwebsite
        sleep(10)
    # Click on Cancel
        assetpage.get_asset_detail_edit_cancel_button.click()
        sleep(10)
    # Assert on Asset name is displayed in the breadcrumb
        self.assertEqual(assetpage.asset_place_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        assetpage.click_on_asset_link.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_27_To_Save_All_Contact_Info_Place_Asset_ContactInfo_Field(self):
        try:
            #Test all manadatory fields.
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            #Select user defined place from the available asset list.
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(6)
            #delete existing contacts.
            assetpage.delete_existing_contact()
            sleep(2)
            #create new contact.
            assetpage.create_new_contact(firstname,lastname)
            act_new_contact_value = assetpage.get_asset_contact_new_contact_value_text.text
            exp_new_contact_value = lastname+", "+firstname+" Title "+"111-111-1111"+" test@test.com"
            assetpage.click_on_asset_link.click()
            self.assertEqual(act_new_contact_value, exp_new_contact_value, "Expected and actual values for new contact are not matching")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 27 has been failed.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_28_To_Test_Main_Contact_Info_Place_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(6)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.create_new_contact(firstname,lastname)
            try:
                if assetpage.get_asset_main_contact_window:
                    act_name_value = assetpage.get_asset_main_contact_name_text.text
                    exp_name_value = "Shri "+firstname+" "+lastname
                    assetpage.click_on_asset_link.click()
                    self.assertEqual(act_name_value,exp_name_value)
            except NoSuchElementException:
                assetpage.click_on_asset_link.click()
                self.assertFalse("No Main Contact exists.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 28 has been failed.")


    @attr(priority="high")
    #@SkipTest
    def test_AS_29_To_Click_On_Save_Without_FirstName_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(8)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(8)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.click()
            assetpage.get_asset_newcontact_prefix_textbox.clear()
            sleep(5)
            firstname_error = assetpage.get_asset_newcontact_firstname_error_message.is_displayed()
            lastname_error = assetpage.get_asset_newcontact_lastname_error_message.is_displayed()
            sleep(3)
            assetpage.get_asset_newcontact_window_cross_button.click()
            assetpage.click_on_asset_link.click()
            sleep(2)
            self.assertTrue(firstname_error, "Error message is not displayed for First Name")
            self.assertTrue(lastname_error, "Error message is not displayed for Last Name")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 29 has been failed.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_30_To_Click_On_Save_With_Phone_Place_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            assetpage.get_asset_newcontact_phone_textbox.clear()
            assetpage.get_asset_newcontact_phone_textbox.send_keys("111-222-3343")
            sleep(2)
            assetpage.get_asset_newcontact_save_button.click()
            sleep(2)
            exp_phone = assetpage.get_asset_contact_phone_value_text.text
            sleep(2)
            assetpage.click_on_asset_link.click()
            regex = re.compile(r'^\(?([A-Za-z0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([A-Za-z0-9]{4})$')
            self.assertRegexpMatches(exp_phone, regex, "Expected and actual phone value are not matching")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 30 has been failed.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_31_1_To_Click_On_Save_With_Email_Place_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            assetpage.get_asset_newcontact_email_textbox.clear()
            assetpage.get_asset_newcontact_email_textbox.send_keys("test@test.com")
            sleep(2)
            assetpage.get_asset_newcontact_save_button.click()
            sleep(2)
            exp_email = assetpage.get_asset_contact_email_value_text.text
            sleep(2)
            assetpage.click_on_asset_link.click()
            regex = re.compile(r'[\w.-]+@[\w.-]+')
            self.assertRegexpMatches(exp_email, regex, "Expected and actual value is not matching for EMAIL")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 31_1 has been failed.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_31_2_To_Click_On_Save_With_Wrong_Email_Place_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            assetpage.get_asset_newcontact_email_textbox.clear()
            assetpage.get_asset_newcontact_email_textbox.send_keys("testtest.com")
            sleep(2)
            assetpage.get_asset_newcontact_firstname_textbox.click()
            sleep(2)
            exp_error_message = assetpage.get_asset_newcontact_email_error_message.is_displayed()
            sleep(2)
            assetpage.get_asset_newcontact_window_cross_button.click()
            assetpage.click_on_asset_link.click()
            self.assertTrue(exp_error_message, "Error message is not displayed for wrong EMAIL address.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 31_2 has been failed.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_32_To_Click_On_Cancel_Place_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstNameDel"
            lastname = "ZLastNameDel"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            sleep(2)
            assetpage.get_asset_newcontact_cancel_button.click()
            try:
                if assetpage.get_asset_contact_first_last_name_value_text.is_displayed():
                    assetpage.click_on_asset_link.click()
                    self.assertFalse("Contact has been created. Cancel button is not working")
            except:
                assetpage.click_on_asset_link.click()
                self.assertTrue("New Contact is not created.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 32 has been failed.")

    @attr(priority="high")
    def test_AS_33_1_To_Name_Ascending_order_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_name_ascending = "stu, def, mno, jkl, ghi, pqr, abc, vwx"
            assetpage.get_asset_point_of_contact_name_tab.click()
            act_name_list = assetpage.get_asset_point_of_contact_name_text_value
            act_name_list_value = []
            for name in act_name_list:
                act_name_list_value.append(name.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_name_ascending, ", ".join(act_name_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 33_1 has been failed.")

    @attr(priority="high")
    def test_AS_33_2_To_Name_Descending_order_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_name_descending = "abc, vwx, ghi, pqr, mno, jkl, stu, def"
            assetpage.get_asset_point_of_contact_name_tab.click()
            sleep(1)
            assetpage.get_asset_point_of_contact_name_tab.click()
            act_name_list = assetpage.get_asset_point_of_contact_name_text_value
            act_name_list_value =[]
            for name in act_name_list:
                act_name_list_value.append(name.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_name_descending, ", ".join(act_name_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 33_2 has been failed.")

    @attr(priority="high")
    def test_AS_33_3_To_Title_Ascending_order_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_title_ascending = "CC, HH, PP, ZZ"
            assetpage.get_asset_point_of_contact_title_tab.click()
            sleep(1)
            act_title_list = assetpage.get_asset_point_of_contact_title_text_value
            act_title_list_value = []
            for title in act_title_list:
                act_title_list_value.append(title.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_title_ascending, ", ".join(act_title_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 33_3 has been failed.")

    @attr(priority="high")
    def test_AS_33_4_To_Title_Descending_order_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_title_descending = "ZZ, PP, HH, CC"
            assetpage.get_asset_point_of_contact_title_tab.click()
            assetpage.get_asset_point_of_contact_title_tab.click()
            act_title_list = assetpage.get_asset_point_of_contact_title_text_value
            act_title_list_value = []
            for title in act_title_list:
                act_title_list_value.append(title.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_title_descending, ", ".join(act_title_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 33_4 has been failed.")

    @attr(priority="high")
    def test_AS_33_5_To_Phone_Ascending_order_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_phone_ascending = "123-444-4444, 222-222-2222, 433-333-3333, 661-111-1111"
            assetpage.get_asset_point_of_contact_phone_tab.click()
            sleep(1)
            act_phone_list = assetpage.get_asset_point_of_contact_phone_text_value
            act_phone_list_value = []
            for phone in act_phone_list:
                act_phone_list_value.append(phone.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_phone_ascending, ", ".join(act_phone_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 33_5 has been failed.")

    @attr(priority="high")
    def test_AS_33_6_To_Phone_Descending_order_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_phone_descending = "661-111-1111, 433-333-3333, 222-222-2222, 123-444-4444"
            assetpage.get_asset_point_of_contact_phone_tab.click()
            sleep(1)
            assetpage.get_asset_point_of_contact_phone_tab.click()
            act_phone_list = assetpage.get_asset_point_of_contact_phone_text_value
            act_phone_list_value = []
            for phone in act_phone_list:
                act_phone_list_value.append(phone.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_phone_descending, ", ".join(act_phone_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 33_6 has been failed.")

    @attr(priority="high")
    def test_AS_33_7_To_Email_Ascending_order_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_email_ascending = "abc@def, ghi@jkl, mno@pqr, stu@vwx"
            assetpage.get_asset_point_of_contact_email_tab.click()
            sleep(1)
            act_email_list = assetpage.get_asset_point_of_contact_email_text_value
            act_email_list_value = []
            for email in act_email_list:
                act_email_list_value.append(email.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_email_ascending, ", ".join(act_email_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 33_7 has been failed.")

    @attr(priority="high")
    def test_AS_33_8_To_Email_Descending_order_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_email_descending = "stu@vwx, mno@pqr, ghi@jkl, abc@def"
            assetpage.get_asset_point_of_contact_email_tab.click()
            sleep(1)
            assetpage.get_asset_point_of_contact_email_tab.click()
            act_email_list = assetpage.get_asset_point_of_contact_email_text_value
            act_email_list_value = []
            for email in act_email_list:
                act_email_list_value.append(email.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_email_descending, ", ".join(act_email_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 33_8 has been failed.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_34_To_Delete_Contact_Place_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            sleep(2)
            assetpage.get_asset_newcontact_save_button.click()
            assetpage.delete_existing_contact()
            try:
                if assetpage.get_asset_newcontact_delete_icon.is_displayed():
                    sleep(2)
                    assetpage.click_on_asset_link.click()
                    self.assertFalse("New Contact is not Deleted")
            except NoSuchElementException:
                assetpage.click_on_asset_link.click()
                self.assertTrue("The Contact has been Deleted")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 34 has been failed.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_35_To_Delete_Cancel_Contact_Place_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            sleep(2)
            assetpage.get_asset_newcontact_save_button.click()
            try:
                if assetpage.get_asset_newcontact_delete_icon.is_displayed():
                    sleep(2)
                    assetpage.get_asset_newcontact_delete_icon.click()
                    sleep(2)
                    assetpage.get_asset_newcontact_delete_popup_cancel_button.click()
                    sleep(2)
                    assetpage.click_on_asset_link.click()
                    self.assertTrue("Pass. Cancel Button is working properly.")
            except NoSuchElementException:
                assetpage.click_on_asset_link.click()
                self.assertFalse("The Contact has been Deleted.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 35 has been failed.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_36_To_Verify_Latitude_and_Longitude_Boundary_Values(self):
        assetpage = AssetPage(self.driver)

        # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)

        # Verify that map is displayed in EDIT mode
        #MapInEditModeDisplayed = self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[1]/div/div[2]/img[1]")
        MapInEditModeDisplayed = self.driver.find_element_by_id("map_control")

        #MapInEditModeDisplayed = assetpage.get_asset_location_map()
        self.assertTrue(MapInEditModeDisplayed.is_displayed(), "Location map not displayed.")
        sleep(5)

        # Click on the Location Edit, to display Latitude and Logitude
        locationEdit = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[4]/div/div[2]/div/img")
        locationEdit.click()
        # assetpage.get_asset_location_edit_icon.click()
        sleep(5)

        # Verify that title is displayed as Asset Location.
        locationTitle = self.driver.find_elements_by_xpath(".//*[@id='H1']")[1].text
        #locationTitle = assetpage.get_asset_location_title.text()
        self.assertEqual("Asset location", locationTitle, "Location Title not displayed")
        sleep(5)

        # Enter the value for Latitude
        lati = "550"
        latitudeValue = self.driver.find_element_by_name("latitude")
        #latitudeValue = assetpage.get_asset_location_latitude_textbox()
        latitudeValue.clear()
        latitudeValue.send_keys(lati)

        # Verify that it displays the error message as - "Latitude must be a number between -90 and 90"
        latitudeerrorMessage = self.driver.find_element_by_xpath(".//*[@id='map_popup']/div[1]/span/small").text
        #latitudeerrorMessage = assetpage.get_asset_location_latitude_error_text.text
        self.assertEqual("Latitude must be a number between -90 and 90", latitudeerrorMessage, "Latitude error message not displayed")

        # Verify that SAVE button is disabled.
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        #locationSave = assetpage.get_asset_location_save_button()
        self.assertFalse(locationSave.is_enabled(), "Location Save button is not disabled")

        # Enter the value for Longitude
        longi = "200"
        longitudeValue = self.driver.find_element_by_name("longitude")
        #longitudeValue = assetpage.get_asset_location_longitude_textbox()
        longitudeValue.clear()
        longitudeValue.send_keys(longi)

        # Verify that it displays the error message as - "Longitude must be a number between -180 and 180"
        longitudeerrorMessage = self.driver.find_element_by_xpath(".//*[@id='map_popup']/div[2]/span/small").text
        #longitudeerrorMessage = assetpage.get_asset_location_longitude_error_text.text
        self.assertEqual("Longitude must be a number between -180 and 180", longitudeerrorMessage, "Longitude error message not displayed")
        sleep(5)

        # Verify that SAVE button is disabled.
        #locationSave = assetpage.get_asset_location_save_button()
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        self.assertFalse(locationSave.is_enabled(), "Location Save button is not disabled")


    @attr(priority="high")
    #@SkipTest
    def test_AS_37_To_Verify_Marker_Is_Displayed_On_The_Map_After_Setting_Latitude_And_Longitude_Values(self):
        assetpage = AssetPage(self.driver)

        # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)

        # Verify that map is displayed in EDIT mode
        #MapInEditModeDisplayed = self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[1]/div/div[2]/img[1]")
        MapInEditModeDisplayed = self.driver.find_element_by_id("map_control")
        self.assertTrue(MapInEditModeDisplayed.is_displayed(), "Location map not displayed.")
        sleep(5)

        # Click on the Location Edit, to display Latitude and Logitude
        locationEdit = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[4]/div/div[2]/div/img")
        locationEdit.click()
        sleep(5)

        # Verify that title is displayed as Asset Location.
        locationTitle = self.driver.find_elements_by_xpath(".//*[@id='H1']")[1].text
        print locationTitle
        self.assertEqual("Asset location", locationTitle, "Location Title not displayed")
        sleep(5)

        # Enter the value for Latitude
        lati = "40.7127"
        latitudeValue = self.driver.find_element_by_name("latitude")
        latitudeValue.clear()
        latitudeValue.send_keys(lati)
        sleep(5)

        # Enter the value for Longitude
        longi = "74.0059"
        longitudeValue = self.driver.find_element_by_name("longitude")
        longitudeValue.clear()
        longitudeValue.send_keys(longi)
        sleep(5)

        # Verify that SAVE button is enabled and Click.
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        self.assertTrue(locationSave.is_enabled(), "Location Save button is not disabled")
        locationSave.click()

        sleep(15)

        # Verify that Marker is available on the Map in Edit page
        markerAvailable =  self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[2]/div[3]/img")
        self.assertTrue(markerAvailable.is_displayed(), "Marker not displayed on Map")
        sleep(5)


    @attr(priority="high")
    #@SkipTest
    def test_AS_38_To_Verify_Place_Name_When_Click_On_Marker(self):
        assetpage = AssetPage(self.driver)

        # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)

        # Verify that map is displayed in EDIT mode
        #MapInEditModeDisplayed = self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[1]/div/div[2]/img[1]")
        MapInEditModeDisplayed = self.driver.find_element_by_id("map_control")
        self.assertTrue(MapInEditModeDisplayed.is_displayed(), "Location map not displayed.")
        sleep(5)

        # Click on the Location Edit, to display Latitude and Logitude
        locationEdit = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[4]/div/div[2]/div/img")
        locationEdit.click()
        sleep(5)

        # Verify that title is displayed as Asset Location.
        locationTitle = self.driver.find_elements_by_xpath(".//*[@id='H1']")[1].text
        print locationTitle
        self.assertEqual("Asset location", locationTitle, "Location Title not displayed")
        sleep(5)

        # Enter the value for Latitude
        lati = "40.7127"
        latitudeValue = self.driver.find_element_by_name("latitude")
        latitudeValue.clear()
        latitudeValue.send_keys(lati)
        sleep(5)

        # Enter the value for Longitude
        longi = "74.0059"
        longitudeValue = self.driver.find_element_by_name("longitude")
        longitudeValue.clear()
        longitudeValue.send_keys(longi)
        sleep(5)

        # Verify that SAVE button is enabled and Click.
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        self.assertTrue(locationSave.is_enabled(), "Location Save button is not disabled")
        locationSave.click()

        sleep(15)

        # Verify that Marker is available on the Map in Edit page
        markerAvailable =  self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[2]/div[3]/img")
        self.assertTrue(markerAvailable.is_displayed(), "Marker not displayed on Map")
        sleep(5)


        # Click on Marker and Verify the text of the place
        markerAvailable.click()
        sleep(5)
        placeText = self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[2]/div[4]/div/div[1]/div/b").text
        print placeText
        self.assertEqual(assetpage.asset_place_name, placeText, "Marker name not displayed.")



    @attr(priority="high")
    def test_AS_40_To_Delete_Upload_Image_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(20)
            assetpage.delete_uploaded_files()
            sleep(2)
            caption_val = "Test_Case_40"
            image_file_name = "Test_Case_40.jpg"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(10)
            number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
            image_count_after_file_upload = len(number_of_image_after_upload)
            sleep(2)
            caption_path = "//div//a[contains(text(),'"+caption_val+"')]//preceding-sibling::img[@class='neutron_document_img']"
            sleep(2)
            image_icon = self.driver.find_element_by_xpath(caption_path)
            Hover = ActionChains(self.driver).move_to_element(image_icon)
            Hover.perform()
            delete_icon = self.driver.find_element_by_xpath(".//img[contains(@src,'delete_icon')]")
            delete_icon.click()
            sleep(2)
            self.driver.find_element_by_xpath("//div[@id='delete_document_modal']//button[contains(text(),'Delete')]").click()
            sleep(10)
            number_of_image_after_delete = assetpage.get_asset_photos_documents_header_text
            image_count_after_file_delete = len(number_of_image_after_delete)
            if (image_count_after_file_upload == image_count_after_file_delete+1):
                try:
                    if (assetpage.get_asset_photos_documents_header_caption_text(caption_val).is_displayed()):
                        assetpage.click_on_asset_link.click()
                        self.assertFalse("Test Case has been failed.")
                except NoSuchElementException:
                    assetpage.click_on_asset_link.click()
                    self.assertTrue("Test Case 40 has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case 40 has been failed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case 40 has been failed.")

    @attr(priority="high")
    def test_AS_41_To_Upload_Image_Cancel_Place_Asset_ContactInfo_Field(self):
        assetpage = AssetPage(self.driver)
        # Search and Click on Place in the List for EDIT mode
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(10)
        assetpage.delete_uploaded_files()
        number_of_image_before_upload = assetpage.get_asset_photos_documents_header_text
        image_count_before_file_upload = len(number_of_image_before_upload)

        # Click on Photo/Document panel - File Upload button
        assetpage.get_asset_photos_documents_upload_file_button.click()
        sleep(2)

        # Click on Attach file button and attached the file path with the send_keys
        file_path = assetpage.file_path("Test_Case_41.jpg")
        assetpage.get_asset_photos_documents_attached_file_button.send_keys(file_path)
        sleep(3)
        # Enter Caption
        caption_val = "Test_Case_41"
        assetpage.get_asset_photos_documents_caption_textbox.send_keys(caption_val)
        sleep(2)
        # Click Cancel.
        assetpage.get_asset_photos_documents_window_cancel_button.click()
        try:
            number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
            image_count_after_file_upload = len(number_of_image_after_upload)
            if (image_count_after_file_upload == image_count_before_file_upload):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case 41 has been passed.")

            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case 41 has been failed")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test case 41 has been failed")

    @attr(priority="high")
    def test_AS_42_To_Upload_Image_With_Caption_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(20)
            assetpage.delete_uploaded_files()

            caption_val = "Test_Case_42"
            image_file_name = "Test_Case_42.jpg"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(5)
            image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
            header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)

            if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed()):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case has been failed. No Caption Displayed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test case 42 has been failed")


    @attr(priority="high")
    def test_AS_43_To_Upload_Image_With_Max_size_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(15)
            assetpage.delete_uploaded_files()

            caption_val = "Test_Case_43"
            image_file_name = "Test_Case_43.jpg"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            try:
                WebDriverWait(self.driver, 140).until(expected_conditions.text_to_be_present_in_element((By.XPATH, assetpage._asset_header_save_text_locator),"415 - UNSUPPORTED MEDIA TYPE"))
            except:
                print "Error is not appeared."
            if assetpage.get_asset_header_save_text.text ==r"415 - UNSUPPORTED MEDIA TYPE":
                assetpage.retuntoappmainpage
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been Failed.")
                assetpage.retuntoappmainpage
                self.assertFalse("Test Case has been failed. No Error message displayed.")
        except:
            assetpage.retuntoappmainpage
            self.assertFalse("Test case 43 has been failed")


    @attr(priority="high")
    def test_AS_44_1_To_Upload_PDF_With_Caption_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(20)
            assetpage.delete_uploaded_files()

            caption_val = "Test_Case_44_1"
            image_file_name = "Test_Case_44_1.pdf"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(20)
            image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
            header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)

            if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed() and (assetpage.get_asset_header_save_text.text == r"Saved")):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case has been failed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test case 44_1 has been failed")

    @attr(priority="high")
    def test_AS_44_2_To_Upload_HTML_With_Caption_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(20)
            assetpage.delete_uploaded_files()

            caption_val = "Test_Case_44_2"
            image_file_name = "Test_Case_44_2.html"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(15)
            image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
            header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)

            if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed() and (assetpage.get_asset_header_save_text.text == r"Saved")):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case has been failed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test case 44_2 has been failed")

    @attr(priority="high")
    def test_AS_44_3_To_Upload_TXT_With_Caption_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(20)
            assetpage.delete_uploaded_files()

            caption_val = "Test_Case_44_3"
            image_file_name = "Test_Case_44_3.txt"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(14)
            image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
            header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)

            if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed() and (assetpage.get_asset_header_save_text.text == r"Saved")):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case has been failed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test case 44_3 has been failed")


    @attr(priority="high")
    def test_AS_45_To_Upload_Images_Count_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(10)
            assetpage.delete_uploaded_files()
            number_of_image_before_upload = assetpage.get_asset_photos_documents_header_text
            image_count_before_file_upload = len(number_of_image_before_upload)

            caption_val = ["Test_Case_45_1", "Test_Case_45_2", "Test_Case_45_3"]
            image_file_name = ["Test_Case_45_1.jpg", "Test_Case_45_2.jpg", "Test_Case_45_3.jpg"]
            for num in range(3):
                assetpage.upload_a_file_with_caption(caption_val[num], image_file_name[num])
                sleep(4)

            sleep(10)
            number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
            image_count_after_file_upload = len(number_of_image_after_upload)


            if (image_count_after_file_upload == image_count_before_file_upload+3):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case has been failed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test case 45 has been failed")

    @attr(priority="high")
    def test_AS_47_To_Upload_Image_Place_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
            sleep(10)
            assetpage.delete_uploaded_files()
            number_of_image_before_upload = assetpage.get_asset_photos_documents_header_text
            image_count_before_file_upload = len(number_of_image_before_upload)

            caption_val = ""
            image_file_name = "Test_Case_47.jpg"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(10)
            number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
            image_count_after_file_upload = len(number_of_image_after_upload)

            header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(image_file_name)
            if (header_caption_text.is_displayed() and (image_count_after_file_upload == image_count_before_file_upload+1)):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been passed")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case has been failed")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test case 47 has been failed")


    @attr(priority="high")
    def test_AS_48_1_To_Annotation_Groups_Text_Place_Asset(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(10)
            exp_text_val = "This is Indecomm Testing. Groups."
            assetpage.delete_all_annotation()
            sleep(2)
            assetpage.get_asset_annotation_plus_image.click()
            assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)
            assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
            assetpage.get_asset_annotation_edit_window_dropdown_groups.click()
            assetpage.get_asset_annotation_edit_window_save_button.click()
            sleep(2)
            text = assetpage.get_asset_annotation_text_value.text
            act_text_val = (text.split('-'))[0].strip()
            assetpage.click_on_asset_link.click()
            self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 48_1 has been failed.")

    @attr(priority="high")
    def test_AS_48_2_To_Annotation_Tenant_Text_Place_Asset(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(10)
            exp_text_val = "This is Indecomm Testing. Tenant."
            assetpage.delete_all_annotation()
            sleep(2)
            assetpage.get_asset_annotation_plus_image.click()
            assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)
            assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
            assetpage.get_asset_annotation_edit_window_dropdown_tenant.click()
            assetpage.get_asset_annotation_edit_window_save_button.click()
            sleep(2)
            text = assetpage.get_asset_annotation_text_value.text
            act_text_val = (text.split('-'))[0].strip()
            assetpage.click_on_asset_link.click()
            self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 48_2 has been failed.")

    @attr(priority="high")
    def test_AS_83_3_To_Annotation_User_Text_Place_Asset(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(10)
            exp_text_val = "This is Indecomm Testing. Groups."
            assetpage.delete_all_annotation()
            sleep(2)
            assetpage.get_asset_annotation_plus_image.click()
            assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)
            assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
            assetpage.get_asset_annotation_edit_window_dropdown_user.click()
            assetpage.get_asset_annotation_edit_window_save_button.click()
            sleep(2)
            text = assetpage.get_asset_annotation_text_value.text
            act_text_val = (text.split('-'))[0].strip()
            assetpage.click_on_asset_link.click()
            self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 48_3 has been failed.")

    @attr(priority="high")
    def test_AS_48_4_To_Annotation_Edit_Text_Place_Asset(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(10)
            exp_text_val = "This is Indecomm Testing. User."
            assetpage.delete_all_annotation()
            sleep(30)
            assetpage.get_asset_annotation_plus_image.click()
            assetpage.get_asset_annotation_edit_window_text_area.send_keys("Random Text Value.")
            assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
            assetpage.get_asset_annotation_edit_window_dropdown_groups.click()
            assetpage.get_asset_annotation_edit_window_save_button.click()
            sleep(2)
            assetpage.get_asset_annotation_edit_image.click()
            assetpage.get_asset_annotation_edit_window_text_area.clear()
            sleep(4)
            assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)
            sleep(4)
            assetpage.get_asset_annotation_edit_window_save_button.click()
            text = assetpage.get_asset_annotation_text_value.text
            act_text_val = (text.split('-'))[0].strip()
            assetpage.click_on_asset_link.click()
            self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 48_4 has been failed.")


    @attr(priotity = "high")
    def test_AS_49_To_Verify_Create_Asset_Function_Create_School_Asset(self):
        assetpage = AssetPage(self.driver)
        assetpage.create_asset("School")
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='header']/div[1]/span[3]/span")))
        self.assertEqual(assetpage.asset_school_name[0], self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        assetpage.click_on_asset_link.click()


    @attr(priority = "high")
    #  @SkipTest
    def test_AS_50_To_Verify_That_Created_SchoolAsset_Displayed_In_The_List(self):
        check = 0
        assetpage = AssetPage(self.driver)
        sleep(2)
        assetpage.asset_search_assetname(assetpage.asset_school_name[0])
        sleep(20)
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[2]"):
            if (i.text  == assetpage.asset_school_name[0]) and (i.value_of_css_property("background-color") == "rgba(255, 236, 158, 1)"):
                check = 1
                #self.assertEqual("rgba(255, 236, 158, 1)", i.value_of_css_property("background-color"))
                break
        assetpage.textbox_clear(self.driver.find_element_by_xpath(assetpage._asset_search_textbox_locator))
        self.assertFalse(check == 0, "Newly created asset is not appaering with yellow background")



    @attr(priority="high")
#    @SkipTest
    def test_AS_51_To_validate_SchoolName_Field(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_create_click()
        assetpage.select_asset_template_type("School")
        self.assertFalse(assetpage.get_asset_overview_save_button.is_enabled())
        assetpage.get_asset_overview_cancel_button.click()
        sleep(5)
        self.assertTrue(self.driver.find_element_by_xpath(assetpage._asset_create_asset).is_displayed())

    @attr(priority="high")
#   @SkipTest
    def test_AS_53_To_validate_GradeandDistrict_Fields(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_create_click()
        assetpage.select_asset_template_type("School")
        assetpage.enter_asset_type_name.send_keys(assetpage.asset_school_name[0])
        assetpage.enter_school_district(assetpage.asset_school_district_grade_validation)
        assetpage.enter_school_grade(assetpage.asset_school_district_grade_validation)
        assetpage.asset_overview_save_click()
        self.assertEqual(assetpage.asset_school_district_grade_validation, assetpage.get_overview_district_text)
        self.assertEqual(assetpage.asset_school_district_grade_validation, assetpage.get_overview_grade_text)


    @attr(priority="high")
    def test_AS_54_To_Verify_Create_Asset_Function_Create_School_Asset_Cancel(self):
        assetpage = AssetPage(self.driver)
        assetpage.create_asset_cancel("School")
        self.assertTrue(self.driver.find_element_by_xpath(assetpage._asset_create_asset).is_displayed())

    @attr(priority="high")
    @SkipTest
    def test_AS_55_To_Verify_SchoolAsset_Edit(self):
        assetpage = AssetPage(self.driver)
        assetpage.edit_asset("School")
        print assetpage.get_overview_address1_text
        self.assertEqual(assetpage.asset_school_name[assetpage.editSchool], assetpage.get_asset_overview_edit_name_text_box)
        self.assertEqual(assetpage.asset_school_district[1], assetpage.get_overview_district_text)
        self.assertEqual(assetpage.asset_school_grade[1], assetpage.get_overview_grade_text)

    @attr(priority="high")
    #@SkipTest
    def test_AS_56_To_Verify_That_The_SchoolAsset_In_Details_Panel_Edit_Mode_Is_Cancelled_Successfully(self):
        assetpage = AssetPage(self.driver)

    # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
        sleep(15)

    # Click on Details panel
        assetpage.get_asset_detail_edit_link.click()

    # Modify the values
        assetpage.set_place_details_fields("1234", "2017-05-16", "Description of School 3","2", "ki22ran2.k@indecomm.net", "123-4567-892", "2015-02-23", "3", "6300", "http://www.haystax.com")
        # pcapacity, pclosed, pdescription, pdistrict, pemail, pfax, popened, pschoolnumber, psize, pwebsite
    # Click on Save
        assetpage.get_asset_detail_edit_cancel_button.click()
        sleep(10)

        self.assertEqual(assetpage.asset_school_name[0], self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        assetpage.click_on_asset_link.click()

    @attr(priority="high")
    #@SkipTest
    def test_AS_58_To_Verify_That_The_SchoolAsset_In_Details_Panel_Edit_Mode_Is_Saved_Successfully(self):
        assetpage = AssetPage(self.driver)

    # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
        sleep(15)

    # Click on Details panel
        assetpage.get_asset_detail_edit_link.click()

    # Modify the values
        assetpage.set_place_details_fields("1234", "2017-05-16", "Description of School 3","2", "ki22ran2.k@indecomm.net", "123-4567-892", "2015-02-23", "3", "6300", "http://www.haystax.com")
        # pcapacity, pclosed, pdescription, pdistrict, pemail, pfax, popened, pschoolnumber, psize, pwebsite
    # Click on Save
        assetpage.get_asset_detail_edit_save_button.click()
        sleep(10)

    # Assert on Saved text is displayed
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='header']/div[3]").is_displayed(), "Saved text is not displayed")
        assetpage.click_on_asset_link.click()

    @attr(priority="high")
    def test_AS_59_1_To_Click_On_Save_With_Email_Asset_Detail_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(8)
            assetpage.get_asset_detail_edit_link.click()
            assetpage.get_asset_detail_edit_email_text_box.clear()
            sleep(2)
            assetpage.get_asset_detail_edit_email_text_box.send_keys("test@test")
            sleep(2)
            assetpage.get_asset_detail_edit_save_button.click()
            sleep(2)
            email = assetpage.get_asset_detail_email_value_text.text
            sleep(2)
            assetpage.click_on_asset_link.click()
            regex = re.compile(r'[\w.-]+@[\w.-]+')
            self.assertRegexpMatches(email, regex, "Expected and actual value is not matching for EMAIL")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 59_1 has been failed.")


    @attr(priority="high")
    def test_AS_59_2_To_Click_On_Save_With_Wrong_Email_Asset_Detail_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(8)
            assetpage.get_asset_detail_edit_link.click()
            assetpage.get_asset_detail_edit_email_text_box.clear()
            sleep(2)
            assetpage.get_asset_detail_edit_email_text_box.send_keys("testtest")
            sleep(2)
            assetpage.get_asset_detail_edit_save_button.click()
            sleep(2)
            state = assetpage.get_asset_detail_edit_save_button.is_enabled()
            assetpage.get_asset_detail_edit_window_cross_button.click()
            assetpage.click_on_asset_link.click()
            sleep(2)
            self.assertFalse(state, "Save Button is enabled even though EMAIL value is wrong")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 59_2 has been failed.")

    @attr(priority="high")
    def test_AS_62_1_To_Click_On_Save_With_FirstLastName_School_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            sleep(2)
            assetpage.get_asset_newcontact_save_button.click()
            sleep(2)
            exp_first_last_name = assetpage.get_asset_contact_first_last_name_value_text.text
            sleep(2)
            regex = re.compile(r'[\w.-@]+\,\s[\w.-@]+')
            assetpage.click_on_asset_link.click()
            self.assertRegexpMatches(exp_first_last_name, regex, "Expected and actual values are not matching for First & Last Name")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 62_1 has been failed.")

    @attr(priority="high")
    def test_AS_62_2_To_Click_On_Save_With_Title_School_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            assetpage.get_asset_newcontact_title_textbox.clear()
            assetpage.get_asset_newcontact_title_textbox.send_keys("Title")
            sleep(2)
            assetpage.get_asset_newcontact_save_button.click()
            sleep(2)
            exp_title = assetpage.get_asset_contact_title_value_text.text
            sleep(2)
            assetpage.click_on_asset_link.click()
            self.assertEqual("Title", exp_title, "Expected and actual value is not matching for Title")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 62_2 has been failed.")

    @attr(priority="high")
    def test_AS_62_3_To_Save_All_Contact_Info_School_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(6)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.create_new_contact(firstname,lastname)
            act_new_contact_value = assetpage.get_asset_contact_new_contact_value_text.text
            exp_new_contact_value = lastname+", "+firstname+" Title "+"111-111-1111"+" test@test.com"
            assetpage.click_on_asset_link.click()
            self.assertEqual(act_new_contact_value, exp_new_contact_value, "Expected and actual values for new contact are not matching")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 62_3 has been failed.")

    @attr(priority="high")
    def test_AS_63_To_Test_Main_Contact_Info_School_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(6)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.create_new_contact(firstname,lastname)
            try:
                if assetpage.get_asset_main_contact_window:
                    act_name_value = assetpage.get_asset_main_contact_name_text.text
                    exp_name_value = "Shri "+firstname+" "+lastname
                    assetpage.click_on_asset_link.click()
                    self.assertEqual(act_name_value,exp_name_value)
            except NoSuchElementException:
                assetpage.click_on_asset_link.click()
                self.assertFalse("No Main Contact exists.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 63 has been failed.")

    @attr(priority="high")
    def test_AS_64_To_Click_On_Save_Without_FirstLastName_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name, "School")
            sleep(8)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(8)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.click()
            assetpage.get_asset_newcontact_prefix_textbox.clear()
            sleep(5)
            firstname_error = assetpage.get_asset_newcontact_firstname_error_message.is_displayed()
            lastname_error = assetpage.get_asset_newcontact_lastname_error_message.is_displayed()
            sleep(3)
            assetpage.get_asset_newcontact_window_cross_button.click()
            assetpage.click_on_asset_link.click()
            sleep(2)
            self.assertTrue(firstname_error, "Error message is not displayed for First Name")
            self.assertTrue(lastname_error, "Error message is not displayed for Last Name")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 64 has been failed.")

    @attr(priority="high")
    def test_AS_65_To_Click_On_Save_With_Phone_School_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            assetpage.get_asset_newcontact_phone_textbox.clear()
            assetpage.get_asset_newcontact_phone_textbox.send_keys("111-222-3343")
            sleep(2)
            assetpage.get_asset_newcontact_save_button.click()
            sleep(2)
            exp_phone = assetpage.get_asset_contact_phone_value_text.text
            sleep(2)
            assetpage.click_on_asset_link.click()
            regex = re.compile(r'^\(?([A-Za-z0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([A-Za-z0-9]{4})$')
            self.assertRegexpMatches(exp_phone, regex, "Expected and actual phone value are not matching")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 65 has been failed.")

    @attr(priority="high")
    def test_AS_66_1_To_Click_On_Save_With_Email_School_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            assetpage.get_asset_newcontact_email_textbox.clear()
            assetpage.get_asset_newcontact_email_textbox.send_keys("test@test.com")
            sleep(2)
            assetpage.get_asset_newcontact_save_button.click()
            sleep(2)
            exp_email = assetpage.get_asset_contact_email_value_text.text
            sleep(2)
            assetpage.click_on_asset_link.click()
            regex = re.compile(r'[\w.-]+@[\w.-]+')
            self.assertRegexpMatches(exp_email, regex, "Expected and actual value is not matching for EMAIL")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 67_1 has been failed.")

    @attr(priority="high")
    def test_AS_66_2_To_Click_On_Save_With_Wrong_Email_School_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            assetpage.get_asset_newcontact_email_textbox.clear()
            assetpage.get_asset_newcontact_email_textbox.send_keys("testtest.com")
            sleep(2)
            assetpage.get_asset_newcontact_firstname_textbox.click()
            sleep(2)
            exp_error_message = assetpage.get_asset_newcontact_email_error_message.is_displayed()
            sleep(2)
            assetpage.get_asset_newcontact_window_cross_button.click()
            assetpage.click_on_asset_link.click()
            self.assertTrue(exp_error_message, "Error message is not displayed for wrong EMAIL address.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 67_2 has been failed.")

    @attr(priority="high")
    def test_AS_67_To_Click_On_Cancel_School_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstNameDel"
            lastname = "ZLastNameDel"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            sleep(2)
            assetpage.get_asset_newcontact_cancel_button.click()
            try:
                if assetpage.get_asset_contact_first_last_name_value_text.is_displayed():
                    assetpage.click_on_asset_link.click()
                    self.assertFalse("Contact has been created. Cancel button is not working")
            except:
                assetpage.click_on_asset_link.click()
                self.assertTrue("New Contact is not created.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 67 has been failed.")

    @attr(priority="high")
    def test_AS_68_1_To_Name_Ascending_order_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_name_ascending = "stu, def, mno, jkl, ghi, pqr, abc, vwx"
            assetpage.get_asset_point_of_contact_name_tab.click()
            act_name_list = assetpage.get_asset_point_of_contact_name_text_value
            act_name_list_value = []
            for name in act_name_list:
                act_name_list_value.append(name.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_name_ascending, ", ".join(act_name_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 68_1 has been failed.")

    @attr(priority="high")
    def test_AS_68_2_To_Name_Descending_order_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_name_descending = "abc, vwx, ghi, pqr, mno, jkl, stu, def"
            assetpage.get_asset_point_of_contact_name_tab.click()
            sleep(1)
            assetpage.get_asset_point_of_contact_name_tab.click()
            act_name_list = assetpage.get_asset_point_of_contact_name_text_value
            act_name_list_value =[]
            for name in act_name_list:
                act_name_list_value.append(name.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_name_descending, ", ".join(act_name_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 68_2 has been failed.")

    @attr(priority="high")
    def test_AS_68_3_To_Title_Ascending_order_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_title_ascending = "CC, HH, PP, ZZ"
            assetpage.get_asset_point_of_contact_title_tab.click()
            sleep(1)
            act_title_list = assetpage.get_asset_point_of_contact_title_text_value
            act_title_list_value = []
            for title in act_title_list:
                act_title_list_value.append(title.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_title_ascending, ", ".join(act_title_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 68_3 has been failed.")

    @attr(priority="high")
    def test_AS_68_4_To_Title_Descending_order_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_title_descending = "ZZ, PP, HH, CC"
            assetpage.get_asset_point_of_contact_title_tab.click()
            assetpage.get_asset_point_of_contact_title_tab.click()
            act_title_list = assetpage.get_asset_point_of_contact_title_text_value
            act_title_list_value = []
            for title in act_title_list:
                act_title_list_value.append(title.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_title_descending, ", ".join(act_title_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 68_4 has been failed.")

    @attr(priority="high")
    def test_AS_68_5_To_Phone_Ascending_order_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_phone_ascending = "123-444-4444, 222-222-2222, 433-333-3333, 661-111-1111"
            assetpage.get_asset_point_of_contact_phone_tab.click()
            sleep(1)
            act_phone_list = assetpage.get_asset_point_of_contact_phone_text_value
            act_phone_list_value = []
            for phone in act_phone_list:
                act_phone_list_value.append(phone.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_phone_ascending, ", ".join(act_phone_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 68_5 has been failed.")

    @attr(priority="high")
    def test_AS_68_6_To_Phone_Descending_order_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_phone_descending = "661-111-1111, 433-333-3333, 222-222-2222, 123-444-4444"
            assetpage.get_asset_point_of_contact_phone_tab.click()
            sleep(1)
            assetpage.get_asset_point_of_contact_phone_tab.click()
            act_phone_list = assetpage.get_asset_point_of_contact_phone_text_value
            act_phone_list_value = []
            for phone in act_phone_list:
                act_phone_list_value.append(phone.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_phone_descending, ", ".join(act_phone_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 68_6 has been failed.")

    @attr(priority="high")
    def test_AS_68_7_To_Email_Ascending_order_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_email_ascending = "abc@def, ghi@jkl, mno@pqr, stu@vwx"
            assetpage.get_asset_point_of_contact_email_tab.click()
            sleep(1)
            act_email_list = assetpage.get_asset_point_of_contact_email_text_value
            act_email_list_value = []
            for email in act_email_list:
                act_email_list_value.append(email.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_email_ascending, ", ".join(act_email_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 68_7 has been failed.")

    @attr(priority="high")
    def test_AS_68_8_To_Email_Descending_order_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(6)
            assetpage.multiple_contact_create()
            sleep(2)
            exp_email_descending = "stu@vwx, mno@pqr, ghi@jkl, abc@def"
            assetpage.get_asset_point_of_contact_email_tab.click()
            sleep(1)
            assetpage.get_asset_point_of_contact_email_tab.click()
            act_email_list = assetpage.get_asset_point_of_contact_email_text_value
            act_email_list_value = []
            for email in act_email_list:
                act_email_list_value.append(email.text)
            assetpage.click_on_asset_link.click()
            self.assertEqual(exp_email_descending, ", ".join(act_email_list_value))
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 68_8 has been failed.")

    @attr(priority="high")
    def test_AS_69_To_Delete_Contact_School_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            sleep(2)
            assetpage.get_asset_newcontact_save_button.click()
            assetpage.delete_existing_contact()
            try:
                if assetpage.get_asset_newcontact_delete_icon.is_displayed():
                    sleep(2)
                    assetpage.click_on_asset_link.click()
                    self.assertFalse("New Contact is not Deleted")
            except NoSuchElementException:
                assetpage.click_on_asset_link.click()
                self.assertTrue("The Contact has been Deleted")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 69 has been failed.")

    @attr(priority="high")
    def test_AS_70_To_Delete_Cancel_Contact_School_Asset_ContactInfo_Field(self):
        try:
            firstname = "FirstName"
            lastname = "ZLastName"
            assetpage = AssetPage(self.driver)
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(8)
            assetpage.delete_existing_contact()
            sleep(2)
            assetpage.get_asset_points_of_contact_header.click()
            assetpage.get_asset_add_contact_button.click()
            sleep(4)
            assetpage.get_asset_newcontact_firstname_textbox.clear()
            assetpage.get_asset_newcontact_firstname_textbox.send_keys(firstname)
            assetpage.get_asset_newcontact_lastname_textbox.clear()
            assetpage.get_asset_newcontact_lastname_textbox.send_keys(lastname)
            sleep(2)
            assetpage.get_asset_newcontact_save_button.click()
            try:
                if assetpage.get_asset_newcontact_delete_icon.is_displayed():
                    sleep(2)
                    assetpage.get_asset_newcontact_delete_icon.click()
                    sleep(2)
                    assetpage.get_asset_newcontact_delete_popup_cancel_button.click()
                    sleep(2)
                    assetpage.click_on_asset_link.click()
                    self.assertTrue("Pass. Cancel Button is working properly.")
            except NoSuchElementException:
                assetpage.click_on_asset_link.click()
                self.assertFalse("The Contact has been Deleted.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 70 has been failed.")

    @attr(priority="high")
    #@SkipTest
    def test_AS_71_To_Verify_Latitude_and_Longitude_Boundary_Values(self):
        assetpage = AssetPage(self.driver)

        # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
        sleep(8)

        # Verify that map is displayed in EDIT mode
        #MapInEditModeDisplayed = self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[1]/div/div[2]/img[1]")
        MapInEditModeDisplayed = self.driver.find_element_by_id("map_control")

        #MapInEditModeDisplayed = assetpage.get_asset_location_map()
        self.assertTrue(MapInEditModeDisplayed.is_displayed(), "Location map not displayed.")
        sleep(5)

        # Click on the Location Edit, to display Latitude and Logitude
        locationEdit = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[4]/div/div[2]/div/img")
        locationEdit.click()
        # assetpage.get_asset_location_edit_icon.click()
        sleep(5)

        # Verify that title is displayed as Asset Location.
        locationTitle = self.driver.find_elements_by_xpath(".//*[@id='H1']")[1].text
        #locationTitle = assetpage.get_asset_location_title.text()
        self.assertEqual("Asset location", locationTitle, "Location Title not displayed")
        sleep(5)

        # Enter the value for Latitude
        lati = "500"
        latitudeValue = self.driver.find_element_by_name("latitude")
        #latitudeValue = assetpage.get_asset_location_latitude_textbox()
        latitudeValue.clear()
        latitudeValue.send_keys(lati)

        # Verify that it displays the error message as - "Latitude must be a number between -90 and 90"
        latitudeerrorMessage = self.driver.find_element_by_xpath(".//*[@id='map_popup']/div[1]/span/small").text
        #latitudeerrorMessage = assetpage.get_asset_location_latitude_error_text.text
        self.assertEqual("Latitude must be a number between -90 and 90", latitudeerrorMessage, "Latitude error message not displayed")

        # Verify that SAVE button is disabled.
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        #locationSave = assetpage.get_asset_location_save_button()
        self.assertFalse(locationSave.is_enabled(), "Location Save button is not disabled")

        # Enter the value for Longitude
        longi = "200"
        longitudeValue = self.driver.find_element_by_name("longitude")
        #longitudeValue = assetpage.get_asset_location_longitude_textbox()
        longitudeValue.clear()
        longitudeValue.send_keys(longi)

        # Verify that it displays the error message as - "Longitude must be a number between -180 and 180"
        longitudeerrorMessage = self.driver.find_element_by_xpath(".//*[@id='map_popup']/div[2]/span/small").text
        #longitudeerrorMessage = assetpage.get_asset_location_longitude_error_text.text
        self.assertEqual("Longitude must be a number between -180 and 180", longitudeerrorMessage, "Longitude error message not displayed")
        sleep(5)

        # Verify that SAVE button is disabled.
        #locationSave = assetpage.get_asset_location_save_button()
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        self.assertFalse(locationSave.is_enabled(), "Location Save button is not disabled")

    @attr(priority="high")
    #@SkipTest
    def test_AS_72_To_Verify_Marker_Is_Displayed_On_The_Map_After_Setting_Latitude_And_Longitude_Values(self):
        assetpage = AssetPage(self.driver)

        # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
        sleep(8)

        # Verify that map is displayed in EDIT mode
        #MapInEditModeDisplayed = self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[1]/div/div[2]/img[1]")
        MapInEditModeDisplayed = self.driver.find_element_by_id("map_control")
        self.assertTrue(MapInEditModeDisplayed.is_displayed(), "Location map not displayed.")
        sleep(5)

        # Click on the Location Edit, to display Latitude and Logitude
        locationEdit = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[4]/div/div[2]/div/img")
        locationEdit.click()
        sleep(5)

        # Verify that title is displayed as Asset Location.
        locationTitle = self.driver.find_elements_by_xpath(".//*[@id='H1']")[1].text
        print locationTitle
        self.assertEqual("Asset location", locationTitle, "Location Title not displayed")
        sleep(5)

        # Enter the value for Latitude
        lati = "40.7127"
        latitudeValue = self.driver.find_element_by_name("latitude")
        latitudeValue.clear()
        latitudeValue.send_keys(lati)
        sleep(5)

        # Enter the value for Longitude
        longi = "74.0059"
        longitudeValue = self.driver.find_element_by_name("longitude")
        longitudeValue.clear()
        longitudeValue.send_keys(longi)
        sleep(5)

        # Verify that SAVE button is enabled and Click.
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        self.assertTrue(locationSave.is_enabled(), "Location Save button is not disabled")
        locationSave.click()

        sleep(15)

        # Verify that Marker is available on the Map in Edit page
        markerAvailable =  self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[2]/div[3]/img")
        self.assertTrue(markerAvailable.is_displayed(), "Marker not displayed on Map")
        sleep(5)


    @attr(priority="high")
    #@SkipTest
    def test_AS_73_To_Verify_Place_Name_When_Click_On_Marker(self):
        assetpage = AssetPage(self.driver)

        # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
        sleep(8)

        # Verify that map is displayed in EDIT mode
        #MapInEditModeDisplayed = self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[1]/div/div[2]/img[1]")
        MapInEditModeDisplayed = self.driver.find_element_by_id("map_control")
        self.assertTrue(MapInEditModeDisplayed.is_displayed(), "Location map not displayed.")
        sleep(5)

        # Click on the Location Edit, to display Latitude and Logitude
        locationEdit = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[4]/div/div[2]/div/img")
        locationEdit.click()
        sleep(5)

        # Verify that title is displayed as Asset Location.
        locationTitle = self.driver.find_elements_by_xpath(".//*[@id='H1']")[1].text
        print locationTitle
        self.assertEqual("Asset location", locationTitle, "Location Title not displayed")
        sleep(5)

        # Enter the value for Latitude
        lati = "40.7127"
        latitudeValue = self.driver.find_element_by_name("latitude")
        latitudeValue.clear()
        latitudeValue.send_keys(lati)
        sleep(5)

        # Enter the value for Longitude
        longi = "74.0059"
        longitudeValue = self.driver.find_element_by_name("longitude")
        longitudeValue.clear()
        longitudeValue.send_keys(longi)
        sleep(5)

        # Verify that SAVE button is enabled and Click.
        locationSave = self.driver.find_element_by_xpath(".//*[@id='location_modal']/div/div/form/div[2]/button[2]")
        self.assertTrue(locationSave.is_enabled(), "Location Save button is not disabled")
        locationSave.click()

        sleep(15)

        # Verify that Marker is available on the Map in Edit page
        markerAvailable =  self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[2]/div[3]/img")
        self.assertTrue(markerAvailable.is_displayed(), "Marker not displayed on Map")
        sleep(5)


        # Click on Marker and Verify the text of the place
        markerAvailable.click()
        sleep(5)
        schoolText = self.driver.find_element_by_xpath(".//*[@id='map_control']/div[1]/div[2]/div[4]/div/div[1]/div/b").text
        self.assertEqual(assetpage.asset_school_name[0], schoolText, "Marker name not displayed.")


    @attr(priority="high")
    def test_AS_75_To_Delete_Upload_Image_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(20)
            assetpage.delete_uploaded_files()
            sleep(2)
            caption_val = "Test_Case_75"
            image_file_name = "Test_Case_75.jpg"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(10)
            number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
            image_count_after_file_upload = len(number_of_image_after_upload)
            sleep(2)
            caption_path = "//div//a[contains(text(),'"+caption_val+"')]//preceding-sibling::img[@class='neutron_document_img']"
            self.driver.find_element_by_xpath(caption_path).click()
            sleep(2)
            delete_icon = self.driver.find_element_by_xpath(".//img[contains(@src,'delete_icon')]")
            delete_icon.click()
            sleep(2)
            self.driver.find_element_by_xpath("//div[@id='delete_document_modal']//button[contains(text(),'Delete')]").click()
            sleep(10)
            number_of_image_after_delete = assetpage.get_asset_photos_documents_header_text
            image_count_after_file_delete = len(number_of_image_after_delete)
            if (image_count_after_file_upload == image_count_after_file_delete+1):
                try:
                    if (assetpage.get_asset_photos_documents_header_caption_text(caption_val).is_displayed()):
                        assetpage.click_on_asset_link.click()
                        self.assertFalse("Test Case has been failed.")
                except NoSuchElementException:
                    assetpage.click_on_asset_link.click()
                    self.assertTrue("Test Case has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case has been failed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 75 has been failed.")

    @attr(priority="high")
    def test_AS_76_To_Upload_Image_Cancel_School_Asset_ContactInfo_Field(self):
        assetpage = AssetPage(self.driver)
        # Search and Click on Place in the List for EDIT mode
        assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
        sleep(10)
        assetpage.delete_uploaded_files()
        number_of_image_before_upload = assetpage.get_asset_photos_documents_header_text
        image_count_before_file_upload = len(number_of_image_before_upload)

        # Click on Photo/Document panel - File Upload button
        assetpage.get_asset_photos_documents_upload_file_button.click()
        sleep(2)

        # Click on Attach file button and attached the file path with the send_keys
        file_path = assetpage.file_path("Test_Case_76.jpg")
        assetpage.get_asset_photos_documents_attached_file_button.send_keys(file_path)
        sleep(3)
        # Enter Caption
        caption_val = "Test_Case_76"
        assetpage.get_asset_photos_documents_caption_textbox.send_keys(caption_val)
        sleep(2)
        # Click Cancel.
        assetpage.get_asset_photos_documents_window_cancel_button.click()
        sleep(2)
        try:
            number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
            image_count_after_file_upload = len(number_of_image_after_upload)
            if (image_count_after_file_upload == image_count_before_file_upload):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case 76 has been passed.")

            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case 76 has been failed")
        except:
            self.assertFalse("Test case 76 has been failed")
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test case has been failed")

    @attr(priority="high")
    def test_AS_77_To_Upload_Image_With_Caption_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(20)
            assetpage.delete_uploaded_files()

            caption_val = "Test_Case_77"
            image_file_name = "Test_Case_77.jpg"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(5)
            image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
            header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)

            if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed()):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case has been failed. No Caption Displayed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 77 has been failed.")

    @attr(priority="high")
    def test_AS_78_To_Upload_Image_With_Max_size_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(15)
            assetpage.delete_uploaded_files()

            caption_val = "Test_Case_78"
            image_file_name = "Test_Case_78.jpg"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            try:
                WebDriverWait(self.driver, 140).until(expected_conditions.text_to_be_present_in_element((By.XPATH, assetpage._asset_header_save_text_locator),"415 - UNSUPPORTED MEDIA TYPE"))
            except:
                print "Error is not appeared."
            if assetpage.get_asset_header_save_text.text ==r"415 - UNSUPPORTED MEDIA TYPE":
                assetpage.retuntoappmainpage
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.retuntoappmainpage
                self.assertFalse("Test Case has been failed. No Error message displayed.")
        except:
            assetpage.retuntoappmainpage
            self.assertFalse("Test Case no 78 has been failed.")

    @attr(priority="high")
    def test_AS_79_1_To_Upload_PDF_With_Caption_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(20)
            assetpage.delete_uploaded_files()

            caption_val = "Test_Case_79_1"
            image_file_name = "Test_Case_79_1.pdf"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(14)
            image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
            header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)

            if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed() and (assetpage.get_asset_header_save_text.text == r"Saved")):
                assetpage.retuntoappmainpage
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.retuntoappmainpage
                self.assertFalse("Test Case has been failed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 79_1 has been failed.")

    @attr(priority="high")
    def test_AS_79_2_To_Upload_HTML_With_Caption_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(20)
            assetpage.delete_uploaded_files()

            caption_val = "Test_Case_79_2"
            image_file_name = "Test_Case_79_2.html"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(14)
            image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
            header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)

            if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed() and (assetpage.get_asset_header_save_text.text == r"Saved")):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case has been failed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 79_2 has been failed.")

    @attr(priority="high")
    def test_AS_79_3_To_Upload_TXT_With_Caption_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(20)
            assetpage.delete_uploaded_files()

            caption_val = "Test_Case_79_3"
            image_file_name = "Test_Case_79_3.txt"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(14)
            image_caption_text = assetpage.get_asset_photos_documents_image_caption_text(caption_val)
            header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(caption_val)

            if (image_caption_text.is_displayed()) and (header_caption_text.is_displayed() and (assetpage.get_asset_header_save_text.text == r"Saved")):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case has been failed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 79_3 has been failed.")


    @attr(priority="high")
    def test_AS_80_To_Upload_Images_Count_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(10)
            assetpage.delete_uploaded_files()
            number_of_image_before_upload = assetpage.get_asset_photos_documents_header_text
            image_count_before_file_upload = len(number_of_image_before_upload)

            caption_val = ["Test_Case_80_1", "Test_Case_80_2", "Test_Case_80_3"]
            image_file_name = ["Test_Case_80_1.jpg", "Test_Case_80_2.jpg", "Test_Case_80_3.jpg"]
            for num in range(3):
                assetpage.upload_a_file_with_caption(caption_val[num], image_file_name[num])

            sleep(10)
            number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
            image_count_after_file_upload = len(number_of_image_after_upload)


            if (image_count_after_file_upload == image_count_before_file_upload+3):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been passed.")
            else:
                assetpage.click_on_asset_link.click()
                self.assertFalse("Test Case has been failed.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 80 has been failed.")

    @attr(priority="high")
    def test_AS_82_To_Upload_Image_School_Asset_ContactInfo_Field(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on Place in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(10)
            assetpage.delete_uploaded_files()
            number_of_image_before_upload = assetpage.get_asset_photos_documents_header_text
            image_count_before_file_upload = len(number_of_image_before_upload)

            caption_val = ""
            image_file_name = "Test_Case_82.jpg"
            assetpage.upload_a_file_with_caption(caption_val, image_file_name)
            sleep(10)
            number_of_image_after_upload = assetpage.get_asset_photos_documents_header_text
            image_count_after_file_upload = len(number_of_image_after_upload)

            header_caption_text = assetpage.get_asset_photos_documents_header_caption_text(image_file_name)
            if (header_caption_text.is_displayed() and (image_count_after_file_upload == image_count_before_file_upload+1)):
                assetpage.click_on_asset_link.click()
                self.assertTrue("Test Case has been passed")
            else:
                assetpage.retuntoappmainpage
                self.assertFalse("Test Case has been failed")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 82 has been failed.")

    @attr(priority="high")
    def test_AS_83_1_To_Annotation_Groups_Text_School_Asset(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on school in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(10)
            exp_text_val = "This is Indecomm Testing. Groups."
            assetpage.delete_all_annotation()
            sleep(2)
            assetpage.get_asset_annotation_plus_image.click()
            assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)
            assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
            assetpage.get_asset_annotation_edit_window_dropdown_groups.click()
            assetpage.get_asset_annotation_edit_window_save_button.click()
            sleep(2)
            text = assetpage.get_asset_annotation_text_value.text
            act_text_val = (text.split('-'))[0].strip()
            assetpage.click_on_asset_link.click()
            self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 83_1 has been failed.")

    @attr(priority="high")
    def test_AS_83_2_To_Annotation_Tenant_Text_School_Asset(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on school in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(10)
            exp_text_val = "This is Indecomm Testing. Tenant."
            assetpage.delete_all_annotation()
            sleep(2)
            assetpage.get_asset_annotation_plus_image.click()
            assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)
            assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
            assetpage.get_asset_annotation_edit_window_dropdown_tenant.click()
            assetpage.get_asset_annotation_edit_window_save_button.click()
            sleep(2)
            text = assetpage.get_asset_annotation_text_value.text
            act_text_val = (text.split('-'))[0].strip()
            assetpage.click_on_asset_link.click()
            self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 83_2 has been failed.")

    @attr(priority="high")
    def test_AS_83_3_To_Annotation_User_Text_School_Asset(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on school in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(10)
            exp_text_val = "This is Indecomm Testing. Groups."
            assetpage.delete_all_annotation()
            sleep(2)
            assetpage.get_asset_annotation_plus_image.click()
            assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)
            assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
            assetpage.get_asset_annotation_edit_window_dropdown_user.click()
            assetpage.get_asset_annotation_edit_window_save_button.click()
            sleep(2)
            text = assetpage.get_asset_annotation_text_value.text
            act_text_val = (text.split('-'))[0].strip()
            assetpage.click_on_asset_link.click()
            self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 83_3 has been failed.")

    @attr(priority="high")
    def test_AS_83_4_To_Annotation_Edit_Text_School_Asset(self):
        try:
            assetpage = AssetPage(self.driver)
            # Search and Click on school in the List for EDIT mode
            assetpage.select_school_or_place_asset(assetpage.asset_school_name[0], "School")
            sleep(10)
            exp_text_val = "This is Indecomm Testing. User."
            assetpage.delete_all_annotation()
            sleep(30)
            assetpage.get_asset_annotation_plus_image.click()
            assetpage.get_asset_annotation_edit_window_text_area.send_keys("Random Text Value.")
            assetpage.get_asset_annotation_edit_window_visibility_dropdown.click()
            assetpage.get_asset_annotation_edit_window_dropdown_groups.click()
            assetpage.get_asset_annotation_edit_window_save_button.click()
            sleep(2)
            assetpage.get_asset_annotation_edit_image.click()
            assetpage.get_asset_annotation_edit_window_text_area.clear()
            sleep(4)
            assetpage.get_asset_annotation_edit_window_text_area.send_keys(exp_text_val)
            sleep(4)
            assetpage.get_asset_annotation_edit_window_save_button.click()
            text = assetpage.get_asset_annotation_text_value.text
            act_text_val = (text.split('-'))[0].strip()
            assetpage.click_on_asset_link.click()
            self.assertEqual(act_text_val,exp_text_val, "The Annotation Texts are not Matching.")
        except:
            assetpage.click_on_asset_link.click()
            self.assertFalse("Test Case no 83_4 has been failed.")


    @attr(priority="high")
    #@SkipTest
    def test_AS_To_Verify_Chart_Is_Displayed(self):
        assetpage = AssetPage(self.driver)
        sleep(5)
        # Click on Chart - Dashboard
        self.driver.find_element_by_xpath("//img[@title='Dashboard']").click()
        sleep(5)
        self.driver.find_element_by_xpath("//img[@title='Dashboard']").click()
        sleep(5)

        # Verify Graph label is displayed - here it should display as Asset Type
        graphLabel = self.driver.find_element_by_class_name("graph_label")
        print graphLabel.text
        self.assertTrue(graphLabel.is_displayed(), "Graph label not displayed")
        sleep(5)

        # Verify Place text is displayed.
        placeText = self.driver.find_element_by_xpath("//*[name()='svg' and namespace-uri()='http://www.w3.org/2000/svg']/*[name()='text'][1]/*[name()='tspan']").text
        print placeText
        self.assertEqual("place", placeText, "place text not displayed")
        sleep(10)


        # Verify School text is displayed.
        schoolText = self.driver.find_element_by_xpath("//*[name()='svg' and namespace-uri()='http://www.w3.org/2000/svg']/*[name()='text'][2]/*[name()='tspan']").text
        print schoolText
        self.assertEqual("school", schoolText, "school text not displayed")
        sleep(5)

        assets = self.driver.find_elements_by_xpath("//*[name()='svg' and namespace-uri()='http://www.w3.org/2000/svg']/*[name()='text']/*[name()='tspan']")
        for asset in assets:
            print asset.text

if __name__ =='__main__':
    unittest.main(verbosity=2)

