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
from pages.IconListPage import IconListPage
import json, os, re


class AssessmenttPageTest(BaseTestCase):

    @attr(priority="high")
    @SkipTest
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
    @SkipTest
    def test_AST_01_To_test_creation_of_new_assessment_without_StartEnd_and_Email_info(self):
        ast = AssessmentPage(self.driver)
        sleep(10)
        ast.get_main_create_assessment_button.click()
        sleep(10)
        ast.get_create_templatetype_dropdown.click()
        ast.get_create_haystax_template_option.click()
        ast.get_create_assignedto_textbox.clear()
        ast.get_create_startdate_textbox.clear()
        ast.get_create_enddate_textbox.clear()

    @attr(priority="high")
    #@SkipTest
    def test_AST_26_1_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_statusfilter_dropdown.click()
        ast.get_statusfilter_InProgress_link.click()
        sleep(2)
        for item in ast.get_assessment_table("Status"):
            self.assertTrue(item.text, "In Progress")
        ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_26_2_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_statusfilter_dropdown.click()
        ast.get_statusfilter_Submitted_link.click()
        sleep(2)
        for item in ast.get_assessment_table("Status"):
            self.assertTrue(item.text, "Submitted")
        ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_26_3_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_statusfilter_dropdown.click()
        ast.get_statusfilter_NotStarted_link.click()
        sleep(2)
        for item in ast.get_assessment_table("Status"):
            self.assertTrue(item.text, "Not Started")
        ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_27_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_typefilter_dropdown.click()
        ast.get_typefilter_haystax_link.click()
        sleep(2)
        for item in ast.get_assessment_table("Assessment"):
            self.assertTrue(item.text, "Haystax School Safety")
        ast.get_resetfilter_button.click()


    @attr(priority="high")
    #@SkipTest
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
    def test_AS_29_to_32_To_Verify_The_Search_(self):
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
                sleep(2)
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


    @attr(priority="high")
    #@SkipTest
    def test_AS_34_To_Verify_Delete_Assessment(self):
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
    def test_AS_35_To_Verify_Delete_MultipleAssessment(self):
        ast = AssessmentPage(self.driver)
        ast.app_sanity_check()
        countbeforedeletion = ast.get_total_row_count()
        ast.select_multiple_checkboxes(2)
        sleep(10)
        ast.get_action_dropdown.click()
        ast.get_action_delete_button.click()
        sleep(2)
        ast.get_delete_assessment_delete_button.click()
        sleep(2)
        countafterdeletion = ast.get_total_row_count()
        self.assertGreater(countbeforedeletion, countafterdeletion, "Couldn't delete assets")

    @attr(priority="high")
    #@SkipTest
    def test_AS_36_To_Verify_Delete_Assessment_Cancel(self):
        ast = AssessmentPage(self.driver)
        ast.app_sanity_check()
        countbeforedeletion = ast.get_total_row_count()
        ast.select_multiple_checkboxes(2)
        sleep(10)
        ast.get_action_dropdown.click()
        ast.get_action_delete_button.click()
        sleep(2)
        ast.get_delete_assessment_cancel_button.click()
        sleep(2)
        countafterdeletion = ast.get_total_row_count()
        self.assertEqual(countbeforedeletion, countafterdeletion, "Assessment deleted even after cancel is pressed")

    @attr(priority="high")
    #@SkipTest
    def test_AS_37_To_Verify_Assign_Assessment(self):
        ast = AssessmentPage(self.driver)
        emailid = "Email@domain"
        ast.app_sanity_check()
        ast.select_multiple_checkboxes(1)
        sleep(5)
        ast.get_action_dropdown.click()
        ast.get_action_assign_button.click()
        ast.get_ast_assignto_textbox.send_keys(emailid)
        ast.get_ast_assignto_assign_button.click()
        sleep(2)
        assignedto = ast.get_assessment_table("Assigned to")
        self.assertEqual(assignedto[0].text, emailid, "Assigned Email id is not appearing")

    @attr(priority="high")
    #@SkipTest
    def test_AS_38_To_Verify_Assign_MultipleAssessment(self):
        ast = AssessmentPage(self.driver)
        emailid = "Email@domain"
        #noofassessment should not be greater than 10
        noofassessments = 10
        ast.app_sanity_check()
        ast.select_multiple_checkboxes(noofassessments)
        sleep(5)
        ast.get_action_dropdown.click()
        ast.get_action_assign_button.click()
        ast.get_ast_assignto_textbox.send_keys(emailid)
        ast.get_ast_assignto_assign_button.click()
        sleep(2)
        assignedto = ast.get_assessment_table("Assigned to")
        for num in range(noofassessments):
             self.assertEqual(assignedto[num].text, emailid, "Assigned Email id is not appearing")

    @attr(priority="high")
    #@SkipTest
    def test_AS_39_To_Verify_Assign_Email_Validation(self):
        ast = AssessmentPage(self.driver)
        ast.app_sanity_check()
        emailid = ['Email', 'Email.', 'email.com', 'email@']
        #noofassessment should not be greater than 10
        noofassessments = 1
        ast.select_multiple_checkboxes(noofassessments)
        sleep(5)
        ast.get_action_dropdown.click()
        ast.get_action_assign_button.click()
        for item in emailid:
            ast.get_ast_assignto_textbox.send_keys(item)
            self.assertFalse(ast.get_ast_assignto_assign_button.is_enabled(), "Email Id validation error")
            ast.get_ast_assignto_textbox.clear()

    @attr(priority="high")
    #@SkipTest
    def test_AS_40_To_Verify_Assign_Assessment_cancel(self):
        ast = AssessmentPage(self.driver)
        emailid = ['Email1@domain', 'Email2@domain']
        ast.app_sanity_check()
        ast.select_multiple_checkboxes(1)
        sleep(5)
        ast.get_action_dropdown.click()
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


    @attr(priority="high")
    #@SkipTest
    def test_AS_41_To_Verify_overview(self):
        ast = AssessmentPage(self.driver)
        if ast.select_assessment("september school"):
            pass
        else:
            ast.create_assessment("september school")

    @attr(priority="high")
    #@SkipTest
    def test_AS_05_To_create_assessment(self):
        ast = AssessmentPage(self.driver)
        check = 0
        assetname = "September school"
        sleep(8)
        ast.create_assessment(assetname)
        sleep(5)
        ast.search_assessment_textbox(assetname)
        sleep(2)
        for item in ast.get_assessment_table("Asset"):
            if (item.text  == assetname) and (item.value_of_css_property("background-color") == "rgba(255, 236, 158, 1)"):
                check = 1
                break
        ast.get_search_assessment_textbox.clear()
        self.assertFalse(check == 0, "No assessment is created or is not appearing with yellow background")


if __name__ == '__main__':
    unittest.main(verbosity=2)

