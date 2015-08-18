import unittest
from pages.assetpage import AssetPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from lib.getFilterData import getFilterData, getSchoolFilterData


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

