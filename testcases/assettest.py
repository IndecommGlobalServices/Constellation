import unittest
from pages.assetpage import AssetPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from lib.getFilterData import getFilterData, getSchoolFilterData
from time import sleep


class AssetPageTest(BaseTestCase):
    @attr(priority="high")
    def test_AS_01_To_Verify_Delete_When_No_Assets_Are_Available(self):
        assetpage = AssetPage(self.driver)
        assetpage.select_action_drop_down.click()
        self.assertFalse(assetpage.click_delete_text.is_enabled(), "Delete must be disabled.")

    @attr(priority="high")
    def test_AS_02_To_Verify_Delete_Deselect_All_Assets(self):
        assetpage = AssetPage(self.driver)
        assetpage.select_checkbox_in_grid()
        assetpage.select_action_drop_down.click()
        self.assertFalse(assetpage.click_delete_text.is_enabled(), "Delete must be disabled.")

    @attr(priority="high")
    def test_AS_06_To_Verify_The_Filter_Function_Filter_By_Place(self):
        assetpage = AssetPage(self.driver)
        print "Filtering data based on Place from Json"
        getFilterData(self)
        self.assertTrue(assetpage.display_place_type_drop_down.is_displayed(), "Invalid filter")

    @attr(priority="high")
    def test_AS_07_To_Verify_The_Filter_Function_Filter_By_School(self):
        assetpage = AssetPage(self.driver)
        print "Filtering data based on School from Json"
        getSchoolFilterData(self)
        self.assertTrue(assetpage.display_school_district_drop_down.is_displayed(), "Invalid filter")

    @attr(priority="high")
    def test_AS_11_To_Verify_The_Reset_Filter_Function(self):
        resetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/button")
        resetFilter.click()
        expectedAfterResetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div/div/button[1]").text
        self.assertEqual("Asset Type",expectedAfterResetFilter)

    @attr(priority="high")
    def test_AS_14_To_Verify_Create_Asset_Function_Create_Place_Asset(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_create()
        assetpage.select_place_asset_template_type()

        assetpage.input_asset_fields()
        assetpage.asset_save()

        expected_placename = "bb"

        self.assertEqual(expected_placename, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        self.driver.find_element_by_link_text("Assets").click()


    @attr(priority="high")
    def test_AS_17_To_Verify_That_Created_Asset_Displayed_In_The_List(self):

        table = self.driver.find_element_by_xpath(".//*[@id='main_content']")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn('bb' + ' Place' , [row.text for row in rows])
        #self.assertEqual("rgba(255, 236, 158, 1)", [row.value_of_css_property("background-color") for row in rows])

    @attr(priority="high")
    def test_AS_18_To_Verify_Create_Asset_Function_Create_Place_Asset(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_create()
        assetpage.select_place_asset_template_type()
        assetpage.input_asset_fields()
        assetpage.asset_cancel()

        expectedAfterResetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div/div/button[1]").text
        self.assertEqual("Asset Type",expectedAfterResetFilter)

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

if __name__ =='__main__':
    unittest.main(verbosity=2)

