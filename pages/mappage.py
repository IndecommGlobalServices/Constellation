__author__ = 'Deepa.Sivadas'


from lib.base import BasePageClass
from selenium.webdriver.common.keys import Keys

class MapPage(BasePageClass):


    def __init__(self, driver):
        super(MapPage, self).__init__(driver)
