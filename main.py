import unittest
from time import sleep

from nose.plugins.attrib import attr
from selenium.webdriver.common.keys import Keys
from faker import Factory

from testcases.basetestcase import BaseTestCase
import json, os, re

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from nose.plugins.skip import SkipTest
from pages.assetpage import AssetPage

cwd = os.getcwd()
os.chdir('..')
searchasset_filepath = os.path.join(os.getcwd(), "data\jjson_searchAssets.json")
os.chdir(cwd)


class MainDriverScript(BaseTestCase):

    fake = Factory.create()
    #Place_name = fake.company()
    #School_name = fake.name()

    @attr(priority="high")
    def test_AS_01_To_Verify_Delete_When_No_Assets_Are_Available(self):
        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()
        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        self.assertFalse(selectAction_dropdown_delete.is_enabled(), "Delete must be disabled.")

    @attr(priority="high")
    def test_AS_02_To_Verify_Delete_Deselect_All_Assets(self):
        assets_checkbox = self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[1]/label/span/span[2]")
        for asset_checkbox in assets_checkbox:
            if asset_checkbox.is_selected():
                asset_checkbox.click()

        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()
        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        self.assertFalse(selectAction_dropdown_delete.is_enabled(), "Delete must be disabled.")


    @attr(priority="high")
    @SkipTest
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
 #   @SkipTest
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

        '''
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
        '''

        fake = Factory.create()
        # fill out the fields
        #place_name.send_keys(self.Place_name)
        place_name.send_keys("kk place automation test")
        place_name.send_keys(Keys.TAB)
        sleep(2)

        # switch to the alert
        #alert = self.driver.switch_to().alert

        # get the text from alert
        #alert_text = alert.text

        # check alert text
        #self.assertEqual("Would you like to share your location with constellation-dev.haystax.com?", alert_text)

        # click on close button
        #alert.dismiss()

        place_address.send_keys(fake.address())
        #place_address.send_keys("indecomm")
        place_address.send_keys(Keys.TAB)
        sleep(2)
        place_address2.send_keys(fake.secondary_address())
        #place_address2.send_keys("MG Road")
        place_address2.send_keys(Keys.TAB)
        sleep(2)
        #place_city.send_keys("Bangalore")
        place_city.send_keys(fake.city())
        place_city.send_keys(Keys.TAB)
        sleep(2)
        #place_state.send_keys("KA")
        place_state.send_keys(fake.state_abbr())
        place_state.send_keys(Keys.TAB)
        sleep(2)
        #place_zip.send_keys("56009")
        place_zip.send_keys(fake.zipcode())
        place_zip.send_keys(Keys.TAB)
        sleep(2)
        #place_phone.send_keys("994-550-8652")
        place_phone.send_keys(fake.phone_number())
        place_phone.send_keys(Keys.TAB)
        sleep(2)
        #place_owner.send_keys("indecomm")
        place_owner.send_keys(fake.domain_name())
        place_owner.send_keys(Keys.TAB)
        sleep(2)
        # Type selection
        place_type.click()
        self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[2]/a").click()
        sleep(2)
        # Click SAVE button to save the form
        place_save.click()
        sleep(20)
        expected_placename = self.driver.find_element_by_xpath(".//*[@id='header']/div[1]/span[3]/span").text
        self.driver.find_element_by_link_text("Assets").click()
        # check new place is created - verifying on Breadcrumb
        # self.assertEqual(self.Place_name, expected_placename )
        self.assertEqual("kk place automation test", expected_placename )
        # go to search and filter page
        sleep(20)

    @attr(priority="high")
    @SkipTest
    def test_AS_17_To_Verify_That_Created_Asset_Displayed_In_The_List(self):
        searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
        searchAsset_textbox.clear()
        searchAsset_textbox.send_keys(self.Place_name)
        sleep(10)
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[2]"):
            print (i.text)
            self.assertEqual("rgba(255, 236, 158, 1)", i.value_of_css_property("background-color"))
        searchAsset_textbox.clear()


    @attr(priority="high")
    def test_AS_29_To_Click_On_Save_Without_FirstName_Asset_ContactInfo_Field(self):
        searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
        searchAsset_textbox.clear()
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[2]").click()
        self.driver.find_element_by_name("last_name").click()
        state = self.driver.find_element_by_xpath(".//*[@id='asset_contact_error']/div[1]/small").is_displayed()
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/div/button").click()
        self.driver.find_element_by_link_text("Assets").click()
        sleep(2)
        self.assertTrue(state)

    @attr(priority="high")
    def test_AS_30_To_Click_On_Save_Without_LastName_Asset_ContactInfo_Field(self):
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        self.driver.find_element_by_name("first_name").send_keys("Firtst Name")
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[2]").click()
        self.driver.find_element_by_name("first_name").click()
        state =(self.driver.find_element_by_xpath(".//*[@id='asset_contact_error']/div[2]/small").is_displayed())
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/div/button").click()
        self.driver.find_element_by_link_text("Assets").click()
        sleep(2)
        self.assertTrue(state)


    @attr(priority="high")
    def test_AS_31_To_Click_On_Save_With_Email_Asset_Detail_Field(self):
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(5)
        self.driver.find_element_by_xpath(".//div[contains(text(),'Details')]/div/img").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Email']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("test@test")
        sleep(4)
        self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[2]/button[2]").click()
        sleep(4)
        email = (self.driver.find_element_by_xpath(".//span[text()='Email']/../following-sibling::td").text)
        sleep(2)
        self.driver.find_element_by_link_text("Assets").click()
        regex = re.compile(r'[\w.-]+@[\w.-]+')
        self.assertRegexpMatches(email, regex)


    @attr(priority="high")
    def test_AS_32_To_Click_On_Save_With_Wrong_Email_Asset_Detail_Field(self):
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(5)
        self.driver.find_element_by_xpath(".//div[contains(text(),'Details')]/div/img").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Email']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("testtest")
        self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[2]/button[2]").click()
        state =(self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[2]/button[2]").is_enabled())
        self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/div/button").click()
        self.driver.find_element_by_link_text("Assets").click()
        sleep(2)
        self.assertFalse(state)


    @attr(priority="high")
    def test_AS_33_To_Click_On_Save_With_FirstName_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        try:
            if self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").is_displayed():
                self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").click()
                self.driver.find_element_by_xpath(".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]").click()
        except NoSuchElementException:
            print "No contact"
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        sleep(4)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("first_name").send_keys(firstname)
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_name("last_name").send_keys(lastname)
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[2]").click()
        exp_firstname = self.driver.find_element_by_xpath("(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])[1]").text
        print exp_firstname
        self.driver.find_element_by_link_text("Assets").click()
        regex = re.compile(r'[\w.-@]+\,\s[\w.-@]+')
        self.assertRegexpMatches(exp_firstname, regex)

    @attr(priority="high")
    def test_AS_34_To_Click_On_Save_With_Title_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        try:
            if self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").is_displayed():
                self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").click()
                self.driver.find_element_by_xpath(".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]").click()
        except NoSuchElementException:
            print "No contact"
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        sleep(4)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("first_name").send_keys(firstname)
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_name("last_name").send_keys(lastname)
        self.driver.find_element_by_xpath("//input[@placeholder='Prefix']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Prefix']").send_keys("Prefix")
        self.driver.find_element_by_xpath("//input[@placeholder='Title']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Title']").send_keys("Title")
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[2]").click()
        title = self.driver.find_element_by_xpath("(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])[1]/../following-sibling::td[1]").text
        self.driver.find_element_by_link_text("Assets").click()
        self.assertTrue("Title", title)

    @attr(priority="high")
    def test_AS_35_To_Click_On_Save_With_Phone_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        try:
            if self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").is_displayed():
                self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").click()
                self.driver.find_element_by_xpath(".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]").click()
        except NoSuchElementException:
            print "No contact"
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        sleep(4)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("first_name").send_keys(firstname)
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_name("last_name").send_keys(lastname)
        self.driver.find_element_by_name("phone").clear()
        self.driver.find_element_by_name("phone").send_keys("111-222-9999")
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[2]").click()
        phone = self.driver.find_element_by_xpath("(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])[1]/../following-sibling::td[2]").text
        self.driver.find_element_by_link_text("Assets").click()

    @attr(priority="high")
    def test_AS_36_To_Click_On_Save_With_Email_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        try:
            if self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").is_displayed():
                self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").click()
                self.driver.find_element_by_xpath(".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]").click()
        except NoSuchElementException:
            print "No contact"
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        sleep(4)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("first_name").send_keys(firstname)
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_name("last_name").send_keys(lastname)
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys("text@text")
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[2]").click()
        email = self.driver.find_element_by_xpath("(//table[@id='contacts_table']//tbody//tr/td//a[@class='showaslink showaslink-edit'])[1]/../following-sibling::td[3]").text
        self.driver.find_element_by_link_text("Assets").click()
        regex = re.compile(r'[\w.-]+@[\w.-]+')
        self.assertRegexpMatches(email, regex)

    @attr(priority="high")
    #@SkipTest
    def test_AS_37_To_Click_On_Save_With_Wrong_Email_Asset_ContactInfo_Field(self):
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        try:
            if self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").is_displayed():
                self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").click()
                self.driver.find_element_by_xpath(".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]").click()
        except NoSuchElementException:
            print "No contact"
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        sleep(2)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("first_name").send_keys("Test")
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_name("last_name").send_keys("Test1")
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys("texttext.com")
        sleep(2)
        self.driver.find_element_by_name("last_name").click()
        state =(self.driver.find_element_by_xpath("//*[@id='asset_contact_error']/div[6]//small").is_displayed())
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/div/button").click()
        self.driver.find_element_by_link_text("Assets").click()
        self.assertTrue(state)

    @attr(priority="high")
    #SkipTest
    def test_AS_38_To_Delete_Contact_Asset_ContactInfo_Field(self):
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        sleep(4)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("first_name").send_keys("Test")
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_name("last_name").send_keys("Test1")
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[2]").click()
        self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").click()
        self.driver.find_element_by_xpath(".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]").click()
        sleep(2)
        try:
            self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").is_displayed()
            self.driver.find_element_by_link_text("Assets").click()
            self.assertFalse("Fail")
        except NoSuchElementException:
            self.driver.find_element_by_link_text("Assets").click()
            self.assertTrue("Pass")

    @attr(priority="high")
    def test_AS_39_To_Click_On_Save_Address_Asset_ContactInfo_Field(self):
        address_1 = r"635 Lubowitz Lights Apt. 404"
        address_2 = r"Suite 950"
        city = r"North Estiefurt"
        state = "AB"
        zip_code = "12345"
        exp_city = city+", "+state+"  "+zip_code
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        try:
            if self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").is_displayed():
                self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").click()
                self.driver.find_element_by_xpath(".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]").click()
        except NoSuchElementException:
            print "No contact"
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        sleep(4)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("first_name").send_keys("firstname")
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_name("last_name").send_keys("lastname")
        self.driver.find_element_by_name("address").clear()
        self.driver.find_element_by_name("address").send_keys(address_1)
        self.driver.find_element_by_xpath("*//input[@ng-model='contact_edit.address.address2']").clear()
        self.driver.find_element_by_xpath("*//input[@ng-model='contact_edit.address.address2']").send_keys(address_2)
        self.driver.find_element_by_xpath("*//input[@placeholder='City']").clear()
        self.driver.find_element_by_xpath("*//input[@placeholder='City']").send_keys(city)
        self.driver.find_element_by_name("state").clear()
        self.driver.find_element_by_name("state").send_keys(state)
        self.driver.find_element_by_name("zip").clear()
        self.driver.find_element_by_name("zip").send_keys(zip_code)
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[2]").click()
        sleep(2)
        act_address_1 = self.driver.find_element_by_xpath("//tr[@ng-if='main_contact.address.address1']//td[contains(@class, 'tableitemvalue ng-binding')]").text
        act_address_2 = self.driver.find_element_by_xpath("//tr[@ng-if='main_contact.address.address2']//td[contains(@class,'tableitemvalue ng-binding')]").text
        act_city =  self.driver.find_element_by_xpath("//tr[@ng-if='main_contact.address.state']//td[contains(@class,'tableitemvalue ng-binding')]").text
        self.driver.find_element_by_link_text("Assets").click()
        self.assertEqual(address_1, act_address_1)
        self.assertEqual (address_2, act_address_2)
        self.assertEqual(exp_city, act_city)
        sleep(2)

    @attr(priority="high")
    def test_AS_40_To_Click_On_Save_Wrong_State_Asset_ContactInfo_Field(self):
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        try:
            if self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").is_displayed():
                self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").click()
                self.driver.find_element_by_xpath(".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]").click()
        except NoSuchElementException:
            print "No contact"
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        sleep(4)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("first_name").send_keys("firstname")
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_name("last_name").send_keys("lastname")
        self.driver.find_element_by_name("state").clear()
        self.driver.find_element_by_name("state").send_keys("ABC")
        self.driver.find_element_by_name("zip").click()
        state =(self.driver.find_element_by_xpath("//*[@id='asset_contact_error']/div[3]/small").is_displayed())
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/div/button").click()
        self.driver.find_element_by_link_text("Assets").click()
        sleep(2)
        self.assertTrue(state)

    @attr(priority="high")
    def test_AS_41_To_Click_On_Save_Wrong_Zip_1_Asset_ContactInfo_Field(self):
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        try:
            if self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").is_displayed():
                self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").click()
                self.driver.find_element_by_xpath(".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]").click()
        except NoSuchElementException:
            print "No contact"
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        sleep(4)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("first_name").send_keys("firstname")
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_name("last_name").send_keys("lastname")
        self.driver.find_element_by_name("zip").clear()
        self.driver.find_element_by_name("zip").send_keys("AAAAA")
        self.driver.find_element_by_name("state").click()
        state =(self.driver.find_element_by_xpath("//*[@id='asset_contact_error']/div[4]/small").is_displayed())
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/div/button").click()
        self.driver.find_element_by_link_text("Assets").click()
        sleep(2)
        self.assertTrue(state)

    @attr(priority="high")
    def test_AS_42_To_Click_On_Save_Wrong_Zip_2_Asset_ContactInfo_Field(self):
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(2)
        try:
            if self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").is_displayed():
                self.driver.find_element_by_xpath(".//*[@id='contacts_table']/tbody/tr/td[5]/a/img").click()
                self.driver.find_element_by_xpath(".//*[@id='asset_delete_contact_modal']/div/div/div[3]/button[2]").click()
        except NoSuchElementException:
            print "No contact"
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        sleep(4)
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_name("first_name").send_keys("firstname")
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_name("last_name").send_keys("lastname")
        self.driver.find_element_by_name("zip").clear()
        self.driver.find_element_by_name("zip").send_keys(123456)
        self.driver.find_element_by_name("state").click()
        state =(self.driver.find_element_by_xpath("//*[@id='asset_contact_error']/div[4]/small").is_displayed())
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/div/button").click()
        self.driver.find_element_by_link_text("Assets").click()
        sleep(2)
        self.assertTrue(state)

    @attr(priority="high")
#    @SkipTest
    def test_AS_49_To_Verify_Create_Asset_Function_Create_School_Asset(self):

        sleep(10)
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
        self.driver.find_element_by_link_text("School").click()
        sleep(10)

        # Verify that all the controls displayed related to Place asset
        # 1. Name, 2. Address, 3. Address2, 4. City, 5. State, 6. Zip, 7. Owner, 8. Phone, 9. Type, 10. Cancel, 11. Save

        school_name = self.driver.find_element_by_xpath("//input[@ng-model='model']")
        school_address = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.address1']")
        school_address2 = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.address2']")
        school_city = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.city']")
        school_state = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.state']")
        school_zip = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.zip']")
        school_owner = self.driver.find_element_by_xpath("//input[@placeholder='Owner']")
        school_phone = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/div[3]/input")
        school_district = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/button[1]")
        school_grade = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/button[1]")
        school_type = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/button[2]")
        school_cancel = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[1]")
        school_save = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[2]")

        # check all fields are enabled
        self.assertTrue(school_name.is_enabled()
                        and school_address.is_enabled()
                        and school_address2.is_enabled()
                        and school_city.is_enabled()
                        and school_state.is_enabled()
                        and school_zip.is_enabled()
                        and school_owner.is_enabled()
                        and school_phone.is_enabled()
                        and school_type.is_enabled()
                        and school_cancel.is_enabled()
                        and school_save.is_enabled())

        # fill out the fields
        school_name.send_keys("kk school automation test")
        #school_name.send_keys(self.School_name)
        school_name.send_keys(Keys.TAB)
        sleep(2)
        school_address.send_keys("indecomm")
        school_address.send_keys(Keys.TAB)
        sleep(2)
        school_address2.send_keys("MG Road")
        school_address2.send_keys(Keys.TAB)
        sleep(2)
        school_city.send_keys("Bangalore")
        school_city.send_keys(Keys.TAB)
        sleep(2)
        school_state.send_keys("KA")
        school_state.send_keys(Keys.TAB)
        sleep(2)
        school_zip.send_keys("56009")
        school_zip.send_keys(Keys.TAB)
        sleep(2)
        school_phone.send_keys("994-550-8652")
        school_phone.send_keys(Keys.TAB)
        sleep(2)
        #school_district.click()
        #self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li[1]/a").click()
        #sleep(2)
        #school_grade.click()
        #self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[1]/a").click()
        #sleep(2)

        school_district.click()
        sleep(2)
        try:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li[1]/a").click()
        except:
            school_newdistrict = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li/input")
            school_newdistrict.click()
            school_newdistrict.send_keys("new")
            school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
            self.assertTrue(school_add.is_enabled())
            school_add.click()
        sleep(2)

        school_grade.click()
        sleep(2)
        try:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[1]/a").click()
        except:
            school_newgrade = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li/input")
            school_newgrade.click()
            school_newgrade.send_keys("new")
            school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
            try:
                self.assertTrue(school_add.is_displayed())
            except:
                print("Add button not enabled")
            else:
                school_add.click()
        sleep(10)
        school_grade.send_keys(Keys.TAB)

        school_owner.send_keys("indecomm")
        school_owner.send_keys(Keys.TAB)
        sleep(10)
        # Type selection (add the code)


        # Click SAVE button to save the form
        school_save.click()
        sleep(5)
        # check new place is created - verifying on Breadcrumb
        self.assertEqual("kk school automation test", self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        # go to search and filter page
        self.driver.find_element_by_link_text("Assets").click()


    @attr(priority="high")
 #  @SkipTest
    def test_AS_50_To_Verify_That_Created_SchoolAsset_Displayed_In_The_List(self):

        searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
        searchAsset_textbox.clear()
        searchAsset_textbox.send_keys("kk school automation test")
        sleep(20)
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[2]"):
            print (i.text)
            self.assertEqual("rgba(255, 236, 158, 1)", i.value_of_css_property("background-color"))
        searchAsset_textbox.clear()


    @attr(priority="high")
#    @SkipTest
    def test_AS_51_To_validate_SchoolName_Field(self):

        sleep(10)
        #Navigate to create asset dialouge
        clickCreateAsset = self.driver.find_element_by_xpath("//img[@alt='Create asset']")
        clickCreateAsset.click()
        sleep(12)

        # switch to new window
        self.driver.switch_to.active_element

        # Verify title "Asset overview" window
        #Create_Asset = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(By.XPATH,"//div[@id='asset_overview_modal']/div/div/div/h4"))
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='asset_overview_modal']/div/div/div/h4")))
        #Create_Asset = WebDriverWait(self.driver, 3).until(expected_conditions.title_is("Asset overview"))
        Create_Asset_Title = self.driver.find_element_by_xpath("//div[@id='asset_overview_modal']/div/div/div/h4").text
        sleep(2)
        self.assertEqual("Asset overview", Create_Asset_Title)

        # Select Place from the dropdown to create new school asset
        self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[1]/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()

        # Verify that all the controls displayed related to School asset
        school_name = self.driver.find_element_by_xpath("//input[@ng-model='model']")
        school_save = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[2]")
        school_cancel = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[1]")

        #Try to save without entering school name
        school_save.click()

        #Verfiy the dialouge is not dismissed and the name field is still available after the save operation
        self.assertEqual("Asset overview", Create_Asset_Title)
        self.assertTrue(school_name.is_enabled)

        #****Red star validation script to be added later

        school_cancel.click()
        sleep(10)



    @attr(priority="high")
#   @SkipTest
    def test_AS_53_To_validate_GradeandDistrict_Fields(self):

        fake= Factory.create()
        sleep(10)
        #Navigate to create asset dialouge
        clickCreateAsset = self.driver.find_element_by_xpath("//img[@alt='Create asset']")
        clickCreateAsset.click()
        sleep(12)

        # switch to new window
        self.driver.switch_to.active_element


        # Verify title "Asset overview" window
        #Create_Asset = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(By.XPATH,"//div[@id='asset_overview_modal']/div/div/div/h4"))
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='asset_overview_modal']/div/div/div/h4")))
        #Create_Asset = WebDriverWait(self.driver, 3).until(expected_conditions.title_is("Asset overview"))
        Create_Asset_Title = self.driver.find_element_by_xpath("//div[@id='asset_overview_modal']/div/div/div/h4").text
        sleep(2)
        self.assertEqual("Asset overview", Create_Asset_Title)

        # Select Place from the dropdown to create new school asset
        self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[1]/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()

        # Verify that all the controls displayed related to School asset
        school_name = self.driver.find_element_by_xpath("//input[@ng-model='model']")
        school_save = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[2]")
        school_district = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/button[1]")
        school_grade = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/button[1]")
        school_cancel = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[1]")

        # check all fields are enabled
        self.assertTrue(school_name.is_enabled()
                        and school_grade.is_enabled()
                        and school_district.is_enabled()
                        and school_save.is_enabled())

        schoolName = fake.company()
        school_name.send_keys(schoolName)

        school_district.click()
        sleep(2)
        school_newdistrict = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li/input")
        school_newdistrict.click()
        school_newdistrict.send_keys("Vali123@*>? ")
        school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
        self.assertTrue(school_add.is_enabled())
        school_add.click()
        sleep(2)

        school_grade.click()
        sleep(2)
        school_newgrade = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li/input")
        school_newgrade.click()
        school_newgrade.send_keys("Vali123@*>? ")
        school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
        try:
            self.assertTrue(school_add.is_displayed())
        except:
            print("Add button not enabled")
        else:
            school_add.click()


        #Save the school asset
        school_save.click()

        # check new school is created - verifying on Breadcrumb
        self.assertEqual(schoolName, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)

        school_name_page = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[1]/div/div[2]/table/tbody/tr[1]/td[2]")
        school_district_page = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[1]/div/div[2]/table/tbody/tr[4]/td[2]")
        school_grade_page = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[1]/div/div[2]/table/tbody/tr[5]/td[2]")
        act_schoolname = str(school_name_page.text)
        act_distname = str(school_district_page.text)
        self.driver.find_element_by_link_text("Assets").click()
        self.assertEqual(schoolName,act_schoolname)
        self.assertEqual("Vali123@*>?",act_distname)
        print(act_distname,act_schoolname, schoolName)
        #self.assertEqual("Vali123@*(>?",school_grade_page.text)

        # go to search and filter page



    @attr(priority="high")
