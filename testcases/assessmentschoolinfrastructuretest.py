__author__ = 'Deepa.Sivadas'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.assessmentpage import AssessmentPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
import ConfigParser
import os,json

cwd = os.getcwd()
os.chdir('..')
sectionfile = os.path.join(os.getcwd(), "data", "json_assessment_infrastructure_sections.json")
os.chdir(cwd)

class AssessmentSchoolInfrastructurePageTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(AssessmentSchoolInfrastructurePageTest, cls).setUpClass()
        cls.AssessmentSections = 'AssessmentSections'
        cls.messages = 'Messages'
        cls.mainsection = 'SchoolInfrastructureMainSections'
        cls.subsection = 'SchoolInfrastructureSubSections'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))
        cls.ast = AssessmentPage(cls.driver)
        cls.ast.get_asset_avilability(cls.config.get(cls.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast.open_main_section(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        for subsection in self.config.options(self.subsection):
            self.ast.delete_attchedimage(self.config.get(self.subsection, subsection))
        self.ast.get_overview_button.click()
        self.ast.return_to_assessment_main_page()

    @attr(priority="high")
    #@SkipTest
    def test_AST_106_To_Test_Land_And_Buildings_Acres_Radio_Button(self):
        """
        Description : To test the acres option radio buttons
        :return:
        """
        for option in range(8):
            landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
            self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_ACRES'))
            if not landoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                landoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
                self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_ACRES'))
                self.assertEqual(landoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_108_To_Verify_No_Of_Building_Textbox(self):
        """
        Description : To test no of building textbox in SECTION_LANDANDBUILDING_BUILDING
        :return:
        """
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
                                                  self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING')).clear()
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
                                                  self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_locator(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
                self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING')))))
        self.assertEqual(self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
                    self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_110_To_Verify_Building_Number_Radio_Button(self):
        for option in range(2):
            noofbuilding = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
            self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'))
            if not noofbuilding[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                noofbuilding[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                noofbuilding = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
                                                        self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'))
                self.assertEqual(noofbuilding[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_112_To_Verify_Perimeter_Text_Area(self):
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                                                   self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                                                   self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                        self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER')).get_attribute("value"), "100")

    @attr(priority='high')
    #@SkipTest
    def test_AST_114_To_Verify_Parking_Text_Area(self):
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                                                   self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                                                   self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                        self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING')).get_attribute("value"), "100")

    @attr(priority='high')
    #@SkipTest
    def test_AST_115_To_Verify_Adjacent_Building_Text_Area(self):
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                                                   self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                                                   self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')).get_attribute("value"), "100")


    @attr(priority='high')
    #@SkipTest
    def test_AST_117_To_Verify_Surrounding_Toxic_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_SURROUNDING'),
                self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority='high')
    #@SkipTest
    def test_AST_118_To_Verify_Electric_Utility_Text_Area(self):
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                                                   self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                                                   self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                            self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY')).get_attribute("value"), "100")

    @attr(priority='high')
    # @SkipTest
    def test_AST_119_To_Verify_Electric_Loss_Of_Utility_Radio_Button(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_120_To_Verify_Electric_BackUp_Generator_RadioButton(self):
        for option in range(2):
            backupgenerator = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'))
            if not backupgenerator[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                backupgenerator[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                backupgenerator = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'))
                self.assertEqual(backupgenerator[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_121_To_Verify_Electric_Generator_Powered_RadioButton(self):
        for option in range(4):
            backupgenerator = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'))
            if not backupgenerator[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                backupgenerator[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                backupgenerator = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ELECTRIC'),
                self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'))
                self.assertEqual(backupgenerator[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_122_To_Verify_Telephone_Text_Area(self):
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_TELEPHONE'),
                                        self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_TELEPHONE'),
                                                   self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(self.config.get(self.mainsection, 'SECTION_TELEPHONE'),
                self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_TELEPHONE'),
                        self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER')).get_attribute("value"), "100")

    @attr(priority='high')
    #@SkipTest
    def test_AST_123_To_Verify_911_RadioButton(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_TELEPHONE'),
                self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_TELEPHONE'),
                self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_124_To_Verify_Buses_District_Transportation_RadioButton(self):
        for option in range(3):
            lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_125_To_Verify_Buses_GPS_RadioButton(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_GPS'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_GPS'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_126_To_Verify_Buses_Camera_RadioButton(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    # @attr(priority="high")
    # #@SkipTest
    # def test_AST_168_To_Verify_typeofcamers_Checkbox(self):
    #     for option in range(3):
    #         typeofcamera = self.ast.get_schooldata_checkbox('SECTION_BUSES_TYPEOFCAMERA')
    #         print typeofcamera[option].get_attribute("value")
    #         if not typeofcamera[option].get_attribute("class") == "checkbox ng-binding checked":
    #             typeofcamera[option].click()
    #             WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
    #                 (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
    #             self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
    #             typeofcamera = self.ast.get_schooldata_checkbox('SECTION_BUSES_TYPEOFCAMERA')
    #             self.assertEqual(typeofcamera[option].get_attribute("class"), "checkbox ng-binding checked")
    #             typeofcamera[option].click()

    @attr(priority='high')
    #@SkipTest
    def test_AST_129_To_Verify_Buses_Two_Way_Radios_RadioButton(self):
        for option in range(3):
            lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_130_To_Verify_Buses_Dispatch_System_RadioButton(self):
        for option in range(3):
            lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority='high')
    #@SkipTest
    def test_AST_131_To_Verify_Buses_Housed_Overnight_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_132_To_Verify_Buses_Parked_On_Site_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_BUSES'),
                self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_134_To_Verify_Water_Utility_Text_Area(self):
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_WATER'),
                                                   self.config.get(self.subsection, 'SECTION_WATER_UTILITY')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_WATER'),
                                                   self.config.get(self.subsection, 'SECTION_WATER_UTILITY')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(self.config.get(self.mainsection, 'SECTION_WATER'),
                self.config.get(self.subsection, 'SECTION_WATER_UTILITY')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_WATER'),
                                self.config.get(self.subsection, 'SECTION_WATER_UTILITY')).get_attribute("value"), "100")


    @attr(priority='high')
    #@SkipTest
    def test_AST_135_To_Verify_Water_Loss_Utility_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_WATER'),
                self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_WATER'),
                self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_136_To_Verify_ISP_Name_Text_Area(self):
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_ISP'),
                                                   self.config.get(self.subsection, 'SECTION_ISP_NAME')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_ISP'),
                                                   self.config.get(self.subsection, 'SECTION_ISP_NAME')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(self.config.get(self.mainsection, 'SECTION_ISP'),
                self.config.get(self.subsection, 'SECTION_ISP_NAME')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_ISP'),
                                    self.config.get(self.subsection, 'SECTION_ISP_NAME')).get_attribute("value"), "100")

    @attr(priority='high')
    #@SkipTest
    def test_AST_137_To_Verify_ISP_Loss_Utility_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ISP'),
                self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_ISP'),
                self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_138_To_Verify_Gas_Availability_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_140_To_Verify_Gas_Utility_Text_Area(self):
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                                                   self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                                                   self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                        self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY')).get_attribute("value"), "100")


    @attr(priority='high')
    #@SkipTest
    def test_AST_141_To_Verify_Gas_Service_Text_Area(self):
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                                                   self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                                                   self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                            self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES')).get_attribute("value"), "100")

    @attr(priority='high')
    #@SkipTest
    def test_AST_143_To_Verify_Gas_Loss_Utility_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_NATURALGAS'),
                self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_144_To_Verify_Communication_Radio_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_COMMUNICATION'),
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_COMMUNICATION'),
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_145_To_Verify_Communication_Alert_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_COMMUNICATION'),
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_COMMUNICATION'),
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_146_To_Verify_Communication_ENS_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_COMMUNICATION'),
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_COMMUNICATION'),
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_147_To_Verify_Communication_PS_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_COMMUNICATION'),
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_COMMUNICATION'),
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_148_To_Verify_LPGas_Availability_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LP'),
                self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LP'),
                self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_150_To_Verify_LP_Provider_Text_Area(self):
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_LP'),
                                                   self.config.get(self.subsection, 'SECTION_LP_COMPANY')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_LP'),
                                                   self.config.get(self.subsection, 'SECTION_LP_COMPANY')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(self.config.get(self.mainsection, 'SECTION_LP'),
                self.config.get(self.subsection, 'SECTION_LP_COMPANY')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_LP'),
                                self.config.get(self.subsection, 'SECTION_LP_COMPANY')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_151_To_Verify_LP_Tank_Size_Text_Box(self):
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_LP'),
                                                  self.config.get(self.subsection, 'SECTION_LP_TANKSIZE')).clear()
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_LP'),
                                                  self.config.get(self.subsection, 'SECTION_LP_TANKSIZE')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_locator(self.config.get(self.mainsection, 'SECTION_LP'),
                self.config.get(self.subsection, 'SECTION_LP_TANKSIZE')))))
        self.assertEqual(self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_LP'),
                                    self.config.get(self.subsection, 'SECTION_LP_TANKSIZE')).get_attribute("value"), "100")

    @attr(priority='high')
    #@SkipTest
    def test_AST_154_To_Verify_LPGas_Location_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LP'),
                self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LP'),
                self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority='high')
    #@SkipTest
    def test_AST_156_To_Verify_LP_Service_Text_Area(self):
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_LP'),
                                                   self.config.get(self.subsection, 'SECTION_LP_SERVICES')).clear()
        self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_LP'),
                                                   self.config.get(self.subsection, 'SECTION_LP_SERVICES')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(self.config.get(self.mainsection, 'SECTION_LP'),
                self.config.get(self.subsection, 'SECTION_LP_SERVICES')))))
        self.assertEqual(self.ast.get_schooldata_textarea(self.config.get(self.mainsection, 'SECTION_LP'),
                                self.config.get(self.subsection, 'SECTION_LP_SERVICES')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_158_To_Verify_LP_Duration_Text_Box(self):
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_LP'),
                                                  self.config.get(self.subsection, 'SECTION_LP_POWERDURATION')).clear()
        self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_LP'),
                                                  self.config.get(self.subsection, 'SECTION_LP_POWERDURATION')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textbox_locator(self.config.get(self.mainsection, 'SECTION_LP'),
                self.config.get(self.subsection, 'SECTION_LP_POWERDURATION')))))
        self.assertEqual(self.ast.get_schooldata_textbox(self.config.get(self.mainsection, 'SECTION_LP'),
                            self.config.get(self.subsection, 'SECTION_LP_POWERDURATION')).get_attribute("value"), "100")

    @attr(priority='high')
    #@SkipTest
    def test_AST_160_To_Verify_LPGas_Loss_Utility_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LP'),
                self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schooldata_radiobutton(self.config.get(self.mainsection, 'SECTION_LP'),
                self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_161_To_Verify_File_Upload_For_All_Sections(self):
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
                                                self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
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
                                                self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_162_To_Verify_Edit_Caption_For_All_Sections(self):
        """
        Description : To test edit caption
        :return:
        """
        with open(sectionfile) as data_file:
            for section in json.load(data_file):
                self.ast.schooldata_edit_caption_image(self.config.get(self.mainsection, section["main_section"]),
                                                       self.config.get(self.subsection, section["sub_section"]),
                                                       self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                try:
                    self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.mainsection, section["main_section"]),
                                                self.config.get(self.subsection, section["sub_section"]))[0].text, "Hello")
                except Exception, err:
                    print err.message + " under " + self.config.get(self.mainsection, section["main_section"]) \
                          +" - " +self.config.get(self.subsection, section["sub_section"])
                self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.mainsection, section["main_section"]),
                                                              self.config.get(self.subsection, section["sub_section"]),
                                                              self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_163_To_Verify_Add_Comment_For_All_Sections(self):
        """
        Description : To test add comment in
        :return:
        """
        flag = 0
        with open(sectionfile) as data_file:
            for section in json.load(data_file):
                self.ast.schooldata_edit_comment(self.config.get(self.mainsection, section["main_section"]),
                                                 self.config.get(self.subsection, section["sub_section"]),
                                                 self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                try:
                    self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.mainsection, section["main_section"]),
                            self.config.get(self.subsection, section["sub_section"])).get_attribute("value"), "Comment")
                except Exception, err:
                    flag = 1
                    print err.message + " under " + self.config.get(self.mainsection, section["main_section"]) \
                          +" - " +self.config.get(self.subsection, section["sub_section"])
                self.ast.schooldata_delete_comment(self.config.get(self.mainsection, section["main_section"]),
                                                 self.config.get(self.subsection, section["sub_section"]))
        if flag == 1:
            self.fail("Test has failed")