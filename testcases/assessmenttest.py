__author__ = 'Deepa.Sivadas'
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pages.assessmentpage import AssessmentPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from lib.getFilterData import getFilterData, getSchoolFilterData
from time import sleep
from pages.IconListPage import IconListPage
import json, os, re


class AssessmenttPageTest(BaseTestCase):

    @attr(priority="high")
    #@SkipTest
    def test_AST_01_To_Test(self):
        sleep(5)
        assessmentpage = AssessmentPage(self.driver)
        sleep(20)
        #self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='header']/span[2]/span").text)



if __name__ == '__main__':
    unittest.main(verbosity=2)


