__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException
from selenium.webdriver.common.keys import Keys

class IconListPage(BasePageClass):
    _app_asset_icon_locator  = "app_assets"
    #_app_assessments_icon_locator = "app_assessments"
    _app_assessments_icon_locator = ".//*[@id='app_assessments']/div/img"
    _app_map_icon_locator = "app_map"
    _app_dashboard_icon_locator = "app_dashboard"
    _app_threatstreams_icon_locator = "app_threatstreams"
    _app_incidents_icon_locator = "app_incidents"

    @property
    def get_app_asset_icon(self):
        return self.driver.find_element_by_id(self._app_asset_icon_locator)

    @property
    def get_app_assessments_icon(self):
        return self.driver.find_element_by_xpath(self._app_assessments_icon_locator)

    @property
    def get_app_map_icon(self):
        return self.driver.find_element_by_id(self._app_map_icon_locator)

    @property
    def get_app_dashboard_icon(self):
        return self.driver.find_element_by_id(self._app_dashboard_icon_locator)


    @property
    def get_app_threatstreams_icon(self):
        return self.driver.find_element_by_id(self._app_threatstreams_icon_locator)

    @property
    def get_app_incidents_icon(self):
        return self.driver.find_element_by_id(self._app_incidents_icon_locator)

    def __init__(cls, driver):
        super(IconListPage,cls).__init__(driver)

    def click_asset_icon(cls):
        try:
            cls.get_app_asset_icon.click()
        except:
            print "Asset app is open"

    def click_assessments_icon(self):
        try:
            self.get_app_assessments_icon.click()
        except:
            print "Assessment app is open"
        #self.get_app_assessments_icon.click()


    def click_map(self):
        self.get_app_map_icon.click()

    def click_dashboard(self):
        self.get_app_dashboard_icon.click()

    def click_incident(self):
        self.get_app_incidents_icon.click()

    def click_threatstream(self):
        self.get_app_threatstreams_icon.click()