#    @SkipTest
    def test_AS_54_To_Verify_Create_Asset_Function_Create_School_Asset_Cancel(self):

        sleep(10)
        # Click on Create asset
        #self.driver.find_element_by_xpath("//img[contains(@title,'Create asset')]").click()
        self.driver.find_element_by_xpath("//img[@alt='Create asset']").click()
        sleep(12)
        # switch to new window
        self.driver.switch_to.active_element
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='asset_overview_modal']/div/div/div/h4")))
        # Verify title "Asset overview" window
        Create_Asset_Title = self.driver.find_element_by_xpath("//div[@id='asset_overview_modal']/div/div/div/h4").text
        sleep(2)
        self.assertEqual("Asset overview", Create_Asset_Title)

        # Select Place from the dropdown to create new place asset
        self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[1]/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()
        sleep(10)

        # Verify that all the controls displayed related to Place asset
        # 1. Name, 2. Address, 3. Address2, 4. City, 5. State, 6. Zip, 7. Owner, 8. Phone, 9. Type, 10. Cancel, 11. Save

        school_name = self.driver.find_element_by_xpath("//input[@ng-model='model']")
        school_address = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.address1']")
        school_address2 = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.address2']")
        school_city = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.city']")
        school_state = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.state']")
        school_zip = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.zip']")
        school_owner = self.driver.find_element_by_xpath("//input[@placeholder='Owner']")
        school_phone = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/div[3]/input")
        school_district = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/button[1]")
        school_grade = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/button[1]")
        school_type = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/button[1]")
        school_cancel = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[1]")
        school_save = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[2]")

        # check all fields are enabled
        self.assertTrue(school_name.is_enabled()
                        and school_address.is_enabled()
                        and school_address2.is_enabled()
                        and school_city.is_enabled()
                        and school_state.is_enabled()
                        and school_zip.is_enabled()
                        and school_owner.is_enabled()
                        and school_phone.is_enabled()
                        and school_type.is_enabled()
                        and school_cancel.is_enabled()
                        and school_save.is_enabled())

        # fill out the fields
        school_name.send_keys("kk school automation test")
        school_name.send_keys(Keys.TAB)
        sleep(2)
        school_address.send_keys("indecomm")
        school_address.send_keys(Keys.TAB)
        sleep(2)
        school_address2.send_keys("MG Road")
        school_address2.send_keys(Keys.TAB)
        sleep(2)
        school_city.send_keys("Bangalore")
        school_city.send_keys(Keys.TAB)
        sleep(2)
        school_state.send_keys("KA")
        school_state.send_keys(Keys.TAB)
        sleep(2)
        school_zip.send_keys("56009")
        school_zip.send_keys(Keys.TAB)
        sleep(2)
        school_phone.send_keys("994-550-8652")
        school_phone.send_keys(Keys.TAB)
        sleep(2)

        school_district.click()
        try:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li[1]/a")
        except NoSuchElementException:
            school_newdistrict = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li/input")
            school_newdistrict.click()
            school_newdistrict.send_keys("hm")
            school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
            self.assertTrue(school_add.is_enabled())
            school_add.click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li[1]/a").click()
        sleep(2)

        school_grade.click()
        sleep(2)
        try:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[1]/a")
        except NoSuchElementException:
            school_newgrade = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li/input")
            school_newgrade.click()
            school_newgrade.send_keys("hm")
            school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
            try:
                 self.assertTrue(school_add.is_displayed())
            except:
                 print("Add button not enabled")
            else:
                school_add.click()
        else:
          self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[1]/a").click()
          sleep(2)

        school_owner.send_keys("indecomm")
        school_owner.send_keys(Keys.TAB)
        sleep(2)
        # Type selection
        '''school_type.click()
        try:
              self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/ul/li[2]/a")
        except NoSuchElementException:
            school_newtype=self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/ul/li[2]/input")
            school_newtype.click()
            school_newtype.send_keys("hm")
            school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
            self.assertTrue(school_add.is_enabled())
            school_add.click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/ul/li[2]/a").click()
        sleep(2)'''

        # Click cancel button to save the form
        school_cancel.click()
        sleep(5)

        # check new place is created - verifying on Breadcrumb

        try:
            self.driver.find_element_by_xpath(".//*[@id='header']/div[1]/span[3]/span")
        except NoSuchElementException:
            print ("In Assets main page")


    @attr(priority="high")
