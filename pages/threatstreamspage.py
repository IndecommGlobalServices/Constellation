__author__ = 'Deepa.Sivadas'

from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from selenium.webdriver.common.keys import Keys

class ThreatStreamPage(BasePageClass):


    _ts_app_name_text = ".//*[@id='header']/span[2]/span"

    @property
    def get_ts_app_name(self):
        return self.driver.find_element_by_xpath(self._ts_app_name_text)




    def __init__(self, driver):
        super(ThreatStreamPage, self).__init__(driver)
        appicon = IconListPage(self.driver)
        appicon.click_threatstream()
