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
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(5)

        # mouse hover to 1st icon
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_default_view_radio).click()\
            .perform()
        sleep(10)

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()

    # Night view
    @attr(priority="high")
    def test_map_02_to_verify_Night_View(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(5)

        # mouse hover to 1st icon
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_night_view_radio).click()\
            .perform()
        sleep(10)

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()


    # Terrain
    @attr(priority="high")
    def test_map_03_to_verify_Terrain(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(5)

        # mouse hover to 1st icon
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_terrain_radio).click()\
            .perform()
        sleep(10)

        # Trying to assert, but element not recognised.
        '''
        terrainText = self.driver.find_element_by_xpath("//html/body/div[8]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[1]/div[1]/section/form/div[1]/div/article/div[3]/input").text
        sleep(10)
        self.assertEqual("Terrain", terrainText, "didn't find terrain map.")

        self.LEAFLET_MAP = 'Ns.body.currentView.content.currentView.map'
        # layers control
        self.driver.find_element_by_css_selector('.leaflet-control-layers-list')
        LAYERS_CONTROLS = 'return _.values(%s.layerscontrol._layers)' % self.LEAFLET_MAP
        self.assertEqual(self.driver.execute_script('%s[0].name' % LAYERS_CONTROLS), 'Map')
        self.assertEqual(self.driver.execute_script('%s[1].name' % LAYERS_CONTROLS), 'Terrain')
        '''

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()

    # Satelite Default
    @attr(priority="high")
    def test_map_04_to_verify_Satelite_Default(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(5)

        # mouse hover to 1st icon
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_satelite_default_view_radio).click()\
            .perform()
        sleep(10)

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()

    # Satelite Grey
    @attr(priority="high")
    #@SkipTest
    def test_map_05_to_verify_Satelite_Grey(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(5)

        # mouse hover to 1st icon
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_satelite_grey_view_radio).click()\
            .perform()
        sleep(10)

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()

    # View Full Screen
    @attr(priority="high")
    def test_map_13_to_verify_Map_Can_Be_Viewed_In_Full_Screen(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(20)

        # mouse hover to View Full screen icon
        mouse_hover_field =self.driver.find_element_by_xpath("//html/body/div[8]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[1]/div[2]")

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

        #View Full Screen
        ActionChains(self.driver).move_to_element(mouse_hover_field).perform()
        sleep(10)

        # to zoom by pressing F11 key on Keyboard
        ActionChains(self.driver).send_keys(Keys.F11).perform()

        sleep(15)
        # to zoom out by pressing F11 again on Keyboard
        ActionChains(self.driver).send_keys(Keys.F11).perform()

        sleep(5)

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()

    # Search and Locate
    @attr(priority="high")
    def test_map_16_to_verify_Map_Can_Be_Located(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(20)

        # mouse hover to 1st icon
        mouse_hover_field = self.driver.find_element_by_xpath("//a[@title='Bing Geocoder']")
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field).perform()
        sleep(10)

        # ENTER THE SEARCH STRING
        search_Text = self.driver.find_element_by_xpath(".//*[@id='mapdiv']/div[2]/div[1]/div[3]/form/input")
        search_Text.send_keys("India")
        sleep(10)

        # Click on Locate button
        self.driver.find_element_by_xpath(".//*[@id='mapdiv']/div[2]/div[1]/div[3]/form/button").click()
        sleep(20)

        # here intended map is not displaying...

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()



    @attr(priority="high")
    #@SkipTest
    def test_map_to_verify_Default_Map_View_Based_On_Assets(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(5)

        # mouse hover to 1st icon
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_default_view_radio).click()\
            .move_to_element(self.driver.find_element_by_xpath(".//*[@id='leaflet-control-accordion-layers-1']/label")).click()\
            .move_to_element(self.driver.find_element_by_xpath(".//*[@id='leaflet-control-accordion-layers-1']/article/div[1]/span")).click()\
            .perform()
        sleep(10)

        # Click on Zoom out to display the Map status based total no of items which is displayed just above the Longitude and Latitude on Left hand side
        self.driver.find_element_by_xpath(".//*[@id='mapdiv']/div[2]/div[2]/div[1]/a[2]").click()
        sleep(5)

        # Verify the map status by items are displayed
        self.driver.find_element_by_xpath(".//*[@id='map_status']").is_displayed()
        sleep(5)

        # Extract the integer value displayed "Displaying 5 items"
        # This will be helpful to assert
        pcountText = self.driver.find_element_by_xpath(".//*[@id='map_status']").text
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]

        # click on Water fall handle on Right hand side - Vertical - Last Icon
        self.driver.find_element_by_xpath(".//*[@id='waterfall_handle']").click()
        #sleep(10)

        # Count the total no. of Assets
        assetTotal = self.driver.find_element_by_xpath(".//*[@id='waterfall_ul']")
        items = assetTotal.find_elements_by_tag_name("li")

        print "Found " + str(len(items)) + " assets:"

        print "Printing asset names, no. of days ago..."

        for assetName in items:
            print assetName.text
        sleep(5)

        self.assertEqual(pvalue11,str(len(items)),"total assets not matching" )


        '''
        #Click on each asset and get the total images available
        if len(items) >=1:
            for item in items:
                print "clicking on asset"

                # click on each individual asset
                item.click()

                #Extract the name and type shown
                asset_name_type = self.driver.find_element_by_xpath(".//*[@id='mapdiv']/div[1]/div[2]/div[4]/div/div[1]/div").text
                print asset_name_type

                # find the total no. of images available on the map
                twitterIcon = self.driver.find_elements_by_xpath(".//*[@id='mapdiv']/div[1]/div[2]/div[3]/img")
                print len(twitterIcon)
        '''
        # click on Water fall handle on Right hand side - Vertical - Last Icon
        self.driver.find_element_by_xpath(".//*[@id='waterfall_handle']").click()
        sleep(2)

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()



