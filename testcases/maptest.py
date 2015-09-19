__author__ = 'Deepa.Sivadas'
import unittest
from testcases.basetestcase import BaseTestCase
from pages.mappage import MapPage
from nose.plugins.attrib import attr
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest

class MapPageTest(BaseTestCase):

    @attr(priority="high")
    @SkipTest
    def test_smoketest_map(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(20)
        self.assertEqual(mappage.get_map_app_name.text, "Map")

    # Default view
    @attr(priority="high")
    def test_map_01_to_verify_default(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(5)

        # mouse hover to 1st icon
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_default_view_radio).click()\
            .perform()
        sleep(10)

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()

    # Night view
    @attr(priority="high")
    def test_map_02_to_verify_Night_View(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(5)

        # mouse hover to 1st icon
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_night_view_radio).click()\
            .perform()
        sleep(10)

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()


    # Terrain
    @attr(priority="high")
    def test_map_03_to_verify_Terrain(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(5)

        # mouse hover to 1st icon
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_terrain_radio).click()\
            .perform()
        sleep(10)

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()

    # Satelite Default
    @attr(priority="high")
    def test_map_04_to_verify_Satelite_Default(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(5)

        # mouse hover to 1st icon
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_satelite_default_view_radio).click()\
            .perform()
        sleep(10)

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()

    # Satelite Grey
    @attr(priority="high")
    #@SkipTest
    def test_map_05_to_verify_Satelite_Grey(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(5)

        # mouse hover to 1st icon
        mouse_hover_field = mappage.get_map_mouse_hover_icon
        sleep(10)

        ActionChains(self.driver).move_to_element(mouse_hover_field)\
            .move_to_element(mappage.get_map_base_map_accordian).click()\
            .move_to_element(mappage.get_map_satelite_grey_view_radio).click()\
            .perform()
        sleep(10)

        # Click on Bread crumb - Apps link
        mappage.get_bread_crumb_apps.click()

if __name__ == '__main__':
    unittest.main(verbosity=2)