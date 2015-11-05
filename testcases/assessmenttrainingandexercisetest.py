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
from selenium.webdriver.common.keys import Keys


class AssessmentTrainningandExercisePageTest(BaseTestCase):

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast = AssessmentPage(self.driver)
        self.AssessmentSections = 'AssessmentSections'
        self.mainsection = 'TrainingExercisesMainSections'
        self.subsection = 'TrainingExercisesSubSections'
        self.messages = 'Messages'
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open('baseconfig.cfg'))
        self.ast.open_trainingandexercise_page()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        for subsection in self.config.options(self.subsection):
            self.ast.delete_attchedimage(self.config.get(self.subsection, subsection))
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
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SCHOOL'),
                self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SCHOOL'),
                    self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")
    '''
    @attr(priority="high")
    #@SkipTest
    def test_AST_140_To_Verfiy_Add_Comment_SECTION_ELECTRIC_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                                         self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                                           self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    '''
    @attr(priority="high")
    #@SkipTest
    def test_AST_292_2_To_Verfiy_Add_Comment_SchoolType_SECTION_SCHOOL_SAFETY_PLAN(self):
        """
        Description : To test the add comment to school type section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.mainsection, 'SECTION_SCHOOL'),
                                         self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, 'SECTION_SCHOOL'),
                self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.mainsection, 'SECTION_SCHOOL'),
                                           self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_292_3_To_Verify_Fileupload_SchoolType_SECTION_SCHOOL_SAFETY_PLAN(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN'),
                                        self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_293_1_To_Test_SchoolType_Radio_Button_SECTION_EXERCISE_DISTRICT_WIDE(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """
        self.ast.get_assessment_scroll.send_keys(Keys.ARROW_DOWN)
        self.ast.get_assessment_scroll.send_keys(Keys.ARROW_DOWN)
        for option in range(2):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_DISTRICT_WIDE'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                    self.config.get(self.subsection, 'SECTION_EXERCISE_DISTRICT_WIDE'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_293_2_To_Verfiy_Add_Comment_SchoolType_SECTION_EXERCISE_DISTRICT_WIDE(self):
        """
        Description : To test the add comment to school type section
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                         self.config.get(self.subsection, 'SECTION_EXERCISE_DISTRICT_WIDE'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_DISTRICT_WIDE')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                           self.config.get(self.subsection, 'SECTION_EXERCISE_DISTRICT_WIDE'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
    '''
    @attr(priority="high")
    #@SkipTest
    def test_AST_293_3_To_Verify_Fileupload_SchoolType_SECTION_EXERCISE_DISTRICT_WIDE(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN'),
                                        self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN'))),
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_DISTRICT_WIDE')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_EXERCISE_DISTRICT_WIDE'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_DISTRICT_WIDE'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_EXERCISE_DISTRICT_WIDE'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
    '''
    @attr(priority="high")
    #@SkipTest
    def test_AST_294_1_To_Test_SchoolType_Radio_Button_SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """
        self.ast.get_assessment_scroll.send_keys(Keys.ARROW_DOWN)
        self.ast.get_assessment_scroll.send_keys(Keys.ARROW_DOWN)
        for option in range(2):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                    self.config.get(self.subsection, 'SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_294_2_To_Verfiy_Add_Comment_SchoolType_SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL(self):
        """
        Description : To test the add comment to school type section
        :return:
        """

        self.ast.schooldata_edit_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                         self.config.get(self.subsection, 'SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                           self.config.get(self.subsection, 'SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_294_3_To_Verify_Fileupload_SchoolType_SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_EXERCISE_COUNTYS_MASS_CASUALTY_DRILL'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
    @attr(priority="high")
    #@SkipTest
    def test_AST_295_1_To_Test_SchoolType_Radio_Button_SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """

        for option in range(2):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                    self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_295_2_To_Verfiy_Add_Comment_SchoolType_SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT(self):
        """
        Description : To test the add comment to school type section
        :return:
        """

        self.ast.schooldata_edit_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                         self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                           self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_295_3_To_Verify_Fileupload_SchoolType_SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_296_1_To_Test_SchoolType_Radio_Button_SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """

        for option in range(3):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                    self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_296_2_To_Verfiy_Add_Comment_SchoolType_SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR(self):
        """
        Description : To test the add comment to school type section
        :return:
        """

        self.ast.schooldata_edit_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                         self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                           self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_296_3_To_Verify_Fileupload_SchoolType_SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_THE_LOCAL_FIRE_DEPARTMENT_OCCUR'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_297_1_To_Test_SchoolType_Radio_Button_SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """

        for option in range(2):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                    self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_297_2_To_Verfiy_Add_Comment_SchoolType_SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT(self):
        """
        Description : To test the add comment to school type section
        :return:
        """

        self.ast.schooldata_edit_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                         self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                           self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
    @attr(priority="high")
    #@SkipTest
    def test_AST_297_3_To_Verify_Fileupload_SchoolType_SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_298_1_To_Test_SchoolType_Radio_Button_SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """

        for option in range(3):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                    self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_298_2_To_Verfiy_Add_Comment_SchoolType_SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR(self):
        """
        Description : To test the add comment to school type section
        :return:
        """

        self.ast.schooldata_edit_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                         self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                           self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_298_3_To_Verify_Fileupload_SchoolType_SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_EXERCISE_DRILLS_WITH_LOCAL_LAW_ENFORCEMENT_OCCUR'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_299_1_To_Test_SchoolType_Radio_Button_SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """

        for option in range(4):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                    self.config.get(self.subsection, 'SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_299_2_To_Verfiy_Add_Comment_SchoolType_SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED(self):
        """
        Description : To test the add comment to school type section
        :return:
        """

        self.ast.schooldata_edit_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                         self.config.get(self.subsection, 'SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                self.config.get(self.subsection, 'SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.mainsection, 'SECTION_EXERCISE'),
                                           self.config.get(self.subsection, 'SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED'),
                                         self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_299_3_To_Verify_Fileupload_SchoolType_SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_EXERCISE_CRISIS_INCIDENT_MANAGEMENT_EXERCISED'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_300_1_To_Test_SchoolType_Radio_Button_SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS_AGAINST_THE_SCHOOL_OR_STUDENTS(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """

        for option in range(4):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EMERGENCY_CHECKLIST'),
                self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS_AGAINST_THE_SCHOOL_OR_STUDENTS'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EMERGENCY_CHECKLIST'),
                    self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS_AGAINST_THE_SCHOOL_OR_STUDENTS'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_300_2_To_Verfiy_Add_Comment_SchoolType_SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS_AGAINST_THE_SCHOOL_OR_STUDENTS(self):
        """
        Description : To test the add comment to school type section
        :return:
        """

        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS_AGAINST_THE_SCHOOL_OR_STUDENTS'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS_AGAINST_THE_SCHOOL_OR_STUDENTS')).get_attribute("value"), "Comment")

        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS_AGAINST_THE_SCHOOL_OR_STUDENTS'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_300_3_To_Verify_Fileupload_SchoolType_SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACKS'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_301_1_To_Test_SchoolType_Radio_Button_SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """

        for option in range(4):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EMERGENCY_CHECKLIST'),
                self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_EMERGENCY_CHECKLIST'),
                    self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_301_2_To_Verfiy_Add_Comment_SchoolType_SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN(self):
        """
        Description : To test the add comment to school type section
        :return:
        """

        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN')).get_attribute("value"), "Comment")

        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_301_3_To_Verify_Fileupload_SchoolType_SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_TRAINED_IN_THE_REUNIFICATION_PLAN'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_303_1_To_Verfiy_textarea_SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS')).get_attribute("value"), "100")



    @attr(priority="high")
    #@SkipTest
    def test_AST_303_2_To_Verify_Fileupload_SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_303_3_To_Verify_Edit_Caption_SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS'),
                                               self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_303_4_To_Verfiy_Add_Comment_SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_304_1_To_Test_SchoolType_Radio_Button_SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """

        for option in range(3):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT'),
                self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT'),
                    self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_304_2_To_Verfiy_Add_Comment_SchoolType_SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY(self):
        """
        Description : To test the add comment to school type section
        :return:
        """

        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY')).get_attribute("value"), "Comment")

        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_304_3_To_Verify_Fileupload_SchoolType_SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_COMMAND_TEAM_TRAINED_REGULARLY'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_305_1_To_Test_SchoolType_Radio_Button_SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """

        for option in range(2):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT'),
                self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT'),
                    self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_305_2_To_Verfiy_Add_Comment_SchoolType_SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST(self):
        """
        Description : To test the add comment to school type section
        :return:
        """

        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST')).get_attribute("value"), "Comment")

        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_305_3_To_Verify_Fileupload_SchoolType_SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_STAFF_WOULD_NEED_LIST'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_306_1_To_Test_SchoolType_Radio_Button_SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY(self):
        """
        Description : To test the school type option radio buttons
        :return:
        """

        for option in range(2):
            schoolsafetyoptions = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT'),
                self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY'))
            if not schoolsafetyoptions[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                schoolsafetyoptions[option].click()
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                self.ast.get_assessment_scroll.send_keys(Keys.ARROW_UP)
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                schoolsafetychecked = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT'),
                    self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY'))
                self.assertEqual(schoolsafetychecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_306_2_To_Verfiy_Add_Comment_SchoolType_SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY(self):
        """
        Description : To test the add comment to school type section
        :return:
        """

        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY')).get_attribute("value"), "Comment")

        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY'),
                                         self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_306_3_To_Verify_Fileupload_SchoolType_SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY(self):
        """
        Test : test_AST_69
        Description : To test the add photo to school type section
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY'),
                                        self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_MANAGEMENT_IMPACT_YOUR_SCHOOL_SAFETY'),
                                                      self.config.get(self.mainsection, 'MAIN_TRAINING_EXERCISE'))

