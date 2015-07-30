import unittest
from selenium import webdriver
from time import sleep
from datetime import datetime
from xvfbwrapper import Xvfb
import os
import sys
import nose
#Hi from deepa
from nose.plugins.attrib import attr

class FilterSearchCreateAssetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        #cls.driver = webdriver.Firefox()
        #cls.driver.implicitly_wait(30)
        #cls.driver.maximize_window()
        cls.display = Xvfb()
        cls.display.start()

        #cls.driver = webdriver.PhantomJS('phantomjs')
        #cls.driver.set_window_size(1124, 850)

        cls.driver = webdriver.Firefox()

        # navigate to the application home page
        cls.driver.get("https://constellation-dev.haystax.com/#/")

        # get Login link
        lnkLogin = cls.driver.find_element_by_link_text("Or log in")

        # click on Login link
        lnkLogin.click()
        sleep(10)
        #get the Email textbox
        email_field = cls.driver.find_element_by_id("inputusername")
        #email_field.clear()
        sleep(10)

        # enter email
        email_field.send_keys("Deepa.Sivadas@indecomm.net")
        sleep(10)
        # get the password textbox
        password_field = cls.driver.find_element_by_id("inputpassword")
        #password_field.clear()
        sleep(10)
        # enter password
        password_field.send_keys("myhaystax")
        sleep(10)
        # click on Login button
        btnLogin_field = cls.driver.find_element_by_xpath("//form[@id='login_form']/li[3]/button")
        btnLogin_field.click()
        sleep(10)

        # click on Assets
        lnkAssets_field = cls.driver.find_element_by_id("app_assets")
        lnkAssets_field.click()
        sleep(10)

    @attr(priority="high")
    def test_01_Filter_By_Place(self):
        self.driver.find_element_by_xpath("//*[@id='span_filters']/div/div/button[2]").click()
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

    @classmethod
    def tearDownClass(cls):
        if sys.exc_info()[0]:
            test_method_name = cls._testMethodName
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            cls.driver.save_screenshot(os.getcwd() + '/screenshots/' + test_method_name + "-" + now + ".png")
        cls.driver.quit()
        cls.display.stop()

    if __name__ == '__main__':
        nose.main(verbosity=2)
