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
class MapPageTest(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(MapPageTest, self).setUpClass()
        self.mappage = MapPage(self.driver)
        self.mappage.logintoapp()

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.mappage.open_map_app()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        try:
            if self.mappage.get_map_404.is_displayed():
                self.mappage.get_map_404_close.click()
                #print "Server Error 500 - Something has gone terribly wrong."
        except Exception :
            pass
        self.mappage.return_to_apps_main_page()

    # All maps in one test case
    @attr(priority="high")
    @SkipTest
    def test_map_01_08_to_verify_all_maps(self):
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
            self.mappage.get_map_satelite_esri_world_view_radio.click()
            self.mappage.get_map_streets_view_radio.click()
            self.mappage.get_map_outdoor_view_radio.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_09_to_verify_Default_Map_View_Based_On_Assets(self):
        try:
            self.driver.refresh()
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon   # mouse hover to 1st icon on Left hand side
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_UP)
            self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_UP)
            self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_UP)
            self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_UP)
            self.mappage.get_map_basic_data_layer_asset.click()
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            # click on Water fall handle on Right hand side - Vertical - Last Icon
            self.mappage.get_map_water_fall_handle.click()
            # Count the total no. of Assets displayed in the collection
            assetTotal = self.mappage.get_map_water_fall_list
            items = assetTotal.find_elements_by_tag_name("li")
            map_assets_count = self.mappage.get_total_map_status_count()
            self.assertEqual(map_assets_count,len(items)-1,"total assets not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise


    @attr(priority="high")
    #@SkipTest
    def test_map_10_to_verify_Default_Map_View_Based_On_Assessment(self):
        try:
            self.driver.refresh()
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_sub_scroll.send_keys(Keys.ARROW_UP)
            self.mappage.get_map_scroll.send_keys(Keys.ARROW_UP)
            self.mappage.get_map_basic_data_layer_assessment.click()
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            # map_assessment_count = self.mappage.get_total_map_status_count()
            # self.mappage.get_map_water_fall_handle.click()
            # assessmentTotal = self.mappage.get_map_water_fall_list
            # items = assessmentTotal.find_elements_by_tag_name("li")
            # self.assertEqual(map_assessment_count,len(items)-1,"total assessment not matching" )
            # self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_11_to_verify_Default_Map_View_Based_On_Incidents(self):
        try:
            self.driver.refresh()
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                    .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_basic_data_layer_incident.click()
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            map_incident_count = self.mappage.get_total_map_status_count()
            self.mappage.get_map_water_fall_handle.click()
            incidentTotal = self.mappage.get_map_water_fall_list
            items = incidentTotal.find_elements_by_tag_name("li")
            self.assertEqual(map_incident_count,len(items)-1,"total incident not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_12_to_verify_Default_Map_View_Based_On_Indicator_Teams(self):
        try:
            self.driver.refresh()
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_basic_data_layer_indicator_teams.click()
            self.mappage.get_map_water_fall_handle.click()
            indicatorteamsTotal = self.mappage.get_map_water_fall_list
            items = indicatorteamsTotal.find_elements_by_tag_name("li")
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            map_indicator_teams_count = self.mappage.get_total_map_status_count()
            self.assertEqual(map_indicator_teams_count,len(items)-1,"total indicator teams not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_13_to_verify_Default_Map_View_Based_On_Field_Interviews(self):
        try:
            self.driver.refresh()
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_basic_data_layer_field_interviews.click()
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            map_field_interviews_count = self.mappage.get_total_map_status_count()
            self.mappage.get_map_water_fall_handle.click()
            fieldinterviewsTotal = self.mappage.get_map_water_fall_list
            items = fieldinterviewsTotal.find_elements_by_tag_name("li")
            self.assertEqual(map_field_interviews_count,len(items)-1,"total field interviews not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_14_to_verify_Default_Map_View_Based_On_Events(self):
        try:
            self.driver.refresh()
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_basic_data_layer_events.click()
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            eventsTotal_count = self.mappage.get_total_map_status_count()
            self.mappage.get_map_water_fall_handle.click()
            eventsTotal = self.mappage.get_map_water_fall_list
            items = eventsTotal.find_elements_by_tag_name("li")
            self.assertEqual(eventsTotal_count,len(items)-1,"total events not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_15_to_verify_Default_Map_View_Based_On_Threat_Streams(self):
        try:
            self.driver.refresh()
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_basic_data_layer_threat_streams.click()
            self.mappage.get_map_water_fall_handle.click()
            threatstreamsTotal = self.mappage.get_map_water_fall_list
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
                pass
            ####################################
            items = threatstreamsTotal.find_elements_by_tag_name("li")
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            map_threat_streams_count = self.mappage.get_total_map_status_count()
            ################################
            self.assertEqual(map_threat_streams_count,len(items)-1,"total threat streams not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_16_to_verify_Default_Map_View_Based_On_Threat_Streams_Heat_Map(self):
        try:
            self.driver.refresh()
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                           .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_basic_data_layer_threat_streams_heat_map.click()
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            map_threat_streams_heat_map_count = self.mappage.get_total_map_status_count()
            self.mappage.get_map_water_fall_handle.click()
            threatstreamsheatmapTotal = self.mappage.get_map_water_fall_list
            items = threatstreamsheatmapTotal.find_elements_by_tag_name("li")
            self.assertEqual(map_threat_streams_heat_map_count,len(items)-1,
                             "total threat streams heat map not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_17_to_verify_Default_Map_View_Based_On_Annotations(self):
        try:
            self.driver.refresh()
            mouse_hover_field = self.mappage.get_map_mouse_hover_icon
            ActionChains(self.driver).move_to_element(mouse_hover_field)\
                .perform()
            self.mappage.get_map_base_map_accordian.click()
            self.mappage.get_map_default_view_radio.click()
            self.mappage.get_map_basic_data_layer.click()
            self.mappage.get_checking_and_unchecking_basic_data_layer()
            self.mappage.get_map_basic_data_layer_annotations.click()
            self.mappage.get_map_items_map_status.is_displayed()# Verify the map status by items are displayed
            map_annotations_count = self.mappage.get_total_map_status_count()
            self.mappage.get_map_water_fall_handle.click()
            annotationsTotal = self.mappage.get_map_water_fall_list
            items = annotationsTotal.find_elements_by_tag_name("li")
            self.assertEqual(map_annotations_count,len(items)-1,"total annotations not matching" )
            self.mappage.get_map_water_fall_handle.click()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_18_to_verify_tag_is_added_in_manage_filter(self):
        try:
            self.mappage.manage_filter_tags()
            new_asset_tag = self.mappage.get_map_tag_add_textbox
            self.assertTrue(new_asset_tag.is_displayed())
            add_button = self.mappage.get_map_tag_add_button
            self.assertTrue(add_button.is_displayed())
            tag_name = "Dallas"
            new_asset_tag.send_keys(tag_name)
            add_button.click()
            sleep(5)
            tag_name = "lowa"
            new_asset_tag.send_keys(tag_name)
            add_button.click()
            sleep(5)
            last_element = self.mappage.get_map_tag_last_element.text
            self.assertEqual(tag_name.strip(),last_element.strip(), "Tag not added.")
            self.mappage.manage_filter_save()
        except Exception as e:
            print e
            raise

    @attr(priority="high")
    #@SkipTest
    def test_map_19_to_verify_tag_is_deleted_in_manage_filter(self):
        try:
            self.mappage.manage_filter_tags()
            new_asset_tag = self.mappage.get_map_tag_add_textbox
            self.assertTrue(new_asset_tag.is_displayed())
            add_button = self.mappage.get_map_tag_add_button
            self.assertTrue(add_button.is_displayed())
            tag_total_count = self.mappage.get_map_tag_total_count
            if tag_total_count >= 1:
                sleep(2)
                last_element_delete = self.mappage.get_map_tag_last_element_delete
                last_element_delete.click()
            else:
                pass
            tag_total_count1 = self.mappage.get_map_tag_total_count
            self.assertNotEqual(tag_total_count, tag_total_count1, "count are same." )
            self.mappage.manage_filter_save()
        except Exception as e:
            print e
            raise