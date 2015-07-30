import unittest
from homepage import HomePage
from basetestcase import BaseTestCase
from time import sleep
from nose.plugins.attrib import attr


class MainDriverScript(BaseTestCase):

    @attr(priority="high")
    def test_01_Filter_By_Place(self):
        sleep(10)
        self.driver.find_element_by_xpath("//*[@id='span_filters']/div/div/button[2]").click()
        sleep(10)
        self.driver.find_element_by_link_text("Place").click()
        sleep(10)
        places = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        sleep(10)
        print "Found " + str(len(places)) + " Places Asset Types :"
        for place in places:
            print place.text
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[3]"):
             self.assertEqual (i.text, "Place")

    @attr(priority="high")
    def test_02_Filter_By_School(self):
        self.driver.find_element_by_xpath("//span[@id='span_filters']/div/div/button[2]").click()
        self.driver.find_element_by_link_text("School").click()
        sleep(10)
        schools = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        sleep(10)
        print "Found " + str(len(schools)) + " Schools Asset Types :"
        for school in schools:
            print school.text
        for i in self.driver.find_elements_by_xpath(".//*[@id='assetstable']/tbody/tr/td[3]"):
             self.assertEqual (i.text, "School")

    @attr(priority="high")
    def test_03_Search_By_Name(self):
        searchAsset_textbox = self.driver.find_element_by_id("txt_search_assets")
        searchAsset_textbox.send_keys("k")
        sleep(10)
        searchNames = self.driver.find_elements_by_xpath("//tbody/tr/td/a")
        sleep(10)
        print "Found " + str(len(searchNames)) + " by Name search."
        for searchName in searchNames:
            print searchName.text

if __name__ =='__main__':
    unittest.main(verbosity=2)
