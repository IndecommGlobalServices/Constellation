__author__ = 'Deepa.Sivadas'
import unittest
from testcases.basetestcase import BaseTestCase
from pages.mappage import MapPage
from nose.plugins.attrib import attr
from time import sleep


class MapPageTest(BaseTestCase):

    @attr(priority="high")
    #@SkipTest
    def test_MAP_01_To_Test(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(20)
        #self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='header']/span[2]/span").text)



if __name__ == '__main__':
    unittest.main(verbosity=2)