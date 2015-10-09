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

    #Bread crumb related
    #Apps link
    _bread_crumb_click_apps_link_xpath_locator = ".//*[@id='header']/div[1]/span[1]/span/a"


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


    def __init__(self, driver):
        super(MapPage, self).__init__(driver)
        appicon = IconListPage(self.driver)
        appicon.click_map_icon()

    #def get_map_based_on_basic_data_layer(self):

