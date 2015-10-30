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
from nose.plugins.skip import SkipTest


class AssessmentSchoolDataPageTest(BaseTestCase):

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast = AssessmentPage(self.driver)
        self.schooldatasection = 'AssessmentSchoolData'
        self.mainsection = 'Sections'
        self.messages = 'Messages'
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open('baseconfig.cfg'))
        self.ast.open_schooldata_page()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        self.ast.deleteuploaded_schooldata_images(self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.ast.return_to_assessment_main_page()

    @attr(priority="high")
    @SkipTest
    def test_AST_68_To_Test_SchoolType_Radio_Button(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """
        for option in range(4):
            schooltypeoption = self.ast.get_schooldata_schooltype_radiobuttons
            if not schooltypeoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schooltypeoption[option].click()
                self.ast.save_schooldata(self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
                schoolchecked = self.ast.get_schooldata_schooltype_radiobuttons
                self.assertEqual(schoolchecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_69_1_To_Verify_Fileupload_SchoolType(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_TYPE')))
        self.ast.schooldata_upload_file(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_TYPE'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_TYPE'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_TYPE'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_69_2_To_Verify_Edit_Caption_File_SchoolType(self):
        """
        Test : test_AST_69_2
        Description : To test the add photo to school type section
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_TYPE'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_TYPE'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_TYPE'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_73_To_Verfiy_Add_Comment_SchoolType(self):
        """
        Description : To test the add comment to school type section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_TYPE'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.schooldatasection,
                                                            'SECTION_SCHOOL_TYPE')).get_attribute("value"), "Comment")


    @attr(priority="high")
    #@SkipTest
    def test_AST_74_To_Verify_SchooGrade_Checkbox(self):
        """
        Description : To test the school grade option checkbox
        :return:
        """
        for option in range(6):
            schoolgradeoption = self.ast.get_schooldata_gradelevel_checkbox
            if not schoolgradeoption[option].get_attribute("class") == "checkbox ng-binding checked":
                schoolgradeoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_schooldata(self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
                schoolgradechecked = self.ast.get_schooldata_gradelevel_checkbox
                self.assertEqual(schoolgradechecked[option].get_attribute("class"), "checkbox ng-binding checked")
                schoolgradechecked[option].click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_74_1_To_Verify_Add_Comment_SchoolGrade(self):
        """
        Description : To test the add comment to school grade section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooldatasection, 'SECTION_GRADE_LEVELS'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.schooldatasection,
                                                        'SECTION_GRADE_LEVELS')).get_attribute("value"), "Comment")

    @attr(priority="high")
    #@SkipTest
    def test_AST_74_2_To_Verify_Fileupload_SchoolGrade(self):
        """
        Description : To test the add file to school grade section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.schooldatasection, 'SECTION_GRADE_LEVELS')))
        self.ast.schooldata_upload_file(self.config.get(self.schooldatasection, 'SECTION_GRADE_LEVELS'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.schooldatasection, 'SECTION_GRADE_LEVELS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_GRADE_LEVELS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_69_2_To_Verify_Edit_Caption_File_SchoolGrade(self):
        """
        Test : test_AST_69_2
        Description : To test the add photo to school grade section
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.schooldatasection, 'SECTION_GRADE_LEVELS'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.schooldatasection, 'SECTION_GRADE_LEVELS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_GRADE_LEVELS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_75_To_Verify_SchoolHours_TextBox(self):
        """
        Description : To test the school hours section
        :return:
        """
        self.ast.get_schooldata_schoolhours_textarea.clear()
        self.ast.get_schooldata_schoolhours_textarea.send_keys("100")
        self.ast.save_schooldata(self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast._ast_schooldata_schoolhours_text_are_locator)))
        self.assertEqual(self.ast.get_schooldata_schoolhours_textarea.get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_75_1_To_Verify_Add_Comment_SchoolHours(self):
        """
        Description : To test the add comment to school hours section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_HOURS'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.schooldatasection,
                                                        'SECTION_SCHOOL_HOURS')).get_attribute("value"), "Comment")

    @attr(priority="high")
    #@SkipTest
    def test_AST_75_2_To_Verify_Fileupload_SchoolHours(self):
        """
        Description : To test the add file to school hours section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_HOURS')))
        self.ast.schooldata_upload_file(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_HOURS'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_HOURS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_HOURS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_75_3_To_Verify_Edit_Caption_File_SchoolHours(self):
        """
        Test : test_AST_69_2
        Description : To test the add photo to school grade section
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_HOURS'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_HOURS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_SCHOOL_HOURS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_78_To_Verify_Number_Of_Students_TextBox(self):
        """
        Description : To test the No of students section
        :return:
        """
        self.ast.get_schooldata_noofstudents_textarea.clear()
        self.ast.get_schooldata_noofstudents_textarea.send_keys("100")
        self.ast.save_schooldata(self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast._ast_schooldata_numberofstudents_text_are_locator)))
        self.assertEqual(self.ast.get_schooldata_noofstudents_textarea.get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_78_1_To_Verify_Add_Comment_Number_Of_Students(self):
        """
        Description : To test the add comment to no of students section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooldatasection, 'SECTION_NUMBER_OF_STUDENTS'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.schooldatasection,
                                                    'SECTION_NUMBER_OF_STUDENTS')).get_attribute("value"), "Comment")

    @attr(priority="high")
    #@SkipTest
    def test_AST_78_2_To_Verify_Fileupload_Number_Of_Students(self):
        """
        Test : test_AST_78_2
        Description : To test the add file to no of students section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.schooldatasection, 'SECTION_NUMBER_OF_STUDENTS')))
        self.ast.schooldata_upload_file(self.config.get(self.schooldatasection, 'SECTION_NUMBER_OF_STUDENTS'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertGreater(len(self.ast.get_schooldata_image(
            self.config.get(self.schooldatasection, 'SECTION_NUMBER_OF_STUDENTS'))),
            count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_NUMBER_OF_STUDENTS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_78_3_To_Verify_Edit_Caption_File_Number_Of_Students(self):
        """
        Test : test_AST_78_3
        Description : To test the add photo to no of students section
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.schooldatasection, 'SECTION_NUMBER_OF_STUDENTS'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_image_caption(
            self.config.get(self.schooldatasection, 'SECTION_NUMBER_OF_STUDENTS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_NUMBER_OF_STUDENTS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_79_To_Verify_Validation_No_Of_Students_TextBox(self):
        """
        Description : To test validations of no of students text area
        :return:
        """
        self.ast.get_schooldata_noofstudents_textarea.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_81_To_Verify_Special_Students_Text_Box(self):
        """
        Description : To test Special students section
        :return:
        """
        self.ast.get_schooldata_specialneedsstudents_textarea.clear()
        self.ast.get_schooldata_specialneedsstudents_textarea.send_keys("100")
        self.ast.save_schooldata(self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast._ast_schooldata_specialneedsstudents_text_area_locator)))
        self.assertEqual(self.ast.get_schooldata_specialneedsstudents_textarea.get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_81_1_To_Verify_Add_Comment_Special_Students(self):
        """
        Description : To test the add comment to special students section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooldatasection, 'SECTION_SPECIAL_NEEDS_STUDENT'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(
            self.schooldatasection, 'SECTION_SPECIAL_NEEDS_STUDENT')).get_attribute("value"), "Comment")


    @attr(priority="high")
    #@SkipTest
    def test_AST_81_2_To_Verify_Fileupload_Special_Students(self):
        """
        Description : To test the add file to special students section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.schooldatasection, 'SECTION_SPECIAL_NEEDS_STUDENT')))
        self.ast.schooldata_upload_file(self.config.get(self.schooldatasection, 'SECTION_SPECIAL_NEEDS_STUDENT'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(
            self.schooldatasection, 'SECTION_SPECIAL_NEEDS_STUDENT'))), count_of_image_before_upload,
            self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_SPECIAL_NEEDS_STUDENT'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_81_3_To_Verify_Edit_Caption_File_Special_Students(self):
        """
        Test : test_AST_81_3
        Description : To test the add photo to no of special students section
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.schooldatasection, 'SECTION_SPECIAL_NEEDS_STUDENT'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(
            self.schooldatasection, 'SECTION_SPECIAL_NEEDS_STUDENT'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_SPECIAL_NEEDS_STUDENT'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_84_To_Verify_No_of_Staff_Text_Box(self):
        """
        Description : To test the no of staff section
        :return:
        """
        self.ast.get_schooldata_noofstaff_textarea.clear()
        self.ast.get_schooldata_noofstaff_textarea.send_keys("100")
        self.ast.save_schooldata(self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast._ast_schooldata_numberofstaff_text_area_locator)))
        sleep(20)
        self.assertEqual(self.ast.get_schooldata_noofstaff_textarea.get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_84_1_To_Verify_Add_Comment_No_of_Staff(self):
        """
        Description : To test the add comment to no of staff section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooldatasection, 'SECTION_NO_OF_STAFF'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(
            self.config.get(self.schooldatasection, 'SECTION_NO_OF_STAFF')).get_attribute("value"), "Comment")


    @attr(priority="high")
    #@SkipTest
    def test_AST_84_2_To_Verify_fileupload_No_of_Staff(self):
        """
        Description : To test the add file to no of staff section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.schooldatasection, 'SECTION_NO_OF_STAFF')))
        self.ast.schooldata_upload_file(self.config.get(self.schooldatasection, 'SECTION_NO_OF_STAFF'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertGreater(len(self.ast.get_schooldata_image(
            self.config.get(self.schooldatasection, 'SECTION_NO_OF_STAFF'))), count_of_image_before_upload,
            self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_NO_OF_STAFF'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_84_3_To_Verify_Edit_Caption_File_Number_Of_Staff(self):
        """
        Test : test_AST_78_3
        Description : To test the add photo to no of staff section
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.schooldatasection, 'SECTION_NO_OF_STAFF'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.schooldatasection, 'SECTION_NO_OF_STAFF'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_NO_OF_STAFF'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_87_To_Verify_No_of_Visitors_TextBox(self):
        """
        Description : To test the no of visitors section
        :return:
        """
        self.ast.get_schooldata_noofvisitors_textarea.clear()
        self.ast.get_schooldata_noofvisitors_textarea.send_keys("100")
        self.ast.save_schooldata(self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast._ast_schooldata_numberofvisitors_text_area_locator)))
        sleep(20)
        self.assertEqual(self.ast.get_schooldata_noofvisitors_textarea.get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_87_1_To_Verify_Add_Comment_No_of_Visitors(self):
        """
        Description : To test the add comment to no of staff section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooldatasection, 'SECTION_NO_OF_VISITORS'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(
            self.config.get(self.schooldatasection, 'SECTION_NO_OF_VISITORS')).get_attribute("value"), "Comment")


    @attr(priority="high")
    #@SkipTest
    def test_AST_87_2_To_Verify_fileupload_No_of_Visitors(self):
        """
        Description : To test the add file to no of staff section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.schooldatasection, 'SECTION_NO_OF_VISITORS')))
        self.ast.schooldata_upload_file(self.config.get(self.schooldatasection, 'SECTION_NO_OF_VISITORS'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertGreater(len(self.ast.get_schooldata_image(
            self.config.get(self.schooldatasection, 'SECTION_NO_OF_VISITORS'))), count_of_image_before_upload,
            self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_NO_OF_VISITORS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_87_3_To_Verify_Edit_Caption_File_Number_Of_Visitors(self):
        """
        Test : test_AST_87_3
        Description : To test the add photo to no of visitors section
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.schooldatasection, 'SECTION_NO_OF_VISITORS'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_image_caption(
            self.config.get(self.schooldatasection, 'SECTION_NO_OF_VISITORS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_NO_OF_VISITORS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_88_To_Verify_validation_No_of_Visitors(self):
        """
        Description : To test the validation of no of staff section
        :return:
        """

    @attr(priority="high")
    #@SkipTest
    def test_AST_89_1_To_Verify_Police_RadioButton(self):
        """
        Description : To test the add file to no of staff section
        :return:
        """
        self.ast.get_schooldata_lawenforcement_Yes_radiobutton.click()
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
        self.ast.save_schooldata(self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_lawenforcement_Yes_radiobutton.get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")
        self.ast.get_schooldata_lawenforcement_No_radiobutton.click()
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
        self.ast.save_schooldata(self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_lawenforcement_No_radiobutton.get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_89_2_To_Verify_Add_Comment_LawEnforcement(self):
        """
        Description : To test the add comment to LawEnforcement section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooldatasection, 'SECTION_LAW_ENFORCEMENT_OFFICER'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(
            self.config.get(self.schooldatasection, 'SECTION_LAW_ENFORCEMENT_OFFICER')).get_attribute("value"), "Comment")


    @attr(priority="high")
    #@SkipTest
    def test_AST_89_3_To_Verify_fileupload_LawEnforcement(self):
        """
        Description : To test the add file to no of staff section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(
            self.config.get(self.schooldatasection, 'SECTION_LAW_ENFORCEMENT_OFFICER')))
        self.ast.schooldata_upload_file(self.config.get(self.schooldatasection, 'SECTION_LAW_ENFORCEMENT_OFFICER'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(
            self.schooldatasection, 'SECTION_LAW_ENFORCEMENT_OFFICER'))), count_of_image_before_upload,
            self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_LAW_ENFORCEMENT_OFFICER'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_89_3_To_Verify_Edit_Caption_File_LawEnforcement(self):
        """
        Test : test_AST_87_3
        Description : To test the add photo to no of visitors section
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.schooldatasection, 'SECTION_LAW_ENFORCEMENT_OFFICER'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_image_caption(
            self.config.get(self.schooldatasection, 'SECTION_LAW_ENFORCEMENT_OFFICER'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_LAW_ENFORCEMENT_OFFICER'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    # @attr(priority="high")
    # #@SkipTest
    # def test_AST_91_1_To_Verify_No_of_Visitors_TextBox(self):
    #     """
    #     Description : To test the no of visitors section
    #     :return:
    #     """
    #     self.ast.get_schooldata_nooflawenforcement_textarea.clear()
    #     self.ast.get_schooldata_nooflawenforcement_textarea.send_keys("100")
    #     self.ast.save_schooldata()
    #     WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
    #         (By.XPATH, self.ast._ast_schooldata_numberoflawenforcement_text_area_locator)))
    #     sleep(20)
    #     self.assertEqual(self.ast.get_schooldata_nooflawenforcement_textarea.get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_91_2_To_Verify_Add_Comment_No_of_LawEnforcement(self):
        """
        Description : To test the add comment to no of staff section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooldatasection, 'SECTION_NO_OF_LAW_ENFORCEMENT_OFFICER'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(
            self.config.get(self.schooldatasection, 'SECTION_NO_OF_LAW_ENFORCEMENT_OFFICER')).get_attribute("value"), "Comment")

    @attr(priority="high")
    #@SkipTest
    def test_AST_91_3_To_Verify_fileupload_No_of_LawEnforcement(self):
        """
        Description : To test the add file to no of staff section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(
            self.config.get(self.schooldatasection, 'SECTION_NO_OF_LAW_ENFORCEMENT_OFFICER')))
        self.ast.schooldata_upload_file(self.config.get(self.schooldatasection, 'SECTION_NO_OF_LAW_ENFORCEMENT_OFFICER'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertGreater(len(self.ast.get_schooldata_image(
            self.config.get(self.schooldatasection, 'SECTION_NO_OF_LAW_ENFORCEMENT_OFFICER'))), count_of_image_before_upload,
            self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_NO_OF_LAW_ENFORCEMENT_OFFICER'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_89_3_To_Verify_Edit_Caption_File_No_Of_LawEnforcement(self):
        """
        Test : test_AST_87_3
        Description : To test the add photo to no of visitors section
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.schooldatasection, 'SECTION_NO_OF_LAW_ENFORCEMENT_OFFICER'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))
        self.assertEqual(self.ast.get_schooldata_image_caption(
            self.config.get(self.schooldatasection, 'SECTION_NO_OF_LAW_ENFORCEMENT_OFFICER'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooldatasection, 'SECTION_NO_OF_LAW_ENFORCEMENT_OFFICER'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOLDATA'))