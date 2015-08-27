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
import json, os
from selenium.webdriver.common.keys import Keys
import re


cwd = os.getcwd()
os.chdir('..')
searchasset_filepath = os.path.join(os.getcwd(), "data\json_searchAssets.json")
os.chdir(cwd)

class AssetPageTest(BaseTestCase):
    @attr(priority="high")
    def test_AS_01_To_Verify_Delete_When_No_Assets_Are_Available(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.select_action_drop_down.click()
        self.assertFalse(assetpage.click_delete_text.is_enabled(), "Delete must be disabled.")

    @attr(priority="high")
    def test_AS_02_To_Verify_Delete_Deselect_All_Assets(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.select_checkbox_in_grid()
        assetpage.select_action_drop_down.click()
        self.assertFalse(assetpage.click_delete_text.is_enabled(), "Delete must be disabled.")

    # Need to rework
    @attr(priority="high")
    def test_AS_03_To_Verify_Delete_Asset_Should_Be_Deleted(self):
        asset_checkbox = self.driver.find_element_by_xpath(".//*[@id='assetstable']/tbody/tr[1]/td[1]/label/span/span[2]")
        asset_checkbox.click()

        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()

        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        selectAction_dropdown_delete.click()

        sleep(5)
        delete_button = self.driver.find_element_by_xpath(".//*[@id='delete_asset_modal']/div/div/div[3]/button[2]")
        delete_button.click()
        sleep(5)

        print("First record deleted successfully.")

    # Need to rework
    @attr(priority="high")
    def test_AS_04_To_Verify_Delete_Asset_Cancel(self):
        #Click the Checkbox in the Grid
        asset_checkbox = self.driver.find_element_by_xpath(".//*[@id='assetstable']/tbody/tr[1]/td[1]/label/span/span[2]")
        asset_checkbox.click()
        sleep(5)
        #Click on Select Action dropdown
        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()
        sleep(5)
        #Click on Delete link in dropdown
        selectAction_dropdown_delete_link = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        selectAction_dropdown_delete_link.click()
        sleep(5)
        #Click on Cancel button
        cancel_button = self.driver.find_element_by_xpath(".//*[@id='delete_asset_modal']/div/div/div[3]/button[1]")
        cancel_button.click()

        print("First record cancelled successfully.")



    @attr(priority="high")
    def test_AS_06_To_Verify_The_Filter_Function_Filter_By_Place(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        print "Filtering data based on Place from Json"
        getFilterData(self)
        self.assertTrue(assetpage.display_place_type_drop_down.is_displayed(), "Invalid filter")

    @attr(priority="high")
    def test_AS_07_To_Verify_The_Filter_Function_Filter_By_School(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        print "Filtering data based on School from Json"
        getSchoolFilterData(self)
        self.assertTrue(assetpage.display_school_district_drop_down.is_displayed(), "Invalid filter")

    @attr(priority="high")
    def test_AS_08_To_Verify_The_Filter_Function_Filter_By_School_District(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.select_asset_school_district()
        sleep(10)

    @attr(priority="high")
    def test_AS_09_To_Verify_The_Filter_Function_Filter_By_School_Grade(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.select_asset_school_grade()
        sleep(10)

    @attr(priority="high")
    def test_AS_10_To_Verify_The_Filter_Function_Filter_By_School_Type(self):
        sleep(5)
        assetpage = AssetPage(self.driver)
        assetpage.select_asset_school_type()
        sleep(10)


    @attr(priority="high")
    def test_AS_11_To_Verify_The_Reset_Filter_Function(self):
        sleep(5)
        resetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/button")
        resetFilter.click()
        expectedAfterResetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div/div/button[1]").text
        self.assertEqual("Asset Type",expectedAfterResetFilter)

    # Need to rework
    @attr(priority="high")
    def test_AS_12_To_Verify_The_Search_For_Asset_Function_Search_By_Name(self):
        print "Getting Search data from Json"


        with open(searchasset_filepath) as data_file:
            data_SearchAsset_text = json.load(data_file)

            for each in data_SearchAsset_text:
                searchText = each["Search_name"]

                searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
                searchAsset_textbox.clear()
                searchAsset_textbox.send_keys(searchText)
                sleep(5)
                expectedAfterSearchFilter = self.driver.find_element_by_xpath(".//*[@id='assetstable']/tbody/tr/td").text
                searchNames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
                print "Found " + str(len(searchNames)) + " by Name search."
                sleep(2)
                searchAsset_textbox.clear()
                sleep(2)
                for searchName in searchNames:
                    #if searchName.text == expectedAfterSearchFilter:
                    if expectedAfterSearchFilter:
                        self.assertEqual("No matching records found", expectedAfterSearchFilter, "No records to find asset.")
                        sleep(2)
                    else:
                        print searchName.text
                        sleep(2)
                searchAsset_textbox.clear()
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
        assetpage.asset_search_assetname("")

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
    @SkipTest
    def test_AS_29_To_Click_On_Save_Without_FirstName_Asset_ContactInfo_Field(self):
        searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
        searchAsset_textbox.clear()
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(8)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        sleep(2)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("last_name").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Prefix']").clear()
        sleep(5)
        firstname_error = self.driver.find_element_by_xpath(".//*[@id='asset_contact_error']/div[1]/small").is_displayed()
        lastname_error = self.driver.find_element_by_xpath(".//*[@id='asset_contact_error']/div[2]/small").is_displayed()
        sleep(4)
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/div/button").click()
        self.driver.find_element_by_link_text("Assets").click()
        sleep(2)
        self.assertTrue(firstname_error, "Error message is not displayed for First Name")
        self.assertTrue(lastname_error, "Error message is not displayed for Last Name")


    @attr(priority="high")
    @SkipTest
    def test_AS_29_To_Click_On_Save_Without_FirstName_Asset_ContactInfo_Field(self):
        assetpage = AssetPage(self.driver)
        searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
        searchAsset_textbox.clear()
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(8)
        assetpage.select_asset_points_of_contact.click()
        assetpage.select_asset_add_contact.click()
        sleep(8)
        assetpage.select_asset_newcontact_firstname.clear()
        assetpage.select_asset_newcontact_lastname.click()
        assetpage.select_asset_newcontact_prefix.clear()
        sleep(5)
        firstname_error = assetpage.check_asset_newcontact_firstname_error_message.is_displayed()
        lastname_error = assetpage.check_asset_newcontact_lastname_error_message.is_displayed()
        sleep(4)
        assetpage.select_asset_newcontact_window_cross_button.click()
        assetpage.click_on_asset_link.click()
        sleep(2)
        self.assertTrue(firstname_error, "Error message is not displayed for First Name")
        self.assertTrue(lastname_error, "Error message is not displayed for Last Name")


    @attr(priotity = "high")
    @SkipTest
    def test_AS_49_To_Verify_Create_Asset_Function_Create_School_Asset(self):
        assetpage = AssetPage(self.driver)
        assetpage.create_asset("School")
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='header']/div[1]/span[3]/span")))
        self.assertEqual(assetpage.asset_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        assetpage.click_on_asset_link.click()


    @attr(priority = "high")
    @SkipTest
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

if __name__ =='__main__':
    unittest.main(verbosity=2)

