__author__ = 'Deepa.Sivadas'
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.assessmentpage import AssessmentPage
from pages.loginpage import LoginPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from time import sleep
import ConfigParser
import os, json

cwd = os.getcwd()
os.chdir('..')
sectionfile = os.path.join(os.getcwd(), "data", "json_assessment_schooldata_section.json")
os.chdir(cwd)

class AssessmentSchoolDataPageTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(AssessmentSchoolDataPageTest, cls).setUpClass()
        cls.AssessmentSections = 'AssessmentSections'
        cls.messages = 'Messages'
        cls.mainsection = 'SchoolDataMainSection'
        cls.subsection = 'SchoolDataSubSection'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))
        cls.ast = AssessmentPage(cls.driver)
        cls.ast.get_asset_avilability(cls.config.get(cls.AssessmentSections, 'MAIN_SCHOOLDATA'))
        cls.ast.delete_existing_assessments()

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast.open_main_section(self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        # for section in self.config.options(self.subsection):
        #     self.ast.delete_attchedimage(self.config.get(self.subsection, section))
        self.ast.get_overview_button.click()
        self.ast.return_to_assessment_main_page()

    @attr(priority="high")
    #@SkipTest
    def test_AST_68_To_Test_SchoolType_Radio_Button(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """

        for option in range(4):
            schooltypeoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                    self.config.get(self.subsection, 'SECTION_SCHOOL_TYPE'))
            if not schooltypeoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schooltypeoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
                schooltypeoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                self.config.get(self.subsection, 'SECTION_SCHOOL_TYPE'))
                self.assertEqual(schooltypeoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_69_To_Verify_SchoolGrade_Checkbox(self):
        """
        Description : To test the school grade option checkbox
        :return:
        """
        for option in range(6):
            schoolgradeoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                    self.config.get(self.subsection, 'SECTION_GRADE_LEVELS'))
            if not schoolgradeoption[option].get_attribute("class") == "checkbox ng-binding checked":
                schoolgradeoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
                schoolgradeoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                    self.config.get(self.subsection, 'SECTION_GRADE_LEVELS'))
                self.assertEqual(schoolgradeoption[option].get_attribute("class"), "checkbox ng-binding checked")
                schoolgradeoption[option].click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_70_To_Verify_SchoolHours_TextBox(self):
        """
        Description : To test the school hours section
        :return:
        """
        self.ast.get_schooldata_textbox_textinput(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                  self.config.get(self.subsection, 'SECTION_SCHOOL_HOURS')).clear()
        self.ast.get_schooldata_textbox_textinput(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                  self.config.get(self.subsection, 'SECTION_SCHOOL_HOURS')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_textinput_locator(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                self.config.get(self.subsection, 'SECTION_SCHOOL_HOURS')))))
        self.assertEqual(self.ast.get_schooldata_textbox_textinput(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                            self.config.get(self.subsection, 'SECTION_SCHOOL_HOURS')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_73_To_Verify_Number_Of_Students_TextBox(self):
        """
        Description : To test the No of students section
        :return:
        """
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                  self.config.get(self.subsection, 'SECTION_NUMBER_OF_STUDENTS')).clear()
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                  self.config.get(self.subsection, 'SECTION_NUMBER_OF_STUDENTS')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_locator(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                self.config.get(self.subsection, 'SECTION_NUMBER_OF_STUDENTS')))))
        self.assertEqual(self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                            self.config.get(self.subsection, 'SECTION_NUMBER_OF_STUDENTS')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_74_To_Verify_Validation_No_Of_Students_TextBox(self):
        """
        Description : To test validations of no of students text area
        :return:
        """
        pass

    @attr(priority="high")
    #@SkipTest
    def test_AST_76_To_Verify_Special_Students_Text_Box(self):
        """
        Description : To test Special students section
        :return:
        """
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                  self.config.get(self.subsection, 'SECTION_SPECIAL_NEEDS_STUDENT')).clear()
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                  self.config.get(self.subsection, 'SECTION_SPECIAL_NEEDS_STUDENT')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_locator(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                self.config.get(self.subsection, 'SECTION_SPECIAL_NEEDS_STUDENT')))))
        self.assertEqual(self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                            self.config.get(self.subsection, 'SECTION_SPECIAL_NEEDS_STUDENT')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_78_To_Verify_No_of_Staff_Text_Box(self):
        """
        Description : To test the no of staff section
        :return:
        """
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                  self.config.get(self.subsection, 'SECTION_NO_OF_STAFF')).clear()
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                  self.config.get(self.subsection, 'SECTION_NO_OF_STAFF')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_locator(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                self.config.get(self.subsection, 'SECTION_NO_OF_STAFF')))))
        self.assertEqual(self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                            self.config.get(self.subsection, 'SECTION_NO_OF_STAFF')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_81_To_Verify_No_of_Visitors_TextBox(self):
        """
        Description : To test the no of visitors section
        :return:
        """
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                  self.config.get(self.subsection, 'SECTION_NO_OF_VISITORS')).clear()
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                                                  self.config.get(self.subsection, 'SECTION_NO_OF_VISITORS')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_locator(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                self.config.get(self.subsection, 'SECTION_NO_OF_VISITORS')))))
        self.assertEqual(self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL_INFORMATION'),
                            self.config.get(self.subsection, 'SECTION_NO_OF_VISITORS')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_82_To_Verify_validation_No_of_Visitors(self):
        """
        Description : To test the validation of no of visitors section
        :return:
        """

    @attr(priority="high")
    #@SkipTest
    def test_AST_83_To_Verify_Police_RadioButton(self):
        """
        Description : To test a certified law enforcement officer option radio buttons
        :return:
        """
        for option in range(2):
            policeoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_POLICE'),
                                    self.config.get(self.subsection, 'SECTION_LAW_ENFORCEMENT_OFFICER'))
            if not policeoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                policeoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
                policeoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_POLICE'),
                                self.config.get(self.subsection, 'SECTION_LAW_ENFORCEMENT_OFFICER'))
                self.assertEqual(policeoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_84_Verify_File_Upload_For_All_Sections(self):
        """
        Description : To test file upload in All the sections under School Data Tab.
        :return:
        """
        with open(sectionfile) as data_file:
            for section in json.load(data_file):
                count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(
                                        self.mainsection, section["main_section"]),
                                        self.config.get(self.subsection, section["sub_section"])))
                try:
                    self.ast.schooldata_upload_file(self.config.get(self.mainsection, section["main_section"]),
                                                self.config.get(self.subsection, section["sub_section"]),
                                                self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
                    self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(
                                                    self.mainsection, section["main_section"]),
                                                    self.config.get(self.subsection, section["sub_section"]))),
                                                    count_of_image_before_upload, self.config.get(
                                                    self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
                except Exception, err:
                    # self.defaultTestResult()
                    print err.message + " under " + self.config.get(self.mainsection, section["main_section"]) \
                          +" - " +self.config.get(self.subsection, section["sub_section"])
                    pass
                self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.mainsection, section["main_section"]),
                                                self.config.get(self.subsection, section["sub_section"]),
                                                self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_85_To_Verify_Edit_Caption_For_All_Sections(self):
        """
        Description : To test file upload with caption in All the sections under School Data Tab.
        :return:
        """
        with open(sectionfile) as data_file:
            for section in json.load(data_file):
                try:
                    self.ast.schooldata_edit_caption_image(self.config.get(self.mainsection, section["main_section"]),
                                                       self.config.get(self.subsection, section["sub_section"]),
                                                       self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
                    self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.mainsection, section["main_section"]),
                                                self.config.get(self.subsection, section["sub_section"]))[0].text, "Hello")
                except Exception, err:
                    print err.message + " under " + self.config.get(self.mainsection, section["main_section"]) \
                          +" - " +self.config.get(self.subsection, section["sub_section"])
                    pass
                self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.mainsection, section["main_section"]),
                                                              self.config.get(self.subsection, section["sub_section"]),
                                                              self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_86_To_Verify_Add_Comment_For_All_Sections(self):
        """
        Description : To test add comment in All the sections under School Data Tab.
        :return:
        """
        flag = 0
        with open(sectionfile) as data_file:
            for section in json.load(data_file):
                self.ast.schooldata_edit_comment(self.config.get(self.mainsection, section["main_section"]),
                                                 self.config.get(self.subsection, section["sub_section"]),
                                                 self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
                try:
                    self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, section["main_section"]),
                            self.config.get(self.subsection, section["sub_section"])).get_attribute("value"), "Comment")
                except Exception, err:
                    flag = 1
                    print err.message + " under " + self.config.get(self.mainsection, section["main_section"]) \
                          +" - " +self.config.get(self.subsection, section["sub_section"])
                    pass
                self.ast.schooldata_delete_comment(self.config.get(self.mainsection, section["main_section"]),
                                                 self.config.get(self.subsection, section["sub_section"]))

        if flag == 1:
            self.fail("Test has failed")