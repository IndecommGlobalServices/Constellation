__author__ = 'Deepa.Sivadas'
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pages.assessmentpage import AssessmentPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from time import sleep
from datetime import date, timedelta, datetime
from pages.IconListPage import IconListPage
import json, os, re


class AssessmenttPageTest(BaseTestCase):

    cwd = os.getcwd()
    os.chdir('..')
    searchasset_filepath = os.path.join(os.getcwd(), "data\json_SearchAssessments.json")
    os.chdir(cwd)

    @attr(priority="high")
    @SkipTest
    @attr(status='smoke')
    def test_smoketest_assessment(self):
        assessmentpage = AssessmentPage(self.driver)
        sleep(2)
        try:
            self.assertEqual(assessmentpage.get_ast_app_name.text, "Assessments")
        except:
            print "The Assessment link text not available"

        assessmentpage.get_ast_statusfilter_dropdown.click()

        try:
            self.assertTrue(assessmentpage.get_statusfilter_InProgress_link)
            self.assertTrue(assessmentpage.get_statusfilter_NotStarted_link)
            self.assertTrue(assessmentpage.get_statusfilter_Submitted_link)
        except:
            print " One or more filter option for status not present"

        try:
            self.assertEqual(assessmentpage.get_resetfilter_button.text, "Reset filters")
        except:
            print "Reset filters button not available or text not matching"

        try:
            self.assertTrue(assessmentpage.get_search_assessment_textbox)
        except:
            print "Search textbox not available"

        try:
            self.assertTrue(assessmentpage.get_main_create_assessment_button)
        except:
            print "Create assessment button not present"

    @attr(priority="high")
    #@SkipTest
    def test_AST_01_To_verify_noemailid_createassessment(self):
        ast = AssessmentPage(self.driver)
        sleep(10)
        ast.create_assessment_select_haystax_template()
        ast.select_first_asset()
        ast.get_create_assignedto_textbox.clear()
        ast.get_create_startdate_textbox.send_keys("2015-09-10")
        ast.get_create_enddate_textbox.send_keys("2015-09-11")
        self.assertFalse(ast.get_create_assessments_button.is_enabled(),"Create assessment button enabled even without entering email")
        sleep(2)
        ast.get_main_create_assessment_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_02_To_verify_nodate_createassessment(self):
        ast = AssessmentPage(self.driver)
        ast.create_assessment_select_haystax_template()
        ast.select_first_asset()
        ast.get_create_assignedto_textbox.clear()
        ast.get_create_assignedto_textbox.send_keys("deep@dee")
        ast.get_create_startdate_textbox.send_keys("")
        ast.get_create_enddate_textbox.send_keys("")
        self.assertFalse(ast.get_create_assessments_button.is_enabled(),"Create assessment button enabled even without entering start and end date")
        sleep(2)
        ast.get_main_create_assessment_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_04_To_verify_datevaidation_createassessment(self):
        ast = AssessmentPage(self.driver)
        sleep(8)
        dateformat = ['date', '23-11-2015', '2015-22-11']
        ast.create_assessment_select_haystax_template()
        ast.select_first_asset()
        for date in dateformat:
            ast.get_create_startdate_textbox.clear()
            ast.get_create_startdate_textbox.send_keys(date)
            ast.get_create_startdate_textbox.send_keys(Keys.TAB)
            self.assertNotEqual(ast.get_create_startdate_textbox.text, date, "Start date textbox no date format validation")
        for date in dateformat:
            ast.get_create_enddate_textbox.clear()
            ast.get_create_enddate_textbox.send_keys(date)
            ast.get_create_enddate_textbox.send_keys(Keys.TAB)
            self.assertNotEqual(ast.get_create_enddate_textbox.text, date, "Start date textbox no date format validation")
        sleep(2)
        ast.get_main_create_assessment_button.click()

    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_AST_05_To_create_assessment(self):
        ast = AssessmentPage(self.driver)
        check = 0
        ast.create_assessment(ast.asset_school_name)
        sleep(8)
        ast.search_assessment_textbox(ast.asset_school_name)
        sleep(5)
        for item in ast.get_assessment_table("Asset"):
            if (item.text  == ast.asset_school_name) and (item.value_of_css_property("background-color") == "rgba(255, 236, 158, 1)"):
                check = 1
                break
        ast.get_search_assessment_textbox.clear()
        ast.get_search_assessment_textbox.send_keys(Keys.BACKSPACE)
        self.assertFalse(check == 0, "No assessment is created or is not appearing with yellow background")

    @attr(priority="high")
    #@SkipTest
    def test_AST_06_To_verify_emailid_field_createassessment(self):
        ast = AssessmentPage(self.driver)
        emailid = ['Email', 'Email.', 'email.com', 'email@']
        sleep(10)
        ast.create_assessment_select_haystax_template()
        sleep(2)
        ast.get_create_assignedto_textbox.clear()
        for item in emailid:
            ast.get_create_assignedto_textbox.send_keys(item)
            ast.get_create_assignedto_textbox.send_keys(Keys.TAB)
            sleep(5)
            self.assertEqual("rgba(192, 57, 43, 1)", ast.get_create_assignedto_textbox.value_of_css_property("border-bottom-color"),  "Email ID validation error in create assessment")
            ast.get_create_assignedto_textbox.clear()
        ast.get_main_create_assessment_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_08_to_11_To_Verify_The_Search_(self):
        ast = AssessmentPage(self.driver)
        sleep(10)
        ast.create_assessment_select_haystax_template()
        ast.select_first_asset()
        ast.get_create_assignedto_textbox.clear()
        ast.get_create_assignedto_textbox.send_keys("dee@dee")
        ast.get_create_startdate_textbox.clear()
        ast.get_create_startdate_textbox.send_keys("2015-09-10")
        ast.get_create_enddate_textbox.clear()
        ast.get_create_enddate_textbox.send_keys("2015-09-10")
        with open(self.searchasset_filepath) as data_file:
            data_SearchAsset_text = json.load(data_file)
            for each in data_SearchAsset_text:
                searchText = each["Search_name"]
                ast.search_asset_textbox(searchText)
                sleep(5)
                expectedAfterSearchFilter = ast.get_list_no_matching_records_found.text
                searchNames = ast.get_asset_table("Asset")
                print "Found " + str(len(searchNames)) + " by search." + searchText
                sleep(2)
                for searchName in searchNames:
                    if expectedAfterSearchFilter:
                        self.assertEqual("No matching records found", expectedAfterSearchFilter, "No records to find asset.")
                        sleep(2)
                    else:
                        print searchName.text
                        sleep(2)
                ast.get_search_asset_textbox.clear()
                ast.get_search_asset_textbox.send_keys(Keys.BACKSPACE)
        ast.get_main_create_assessment_button.click()

    @attr(priority = "high")
    #@SkipTest
    def test_AST_12_To_Test_Sorting_on_Create_Assessment(self):
        ast = AssessmentPage(self.driver)
        sleep(10)
        ast.create_assessment_select_haystax_template()
        ast.get_asset_table_column_header("Asset").click()
        sleep(5)
        searchNames = ast.get_asset_table("Asset")
        searchNameslist=[]
        for name in searchNames:
            searchNameslist.append(str(name.text))
        searchNamessorted = sorted(searchNameslist, reverse=True)
        self.assertListEqual(searchNameslist, searchNamessorted, "List is not sorted in Descending order")

        ast.get_asset_table_column_header("Asset").click()
        sleep(5)
        searchNames = ast.get_asset_table("Asset")
        searchNameslist=[]
        for name in searchNames:
            searchNameslist.append(str(name.text))
        searchNamessorted = sorted(searchNameslist)
        self.assertListEqual(searchNameslist, searchNamessorted, "List is not sorted in Ascending order")

    @attr(priority="high")
    #@SkipTest
    def test_AST_26_1_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_statusfilter_dropdown.click()
        try:
            ast.get_statusfilter_InProgress_link.click()
        except:
            ast.get_ast_statusfilter_dropdown.click()
            self.skipTest("In progress option not in the Type filter dropdown available")
        sleep(2)
        for item in ast.get_assessment_table("Status"):
            self.assertTrue(item.text, "In Progress")
        ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_26_2_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_statusfilter_dropdown.click()
        try:
            ast.get_statusfilter_Submitted_link.click()
        except:
            ast.get_ast_statusfilter_dropdown.click()
            self.skipTest("Submitted option not available in the Type filter dropdown")
        sleep(2)
        for item in ast.get_assessment_table("Status"):
            self.assertTrue(item.text, "Submitted")
        ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_26_3_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_statusfilter_dropdown.click()
        try:
            ast.get_statusfilter_NotStarted_link.click()
        except:
            ast.get_ast_statusfilter_dropdown.click()
            self.skipTest("Not Started option not available in Type filter dropdown")
        sleep(2)
        for item in ast.get_assessment_table("Status"):
            self.assertTrue(item.text, "Not Started")
        ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_27_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_typefilter_dropdown.click()
        try:
            ast.get_typefilter_haystax_link.click()
        except:
            ast.get_ast_typefilter_dropdown.click()
            self.skipTest("Haystax School safety option not available in the filter")
        sleep(5)
        for item in ast.get_assessment_table("Assessment"):
            self.assertTrue(item.text, "Haystax School Safety")
        ast.get_resetfilter_button.click()

    #should select the first available link on the dropdown
    @attr(priority="high")
    @SkipTest
    def test_AST_28_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_statusfilter_dropdown.click()
        ast.get_statusfilter_NotStarted_link.click()
        try:
            self.assertEqual(ast.get_ast_statusfilter_dropdown.text, "Not Started")
        except:
            ast.get_resetfilter_button.click()
        ast.get_ast_typefilter_dropdown.click()
        ast.get_typefilter_haystax_link.click()
        try:
            self.assertEqual(ast.get_ast_typefilter_dropdown.text, "Haystax School Safety")
        except:
            ast.get_resetfilter_button.click()
        ast.get_resetfilter_button.click()
        self.assertEqual(ast.get_ast_statusfilter_dropdown.text, "Status")
        self.assertEqual(ast.get_ast_typefilter_dropdown.text, "Type")

    @attr(priority="high")
    #@SkipTest
    def test_AST_29_to_32_To_Verify_The_Search_(self):
        cwd = os.getcwd()
        os.chdir('..')
        searchasset_filepath = os.path.join(os.getcwd(), "data\json_SearchAssessments.json")
        os.chdir(cwd)
        ast = AssessmentPage(self.driver)
        sleep(10)
        with open(searchasset_filepath) as data_file:
            data_SearchAsset_text = json.load(data_file)
            for each in data_SearchAsset_text:
                searchText = each["Search_name"]
                ast.search_assessment_textbox(searchText)
                sleep(5)
                expectedAfterSearchFilter = ast.get_list_no_matching_records_found.text
                searchNames = ast.get_assessment_table("Asset")
                print "Found " + str(len(searchNames)) + " by search." + searchText
                sleep(2)
                for searchName in searchNames:
                    if expectedAfterSearchFilter:
                        self.assertEqual("No matching records found", expectedAfterSearchFilter, "No records to find asset.")
                        sleep(2)
                    else:
                        print searchName.text
                        sleep(2)
                ast.get_search_assessment_textbox.clear()
                ast.get_search_assessment_textbox.send_keys(Keys.BACKSPACE)

    @attr(priority="high")
    #@SkipTest
    def test_AST_34_To_Verify_Delete_Assessment(self):
        ast = AssessmentPage(self.driver)
        ast.app_sanity_check()
        countbeforedeletion = ast.get_total_row_count()
        ast.select_multiple_checkboxes(1)
        ast.get_action_dropdown.click()
        ast.get_action_delete_button.click()
        sleep(2)
        ast.get_delete_assessment_delete_button.click()
        sleep(5)
        countafterdeletion = ast.get_total_row_count()
        self.assertGreater(countbeforedeletion, countafterdeletion, "Couldn't delete asset")

    @attr(priority="high")
    #@SkipTest
    def test_AST_35_To_Verify_Delete_MultipleAssessment(self):
        ast = AssessmentPage(self.driver)
        ast.app_sanity_check()
        countbeforedeletion = ast.get_total_row_count()
        if countbeforedeletion >= 1:
            ast.select_multiple_checkboxes(2)
            sleep(10)
            ast.get_action_dropdown.click()
            ast.get_action_delete_button.click()
            sleep(2)
            ast.get_delete_assessment_delete_button.click()
            sleep(2)
            countafterdeletion = ast.get_total_row_count()
            self.assertGreater(countbeforedeletion, countafterdeletion, "Couldn't delete assets")
        else:
            self.skipTest("No Assessments listed")

    @attr(priority="high")
    #@SkipTest
    def test_AST_36_To_Verify_Delete_Assessment_Cancel(self):
        ast = AssessmentPage(self.driver)
        ast.app_sanity_check()
        countbeforedeletion = ast.get_total_row_count()
        if countbeforedeletion >= 1:
            ast.select_multiple_checkboxes(2)
            sleep(10)
            ast.get_action_dropdown.click()
            ast.get_action_delete_button.click()
            sleep(2)
            ast.get_delete_assessment_cancel_button.click()
            sleep(2)
            countafterdeletion = ast.get_total_row_count()
            self.assertEqual(countbeforedeletion, countafterdeletion, "Assessment deleted even after cancel is pressed")
            ast.deselect_checkboxes()
        else:
            self.skipTest("No Assessments listed")

    @attr(priority="high")
    #@SkipTest
    def test_AST_37_To_Verify_Assign_Assessment(self):
        ast = AssessmentPage(self.driver)
        emailid = "Email@domain"
        ast.app_sanity_check()
        countbeforedeletion = ast.get_total_row_count()
        if countbeforedeletion >= 1:
            ast.select_multiple_checkboxes(1)
            sleep(5)
            ast.get_action_dropdown.click()
            ast.get_action_assign_button.click()
            ast.get_ast_assignto_textbox.send_keys(emailid)
            ast.get_ast_assignto_assign_button.click()
            ast.deselect_checkboxes()
            assignedto = ast.get_assessment_table("Assigned to")
            self.assertEqual(assignedto[0].text, emailid, "Assigned Email id is not appearing")
        else:
            self.skipTest("No Assessments listed")

    @attr(priority="high")
    #@SkipTest
    def test_AST_38_To_Verify_Assign_MultipleAssessment(self):
        ast = AssessmentPage(self.driver)
        emailid = "Email@domain"
        #noofassessment should not be greater than 10
        noofassessments = 10
        ast.app_sanity_check()
        countbeforedeletion = ast.get_total_row_count()
        if countbeforedeletion >= 1:
            ast.select_multiple_checkboxes(noofassessments)
            sleep(5)
            ast.get_action_dropdown.click()
            ast.get_action_assign_button.click()
            ast.get_ast_assignto_textbox.send_keys(emailid)
            ast.get_ast_assignto_assign_button.click()
            ast.deselect_checkboxes()
            assignedto = ast.get_assessment_table("Assigned to")
            if len(assignedto) < noofassessments:
                noofassessments = len(assignedto)
            for num in range(noofassessments):
                 self.assertEqual(assignedto[num].text, emailid, "Assigned Email id is not appearing")
        else:
            self.skipTest("No Assessments listed")

    @attr(priority="high")
    #@SkipTest
    def test_AST_39_To_Verify_Assign_Email_Validation(self):
        ast = AssessmentPage(self.driver)
        ast.app_sanity_check()
        if ast.get_total_row_count() >= 1:
            emailid = ['Email', 'Email.', 'email.com', 'email@']
            #noofassessment should not be greater than 10
            ast.select_multiple_checkboxes(1)
            sleep(5)
            ast.get_action_dropdown.click()
            ast.get_action_assign_button.click()
            for item in emailid:
                ast.get_ast_assignto_textbox.send_keys(item)
                self.assertFalse(ast.get_ast_assignto_assign_button.is_enabled(), "Email Id validation error")
                ast.get_ast_assignto_textbox.clear()
            ast.get_ast_assignto_cancel_button.click()
        else:
            self.skipTest("No assessment listed")

    @attr(priority="high")
    #@SkipTest
    def test_AST_40_To_Verify_Assign_Assessment_cancel(self):
        ast = AssessmentPage(self.driver)
        emailid = ['Email1@domain', 'Email2@domain']
        ast.app_sanity_check()
        countbeforedeletion = ast.get_total_row_count()
        if countbeforedeletion >= 1:
            ast.select_multiple_checkboxes(1)
            sleep(5)
            ast.get_action_dropdown.click()
            sleep(2)
            ast.get_action_assign_button.click()
            #To check if the assigned email is not already present
            if emailid[1] == ast.get_assessment_table("Assigned to"):
                emailidtoenter = emailid[2]
            else:
                emailidtoenter = emailid[1]
            ast.get_ast_assignto_textbox.send_keys(emailidtoenter)
            ast.get_ast_assignto_cancel_button.click()
            sleep(2)
            assignedto = ast.get_assessment_table("Assigned to")
            self.assertNotEqual(assignedto[0].text, emailidtoenter, "Assigned Email id saved on cancel operation")
            sleep(3)
        else:
            self.skipTest("No assessment listed")

    @attr(priority="high")
    #@SkipTest
    def test_AST_44_To_Verify_Overview_Add_Notes(self):
        ast = AssessmentPage(self.driver)
        note = "New Note"
        self.get_assessment_page(ast)
        self.assertEqual(ast.get_ast_overview_text.text, "Overview")
        # ast.get_overview_startdate_textbox.send_keys("2015-09-10")
        # ast.get_overview_enddate_textbox.send_keys("2015-09-10")
        sleep(5)
        ast.get_overview_notes_textbox.clear()
        ast.get_overview_notes_textbox.send_keys(note)
        ast.get_overview_save_button.click()
        #WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ast._ast_saved_text_locator), "Saved"))
        sleep(10)
        self.assertEqual(note, ast.get_overview_notes_textbox.get_attribute("value"), "Entered text not appearing in notes textarea")
        sleep(10)

    @attr(priority="high")
    #@SkipTest
    def test_AST_45_To_Verify_Overview_Upload_image_file_without_caption(self):
        ast = AssessmentPage(self.driver)
        self.get_assessment_page(ast)
        no_of_images_present = len(ast.get_photos_documents_header_text)
        ast.upload_a_file("", "Test_Case_40.jpg")
        no_of_images_present_after = len(ast.get_photos_documents_header_text)
        self.assertGreater(no_of_images_present_after, no_of_images_present, "Upload failed")
        self.assertTrue(ast.get_caption_path("Test_Case_40").is_displayed(), "Upload failed")
        self.assertFalse(self.driver.find_element_by_xpath(ast.get_file_caption_text_path("Test_Case_40")).is_displayed())
        sleep(5)

    @attr(priority="high")
    #@SkipTest
    def test_AST_46_To_Verify_Overview_Upload_pdf_file_without_caption(self):
        ast = AssessmentPage(self.driver)
        self.get_assessment_page(ast)
        no_of_images_present = len(ast.get_photos_documents_header_text)
        ast.upload_a_file("", "Test_Case_44_1.pdf")
        no_of_images_present_after = len(ast.get_photos_documents_header_text)
        self.assertGreater(no_of_images_present_after, no_of_images_present, "Upload failed")
        self.assertTrue(ast.get_caption_path("Test_Case_44_1").is_displayed(), "Upload failed")
        self.assertFalse(self.driver.find_element_by_xpath(ast.get_file_caption_text_path("Test_Case_44_")).is_displayed())
        sleep(5)

    @attr(priority="high")
    #@SkipTest
    def test_AST_47_1_To_Verify_Overview_Upload_image_file_with_caption(self):
        ast = AssessmentPage(self.driver)
        self.get_assessment_page(ast)
        no_of_images_present = len(ast.get_photos_documents_header_text)
        ast.upload_a_file("Test_Case_40", "Test_Case_40.jpg")
        no_of_images_present_after = len(ast.get_photos_documents_header_text)
        self.assertGreater(no_of_images_present_after, no_of_images_present, "Upload failed")
        self.assertTrue(ast.get_caption_path("Test_Case_40").is_displayed(), "Upload failed")
        self.assertTrue(ast.get_file_caption_text("Test_Case_40").is_displayed(), "Uploaded file doesnt appear with caption specified")
        sleep(5)

    @attr(priority="high")
    #@SkipTest
    def test_AST_47_2_To_Verify_Overview_Upload_pdf_file_with_caption(self):
        ast = AssessmentPage(self.driver)
        self.get_assessment_page(ast)
        no_of_images_present = len(ast.get_photos_documents_header_text)
        ast.upload_a_file("Test_Case_44_1", "Test_Case_44_1.pdf")
        no_of_images_present_after = len(ast.get_photos_documents_header_text)
        self.assertGreater(no_of_images_present_after, no_of_images_present, "Upload failed")
        self.assertTrue(ast.get_caption_path("Test_Case_44_1").is_displayed(), "Upload failed")
        self.assertTrue(ast.get_file_caption_text("Test_Case_44_").is_displayed(), "Uploaded file doesnt appear with caption specified")
        sleep(5)

    @attr(priority="high")
    #@SkipTest
    def test_AST_50_To_Verify_Overview_Upload_File_Cancel(self):
        ast = AssessmentPage(self.driver)
        self.get_assessment_page(ast)
        no_of_images_present = len(ast.get_photos_documents_header_text)
        ast.upload_a_file_cancel("Test_Case_41", "Test_Case_41.jpg")
        no_of_images_present_after = len(ast.get_photos_documents_header_text)
        self.assertEqual(no_of_images_present_after, no_of_images_present, "Upload cancel failed")
        self.assertFalse(ast.get_caption_path("Test_Case_41").is_displayed(), "Upload cancel failed")
        sleep(5)

    @attr(priority="high")
    #@SkipTest
    def test_AST_58_To_Verify_Overview_Dates_Change_Day(self):
        ast = AssessmentPage(self.driver)
        start_date = datetime.today().date()
        end_date = start_date + timedelta(days=1)
        self.get_assessment_page(ast)
        self.assertEqual(ast.get_ast_overview_text.text, "Overview")
        ast.get_overview_startdate_textbox.clear()
        ast.get_overview_startdate_textbox.send_keys(str(start_date))
        ast.get_overview_enddate_textbox.clear()
        ast.get_overview_enddate_textbox.send_keys(str(end_date))
        ast.get_overview_enddate_textbox.send_keys(Keys.TAB)
        sleep(5)
        ast.get_overview_save_button.click()
        #WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ast._ast_saved_text_locator), "Saved"))
        sleep(10)
        self.assertEqual(str(start_date), ast.get_overview_startdate_textbox.get_attribute("value"))
        self.assertEqual(str(end_date), ast.get_overview_enddate_textbox.get_attribute("value"))

    @attr(priority="high")
    #@SkipTest
    def test_AST_59_To_Verify_Overview_Dates_Change_Month(self):
        ast = AssessmentPage(self.driver)
        start_date = datetime.today().date()
        end_date = start_date + timedelta(days=31)
        self.get_assessment_page(ast)
        self.assertEqual(ast.get_ast_overview_text.text, "Overview")
        ast.get_overview_startdate_textbox.clear()
        ast.get_overview_startdate_textbox.send_keys(str(start_date))
        ast.get_overview_enddate_textbox.clear()
        ast.get_overview_enddate_textbox.send_keys(str(end_date))
        ast.get_overview_enddate_textbox.send_keys(Keys.TAB)
        sleep(5)
        ast.get_overview_save_button.click()
        #WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ast._ast_saved_text_locator), "Saved"))
        sleep(10)
        self.assertEqual(str(start_date), ast.get_overview_startdate_textbox.get_attribute("value"))
        self.assertEqual(str(end_date), ast.get_overview_enddate_textbox.get_attribute("value"))

    @attr(priority="high")
    #@SkipTest
    def test_AST_60_To_Verify_Overview_Dates_Change_Year(self):
        ast = AssessmentPage(self.driver)
        start_date = datetime.today().date()
        end_date = start_date + timedelta(days=365)
        self.get_assessment_page(ast)
        self.assertEqual(ast.get_ast_overview_text.text, "Overview")
        ast.get_overview_startdate_textbox.clear()
        ast.get_overview_startdate_textbox.send_keys(str(start_date))
        ast.get_overview_enddate_textbox.clear()
        ast.get_overview_enddate_textbox.send_keys(str(end_date))
        ast.get_overview_enddate_textbox.send_keys(Keys.TAB)
        sleep(5)
        ast.get_overview_save_button.click()
        #WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, ast._ast_saved_text_locator), "Saved"))
        sleep(10)
        self.assertEqual(str(start_date), ast.get_overview_startdate_textbox.get_attribute("value"))
        self.assertEqual(str(end_date), ast.get_overview_enddate_textbox.get_attribute("value"))

    def get_assessment_page(self, ast):
        sleep(5)
        try:
            self.assertTrue(ast.get_breadcrumb_assessmentname_text.is_displayed())
            return True
        except:
            if not ast.get_main_create_assessment_button.is_displayed():
                ast.recoverapp()
            if ast.select_assessment(ast.asset_school_name) == False:
                sleep(10)
                ast.create_assessment(ast.asset_school_name)
                ast.select_assessment(ast.asset_school_name)


if __name__ == '__main__':
    unittest.main(verbosity=2)

