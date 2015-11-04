__author__ = 'Deepa.Sivadas'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.assessmentpage import AssessmentPage
from pages.loginpage import LoginPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from time import sleep
import ConfigParser


class AssessmentTrainningandExercisePageTest(BaseTestCase):

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast = AssessmentPage(self.driver)
        self.schooltrainingsection = 'TrainingExercises'
        self.mainsection = 'Sections'
        self.messages = 'Messages'
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open('baseconfig.cfg'))
        self.ast.open_trainingandexercise_page()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        for section in self.config.options(self.schooltrainingsection):
            self.ast.delete_attchedimage(self.config.get(self.schooltrainingsection, section))
        self.ast.get_overview_button.click()
        self.ast.return_to_assessment_main_page()




    @attr(priority="high")
    #@SkipTest
    def test_AST_292_1_To_Test_SchoolType_Radio_Button_SECTION_SCHOOL_SAFETY_PLAN(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """
        for option in range(4):
            schoolsafetyoptions = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.schooltrainingsection, 'SECTION_SCHOOL_SAFETY_PLAN'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schoolInfrastucture_radiobutton(
                    self.config.get(self.schooltrainingsection, 'SECTION_SCHOOL_SAFETY_PLAN'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_292_2_To_Verfiy_Add_Comment_SchoolType_SECTION_SCHOOL_SAFETY_PLAN(self):
        """
        Description : To test the add comment to school type section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooltrainingsection, 'SECTION_SCHOOL_SAFETY_PLAN'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.schooltrainingsection,
                                                            'SECTION_SCHOOL_SAFETY_PLAN')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.schooltrainingsection, 'SECTION_SCHOOL_SAFETY_PLAN'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_292_3_To_Verify_Fileupload_SchoolType_SECTION_SCHOOL_SAFETY_PLAN(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.schooltrainingsection, 'SECTION_SCHOOL_SAFETY_PLAN')))
        self.ast.schooldata_upload_file(self.config.get(self.schooltrainingsection, 'SECTION_SCHOOL_SAFETY_PLAN'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.schooltrainingsection, 'SECTION_SCHOOL_SAFETY_PLAN'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooltrainingsection, 'SECTION_SCHOOL_SAFETY_PLAN'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_293_1_To_Test_SchoolType_Radio_Button_SECTION_EXERCISE_DISTRICT_WIDE(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """
        #self.ast.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        #self.ast.get_map_scroll.send_keys(Keys.ARROW_DOWN)
        for option in range(2):
            schoolsafetyoptions = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.schooltrainingsection, 'SECTION_EXERCISE_DISTRICT_WIDE'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schoolInfrastucture_radiobutton(
                    self.config.get(self.schooltrainingsection, 'SECTION_EXERCISE_DISTRICT_WIDE'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_293_2_To_Verfiy_Add_Comment_SchoolType_SECTION_EXERCISE_DISTRICT_WIDE(self):
        """
        Description : To test the add comment to school type section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooltrainingsection, 'SECTION_EXERCISE_DISTRICT_WIDE'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.schooltrainingsection,
                                                            'SECTION_EXERCISE_DISTRICT_WIDE')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.schooltrainingsection, 'SECTION_EXERCISE_DISTRICT_WIDE'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_293_3_To_Verify_Fileupload_SchoolType_SECTION_EXERCISE_DISTRICT_WIDE(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.schooltrainingsection, 'SECTION_EXERCISE_DISTRICT_WIDE')))
        self.ast.schooldata_upload_file(self.config.get(self.schooltrainingsection, 'SECTION_EXERCISE_DISTRICT_WIDE'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.schooltrainingsection, 'SECTION_EXERCISE_DISTRICT_WIDE'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooltrainingsection, 'SECTION_EXERCISE_DISTRICT_WIDE'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_139_To_Verify_Edit_Caption_SECTION_EXERCISE_DISTRICT_WIDE(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.schooltrainingsection, 'SECTION_EXERCISE_DISTRICT_WIDE'),
                                               self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.schooltrainingsection, 'SECTION_EXERCISE_DISTRICT_WIDE'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.schooltrainingsection, 'SECTION_EXERCISE_DISTRICT_WIDE'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))