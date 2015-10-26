__author__ = 'Deepa.Sivadas'

from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from selenium.webdriver.common.keys import Keys

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

    # Water fall handle - Right hand side - Last Icon
    _map_water_fall_handle = ".//*[@id='waterfall_handle']"

    @property
    def get_map_app_name(self):
        return self.driver.find_element_by_xpath(self._map_name_text)

    @property
    def get_map_container(self):
        return self.driver.find_element_by_id(self._map_container)

    @property
    def get_bread_crumb_apps(self):
        return self.driver.find_element_by_xpath(self._bread_crumb_click_apps_link_xpath_locator)

    @property
    def get_map_mouse_hover_icon(self):
        return self.driver.find_element_by_xpath(self._map_mouse_hover_action_icon_xpath_locator)

    @property
    def get_map_base_map_accordian(self):
        return self.driver.find_element_by_xpath(self._map_click_base_map_action_accordion_xpath_locator)

    @property
    def get_map_default_view_radio(self):
        return self.driver.find_element_by_xpath(self._map_click_default_action_radio_xpath_locator)

    @property
    def get_map_night_view_radio(self):
        return self.driver.find_element_by_xpath(self._map_click_night_view_action_radio_xpath_locator)

    @property
    def get_map_terrain_radio(self):
        return self.driver.find_element_by_xpath(self._map_click_terrain_action_radio_xpath_locator)

    @property
    def get_map_satelite_default_view_radio(self):
        return self.driver.find_element_by_xpath(self._map_click_satelite_default_action_radio_xpath_locator)

    @property
    def get_map_satelite_grey_view_radio(self):
        return self.driver.find_element_by_xpath(self._map_click_satelite_grey_action_radio_xpath_locator)

    # Full Screen related
    @property
    def get_map_full_screen(self):
        return self.driver.find_element_by_xpath(self._map_mouse_hover_full_screen_icon)

    # Search and Locate
    @property
    def get_search_and_locate_on_map(self):
        return self.driver.find_element_by_xpath(self._mouse_hover_search_and_locate)

    @property
    def get_search_on_map(self):
        return self.driver.find_element_by_xpath(self._map_search_text_box)

    @property
    def get_locate_button_on_map(self):
        return self.driver.find_element_by_xpath(self._map_locate_button)

    # Zoom out
    @property
    def get_map_zoom_out(self):
        return self.driver.find_element_by_xpath(self._map_zoom_out)

    # Map status
    @property
    def get_map_items_map_status(self):
        return self.driver.find_element_by_xpath(self._map_items_map_status)

    # Basic data layer
    @property
    def get_map_basic_data_layer(self):
        return self.driver.find_element_by_xpath(self._map_basic_data_layer)

    @property
    def get_map_basic_data_layer_asset(self):
        return self.driver.find_element_by_xpath(self._map_basic_data_layer_asset)

    @property
    def get_map_basic_data_layer_assessment(self):
        return self.driver.find_element_by_xpath(self._map_basic_data_layer_assessment)

    @property
    def get_map_basic_data_layer_incident(self):
        return self.driver.find_element_by_xpath(self._map_basic_data_layer_incident)

    # Water fall handle - Right hand side - Last Icon
    @property
    def get_map_water_fall_handle(self):
        return self.driver.find_element_by_xpath(self._map_water_fall_handle)


    def __init__(self, driver):
        super(MapPage, self).__init__(driver)
        appicon = IconListPage(self.driver)
        appicon.click_map_icon()

    #def get_map_based_on_basic_data_layer(self):

