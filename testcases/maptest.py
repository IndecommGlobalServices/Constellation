__author__ = 'Deepa.Sivadas'
from testcases.basetestcase import BaseTestCase
from pages.mappage import MapPage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from selenium.webdriver.common.keys import Keys
from pages.basepage import InvalidPageException
import sys

class MapPageTest(BaseTestCase):

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.mappage = MapPage(self.driver)



    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()

        try:
            if self.driver.find_element_by_xpath(".//*[@id='error_modal' and @hide-modal='' and @aria-hidden='false']").is_displayed():
                self.driver.find_element_by_xpath(".//*[@id='error_modal']/div/div/form/div[2]/button").click()
                print "Server Error 500 - Something has gone terribly wrong."
        except Exception :
            pass

    # All maps in one test case
    @attr(priority="high")
    def test_map_01_05_to_verify_all_maps(self):
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .perform()
        self.mappage.get_map_default_view_radio.click()
        sleep(2)
        self.mappage.get_map_night_view_radio.click()
        sleep(2)
        self.mappage.get_map_terrain_radio.click()
        sleep(2)
        self.mappage.get_map_satelite_default_view_radio.click()
        sleep(2)
        self.mappage.get_map_satelite_grey_view_radio.click()
        sleep(2)
        self.mappage.return_to_icon_list_page()
        sleep(2)

    @attr(priority="high")
    #@SkipTest
    def test_map_06_to_verify_Default_Map_View_Based_On_Assets(self):
        try:

            sleep(5)
            if self.mappage.get_map_water_fall_scrollable.is_displayed():
                self.mappage.get_map_water_fall_handle.click()
            sleep(5)
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon   # mouse hover to 1st icon on Left hand side
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .move_to_element(self.mappage.get_map_base_map_accordian).click()\
                .perform()

            self.mappage.get_map_default_view_radio.click()
            sleep(1)
            self.mappage.get_map_basic_data_layer.click()
            sleep(1)
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            sleep(5)

            self.mappage.get_map_basic_data_layer_asset.click()
            sleep(5)
            self.mappage.get_map_zoom_out.click()
            sleep(10)
            # Click on Zoom out to display the Map status based total no of items which is displayed just
            # above the Longitude and Latitude on Left hand side
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            sleep(1)
            # Extract the integer value displayed "Eg : Displaying 5 items"
            # This will be helpful to assert
            map_assets_count = self.mappage.get_total_map_status_count()
            print "Found " + str(map_assets_count) + " map status asset count"
            # click on Water fall handle on Right hand side - Vertical - Last Icon
            self.mappage.get_map_water_fall_handle.click()
            # Count the total no. of Assets displayed in the collection
            assetTotal = self.mappage.get_map_water_fall_list
            items = assetTotal.find_elements_by_tag_name("li")
            print "Found " + str(len(items)-1) + " assets"
            self.assertEqual(map_assets_count,len(items)-1,"total assets not matching" )
            # click on Water fall handle on Right hand side - Vertical - Last Icon
            self.mappage.get_map_water_fall_handle.click()
            self.mappage.return_to_icon_list_page()
            sleep(2)
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_07_to_verify_Default_Map_View_Based_On_Assessment(self):
        try:
            sleep(5)
            if self.mappage.get_map_water_fall_scrollable.is_displayed():
                sleep(2)
                self.mappage.get_map_water_fall_handle.click()
            sleep(5)
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .move_to_element(self.mappage.get_map_base_map_accordian).click()\
                .perform()

            self.mappage.get_map_default_view_radio.click()
            sleep(1)
            self.mappage.get_map_basic_data_layer.click()
            sleep(1)
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            sleep(5)

            self.mappage.get_map_basic_data_layer_assessment.click()
            sleep(5)
            self.mappage.get_map_zoom_out.click()
            sleep(10)
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            sleep(1)
            map_assessment_count = self.mappage.get_total_map_status_count()
            print "Found " + str(map_assessment_count) + " map status assessment count"
            self.mappage.get_map_water_fall_handle.click()
            assessmentTotal = self.mappage.get_map_water_fall_list
            items = assessmentTotal.find_elements_by_tag_name("li")
            print "Found " + str(len(items)-1) + " assessment"
            self.assertEqual(map_assessment_count,len(items)-1,"total assessment not matching" )
            self.mappage.get_map_water_fall_handle.click()
            self.mappage.return_to_icon_list_page()
            sleep(2)
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_08_to_verify_Default_Map_View_Based_On_Incidents(self):
        sleep(5)
        if self.mappage.get_map_water_fall_scrollable.is_displayed():
            self.mappage.get_map_water_fall_handle.click()
        sleep(5)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .perform()

        self.mappage.get_map_default_view_radio.click()
        sleep(1)
        self.mappage.get_map_basic_data_layer.click()
        sleep(1)
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        sleep(5)

        self.mappage.get_map_basic_data_layer_incident.click()
        sleep(5)
        self.mappage.get_map_zoom_out.click()
        sleep(10)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        sleep(1)
        map_incident_count = self.mappage.get_total_map_status_count()
        print "Found " + str(map_incident_count) + " map status incident count"
        self.mappage.get_map_water_fall_handle.click()
        incidentTotal = self.mappage.get_map_water_fall_list
        items = incidentTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)-1) + " incident"
        self.assertEqual(map_incident_count,len(items)-1,"total incident not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.return_to_icon_list_page()
        sleep(2)

    @attr(priority="high")
    #@SkipTest
    def test_map_09_to_verify_Default_Map_View_Based_On_Threat_Streams(self):
        sleep(5)
        if self.mappage.get_map_water_fall_scrollable.is_displayed():
            self.mappage.get_map_water_fall_handle.click()
        sleep(5)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .perform()

        self.mappage.get_map_default_view_radio.click()
        sleep(1)
        self.mappage.get_map_basic_data_layer.click()
        sleep(1)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        sleep(5)
        self.mappage.get_map_basic_data_layer_threat_streams.click()
        sleep(5)
        self.mappage.get_map_zoom_out.click()
        sleep(10)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        sleep(1)
        map_threat_streams_count = self.mappage.get_total_map_status_count()
        print "Found " + str(map_threat_streams_count) + " map status threat streams count"
        self.mappage.get_map_water_fall_handle.click()
        threatstreamsTotal = self.mappage.get_map_water_fall_list
        items = threatstreamsTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)-1) + " threat streams"
        self.assertEqual(map_threat_streams_count,len(items)-1,"total threat streams not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.return_to_icon_list_page()
        sleep(2)

    @attr(priority="high")
    #@SkipTest
    def test_map_10_to_verify_Default_Map_View_Based_On_Indicator_Teams(self):
        sleep(5)
        if self.mappage.get_map_water_fall_scrollable.is_displayed():
            self.mappage.get_map_water_fall_handle.click()
        sleep(5)
        mouse_hover_field = self.mappage.get_map_mouse_hover_icon
        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(self.mappage.get_map_base_map_accordian).click()\
            .perform()

        self.mappage.get_map_default_view_radio.click()
        sleep(1)
        self.mappage.get_map_basic_data_layer.click()
        sleep(1)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        self.mappage.get_checking_and_unchecking_basic_data_layer()
        self.mappage.get_map_basic_data_layer_indicator_teams.click()
        sleep(5)
        self.mappage.get_map_zoom_out.click()
        sleep(10)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        sleep(1)
        map_indicator_teams_streams_count = self.mappage.get_total_map_status_count()
        print "Found " + str(map_indicator_teams_streams_count) + " map status indicator teams count"
        self.mappage.get_map_water_fall_handle.click()
        indicatorteamsTotal = self.mappage.get_map_water_fall_list
        items = indicatorteamsTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)-1) + " indicator teams"
        self.assertEqual(map_indicator_teams_streams_count,len(items)-1,"total indicator teams not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.return_to_icon_list_page()
        sleep(2)

    @attr(priority="high")
    #@SkipTest
    def test_map_11_to_verify_Default_Map_View_Based_On_Annotations(self):
        sleep(2)
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
        sleep(5)
        self.mappage.get_map_zoom_out.click()
        sleep(10)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        sleep(1)
        map_annotations_count = self.mappage.get_total_map_status_count()
        print "Found " + str(map_annotations_count) + " map status annotations count"
        self.mappage.get_map_water_fall_handle.click()
        annotationsTotal = self.mappage.get_map_water_fall_list
        items = annotationsTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)-1) + " annotations"
        self.assertEqual(map_annotations_count,len(items)-1,"total annotations not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.return_to_icon_list_page()
        sleep(2)

    @attr(priority="high")
    #@SkipTest
    def test_map_12_to_verify_Default_Map_View_Based_On_Threat_Streams_Trending_Last_Day(self):
        sleep(2)
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
        sleep(5)
        self.mappage.get_map_zoom_out.click()
        sleep(10)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        sleep(1)
        map_threat_streams_trending_last_day_count = self.mappage.get_total_map_status_count()
        print "Found " + str(map_threat_streams_trending_last_day_count) + \
              " map status threat streams trending last day count"
        self.mappage.get_map_water_fall_handle.click()
        threatstreamstrendinglastdayTotal = self.mappage.get_map_water_fall_list
        items = threatstreamstrendinglastdayTotal.find_elements_by_tag_name("li")
        print "Found " + str(len(items)-1) + " threat streams trending last day"
        self.assertEqual(map_threat_streams_trending_last_day_count,len(items)-1,
                         "total threat streams trending last day not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.return_to_icon_list_page()
        sleep(2)

    @attr(priority="high")
    #@SkipTest
    def test_map_13_to_verify_Default_Map_View_Based_On_Threat_Streams_Stream_1(self):
        sleep(2)
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
        sleep(5)
        self.mappage.get_map_zoom_out.click()
        sleep(10)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        sleep(1)
        map_threat_streams_stream_1_count = self.mappage.get_total_map_status_count()
        print "Found " + str(map_threat_streams_stream_1_count) + " map status threat streams stream 1 count"
        self.mappage.get_map_water_fall_handle.click()
        threatstreamsstream1Total = self.mappage.get_map_water_fall_list
        items = threatstreamsstream1Total.find_elements_by_tag_name("li")
        print "Found " + str(len(items)-1) + " threat streams stream 1"
        self.assertEqual(map_threat_streams_stream_1_count,len(items)-1,"total threat streams stream 1 not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.return_to_icon_list_page()
        sleep(2)

    @attr(priority="high")
    #@SkipTest
    def test_map_14_to_verify_Default_Map_View_Based_On_Threat_Streams_Stream_2(self):
        sleep(2)
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
        sleep(5)
        self.mappage.get_map_zoom_out.click()
        sleep(10)
        self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
        sleep(1)
        map_threat_streams_stream_2_count = self.mappage.get_total_map_status_count()
        print "Found " + str(map_threat_streams_stream_2_count) + " map status threat streams stream 2 count"
        self.mappage.get_map_water_fall_handle.click()
        threatstreamsstream2Total = self.mappage.get_map_water_fall_list
        items = threatstreamsstream2Total.find_elements_by_tag_name("li")
        print "Found " + str(len(items)-1) + " threat streams stream 2"
        self.assertEqual(map_threat_streams_stream_2_count,len(items)-1,"total threat streams stream 2 not matching" )
        self.mappage.get_map_water_fall_handle.click()
        self.mappage.return_to_icon_list_page()
        sleep(2)