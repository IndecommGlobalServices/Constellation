__author__ = 'Deepa.Sivadas'
from selenium.webdriver.common.keys import Keys
from pages.assessmentpage import AssessmentPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from time import sleep
from datetime import date, timedelta, datetime
import json, os


class AssessmenttPageTest(BaseTestCase):
    filepath = "data" + os.sep + "json_SearchAssessments.json"
    cwd = os.getcwd()
    os.chdir('..')
    searchasset_filepath = os.path.join(os.getcwd(), filepath)
    os.chdir(cwd)

    @classmethod
    def setUpClass(cls):
        super(AssessmenttPageTest, cls).setUpClass()
        cls.ast = AssessmentPage(cls.driver)
        try:
            cls.ast.get_asset_avilability("")
            cls.ast.delete_existing_assessments()
        except:
            pass

    def setUp(self):
        self.errors_and_failures = self.tally()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        try:
            self.ast.get_main_create_assessment_red_button.click()
        except:
            pass

    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_assessment_smoke(self):
        self.assertTrue(self.ast.get_main_create_assessment_button, "Create assessment button not available")
        self.assertTrue(self.ast.get_ast_typefilter_dropdown.is_displayed(), "Type filter dropdown not available")
        self.assertTrue(self.ast.get_ast_statusfilter_dropdown.is_displayed(), "Status filter dropdown not available")
        self.assertTrue(self.ast.get_resetfilter_button.is_displayed(), "Reset button not available")
        self.ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_ast_01_To_verify_noemailid_createassessment(self):
        count = 0
        flag = 0
        assignedto = ""
        start_date = datetime.today().date()
        end_date = start_date + timedelta(days=31)
        self.ast.create_assessment(str(start_date), str(end_date), "")
        self.ast.search_assessment_textbox(self.ast.asset_school_name)
        sleep(10)
        for item in self.ast.get_assessment_table("Asset"):
            count = count + 1
            if (item.text == self.ast.asset_school_name) and (item.value_of_css_property("background-color")
                                                                   == "rgba(255, 236, 158, 1)"):
                flag = 1
                assignedto = self.ast.get_assessment_table_row_values(count, r"Assigned to").text
        self.ast.get_search_assessment_textbox.clear()
        self.ast.get_search_assessment_textbox.send_keys(Keys.BACKSPACE)
        if flag == 1:
            self.assertEqual(assignedto, self.ast.username, "When no email is specified the users login should appear")
        else:
            self.assertTrue(False, "Assessment creation had failed or newly created assessment is not appearing in yellow color background")


    @attr(priority="high")
    #@SkipTest
    def test_ast_04_To_verify_datevalidation_createassessment(self):
        dateformat = ['date', '23-11-2015', '2015-22-11']
        self.ast.create_assessment_select_haystax_template()
        for date in dateformat:
            self.ast.get_create_startdate_textbox.clear()
            self.ast.get_create_startdate_textbox.send_keys(date)
            self.ast.get_create_startdate_textbox.send_keys(Keys.TAB)
            self.assertNotEqual(self.ast.get_create_startdate_textbox.text, date, "Start date textbox no date format validation")
        for date in dateformat:
            self.ast.get_create_enddate_textbox.clear()
            self.ast.get_create_enddate_textbox.send_keys(date)
            self.ast.get_create_enddate_textbox.send_keys(Keys.TAB)
            self.assertNotEqual(self.ast.get_create_enddate_textbox.text, date, "End date textbox no date format validation")
        self.ast.get_create_assessment_cancel_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_ast_05_To_create_assessment(self):
        flag = 0
        count = 0
        start_date = datetime.today().date()
        end_date = start_date + timedelta(days=31)
        self.ast.create_assessment(str(start_date), str(end_date), "Bijesh.Gupta@Indecomm.net")
        self.ast.search_assessment_textbox(self.ast.asset_school_name)
        sleep(8)
        for item in self.ast.get_assessment_table("Asset"):
            count = count + 1
            if (item.text == self.ast.asset_school_name) and (item.value_of_css_property("background-color")
                                                                   == "rgba(255, 236, 158, 1)"):
                flag = 1
                status = self.ast.get_assessment_table_row_values(count, "Status").text
                creationdate = self.ast.get_assessment_table_row_values(count, "Created").text
        self.ast.get_search_assessment_textbox.clear()
        self.ast.get_search_assessment_textbox.send_keys(Keys.BACKSPACE)
        self.assertFalse(flag == 0, "No assessment is created or is not appearing with yellow background")
        self.assertEqual(status, "Not Started", "The newly created assessment status is not 'Not Started'")
        self.assertEqual(creationdate, str(date.today()), "The newly created assessment creation date is not showing todays date")

    @attr(priority="high")
    @SkipTest
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

    # @attr(priority="high")
    # @SkipTest
    # @attr(status='smoke')
    # def test_ast_08_to_11_To_Verify_The_Search_(self):
    #     flag = 0
    #     self.ast.create_assessment_select_haystax_template()
    #     with open(self.searchasset_filepath) as data_file:
    #         data_SearchAsset_text = json.load(data_file)
    #         for each in data_SearchAsset_text:
    #             searchText = each["Search_name"]
    #             self.ast.search_asset_textbox(searchText)
    #             sleep(5)
    #             if len(self.ast.get_asset_table("Asset")) <= 0:
    #                 self.assertEqual("No matching records found", self.ast.get_assetlist_no_matching_records_found.text,
    #                                      "No records to find asset. Searched string is :" + searchText)
    #                 flag = 1
    #             else:
    #                 for searchName in self.ast.get_asset_table("Asset"):
    #                     if searchText in searchName.text:
    #                         flag = 1
    #                 if flag == 0:
    #                     for searchName in self.ast.get_asset_table("Type"):
    #                         if searchText in searchName.text:
    #                             flag = 1
    #             if flag == 0:
    #                 self.assertTrue(False, "The search result doesnt contain the text that is searched. Searched string is :" + searchText)
    #             self.ast.get_search_asset_textbox.clear()
    #             self.ast.get_search_asset_textbox.send_keys(Keys.BACKSPACE)
    #             sleep(2)

    # @attr(priority = "high")
    # @SkipTest
    # def test_ast_12_To_Test_Sorting_on_Create_Assessment(self):
    #     self.ast.create_assessment_select_haystax_template()
    #     self.ast.get_asset_table_column_header("Asset").click()
    #     sleep(5)
    #     searchNames = self.ast.get_asset_table("Asset")
    #     searchNameslist=[]
    #     for name in searchNames:
    #         searchNameslist.append(str(name.text))
    #     if self.ast.get_asset_table_column_header("Asset").get_attribute("class") == "sorting_desc":
    #         searchNamessorted = sorted(searchNameslist, reverse=True)
    #         self.assertListEqual(searchNameslist, searchNamessorted, "List is not sorted in Descending order")
    #     else:
    #         searchNamessorted = sorted(searchNameslist)
    #         self.assertListEqual(searchNameslist, searchNamessorted, "List is not sorted in Ascending order")
    #     sleep(10)
    #     self.ast.get_asset_table_column_header("Asset").click()
    #     sleep(10)
    #     searchNames = self.ast.get_asset_table("Asset")
    #     searchNameslist=[]
    #     for name in searchNames:
    #         searchNameslist.append(str(name.text))
    #     if self.ast.get_asset_table_column_header("Asset").get_attribute("class") == "sorting_desc":
    #         searchNamessorted = sorted(searchNameslist,reverse=True)
    #         self.assertListEqual(searchNameslist, searchNamessorted, "List is not sorted in Descending order")
    #     else:
    #         searchNamessorted = sorted(searchNameslist)
    #         self.assertListEqual(searchNameslist, searchNamessorted, "List is not sorted in Ascending order")

    @attr(priority="high")
    #@SkipTest
    def test_ast_26_1_To_Test_Different_filters_on_Assessment_page(self):
        self.ast.get_ast_statusfilter_dropdown.click()
        try:
            self.ast.get_statusfilter_InProgress_link.click()
        except:
            self.ast.get_ast_statusfilter_dropdown.click()
            self.skipTest("In progress option not in the Type filter dropdown available")
        sleep(5)
        for item in self.ast.get_assessment_table("Status"):
            self.assertEqual(item.text, "In Progress")
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
        sleep(5)
        for item in self.ast.get_assessment_table("Status"):
            self.assertEqual(item.text, "Submitted")
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
        sleep(5)
        for item in self.ast.get_assessment_table("Status"):
            self.assertEqual(item.text, "Not Started")
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
            self.assertEqual(item.text, "Haystax School Safety")
        self.ast.get_resetfilter_button.click()

    #should select the first available link on the dropdown
    @attr(priority="high")
    @SkipTest
    def test_ast_28_To_Test_Different_filters_on_Assessment_page(self):
        self.ast.get_ast_statusfilter_dropdown.click()
        self.ast.get_statusfilter_NotStarted_link.click()
        try:
            self.assertEqual(self.ast.get_ast_statusfilter_dropdown.text, "Not Started", "Not Started ooption not available in filter options")
        except:
            self.ast.get_resetfilter_button.click()
        self.ast.get_ast_typefilter_dropdown.click()
        self.ast.get_typefilter_haystax_link.click()
        try:
            self.assertEqual(self.ast.get_ast_typefilter_dropdown.text, "Haystax School Safety", "Haystax School Safety"
                                                                        " option not available in type filter options")
        except:
            self.ast.get_resetfilter_button.click()
        self.ast.get_resetfilter_button.click()
        self.assertEqual(self.ast.get_ast_statusfilter_dropdown.text, "Status", "Status filter is not reset")
        self.assertEqual(self.ast.get_ast_typefilter_dropdown.text, "Type", "Type filter is not reset")

    @attr(priority="high")
    #@SkipTest
    def test_ast_29_to_32_To_Verify_The_Search_(self):
        flag = 0
        cwd = os.getcwd()
        os.chdir('..')
        searchasset_filepath = os.path.join(os.getcwd(), "data", "json_SearchAssessments.json")
        os.chdir(cwd)
        with open(searchasset_filepath) as data_file:
            data_SearchAsset_text = json.load(data_file)
            for each in data_SearchAsset_text:
                searchText = each["Search_name"]
                self.ast.search_assessment_textbox(searchText)
                sleep(5)
                if len(self.ast.get_assessment_table("Asset")) <= 0:
                    self.assertEqual("No matching records found",
                                         self.ast.get_assessmentlist_no_matching_records_found.text, "No records to find assessments.")
                    flag = 1
                else:
                    for searchName in self.ast.get_assessment_table("Asset"):
                        if searchText in searchName.text:
                            flag = 1
                    if flag == 0:
                        for searchName in self.ast.get_assessment_table("Assessment"):
                            if searchText in searchName.text:
                                flag = 1
                    if flag == 0:
                        for searchName in self.ast.get_assessment_table("Created"):
                            if searchText in searchName.text:
                                flag = 1
                    if flag == 0:
                        for searchName in self.ast.get_assessment_table("Assigned to"):
                            if searchText in searchName.text:
                                flag = 1
                    if flag == 0:
                        for searchName in self.ast.get_assessment_table("Complete"):
                            if searchText in searchName.text:
                                flag = 1
                    if flag == 0:
                        for searchName in self.ast.get_assessment_table("Status"):
                            if searchText in searchName.text:
                                flag = 1
                    if flag == 0:
                        self.assertTrue(False, "The search result doesnt contain the text that is searched. "
                                               "Searched string is :" + searchText)
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
        sleep(5)#Mandatory sleep for the list to refresh
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
            sleep(5)#mandatory for the list to refresh
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
            sleep(5)#mandatory for the list to refresh
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
            sleep(10)
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
            sleep(10)
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
        sleep(8)
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
            sleep(10)
            assignedto = self.ast.get_assessment_table("Assigned to")
            self.assertNotEqual(assignedto[0].text, emailidtoenter, "Assigned Email id saved on cancel operation")
        else:
            self.skipTest("No assessment listed")

