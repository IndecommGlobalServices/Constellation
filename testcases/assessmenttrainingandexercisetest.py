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
        self.ast.return_to_assessment_main_page()


    @attr(priority="high")
    #@SkipTest
    def test_AST_292_1_To_Test_SchoolType_Radio_Button(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """
        for option in range(4):
            schoolsafetyoptions = self.ast.get_trainningandexercises_schoolsafety_radiobutton
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_trainingandexercisedata()
                schoolsafetychecked = self.ast.get_trainningandexercises_schoolsafety_radiobutton
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_292_2_To_Verfiy_Add_Comment_SchoolType(self):
        """
        Description : To test the add comment to school type section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.schooltrainingsection, 'SECTION_SCHOOL_SAFETY_PLAN'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.schooltrainingsection,
                                                            'SECTION_SCHOOL_SAFETY_PLAN')).get_attribute("value"), "Comment")

    @attr(priority="high")
    #@SkipTest
    def test_AST_292_3_To_Verify_Fileupload_SchoolType(self):
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