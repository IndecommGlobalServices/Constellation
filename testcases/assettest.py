import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.assetpage import AssetPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from lib.getFilterData import getFilterData, getSchoolFilterData
from time import sleep
import json, os, re
from selenium.webdriver.common.keys import Keys
cwd = os.getcwd()
os.chdir('..')
searchasset_filepath = os.path.join(os.getcwd(), "data\json_searchAssets.json")
os.chdir(cwd)



class AssetPageTest(BaseTestCase):

    @attr(priority="high")
    def test_AS_01_To_Verify_Delete_When_No_Assets_Are_Available(self):
        sleep(5)
        AssetPage(self.driver).get_asset_select_action_drop_down.click()
        self.assertTrue(AssetPage(self.driver).get_asset_link_delete_text.is_enabled(), "Delete must be disabled.")

    @attr(priority="high")
    def test_AS_02_To_Verify_Delete_Deselect_All_Assets(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.get_select_checkbox_in_grid()
        assetpage.get_asset_select_action_drop_down.click()
        self.assertTrue(assetpage.get_asset_link_delete_text.is_enabled(), "Delete must be disabled.")

    @attr(priority="high")
    def test_AS_03_To_Verify_Delete_Asset_Should_Be_Deleted(self):
        AssetPage(self.driver).get_asset_list_first_check_box.click()
        AssetPage(self.driver).get_asset_select_action_drop_down.click()
        AssetPage(self.driver).get_asset_link_delete_text.click()
        sleep(5)
        AssetPage(self.driver).get_asset_delete_button.click()
        sleep(5)
        print("Record deleted successfully.")

    @attr(priority="high")
    def test_AS_04_To_Verify_Delete_Asset_Cancel(self):
        AssetPage(self.driver).get_asset_list_first_check_box.click()
        AssetPage(self.driver).get_asset_select_action_drop_down.click()
        AssetPage(self.driver).get_asset_link_delete_text.click()
        sleep(5)
        AssetPage(self.driver).get_asset_cancel_button.click()
        sleep(5)
        print("Record cancelled successfully.")


    @attr(priority="high")
    def test_AS_06_To_Verify_The_Filter_Function_Filter_By_Place(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        print "Filtering data based on Place from Json"
        getFilterData(self)
        self.assertTrue(assetpage.get_asset_place_type_drop_down.is_displayed(), "Invalid filter")

    @attr(priority="high")
    def test_AS_07_To_Verify_The_Filter_Function_Filter_By_School(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        print "Filtering data based on School from Json"
        getSchoolFilterData(self)
        self.assertTrue(assetpage.get_asset_school_district_drop_down.is_displayed(), "Invalid filter")

    @attr(priority="high")
    def test_AS_08_To_Verify_The_Filter_Function_Filter_By_School_District(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.get_asset_school_district()
        sleep(10)

    @attr(priority="high")
    def test_AS_09_To_Verify_The_Filter_Function_Filter_By_School_Grade(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.get_asset_school_grade()
        sleep(10)

    @attr(priority="high")
    def test_AS_10_To_Verify_The_Filter_Function_Filter_By_School_Type(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.get_asset_school_type()
        sleep(10)


    @attr(priority="high")
    def test_AS_11_To_Verify_The_Reset_Filter_Function(self):
        sleep(5)
        AssetPage(self.driver).get_asset_reset_button.click()
        expectedAfterResetFilter = AssetPage(self.driver).get_asset_asset_type_text.text
        self.assertEqual("Asset Type",expectedAfterResetFilter)

    # Need to re-visit
    @attr(priority="high")
    def test_AS_12_To_Verify_The_Search_For_Asset_Function_Search_By_Name(self):

        with open(searchasset_filepath) as data_file:
            data_SearchAsset_text = json.load(data_file)

            for each in data_SearchAsset_text:
                searchText = each["Search_name"]

                AssetPage(self.driver).select_asset_search_text_box.send_keys(searchText)
                sleep(2)
                AssetPage(self.driver).select_asset_search_text_box.send_keys(Keys.CONTROL,"a",Keys.DELETE)
                sleep(5)
                expectedAfterSearchFilter = AssetPage(self.driver).get_asset_list_no_matching_records_found.text
                searchNames = self.driver.find_elements_by_xpath(AssetPage(self.driver)._asset_list_locator)
                print "Found " + str(len(searchNames)) + " by Name search."
                sleep(2)
                for searchName in searchNames:
                    if expectedAfterSearchFilter:
                        self.assertEqual("No matching records found", expectedAfterSearchFilter, "No records to find asset.")
                        sleep(2)
                    else:
                        print searchName.text
                        sleep(2)
                sleep(2)

    @attr(priority="high")
    def test_AS_13_To_Verify_The_Search_For_Asset_Function_Search_By_Special_Characters(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_search_assetname("{}")
        assetpage.asset_search_special_characters()
        sleep(2)
        assetpage.asset_search_assetname("")
        sleep(5)


    @attr(priority="high")
    def test_AS_14_To_Verify_Create_Asset_Function_Create_Place_Asset(self):
        assetpage = AssetPage(self.driver)
        sleep(5)
        assetpage.create_asset("Place")
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='header']/div[1]/span[3]/span")))
        self.assertEqual(assetpage.asset_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        self.driver.find_element_by_link_text("Assets").click()

    @attr(priority="high")
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
            self.assertFalse(assetpage.click_asset_type_save.is_enabled(), "Save button is not disabled.")
        assetpage.asset_cancel()


    @attr(priority="high")
    def test_AS_16_To_Verify_Validation_Of_Phone_Field(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_create_click()
        assetpage.select_asset_template_type("Place")
        sleep(2)

        aphone = "123abc1234"
        assetpage.enter_asset_type_phone.send_keys(aphone)
        #assetpage.enter_asset_type_phone.send_keys(Keys.TAB)

        sleep(5)
        regex = re.compile(r'^\(?([0-9]{3})\)?[-. ]?([A-Za-z0-9]{3})[-. ]?([0-9]{4})$')
        self.assertRegexpMatches(aphone, regex, "Expected and actual value is not matching for EMAIL")
        assetpage.asset_cancel()

    @attr(priority="high")
    def test_AS_17_To_Verify_That_Created_Asset_Displayed_In_The_List(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.create_asset("Place")
        assetpage.click_on_asset_link.click()
        sleep(10)
        assetpage.asset_search_assetname(assetpage.asset_name)
        sleep(20)
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[2]"):
            print (i.text)
            self.assertEqual("rgba(255, 236, 158, 1)", i.value_of_css_property("background-color"))
        #assetpage.asset_search_assetname("")

    @attr(priority="high")
    def test_AS_18_To_Verify_Create_Asset_Function_Cancel_Place_Asset(self):
        assetpage = AssetPage(self.driver)
        sleep(5)
        assetpage.asset_create_click()
        assetpage.asset_cancel()

        expectedAfterResetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div/div/button[1]").text
        self.assertEqual("Asset Type",expectedAfterResetFilter)

    @attr(priority="high")
    def test_AS_19_To_Verify_Create_Asset_Function_Cancel_Place_Asset(self):
        assetpage = AssetPage(self.driver)
        sleep(5)
        assetpage.asset_create_click()
        assetpage.create_place_asset()
        assetpage.asset_cancel()

        expectedAfterResetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div/div/button[1]").text
        self.assertEqual("Asset Type",expectedAfterResetFilter)

    @attr(priority="high")
    def test_AS_20_To_Verify_That_The_Asset_In_Overview_Panel_Edit_Mode_Is_Saved_Successfully(self):
        assetpage = AssetPage(self.driver)

    # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)

    # Click on Overview panel
        assetpage.get_asset_overview_edit_link.click()

    # Modify the values
        assetpage.set_place_overview_fields("kk address", "kk address 2", "kk city", "KA", "94821", "Indecomm")

    # Click on Save
        assetpage.asset_save()

    # Assert on Saved text is displayed
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='header']/div[3]").is_displayed(), "Saved text is not displayed")


    @attr(priority="high")
    def test_AS_21_To_Verify_That_The_Asset_In_Overview_Panel_Edit_Mode_Is_Cancelled_Successfully(self):
        assetpage = AssetPage(self.driver)

    # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)

    # Click on Overview panel
        assetpage.get_asset_overview_edit_link.click()

    # Modify the values
        assetpage.set_place_overview_fields("kk address cancel", "kk address 2 cancel", "kk city", "KA", "94821", "Indecomm")

    # Click on Cancel
        assetpage.asset_cancel()

    # Assert on Asset name is displayed in the breadcrumb
        self.assertEqual(assetpage.asset_place_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)


    @attr(priority="high")
    def test_AS_23_To_Verify_That_The_Asset_In_Details_Panel_Edit_Mode_Is_Saved_Successfully(self):
        assetpage = AssetPage(self.driver)

    # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(15)

    # Click on Details panel
        assetpage.get_asset_detail_edit_link.click()
        sleep(10)

    # Modify the values
        assetpage.set_place_details_fields("1234", "2017-05-16", "Description of School 3", "ki22ran2.k@indecomm.net", "123-4567-892", "2015-02-23", "6300", "http://www.haystax.com")
        sleep(10)
        # pcapacity, pclosed, pdescription, pdistrict, pemail, pfax, popened, pschoolnumber, psize, pwebsite
        # Capacity, Closed, Description, Email, Fax, Opened, Size, Website
    # Click on Save
        assetpage.get_asset_detail_edit_save_button.click()
        sleep(10)
    # Assert on Saved text is displayed
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='header']/div[3]").is_displayed(), "Saved text is not displayed")



    @attr(priority="high")
    def test_AS_29_To_Click_On_Save_Without_FirstName_Asset_ContactInfo_Field(self):
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


    @attr(priotity = "high")
    def test_AS_49_To_Verify_Create_Asset_Function_Create_School_Asset(self):
        assetpage = AssetPage(self.driver)
        assetpage.create_asset("School")
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='header']/div[1]/span[3]/span")))
        self.assertEqual(assetpage.asset_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        assetpage.click_on_asset_link.click()


    @attr(priority = "high")
    #  @SkipTest
    def test_AS_50_To_Verify_That_Created_SchoolAsset_Displayed_In_The_List(self):
        assetpage = AssetPage(self.driver)
        assetpage.create_asset("School")
        assetpage.click_on_asset_link.click()
        assetpage.asset_search_assetname(assetpage.asset_name)
        sleep(20)
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[2]"):
            print (i.text)
            self.assertEqual("rgba(255, 236, 158, 1)", i.value_of_css_property("background-color"))
        assetpage.textbox_clear(self.driver.find_element_by_xpath(assetpage._asset_search_textbox_locator))

    @attr(priority="high")
    def test_AS_59_1_To_Click_On_Save_With_Email_Asset_Detail_Field(self):
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_school_name, "School")
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


    @attr(priority="high")
    def test_AS_59_2_To_Click_On_Save_With_Wrong_Email_Asset_Detail_Field(self):
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_school_name, "School")
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

    @attr(priority="high")
    def test_AS_62_1_To_Click_On_Save_With_FirstLastName_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset("Test1", "School")
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

    @attr(priority="high")
    def test_AS_62_2_To_Click_On_Save_With_Title_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset("Test1", "School")
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

    @attr(priority="high")
    def test_AS_64_To_Click_On_Save_Without_FirstLastName_School_Asset_ContactInfo_Field(self):
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

    @attr(priority="high")
    def test_AS_65_To_Click_On_Save_With_Phone_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset("Test1", "School")
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

    @attr(priority="high")
    def test_AS_66_1_To_Click_On_Save_With_Email_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset("Test1", "School")
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

    @attr(priority="high")
    def test_AS_66_2_To_Click_On_Save_With_Wrong_Email_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset("Test1", "School")
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

    @attr(priority="high")
    def test_AS_67_To_Click_On_Cancel_Asset_ContactInfo_Field(self):
        firstname = "FirstNameDel"
        lastname = "ZLastNameDel"
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset("Test1", "School")
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

    @attr(priority="high")
    @SkipTest
    def test_AS_100_To_Upload_a_document(self):
        assetpage = AssetPage(self.driver)

        # Search and Click on Place in the List for EDIT mode
        assetpage = AssetPage(self.driver)
        assetpage.select_school_or_place_asset(assetpage.asset_place_name, "Place")
        sleep(8)

        # Click on Photo/Document panel - File Upload button
        self.driver.find_element_by_xpath(".//*[@id='widgets']/div[6]/div[1]/div/div[2]/button").click()
        sleep(10)

        # Click on Attach file button and attached the file path with the send_keys
        attachfile = self.driver.find_element_by_xpath(".//*[@id='upload_document_file_upload']")
        #attachfile.click()
        sleep(10)
        #D:\Project\Constellation
        #attachfile.send_keys(os.getcwd()+"/test.txt")
        attachfile.send_keys("D:/Project/Constellation/test.txt")
        #attachfile.send_keys(Keys.ENTER)
        sleep(10)


if __name__ =='__main__':
    unittest.main(verbosity=2)