#    @SkipTest
    def test_AS_55_To_Verify_SchoolAsset_Edit(self):
        sleep(12)

        self.driver.find_element_by_xpath("//span[@id='span_filters']/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()

        sleep(10)
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(20)

        editOverview = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[1]/div/div[1]/div/img")
        editOverview.click()

        # switch to new window
        self.driver.switch_to.active_element

        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='asset_overview_modal']/div/div/div/h4")))
        # Verify title "Asset overview" window
        # Create_Asset_Title = self.driver.find_element_by_xpath(".//*[@id='H1']").text
        Create_Asset_Title = self.driver.find_element_by_xpath("//div[@id='asset_overview_modal']/div/div/div/h4").text
        print(Create_Asset_Title)
        sleep(10)
        self.assertEqual("Asset overview", Create_Asset_Title)

        # Verify that all the controls displayed related to Place asset
        # 1. Name, 2. Address, 3. Address2, 4. City, 5. State, 6. Zip, 7. Owner, 8. Phone, 9. Type, 10. Cancel, 11. Save

        school_name = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.name']")
        school_address = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.address1']")
        school_address2 = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.address2']")
        school_city = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.city']")
        school_state = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.state']")
        school_zip = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.zip']")
        #school_owner = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[4]/div/input")
        school_phone = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/div[3]/input")
        school_district = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/button[1]")
        school_grade = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/button[1]")
        school_type = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/button[1]")
        school_cancel = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[1]")
        school_save = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[2]")

        # check all fields are enabled
        self.assertTrue(school_name.is_enabled()
                        and school_address.is_enabled()
                        and school_address2.is_enabled()
                        and school_city.is_enabled()
                        and school_state.is_enabled()
                        and school_zip.is_enabled()
                       # and school_owner.is_enabled()
                        and school_phone.is_enabled()
                        and school_type.is_enabled()
                        and school_cancel.is_enabled()
                        and school_save.is_enabled())

        # fill out the fields
        school_name.clear()
        school_name.send_keys("kk school automation edit")
        school_name.send_keys(Keys.TAB)
        sleep(2)
        school_address.clear()
        school_address.send_keys("indecomm")
        school_address.send_keys(Keys.TAB)
        sleep(2)
        school_address2.clear()
        school_address2.send_keys("MG Road")
        school_address2.send_keys(Keys.TAB)
        sleep(2)
        school_city.clear()
        school_city.send_keys("Bangalore")
        school_city.send_keys(Keys.TAB)
        sleep(2)
        school_state.clear()
        school_state.send_keys("KA")
        school_state.send_keys(Keys.TAB)
        sleep(2)
        school_zip.clear()
        school_zip.send_keys("56009")
        school_zip.send_keys(Keys.TAB)
        sleep(2)
        school_phone.clear()
        school_phone.send_keys("994-550-8652")
        school_phone.send_keys(Keys.TAB)
        sleep(2)

        school_district.click()
        try:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li[1]/a")
        except NoSuchElementException:
            school_newdistrict = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li/input")
            school_newdistrict.click()
            school_newdistrict.send_keys("hm")
            school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
            self.assertTrue(school_add.is_enabled())
            school_add.click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li[1]/a").click()
        sleep(2)

        school_grade.click()
        sleep(2)
        try:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[1]/a")
        except NoSuchElementException:
            school_newgrade = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li/input")
            school_newgrade.click()
            school_newgrade.send_keys("hm")
            school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
            try:
                 self.assertTrue(school_add.is_displayed())
            except:
                 print("Add button not enabled")
            else:
                school_add.click()
        else:
          self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[1]/a").click()
          sleep(2)

        #school_owner.clear()
        #school_owner.send_keys("indecomm")
        #school_owner.send_keys(Keys.TAB)
        sleep(2)
        # Type selection
        '''school_type.click()
        try:
              self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/ul/li[2]/a")
        except NoSuchElementException:
            school_newtype=self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/ul/li[2]/input")
            school_newtype.click()
            school_newtype.send_keys("hm")
            school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
            self.assertTrue(school_add.is_enabled())
            school_add.click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/ul/li[2]/a").click()
        sleep(2)'''
        # Click save button to save the form
        school_save.click()
        sleep(5)

        # check new place is created - verifying on Breadcrumb
        self.assertEqual("kk school automation edit", self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        # go to search and filter page
        self.driver.find_element_by_link_text("Assets").click()


    @attr(priority="high")
#    @SkipTest
    def test_AS_56_To_Verify_SchoolAsset_Edit_Cancel(self):
        sleep(12)

        self.driver.find_element_by_xpath("//span[@id='span_filters']/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()

        sleep(10)
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(20)

        editOverview = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[1]/div/div[1]/div/img")
        editOverview.click()

        # switch to new window
        self.driver.switch_to.active_element

        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='asset_overview_modal']/div/div/div/h4")))
        # Verify title "Asset overview" window
        # Create_Asset_Title = self.driver.find_element_by_xpath(".//*[@id='H1']").text
        Create_Asset_Title = self.driver.find_element_by_xpath("//div[@id='asset_overview_modal']/div/div/div/h4").text
        print(Create_Asset_Title)
        sleep(10)
        self.assertEqual("Asset overview", Create_Asset_Title)

        # Verify that all the controls displayed related to Place asset
        # 1. Name, 2. Address, 3. Address2, 4. City, 5. State, 6. Zip, 7. Owner, 8. Phone, 9. Type, 10. Cancel, 11. Save

        school_name = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.name']")
        school_address = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.address1']")
        school_address2 = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.address2']")
        school_city = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.city']")
        school_state = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.state']")
        school_zip = self.driver.find_element_by_xpath("//input[@ng-model='asset_edit.address.zip']")
        school_owner = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[4]/div/input")
        school_phone = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/div[3]/input")
        school_district = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/button[1]")
        school_grade = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/button[1]")
        school_type = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/button[1]")
        school_cancel = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[1]")
        school_save = self.driver.find_element_by_xpath("//*[@id='asset_overview_modal']/div/div/form/div[2]/button[2]")

        # check all fields are enabled
        self.assertTrue(school_name.is_enabled()
                        and school_address.is_enabled()
                        and school_address2.is_enabled()
                        and school_city.is_enabled()
                        and school_state.is_enabled()
                        and school_zip.is_enabled()
                        and school_owner.is_enabled()
                        and school_phone.is_enabled()
                        and school_type.is_enabled()
                        and school_cancel.is_enabled()
                        and school_save.is_enabled())

        # fill out the fields
        school_name.clear()
        school_name.send_keys("kk school automation edit")
        school_name.send_keys(Keys.TAB)
        sleep(2)
        school_address.clear()
        school_address.send_keys("indecomm")
        school_address.send_keys(Keys.TAB)
        sleep(2)
        school_address2.clear()
        school_address2.send_keys("MG Road")
        school_address2.send_keys(Keys.TAB)
        sleep(2)
        school_city.clear()
        school_city.send_keys("Bangalore")
        school_city.send_keys(Keys.TAB)
        sleep(2)
        school_state.clear()
        school_state.send_keys("KA")
        school_state.send_keys(Keys.TAB)
        sleep(2)
        school_zip.clear()
        school_zip.send_keys("56009")
        school_zip.send_keys(Keys.TAB)
        sleep(2)
        school_phone.clear()
        school_phone.send_keys("994-550-8652")
        school_phone.send_keys(Keys.TAB)
        sleep(2)

        school_district.click()
        try:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li[1]/a")
        except NoSuchElementException:
            school_newdistrict = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li/input")
            school_newdistrict.click()
            school_newdistrict.send_keys("hm")
            school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
            self.assertTrue(school_add.is_enabled())
            school_add.click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li[1]/a").click()
        sleep(2)

        school_grade.click()
        sleep(2)
        try:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[1]/a")
        except NoSuchElementException:
            school_newgrade = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li/input")
            school_newgrade.click()
            school_newgrade.send_keys("hm")
            school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
            try:
                 self.assertTrue(school_add.is_displayed())
            except:
                 print("Add button not enabled")
            else:
                school_add.click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[1]/a").click()
            sleep(2)

        school_owner.clear()
        school_owner.send_keys("indecomm")
        school_owner.send_keys(Keys.TAB)
        sleep(10)
        # Type selection
        school_type.click()
        try:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/ul/li[2]/a")
        except NoSuchElementException:
            school_newtype=self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/ul/li[2]/input")
            school_newtype.click()
            school_newtype.send_keys("hm")
            school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
            self.assertTrue(school_add.is_enabled())
            school_add.click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/ul/li[2]/a").click()
        sleep(2)
        # Click cancel button to save the form
        school_cancel.click()
        sleep(5)

        # check new place is created - verifying on Breadcrumb
        self.assertEqual(self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        # go to search and filter page
        self.driver.find_element_by_link_text("Assets").click()


    @attr(priority="high")
#    @SkipTest
    def test_AS_58_To_Verify_School_Asset_Edit_Details_Panel_Save(self):
        sleep(12)

        self.driver.find_element_by_xpath("//span[@id='span_filters']/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()

        sleep(10)
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(20)

        editSchoolDetailsPanel = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[1]/div/img")
        editSchoolDetailsPanel.click()

        # switch to new window
        self.driver.switch_to.active_element

        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='asset_overview_modal']/div/div/div/h4")))
        # Verify title "Asset overview" window
        # Create_Asset_Title = self.driver.find_element_by_xpath(".//*[@id='H1']").text
        Asset_Details_Title = self.driver.find_element_by_xpath(".//*[@id='H2']").text
        print(Asset_Details_Title)
        sleep(10)
        self.assertEqual("Asset details", Asset_Details_Title)

        # Verify that all the controls displayed related to Place asset
        # 1. Name, 2. Address, 3. Address2, 4. City, 5. State, 6. Zip, 7. Owner, 8. Phone, 9. Type, 10. Cancel, 11. Save

        school_edit_details_capacity = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[1]/div/span/input")
        school_edit_details_closed = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[2]/div/span/input")
        school_edit_details_description = self.driver.find_element_by_xpath(".//*[@id='asset_details_description_edit']")
        school_edit_details_district_number = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[4]/div/span/input")
        school_edit_details_email = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[5]/div/span/input")
        school_edit_details_fax = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[6]/div/span/input")
        school_edit_details_opened = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[7]/div/span/input")
        school_edit_details_school_number = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[8]/div/span/input")
        school_edit_details_size = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[9]/div/span/input")
        school_edit_details_website = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[10]/div/span/input")

        school_edit_details_cancel = self.driver.find_element_by_xpath("//*[@id='asset_details_modal']/div/div/form/div[2]/button[1]")
        school_edit_details_save = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[2]/button[2]")





        # check all fields are enabled
        self.assertTrue(school_edit_details_capacity.is_enabled()
                        and school_edit_details_closed.is_enabled()
                        and school_edit_details_description.is_enabled()
                        and school_edit_details_district_number.is_enabled()
                        and school_edit_details_email.is_enabled()
                        and school_edit_details_fax.is_enabled()
                        and school_edit_details_opened.is_enabled()
                        and school_edit_details_school_number.is_enabled()
                        and school_edit_details_size.is_enabled()
                        and school_edit_details_website.is_enabled()
                        and school_edit_details_cancel.is_enabled()
                        and school_edit_details_save.is_enabled())

        # save these values for future reference, since once saved, we are comparing these values with the widget values.
        school_edit_value_capacity = "1234"
        school_edit_value_closed = "2017-05-16"
        school_edit_value_description = "Description of School 3"
        school_edit_value_district_number = "22222"
        school_edit_value_email = "ki22ran2.k@indecomm.net"
        school_edit_value_fax = "123-4567-892"
        school_edit_value_opened = "2015-02-23"
        school_edit_value_school_number = "63"
        school_edit_value_size = "12001"
        school_edit_value_website = "http://www.haystax.com"



        # fill out the fields
        school_edit_details_capacity.clear()
        school_edit_details_capacity.send_keys(school_edit_value_capacity)
        school_edit_details_capacity.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_closed.clear()
        school_edit_details_closed.send_keys(school_edit_value_closed)
        school_edit_details_closed.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_description.clear()
        school_edit_details_description.send_keys(school_edit_value_description)
        school_edit_details_description.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_district_number.clear()
        school_edit_details_district_number.send_keys(school_edit_value_district_number)
        school_edit_details_district_number.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_email.clear()
        school_edit_details_email.send_keys(school_edit_value_email)
        school_edit_details_email.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_fax.clear()
        school_edit_details_fax.send_keys(school_edit_value_fax)
        school_edit_details_fax.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_opened.clear()
        school_edit_details_opened.send_keys(school_edit_value_opened)
        school_edit_details_opened.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_school_number.clear()
        school_edit_details_school_number.send_keys(school_edit_value_school_number)
        school_edit_details_school_number.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_size.clear()
        school_edit_details_size.send_keys(school_edit_value_size)
        school_edit_details_size.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_website.clear()
        school_edit_details_website.send_keys(school_edit_value_website)
        school_edit_details_website.send_keys(Keys.TAB)
        sleep(2)




        # Click save button to save the form
        school_edit_details_save.click()
        sleep(5)



    @attr(priority="high")
#    @SkipTest
    def test_AS_58_To_Verify_School_Asset_Edit_Details_Panel_Cancel(self):
        sleep(12)

        self.driver.find_element_by_xpath("//span[@id='span_filters']/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()

        sleep(10)
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(20)

        editSchoolDetailsPanel = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[1]/div/img")
        editSchoolDetailsPanel.click()

        # switch to new window
        self.driver.switch_to.active_element

        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@id='asset_overview_modal']/div/div/div/h4")))
        # Verify title "Asset overview" window
        # Create_Asset_Title = self.driver.find_element_by_xpath(".//*[@id='H1']").text
        Asset_Details_Title = self.driver.find_element_by_xpath(".//*[@id='H2']").text
        print(Asset_Details_Title)
        sleep(10)
        self.assertEqual("Asset details", Asset_Details_Title)

        # Verify that all the controls displayed related to Place asset
        # 1. Name, 2. Address, 3. Address2, 4. City, 5. State, 6. Zip, 7. Owner, 8. Phone, 9. Type, 10. Cancel, 11. Save

        school_edit_details_capacity = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[1]/div/span/input")
        school_edit_details_closed = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[2]/div/span/input")
        school_edit_details_description = self.driver.find_element_by_xpath(".//*[@id='asset_details_description_edit']")
        school_edit_details_district_number = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[4]/div/span/input")
        school_edit_details_email = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[5]/div/span/input")
        school_edit_details_fax = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[6]/div/span/input")
        school_edit_details_opened = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[7]/div/span/input")
        school_edit_details_school_number = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[8]/div/span/input")
        school_edit_details_size = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[9]/div/span/input")
        school_edit_details_website = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[1]/span[10]/div/span/input")

        school_edit_details_cancel = self.driver.find_element_by_xpath("//*[@id='asset_details_modal']/div/div/form/div[2]/button[1]")
        school_edit_details_save = self.driver.find_element_by_xpath(".//*[@id='asset_details_modal']/div/div/form/div[2]/button[2]")





        # check all fields are enabled
        self.assertTrue(school_edit_details_capacity.is_enabled()
                        and school_edit_details_closed.is_enabled()
                        and school_edit_details_description.is_enabled()
                        and school_edit_details_district_number.is_enabled()
                        and school_edit_details_email.is_enabled()
                        and school_edit_details_fax.is_enabled()
                        and school_edit_details_opened.is_enabled()
                        and school_edit_details_school_number.is_enabled()
                        and school_edit_details_size.is_enabled()
                        and school_edit_details_website.is_enabled()
                        and school_edit_details_cancel.is_enabled()
                        and school_edit_details_save.is_enabled())

        # save these values for future reference, since once saved, we are comparing these values with the widget values.
        school_edit_value_capacity = "1112345"
        school_edit_value_closed = "2013-05-16"
        school_edit_value_description = "aaa Description of School 3"
        school_edit_value_district_number = "11122222"
        school_edit_value_email = "kkkki22ran2.k@indecomm.net"
        school_edit_value_fax = "111-4567-892"
        school_edit_value_opened = "2222-02-23"
        school_edit_value_school_number = "22263"
        school_edit_value_size = "222001"
        school_edit_value_website = "http://www.myhaystax.com"



        # fill out the fields
        school_edit_details_capacity.clear()
        school_edit_details_capacity.send_keys(school_edit_value_capacity)
        school_edit_details_capacity.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_closed.clear()
        school_edit_details_closed.send_keys(school_edit_value_closed)
        school_edit_details_closed.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_description.clear()
        school_edit_details_description.send_keys(school_edit_value_description)
        school_edit_details_description.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_district_number.clear()
        school_edit_details_district_number.send_keys(school_edit_value_district_number)
        school_edit_details_district_number.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_email.clear()
        school_edit_details_email.send_keys(school_edit_value_email)
        school_edit_details_email.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_fax.clear()
        school_edit_details_fax.send_keys(school_edit_value_fax)
        school_edit_details_fax.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_opened.clear()
        school_edit_details_opened.send_keys(school_edit_value_opened)
        school_edit_details_opened.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_school_number.clear()
        school_edit_details_school_number.send_keys(school_edit_value_school_number)
        school_edit_details_school_number.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_size.clear()
        school_edit_details_size.send_keys(school_edit_value_size)
        school_edit_details_size.send_keys(Keys.TAB)
        sleep(2)
        school_edit_details_website.clear()
        school_edit_details_website.send_keys(school_edit_value_website)
        school_edit_details_website.send_keys(Keys.TAB)
        sleep(2)




        # Click save button to save the form
        school_edit_details_cancel.click()
        sleep(5)



        # Details of Widget values
        school_widget_value_capacity = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[2]/table/tbody/tr[1]/td[2]/span").text
        school_widget_value_closed = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[2]/table/tbody/tr[2]/td[2]/span").text
        school_widget_value_description = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[2]/table/tbody/tr[3]/td[2]/span").text
        school_widget_value_district_number = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[2]/table/tbody/tr[4]/td[2]/span").text
        school_widget_value_email = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[2]/table/tbody/tr[5]/td[2]/span").text
        school_widget_value_fax = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[2]/table/tbody/tr[6]/td[2]/span").text
        school_widget_value_opened = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[2]/table/tbody/tr[7]/td[2]/span").text
        school_widget_value_school_number = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[2]/table/tbody/tr[8]/td[2]/span").text
        school_widget_value_size = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[2]/table/tbody/tr[9]/td[2]/span").text
        school_widget_value_website = self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[2]/table/tbody/tr[10]/td[2]/span").text




        # check Details created -
        self.assertNotEqual(school_edit_value_capacity, school_widget_value_capacity, "Capacity didn't match")
        self.assertNotEqual(school_edit_value_closed, school_widget_value_closed)
        self.assertNotEqual(school_edit_value_description, school_widget_value_description)
        self.assertNotEqual(school_edit_value_district_number, school_widget_value_district_number)
        self.assertNotEqual(school_edit_value_email, school_widget_value_email)
        self.assertNotEqual(school_edit_value_fax, school_widget_value_fax)
        self.assertNotEqual(school_edit_value_opened, school_widget_value_opened)
        self.assertNotEqual(school_edit_value_school_number, school_widget_value_school_number)
        self.assertNotEqual(school_edit_value_size, school_widget_value_size)
        self.assertNotEqual(school_edit_value_website, school_widget_value_website)


        # go to search and filter page
        self.driver.find_element_by_link_text("Assets").click()


if __name__ =='__main__':
    unittest.main(verbosity=2)
