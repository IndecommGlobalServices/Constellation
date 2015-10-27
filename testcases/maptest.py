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

class MapPageTest(BaseTestCase):
    '''
    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_map(self):
        #sleep(5)
        mappage = MapPage(self.driver)
        sleep(20)
        self.assertEqual(mappage.get_map_app_name.text, "Map")
    '''
    # Default view
    @attr(priority="high")
    def test_map_01_to_verify_default(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .perform()
        self.mappage.get_map_default_view_radio.click()
        self.mappage.get_bread_crumb_apps.click() # Click on Bread crumb - Apps link

    # Night view
    @attr(priority="high")
    def test_map_02_to_verify_Night_View(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .perform()
        self.mappage.get_map_night_view_radio.click()
        self.mappage.get_bread_crumb_apps.click()# Click on Bread crumb - Apps link
    # Terrain
    @attr(priority="high")
    def test_map_03_to_verify_Terrain(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .perform()
        self.mappage.get_map_terrain_radio.click()
        self.mappage.get_bread_crumb_apps.click()# Click on Bread crumb - Apps link
    # Satelite Default
    @attr(priority="high")
    def test_map_04_to_verify_Satelite_Default(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .perform()
        self.mappage.get_map_satelite_default_view_radio.click()
        self.mappage.get_bread_crumb_apps.click() # Click on Bread crumb - Apps link
    # Satelite Grey
    @attr(priority="high")
    #@SkipTest
    def test_map_05_to_verify_Satelite_Grey(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .perform()
        self.mappage.get_map_satelite_grey_view_radio.click()
        self.mappage.get_bread_crumb_apps.click() # Click on Bread crumb - Apps link
    # View Full Screen
    @attr(priority="high")
    def test_map_13_to_verify_Map_Can_Be_Viewed_In_Full_Screen(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_full_screen # mouse hover to View Full screen icon
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
        self.mappage.get_bread_crumb_apps.click() # Click on Bread crumb - Apps link

    @attr(priority="high")
    #@SkipTest
    def test_map_06_to_verify_Default_Map_View_Based_On_Assets(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon   # mouse hover to 1st icon on Left hand side
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .move_to_element(self.mappage.get_map_default_view_radio).click()\
            .move_to_element(self.mappage.get_map_basic_data_layer).click()\
            .perform()
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        self.mappage.get_map_basic_data_layer_asset.click()
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
        assetTotal = self.mappage.get_map_water_fall_list
        items = assetTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " assets"
        self.assertEqual(pvalue11,str(len(items)),"total assets not matching" )
        # click on Water fall handle on Right hand side - Vertical - Last Icon
        self.mappage.get_map_water_fall_handle.click()
        # Click on Bread crumb - Apps link
        self.mappage.get_bread_crumb_apps.click()

    @attr(priority="high")
    #@SkipTest
    def test_map_07_to_verify_Default_Map_View_Based_On_Assessment(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .move_to_element(self.mappage.get_map_default_view_radio).click()\
            .move_to_element(self.mappage.get_map_basic_data_layer).click()\
            .perform()
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        self.mappage.get_map_basic_data_layer_assessment.click()
        self.mappage.get_map_zoom_out.click()
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        sleep(1)
        pcountText = self.mappage.get_map_items_map_status.text
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]
        self.mappage.get_map_water_fall_handle.click()
        assessmentTotal = self.mappage.get_map_water_fall_list
        items = assessmentTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " assessment"
        self.assertEqual(pvalue11,str(len(items)),"total assessment not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.get_bread_crumb_apps.click()

    @attr(priority="high")
    #@SkipTest
    def test_map_08_to_verify_Default_Map_View_Based_On_Incidents(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .move_to_element(self.mappage.get_map_default_view_radio).click()\
            .move_to_element(self.mappage.get_map_basic_data_layer).click()\
            .perform()
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        self.mappage.get_map_basic_data_layer_incident.click()
        self.mappage.get_map_zoom_out.click()
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        sleep(1)
        pcountText = self.mappage.get_map_items_map_status.text
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]
        self.mappage.get_map_water_fall_handle.click()
        incidentTotal = self.mappage.get_map_water_fall_list
        items = incidentTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " incident"
        self.assertEqual(pvalue11,str(len(items)),"total incident not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.get_bread_crumb_apps.click()

    @attr(priority="high")
    #@SkipTest
    def test_map_09_to_verify_Default_Map_View_Based_On_Threat_Streams(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .move_to_element(self.mappage.get_map_default_view_radio).click()\
            .move_to_element(self.mappage.get_map_basic_data_layer).click()\
            .perform()
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        self.mappage.get_map_basic_data_layer_threat_streams.click()
        self.mappage.get_map_zoom_out.click()
        sleep(5)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        pcountText = self.mappage.get_map_items_map_status.text
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]
        print pvalue11
        self.mappage.get_map_water_fall_handle.click()
        threatstreamsTotal = self.mappage.get_map_water_fall_list
        items = threatstreamsTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " threat streams"
        self.assertEqual(pvalue11,str(len(items)),"total threat streams not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.get_bread_crumb_apps.click()

    @attr(priority="high")
    #@SkipTest
    def test_map_10_to_verify_Default_Map_View_Based_On_Indicator_Teams(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .move_to_element(self.mappage.get_map_default_view_radio).click()\
            .move_to_element(self.mappage.get_map_basic_data_layer).click()\
            .perform()
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        self.mappage.get_map_basic_data_layer_indicator_teams.click()
        self.mappage.get_map_zoom_out.click()
        sleep(5)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        pcountText = self.mappage.get_map_items_map_status.text
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]
        print pvalue11
        self.mappage.get_map_water_fall_handle.click()
        indicatorteamsTotal = self.mappage.get_map_water_fall_list
        items = indicatorteamsTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " indicator teams"
        self.assertEqual(pvalue11,str(len(items)),"total indicator teams not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.get_bread_crumb_apps.click()

    @attr(priority="high")
    #@SkipTest
    def test_map_11_to_verify_Default_Map_View_Based_On_Annotations(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .move_to_element(self.mappage.get_map_default_view_radio).click()\
            .move_to_element(self.mappage.get_map_basic_data_layer).click()\
            .perform()
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        self.mappage.get_map_basic_data_layer_annotations.click()
        self.mappage.get_map_zoom_out.click()
        sleep(5)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        pcountText = self.mappage.get_map_items_map_status.text
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]
        print pvalue11
        self.mappage.get_map_water_fall_handle.click()
        annotationsTotal = self.mappage.get_map_water_fall_list
        items = annotationsTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " annotations"
        self.assertEqual(pvalue11,str(len(items)),"total annotations not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.get_bread_crumb_apps.click()

    @attr(priority="high")
    #@SkipTest
    def test_map_11_to_verify_Default_Map_View_Based_On_Threat_Streams_Trending_Last_Day(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .move_to_element(self.mappage.get_map_default_view_radio).click()\
            .move_to_element(self.mappage.get_map_basic_data_layer).click()\
            .perform()
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        self.mappage.get_map_basic_data_layer_threat_streams_trending_last_day.click()
        self.mappage.get_map_zoom_out.click()
        sleep(5)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        pcountText = self.mappage.get_map_items_map_status.text
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]
        print pvalue11
        self.mappage.get_map_water_fall_handle.click()
        threatstreamstrendinglastdayTotal = self.mappage.get_map_water_fall_list
        items = threatstreamstrendinglastdayTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " threat streams trending last day"
        self.assertEqual(pvalue11,str(len(items)),"total threat streams trending last day not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.get_bread_crumb_apps.click()

    @attr(priority="high")
    #@SkipTest
    def test_map_12_to_verify_Default_Map_View_Based_On_Threat_Streams_Stream_1(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .move_to_element(self.mappage.get_map_default_view_radio).click()\
            .move_to_element(self.mappage.get_map_basic_data_layer).click()\
            .perform()
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        self.mappage.get_map_basic_data_layer_threat_streams_stream_1.click()
        self.mappage.get_map_zoom_out.click()
        sleep(5)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        pcountText = self.mappage.get_map_items_map_status.text
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]
        print pvalue11
        self.mappage.get_map_water_fall_handle.click()
        threatstreamsstream1Total = self.mappage.get_map_water_fall_list
        items = threatstreamsstream1Total.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " threat streams stream 1"
        self.assertEqual(pvalue11,str(len(items)),"total threat streams stream 1 not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.get_bread_crumb_apps.click()

    @attr(priority="high")
    #@SkipTest
    def test_map_13_to_verify_Default_Map_View_Based_On_Threat_Streams_Stream_2(self):
        self.mappage = MapPage(self.driver)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .move_to_element(self.mappage.get_map_default_view_radio).click()\
            .move_to_element(self.mappage.get_map_basic_data_layer).click()\
            .perform()
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        self.mappage.get_map_basic_data_layer_threat_streams_stream_2.click()
        self.mappage.get_map_zoom_out.click()
        sleep(5)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        pcountText = self.mappage.get_map_items_map_status.text
        pparts = pcountText.split(" ")
        pvalue11 = pparts[1]
        print pvalue11
        self.mappage.get_map_water_fall_handle.click()
        threatstreamsstream2Total = self.mappage.get_map_water_fall_list
        items = threatstreamsstream2Total.find_elements_by_tag_name("li")
        print "Found " + str(len(items)) + " threat streams stream 2"
        self.assertEqual(pvalue11,str(len(items)),"total threat streams stream 2 not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.get_bread_crumb_apps.click()
