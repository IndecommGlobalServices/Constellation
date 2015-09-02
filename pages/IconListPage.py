__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException

class IconListPage(BasePageClass):
    _app_asset_icon_locator  = "app_assets"
    _app_assessments_icon_locator = "app_assessments"

    @property
    def get_app_asset_icon(self):
        return self.driver.find_element_by_id(self._app_asset_icon_locator)

    def get_app_assessments_icon(self):
        return self.driver.find_element_by_id(self._app_assessments_icon_locator)

    def __init__(cls, driver):
        super(IconListPage,cls).__init__(driver)

    def click_asset_Icon(self):
        self.get_app_asset_icon.click()

    def click_assessments_icon(self):
        self.get_app_assessments_icon.click()

