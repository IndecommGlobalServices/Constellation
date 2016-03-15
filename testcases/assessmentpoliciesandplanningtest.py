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
from nose.plugins.skip import SkipTest
import json, os, re

cwd = os.getcwd()
os.chdir('..')
sectionfile = os.path.join(os.getcwd(), "data", "json_assessment_policies_n_planning_sections.json")
os.chdir(cwd)


class AssessmentPoliciesandPlanningPageTest(BaseTestCase):
    checked_var = r"answer_choice radio ng-binding ng-isolate-scope checked"
    unchecked_var = r"answer_choice radio ng-binding ng-isolate-scope"

    @classmethod
    def setUpClass(cls):
        super(AssessmentPoliciesandPlanningPageTest, cls).setUpClass()
        cls.AssessmentSections = 'AssessmentSections'
        cls.messages = 'Messages'
        cls.mainsection = 'PoliciesAndPlanningMainSections'
        cls.subsection = 'PoliciesAndPlanningSubSections'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))
        cls.ast = AssessmentPage(cls.driver)
        try:
            cls.ast.get_asset_avilability(cls.config.get(cls.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
            cls.ast.delete_existing_assessments()
            cls.ast.create_initial_assessment()
        except:
            pass

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast.open_main_section(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        for subsection in self.config.options(self.subsection):
            self.ast.delete_attchedimage(self.config.get(self.subsection, subsection))
        self.ast.get_overview_button.click()
        self.ast.return_to_assessment_main_page()

    @attr(priority="high")
    #@SkipTest
    def test_AST_235_To_Verify_Radio_Buttons_Of_School_Safety_Plan(self):
        """
        Description : To test the school type option radio buttons
        Author : Bijesh
        :return: None
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_SCHOOL_SAFETY')
        config_sub_var = self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_COMPREHENSIVE_PLAN')
        for option in range(4):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_237_To_Test_Check_Box_Of_School_Safety_Plan_Shared(self):
        """
        Description : To test the school safety plan share option check box
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_SCHOOL_SAFETY')
        config_sub_var = self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN_SHARED')
        for option in range(6):
            schoolsafetyplanshare = self.ast.get_schooldata_checkbox(config_main_var, config_sub_var)
            if not schoolsafetyplanshare[option].get_attribute("class") == "checkbox ng-binding checked":
                schoolsafetyplanshare[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                planshare = self.ast.get_schooldata_checkbox(config_main_var, config_sub_var)
                self.assertEqual(planshare[option].get_attribute("class"), "checkbox ng-binding checked")
                planshare[option].click()
            else:
                schoolsafetyplanshare[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                planshare = self.ast.get_schooldata_checkbox(config_main_var, config_sub_var)
                self.assertEqual(planshare[option].get_attribute("class"), "checkbox ng-binding")
                planshare[option].click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_240_To_Verify_Radio_Buttons_Of_School_Safety_Plan_Review(self):
        """
        Description : To test the radio buttons of school Safety Plan Review option
        Author : Bijesh
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_SCHOOL_SAFETY')
        config_sub_var = self.config.get(self.subsection, 'SECTION_SCHOOL_SAFETY_PLAN_REVIEW')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_241_To_Verify_Radio_Buttons_Of_Fire_Safety_Inspector(self):
        """
        Description : To test the radio buttons of Fire Safety Certified Inspector option
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_FIRE_SAFETY')
        config_sub_var = self.config.get(self.subsection, 'SECTION_FIRE_SAFETY_CERTIFIED_INSPECTOR')
        for option in range(2):
            firesafetyoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not firesafetyoptions[option].get_attribute("class") == self.checked_var:
                firesafetyoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                firesafetychecked = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(firesafetychecked[option].get_attribute("class"), self.checked_var)
            else:
                firesafetyoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                firesafetychecked = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(firesafetychecked[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_242_To_Verify_Radio_Buttons_Of_Fire_Safety_Inspection(self):
        """
        Description : To test the radio buttons of Fire Safety Certified Inspection option
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_FIRE_SAFETY')
        config_sub_var = self.config.get(self.subsection, 'SECTION_FIRE_SAFETY_INSPECTION')
        for option in range(3):
            firesafetyoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not firesafetyoptions[option].get_attribute("class") == self.checked_var:
                firesafetyoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                firesafetychecked = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(firesafetychecked[option].get_attribute("class"), self.checked_var)
            else:
                firesafetyoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                firesafetychecked = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(firesafetychecked[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_243_To_Verify_Radio_Buttons_Of_Physical_Key_Access_Review(self):
        """
        Description : To test the radio buttons of Physical Access Review option
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_PHYSICAL_ACCESS')
        config_sub_var = self.config.get(self.subsection, 'SECTION_PHYSICAL_ACCESS_REVIEW')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_245_To_Verify_Radio_Buttons_Of_Physical_Access_Key_Return(self):
        """
        Description : To test the radio buttons of Physical Access Keys Return option
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_PHYSICAL_ACCESS')
        config_sub_var = self.config.get(self.subsection, 'SECTION_PHYSICAL_ACCESS_KEYS_RETURN')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_247_To_Verify_Radio_Buttons_Of_Physical_Access_Annual_Inventory(self):
        """
        Description : To test the radio buttons of Physical Access Annual Inventory option
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_PHYSICAL_ACCESS')
        config_sub_var = self.config.get(self.subsection, 'SECTION_PHYSICAL_ACCESS_ANNUAL_INVENTORY')
        for option in range(3):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_248_To_Verify_Radio_Buttons_Of_Metal_Detector_Screen_Weapons(self):
        """
        Description : To test the radio buttons of Metal Detector Screen Weapons option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_METAL_DETECTOR')
        config_sub_var = self.config.get(self.subsection, 'SECTION_METAL_DETECTOR_SCREEN_WEAPONS')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_249_To_Verify_Radio_Buttons_Of_Metal_Detector_Airport_Style(self):
        """
        Description : To test the radio buttons of Metal Detector Airport Style option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_METAL_DETECTOR')
        config_sub_var = self.config.get(self.subsection, 'SECTION_METAL_DETECTOR_AIRPORT_STYLE')
        for option in range(3):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_251_To_Verify_Radio_Buttons_Of_Metal_Detector_Extra_Screen(self):
        """
        Description : To test the radio buttons of Metal Detector Extra Screen option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_METAL_DETECTOR')
        config_sub_var = self.config.get(self.subsection, 'SECTION_METAL_DETECTOR_EXTRA_SCREEN')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_252_To_Verify_Radio_Buttons_Of_Hand_Held_Radio_Policy(self):
        """
        Description : To test the radio buttons of Hand Held Radio Policy option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_HANDHELD_RADIO')
        config_sub_var = self.config.get(self.subsection, 'SECTION_HANDHELD_RADIO_POLICY')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_254_To_Verify_Radio_Buttons_Of_Hand_Held_Radio_List(self):
        """
        Description : To test the radio buttons of Hand Held Radio List option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_HANDHELD_RADIO')
        config_sub_var = self.config.get(self.subsection, 'SECTION_HANDHELD_RADIO_LIST')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_256_To_Verify_Radio_Buttons_Of_Emergency_Checklist_Potential_Attack(self):
        """
        Description : To test the radio buttons of Emergency Checklist Potential Attack option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_EMERGENCY_CHECKLIST')
        config_sub_var = self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_POTENTIAL_ATTACK')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_258_To_Verify_Radio_Buttons_Of_Emergency_Checklist_Procedures(self):
        """
        Description : To test the radio buttons of Emergency Checklist Procedures option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_EMERGENCY_CHECKLIST')
        config_sub_var = self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_PROCEDURES')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_260_To_Verify_Radio_Buttons_Of_Emergency_Checklist_Shared(self):
        """
        Description : To test the radio buttons of Emergency Checklist Shared option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_EMERGENCY_CHECKLIST')
        config_sub_var = self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_SHARED')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_261_To_Verify_Radio_Buttons_Of_Emergency_Checklist_Reunification_Plan(self):
        """
        Description : To test the radio buttons of Emergency Checklist Reunification Plan option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_EMERGENCY_CHECKLIST')
        config_sub_var = self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_REUNIFICATION_PLAN')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_263_To_Verify_Radio_Buttons_Of_Emergency_Checklist_Reunification_Update(self):
        """
        Description : To test the radio buttons of Emergency Checklist Reunification Update option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_EMERGENCY_CHECKLIST')
        config_sub_var = self.config.get(self.subsection, 'SECTION_EMERGENCY_CHECKLIST_REUNIFICATION_UPDATE')
        for option in range(4):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_264_To_Verify_Radio_Buttons_Of_Safety_hazards_Assessment(self):
        """
        Description : To test the radio buttons of Safety hazards Assessment option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_SAFETY_HAZARDS')
        config_sub_var = self.config.get(self.subsection, 'SECTION_SAFETY_HAZARDS_ASSESSMENT')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_265_To_Verify_Radio_Buttons_Of_Electronics_locks_Access_Reviewed(self):
        """
        Description : To test the radio buttons of Electronics locks Access Reviewed option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_ELECTRONIC_LOCKS')
        config_sub_var = self.config.get(self.subsection, 'SECTION_ELECTRONIC_LOCKS_ACCESS_REVIEWED')
        for option in range(3):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_267_To_Verify_Radio_Buttons_Of_Electronics_locks_Access_Suspended(self):
        """
        Description : To test the radio buttons of Electronics locks Access Suspended option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_ELECTRONIC_LOCKS')
        config_sub_var = self.config.get(self.subsection, 'SECTION_ELECTRONIC_LOCKS_ACCESS_SUSPENDED')
        for option in range(3):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_269_To_Verify_Radio_Buttons_Of_PA_System_Policy(self):
        """
        Description : To test the radio buttons of PA System Policy option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_PA_SYSTEM')
        config_sub_var = self.config.get(self.subsection, 'SECTION_PA_SYSTEM_POLICY')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority='high')
    #@SkipTest
    def test_AST_271_To_Verify_PA_System_Announcements_Text_Area(self):
        """
        Description : To test the radio buttons of PA System Policy option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_PA_SYSTEM')
        config_sub_var = self.config.get(self.subsection, 'SECTION_PA_SYSTEM_ANNOUNCEMENTS')
        self.ast.get_schooldata_textarea(config_main_var,config_sub_var).clear()
        self.ast.get_schooldata_textarea(config_main_var,config_sub_var).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schooldata_textarea_locator(config_main_var,config_sub_var))))
        self.assertEqual(self.ast.get_schooldata_textarea(config_main_var,config_sub_var).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_272_To_Verify_Radio_Buttons_Of_Crisis_Incident_Team_Composition(self):
        """
        Description : To test the radio buttons of Crisis Incident Team Composition option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_CRISIS_INCIDENT_TEAM')
        config_sub_var = self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_TEAM_COMPOSITION')
        for option in range(3):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_273_To_Verify_Radio_Buttons_Of_Crisis_Incident_Team_Trained_IS700(self):
        """
        Description : To test the radio buttons of Crisis Incident Team Trained IS700 option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_CRISIS_INCIDENT_TEAM')
        config_sub_var = self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_TEAM_TRAINED_IS700')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_275_To_Verify_Radio_Buttons_Of_Crisis_Incident_Team_Trained_ICS100(self):
        """
        Description : To test the radio buttons of Crisis Incident Team Trained IS100 option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_CRISIS_INCIDENT_TEAM')
        config_sub_var = self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_TEAM_TRAINED_ICS100')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_277_To_Verify_Radio_Buttons_Of_Crisis_Incident_Team_Trained_ICS200(self):
        """
        Description : To test the radio buttons of Crisis Incident Team Trained IS200 option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_CRISIS_INCIDENT_TEAM')
        config_sub_var = self.config.get(self.subsection, 'SECTION_CRISIS_INCIDENT_TEAM_TRAINED_ICS_200')
        for option in range(2):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_279_To_Test_Check_Box_Of_General_Policies(self):
        """
        Description : To test the school safety plan share option check box
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_GENERAL_POLICIES')
        config_sub_var = self.config.get(self.subsection, 'SECTION_GENERAL_POLICIES_TO_ADDRESS')
        for option in range(6):
            schoolsafetyplanshare = self.ast.get_schooldata_checkbox(config_main_var, config_sub_var)
            if not schoolsafetyplanshare[option].get_attribute("class") == "checkbox ng-binding checked":
                schoolsafetyplanshare[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                planshare = self.ast.get_schooldata_checkbox(config_main_var, config_sub_var)
                self.assertEqual(planshare[option].get_attribute("class"), "checkbox ng-binding checked")
                planshare[option].click()
            else:
                schoolsafetyplanshare[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                planshare = self.ast.get_schooldata_checkbox(config_main_var, config_sub_var)
                self.assertEqual(planshare[option].get_attribute("class"), "checkbox ng-binding")
                planshare[option].click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_281_To_Verify_Radio_Buttons_Of_Emergency_Notification_System(self):
        """
        Description : To test the radio buttons of Emergency Notification System option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_EMERGENCY_NOTIFICATION_SYSTEM')
        config_sub_var = self.config.get(self.subsection, 'SECTION_EMERGENCY_NOTIFICATION_SYSTEM_POLICY')
        for option in range(3):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    #@SkipTest
    def test_AST_283_To_Verify_Radio_Buttons_Of_Alert_Notification_System(self):
        """
        Description : To test the radio buttons of Alert Notification System option
        Revision:
        Author : Bijesh
        :return:
        """
        config_main_var = self.config.get(self.mainsection, 'SECTION_ALERT_NOTIFICATION_SYSTEM')
        config_sub_var = self.config.get(self.subsection, 'SECTION_ALERT_NOTIFICATION_SYSTEM_POLICY')
        for option in range(3):
            radiobuttonoptions = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
            if not radiobuttonoptions[option].get_attribute("class") == self.checked_var:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.checked_var)
            else:
                radiobuttonoptions[option].click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                radiobuttonstatus = self.ast.get_schooldata_radiobutton(config_main_var,config_sub_var)
                self.assertEqual(radiobuttonstatus[option].get_attribute("class"), self.unchecked_var)

    @attr(priority="high")
    @SkipTest
    def test_AST_285_To_Verify_File_Upload_For_All_Sections(self):
        """
        Description : To test file upload in all sections.
        :return:
        """
        with open(sectionfile) as data_file:
            for section in json.load(data_file):
                count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(
                                        self.mainsection, section["main_section"]),
                                        self.config.get(self.subsection, section["sub_section"])))
                self.ast.schooldata_upload_file(self.config.get(self.mainsection, section["main_section"]),
                                                self.config.get(self.subsection, section["sub_section"]),
                                                self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
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
                                                self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))

    @attr(priority="high")
    @SkipTest
    def test_AST_286_To_Verify_Edit_Caption_For_All_Sections(self):
        """
        Description : To test edit caption for all the sections.
        :return:
        """
        with open(sectionfile) as data_file:
            for section in json.load(data_file):
                self.ast.schooldata_edit_caption_image(self.config.get(self.mainsection, section["main_section"]),
                                                       self.config.get(self.subsection, section["sub_section"]),
                                                       self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
                try:
                    self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.mainsection, section["main_section"]),
                                                self.config.get(self.subsection, section["sub_section"]))[0].text, "Hello")
                except Exception, err:
                    print err.message + " under " + self.config.get(self.mainsection, section["main_section"]) \
                          +" - " +self.config.get(self.subsection, section["sub_section"])
                    pass
                self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.mainsection, section["main_section"]),
                                                              self.config.get(self.subsection, section["sub_section"]),
                                                              self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_287_To_Verify_Add_Comment_For_All_Sections(self):
        """
        Description : To test add comment in all the sections.
        :return:
        """
        flag = 0
        with open(sectionfile) as data_file:
            for section in json.load(data_file):
                self.ast.schooldata_edit_comment(self.config.get(self.mainsection, section["main_section"]),
                                                 self.config.get(self.subsection, section["sub_section"]),
                                                 self.config.get(self.AssessmentSections, 'MAIN_POLICIES_PLANNING'))
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