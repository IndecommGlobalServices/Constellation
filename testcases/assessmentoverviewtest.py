import ConfigParser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pages.assessmentpage import AssessmentPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from time import sleep
from datetime import timedelta, datetime
from nose.plugins.skip import SkipTest



class AssessmentOverviewPageTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(AssessmentOverviewPageTest, cls).setUpClass()
        cls.AssessmentSections = 'AssessmentSections'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))
        cls.ast = AssessmentPage(cls.driver)
        cls.ast.logintoapp()
        try:
            cls.ast.get_asset_avilability(cls.config.get(cls.AssessmentSections, 'MAIN_OVERVIEW'))
            cls.ast.delete_existing_assessments()
            cls.ast.create_initial_assessment()
        except:
            pass

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast.open_overview_page()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        # try:
        #     self.ast.delete_uploaded_files()
        # except:
        #     pass
        self.ast.return_to_assessment_main_page()

    @attr(priority="high")
    #@SkipTest
    def test_AST_44_To_Verify_Overview_Add_Notes(self):
        note = "New note"
        sleep(5)
        self.ast.get_overview_notes_textbox.clear()
        self.ast.get_overview_notes_textbox.send_keys(note)
        self.ast.get_overview_save_button.click()
        WebDriverWait(self.driver, 80).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, self.ast._ast_saved_text_locator), "Saved"),"The message appeared is " +
                                            self.basepage.findElementByXpath(self.ast._ast_saved_text_locator).text)
        self.assertEqual(note, self.ast.get_overview_notes_edited_textbox.get_attribute("value"),
                         "Entered text not appearing in notes textarea")


    @attr(priority="high")
    @SkipTest
    def test_AST_45_To_Verify_Overview_Upload_image_file_without_caption(self):
        self.ast.upload_a_file("", "Test_Case_40.jpg")
        self.assertTrue(self.ast.get_caption_path("Test_Case_40").is_displayed(), "Upload failed")
        self.assertTrue(self.driver.find_element_by_xpath(self.ast.get_file_header_path("Test_Case_40")
                                                          ).is_displayed(), "Upload failed")

    @attr(priority="high")
    @SkipTest
    def test_AST_46_To_Verify_Overview_Upload_pdf_file_without_caption(self):
        self.ast.upload_a_file("", "Test_Case_44_1.pdf")
        self.assertTrue(self.ast.get_caption_path("Test_Case_44_1").is_displayed(), "Upload failed")
        self.assertTrue(self.driver.find_element_by_xpath(self.ast.get_file_header_path("Test_Case_44_1")
                                                          ).is_displayed(), "Upload failed")

    @attr(priority="high")
    @SkipTest
    def test_AST_47_1_To_Verify_Overview_Upload_image_file_with_caption(self):
        self.ast.upload_a_file("File_caption", "Test_Case_40.jpg")
        self.assertTrue(self.ast.get_caption_path("File_caption").is_displayed(), "Upload failed")
        self.assertTrue(self.driver.find_element_by_xpath(self.ast.get_file_header_path("File_caption")
                                                          ).is_displayed(), "Upload failed")

    @attr(priority="high")
    @SkipTest
    def test_AST_47_2_To_Verify_Overview_Upload_pdf_file_with_caption(self):
        self.ast.upload_a_file("File_pdf_caption", "Test_Case_44_1.pdf")
        self.assertTrue(self.ast.get_caption_path("File_pdf_caption").is_displayed(), "Upload failed")
        self.assertTrue(self.driver.find_element_by_xpath(self.ast.get_file_header_path("File_pdf_caption")
                                                          ).is_displayed(), "Upload failed")

    @attr(priority="high")
    @SkipTest
    def test_AST_50_To_Verify_Overview_Upload_File_Cancel(self):
        self.ast.upload_a_file_cancel("Test_Case_41", "Test_Case_41.jpg")
        try:
            self.assertTrue(self.driver.find_element_by_xpath(self.ast.get_file_header_path("Test_Case_41")).is_displayed())
        except NoSuchElementException:
            pass

    @attr(priority="high")
    #@SkipTest
    def test_AST_58_To_Verify_Overview_Dates_Change_Day(self):
        start_date = datetime.today().date()
        end_date = start_date + timedelta(days=1)
        sleep(2)
        self.ast.get_overview_startdate_textbox.clear()
        self.ast.get_overview_startdate_textbox.send_keys(str(start_date))
        sleep(1)
        self.ast.get_overview_enddate_textbox.clear()
        self.ast.get_overview_enddate_textbox.send_keys(str(end_date))
        self.ast.get_overview_save_button.click()
        WebDriverWait(self.driver, 100).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, self.ast._ast_saved_text_locator), "Saved"), "The message appeared is" +
                                            self.driver.find_element_by_xpath(self.ast._ast_saved_text_locator).text)
        self.assertEqual(str(start_date), self.ast.get_overview_startdate_textbox.get_attribute("value"))
        self.assertEqual(str(end_date), self.ast.get_overview_enddate_textbox.get_attribute("value"))

    @attr(priority="high")
    #@SkipTest
    def test_AST_59_To_Verify_Overview_Dates_Change_Month(self):
        start_date = datetime.today().date()
        end_date = start_date + timedelta(days=31)
        sleep(1)
        self.ast.get_overview_startdate_textbox.clear()
        self.ast.get_overview_startdate_textbox.send_keys(str(start_date))
        self.ast.get_overview_enddate_textbox.clear()
        self.ast.get_overview_enddate_textbox.send_keys(str(end_date))
        #self.ast.get_overview_enddate_textbox.send_keys(Keys.TAB)
        sleep(10)
        self.ast.get_overview_save_button.click()
        WebDriverWait(self.driver, 100).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, self.ast._ast_saved_text_locator), "Saved"), "The message appeared is" +
                                            self.driver.find_element_by_xpath(self.ast._ast_saved_text_locator).text)

        self.assertEqual(str(start_date), self.ast.get_overview_startdate_textbox.get_attribute("value"))
        self.assertEqual(str(end_date), self.ast.get_overview_enddate_textbox.get_attribute("value"))

    @attr(priority="high")
    #@SkipTest
    def test_AST_60_To_Verify_Overview_Dates_Change_Year(self):
        start_date = datetime.today().date()
        end_date = start_date + timedelta(days=365)
        sleep(1)
        self.ast.get_overview_startdate_textbox.clear()
        self.ast.get_overview_startdate_textbox.send_keys(str(start_date))
        self.ast.get_overview_enddate_textbox.clear()
        self.ast.get_overview_enddate_textbox.send_keys(str(end_date))
        self.ast.get_overview_enddate_textbox.send_keys(Keys.TAB)
        sleep(10)
        self.ast.get_overview_save_button.click()
        WebDriverWait(self.driver, 80).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, self.ast._ast_saved_text_locator), "Saved"), "The message appeared is" +
                                             self.driver.find_element_by_xpath(self.ast._ast_saved_text_locator).text)
        self.assertEqual(str(start_date), self.ast.get_overview_startdate_textbox.get_attribute("value"))
        self.assertEqual(str(end_date), self.ast.get_overview_enddate_textbox.get_attribute("value"))




