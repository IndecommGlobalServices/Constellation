__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class IconListPage(BasePageClass, object):
    _app_asset_icon_locator  = "app_assets"
    #_app_assessments_icon_locator = "app_assessments"
    _app_assessments_icon_locator = ".//*[@id='app_assessments']/div/img"
    _app_map_icon_locator = "//img[@src = '../images/app_icon_map.png']"
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
        return self.driver.find_element_by_xpath(self._app_map_icon_locator)

    @property
    def get_app_dashboard_icon(self):
        return self.driver.find_element_by_id(self._app_dashboard_icon_locator)

    @property
    def get_app_threatstreams_icon(self):
        return self.driver.find_element_by_id(self._app_threatstreams_icon_locator)

    @property
    def get_app_incidents_icon(self):
        return self.driver.find_element_by_id(self._app_incidents_icon_locator)

    def __init__(self, driver):
        super(IconListPage,self).__init__(driver)



    def click_asset_icon(self):
        try:
            self.get_app_asset_icon.click()
        except:
            pass

    def click_assessments_icon(self):
        try:
            self.get_app_assessments_icon.click()
        except:
            pass

    def click_map_icon(self):
        try:
            WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                (By.XPATH, self._app_map_icon_locator)))
            self.get_app_map_icon.click()
        except:
            pass

    def click_dashboard(self):
        try:
            self.get_app_dashboard_icon.click()
        except:
            pass

    def click_incident(self):
        try:
            self.get_app_incidents_icon.click()
        except:
            pass

    def click_threatstream(self):
        try:
            self.get_app_threatstreams_icon.click()
        except:
            pass
