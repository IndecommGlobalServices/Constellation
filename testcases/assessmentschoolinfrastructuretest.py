__author__ = 'Deepa.Sivadas'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pages.assessmentpage import AssessmentPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
import ConfigParser
from nose.plugins.skip import SkipTest
from time import sleep
from datetime import date, timedelta, datetime
import json, os, re


class AssessmentSchoolInfrastructurePageTest(BaseTestCase):

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast = AssessmentPage(self.driver)
        self.mainsection = 'Sections'
        self.messages = 'Messages'
        self.infrastructuredata = 'SchoolInfrastructure'
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open('baseconfig.cfg'))
        self.ast.open_schoolinfrastructure_page()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        for section in self.config.options(self.infrastructuredata):
            self.ast.delete_attchedimage(self.config.get(self.infrastructuredata, section))
        self.ast.get_overview_button.click()
        self.ast.return_to_assessment_main_page()


    @attr(priority="high")
    #@SkipTest
    def test_AST_109_To_Test_LandandBuildings_Acres_Radio_Button(self):
        """
        Description : To test the acres option radio buttons
        :return:
        """
        for option in range(8):
            landacreoption = self.ast.get_school_schoolinfrastructure_land_acre_radiobutton
            if not landacreoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                landacreoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                landchecked = self.ast.get_school_schoolinfrastructure_land_acre_radiobutton
                self.assertEqual(landchecked[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_110_To_Verify_Fileupload_SECTION_LANDANDBUILDING_ACRES(self):
        """
        Description : To test fileupload in SECTION_LANDANDBUILDING_ACRES
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_111_To_Verify_Edit_Caption_SECTION_LANDANDBUILDING_ACRES(self):
        """
        Description : To test edit caption in SECTION_LANDANDBUILDING_ACRES
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_112_To_Verfiy_Add_Comment_SECTION_LANDANDBUILDING_ACRES(self):
        """
        Description : To test add comment in SECTION_LANDANDBUILDING_ACRES
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_LANDANDBUILDING_ACRES')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_ACRES'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_113_To_Verfiy_noofbuilding_textbox__SECTION_LANDANDBUILDING_BUILDING(self):
        """
        Description : To test no of building textbox in SECTION_LANDANDBUILDING_BUILDING
        :return:
        """
        self.ast.get_school_schoolinfrastructure_noofbuilding_textbox.clear()
        self.ast.get_school_schoolinfrastructure_noofbuilding_textbox.send_keys("100")
        self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast._ast_schoolInfrastructure_no_of_building_text_box_locator)))
        self.assertEqual(self.ast.get_school_schoolinfrastructure_noofbuilding_textbox.get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_114_To_Verify_Fileupload_SECTION_LANDANDBUILDING_BUILDING(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_BUILDING')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_BUILDING'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_BUILDING'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_BUILDING'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_115_To_Verify_Edit_Caption_SECTION_LANDANDBUILDING_BUILDING(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_BUILDING'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_BUILDING'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_BUILDING'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_116_To_Verfiy_Add_Comment_SECTION_LANDANDBUILDING_BUILDING(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_BUILDING'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_LANDANDBUILDING_BUILDING')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_BUILDING'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_117_To_Verfiy_BuildingNumber_RadioButton(self):
        for option in range(2):
            noofbuilding = self.ast.get_school_schoolinfrastructure_buildingno_radiobutton
            if not noofbuilding[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                noofbuilding[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                noofbuilding = self.ast.get_school_schoolinfrastructure_buildingno_radiobutton
                self.assertEqual(noofbuilding[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_118_To_Verify_Fileupload_SECTION_LANDANDBUILDING_MARKED(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_MARKED')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_MARKED'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_MARKED'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_MARKED'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.ast.get_school_schoolinfrastructure_noofbuilding_textbox.clear()
        self.ast.get_school_schoolinfrastructure_noofbuilding_textbox.send_keys("100")
        self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast._ast_schoolInfrastructure_no_of_building_text_box_locator)))
        self.assertEqual(self.ast.get_school_schoolinfrastructure_noofbuilding_textbox.get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_119_To_Verify_Edit_Caption_SECTION_LANDANDBUILDING_MARKED(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_MARKED'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_MARKED'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_MARKED'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_120_To_Verfiy_Add_Comment_SECTION_LANDANDBUILDING_MARKED(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_MARKED'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_LANDANDBUILDING_MARKED')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_LANDANDBUILDING_MARKED'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_121_To_Verfiy_perimeter_textbox(self):
        self.ast.get_school_schoolinfrastructure_perimeter_textbox.clear()
        self.ast.get_school_schoolinfrastructure_perimeter_textbox.send_keys("100")
        self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast._ast_schoolInfrastructure_perimeter_text_box_locator)))
        self.assertEqual(self.ast.get_school_schoolinfrastructure_perimeter_textbox.get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_122_To_Verify_Fileupload_SECTION_SURROUNDING_PERIMETER(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PERIMETER')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PERIMETER'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PERIMETER'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PERIMETER'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_123_To_Verify_Edit_Caption_SECTION_SURROUNDING_PERIMETER(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PERIMETER'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PERIMETER'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PERIMETER'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_124_To_Verfiy_Add_Comment_SECTION_SURROUNDING_PERIMETER(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PERIMETER'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_SURROUNDING_PERIMETER')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PERIMETER'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_125_To_Verfiy_Perimeter_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_126_To_Verify_Fileupload_SECTION_SURROUNDING_PARKING(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_127_To_Verify_Edit_Caption_SECTION_SURROUNDING_PARKING(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_128_To_Verfiy_Add_Comment_SECTION_SURROUNDING_PARKING(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_SURROUNDING_PARKING')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PARKING'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_129_To_Verfiy_AdjusantBuilding_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_130_To_Verify_Fileupload_SECTION_SURROUNDING_ADJACENTBUILDINGS(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_131_To_Verify_Edit_Caption_SECTION_SURROUNDING_ADJACENTBUILDINGS(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_132_To_Verfiy_Add_Comment_SECTION_SURROUNDING_ADJACENTBUILDINGS(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_SURROUNDING_ADJACENTBUILDINGS')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_133_To_Verfiy_ElectricUtility_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_134_To_Verify_Fileupload_SECTION_ELECTRIC_UTILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_135_To_Verify_Edit_Caption_SECTION_ELECTRIC_UTILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_136_To_Verfiy_Add_Comment_SECTION_ELECTRIC_UTILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_ELECTRIC_UTILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_UTILITY'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_137_To_Verify_Electric_Loss_Of_Utility_RadioButton(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_LOSSOFUTILITY'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_LOSSOFUTILITY'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_138_To_Verify_Fileupload_SECTION_ELECTRIC_LOSSOFUTILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_LOSSOFUTILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_LOSSOFUTILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_139_To_Verify_Edit_Caption_SECTION_ELECTRIC_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_LOSSOFUTILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_140_To_Verfiy_Add_Comment_SECTION_ELECTRIC_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_ELECTRIC_LOSSOFUTILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_141_To_Verify_Electric_BackUp_Generator_RadioButton(self):
        for option in range(2):
            backupgenerator = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_BACKUPGENERATOR'))
            if not backupgenerator[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                backupgenerator[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                backupgenerator = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_BACKUPGENERATOR'))
                self.assertEqual(backupgenerator[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_142_To_Verify_Fileupload_SECTION_ELECTRIC_BACKUPGENERATOR(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_BACKUPGENERATOR')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_BACKUPGENERATOR'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_142_To_Verify_Edit_Caption_SECTION_ELECTRIC_BACKUPGENERATOR(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_BACKUPGENERATOR'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_143_To_Verfiy_Add_Comment_SECTION_ELECTRIC_BACKUPGENERATOR(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_ELECTRIC_BACKUPGENERATOR')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_144_To_Verify_Electric_Generator_Powered_RadioButton(self):
        for option in range(4):
            backupgenerator = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_GENERATORPOWERED'))
            if not backupgenerator[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                backupgenerator[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                backupgenerator = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_GENERATORPOWERED'))
                self.assertEqual(backupgenerator[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_145_To_Verify_Fileupload_SECTION_ELECTRIC_GENERATORPOWERED(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_GENERATORPOWERED')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_GENERATORPOWERED'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_146_To_Verify_Edit_Caption_SECTION_ELECTRIC_GENERATORPOWERED(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_GENERATORPOWERED'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_147_To_Verfiy_Add_Comment_SECTION_ELECTRIC_GENERATORPOWERED(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_ELECTRIC_GENERATORPOWERED')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_148_To_Verfiy_ISPProvider_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(
            self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER')).get_attribute("value"), "100")



    @attr(priority="high")
    #@SkipTest
    def test_AST_149_To_Verify_Fileupload_SECTION_TELEPHONE_PROVIDER(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_150_To_Verify_Edit_Caption_SECTION_TELEPHONE_PROVIDER(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_151_To_Verfiy_Add_Comment_SECTION_TELEPHONE_PROVIDER(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_TELEPHONE_PROVIDER')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_PROVIDER'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_152_To_Verify_911_RadioButton(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_911PROCEDURE'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_911PROCEDURE'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_153_To_Verify_Fileupload_SECTION_TELEPHONE_911PROCEDURE(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_911PROCEDURE')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_911PROCEDURE'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_911PROCEDURE'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_911PROCEDURE'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_154_To_Verify_Edit_Caption_SECTION_TELEPHONE_911PROCEDURE(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_911PROCEDURE'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_911PROCEDURE'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_911PROCEDURE'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_155_To_Verfiy_Add_Comment_SECTION_TELEPHONE_911PROCEDURE(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_911PROCEDURE'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_TELEPHONE_911PROCEDURE')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_TELEPHONE_911PROCEDURE'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_156_To_Verify_Buses_DistrictTransportation_RadioButton(self):
        for option in range(3):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISTRICTTRANSPORTATION'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISTRICTTRANSPORTATION'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")



    @attr(priority="high")
    #@SkipTest
    def test_AST_157_To_Verify_Fileupload_SECTION_BUSES_DISTRICTTRANSPORTATION(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISTRICTTRANSPORTATION')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISTRICTTRANSPORTATION'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_158_To_Verify_Edit_Caption_SECTION_BUSES_DISTRICTTRANSPORTATION(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISTRICTTRANSPORTATION'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_159_To_Verfiy_Add_Comment_SECTION_BUSES_DISTRICTTRANSPORTATION(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_BUSES_DISTRICTTRANSPORTATION')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_160_To_Verify_Buses_GPS_RadioButton(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_BUSES_GPS'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_BUSES_GPS'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_161_To_Verify_Fileupload_SECTION_BUSES_GPS(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_GPS')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_BUSES_GPS'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_GPS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_GPS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_162_To_Verify_Edit_Caption_SECTION_BUSES_GPS(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_GPS'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_BUSES_GPS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_GPS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_163_To_Verfiy_Add_Comment_SECTION_BUSES_GPS(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_BUSES_GPS'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_BUSES_GPS')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_BUSES_GPS'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_164_To_Verify_Buses_GPS_RadioButton(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_BUSES_CAMERA'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_BUSES_CAMERA'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_165_To_Verify_Fileupload_SECTION_BUSES_CAMERA(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_CAMERA')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_BUSES_CAMERA'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_CAMERA'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_CAMERA'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_166_To_Verify_Edit_Caption_SECTION_BUSES_CAMERA(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_CAMERA'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_BUSES_CAMERA'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_CAMERA'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_167_To_Verfiy_Add_Comment_SECTION_BUSES_CAMERA(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_BUSES_CAMERA'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_BUSES_CAMERA')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_BUSES_CAMERA'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_169_To_Verify_Fileupload_SECTION_BUSES_TYPEOFCAMERA(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TYPEOFCAMERA')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TYPEOFCAMERA'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TYPEOFCAMERA'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TYPEOFCAMERA'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_170_To_Verify_Edit_Caption_SECTION_BUSES_TYPEOFCAMERA(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TYPEOFCAMERA'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TYPEOFCAMERA'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TYPEOFCAMERA'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_171_To_Verfiy_Add_Comment_SECTION_BUSES_TYPEOFCAMERA(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TYPEOFCAMERA'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_BUSES_TYPEOFCAMERA')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TYPEOFCAMERA'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_172_To_Verify_Buses_TwowayRadios_RadioButton(self):
        for option in range(3):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_BUSES_TWOWAYRADIOS'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_BUSES_TWOWAYRADIOS'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_173_To_Verify_Fileupload_SECTION_BUSES_TWOWAYRADIOS(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TWOWAYRADIOS')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TWOWAYRADIOS'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TWOWAYRADIOS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TWOWAYRADIOS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_174_To_Verify_Edit_Caption_SECTION_BUSES_TWOWAYRADIOS(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TWOWAYRADIOS'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TWOWAYRADIOS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TWOWAYRADIOS'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_175_To_Verfiy_Add_Comment_SECTION_BUSES_TWOWAYRADIOS(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_BUSES_TWOWAYRADIOS'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_BUSES_TWOWAYRADIOS')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_SURROUNDING_PERIMETER'),
                                         self.config.get(self.mainsection, 'SECTION_BUSES_TWOWAYRADIOS'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_176_To_Verify_Buses_DispatchSystem_RadioButton(self):
        for option in range(3):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISPATCHSYSTEM'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISPATCHSYSTEM'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_177_To_Verify_Fileupload_SECTION_BUSES_DISPATCHSYSTEM(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISPATCHSYSTEM')))
        self.ast.schooldata_upload_file(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                        self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISPATCHSYSTEM'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_178_To_Verify_Edit_Caption_SECTION_BUSES_DISPATCHSYSTEM(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                               self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISPATCHSYSTEM'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                                      self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_179_To_Verfiy_Add_Comment_SECTION_BUSES_DISPATCHSYSTEM(self):
        self.ast.schooldata_edit_comment(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.infrastructuredata,
                                                            'SECTION_BUSES_DISPATCHSYSTEM')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.infrastructuredata, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                         self.config.get(self.mainsection, 'MAIN_SCHOOL_INFRASTRUCTURE'))
