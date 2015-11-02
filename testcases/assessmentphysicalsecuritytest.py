__author__ = 'Deepa.Sivadas'
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pages.assessmentpage import AssessmentPage
from pages.loginpage import LoginPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from time import sleep
from datetime import date, timedelta, datetime
import json, os, re


class AssessmentPhysicalSecuritiesPageTest(BaseTestCase):

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast = AssessmentPage(self.driver)
        self.ast.open_physicalsecurity_page()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        self.ast.return_to_assessment_main_page()


    @attr(priority="high")
    #@SkipTest
    def test_AST_167(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """
        for option in range(10):
            fencingoptions = self.ast.get_physicalsecurity_fencing_radiobutton
            if not fencingoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                fencingoptions[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_PHYSICAL_SECURITY'))
                fencingchecked = self.ast.get_physicalsecurity_fencing_radiobutton
                self.assertEqual(fencingchecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")
