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
from nose.plugins.skip import SkipTest
from time import sleep
from datetime import date, timedelta, datetime
import json, os, re


class AssessmenttPageTest(BaseTestCase):

    filepath = "data" + os.sep + "json_SearchAssessments.json"
    cwd = os.getcwd()
    os.chdir('..')
    searchasset_filepath = os.path.join(os.getcwd(), filepath)
    os.chdir(cwd)


    def setUp(self):
        self.errors_and_failures = self.tally()
        self.ast = AssessmentPage(self.driver)


    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        try:
            self.ast.get_main_create_assessment_red_button.click()
        except:
            pass

    @attr(priority="high")
    @SkipTest
    @attr(status='smoke')
    def test_smoketest_assessment(self):
        sleep(2)
        try:
            self.assertEqual(self.ast.get_ast_app_name.text, "Assessments")
        except:
            print "The Assessment link text not available"
        self.ast.get_ast_statusfilter_dropdown.click()
        try:
            self.assertTrue(self.ast.get_statusfilter_InProgress_link)
            self.assertTrue(self.ast.get_statusfilter_NotStarted_link)
            self.assertTrue(self.ast.get_statusfilter_Submitted_link)
        except:
            print " One or more filter option for status not present"

        try:
            self.assertEqual(self.ast.get_resetfilter_button.text, "Reset filters")
        except:
            print "Reset filters button not available or text not matching"

        try:
            self.assertTrue(self.ast.get_search_assessment_textbox)
        except:
            print "Search textbox not available"

        try:
            self.assertTrue(self.ast.get_main_create_assessment_button)
        except:
            print "Create assessment button not present"

    @attr(priority="high")
    #@SkipTest
    def test_ast_01_To_verify_noemailid_createassessment(self):
        selecttemplate = self.ast.create_assessment_select_haystax_template()
        #self.assertTrue(selecttemplate[0], selecttemplate[1])
        self.ast.select_first_asset()
        self.ast.get_create_assignedto_textbox.clear()
        self.ast.get_create_startdate_textbox.send_keys("2015-09-10")
        self.ast.get_create_enddate_textbox.send_keys("2015-09-11")
        self.assertFalse(self.ast.get_create_assessments_button.is_enabled(),"Create assessment button enabled even without entering email")


    @attr(priority="high")
    #@SkipTest
    def test_ast_02_To_verify_nodate_createassessment(self):
        self.ast.create_assessment_select_haystax_template()
        self.ast.select_first_asset()
        self.ast.get_create_assignedto_textbox.clear()
        self.ast.get_create_assignedto_textbox.send_keys("deep@dee")
        self.ast.get_create_startdate_textbox.clear()
        self.ast.get_create_enddate_textbox.clear()
        self.assertFalse(self.ast.get_create_assessments_button.is_enabled(),"Create assessment button enabled even without entering start and end date")

    @attr(priority="high")
    #@SkipTest
    def test_ast_04_To_verify_datevaidation_createassessment(self):
        dateformat = ['date', '23-11-2015', '2015-22-11']
        self.ast.create_assessment_select_haystax_template()
        self.ast.select_first_asset()
        for date in dateformat:
            self.ast.get_create_startdate_textbox.clear()
            self.ast.get_create_startdate_textbox.send_keys(date)
            self.ast.get_create_startdate_textbox.send_keys(Keys.TAB)
            self.assertNotEqual(self.ast.get_create_startdate_textbox.text, date, "Start date textbox no date format validation")
        for date in dateformat:
            self.ast.get_create_enddate_textbox.clear()
            self.ast.get_create_enddate_textbox.send_keys(date)
            self.ast.get_create_enddate_textbox.send_keys(Keys.TAB)
            self.assertNotEqual(self.ast.get_create_enddate_textbox.text, date, "Start date textbox no date format validation")

    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_ast_05_To_create_assessment(self):
        flag = 0
        count = 0
        if self.ast.create_assessment(self.ast.asset_school_name) == False:
            self.assertFalse("Assessment creation failed")
        self.ast.search_assessment_textbox(self.ast.asset_school_name)
        sleep(5)
        for item in self.ast.get_assessment_table("Asset"):
            count = count + 1
            if (item.text  == self.ast.asset_school_name) and (item.value_of_css_property("background-color")
                                                                   == "rgba(255, 236, 158, 1)"):
                flag = 1
                status = self.ast.get_assessment_table_row_values(count, "Status").text
                assignedto = self.ast.get_assessment_table_row_values(count, "Assigned to").text
                creationdate = self.ast.get_assessment_table_row_values(count, "Created").text
        self.ast.get_search_assessment_textbox.clear()
        self.ast.get_search_assessment_textbox.send_keys(Keys.BACKSPACE)
        self.assertFalse(flag == 0, "No assessment is created or is not appearing with yellow background")
        self.assertEqual(status ,"Not Started", "The newly created assessment status is not 'Not Started'")
        self.assertEqual(creationdate, str(date.today()), "The newly created assessment creation date is not showing todays date")
