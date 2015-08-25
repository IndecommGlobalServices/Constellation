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
    def test_AS_11_To_Verify_The_Reset_Filter_Function(self):
        sleep(5)
        resetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/button")
        resetFilter.click()
        expectedAfterResetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div/div/button[1]").text
        self.assertEqual("Asset Type",expectedAfterResetFilter)

    @attr(priority="high")
    def test_AS_14_To_Verify_Create_Asset_Function_Create_Place_Asset(self):
        assetpage = AssetPage(self.driver)
        sleep(5)

        assetpage.create_asset("Place")
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='header']/div[1]/span[3]/span")))
        self.assertEqual(assetpage.asset_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        self.driver.find_element_by_link_text("Assets").click()

    @attr(priority="high")
    def test_AS_17_To_Verify_That_Created_Asset_Displayed_In_The_List(self):
        sleep(5)
        with open(placeData) as data_file:
            data_text = json.load(data_file)
            for each in data_text:
                pexp_apame = each["exp_apame"]

        table = self.driver.find_element_by_xpath(".//*[@id='main_content']")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(pexp_apame + ' Place' , [row.text for row in rows])
        #self.assertEqual("rgba(255, 236, 158, 1)", [row.value_of_css_property("background-color") for row in rows])


    @attr(priority="high")
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
    def test_AS_18_To_Verify_Create_Asset_Function_Create_Place_Asset(self):
        assetpage = AssetPage(self.driver)
        sleep(5)
        with open(placeData) as data_file:
            data_text = json.load(data_file)

            for each in data_text:
                passetTemplate = each["assetTemplate"]
                papname = each["apname"]
                papaddress = each["apaddress"]
                papaddress1 = each["apaddress1"]
                papcity=each["apcity"]
                papstate=each["apstate"]
                papzip=each["apzip"]
                papowner=each["apowner"]

                assetpage.asset_create_click()
                assetpage.select_asset_template_type(passetTemplate)
                sleep(4)

                assetpage.input_asset_fields(papname, papaddress, papaddress1, papcity, papstate,papzip, papowner)
                assetpage.asset_cancel()

                expectedAfterResetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div/div/button[1]").text
                self.assertEqual("Asset Type",expectedAfterResetFilter)
       

    @attr(priority="high")
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
    def test_AS_49_To_Verify_Create_Asset_Function_Create_School_Asset(self):
        assetpage = AssetPage(self.driver)
        assetpage.create_asset("School")
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@id='header']/div[1]/span[3]/span")))
        self.assertEqual(assetpage.asset_school_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        assetpage.click_on_asset_link.click()



    @attr(priority = "high")
    #  @SkipTest
    def test_AS_50_To_Verify_That_Created_SchoolAsset_Displayed_In_The_List(self):
        assetpage = AssetPage(self.driver)
        assetpage.create_asset("School")
        assetpage.click_on_asset_link.click()
        assetpage.asset_search_assetname(assetpage.asset_school_name)
        sleep(2)
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[2]"):
            print (i.text)
            self.assertEqual("rgba(255, 236, 158, 1)", i.value_of_css_property("background-color"))
        assetpage.textbox_clear(self.driver.find_element_by_xpath(assetpage._asset_search_textbox_locator))

if __name__ =='__main__':
    unittest.main(verbosity=2)

