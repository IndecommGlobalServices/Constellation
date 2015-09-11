__author__ = 'Deepa.Sivadas'

from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from selenium.webdriver.common.keys import Keys

class MapPage(BasePageClass):

    _map_name_text = ".//*[@id='header']/div[1]/span[2]/span"
    _map_container = "map_control"

    @property
    def get_map_app_name(self):
        return self.driver.find_element_by_xpath(self._map_name_text)

    @property
    def get_map_container(self):
        return self.driver.find_element_by_id(self._map_container)

    def __init__(self, driver):
        super(MapPage, self).__init__(driver)
        appicon = IconListPage(self.driver)
        appicon.click_map_icon()
