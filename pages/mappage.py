__author__ = 'Deepa.Sivadas'

from lib.base import BasePageClass
from pages.IconListPage import IconListPage

class MapPage(BasePageClass):

    def __init__(self, driver):
        super(MapPage, self).__init__(driver)
        appicon = IconListPage(self.driver)
        appicon.click_map()
