__author__ = 'Deepa.Sivadas'
import unittest
from testcases.basetestcase import BaseTestCase
from pages.mappage import MapPage
from nose.plugins.attrib import attr
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions




class MapPageTest(BaseTestCase):

    @attr(priority="high")
    #@SkipTest
    def test_smoketest_map(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(20)
        self.assertEqual(mappage.get_map_app_name.text, "Map")

    @attr(priority="high")
    #@SkipTest
    def test_map_01_to_verify_default(self):
        sleep(5)
        mappage = MapPage(self.driver)
        sleep(20)

        #Actions actions = new Actions(driver);
        #WebElement menuElement = driver.findElement(By.id("menu-element-id"));
        #actions.moveToElement(menuElement).moveToElement(driver.findElement(By.xpath("xpath-of-menu-item-element"))).click();


        title_field = self.driver.find_element_by_xpath("//a[@title='Layers']")
        #leaflet-control-layers-base
        #title_field = self.driver.find_element_by_xpath("//html/body/div[6]/div[3]/div[5]/div[2]/div/div/div[2]/div[1]/div[1]")
        sleep(5)
        ActionChains(self.driver).move_to_element(title_field).move_to_element(self.driver.find_element_by_xpath("//div/leaflet-base-layers")[1]).click()
        sleep(10)
        #default_elm = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME, "leaflet-base-layers")))

        #WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME, "leaflet-base-layers"))).click()
        #self.driver.find_element_by_xpath("//div/leaflet-base-layers")[0].click()
        #default_elm.c

        #self.assertEqual(mappage.get_map_app_name.text, "Map")



if __name__ == '__main__':
    unittest.main(verbosity=2)