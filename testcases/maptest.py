__author__ = 'Deepa.Sivadas'
import unittest
from testcases.basetestcase import BaseTestCase
from pages.mappage import MapPage
from nose.plugins.attrib import attr
from time import sleep


class MapPageTest(BaseTestCase):

    @attr(priority="high")
    #@SkipTest
    def test_smoketest_map(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(20)
        self.assertEqual(mappage.get_map_app_name.text, "Map")




if __name__ == '__main__':
    unittest.main(verbosity=2)