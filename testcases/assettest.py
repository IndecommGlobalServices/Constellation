import unittest
from pages.assetpage import AssetPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from lib.getFilterData import getFilterData, getSchoolFilterData
from time import sleep
import json, os

cwd = os.getcwd()
os.chdir('..')
placeData = os.path.join(os.getcwd(), "data\json_place_asset.json")
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
                pexp_apame = each["exp_apame"]

                sleep(5)
                assetpage.asset_create_click()
                assetpage.select_asset_template_type(passetTemplate)
                sleep(4)
                assetpage.input_asset_fields(papname, papaddress, papaddress1, papcity, papstate,papzip, papowner)
                sleep(5)
                assetpage.asset_save()
                sleep(5)
                expected_placename = pexp_apame

                self.assertEqual(expected_placename, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
                #self.assertEqual(assetpage.asset_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
                self.driver.find_element_by_link_text("Assets").click()

                table = self.driver.find_element_by_css_selector("tbody.pure-table")
                rows = table.find_elements_by_tag_name("tr")
                self.assertIn(expected_placename + ' Place' , [row.text for row in rows])

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

if __name__ =='__main__':
    unittest.main(verbosity=2)

