__author__ = 'Deepa.Sivadas'
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.assessmentpage import AssessmentPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
import ConfigParser
import os, json
from time import sleep


cwd = os.getcwd()
os.chdir('..')
sectionfile = os.path.join(os.getcwd(), "data", "json_assessment_physicalsecurity_sections.json")
os.chdir(cwd)

class AssessmentPhysicalSecuritiesPageTest(BaseTestCase):

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast = AssessmentPage(self.driver)
        self.AssessmentSections = 'AssessmentSections'
        self.messages = 'Messages'
        self.mainsection = 'PhysicalSecurityMainSection'
        self.subsection = 'PhysicalSecuritySubSection'
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open('baseconfig.cfg'))
        self.ast.open_physicalsecurity_page()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        for subsection in self.config.options(self.subsection):
            self.ast.delete_attchedimage(self.config.get(self.subsection, subsection))
        self.ast.get_overview_button.click()
        self.ast.return_to_assessment_main_page()

    @attr(priority="high")
    #@SkipTest
    def test_AST_167(self):
        """
        Description :
        :return:
        """
        for option in range(10):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
            self.config.get(self.subsection, 'SECTION_PERIMETER_TYPE_OF_WALL'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
                                                    self.config.get(self.subsection, 'SECTION_PERIMETER_TYPE_OF_WALL'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_168_SECTION_PERIMETER_FENCING_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(6):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
            self.config.get(self.subsection, 'SECTION_PERIMETER_FENCING'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
                                                    self.config.get(self.subsection, 'SECTION_PERIMETER_FENCING'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_169_SECTION_PERIMETER_GATES_LOCKED_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
            self.config.get(self.subsection, 'SECTION_PERIMETER_GATES_LOCKED'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
                                                    self.config.get(self.subsection, 'SECTION_PERIMETER_GATES_LOCKED'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_170_SECTION_SECTION_PERIMETER_SAME_KEY_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
            self.config.get(self.subsection, 'SECTION_PERIMETER_SAME_KEY'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
                                                    self.config.get(self.subsection, 'SECTION_PERIMETER_SAME_KEY'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_171_SECTION_PERIMETER_ADDITIONAL_FENCING_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
            self.config.get(self.subsection, 'SECTION_PERIMETER_ADDITIONAL_FENCING'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
                                                    self.config.get(self.subsection, 'SECTION_PERIMETER_ADDITIONAL_FENCING'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_172_SECTION_CCTV_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CCTV'),
            self.config.get(self.subsection, 'SECTION_CCTV'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                                    self.config.get(self.subsection, 'SECTION_CCTV'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_173_SECTION_CCTV_Text_Box(self):
        """
        Description :
        :return:
        """
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                                  self.config.get(self.subsection, 'SECTION_CCTC_NO_OF_CAMERAS')).clear()
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                                  self.config.get(self.subsection, 'SECTION_CCTC_NO_OF_CAMERAS')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_locator(self.config.get(self.mainsection, 'SECTION_CCTV'),
                self.config.get(self.subsection, 'SECTION_CCTC_NO_OF_CAMERAS')))))
        self.assertEqual(self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_CCTV'),
                            self.config.get(self.subsection, 'SECTION_CCTC_NO_OF_CAMERAS')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_173_1_SECTION_CCTV_Text_Box_Validation(self):
        """
        Description :
        :return:
        """
        validation_input = ['abc', 'ABC', '@#', 'aB1@']
        for item in validation_input:
            self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                                      self.config.get(self.subsection, 'SECTION_CCTC_NO_OF_CAMERAS')).send_keys("")
            self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                                      self.config.get(self.subsection, 'SECTION_CCTC_NO_OF_CAMERAS')).send_keys(item)
            self.assertEqual(self.ast.get_schooldata_textbox_error(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                self.config.get(self.subsection, 'SECTION_CCTC_NO_OF_CAMERAS')).text, "Enter a number",
                             self.config.get(self.messages, 'MESSAGE_VALIDATION_ERROR'))
            self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                                      self.config.get(self.subsection, 'SECTION_CCTC_NO_OF_CAMERAS')).clear()

    @attr(priority="high")
    #@SkipTest
    def test_AST_174_SECTION_CCTV_ADDITIONAL_CAMERAS_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CCTV'),
            self.config.get(self.subsection, 'SECTION_CCTV_ADDITIONAL_CAMERAS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                                    self.config.get(self.subsection, 'SECTION_CCTV_ADDITIONAL_CAMERAS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_175_SECTION_CCTV_NO_OF_ADDITIONAL_CAMERAS_Text_Box(self):
        """
        Description :
        :return:
        """
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                                  self.config.get(self.subsection, 'SECTION_CCTV_NO_OF_ADDITIONAL_CAMERAS')).clear()
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                                  self.config.get(self.subsection, 'SECTION_CCTV_NO_OF_ADDITIONAL_CAMERAS')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_locator(self.config.get(self.mainsection, 'SECTION_CCTV'),
                self.config.get(self.subsection, 'SECTION_CCTV_NO_OF_ADDITIONAL_CAMERAS')))))
        self.assertEqual(self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_CCTV'),
                            self.config.get(self.subsection, 'SECTION_CCTV_NO_OF_ADDITIONAL_CAMERAS')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_176_SECTION_LOCKS_AVAILABILITY_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LOCK'),
            self.config.get(self.subsection, 'SECTION_LOCKS_AVAILABILITY'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LOCK'),
                                                    self.config.get(self.subsection, 'SECTION_LOCKS_AVAILABILITY'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_177_SECTION_LOCK_MAIN_ENTRANCE_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LOCK'),
            self.config.get(self.subsection, 'SECTION_LOCK_MAIN_ENTRANCE'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LOCK'),
                                                    self.config.get(self.subsection, 'SECTION_LOCK_MAIN_ENTRANCE'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_178_SECTION_LOCK_OTHER_PARTS_Check_Box(self):
        """
        Description :
        :return:
        """
        for option in range(13):
            locksoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_LOCK'),
                                                    self.config.get(self.subsection, 'SECTION_LOCK_OTHER_PARTS'))
            if not locksoption[option].get_attribute("class") == "checkbox ng-binding checked":
                locksoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                locksoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_LOCK'),
                                                    self.config.get(self.subsection, 'SECTION_LOCK_OTHER_PARTS'))
                self.assertEqual(locksoption[option].get_attribute("class"), "checkbox ng-binding checked")
                locksoption[option].click()


    @attr(priority="high")
    #@SkipTest
    def test_AST_179_SECTION_IDENTIFICATION_CARDS_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_CARDS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_CARDS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_180_SECTION_IDENTIFICATION_PHOTOGRAPH_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_PHOTOGRAPH'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_PHOTOGRAPH'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_181_SECTION_IDENTIFICATION_STUDENT_PHOTOGRAPH_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_STUDENT_PHOTOGRAPH'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_STUDENT_PHOTOGRAPH'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_182_SECTION_IDENTIFICATION_VISITOR_SIGN_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_VISITOR_SIGN'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_VISITOR_SIGN'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_182_SECTION_IDENTIFICATION_TEMPORARY_ID_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_TEMPORARY_ID'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_TEMPORARY_ID'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_183_SECTION_IDENTIFICATION_VISITOR_CHECKOUT_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_VISITOR_CHECKOUT'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_VISITOR_CHECKOUT'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_184_SECTION_IDENTIFICATION_DISTRICT_STAFF_CHECKIN_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_DISTRICT_STAFF_CHECKIN'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_DISTRICT_STAFF_CHECKIN'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_185_SECTION_IDENTIFICATION_DISTRICT_STAFF_PHOTOGRAPH_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_DISTRICT_STAFF_PHOTOGRAPH'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_DISTRICT_STAFF_PHOTOGRAPH'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_186_SECTION_LIGHTING_DARK_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
            self.config.get(self.subsection, 'SECTION_LIGHTING_DARK'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
                                                    self.config.get(self.subsection, 'SECTION_LIGHTING_DARK'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_187_SECTION_LIGHTING_CONTROL_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
            self.config.get(self.subsection, 'SECTION_LIGHTING_CONTROL'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
                                                    self.config.get(self.subsection, 'SECTION_LIGHTING_CONTROL'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_188_SECTION_LIGHTING_ADDITIONAL_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
            self.config.get(self.subsection, 'SECTION_LIGHTING_ADDITIONAL'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
                                                    self.config.get(self.subsection, 'SECTION_LIGHTING_ADDITIONAL'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_189_SECTION_ALARMS_ACCESSALARMS_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
            self.config.get(self.subsection, 'SECTION_ALARMS_ACCESSALARMS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
                                                    self.config.get(self.subsection, 'SECTION_ALARMS_ACCESSALARMS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_190_SECTION_ALARM_MONITORS_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
            self.config.get(self.subsection, 'SECTION_ALARM_MONITORS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
                                                    self.config.get(self.subsection, 'SECTION_ALARM_MONITORS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_191_SECTION_ALARMS_PANICALARMS_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
            self.config.get(self.subsection, 'SECTION_ALARMS_PANICALARMS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
                                                    self.config.get(self.subsection, 'SECTION_ALARMS_PANICALARMS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_192_SECTION_ALARMS_KEYINDIVIDUAL_PANICALARM_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
            self.config.get(self.subsection, 'SECTION_ALARMS_KEYINDIVIDUAL_PANICALARM'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
                                                    self.config.get(self.subsection, 'SECTION_ALARMS_KEYINDIVIDUAL_PANICALARM'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_193_SECTION_BIOMETRIC_AVAILABILITY_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
            self.config.get(self.subsection, 'SECTION_BIOMETRIC_AVAILABILITY'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
                                                    self.config.get(self.subsection, 'SECTION_BIOMETRIC_AVAILABILITY'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_194_SECTION_BIOMETRIC_CHARACTERESTICS_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(5):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
            self.config.get(self.subsection, 'SECTION_BIOMETRIC_CHARACTERESTICS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
                                                    self.config.get(self.subsection, 'SECTION_BIOMETRIC_CHARACTERESTICS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_195_SECTION_BIOMETRIC_LOCK_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
            self.config.get(self.subsection, 'SECTION_BIOMETRIC_LOCK'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
                                                    self.config.get(self.subsection, 'SECTION_BIOMETRIC_LOCK'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_196_SECTION_BIOMETRIC_OTHERPARTS_Check_box(self):
        """
        Description :
        :return:
        """
        for option in range(13):
            biometricoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
                                                    self.config.get(self.subsection, 'SECTION_BIOMETRIC_OTHERPARTS'))
            if not biometricoption[option].get_attribute("class") == "checkbox ng-binding checked":
                biometricoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                biometricoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
                                                    self.config.get(self.subsection, 'SECTION_BIOMETRIC_OTHERPARTS'))
                self.assertEqual(biometricoption[option].get_attribute("class"), "checkbox ng-binding checked")
                biometricoption[option].click()



    @attr(priority="high")
    #@SkipTest
    def test_AST_197_SECTION_SECURITY_SWORN_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
            self.config.get(self.subsection, 'SECTION_SECURITY_SWORN'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_SWORN'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_198_SECTION_SECURITY_SRO_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
            self.config.get(self.subsection, 'SECTION_SECURITY_SRO'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_SRO'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_199_SECTION_SECUTITY_GUARD_Text_box(self):
        """
        Description :
        :return:
        """
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                  self.config.get(self.subsection, 'SECTION_SECUTITY_GUARD')).clear()
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                  self.config.get(self.subsection, 'SECTION_SECUTITY_GUARD')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_locator(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                self.config.get(self.subsection, 'SECTION_SECUTITY_GUARD')))))
        self.assertEqual(self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                            self.config.get(self.subsection, 'SECTION_SECUTITY_GUARD')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_200_SECTION_SECURITY_SECTION_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
            self.config.get(self.subsection, 'SECTION_SECURITY_SECTION'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_SECTION'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_201_SECTION_SECURITY_CHARACTERISTICS_Check_box(self):
        """
        Description :
        :return:
        """
        for option in range(6):
            characteristicsoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_CHARACTERISTICS'))
            if not characteristicsoption[option].get_attribute("class") == "checkbox ng-binding checked":
                characteristicsoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                characteristicsoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_CHARACTERISTICS'))
                self.assertEqual(characteristicsoption[option].get_attribute("class"), "checkbox ng-binding checked")
                characteristicsoption[option].click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_202_SECTION_SECURITY_ADDITIONAL_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
            self.config.get(self.subsection, 'SECTION_SECURITY_ADDITIONAL'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_ADDITIONAL'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_203_SECTION_SECURITY_ADDITIONAL_HOWMANY_Text_box(self):
        """
        Description :
        :return:
        """
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                  self.config.get(self.subsection, 'SECTION_SECURITY_ADDITIONAL_HOWMANY')).clear()
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                  self.config.get(self.subsection, 'SECTION_SECURITY_ADDITIONAL_HOWMANY')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_locator(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                self.config.get(self.subsection, 'SECTION_SECURITY_ADDITIONAL_HOWMANY')))))
        self.assertEqual(self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                            self.config.get(self.subsection, 'SECTION_SECURITY_ADDITIONAL_HOWMANY')).get_attribute("value"), "100")



    @attr(priority="high")
    #@SkipTest
    def test_AST_204_SECTION_ROOFACCESS_DESCRIPTION_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ROOFACCESS'),
            self.config.get(self.subsection, 'SECTION_ROOFACCESS_DESCRIPTION'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ROOFACCESS'),
                                                    self.config.get(self.subsection, 'SECTION_ROOFACCESS_DESCRIPTION'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")
    @attr(priority="high")
    #@SkipTest
    def test_AST_205_SECTION_ROOFACCESS_ACCESS_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ROOFACCESS'),
            self.config.get(self.subsection, 'SECTION_ROOFACCESS_ACCESS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ROOFACCESS'),
                                                    self.config.get(self.subsection, 'SECTION_ROOFACCESS_ACCESS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")
    @attr(priority="high")
    #@SkipTest
    def test_AST_206_SECTION_PHYSICALKEY_AREA_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
            self.config.get(self.subsection, 'SECTION_PHYSICALKEY_AREA'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
                                                    self.config.get(self.subsection, 'SECTION_PHYSICALKEY_AREA'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")
    @attr(priority="high")
    #@SkipTest
    def test_AST_207_SECTION_PHYSICALKEY_POSITION_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
            self.config.get(self.subsection, 'SECTION_PHYSICALKEY_POSITION'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
                                                    self.config.get(self.subsection, 'SECTION_PHYSICALKEY_POSITION'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")
    @attr(priority="high")
    #@SkipTest
    def test_AST_208_SECTION_PHYSICALKEY_PoC_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
            self.config.get(self.subsection, 'SECTION_PHYSICALKEY_PoC'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
                                                    self.config.get(self.subsection, 'SECTION_PHYSICALKEY_PoC'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

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
                                                self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
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
                                                self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))

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
                                                       self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                try:
                    self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.mainsection, section["main_section"]),
                                                self.config.get(self.subsection, section["sub_section"]))[0].text, "Hello")
                except Exception, err:
                    print err.message + " under " + self.config.get(self.mainsection, section["main_section"]) \
                          +" - " +self.config.get(self.subsection, section["sub_section"])
                self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.mainsection, section["main_section"]),
                                                              self.config.get(self.subsection, section["sub_section"]),
                                                              self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))


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
                                                 self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                try:
                    self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, section["main_section"]),
                            self.config.get(self.subsection, section["sub_section"])).get_attribute("value"), "Comment")
                except Exception, err:
                    flag = 1
                    print err.message + " under " + self.config.get(self.mainsection, section["main_section"]) \
                          +" - " +self.config.get(self.subsection, section["sub_section"])
                self.ast.schooldata_delete_comment(self.config.get(self.mainsection, section["main_section"]),
                                                 self.config.get(self.subsection, section["sub_section"]),
                                                 self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
        if flag == 1:
            self.fail("Test has failed : Check log file")
