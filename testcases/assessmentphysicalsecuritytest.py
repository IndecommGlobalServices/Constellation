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
from nose.plugins.skip import SkipTest


cwd = os.getcwd()
os.chdir('..')
sectionfile = os.path.join(os.getcwd(), "data", "json_assessment_physicalsecurity_sections.json")
os.chdir(cwd)

class AssessmentPhysicalSecuritiesPageTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(AssessmentPhysicalSecuritiesPageTest, cls).setUpClass()
        cls.AssessmentSections = 'AssessmentSections'
        cls.messages = 'Messages'
        cls.mainsection = 'PhysicalSecurityMainSection'
        cls.subsection = 'PhysicalSecuritySubSection'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))
        cls.ast = AssessmentPage(cls.driver)
        cls.ast.logintoapp()
        try:
            cls.ast.get_asset_avilability(cls.config.get(cls.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
            cls.ast.delete_existing_assessments()
            cls.ast.create_initial_assessment()
        except:
            pass

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast.open_main_section(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        for subsection in self.config.options(self.subsection):
            self.ast.delete_attchedimage(self.config.get(self.subsection, subsection))
        self.ast.get_overview_button.click()
        self.ast.return_to_assessment_main_page()

    @attr(priority="high")
    #@SkipTest
    def test_AST_164_To_Verify_Type_Of_Wall_Fencing_RadioButton(self):
        """
        Description :
        :return:
        """
        for option in range(10):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
            self.config.get(self.subsection, 'SECTION_PERIMETER_TYPE_OF_WALL'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
                                                    self.config.get(self.subsection, 'SECTION_PERIMETER_TYPE_OF_WALL'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_165_To_Test_Site_Secured_By_Fencing_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(6):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
            self.config.get(self.subsection, 'SECTION_PERIMETER_FENCING'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
                                                    self.config.get(self.subsection, 'SECTION_PERIMETER_FENCING'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_166_To_Test_Gate_Locked_Nightly_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
            self.config.get(self.subsection, 'SECTION_PERIMETER_GATES_LOCKED'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
                                                    self.config.get(self.subsection, 'SECTION_PERIMETER_GATES_LOCKED'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_167_To_Test_Gate_Same_Key_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
            self.config.get(self.subsection, 'SECTION_PERIMETER_SAME_KEY'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
                                                    self.config.get(self.subsection, 'SECTION_PERIMETER_SAME_KEY'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_168_To_Test_Additional_Fencing_Required_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
            self.config.get(self.subsection, 'SECTION_PERIMETER_ADDITIONAL_FENCING'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PERIMETER'),
                                                    self.config.get(self.subsection, 'SECTION_PERIMETER_ADDITIONAL_FENCING'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_170_To_Test_CCTV_System_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CCTV'),
            self.config.get(self.subsection, 'SECTION_CCTV'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                                    self.config.get(self.subsection, 'SECTION_CCTV'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_171_To_Test_CCTV_Cameras_On_Campus_Text_Box(self):
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
    def test_AST_173_SECTION_CCTV_ADDITIONAL_CAMERAS_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CCTV'),
            self.config.get(self.subsection, 'SECTION_CCTV_ADDITIONAL_CAMERAS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_CCTV'),
                                                    self.config.get(self.subsection, 'SECTION_CCTV_ADDITIONAL_CAMERAS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_174_1_To_Test_No_Of_CCTV_Additional_Cameras_Text_Box(self):
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
    def test_AST_174_2_To_Test_No_Of_CCTV_Additional_Cameras_Text_Box(self):
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
    def test_AST_176_To_Test_Electronics_Locks_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LOCK'),
            self.config.get(self.subsection, 'SECTION_LOCKS_AVAILABILITY'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LOCK'),
                                                    self.config.get(self.subsection, 'SECTION_LOCKS_AVAILABILITY'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_178_To_Test_Main_Entrance_Electronics_Lock_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LOCK'),
            self.config.get(self.subsection, 'SECTION_LOCK_MAIN_ENTRANCE'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LOCK'),
                                                    self.config.get(self.subsection, 'SECTION_LOCK_MAIN_ENTRANCE'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_179_To_Test_Electronics_Lock_Other_Parts_Check_Box(self):
        """
        Description :
        :return:
        """
        for option in range(13):
            locksoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_LOCK'),
                                                    self.config.get(self.subsection, 'SECTION_LOCK_OTHER_PARTS'))
            if not locksoption[option].get_attribute("class") == "checkbox ng-binding checked":
                locksoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                locksoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_LOCK'),
                                                    self.config.get(self.subsection, 'SECTION_LOCK_OTHER_PARTS'))
                self.assertEqual(locksoption[option].get_attribute("class"), "checkbox ng-binding checked")
                locksoption[option].click()


    @attr(priority="high")
    #@SkipTest
    def test_AST_182_To_Test_Identification_Card_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_CARDS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_CARDS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_183_To_Test_Employee_Identification_Photograph_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_PHOTOGRAPH'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_PHOTOGRAPH'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_184_To_Test_Student_Identification_Photograph_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_STUDENT_PHOTOGRAPH'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_STUDENT_PHOTOGRAPH'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_185_To_Test_Identification_Visitor_Sign_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_VISITOR_SIGN'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_VISITOR_SIGN'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_186_To_Test_Identification_Temporary_Id_For_Visitor_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_TEMPORARY_ID'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_TEMPORARY_ID'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_187_To_Test_Identification_Visitor_Sign_Checkout_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_VISITOR_CHECKOUT'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_VISITOR_CHECKOUT'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_188_To_Test_Identification_District_Staff_Check_In_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_DISTRICT_STAFF_CHECKIN'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_DISTRICT_STAFF_CHECKIN'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_190_To_Test_Identification_District_Staff_Photograph_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
            self.config.get(self.subsection, 'SECTION_IDENTIFICATION_DISTRICT_STAFF_PHOTOGRAPH'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_IDENTIFICATION'),
                                                    self.config.get(self.subsection, 'SECTION_IDENTIFICATION_DISTRICT_STAFF_PHOTOGRAPH'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_191_To_Test_Lighting_Dark_Campus_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
            self.config.get(self.subsection, 'SECTION_LIGHTING_DARK'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
                                                    self.config.get(self.subsection, 'SECTION_LIGHTING_DARK'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_192_To_Test_Lighting_Control_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
            self.config.get(self.subsection, 'SECTION_LIGHTING_CONTROL'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
                                                    self.config.get(self.subsection, 'SECTION_LIGHTING_CONTROL'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_193_To_Test_Lighting_Additional_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
            self.config.get(self.subsection, 'SECTION_LIGHTING_ADDITIONAL'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LIGHTING'),
                                                    self.config.get(self.subsection, 'SECTION_LIGHTING_ADDITIONAL'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_195_To_Test_Alarms_Access_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
            self.config.get(self.subsection, 'SECTION_ALARMS_ACCESSALARMS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
                                                    self.config.get(self.subsection, 'SECTION_ALARMS_ACCESSALARMS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_197_To_Test_Alarms_Monitors_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
            self.config.get(self.subsection, 'SECTION_ALARM_MONITORS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
                                                    self.config.get(self.subsection, 'SECTION_ALARM_MONITORS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_199_To_Test_Alarms_Panic_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
            self.config.get(self.subsection, 'SECTION_ALARMS_PANICALARMS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
                                                    self.config.get(self.subsection, 'SECTION_ALARMS_PANICALARMS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_201_To_Test_Alarms_Key_Individual_Panic_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
            self.config.get(self.subsection, 'SECTION_ALARMS_KEYINDIVIDUAL_PANICALARM'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ALARMS'),
                                                    self.config.get(self.subsection, 'SECTION_ALARMS_KEYINDIVIDUAL_PANICALARM'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_203_To_Test_Biometric_Locks_Availability_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
            self.config.get(self.subsection, 'SECTION_BIOMETRIC_AVAILABILITY'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
                                                    self.config.get(self.subsection, 'SECTION_BIOMETRIC_AVAILABILITY'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_205_To_Test_Biometric_Locks_Characteristic_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(5):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
            self.config.get(self.subsection, 'SECTION_BIOMETRIC_CHARACTERESTICS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
                                                    self.config.get(self.subsection, 'SECTION_BIOMETRIC_CHARACTERESTICS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_206_To_Test_Biometric_Locks_Main_Entrance_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
            self.config.get(self.subsection, 'SECTION_BIOMETRIC_LOCK'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
                                                    self.config.get(self.subsection, 'SECTION_BIOMETRIC_LOCK'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_207_To_Test_Biometric_Locks_School_Other_Parts_Check_box(self):
        """
        Description :
        :return:
        """
        for option in range(13):
            biometricoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
                                                    self.config.get(self.subsection, 'SECTION_BIOMETRIC_OTHERPARTS'))
            if not biometricoption[option].get_attribute("class") == "checkbox ng-binding checked":
                biometricoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                biometricoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_BIOMETRIC'),
                                                    self.config.get(self.subsection, 'SECTION_BIOMETRIC_OTHERPARTS'))
                self.assertEqual(biometricoption[option].get_attribute("class"), "checkbox ng-binding checked")
                biometricoption[option].click()



    @attr(priority="high")
    #@SkipTest
    def test_AST_210_To_Test_Security_Law_Enforcement_Officer_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
            self.config.get(self.subsection, 'SECTION_SECURITY_SWORN'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_SWORN'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_212_To_Test_Security_SRO_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(3):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
            self.config.get(self.subsection, 'SECTION_SECURITY_SRO'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_SRO'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_214_To_Test_Security_Guards_Count_Text_box(self):
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
    def test_AST_217_To_Test_Security_School_District_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
            self.config.get(self.subsection, 'SECTION_SECURITY_SECTION'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_SECTION'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_218_To_Test_Security_Characteristics_Check_box(self):
        """
        Description :
        :return:
        """
        for option in range(6):
            characteristicsoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_CHARACTERISTICS'))
            if not characteristicsoption[option].get_attribute("class") == "checkbox ng-binding checked":
                characteristicsoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                characteristicsoption = self.ast.get_schooldata_checkbox(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_CHARACTERISTICS'))
                self.assertEqual(characteristicsoption[option].get_attribute("class"), "checkbox ng-binding checked")
                characteristicsoption[option].click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_220_To_Test_Security_Additional_Guards_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
            self.config.get(self.subsection, 'SECTION_SECURITY_ADDITIONAL'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SECURITY'),
                                                    self.config.get(self.subsection, 'SECTION_SECURITY_ADDITIONAL'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_222_To_Test_Security_How_Many_Additional_Guards_Text_box(self):
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
    def test_AST_226_To_Test_Roof_Access_Description_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ROOFACCESS'),
            self.config.get(self.subsection, 'SECTION_ROOFACCESS_DESCRIPTION'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ROOFACCESS'),
                                                    self.config.get(self.subsection, 'SECTION_ROOFACCESS_DESCRIPTION'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_227_To_Test_Roof_Access_Who_Can_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ROOFACCESS'),
            self.config.get(self.subsection, 'SECTION_ROOFACCESS_ACCESS'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ROOFACCESS'),
                                                    self.config.get(self.subsection, 'SECTION_ROOFACCESS_ACCESS'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")
    @attr(priority="high")
    #@SkipTest
    def test_AST_228_To_Test_Physical_Key_Area_Secured_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
            self.config.get(self.subsection, 'SECTION_PHYSICALKEY_AREA'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
                                                    self.config.get(self.subsection, 'SECTION_PHYSICALKEY_AREA'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")
    @attr(priority="high")
    #@SkipTest
    def test_AST_229_To_Test_Physical_Key_Management_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
            self.config.get(self.subsection, 'SECTION_PHYSICALKEY_POSITION'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
                                                    self.config.get(self.subsection, 'SECTION_PHYSICALKEY_POSITION'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")
    @attr(priority="high")
    @SkipTest
    def test_AST_231_To_Test_Physical_Key_Point_Of_Contact_Radio_Button(self):
        """
        Description :
        :return:
        """
        for option in range(2):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
            self.config.get(self.subsection, 'SECTION_PHYSICALKEY_PoC'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_PHYSICALKEY'),
                                                    self.config.get(self.subsection, 'SECTION_PHYSICALKEY_PoC'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    @SkipTest
    def test_AST_232_To_Verify_File_Upload_For_All_Sections(self):
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
                    pass
                self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.mainsection, section["main_section"]),
                                                self.config.get(self.subsection, section["sub_section"]),
                                                self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))

    @attr(priority="high")
    @SkipTest
    def test_AST_233_To_Verify_Edit_Caption_For_All_Sections(self):
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
                    pass
                self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.mainsection, section["main_section"]),
                                                              self.config.get(self.subsection, section["sub_section"]),
                                                              self.config.get(self.AssessmentSections, 'MAIN_PHYSICAL_SECURITY'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_234_To_Verify_Add_Comment_For_All_Sections(self):
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
                    pass
                self.ast.schooldata_delete_comment(self.config.get(self.mainsection, section["main_section"]),
                                                 self.config.get(self.subsection, section["sub_section"]))
        if flag == 1:
            self.fail("Test has failed : Check log file")