from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'Deepa.Sivadas'
from testcases.basetestcase import BaseTestCase
from pages.mappage import MapPage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from selenium.webdriver.common.keys import Keys
from random import randint

from selenium.common.exceptions import NoSuchElementException

class MapPageTest(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(MapPageTest, self).setUpClass()
        self.mappage = MapPage(self.driver)

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.mappage.open_map_app()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        try:
            if self.mappage.get_map_404.is_displayed():
                self.mappage.get_map_404_close.click()
                print "Server Error 500 - Something has gone terribly wrong."
        except Exception :
            pass
        self.mappage.return_to_apps_main_page()


    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_map_smoke(self):
        self.assertTrue(self.mappage.get_map_water_fall_scrollable.is_displayed(), "Map is not loaded fully")


    # All maps in one test case
    @attr(priority="high")
    #@SkipTest
    def test_map_01_05_to_verify_all_maps(self):
        try:

            if self.mappage.get_map_water_fall_scrollable.is_displayed():
                self.mappage.get_map_water_fall_handle.click()

            sleep(2)
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon # mouse hover to 1st icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_night_view_radio.click()
            self.mappage.get_map_terrain_radio.click()
            self.mappage.get_map_satelite_default_view_radio.click()
            self.mappage.get_map_satelite_grey_view_radio.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_06_to_verify_Default_Map_View_Based_On_Assets(self):
        try:
            self.driver.refresh()
            sleep(10)
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon   # mouse hover to 1st icon on Left hand side
            sleep(10)
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            sleep(10)
            self.mappage.get_map_base_map_accordian.click()
            sleep(10)
            self.mappage.get_map_default_view_radio.click()
            sleep(10)
            self.mappage.get_map_basic_data_layer.click()
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_UP)
            sleep(2)
            self.mappage.get_map_basic_data_layer_asset.click()
            sleep(2)
            self.mappage.get_map_zoom_out.click()
            sleep(10)
            # Click on Zoom out to display the Map status based total no of items which is displayed just
            # above the Longitude and Latitude on Left hand side
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            # click on Water fall handle on Right hand side - Vertical - Last Icon
            self.mappage.get_map_water_fall_handle.click()
            # Count the total no. of Assets displayed in the collection
            assetTotal = self.mappage.get_map_water_fall_list
            items = assetTotal.find_elements_by_tag_name("li")
            print "Found " + str(len(items)-1) + " assets"





            # Extract the integer value displayed "Eg : Displaying 5 items"
            # This will be helpful to assert
            map_assets_count = self.mappage.get_total_map_status_count()
            print "Found " + str(map_assets_count) + " map status asset count"

            self.assertEqual(map_assets_count,len(items)-1,"total assets not matching" )
            # click on Water fall handle on Right hand side - Vertical - Last Icon
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise


    @attr(priority="high")
    #@SkipTest
    def test_map_07_to_verify_Default_Map_View_Based_On_Assessment(self):
        try:
            self.driver.refresh()
            sleep(10)
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            sleep(10)
            self.mappage.get_map_base_map_accordian.click()
            sleep(10)
            self.mappage.get_map_default_view_radio.click()
            sleep(2)
            self.mappage.get_map_basic_data_layer.click()
            sleep(2)
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            sleep(2)
            self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_UP)
            self.mappage.get_map_scroll.send_keys(Keys.ARROW_UP)
            self.mappage.get_map_basic_data_layer_assessment.click()
            sleep(2)
            self.mappage.get_map_zoom_out.click()
            sleep(10)
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            sleep(10)
            map_assessment_count = self.mappage.get_total_map_status_count()
            sleep(10)
            print "Found " + str(map_assessment_count) + " map status assessment count"
            self.mappage.get_map_water_fall_handle.click()
            sleep(10)
            assessmentTotal = self.mappage.get_map_water_fall_list
            sleep(10)
            items = assessmentTotal.find_elements_by_tag_name("li")
            sleep(10)
            print "Found " + str(len(items)-1) + " assessment"
            self.assertEqual(map_assessment_count,len(items)-1,"total assessment not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_08_to_verify_Default_Map_View_Based_On_Incidents(self):
        try:
            self.driver.refresh()
            sleep(10)
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            sleep(5)
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                    .perform()
            sleep(5)
            self.mappage.get_map_base_map_accordian.click()
            sleep(5)
            self.mappage.get_map_default_view_radio.click()
            sleep(5)
            self.mappage.get_map_basic_data_layer.click()
            sleep(5)
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            sleep(5)
            self.mappage.get_map_basic_data_layer_incident.click()
            sleep(5)
            self.mappage.get_map_zoom_out.click()
            sleep(10)
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            sleep(10)
            map_incident_count = self.mappage.get_total_map_status_count()
            sleep(10)
            print "Found " + str(map_incident_count) + " map status incident count"
            self.mappage.get_map_water_fall_handle.click()
            sleep(10)
            incidentTotal = self.mappage.get_map_water_fall_list
            sleep(10)
            items = incidentTotal.find_elements_by_tag_name("li")
            sleep(10)
            print "Found " + str(len(items)-1) + " incident"
            self.assertEqual(map_incident_count,len(items)-1,"total incident not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_09_to_verify_Default_Map_View_Based_On_Indicator_Teams(self):
        try:
            self.driver.refresh()
            sleep(10)
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            sleep(5)
            self.mappage.get_map_base_map_accordian.click()
            sleep(2)
            self.mappage.get_map_default_view_radio.click()
            sleep(2)
            self.mappage.get_map_basic_data_layer.click()
            sleep(2)

            self.mappage.get_checking_and_unchecking_basic_data_layer()
            sleep(2)

            self.mappage.get_map_basic_data_layer_indicator_teams.click()
            sleep(2)
            self.mappage.get_map_zoom_out.click()
            sleep(10)
            self.mappage.get_map_water_fall_handle.click()
            sleep(10)
            indicatorteamsTotal = self.mappage.get_map_water_fall_list
            sleep(10)
            items = indicatorteamsTotal.find_elements_by_tag_name("li")
            sleep(10)
            print "Found " + str(len(items)-1) + " indicator teams"
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            sleep(10)
            map_indicator_teams_count = self.mappage.get_total_map_status_count()
            sleep(10)
            print "Found " + str(map_indicator_teams_count) + " map status indicator teams count"
            self.assertEqual(map_indicator_teams_count,len(items)-1,"total indicator teams not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_10_to_verify_Default_Map_View_Based_On_Field_Interviews(self):
        try:
            self.driver.refresh()
            sleep(10)

            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()

            self.mappage.get_checking_and_unchecking_basic_data_layer()

            self.mappage.get_map_basic_data_layer_field_interviews.click()
            self.mappage.get_map_zoom_out.click()
            sleep(10)
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            sleep(10)
            map_field_interviews_count = self.mappage.get_total_map_status_count()
            sleep(10)
            print "Found " + str(map_field_interviews_count) + " map status field interviews count"
            self.mappage.get_map_water_fall_handle.click()
            sleep(10)
            fieldinterviewsTotal = self.mappage.get_map_water_fall_list
            sleep(10)
            items = fieldinterviewsTotal.find_elements_by_tag_name("li")
            sleep(10)
            print "Found " + str(len(items)-1) + " field interviews"
            self.assertEqual(map_field_interviews_count,len(items)-1,"total field interviews not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise
    @attr(priority="high")
    #@SkipTest
    def test_map_11_to_verify_Default_Map_View_Based_On_Threat_Streams(self):
        try:
            self.driver.refresh()
            sleep(10)

            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()

            self.mappage.get_checking_and_unchecking_basic_data_layer()

            self.mappage.get_map_basic_data_layer_threat_streams.click()
            self.mappage.get_map_zoom_out.click()
            sleep(5)

            self.mappage.get_map_water_fall_handle.click()
            sleep(10)
            threatstreamsTotal = self.mappage.get_map_water_fall_list
            sleep(10)
            items = threatstreamsTotal.find_elements_by_tag_name("li")

            ######################################

            for i in items:
                self.driver.find_element_by_id("waterfall_scrollable").send_keys(Keys.END)
                while i.text == "Show more items":
                    self.driver.find_element_by_link_text("Show more items").click()
                    sleep(10)
                    if i.text != "Show more items":
                        break
            else:
                print "No Show more items link is displayed"


            ####################################

            items = threatstreamsTotal.find_elements_by_tag_name("li")
            sleep(5)
            print "Found " + str(len(items)-1) + " threat streams"

            ##################################

            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            sleep(5)
            map_threat_streams_count = self.mappage.get_total_map_status_count()
            sleep(5)
            print "Found " + str(map_threat_streams_count) + " map status threat streams count"

            ################################

            self.assertEqual(map_threat_streams_count,len(items)-1,"total threat streams not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_12_to_verify_Default_Map_View_Based_On_Threat_Streams_Heat_Map(self):
        try:
            self.driver.refresh()
            sleep(10)
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                           .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()

            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_basic_data_layer_threat_streams_heat_map.click()
            self.mappage.get_map_zoom_out.click()
            sleep(10)
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            sleep(10)
            map_threat_streams_heat_map_count = self.mappage.get_total_map_status_count()
            print "Found " + str(map_threat_streams_heat_map_count) + \
                  " map status threat streams heat map count"
            self.mappage.get_map_water_fall_handle.click()
            sleep(10)
            threatstreamsheatmapTotal = self.mappage.get_map_water_fall_list
            sleep(10)
            items = threatstreamsheatmapTotal.find_elements_by_tag_name("li")
            sleep(10)
            print "Found " + str(len(items)-1) + " threat streams heat map"
            self.assertEqual(map_threat_streams_heat_map_count,len(items)-1,
                             "total threat streams heat map not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_13_to_verify_Default_Map_View_Based_On_Annotations(self):
        try:
            self.driver.refresh()
            sleep(10)
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()

            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_basic_data_layer_annotations.click()
            self.mappage.get_map_zoom_out.click()
            sleep(10)
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            sleep(10)
            map_annotations_count = self.mappage.get_total_map_status_count()
            sleep(10)
            print "Found " + str(map_annotations_count) + " map status annotations count"
            self.mappage.get_map_water_fall_handle.click()
            sleep(10)
            annotationsTotal = self.mappage.get_map_water_fall_list
            sleep(10)
            items = annotationsTotal.find_elements_by_tag_name("li")
            sleep(10)
            print "Found " + str(len(items)-1) + " annotations"
            self.assertEqual(map_annotations_count,len(items)-1,"total annotations not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_14_to_verify_tag_is_added_in_manage_filter(self):
        try:
            self.mappage.manage_filter_tags()
            new_asset_tag = self.mappage.get_map_tag_add_textbox
            self.assertTrue(new_asset_tag.is_displayed())
            add_button = self.mappage.get_map_tag_add_button
            self.assertTrue(add_button.is_displayed())

            # Enter text inside "Add a tag by using random value"
            tag_name = "Dallas" #+ str(randint(0000,9999))
            new_asset_tag.send_keys(tag_name)

            # Click on Add Tag
            add_button.click()
            sleep(5)

            tag_name = "lowa" #+ str(randint(0000,9999))
            new_asset_tag.send_keys(tag_name)

            # Click on Add Tag
            add_button.click()
            sleep(5)

            # Verify added tag
            last_element = self.mappage.get_map_tag_last_element.text
            self.assertEqual(tag_name.strip(),last_element.strip(), "Tag not added.")
            self.mappage.manage_filter_save()

        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_15_to_verify_tag_is_deleted_in_manage_filter(self):
        try:
            self.mappage.manage_filter_tags()
            new_asset_tag = self.mappage.get_map_tag_add_textbox
            self.assertTrue(new_asset_tag.is_displayed())
            add_button = self.mappage.get_map_tag_add_button
            self.assertTrue(add_button.is_displayed())
            tag_total_count = self.mappage.get_map_tag_total_count
            print "Found before delete " + str(len(tag_total_count)) + " tag"
            if tag_total_count >= 1:
                last_element = self.mappage.get_map_tag_last_element.text
                sleep(2)
                last_element_delete = self.mappage.get_map_tag_last_element_delete
                last_element_delete.click()
                print "Tag " + last_element + " deleted successfully."
            else:
                print "No Tags found to delete."

            tag_total_count1 = self.mappage.get_map_tag_total_count
            print "Found after delete " + str(len(tag_total_count1)) + " tag"

            self.assertNotEqual(tag_total_count, tag_total_count1, "count are same." )

            # Click on Save
            self.mappage.manage_filter_save()


        except Exception as e:
            print e
            raise