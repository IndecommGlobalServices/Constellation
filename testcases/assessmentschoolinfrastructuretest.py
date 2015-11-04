__author__ = 'Deepa.Sivadas'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from pages.assessmentpage import AssessmentPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
import ConfigParser


class AssessmentSchoolInfrastructurePageTest(BaseTestCase):

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast = AssessmentPage(self.driver)
        self.AssessmentSections = 'AssessmentSections'
        self.messages = 'Messages'
        self.mainsection = 'SchoolInfrastructureMainSections'
        self.subsection = 'SchoolInfrastructureSubSections'
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open('baseconfig.cfg'))
        self.ast.open_schoolinfrastructure_page()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        for subsection in self.config.options(self.subsection):
            self.ast.delete_attchedimage(self.config.get(self.subsection, subsection))
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
    def test_AST_110_To_Verify_Fileupload_SECTION_LANDANDBUILDING_ACRES(self):
        """
        Description : To test fileupload in SECTION_LANDANDBUILDING_ACRES
        :return:
        """
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(
                                        self.mainsection, 'SECTION_LANDANDBUILDING'),
                                        self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_ACRES')))
        self.ast.schooldata_upload_file(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
                                        self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_ACRES'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(
                                        self.mainsection, 'SECTION_LANDANDBUILDING'),
                                        self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_ACRES'))),
                                        count_of_image_before_upload, self.config.get(
                                        self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
                                        self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_ACRES'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_111_To_Verify_Edit_Caption_SECTION_LANDANDBUILDING_ACRES(self):
        """
        Description : To test edit caption in SECTION_LANDANDBUILDING_ACRES
        :return:
        """
        self.ast.schooldata_edit_caption_image(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
                                               self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_ACRES'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
                                               self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_ACRES'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.mainsection, 'SECTION_LANDANDBUILDING'),
                                                      self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_ACRES'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_112_To_Verfiy_Add_Comment_SECTION_LANDANDBUILDING_ACRES(self):
        """
        Description : To test add comment in SECTION_LANDANDBUILDING_ACRES
        :return:
        """
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_ACRES'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_LANDANDBUILDING_ACRES')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_ACRES'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_113_To_Verfiy_noofbuilding_textbox(self):
        """
        Description : To test no of building textbox in SECTION_LANDANDBUILDING_BUILDING
        :return:
        """
        self.ast.get_schoolinfrastructure_textbox(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING')).clear()
        self.ast.get_schoolinfrastructure_textbox(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textbox_locator(
                self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING')))))
        self.assertEqual(self.ast.get_schoolinfrastructure_textbox(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_114_To_Verify_Fileupload_SECTION_LANDANDBUILDING_BUILDING(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_115_To_Verify_Edit_Caption_SECTION_LANDANDBUILDING_BUILDING(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_116_To_Verfiy_Add_Comment_SECTION_LANDANDBUILDING_BUILDING(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_LANDANDBUILDING_BUILDING')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_BUILDING'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_117_To_Verfiy_BuildingNumber_RadioButton(self):
        for option in range(2):
            noofbuilding = self.ast.get_schoolInfrastucture_radiobutton(
            self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'))
            if not noofbuilding[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                noofbuilding[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                noofbuilding = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'))
                self.assertEqual(noofbuilding[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")



    @attr(priority="high")
    #@SkipTest
    def test_AST_118_To_Verify_Fileupload_SECTION_LANDANDBUILDING_MARKED(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.ast.get_school_schoolinfrastructure_noofbuilding_textbox.clear()
        self.ast.get_school_schoolinfrastructure_noofbuilding_textbox.send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast._ast_schoolInfrastructure_no_of_building_text_box_locator)))
        self.assertEqual(self.ast.get_school_schoolinfrastructure_noofbuilding_textbox.get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_119_To_Verify_Edit_Caption_SECTION_LANDANDBUILDING_MARKED(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_120_To_Verfiy_Add_Comment_SECTION_LANDANDBUILDING_MARKED(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_LANDANDBUILDING_MARKED')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_LANDANDBUILDING_MARKED'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_121_To_Verfiy_perimeter_textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER')).get_attribute("value"), "100")



    @attr(priority="high")
    #@SkipTest
    def test_AST_122_To_Verify_Fileupload_SECTION_SURROUNDING_PERIMETER(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_123_To_Verify_Edit_Caption_SECTION_SURROUNDING_PERIMETER(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_124_To_Verfiy_Add_Comment_SECTION_SURROUNDING_PERIMETER(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_SURROUNDING_PERIMETER')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_125_To_Verfiy_Parking_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_126_To_Verify_Fileupload_SECTION_SURROUNDING_PARKING(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_127_To_Verify_Edit_Caption_SECTION_SURROUNDING_PARKING(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_128_To_Verfiy_Add_Comment_SECTION_SURROUNDING_PARKING(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_SURROUNDING_PARKING')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_SURROUNDING_PARKING'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_129_To_Verfiy_AdjusantBuilding_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_130_To_Verify_Fileupload_SECTION_SURROUNDING_ADJACENTBUILDINGS(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_131_To_Verify_Edit_Caption_SECTION_SURROUNDING_ADJACENTBUILDINGS(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_132_To_Verfiy_Add_Comment_SECTION_SURROUNDING_ADJACENTBUILDINGS(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_SURROUNDING_ADJACENTBUILDINGS')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_SURROUNDING_ADJACENTBUILDINGS'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_133_To_Verfiy_ElectricUtility_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY')).get_attribute("value"), "100")

    @attr(priority="high")
    #@SkipTest
    def test_AST_134_To_Verify_Fileupload_SECTION_ELECTRIC_UTILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_135_To_Verify_Edit_Caption_SECTION_ELECTRIC_UTILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_136_To_Verfiy_Add_Comment_SECTION_ELECTRIC_UTILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_ELECTRIC_UTILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_ELECTRIC_UTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_137_To_Verify_Electric_Loss_Of_Utility_RadioButton(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_138_To_Verify_Fileupload_SECTION_ELECTRIC_LOSSOFUTILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_139_To_Verify_Edit_Caption_SECTION_ELECTRIC_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_140_To_Verfiy_Add_Comment_SECTION_ELECTRIC_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_ELECTRIC_LOSSOFUTILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_ELECTRIC_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_141_To_Verify_Electric_BackUp_Generator_RadioButton(self):
        for option in range(2):
            backupgenerator = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'))
            if not backupgenerator[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                backupgenerator[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                backupgenerator = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'))
                self.assertEqual(backupgenerator[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_142_To_Verify_Fileupload_SECTION_ELECTRIC_BACKUPGENERATOR(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_142_To_Verify_Edit_Caption_SECTION_ELECTRIC_BACKUPGENERATOR(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_143_To_Verfiy_Add_Comment_SECTION_ELECTRIC_BACKUPGENERATOR(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_ELECTRIC_BACKUPGENERATOR')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_ELECTRIC_BACKUPGENERATOR'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_144_To_Verify_Electric_Generator_Powered_RadioButton(self):
        for option in range(4):
            backupgenerator = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'))
            if not backupgenerator[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                backupgenerator[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                backupgenerator = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'))
                self.assertEqual(backupgenerator[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_145_To_Verify_Fileupload_SECTION_ELECTRIC_GENERATORPOWERED(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_146_To_Verify_Edit_Caption_SECTION_ELECTRIC_GENERATORPOWERED(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_147_To_Verfiy_Add_Comment_SECTION_ELECTRIC_GENERATORPOWERED(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_ELECTRIC_GENERATORPOWERED')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_ELECTRIC_GENERATORPOWERED'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_148_To_Verfiy_ISPProvider_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(
            self.subsection, 'SECTION_TELEPHONE_PROVIDER')).get_attribute("value"), "100")



    @attr(priority="high")
    #@SkipTest
    def test_AST_149_To_Verify_Fileupload_SECTION_TELEPHONE_PROVIDER(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_150_To_Verify_Edit_Caption_SECTION_TELEPHONE_PROVIDER(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_151_To_Verfiy_Add_Comment_SECTION_TELEPHONE_PROVIDER(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_TELEPHONE_PROVIDER')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_TELEPHONE_PROVIDER'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_152_To_Verify_911_RadioButton(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_153_To_Verify_Fileupload_SECTION_TELEPHONE_911PROCEDURE(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_154_To_Verify_Edit_Caption_SECTION_TELEPHONE_911PROCEDURE(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_155_To_Verfiy_Add_Comment_SECTION_TELEPHONE_911PROCEDURE(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_TELEPHONE_911PROCEDURE')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_TELEPHONE_911PROCEDURE'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_156_To_Verify_Buses_DistrictTransportation_RadioButton(self):
        for option in range(3):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")



    @attr(priority="high")
    #@SkipTest
    def test_AST_157_To_Verify_Fileupload_SECTION_BUSES_DISTRICTTRANSPORTATION(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_158_To_Verify_Edit_Caption_SECTION_BUSES_DISTRICTTRANSPORTATION(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_159_To_Verfiy_Add_Comment_SECTION_BUSES_DISTRICTTRANSPORTATION(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_BUSES_DISTRICTTRANSPORTATION')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_BUSES_DISTRICTTRANSPORTATION'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_160_To_Verify_Buses_GPS_RadioButton(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_GPS'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_GPS'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_161_To_Verify_Fileupload_SECTION_BUSES_GPS(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_GPS')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_BUSES_GPS'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_GPS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_GPS'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_162_To_Verify_Edit_Caption_SECTION_BUSES_GPS(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_BUSES_GPS'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_BUSES_GPS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_GPS'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_163_To_Verfiy_Add_Comment_SECTION_BUSES_GPS(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_BUSES_GPS'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_BUSES_GPS')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_BUSES_GPS'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_164_To_Verify_Buses_GPS_RadioButton(self):
        for option in range(2):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_165_To_Verify_Fileupload_SECTION_BUSES_CAMERA(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_CAMERA')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_166_To_Verify_Edit_Caption_SECTION_BUSES_CAMERA(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_167_To_Verfiy_Add_Comment_SECTION_BUSES_CAMERA(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_BUSES_CAMERA')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_BUSES_CAMERA'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    # @attr(priority="high")
    # #@SkipTest
    # def test_AST_168_To_Verify_typeofcamers_Checkbox(self):
    #     for option in range(3):
    #         typeofcamera = self.ast.get_schoolinfrastructure_checkbox('SECTION_BUSES_TYPEOFCAMERA')
    #         print typeofcamera[option].get_attribute("value")
    #         if not typeofcamera[option].get_attribute("class") == "checkbox ng-binding checked":
    #             typeofcamera[option].click()
    #             WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
    #                 (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
    #             self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOLDATA'))
    #             typeofcamera = self.ast.get_schoolinfrastructure_checkbox('SECTION_BUSES_TYPEOFCAMERA')
    #             self.assertEqual(typeofcamera[option].get_attribute("class"), "checkbox ng-binding checked")
    #             typeofcamera[option].click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_169_To_Verify_Fileupload_SECTION_BUSES_TYPEOFCAMERA(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_TYPEOFCAMERA')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_BUSES_TYPEOFCAMERA'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_TYPEOFCAMERA'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_TYPEOFCAMERA'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_170_To_Verify_Edit_Caption_SECTION_BUSES_TYPEOFCAMERA(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_BUSES_TYPEOFCAMERA'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_BUSES_TYPEOFCAMERA'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_TYPEOFCAMERA'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_171_To_Verfiy_Add_Comment_SECTION_BUSES_TYPEOFCAMERA(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_BUSES_TYPEOFCAMERA'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_BUSES_TYPEOFCAMERA')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_BUSES_TYPEOFCAMERA'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_172_To_Verify_Buses_TwowayRadios_RadioButton(self):
        for option in range(3):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_173_To_Verify_Fileupload_SECTION_BUSES_TWOWAYRADIOS(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_174_To_Verify_Edit_Caption_SECTION_BUSES_TWOWAYRADIOS(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_175_To_Verfiy_Add_Comment_SECTION_BUSES_TWOWAYRADIOS(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_BUSES_TWOWAYRADIOS'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_BUSES_TWOWAYRADIOS')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_SURROUNDING_PERIMETER'),
                                         self.config.get(self.AssessmentSections, 'SECTION_BUSES_TWOWAYRADIOS'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_176_To_Verify_Buses_DispatchSystem_RadioButton(self):
        for option in range(3):
            lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'))
            if not lossofutilityoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                lossofutilityoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                lossofutilityoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'))
                self.assertEqual(lossofutilityoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")


    @attr(priority="high")
    #@SkipTest
    def test_AST_177_To_Verify_Fileupload_SECTION_BUSES_DISPATCHSYSTEM(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_178_To_Verify_Edit_Caption_SECTION_BUSES_DISPATCHSYSTEM(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_179_To_Verfiy_Add_Comment_SECTION_BUSES_DISPATCHSYSTEM(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_BUSES_DISPATCHSYSTEM')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_BUSES_DISPATCHSYSTEM'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_180_To_Verify_Surrounding_Toxic_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_181_To_Verify_Fileupload_SECTION_SURROUNDING_TOXIC(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_182_To_Verify_Edit_Caption_SECTION_SURROUNDING_TOXIC(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_183_To_Verfiy_Add_Comment_SECTION_SURROUNDING_TOXIC(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_SURROUNDING_TOXIC')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_SURROUNDING_TOXIC'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_184_To_Verify_Buses_Housed_Overnight_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_185_To_Verify_Fileupload_SECTION_BUSES_HOUSED(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_HOUSED')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_186_To_Verify_Edit_Caption_SECTION_BUSES_HOUSED(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_187_To_Verfiy_Add_Comment_SECTION_BUSES_HOUSED(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_BUSES_HOUSED')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_BUSES_HOUSED'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_188_To_Verify_Buses_Parked_Onsite_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_189_To_Verify_Fileupload_SECTION_BUSES_ACCESS(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_ACCESS')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_190_To_Verify_Edit_Caption_SECTION_BUSES_ACCESS(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_191_To_Verfiy_Add_Comment_SECTION_BUSES_ACCESS(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_BUSES_ACCESS')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_BUSES_ACCESS'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_192_To_Verfiy_Water_Utility_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_WATER_UTILITY')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_WATER_UTILITY')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_WATER_UTILITY')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(
            self.subsection, 'SECTION_WATER_UTILITY')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_193_To_Verify_Fileupload_SECTION_WATER_UTILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_WATER_UTILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_WATER_UTILITY'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_WATER_UTILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_WATER_UTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_194_To_Verify_Edit_Caption_SECTION_WATER_UTILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTISECTION_WATER_UTILITYON_TELEPHONE_PROVIDER'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_WATER_UTILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_WATER_UTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_195_To_Verfiy_Add_Comment_SECTION_WATER_UTILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_WATER_UTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_WATER_UTILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_WATER_UTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_196_To_Verify_Water_Loss_Utility_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_197_To_Verify_Fileupload_SECTION_WATER_LOSSOFUTILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_198_To_Verify_Edit_Caption_SECTION_WATER_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_199_To_Verfiy_Add_Comment_SECTION_WATER_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_WATER_LOSSOFUTILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_WATER_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_200_To_Verfiy_ISP_Name_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_ISP_NAME')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_ISP_NAME')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_ISP_NAME')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(
            self.subsection, 'SECTION_ISP_NAME')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_201_To_Verify_Fileupload_SECTION_SECTION_ISP_NAME(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ISP_NAME')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_ISP_NAME'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ISP_NAME'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ISP_NAME'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_202_To_Verify_Edit_Caption_SECTION_ISP_NAME(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_ISP_NAME'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_ISP_NAME'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ISP_NAME'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_203_To_Verfiy_Add_Comment_SECTION_ISP_NAME(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_ISP_NAME'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_ISP_NAME')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_ISP_NAME'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_204_To_Verify_ISP_Loss_Utility_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_205_To_Verify_Fileupload_SECTION_ISP_LOSSOFUTILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_206_To_Verify_Edit_Caption_SECTION_ISP_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_207_To_Verfiy_Add_Comment_SECTION_ISP_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_ISP_LOSSOFUTILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_ISP_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_208_To_Verify_Gas_Availablity_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_209_To_Verify_Fileupload_SECTION_NATURALGAS_AVAILABILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_210_To_Verify_Edit_Caption_SECTION_NATURALGAS_AVAILABILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_211_To_Verfiy_Add_Comment_SECTION_NATURALGAS_AVAILABILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_NATURALGAS_AVAILABILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_NATURALGAS_AVAILABILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_212_To_Verfiy_Gas_Utility_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(
            self.subsection, 'SECTION_NATURALGAS_UTILITY')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_213_To_Verify_Fileupload_SECTION_NATURALGAS_UTILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_214_To_Verify_Edit_Caption_SECTION_NATURALGAS_UTILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_215_To_Verfiy_Add_Comment_SECTION_NATURALGAS_UTILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_NATURALGAS_UTILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_NATURALGAS_UTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_216_To_Verfiy_Gas_Service_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(
            self.subsection, 'SECTION_NATURALGAS_REQUIRES')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_217_To_Verify_Fileupload_SECTION_NATURALGAS_REQUIRES(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_218_To_Verify_Edit_Caption_SECTION_NATURALGAS_REQUIRES(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_219_To_Verfiy_Add_Comment_SECTION_NATURALGAS_REQUIRES(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_NATURALGAS_REQUIRES')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_NATURALGAS_REQUIRES'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_220_To_Verify_Gas_Loss_Utility_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_221_To_Verify_Fileupload_SECTION_NATURALGAS_LOSSOFUTILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_222_To_Verify_Edit_Caption_SECTION_NATURALGAS_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_223_To_Verfiy_Add_Comment_SECTION_NATURALGAS_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_NATURALGAS_LOSSOFUTILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_224_To_Verify_Communication_Radio_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_225_To_Verify_Fileupload_SECTION_COMMUNICATION_RADIO(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_226_To_Verify_Edit_Caption_SECTION_COMMUNICATION_RADIO(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_227_To_Verfiy_Add_Comment_SECTION_COMMUNICATION_RADIO(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_COMMUNICATION_RADIO')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_COMMUNICATION_RADIO'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
    @attr(priority = 'high')
    #@SkipTest
    def test_AST_228_To_Verify_Communication_Alert_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_229_To_Verify_Fileupload_SECTION_COMMUNICATION_ALERT(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_230_To_Verify_Edit_Caption_SECTION_COMMUNICATION_ALERT(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_231_To_Verfiy_Add_Comment_SECTION_COMMUNICATION_ALERT(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_COMMUNICATION_ALERT')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ALERT'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
    @attr(priority = 'high')
    #@SkipTest
    def test_AST_232_To_Verify_Communication_ENS_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_233_To_Verify_Fileupload_SECTION_COMMUNICATION_ENS(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_234_To_Verify_Edit_Caption_SECTION_COMMUNICATION_ENS(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_235_To_Verfiy_Add_Comment_SECTION_COMMUNICATION_ENS(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_COMMUNICATION_ENS')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_COMMUNICATION_ENS'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_236_To_Verify_Communication_PS_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_237_To_Verify_Fileupload_SECTION_COMMUNICATION_PA(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_NATURALGAS_LOSSOFUTILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_238_To_Verify_Edit_Caption_SECTION_COMMUNICATION_PA(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_239_To_Verfiy_Add_Comment_SECTION_COMMUNICATION_PA(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_COMMUNICATION_PA')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_COMMUNICATION_PA'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_240_To_Verify_LPGas_Availability_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_241_To_Verify_Fileupload_SECTION_LP_AVAILABILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_242_To_Verify_Edit_Caption_SECTION_LP_AVAILABILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_243_To_Verfiy_Add_Comment_SECTION_LP_AVAILABILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_LP_AVAILABILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_LP_AVAILABILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_244_To_Verfiy_LP_Provider_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_LP_COMPANY')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_LP_COMPANY')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_LP_COMPANY')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(
            self.subsection, 'SECTION_LP_COMPANY')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_245_To_Verify_Fileupload_SECTION_LP_COMPANY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_COMPANY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_LP_COMPANY'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_COMPANY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_COMPANY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_246_To_Verify_Edit_Caption_SSECTION_LP_COMPANY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_LP_COMPANY'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_LP_COMPANY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_COMPANY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_247_To_Verfiy_Add_Comment_SECTION_LP_COMPANY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_LP_COMPANY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_LP_COMPANY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_LP_COMPANY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_248_To_Verfiy_LP_TankSize_Text_Box(self):
        self.ast.get_schoolinfrastructure_textbox(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE')).clear()
        self.ast.get_schoolinfrastructure_textbox(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textbox_locator(
                self.config.get(self.subsection, 'SECTION_LP_TANKSIZE')))))
        self.assertEqual(self.ast.get_schoolinfrastructure_textbox(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_249_To_Verify_Fileupload_SECTION_LP_TANKSIZE(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_250_To_Verify_Edit_Caption_SECTION_LP_TANKSIZE(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_251_To_Verfiy_Add_Comment_SECTION_LP_TANKSIZE(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_LP_TANKSIZE')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_LP_TANKSIZE'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_252_To_Verify_LPGas_Location_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_253_To_Verify_Fileupload_SECTION_LP_TANKLOCATION(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_254_To_Verify_Edit_Caption_SECTION_LP_TANKLOCATION(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_255_To_Verfiy_Add_Comment_SECTION_LP_TANKLOCATION(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_LP_TANKLOCATION')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_LP_TANKLOCATION'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority = 'high')
    #@SkipTest
    def test_AST_256_To_Verfiy_LP_Service_Textarea(self):
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_LP_SERVICES')).clear()
        self.ast.get_schoolinfrasturcture_textarea(self.config.get(self.subsection, 'SECTION_LP_SERVICES')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textarea_locator(
                self.config.get(self.subsection, 'SECTION_LP_SERVICES')))))
        self.assertEqual(self.ast.get_schoolinfrasturcture_textarea(self.config.get(
            self.subsection, 'SECTION_LP_SERVICES')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_257_To_Verify_Fileupload_SECTION_LP_SERVICES(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_SERVICES')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_LP_SERVICES'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_SERVICES'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_SERVICES'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_258_To_Verify_Edit_Caption_SECTION_LP_SERVICES(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_LP_SERVICES'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_LP_SERVICES'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_SERVICES'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_259_To_Verfiy_Add_Comment_SECTION_LP_SERVICES(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_LP_SERVICES'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_LP_SERVICES')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_LP_SERVICES'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))


    @attr(priority="high")
    #@SkipTest
    def test_AST_260_To_Verfiy_LP_Duration_Text_Box(self):
        self.ast.get_schoolinfrastructure_textbox(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION')).clear()
        self.ast.get_schoolinfrastructure_textbox(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION')).send_keys("100")
        self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.ast.get_schoolinfrastructure_textbox_locator(
                self.config.get(self.subsection, 'SECTION_LP_POWERDURATION')))))
        self.assertEqual(self.ast.get_schoolinfrastructure_textbox(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION')).get_attribute("value"), "100")


    @attr(priority="high")
    #@SkipTest
    def test_AST_261_To_Verify_Fileupload_SECTION_LP_POWERDURATION(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_262_To_Verify_Edit_Caption_SECTION_LP_POWERDURATION(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_263_To_Verfiy_Add_Comment_SECTION_LP_POWERDURATION(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_LP_POWERDURATION')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_LP_POWERDURATION'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority = 'high')
    #@SkipTest
    def test_AST_264_To_Verify_LPGas_Loss_Utility_RadioButton(self):
        for option in range(2):
            toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'))
            if not toxicoption[option].get_attribute("class") == "answer_choice radio ng-binding ng-isolate-scope checked":
                toxicoption[option].click()
                WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located(
                    (By.XPATH, self.ast._ast_overview_save_button_locator))).click()
                self.ast.save_editeddata(self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
                toxicoption = self.ast.get_schoolInfrastucture_radiobutton(
                self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'))
                self.assertEqual(toxicoption[option].get_attribute("class"), "answer_choice radio ng-binding ng-isolate-scope checked")

    @attr(priority="high")
    #@SkipTest
    def test_AST_265_To_Verify_Fileupload_SECTION_LP_LOSSOFUTILITY(self):
        count_of_image_before_upload = len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY')))
        self.ast.schooldata_upload_file(self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'),
                                        self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertGreater(len(self.ast.get_schooldata_image(self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'))),
                           count_of_image_before_upload, self.config.get(self.messages, 'MESSAGE_FILE_COULD_NOT_BE_UPLOADED'))
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_266_To_Verify_Edit_Caption_SECTION_LP_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_caption_image(self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'),
                                               self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_image_caption(self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'))[0].text, "Hello")
        self.ast.delete_uploaded_files_assessmentpage(self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'),
                                                      self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))

    @attr(priority="high")
    #@SkipTest
    def test_AST_267_To_Verfiy_Add_Comment_SECTION_LP_LOSSOFUTILITY(self):
        self.ast.schooldata_edit_comment(self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
        self.assertEqual(self.ast.get_schooldata_comment_textbox(self.config.get(self.subsection,
                                                            'SECTION_LP_LOSSOFUTILITY')).get_attribute("value"), "Comment")
        self.ast.schooldata_delete_comment(self.config.get(self.subsection, 'SECTION_LP_LOSSOFUTILITY'),
                                         self.config.get(self.AssessmentSections, 'MAIN_SCHOOL_INFRASTRUCTURE'))
