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
import ConfigParser
from nose.plugins.skip import SkipTest
from time import sleep
from datetime import date, timedelta, datetime
import json, os, re


class AssessmentPoliciesandPlanningPageTest(BaseTestCase):
    checked_var = r"answer_choice radio ng-binding ng-isolate-scope checked"
    unchecked_var = r"answer_choice radio ng-binding ng-isolate-scope"

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast = AssessmentPage(self.driver)
        self.AssessmentSections = 'AssessmentSections'
        self.mainsection = 'PoliciesAndPlanningMainSections'
        self.subsection = 'PoliciesAndPlanningSubSections'
        self.messages = 'Messages'
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open('baseconfig.cfg'))
        self.ast.open_policiesandplanning_page()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        for subsection in self.config.options(self.subsection):
            self.ast.delete_attchedimage(self.config.get(self.subsection, subsection))
        self.ast.get_overview_button.click()
        self.ast.return_to_assessment_main_page()

    @attr(priority="high")
    #@SkipTest
    def test_AST_242_1_To_Verfiy_Radio_Buttons_Of_School_Safety_Plan(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_SCHOOL_SAFETY')
        config_sub_var = self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_COMPREHENSIVE_PLAN')
        for option in range(4):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not schoolsafetyoptions[option].get_attribute("class") == self.checked_var:
                schoolsafetyoptions[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), self.checked_var)
            else:
                schoolsafetyoptions[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), self.unchecked_var)


    @attr(priority="high")
    #@SkipTest
    def test_AST_242_2_To_Verfiy_File_Upload_Of_School_Safety_Plan(self):
        """
        Description : To test file upload feature.
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_SCHOOL_SAFETY')
        config_sub_var = self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_COMPREHENSIVE_PLAN')
        config_assessment = self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING')
        count_of_image_before_upload = len(self.ast.get_schooldata_image(config_main_var, config_sub_var))

        self.ast.schooldata_upload_file(config_main_var, config_sub_var, config_assessment)
        self.assertGreater(len(self.ast.get_schooldata_image(config_main_var, config_sub_var)),
                     count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(config_main_var, config_sub_var, config_assessment)

