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


class AssessmentSchoolInfrastructurePageTest(BaseTestCase):

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast = AssessmentPage(self.driver)
        self.mainsection = 'Sections'
        self.messages = 'Messages'
        self.infrastructuredata = 'SchoolInfrastructure'
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open('baseconfig.cfg'))

        self.ast.open_schoolinfrastructure_page()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        for section in self.config.options(self.infrastructuredata):
            self.ast.delete_attchedimage(self.config.get(self.infrastructuredata, section))
        self.ast.get_overview_button.click()
        self.ast.return_to_assessment_main_page()


    @attr(priority="high")
    #@SkipTest
    def test_AST_109_To_Test_SchoolType_Radio_Button(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """
        for option in range(8):
            landacreoption = self.ast.get_school_schoolinfrastructure_land_acre_radiobutton
            if not landacreoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landacreoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                landchecked = self.ast.get_school_schoolinfrastructure_land_acre_radiobutton
                self.assertEqual(landchecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_69_1_To_Verify_Fileupload_SchoolType(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_69_2_To_Verify_Edit_Caption_File_SchoolType(self):
        """
        Test : test_AST_69_2
        Description : To test the add photo to school type section
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_73_To_Verfiy_Add_Comment_SchoolType(self):
        """
        Description : To test the add comment to school type section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_LANDANDBUILDING_ACRES')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
