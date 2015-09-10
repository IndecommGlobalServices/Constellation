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
    def test_smoketest_appmainpage(self):
        assessmentpage = AssessmentPage(self.driver)
        sleep(2)
        try:
            self.assertEqual(assessmentpage.get_ast_app_name.text, "Assessments")
        except:
            print "The Assessment link text not available"

        assessmentpage.get_ast_statusfilter_dropdown.click()

        try:
            self.assertTrue(assessmentpage.get_statusfilter_InProgress_link)
            self.assertTrue(assessmentpage.get_statusfilter_NotStarted_link)
            self.assertTrue(assessmentpage.get_statusfilter_Submitted_link)
        except:
            print " One or more filter option for status not present"

        try:
            self.assertEqual(assessmentpage.get_resetfilter_button.text, "Reset filters")
        except:
            print "Reset filters button not available or text not matching"

        try:
            self.assertTrue(assessmentpage.get_search_textbox)
        except:
            print "Search textbox not available"

        try:
            self.assertTrue(assessmentpage.get_create_assessment_button)
        except:
            print "Create assessment button not present"

if __name__ == '__main__':
    unittest.main(verbosity=2)


