__author__ = 'Deepa.Sivadas'

from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from basepage import BasePage
from time import sleep
import inspect
from selenium.webdriver.support import expected_conditions as EC

class MapPage(BasePageClass):

    _map_name_text = ".//*[@id='header']/div[1]/span[2]/span"
    _map_container = "map_control"

    # Map views related locators like default, Night View, Terrain, Satelite Default, Satelite Grey
    _map_mouse_hover_action_icon_xpath_locator = "//a[@title='Layers']"
    _map_click_base_map_action_accordion_xpath_locator = ".//*[@id='leaflet-control-accordion-layers-0']/label"
    _map_click_default_action_radio_xpath_locator = ".//*[@id='leaflet-control-accordion-layers-0']/article/div[1]/input"
    _map_click_night_view_action_radio_xpath_locator = ".//*[@id='leaflet-control-accordion-layers-0']/article/div[2]/input"
    _map_click_terrain_action_radio_xpath_locator = ".//*[@id='leaflet-control-accordion-layers-0']/article/div[3]/input"
    _map_click_satelite_default_action_radio_xpath_locator = ".//*[@id='leaflet-control-accordion-layers-0']/article/div[4]/input"
    _map_click_satelite_grey_action_radio_xpath_locator = ".//*[@id='leaflet-control-accordion-layers-0']/article/div[5]/input"

    # Scroll vertically to view default, Night View, Terrain, Satelite Default, Satelite Grey
    _map_scroll = ".//*[@id='mapdiv']/div[2]/div[1]/div[1]"
    _map_sub_scroll = ".//*[@id='leaflet-control-accordion-layers-1']/article"

    # View Map in Full Screen
    _map_mouse_hover_full_screen_icon = "//html/body/div[8]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[1]/div[2]"

    #Bread crumb related
    #Apps link
    _bread_crumb_click_apps_link_xpath_locator = ".//*[@id='header']/div[1]/span[1]/span/a"

    #Search and Locate
    _mouse_hover_search_and_locate = "//a[@title='Bing Geocoder']"
    _map_search_text_box = ".//*[@id='mapdiv']/div[2]/div[1]/div[3]/form/input"
    _map_locate_button = ".//*[@id='mapdiv']/div[2]/div[1]/div[3]/form/button"

    # Zoom out
    _map_zoom_out = ".//*[@id='mapdiv']/div[2]/div[2]/div[1]/a[2]"

    # Map status
    _map_items_map_status = ".//*[@id='map_status']"

    # Basic Data layer
    _map_basic_data_layer = ".//*[@id='leaflet-control-accordion-layers-1']/label"
    _map_basic_data_layer_asset = ".//*[@id='leaflet-control-accordion-layers-1']/article/div[1]/input"
    _map_basic_data_layer_assessment = ".//*[@id='leaflet-control-accordion-layers-1']/article/div[2]/input"
    _map_basic_data_layer_incident = ".//*[@id='leaflet-control-accordion-layers-1']/article/div[3]/input"
    _map_basic_data_layer_threat_streams = ".//*[@id='leaflet-control-accordion-layers-1']/article/div[4]/input"
    _map_basic_data_layer_indicator_teams = ".//*[@id='leaflet-control-accordion-layers-1']/article/div[5]/input"
    _map_basic_data_layer_annotations = ".//*[@id='leaflet-control-accordion-layers-1']/article/div[6]/input"
    _map_basic_data_layer_threat_streams_trending_last_day = ".//*[@id='leaflet-control-accordion-layers-1']/article/div[7]/input"
    _map_basic_data_layer_threat_streams_stream_1 = ".//*[@id='leaflet-control-accordion-layers-1']/article/div[8]/input"
    _map_basic_data_layer_threat_streams_stream_2 = ".//*[@id='leaflet-control-accordion-layers-1']/article/div[9]/input"

    # Water fall handle - Right hand side - Last Icon
    _map_water_fall_handle = ".//*[@id='waterfall_handle']"
    _map_water_fall_list = ".//*[@id='waterfall_ul']"
    _map_water_fall_list_items = "li"
    _map_water_fall_scrollable = ".//*[@id='waterfall_scrollable']"

    # Error handling
    _map_404 = ".//*[@id='error_modal' and @hide-modal='' and @aria-hidden='false']"
    _map_404_close = ".//*[@id='error_modal']/div/div/form/div[2]/button"



    @property
    def get_map_404(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located(
                (By.XPATH, self._map_404)))
            return self.driver.find_element_by_xpath(self._map_404)
        except Exception, err:
            raise type(err)("Map 404 - searched XPATH - " + self._map_404 + err.message)

    @property
    def get_map_404_close(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located(
                (By.XPATH, self._map_404_close)))
            return self.driver.find_element_by_xpath(self._map_404_close)
        except Exception, err:
            raise type(err)("Map 404 close btn - searched XPATH - " + self._map_404_close + err.message)

    @property
    def get_map_app_name(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located(
                (By.XPATH, self._map_name_text)))
            return self.driver.find_element_by_xpath(self._map_name_text)
        except Exception, err:
            raise type(err)("Map App Name - searched XPATH - " + self._map_name_text + err.message)

    @property
    def get_map_container(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located(
                (By.ID, self._map_container)))
            return self.driver.find_element_by_id(self._map_container)
        except Exception, err:
            raise type(err)("Map Container - searched ID - " + self._map_container + err.message)

    @property
    def get_bread_crumb_apps(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located(
                (By.XPATH, self._bread_crumb_click_apps_link_xpath_locator)))
            return self.driver.find_element_by_xpath(self._bread_crumb_click_apps_link_xpath_locator)
        except Exception, err:
            raise type(err)("Bread Crumb Apps - searched XPATH - "
                            + self._bread_crumb_click_apps_link_xpath_locator + err.message)


    @property
    def get_map_mouse_hover_icon(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located(
                (By.XPATH, self._map_mouse_hover_action_icon_xpath_locator)))
            return self.driver.find_element_by_xpath(self._map_mouse_hover_action_icon_xpath_locator)
        except Exception, err:
            raise type(err)("Mouse Hover Icon - searched XPATH - "
                            + self._map_mouse_hover_action_icon_xpath_locator + err.message)

    @property
    def get_map_base_map_accordian(self):
         try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_click_base_map_action_accordion_xpath_locator)))
            return self.driver.find_element_by_xpath(self._map_click_base_map_action_accordion_xpath_locator)
         except Exception, err:
            raise type(err)("Base Map Accordian - searched XPATH - "
                            + self._map_click_base_map_action_accordion_xpath_locator + err.message)

    @property
    def get_map_default_view_radio(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_click_default_action_radio_xpath_locator)))
            return self.driver.find_element_by_xpath(self._map_click_default_action_radio_xpath_locator)
        except Exception, err:
            raise type(err)("Default View Radio - searched XPATH - "
                            + self._map_click_default_action_radio_xpath_locator + err.message)

    @property
    def get_map_night_view_radio(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_click_night_view_action_radio_xpath_locator)))
            return self.driver.find_element_by_xpath(self._map_click_night_view_action_radio_xpath_locator)
        except Exception, err:
            raise type(err)("Night View Radio - searched XPATH - "
                            + self._map_click_night_view_action_radio_xpath_locator + err.message)

    @property
    def get_map_terrain_radio(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_click_terrain_action_radio_xpath_locator)))
            return self.driver.find_element_by_xpath(self._map_click_terrain_action_radio_xpath_locator)
        except Exception, err:
            raise type(err)("Terrain Radio - searched XPATH - "
                            + self._map_click_terrain_action_radio_xpath_locator + err.message)

    @property
    def get_map_satelite_default_view_radio(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_click_satelite_default_action_radio_xpath_locator)))
            return self.driver.find_element_by_xpath(self._map_click_satelite_default_action_radio_xpath_locator)
        except Exception, err:
            raise type(err)("Satelite Default View Radio - searched XPATH - "
                            + self._map_click_satelite_default_action_radio_xpath_locator + err.message)

    @property
    def get_map_satelite_grey_view_radio(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_click_satelite_grey_action_radio_xpath_locator)))
            return self.driver.find_element_by_xpath(self._map_click_satelite_grey_action_radio_xpath_locator)
        except Exception, err:
            raise type(err)("Satelite Grey View Radio - searched XPATH - "
                            + self._map_click_satelite_grey_action_radio_xpath_locator + err.message)


    # Full Screen related
    @property
    def get_map_full_screen(self):
        try:
            return self.driver.find_element_by_xpath(self._map_mouse_hover_full_screen_icon)
        except Exception, err:
            raise type(err)("Full Screen - searched XPATH - " + self._map_mouse_hover_full_screen_icon + err.message)


    # Search and Locate
    @property
    def get_search_and_locate_on_map(self):
        try:
            return self.driver.find_element_by_xpath(self._mouse_hover_search_and_locate)
        except Exception, err:
            raise type(err)("Search and Locate On Map - searched XPATH - "
                            + self._mouse_hover_search_and_locate + err.message)


    @property
    def get_search_on_map(self):
        try:
            return self.driver.find_element_by_xpath(self._map_search_text_box)
        except Exception, err:
            raise type(err)("Search On Map - searched XPATH - " + self._map_search_text_box + err.message)


    @property
    def get_locate_button_on_map(self):
        try:
            return self.driver.find_element_by_xpath(self._map_locate_button)
        except Exception, err:
            raise type(err)("Locate Button On Map - searched XPATH - " + self._map_locate_button + err.message)


    # Zoom out
    @property
    def get_map_zoom_out(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_zoom_out)))
            return self.driver.find_element_by_xpath(self._map_zoom_out)
        except Exception, err:
            raise type(err)("Zoom Out - searched XPATH - " + self._map_zoom_out + err.message)


    # Map status
    @property
    def get_map_items_map_status(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_items_map_status)))
            return self.driver.find_element_by_xpath(self._map_items_map_status)
        except Exception, err:
            raise type(err)("Map Items Status - searched XPATH - " + self._map_items_map_status + err.message)


    # Basic data layer
    @property
    def get_map_basic_data_layer(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_basic_data_layer)))
            return self.driver.find_element_by_xpath(self._map_basic_data_layer)
        except Exception, err:
            raise type(err)("Basic Data Layer - searched XPATH - " + self._map_basic_data_layer + err.message)


    @property
    def get_map_basic_data_layer_asset(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_basic_data_layer_asset)))
            return self.driver.find_element_by_xpath(self._map_basic_data_layer_asset)
        except Exception, err:
            raise type(err)("Basic Data Layer Asset - searched XPATH - "
                            + self._map_basic_data_layer_asset + err.message)


    @property
    def get_map_basic_data_layer_assessment(self):
        try:
            return self.driver.find_element_by_xpath(self._map_basic_data_layer_assessment)
        except Exception, err:
            raise type(err)("Basic Data Layer Assessment - searched XPATH - "
                            + self._map_basic_data_layer_assessment + err.message)


    @property
    def get_map_basic_data_layer_incident(self):
        try:
            return self.driver.find_element_by_xpath(self._map_basic_data_layer_incident)
        except Exception, err:
            raise type(err)("Basic Data Layer Incident - searched XPATH - "
                            + self._map_basic_data_layer_incident + err.message)


    @property
    def get_map_basic_data_layer_threat_streams(self):
        try:
            return self.driver.find_element_by_xpath(self._map_basic_data_layer_threat_streams)
        except Exception, err:
            raise type(err)("Basic Data Layer Threat Streams - searched XPATH - "
                            + self._map_basic_data_layer_threat_streams + err.message)


    @property
    def get_map_basic_data_layer_indicator_teams(self):
        try:
            return self.driver.find_element_by_xpath(self._map_basic_data_layer_indicator_teams)
        except Exception, err:
            raise type(err)("Basic Data Layer Indicator Teams - searched XPATH - "
                            + self._map_basic_data_layer_indicator_teams + err.message)


    @property
    def get_map_basic_data_layer_annotations(self):
        try:
            return self.driver.find_element_by_xpath(self._map_basic_data_layer_annotations)
        except Exception, err:
            raise type(err)("Basic Data Layer Annotations - searched XPATH - "
                            + self._map_basic_data_layer_annotations + err.message)


    @property
    def get_map_basic_data_layer_threat_streams_trending_last_day(self):
        try:
            return self.driver.find_element_by_xpath(self._map_basic_data_layer_threat_streams_trending_last_day)
        except Exception, err:
            raise type(err)("Basic Data Layer Threat Streams Trending Last Day - searched XPATH - "
                            + self._map_basic_data_layer_threat_streams_trending_last_day + err.message)


    @property
    def get_map_basic_data_layer_threat_streams_stream_1(self):
        try:
            return self.driver.find_element_by_xpath(self._map_basic_data_layer_threat_streams_stream_1)
        except Exception, err:
            raise type(err)("Basic Data Layer Threat Streams Stream 1 - searched XPATH - "
                            + self._map_basic_data_layer_threat_streams_stream_1 + err.message)


    @property
    def get_map_basic_data_layer_threat_streams_stream_2(self):
        try:
            return self.driver.find_element_by_xpath(self._map_basic_data_layer_threat_streams_stream_2)
        except Exception, err:
            raise type(err)("Basic Data Layer Threat Streams Stream 2 - searched XPATH - "
                            + self._map_basic_data_layer_threat_streams_stream_2 + err.message)


    # Scroll
    @property
    def get_map_scroll(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_scroll)))
            return self.driver.find_element_by_xpath(self._map_scroll)
        except Exception, err:
            raise type(err)("Accordian main scroll bar - searched XPATH - " + self._map_scroll + err.message)


    @property
    def get_map_sub_scroll(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_sub_scroll)))
            return self.driver.find_element_by_xpath(self._map_sub_scroll)
        except Exception, err:
            raise type(err)("Accordian inside scroll bar - searched XPATH - " + self._map_sub_scroll + err.message)


    # Water fall handle - Right hand side - Last Icon
    @property
    def get_map_water_fall_handle(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_water_fall_handle)))
            return self.driver.find_element_by_xpath(self._map_water_fall_handle)
        except Exception, err:
            raise type(err)("Water fall handle - Right hand side - Last Icon - searched XPATH - "
                            + self._map_water_fall_handle + err.message)

    @property
    def get_map_water_fall_scrollable(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_water_fall_scrollable)))
            return self.driver.find_element_by_xpath(self._map_water_fall_scrollable)
        except Exception, err:
            raise type(err)("Water fall Scrollable - Right hand side - Last Icon - searched XPATH - "
                            + self._map_water_fall_scrollable + err.message)

    @property
    def get_map_water_fall_list(self):
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._map_water_fall_list)))
            return self.driver.find_element_by_xpath(self._map_water_fall_list)
        except Exception, err:
            raise type(err)("Water fall list - searched XPATH - " + self._map_water_fall_list + err.message)



    @property
    def get_map_water_fall_list_items(self):
        try:
            return self.driver.find_elements_by_tag_name(self._map_water_fall_list_items)
        except Exception, err:
            raise type(err)("Water fall list items - searched XPATH - "
                            + self._map_water_fall_list_items + err.message)


    def __init__(self, driver):
        super(MapPage, self).__init__(driver)

    def open_map_app(self):
        appicon = IconListPage(self.driver)
        appicon.click_map_icon()
        '''
        feedbackformIcon = self.driver.find_element_by_xpath(".//*[@id='H1']/img")
        sleep(5)
        if feedbackformIcon.is_displayed():
            sleep(5)
            self.driver.find_element_by_xpath(".//*[@id='submit_feedback_modal']/div/div/form/div[2]/button[1]").click()
            print "Closed Feedback form..."
        '''
        #WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH,
        #                                                                "//a[contains(text(),'Leaflet')]"), "Leaflet"))


    # This function is used - if check box is selected, it should be unchecked
    def get_checking_and_unchecking_basic_data_layer(self):
        sleep(2)
        if self.get_map_basic_data_layer_asset.is_displayed():
            if self.get_map_basic_data_layer_asset.is_selected():
                self.get_map_basic_data_layer_asset.click()
        sleep(2)
        if self.get_map_basic_data_layer_assessment.is_displayed():
            if self.get_map_basic_data_layer_assessment.is_selected():
                self.get_map_basic_data_layer_assessment.click()

        if self.get_map_basic_data_layer_incident.is_displayed():
            if self.get_map_basic_data_layer_incident.is_selected():
                self.get_map_basic_data_layer_incident.click()

        if self.get_map_basic_data_layer_threat_streams.is_displayed():
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            if self.get_map_basic_data_layer_threat_streams.is_selected():
                self.get_map_basic_data_layer_threat_streams.click()

        if self.get_map_basic_data_layer_indicator_teams.is_displayed():
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            if self.get_map_basic_data_layer_indicator_teams.is_selected():
                self.get_map_basic_data_layer_indicator_teams.click()

        if self.get_map_basic_data_layer_annotations.is_displayed():
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            if self.get_map_basic_data_layer_annotations.is_selected():
                self.get_map_basic_data_layer_annotations.click()

        if self.get_map_basic_data_layer_threat_streams_trending_last_day.is_displayed():
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
            if self.get_map_basic_data_layer_threat_streams_trending_last_day.is_selected():
                self.get_map_basic_data_layer_threat_streams_trending_last_day.click()

        if self.get_map_basic_data_layer_threat_streams_stream_1.is_displayed():
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
            if self.get_map_basic_data_layer_threat_streams_stream_1.is_selected():
                self.get_map_basic_data_layer_threat_streams_stream_1.click()

        if self.get_map_basic_data_layer_threat_streams_stream_2.is_displayed():
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
            self.get_map_sub_scroll.send_keys(Keys.ARROW_DOWN)
            if self.get_map_basic_data_layer_threat_streams_stream_2.is_selected():
                self.get_map_basic_data_layer_threat_streams_stream_2.click()

    def return_to_icon_list_page(self):
        try:
            self.get_bread_crumb_apps.click()
        except:
            basepage = BasePage(self.driver)
            basepage.accessURL()

    def get_total_map_status_count(self):
        countText = self.driver.find_element_by_xpath(self._map_items_map_status).text
        splitedText = countText.split(" ")
        totalCount = splitedText[1]
        return int(totalCount)

    def return_to_apps_main_page(self):
        """
        Description : This function will helps to go back to assets page.
        Revision:
        :return: None
        """
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, self._bread_crumb_click_apps_link_xpath_locator))).click()

            WebDriverWait(self.driver, 50).until(expected_conditions.presence_of_element_located(
                (By.XPATH, IconListPage(self.driver)._app_map_icon_locator)),"Map Icon")

        except:
            inspectstack = inspect.stack()[1][3]
            self.recoverapp(inspectstack)

    def recoverapp(self, inspectstack):
        """
        Description : This function helps to go back to assets page. Inspect stack prints the test name from which
                                 this function is called.
        Revision:
        :return: None
        """
        print ("Application recovering called from " + inspectstack)
        basepage = BasePage(self.driver)
        basepage.accessURL()
        iconlistpage = IconListPage(self.driver)
        iconlistpage.click_map_icon()