#        self.assertEqual(assignedto, self.username, "When no email is specified the users login should appear")

    @attr(priority="high")
    #@SkipTest
    def test_ast_06_To_verify_emailid_field_createassessment(self):
        emailid = ['Email', 'Email.', 'email.com', 'email@']
        self.ast.create_assessment_select_haystax_template()
        sleep(2)
        self.ast.get_create_assignedto_textbox.clear()
        for item in emailid:
            self.ast.get_create_assignedto_textbox.send_keys(item)
            self.ast.get_create_assignedto_textbox.send_keys(Keys.TAB)
            sleep(5)
            self.assertEqual("rgba(192, 57, 43, 1)", self.ast.get_create_assignedto_textbox.value_of_css_property("border-bottom-color"),  "Email ID validation error in create assessment")
            self.ast.get_create_assignedto_textbox.clear()

    @attr(priority="high")
    #@SkipTest
    def test_ast_08_to_11_To_Verify_The_Search_(self):
        self.ast.create_assessment_select_haystax_template()
        self.ast.select_first_asset()
        self.ast.get_create_assignedto_textbox.clear()
        self.ast.get_create_assignedto_textbox.send_keys("dee@dee")
        self.ast.get_create_startdate_textbox.clear()
        self.ast.get_create_startdate_textbox.send_keys("2015-09-10")
        self.ast.get_create_enddate_textbox.clear()
        self.ast.get_create_enddate_textbox.send_keys("2015-09-10")
        with open(self.searchasset_filepath) as data_file:
            data_SearchAsset_text = json.load(data_file)
            for each in data_SearchAsset_text:
                searchText = each["Search_name"]
                self.ast.search_asset_textbox(searchText)
                sleep(5)
                searchNames = self.ast.get_asset_table("Asset")
                sleep(2)
                for searchName in searchNames:
                    if self.ast.get_list_no_matching_records_found.text:
                        self.assertEqual("No matching records found", self.ast.get_list_no_matching_records_found.text, "No records to find asset.")
                        sleep(2)
                    else:
                       # print searchName.text
                        sleep(2)
                self.ast.get_search_asset_textbox.clear()
                self.ast.get_search_asset_textbox.send_keys(Keys.BACKSPACE)

    @attr(priority = "high")
    #@SkipTest
    def test_ast_12_To_Test_Sorting_on_Create_Assessment(self):
        self.ast.create_assessment_select_haystax_template()
        self.ast.get_asset_table_column_header("Asset").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, self.ast._ast_asset_table_header_locator)))
        searchNames = self.ast.get_asset_table("Asset")
        searchNameslist=[]
        for name in searchNames:
            searchNameslist.append(str(name.text))
        if self.ast.get_asset_table_column_header("Asset").get_attribute("class") == "sorting_desc":
            searchNamessorted = sorted(searchNameslist, reverse=True)
            self.assertListEqual(searchNameslist, searchNamessorted, "List is not sorted in Descending order")
        else:
            searchNamessorted = sorted(searchNameslist)
            self.assertListEqual(searchNameslist, searchNamessorted, "List is not sorted in Ascending order")
        sleep(10)
        self.ast.get_asset_table_column_header("Asset").click()
        sleep(10)
        searchNames = self.ast.get_asset_table("Asset")
        searchNameslist=[]
        for name in searchNames:
            searchNameslist.append(str(name.text))
        if self.ast.get_asset_table_column_header("Asset").get_attribute("class") == "sorting_desc":
            searchNamessorted = sorted(searchNameslist,reverse=True)
            self.assertListEqual(searchNameslist, searchNamessorted, "List is not sorted in Descending order")
        else:
            searchNamessorted = sorted(searchNameslist)
            self.assertListEqual(searchNameslist, searchNamessorted, "List is not sorted in Ascending order")

    @attr(priority="high")
    #@SkipTest
    def test_ast_26_1_To_Test_Different_filters_on_Assessment_page(self):
        self.ast.get_ast_statusfilter_dropdown.click()
        try:
            self.ast.get_statusfilter_InProgress_link.click()
        except:
            self.ast.get_ast_statusfilter_dropdown.click()
            self.skipTest("In progress option not in the Type filter dropdown available")
        sleep(2)
        for item in self.ast.get_assessment_table("Status"):
            self.assertTrue(item.text, "In Progress")
        self.ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_ast_26_2_To_Test_Different_filters_on_Assessment_page(self):
        self.ast.get_ast_statusfilter_dropdown.click()
        try:
            self.ast.get_statusfilter_Submitted_link.click()
        except:
            self.ast.get_ast_statusfilter_dropdown.click()
            self.skipTest("Submitted option not available in the Type filter dropdown")
        sleep(2)
        for item in self.ast.get_assessment_table("Status"):
            self.assertTrue(item.text, "Submitted")
        self.ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_ast_26_3_To_Test_Different_filters_on_Assessment_page(self):
        self.ast.get_ast_statusfilter_dropdown.click()
        try:
            self.ast.get_statusfilter_NotStarted_link.click()
        except:
            self.ast.get_ast_statusfilter_dropdown.click()
            self.skipTest("Not Started option not available in Type filter dropdown")
        sleep(2)
        for item in self.ast.get_assessment_table("Status"):
            self.assertTrue(item.text, "Not Started")
        self.ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_ast_27_To_Test_Different_filters_on_Assessment_page(self):
        self.ast.get_ast_typefilter_dropdown.click()
        try:
            self.ast.get_typefilter_haystax_link.click()
        except:
            self.ast.get_ast_typefilter_dropdown.click()
            self.skipTest("Haystax School safety option not available in the filter")
        sleep(5)
        for item in self.ast.get_assessment_table("Assessment"):
            self.assertTrue(item.text, "Haystax School Safety")
        self.ast.get_resetfilter_button.click()

    #should select the first available link on the dropdown
    @attr(priority="high")
    @SkipTest
    def test_ast_28_To_Test_Different_filters_on_Assessment_page(self):
        self.ast.get_ast_statusfilter_dropdown.click()
        self.ast.get_statusfilter_NotStarted_link.click()
        try:
            self.assertEqual(self.ast.get_ast_statusfilter_dropdown.text, "Not Started")
        except:
            self.ast.get_resetfilter_button.click()
        self.ast.get_ast_typefilter_dropdown.click()
        self.ast.get_typefilter_haystax_link.click()
        try:
            self.assertEqual(self.ast.get_ast_typefilter_dropdown.text, "Haystax School Safety")
        except:
            self.ast.get_resetfilter_button.click()
        self.ast.get_resetfilter_button.click()
        self.assertEqual(self.ast.get_ast_statusfilter_dropdown.text, "Status")
        self.assertEqual(self.ast.get_ast_typefilter_dropdown.text, "Type")

    @attr(priority="high")
    #@SkipTest
    def test_ast_29_to_32_To_Verify_The_Search_(self):
        cwd = os.getcwd()
        os.chdir('..')
        searchasset_filepath = os.path.join(os.getcwd(), "data\json_SearchAssessments.json")
        os.chdir(cwd)
        with open(searchasset_filepath) as data_file:
            data_SearchAsset_text = json.load(data_file)
            for each in data_SearchAsset_text:
                searchText = each["Search_name"]
                self.ast.search_assessment_textbox(searchText)
                sleep(5)
                expectedAfterSearchFilter = self.ast.get_list_no_matching_records_found.text
                searchNames = self.ast.get_assessment_table("Asset")
                sleep(2)
                for searchName in searchNames:
                    if expectedAfterSearchFilter:
                        self.assertEqual("No matching records found", expectedAfterSearchFilter, "No records to find asset.")
                        sleep(2)
                    else:
                       # print searchName.text
                        sleep(2)
                self.ast.get_search_assessment_textbox.clear()
                self.ast.get_search_assessment_textbox.send_keys(Keys.BACKSPACE)

    @attr(priority="high")
    #@SkipTest
    def test_ast_34_To_Verify_Delete_Assessment(self):
        countbeforedeletion = self.ast.get_total_row_count()
        self.ast.select_multiple_checkboxes(1)
        self.ast.get_action_dropdown.click()
        self.ast.get_action_delete_button.click()
        self.ast.get_delete_assessment_delete_button.click()
        sleep(2)#Mandatory sleep for the list to refresh
        countafterdeletion = self.ast.get_total_row_count()
        self.assertGreater(countbeforedeletion, countafterdeletion, "Couldn't delete asset")

    @attr(priority="high")
    #@SkipTest
    def test_ast_35_To_Verify_Delete_MultipleAssessment(self):
        countbeforedeletion = self.ast.get_total_row_count()
        if countbeforedeletion >= 1:
            self.ast.select_multiple_checkboxes(2)
            self.ast.get_action_dropdown.click()
            self.ast.get_action_delete_button.click()
            self.ast.get_delete_assessment_delete_button.click()
            sleep(2)#mandatory for the list to refresh
            countafterdeletion = self.ast.get_total_row_count()
            self.assertGreater(countbeforedeletion, countafterdeletion, "Couldn't delete assets")
        else:
            self.skipTest("No Assessments listed")

    @attr(priority="high")
    #@SkipTest
    def test_ast_36_To_Verify_Delete_Assessment_Cancel(self):
        countbeforedeletion = self.ast.get_total_row_count()
        if countbeforedeletion >= 1:
            self.ast.select_multiple_checkboxes(2)
            self.ast.get_action_dropdown.click()
            self.ast.get_action_delete_button.click()
            self.ast.get_delete_assessment_cancel_button.click()
            sleep(2)#mandatory for the list to refresh
            countafterdeletion = self.ast.get_total_row_count()
            self.assertEqual(countbeforedeletion, countafterdeletion, "Assessment deleted even after cancel is pressed")
            #self.ast.deselect_checkboxes()
        else:
            self.skipTest("No Assessments listed")

    @attr(priority="high")
    #@SkipTest
    def test_ast_37_To_Verify_Assign_Assessment(self):
        emailid = "Email@domain"
        countbeforedeletion = self.ast.get_total_row_count()
        if countbeforedeletion >= 1:
            self.ast.select_multiple_checkboxes(1)
            self.ast.get_action_dropdown.click()
            self.ast.get_action_assign_button.click()
            self.ast.get_ast_assignto_textbox.send_keys(emailid)
            self.ast.get_ast_assignto_assign_button.click()
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, ".//*[@id='assessment_actions_dropdown']/button[2]")))
            assignedto = self.ast.get_assessment_table("Assigned to")
            self.assertEqual(assignedto[0].text, emailid, "Assigned Email id is not appearing")
        else:
            self.skipTest("No Assessments listed")

    @attr(priority="high")
    #@SkipTest
    def test_ast_38_To_Verify_Assign_MultipleAssessment(self):
        emailid = "Email@domain"
        #noofassessment should not be greater than 10
        noofassessments = 2
        countbeforedeletion = self.ast.get_total_row_count()
        if countbeforedeletion >= 1:
            self.ast.select_multiple_checkboxes(noofassessments)
            self.ast.get_action_dropdown.click()
            self.ast.get_action_assign_button.click()
            self.ast.get_ast_assignto_textbox.send_keys(emailid)
            self.ast.get_ast_assignto_assign_button.click()
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, ".//*[@id='assessment_actions_dropdown']/button[2]")))
            assignedto = self.ast.get_assessment_table("Assigned to")
            if len(assignedto) < noofassessments:
                noofassessments = len(assignedto)
            for num in range(noofassessments):
                 self.assertEqual(assignedto[num].text, emailid, "Assigned Email id is not appearing")
        else:
            self.skipTest("No Assessments listed")

    @attr(priority="high")
    #@SkipTest
    def test_ast_39_To_Verify_Assign_Email_Validation(self):
        if self.ast.get_total_row_count() >= 1:
            emailid = ['Email', 'Email.', 'email.com', 'email@']
            #noofassessment should not be greater than 10
            self.ast.select_multiple_checkboxes(1)
            self.ast.get_action_dropdown.click()
            self.ast.get_action_assign_button.click()
            for item in emailid:
                self.ast.get_ast_assignto_textbox.send_keys(item)
                sleep(2)
                #self.assertFalse(self.ast.get_self.ast_assignto_assign_button.is_enabled(), "Email Id validation error")
                self.assertEqual("rgba(192, 57, 43, 1)", self.ast.get_ast_assignto_textbox.value_of_css_property("border-bottom-color"),  "Email ID validation error in create assessment")
                self.ast.get_ast_assignto_textbox.clear()
            self.ast.get_ast_assignto_cancel_button.click()
        else:
            self.skipTest("No assessment listed")

    @attr(priority="high")
    #@SkipTest
    def test_ast_40_To_Verify_Assign_Assessment_cancel(self):
        emailid = ['Email1@domain', 'Email2@domain']
        countbeforedeletion = self.ast.get_total_row_count()
        if countbeforedeletion >= 1:
            self.ast.select_multiple_checkboxes(1)
            self.ast.get_action_dropdown.click()
            self.ast.get_action_assign_button.click()
            #To check if the assigned email is not already present
            if emailid[1] == self.ast.get_assessment_table("Assigned to"):
                emailidtoenter = emailid[2]
            else:
                emailidtoenter = emailid[1]
            self.ast.get_ast_assignto_textbox.send_keys(emailidtoenter)
            self.ast.get_ast_assignto_cancel_button.click()
            WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(
                (By.XPATH, ".//*[@id='assessment_actions_dropdown']/button[2]")))
            assignedto = self.ast.get_assessment_table("Assigned to")
            self.assertNotEqual(assignedto[0].text, emailidtoenter, "Assigned Email id saved on cancel operation")
        else:
            self.skipTest("No assessment listed")

