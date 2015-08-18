import unittest
from pages.homepage import HomePage
from pages.assetpage import AssetPage
from pages.loginpage import LoginPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from nose.plugins.skip import SkipTest
import json, os

cwd = os.getcwd()
os.chdir('..')
filterasset_filepath = os.path.join(os.getcwd(), "data\json_filterAssets.json")
filterSchoolasset_filepath = os.path.join(os.getcwd(), "data\json_filterSchoolAssets.json")
os.chdir(cwd)

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
        with open(filterasset_filepath) as data_file:
            data_FilterAsset_text = json.load(data_file)

            for each in data_FilterAsset_text:
                filterText = each["Filter_name"]
                assetpage.asset_filter_based_on_place_and_school(filterText)
        self.assertTrue(assetpage.display_place_type_drop_down.is_displayed(), "Invalid filter")

    @attr(priority="high")
    def test_AS_07_To_Verify_The_Filter_Function_Filter_By_School(self):
        assetpage = AssetPage(self.driver)

        print "Filtering data based on Place from Json"
        with open(filterSchoolasset_filepath) as data_file:
            data_FilterSchoolAsset_text = json.load(data_file)

            for each in data_FilterSchoolAsset_text:
                filterText = each["Filter_name"]
                assetpage.asset_filter_based_on_place_and_school(filterText)
            self.assertTrue(assetpage.display_school_district_drop_down.is_displayed(), "Invalid filter")


    @attr(priority="high")
    @SkipTest
    def test_AS_14_To_Verify_Create_Asset_Function_Create_Place_Asset(self):
        assetpage = AssetPage(self.driver)
        assetpage.asset_create()

        expected_schoolname = self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text
        self.driver.find_element_by_link_text("Assets").click()
        # check new place is created - verifying on Breadcrumb
        self.assertEqual(assetpage.Place_name, expected_schoolname )
        # go to search and filter page
        #sleep(20)



if __name__ =='__main__':
    unittest.main(verbosity=2)

