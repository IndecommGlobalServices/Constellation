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
import os, json

cwd = os.getcwd()
os.chdir('..')
sectionfile = os.path.join(os.getcwd(), "data", "json_assessment_training_n_exercise_sections.json")
os.chdir(cwd)

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


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_303_1_To_Verfiy_textarea_SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS(self):
        self.ast.get_schooldata_textarea(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(
                self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.subsection, 'SECTION_EXERCISES_OR_DRILLS_LIST_OTHER_DRILLS')).get_attribute("value"), "100")



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
    def test_AST_To_Verify_Fileupload(self):
        """
        Description : To test fileupload in SECTION_PERIMETER_TYPE_OF_WALL
        :return:
        """
        with open(sectionfile) as data_file:
            for section in json.load(data_file):
                count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(
                                        self.mainsection, section["main_section"]),
                                        self.config.get(self.subsection, section["sub_section"])))
                self.ast.schooldata_upload_file(self.config.get(self.mainsection, section["main_section"]),
                                                self.config.get(self.subsection, section["sub_section"]),
                                                self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                try:
                    self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(
                                                    self.mainsection, section["main_section"]),
                                                    self.config.get(self.subsection, section["sub_section"]))),
                                                    count_of_image_before_upload, self.config.get(
                                                    self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
                except Exception, err:
                    print err.message + " under " + self.config.get(self.mainsection, section["main_section"]) \
                          +" - " +self.config.get(self.subsection, section["sub_section"])

                self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.mainsection, section["main_section"]),
                                                self.config.get(self.subsection, section["sub_section"]),
                                                self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_To_Verify_Edit_Caption(self):
        """
        Description : To test edit caption
        :return:
        """
        with open(sectionfile) as data_file:
            for section in json.load(data_file):
                self.ast.schooldata_edit_caption_image(self.config.get(self.mainsection, section["main_section"]),
                                                       self.config.get(self.subsection, section["sub_section"]),
                                                       self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                try:
                    self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.mainsection, section["main_section"]),
                                                self.config.get(self.subsection, section["sub_section"]))[0].text, "Hello")
                except Exception, err:
                    print err.message + " under " + self.config.get(self.mainsection, section["main_section"]) \
                          +" - " +self.config.get(self.subsection, section["sub_section"])
                self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.mainsection, section["main_section"]),
                                                              self.config.get(self.subsection, section["sub_section"]),
                                                              self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_To_Verfiy_Add_Comment(self):
        """
        Description : To test add comment in
        :return:
        """
        flag = 0
        with open(sectionfile) as data_file:
            for section in json.load(data_file):
                self.ast.schooldata_edit_comment(self.config.get(self.mainsection, section["main_section"]),
                                                 self.config.get(self.subsection, section["sub_section"]),
                                                 self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
                try:
                    self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, section["main_section"]),
                            self.config.get(self.subsection, section["sub_section"])).get_attribute("value"), "Comment")
                except Exception, err:
                    flag = 1
                    print err.message + " under " + self.config.get(self.mainsection, section["main_section"]) \
                          +" - " +self.config.get(self.subsection, section["sub_section"])
                self.ast.schooldata_delete_comment(self.config.get(self.mainsection, section["main_section"]),
                                                 self.config.get(self.subsection, section["sub_section"]),
                                                 self.config.get(self.AssessmentSections, 'MAIN_TRAINING_EXERCISE'))
        if flag == 1:
            self.fail("Test has failed")