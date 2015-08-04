import unittest
from homepage import HomePage
from basetestcase import BaseTestCase
from time import sleep
from nose.plugins.attrib import attr


class MainDriverScript(BaseTestCase):

    @attr(priority="high")
    def test_AS_01_To_Verify_Delete_When_No_Assets_Are_Available(self):
        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()
        sleep(2)
        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        selectAction_dropdown_delete.click()
        print("Nothing to delete")

    @attr(priority="high")
    def test_AS_02_To_Verify_Delete_Deselect_All_Assets(self):
        assets_checkbox = self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[1]/label/span/span[2]")
        for asset_checkbox in assets_checkbox:
            if asset_checkbox.is_selected():
                asset_checkbox.click()

        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()
        sleep(2)
        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        selectAction_dropdown_delete.click()
        print("Nothing to delete")

    @attr(priority="high")
    def test_AS_03_To_Verify_Delete_Asset_Should_Be_Deleted(self):
        asset_checkbox = self.driver.find_element_by_xpath(".//*[@id='assetstable']/tbody/tr[1]/td[1]/label/span/span[2]")
        asset_checkbox.click()

        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()
        sleep(2)
        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        selectAction_dropdown_delete.click()


        delete_button = self.driver.find_element_by_xpath(".//*[@id='delete_asset_modal']/div/div/div[3]/button[2]")
        delete_button.click()


        print("First record deleted successfully.")

    @attr(priority="high")
    def test_AS_04_To_Verify_Delete_Asset_Cancel(self):
        asset_checkbox = self.driver.find_element_by_xpath(".//*[@id='assetstable']/tbody/tr[1]/td[1]/label/span/span[2]")
        asset_checkbox.click()

        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()
        sleep(2)
        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        selectAction_dropdown_delete.click()


        delete_button = self.driver.find_element_by_xpath(".//*[@id='delete_asset_modal']/div/div/div[3]/button[1]")
        delete_button.click()

        print("First record cancelled successfully.")


    @attr(priority="high")
    def test_AS_06_To_Verify_The_Filter_Function_Filter_By_Place(self):
        sleep(10)
        self.driver.find_element_by_xpath("//*[@id='span_filters']/div/div/button[2]").click()
        sleep(10)
        self.driver.find_element_by_link_text("Place").click()
        sleep(10)
        places = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        sleep(10)
        print "Found " + str(len(places)) + " Places Asset Types :"
        for place in places:
            print place.text
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[3]"):
             self.assertEqual (i.text, "Place")

    @attr(priority="high")
    def test_AS_07_To_Verify_The_Filter_Function_Filter_By_School(self):
        self.driver.find_element_by_xpath("//span[@id='span_filters']/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()
        sleep(10)
        schools = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        sleep(10)
        print "Found " + str(len(schools)) + " Schools Asset Types :"
        for school in schools:
            print school.text
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[3]"):
             self.assertEqual (i.text, "School")

    @attr(priority="high")
    def test_AS_11_To_Verify_The_Reset_Filter_Function(self):
        #self.driver.find_element_by_xpath("//span[@id='span_filters']/div/div/button[2]").click()
        #self.driver.find_element_by_link_text("School").click()
        #sleep(10)
        expectedAfterResetFilter = self.driver.find_element_by_xpath("//span[@id='span_filters']/div/div/button[1]").text
        resetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/button")
        resetFilter.click()
        self.assertEqual("Asset Type",expectedAfterResetFilter)


    @attr(priority="high")
    def test_AS_12_To_Verify_The_Search_For_Asset_Function_Search_By_Name(self):
        searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
        searchAsset_textbox.send_keys("k")
        sleep(10)
        searchNames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        sleep(10)
        print "Found " + str(len(searchNames)) + " by Name search."
        for searchName in searchNames:
            print searchName.text

if __name__ =='__main__':
    unittest.main(verbosity=2)
