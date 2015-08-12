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


class MainDriverScript(BaseTestCase):

    fake = Factory.create()
    Place_name = fake.company()
    School_name = fake.name()

    @attr(priority="high")
    @SkipTest
    def test_AS_01_To_Verify_Delete_When_No_Assets_Are_Available(self):
        selectAction_dropdown = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/button[2]")
        selectAction_dropdown.click()
        selectAction_dropdown_delete = self.driver.find_element_by_xpath(".//*[@id='asset_actions_dropdown']/ul/li/a")
        self.assertFalse(selectAction_dropdown_delete.is_enabled(), "Delete must be disabled.")

    @attr(priority="high")
    @SkipTest
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
    @SkipTest
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
    @SkipTest
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
    @SkipTest
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
    @SkipTest
    def test_AS_11_To_Verify_The_Reset_Filter_Function(self):
        resetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/button")
        resetFilter.click()
        expectedAfterResetFilter = self.driver.find_element_by_xpath(".//*[@id='span_filters']/div/div/button[1]").text
        self.assertEqual("Asset Type",expectedAfterResetFilter)


    @attr(priority="high")
    @SkipTest
    def test_AS_12_To_Verify_The_Search_For_Asset_Function_Search_By_Name(self):
        print "Getting Search data from Json"
        searchasset_filepath = os.path.abspath('data/json_searchAssets.json')
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
                for searchName in searchNames:
                    #if searchName.text == expectedAfterSearchFilter:
                    if expectedAfterSearchFilter:
                        self.assertEqual("No matching records found", expectedAfterSearchFilter, "No records to find asset.")
                    else:
                        print searchName.text



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

        fake = Factory.create()
        # fill out the fields
        place_name.send_keys(self.Place_name)
        #place_name.send_keys("kk place automation test")
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
        sleep(5)
        # check new place is created - verifying on Breadcrumb
        self.assertEqual(self.School_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        # go to search and filter page
        self.driver.find_element_by_link_text("Assets").click()
        sleep(20)

    @attr(priority="high")
#    @SkipTest
    def test_AS_17_To_Verify_That_Created_Asset_Displayed_In_The_List(self):
        searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
        searchAsset_textbox.send_keys(self.Place_name)
        sleep(20)
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[2]"):
            print (i.text)
            self.assertEqual("rgba(255, 236, 158, 1)", i.value_of_css_property("background-color"))


    @attr(priority="high")
    @SkipTest
    def test_AS_29_To_Click_On_Save_Without_FirstName_Asset_ContactInfo_Field(self):
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(3)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        self.driver.find_element_by_name("first_name").clear()
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[2]").click()
        self.driver.find_element_by_name("last_name").click()
        state = self.driver.find_element_by_xpath(".//*[@id='asset_contact_error']/div[1]/small").is_displayed()
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/div/button").click()
        self.driver.find_element_by_link_text("Assets").click()
        sleep(3)
        self.assertTrue(state)

    @attr(priority="high")
    @SkipTest
    def test_AS_30_To_Click_On_Save_Without_LastName_Asset_ContactInfo_Field(self):
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(3)
        self.driver.find_element_by_xpath("//div[contains(text(), 'Points of Contact')]")
        self.driver.find_element_by_id('btn_add_asset_contact').click()
        self.driver.find_element_by_name("first_name").send_keys("Firtst Name")
        self.driver.find_element_by_name("last_name").clear()
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/form/div[2]/button[2]").click()
        self.driver.find_element_by_name("first_name").click()
        state =(self.driver.find_element_by_xpath(".//*[@id='asset_contact_error']/div[2]/small").is_displayed())
        self.driver.find_element_by_xpath(".//*[@id='asset_contact_modal']/div/div/div/button").click()
        self.driver.find_element_by_link_text("Assets").click()
        sleep(3)
        self.assertTrue(state)


    @attr(priority="high")
    @SkipTest
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
    @SkipTest
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
        sleep(3)
        self.assertFalse(state)


    @attr(priority="high")
    @SkipTest
    def test_AS_33_To_Click_On_Save_With_FirstName_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(3)
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
    @SkipTest
    def test_AS_34_To_Click_On_Save_With_Prefix_Title_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(3)
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
    @SkipTest
    def test_AS_35_To_Click_On_Save_With_Phone_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(3)
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
    @SkipTest
    def test_AS_36_To_Click_On_Save_With_Email_Asset_ContactInfo_Field(self):
        firstname = "FirstName"
        lastname = "ZLastName"
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(3)
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
        print email, "dddddddddddddddddddddddddddddd", type(email)
        self.driver.find_element_by_link_text("Assets").click()
        regex = re.compile(r'[\w.-]+@[\w.-]+')
        self.assertRegexpMatches(email, regex)


    @attr(priority="high")
    @SkipTest
    def test_AS_33_To_Click_On_Save_With_Wrong_Fax_Asset_Detail_Field(self):
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        self.driver.find_element_by_xpath(".//*[@id='widgets']/div[5]/div/div[1]/div/img").click()

    @attr(priority="high")
 #   @SkipTest
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
        #school_name.send_keys("kk school automation test")
        school_name.send_keys(self.School_name)
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
        self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[2]/div/div/ul/li[1]/a").click()
        sleep(2)
        school_grade.click()
        self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[1]/a").click()
        sleep(2)

        school_owner.send_keys("indecomm")
        school_owner.send_keys(Keys.TAB)
        sleep(2)
        # Type selection
        school_type.click()
        self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[5]/div/div/ul/li[2]/a").click()
        sleep(2)
        # Click SAVE button to save the form
        school_save.click()
        sleep(5)
        # check new place is created - verifying on Breadcrumb
        self.assertEqual(self.School_name, self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        # go to search and filter page
        self.driver.find_element_by_link_text("Assets").click()

    @attr(priority="high")
    @SkipTest
    def test_AS_50_To_validate_SchoolName_Field(self):

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


    @attr(priority="high")
    @SkipTest
    def test_AS_52_To_validate_GradeandDistrict_Fields(self):

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
        school_newdistrict.send_keys("Vali123@*(>? ")
        school_add = self.driver.find_element_by_xpath(".//*[@id='newItemButton']")
        self.assertTrue(school_add.is_enabled())
        school_add.click()
        sleep(2)

        school_grade.click()
        sleep(2)
        school_newgrade = self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li/input")
        school_newgrade.click()
        school_newgrade.send_keys("Vali123@*(>? ")
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
        self.assertEqual(schoolName,school_name_page.text)
        self.assertEqual("Vali123@*(>?",school_district_page.text)
        #self.assertEqual("Vali123@*(>?",school_grade_page.text)

        # go to search and filter page
        self.driver.find_element_by_link_text("Assets").click()
        sleep(20)

    @attr(priority="high")
    @SkipTest
    def test_AS_53_To_Verify_That_Created_SchoolAsset_Displayed_In_The_List(self):
        searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
        searchAsset_textbox.send_keys(self.School_name)
        sleep(20)
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[2]"):
            print (i.text)
            self.assertEqual("rgba(255, 236, 158, 1)", i.value_of_css_property("background-color"))


    @attr(priority="high")
    @SkipTest
    def test_AS_54_To_Verify_Create_Asset_Function_Create_School_Asset_Cancel(self):

        sleep(10)
        # Click on Create asset
        clickCreateAsset = self.driver.find_element_by_xpath("//img[@alt='Create asset']")
        clickCreateAsset.click()
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
        #searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
        #searchAsset_textbox.send_keys(self.School_name)
        #sleep(20)
        searchnames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        searchnames[0].click()
        sleep(10)

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
        school_save.click()
        sleep(5)
        # check new place is created - verifying on Breadcrumb
        self.assertEqual("kk school automation edit", self.driver.find_element_by_xpath("//*[@id='header']/div[1]/span[3]/span").text)
        # go to search and filter page
        self.driver.find_element_by_link_text("Assets").click()


        if __name__ =='__main__':
            unittest.main(verbosity=2)
