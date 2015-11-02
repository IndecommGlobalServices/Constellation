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


class AssessmentPoliciesandPlanningPageTest(BaseTestCase):

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast = AssessmentPage(self.driver)
        self.ast.open_policiesandplanning_page()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        self.ast.return_to_assessment_main_page()


    @attr(priority="high")
    #@SkipTest
    def test_AST_242(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """
        for option in range(4):
            schoolsafetyoptions = self.ast.get_policiesandplanning_schoolsafety_radiobutton
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_POLICIES_PLANNING'))
                schoolsafetychecked = self.ast.get_policiesandplanning_schoolsafety_radiobutton
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")
