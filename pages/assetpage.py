from lib.base import BasePage
from lib.base import InvalidPageException
from time import sleep
from faker import Factory
from selenium.webdriver.common.keys import Keys


class AssetPage(BasePage):
    # Asset Delete related locators
    _select_action_delete_click_xpath_locator = ".//*[@id='asset_actions_dropdown']/button[2]"
    _click_delete_text_xpath_locator = ".//*[@id='asset_actions_dropdown']/ul/li/a"

    # Asset List related
    _asset_list_locator = "//tbody/tr/td/a"
    _asset_list_check_box_locator = ".//*[@id='assetstable']/tbody/tr/td[1]/label/span/span[2]"
    _asset_list_asset_name_locator = ".//*[@id='assetstable']/tbody/tr/td[2]/a"
    _asset_list_asset_type_locator = ".//*[@id='assetstable']/tbody/tr/td[3]"

    # Asset Filter related to place and school
    _asset_filter_drop_down_locator = "//*[@id='span_filters']/div/div/button[2]"
    #asset list is already specified above i,e _asset_list_locator
    # we need xpath for type column i,e place or school. locator is already defined above i,e _asset_list_asset_type_locator
    _asset_place_type_drop_down_locator = "//div[@label='Type']"
    _asset_school_district_drop_down_locator = "//div[@label= 'District']"

    # New Asset creation related
    _asset_create_asset = "//img[@alt='Create asset']"




    _asset_count = 0
    _assets = {}


    def __init__(self, driver):
        super(AssetPage, self).__init__(driver)

        '''
        assets_results = self.driver.find_elements_by_xpath(self._asset_list_locator)
        for asset in assets_results:
            assetname = asset.find_elements_by_xpath(self._asset_list_asset_name_locator).text
            self._assets[assetname] = asset.find_element_by_xpath(self._asset_list_check_box_locator)
            self._assets[assetname] = asset.find_element_by_xpath(self._asset_list_asset_type_locator)
        '''


    @property
    def select_action_drop_down(cls):
        return cls.driver.find_element_by_xpath(cls._select_action_delete_click_xpath_locator)

    @property
    def click_delete_text(cls):
        return cls.driver.find_element_by_xpath(cls._click_delete_text_xpath_locator)

    @property
    def display_place_type_drop_down(cls):
        return cls.driver.find_element_by_xpath(cls._asset_place_type_drop_down_locator)

    @property
    def display_school_district_drop_down(cls):
        return cls.driver.find_element_by_xpath(cls._asset_school_district_drop_down_locator)

    def select_checkbox_in_grid(self):
        assets_checkbox = self.driver.find_elements_by_xpath(self._asset_list_check_box_locator)
        sleep(2)
        for asset_checkbox in assets_checkbox:
            sleep(1)
            asset_checkbox.click()

        for asset_checkbox in assets_checkbox:
            sleep(1)
            asset_checkbox.click()

    def asset_filter_based_on_place_and_school(cls, assetType):

        cls.driver.find_element_by_xpath(cls._asset_filter_drop_down_locator).click()
        cls.driver.find_element_by_link_text(assetType).click()

        assetsType = cls.driver.find_elements_by_xpath(cls._asset_list_locator)
        print "Found " + str(len(assetsType)) + " - " + assetType + " Asset Types"


    def asset_create(self):
        # Click on Create asset
        clickCreateAsset = self.driver.find_element_by_xpath(self._asset_create_asset)
        clickCreateAsset.click()
        sleep(12)
        # switch to new window
        self.driver.switch_to.active_element


        # Verify title "Asset overview" window
        Create_Asset_Title = self.driver.find_element_by_xpath("//div[@id='asset_overview_modal']/div/div/div/h4").text
        sleep(2)
        print("Asset overview", Create_Asset_Title)

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

        place_name.send_keys("kk validation")
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
        #place_owner.send_keys(fake.domain_name())
        #place_owner.send_keys(validate_email("kk@indecomm.net"))
        place_owner.send_keys(Keys.TAB)
        sleep(2)
        # Type selection
        place_type.click()
        self.driver.find_element_by_xpath(".//*[@id='asset_overview_modal']/div/div/form/div[1]/span/span[3]/div/div/ul/li[2]/a").click()
        sleep(2)
        # Click SAVE button to save the form
        place_save.click()
        sleep(20)


    def _validate_page(cls, driver):
        try:
            driver.find_element_by_xpath(cls._select_action_delete_click_xpath_locator)
        except:
            raise InvalidPageException("Select Action drop down not found.")

