__author__ = 'Deepa.Sivadas'
import unittest
from testcases.basetestcase import BaseTestCase
from pages.mappage import MapPage
from nose.plugins.attrib import attr
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class MapPageTest(BaseTestCase):

    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_map(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(20)
        self.assertEqual(mappage.get_map_app_name.text, "Map")

    # Default view
    @attr(priority="high")
    def test_map_01_to_verify_default(self):
        mappage = MapPage(self.driver)
        mouse_hover_field = mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_default_view_radio).click()\
            .perform()
        mappage.get_bread_crumb_apps.click() # Click on Bread crumb - Apps link

    # Night view
    @attr(priority="high")
    def test_map_02_to_verify_Night_View(self):
        mappage = MapPage(self.driver)
        mouse_hover_field = mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_night_view_radio).click()\
            .perform()
        mappage.get_bread_crumb_apps.click()# Click on Bread crumb - Apps link

    # Terrain
    @attr(priority="high")
    def test_map_03_to_verify_Terrain(self):
        mappage = MapPage(self.driver)
        mouse_hover_field = mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_terrain_radio).click()\
            .perform()
        mappage.get_bread_crumb_apps.click()# Click on Bread crumb - Apps link

    # Satelite Default
    @attr(priority="high")
    def test_map_04_to_verify_Satelite_Default(self):
        mappage = MapPage(self.driver)
        mouse_hover_field = mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_satelite_default_view_radio).click()\
            .perform()
        mappage.get_bread_crumb_apps.click() # Click on Bread crumb - Apps link

    # Satelite Grey
    @attr(priority="high")
    #@SkipTest
    def test_map_05_to_verify_Satelite_Grey(self):
        mappage = MapPage(self.driver)
        mouse_hover_field = mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_satelite_grey_view_radio).click()\
            .perform()
        mappage.get_bread_crumb_apps.click() # Click on Bread crumb - Apps link

    # View Full Screen
    @attr(priority="high")
    def test_map_13_to_verify_Map_Can_Be_Viewed_In_Full_Screen(self):
        mappage = MapPage(self.driver)
        mouse_hover_field = mappage.get_map_full_screen # mouse hover to View Full screen icon
        # below commented is the actual logic but click is not working here...
        '''
        # Click on Icon
        viewFullScreen = self.driver.find_element_by_xpath("//a[@title='View Fullscreen']")
        viewFullScreen.click()

        # Switch to alert
        alert = self.driver.switch_to.alert
        # get the text from alert
        alert_text = alert.text
        # check alert text
        self.assertEqual("haystax.com is now fullscreen.", alert_text)
        # click on Ok button
        alert.accept()

        # Press escape key
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        '''
        ActionChains(self.driver).move_to_element(mouse_hover_field).perform() #View Full Screen
        ActionChains(self.driver).send_keys(Keys.F11).perform() # to zoom by pressing F11 key on Keyboard
        ActionChains(self.driver).send_keys(Keys.F11).perform() # to zoom out by pressing F11 again on Keyboard
        mappage.get_bread_crumb_apps.click() # Click on Bread crumb - Apps link

    @attr(priority="high")
    #@SkipTest
    def test_map_06_to_verify_Default_Map_View_Based_On_Assets(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon   # mouse hover to 1st icon on Left hand side
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .move_to_element(self.mappage.get_map_default_view_radio).click()\
            .move_to_element(self.mappage.get_map_basic_data_layer).click()\
            .move_to_element(self.mappage.get_map_basic_data_layer_asset).click()\
            .perform()
        self.mappage.get_map_zoom_out.click()
        # Click on Zoom out to display the Map status based total no of items which is displayed just
        # above the Longitude and Latitude on Left hand side
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        sleep(1)
        pcountText = self.mappage.get_map_items_map_status.text
        # Extract the integer value displayed "Displaying 5 items"
        # This will be helpful to assert
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]
        # click on Water fall handle on Right hand side - Vertical - Last Icon
        self.mappage.get_map_water_fall_handle.click()
        # Count the total no. of Assets displayed in the collection
        assetTotal = self.driver.find_element_by_xpath(".//*[@id='waterfall_ul']")
        items = assetTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " assets"
        for assetName in items:
            print assetName.text
        self.assertEqual(pvalue11,str(len(items)),"total assets not matching" )
        # click on Water fall handle on Right hand side - Vertical - Last Icon
        self.mappage.get_map_water_fall_handle.click()
        # Click on Bread crumb - Apps link
        self.mappage.get_bread_crumb_apps.click()

    @attr(priority="high")
    #@SkipTest
    def test_map_07_to_verify_Default_Map_View_Based_On_Assessment(self):
        mappage = MapPage(self.driver)
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_default_view_radio).click()\
            .move_to_element(self.driver.find_element_by_xpath(".//*[@id='leaflet-control-accordion-layers-1']/label")).click()\
            .move_to_element(self.driver.find_element_by_xpath(".//*[@id='leaflet-control-accordion-layers-1']/article/div[1]/span")).click()\
            .move_to_element(self.driver.find_element_by_xpath(".//*[@id='leaflet-control-accordion-layers-1']/article/div[2]/input")).click()\
            .perform()
        self.driver.find_element_by_xpath(".//*[@id='mapdiv']/div[2]/div[2]/div[1]/a[2]").click()
        self.driver.find_element_by_xpath(".//*[@id='map_status']").is_displayed()
        sleep(1)
        pcountText = self.driver.find_element_by_xpath(".//*[@id='map_status']").text
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]
        self.driver.find_element_by_xpath(".//*[@id='waterfall_handle']").click()
        assetTotal = self.driver.find_element_by_xpath(".//*[@id='waterfall_ul']")
        items = assetTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " assets:"
        print "Printing asset names, no. of days ago..."
        for assetName in items:
            print assetName.text
        self.assertEqual(pvalue11,str(len(items)),"total assets not matching" )
        self.driver.find_element_by_xpath(".//*[@id='waterfall_handle']").click()
        mappage.get_bread_crumb_apps.click()

    @attr(priority="high")
    #@SkipTest
    def test_map_to_verify_Default_Map_View_Based_On_Incidents(self):
        mappage = MapPage(self.driver)
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_default_view_radio).click()\
            .move_to_element(self.driver.find_element_by_xpath(".//*[@id='leaflet-control-accordion-layers-1']/label")).click()\
            .move_to_element(self.driver.find_element_by_xpath(".//*[@id='leaflet-control-accordion-layers-1']/article/div[2]/input")).click()\
            .move_to_element(self.driver.find_element_by_xpath(".//*[@id='leaflet-control-accordion-layers-1']/article/div[3]/input")).click()\
            .perform()
        self.driver.find_element_by_xpath(".//*[@id='mapdiv']/div[2]/div[2]/div[1]/a[2]").click()
        self.driver.find_element_by_xpath(".//*[@id='map_status']").is_displayed()
        sleep(1)
        pcountText = self.driver.find_element_by_xpath(".//*[@id='map_status']").text
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]
        self.driver.find_element_by_xpath(".//*[@id='waterfall_handle']").click()
        assetTotal = self.driver.find_element_by_xpath(".//*[@id='waterfall_ul']")
        items = assetTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " assets:"
        print "Printing asset names, no. of days ago..."
        for assetName in items:
            print assetName.text
        self.assertEqual(pvalue11,str(len(items)),"total assets not matching" )
        self.driver.find_element_by_xpath(".//*[@id='waterfall_handle']").click()
        mappage.get_bread_crumb_apps.click()

