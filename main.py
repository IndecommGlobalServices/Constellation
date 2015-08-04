import unittest
from homepage import HomePage
from basetestcase import BaseTestCase
from time import sleep
from nose.plugins.attrib import attr
from selenium.webdriver.common.keys import Keys


class MainDriverScript(BaseTestCase):

    @attr(priority="high")
    def test_AS_01_To_Verify_Delete_When_No_Assets_Are_Available(self):
        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()
        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        self.assertFalse(selectAction_dropdown_delete.is_enabled())

    @attr(priority="high")
    def test_AS_02_To_Verify_Delete_Deselect_All_Assets(self):
        assets_checkbox = self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[1]/label/span/span[2]")
        for asset_checkbox in assets_checkbox:
            if asset_checkbox.is_selected():
                asset_checkbox.click()

        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()
        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        self.assertFalse(selectAction_dropdown_delete.is_enabled())

    '''
    @attr(priority="high")
    def test_AS_03_To_Verify_Delete_Asset_Should_Be_Deleted(self):
        asset_checkbox = self.driver.find_element_by_xpath(".//*[@id='assetstable']/tbody/tr[1]/td[1]/label/span/span[2]")
        asset_checkbox.click()

        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()

        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        selectAction_dropdown_delete.click()


        delete_button = self.driver.find_element_by_xpath(".//*[@id='delete_asset_modal']/div/div/div[3]/button[2]")
        delete_button.click()


        print("First record deleted successfully.")
    '''

    @attr(priority="high")
    def test_AS_04_To_Verify_Delete_Asset_Cancel(self):
        asset_checkbox = self.driver.find_element_by_xpath(".//*[@id='assetstable']/tbody/tr[1]/td[1]/label/span/span[2]")
        asset_checkbox.click()

        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()

        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        selectAction_dropdown_delete.click()

        cancel_button = self.driver.find_element_by_xpath(".//*[@id='delete_asset_modal']/div/div/div[3]/button[1]")
        cancel_button.click()

        print("First record cancelled successfully.")


    @attr(priority="high")
    def test_AS_06_To_Verify_The_Filter_Function_Filter_By_Place(self):
        self.driver.find_element_by_xpath("//*[@id='span_filters']/div/div/button[2]").click()
        self.driver.find_element_by_link_text("Place").click()
        places = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        print "Found " + str(len(places)) + " Places Asset Types :"
        for place in places:
            print place.text
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[3]"):
             self.assertEqual (i.text, "Place")

    @attr(priority="high")
    def test_AS_07_To_Verify_The_Filter_Function_Filter_By_School(self):
        self.driver.find_element_by_xpath("//span[@id='span_filters']/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()
        schools = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        print "Found " + str(len(schools)) + " Schools Asset Types :"
        for school in schools:
            print school.text
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[3]"):
             self.assertEqual (i.text, "School")

    @attr(priority="high")
    def test_AS_11_To_Verify_The_Reset_Filter_Function(self):
        resetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/button")
        resetFilter.click()
        expectedAfterResetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div/div/button[1]").text
        self.assertEqual("Asset Type",expectedAfterResetFilter)


    @attr(priority="high")
    def test_AS_12_To_Verify_The_Search_For_Asset_Function_Search_By_Name(self):
        searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
        searchAsset_textbox.send_keys("k")
        searchNames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        print "Found " + str(len(searchNames)) + " by Name search."
        for searchName in searchNames:
            print searchName.text

    @attr(priority="high")
    def test_AS_14_To_Verify_Create_Asset_Function_Create_Place_Asset(self):

        # Click on Create asset
        clickCreateAsset = self.driver.find_element_by_xpath("//img[@alt='Create asset']")
        clickCreateAsset.click()
        sleep(12)
        # switch to new window
        self.driver.switch_to.active_element

        # Verify title "Asset overview" window
        Create_Asset_Title = self.driver.find_element_by_xpath("//div[@id='asset_overview_modal']/div/div/div/h4").text
        sleep(2)
        self.assertEqual("Asset overview", Create_Asset_Title)

        # Select Place from the dropdown to create new place asset
        self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[1]/div/div/button[2]").click()
        self.driver.find_element_by_link_text("Place").click()
        sleep(10)

        # Verify that all the controls displayed related to Place asset
        # 1. Name, 2. Address, 3. Address2, 4. City, 5. State, 6. Zip, 7. Owner, 8. Phone, 9. Type, 10. Cancel, 11. Save

        place_name = self.driver.find_element_by_xpath("//input[@ng-model='model']")
        place_address = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.address1']")
        place_address2 = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.address2']")
        place_city = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.city']")
        place_state = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.state']")
        place_zip = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.zip']")
        place_owner = self.driver.find_element_by_xpath("//input[@placeholder='Owner']")
        place_phone = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/div[3]/input")
        place_type = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/button[2]")
        place_cancel = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[1]")
        place_save = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[2]")

        # check all fields are enabled
        self.assertTrue(place_name.is_enabled()
                        and place_address.is_enabled()
                        and place_address2.is_enabled()
                        and place_city.is_enabled()
                        and place_state.is_enabled()
                        and place_zip.is_enabled()
                        and place_owner.is_enabled()
                        and place_phone.is_enabled()
                        and place_type.is_enabled()
                        and place_cancel.is_enabled()
                        and place_save.is_enabled())

        # fill out the fields
        place_name.send_keys("kk place automation test")
        place_name.send_keys(Keys.TAB)
        sleep(2)
        place_address.send_keys("indecomm")
        place_address.send_keys(Keys.TAB)
        sleep(2)
        place_address2.send_keys("MG Road")
        place_address2.send_keys(Keys.TAB)
        sleep(2)
        place_city.send_keys("Bangalore")
        place_city.send_keys(Keys.TAB)
        sleep(2)
        place_state.send_keys("KA")
        place_state.send_keys(Keys.TAB)
        sleep(2)
        place_zip.send_keys("56009")
        place_zip.send_keys(Keys.TAB)
        sleep(2)
        place_phone.send_keys("994-550-8652")
        place_phone.send_keys(Keys.TAB)
        sleep(2)
        place_owner.send_keys("indecomm")
        place_owner.send_keys(Keys.TAB)
        sleep(2)
        # Type selection
        place_type.click()
        self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[2]/a").click()
        sleep(2)
        # Click SAVE button to save the form
        place_save.click()
        sleep(5)
        # check new place is created - verifying on Breadcrumb
        self.assertEqual("kk place automation test", self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        # go to search and filter page
        self.driver.find_element_by_link_text("Assets").click()

if __name__ =='__main__':
    unittest.main(verbosity=2)
