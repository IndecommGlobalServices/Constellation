import ConfigParser

__author__ = 'Deepa.Sivadas'
from selenium.webdriver.common.keys import Keys
from pages.assessmentpage import AssessmentPage
from testcases.basetestcase import BaseTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from time import sleep
from datetime import date, timedelta, datetime
import json, os
from lib.pagination import Pagination
from nose.tools import assert_equals


class AssessmenttPageTest(BaseTestCase):
    filepath = "data" + os.sep + "json_SearchAssessments.json"
    cwd = os.getcwd()
    os.chdir('..')
    searchasset_filepath = os.path.join(os.getcwd(), filepath)
    os.chdir(cwd)

    @classmethod
    def setUpClass(cls):
        super(AssessmenttPageTest, cls).setUpClass()
        cls.AssessmentSections = 'AssessmentSections'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))
        cls.ast = AssessmentPage(cls.driver)
        cls.ast.logintoapp()
        cls.pagination = Pagination(cls.driver)
        try:
            cls.ast.get_asset_avilability(cls.config.get(cls.AssessmentSections, 'MAIN_MAINSCHOOL'))
        except Exception, err:
            print err.message

    def setUp(self):
        self.errors_and_failures = self.tally()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()


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
                break
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
        # self.assertEqual(creationdate, str(date.today()), "The newly created assessment creation date is not showing todays date")

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
                sleep(2)

    @attr(priority="high")
    @SkipTest
    def test_ast_34_To_Verify_Delete_Assessment(self):
        countbeforedeletion = self.ast.get_total_row_count()
        self.ast.select_multiple_checkboxes(1)
        self.ast.get_action_dropdown.click()
        self.ast.get_action_delete_button.click()
        sleep(2)
        self.ast.get_delete_assessment_delete_button.click()
        sleep(10)#Mandatory sleep for the list to refresh
        countafterdeletion = self.ast.get_total_row_count()
        self.assertGreater(countbeforedeletion, countafterdeletion, "Couldn't delete asset")

    @attr(priority="high")
    @SkipTest
    def test_ast_35_To_Verify_Delete_MultipleAssessment(self):
        countbeforedeletion = self.ast.get_total_row_count()
        if countbeforedeletion >= 1:
            sleep(5)
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
            sleep(5)
            self.ast.select_multiple_checkboxes(2)
            self.ast.get_action_dropdown.click()
            self.ast.get_action_delete_button.click()
            self.ast.get_delete_assessment_cancel_button.click()
            sleep(5)#mandatory for the list to refresh
            self.ast.deselect_checkboxes()
            countafterdeletion = self.ast.get_total_row_count()
            self.assertEqual(countbeforedeletion, countafterdeletion, "Assessment deleted even after cancel is pressed")
        else:
            self.skipTest("No Assessments listed")

    @attr(priority="high")
    #@SkipTest
    def test_ast_37_To_Verify_Assign_Assessment(self):
        emailid = "Email@domain"
        countbeforedeletion = self.ast.get_total_row_count()
        if countbeforedeletion >= 1:
            sleep(5)
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
            sleep(5)
            self.ast.select_multiple_checkboxes(noofassessments)
            self.ast.get_action_dropdown.click()
            self.ast.get_action_assign_button.click()
            self.ast.get_ast_assignto_textbox.send_keys(emailid)
            self.ast.get_ast_assignto_assign_button.click()
            sleep(12)
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
            self.ast.deselect_checkboxes()
        else:
            self.skipTest("No assessment listed")

    @attr(priority="high")
    #@SkipTest
    def test_ast_40_To_Verify_Assign_Assessment_cancel(self):
        emailid = ['Email1@domain', 'Email2@domain']
        countbeforedeletion = self.ast.get_total_row_count()
        if countbeforedeletion >= 1:
            sleep(10)
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

    @attr(priority="high")
    #@SkipTest
    def test_ast_111_to_test_pagination_next_button(self):
        """
        Test : test_ast_111
        Description :To Test pagination next button.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        if self.pagination.pagination_total_pages() >=1 :
            self.pagination.pagination_previous()
            sleep(2)
            current_page_num = self.pagination.pagination_active_page()
            self.pagination.pagination_next()
            sleep(2)
            next_page_num = self.pagination.pagination_active_page()
            self.assertEqual(next_page_num, current_page_num + 1,"The next button click is not working.")
        else:
             self.skipTest("Pagination has only one page.")

    @attr(priority="high")
    #@SkipTest
    def test_ast_112_to_test_pagination_next_button_disabled(self):
        """
        Test : test_ast_112
        Description :To Test pagination next button. Last Page is active.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        if self.pagination.pagination_total_pages() >=1 :
            self.pagination.pagination_drop_down_click(-1)
            sleep(2)
            current_page_num = self.pagination.pagination_active_page()
            total_pages = self.pagination.pagination_total_pages()
            flag = 1
            while flag:
                if int(current_page_num) == int(total_pages):
                    flag = 0
                else:
                    self.pagination.pagination_next()
                    current_page_num = self.pagination.pagination_active_page()
            next_page_num = self.pagination.pagination_active_page()
            self.assertEqual(current_page_num, next_page_num, "Next Arrow button is not disabled.")
        else:
            self.skipTest("Pagination has only one page.")

    @attr(priority="high")
    #@SkipTest
    def test_ast_113_to_test_pagination_previous_button(self):
        """
        Test : test_ast_113
        Description :To Test pagination previous button.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        if self.pagination.pagination_total_pages() >=1 :
            self.pagination.pagination_next()
            current_page_num = self.pagination.pagination_active_page()
            self.pagination.pagination_previous()
            sleep(2)
            previous_page_num = self.pagination.pagination_active_page()
            self.assertEqual(previous_page_num, current_page_num - 1, "The Previous button click is not working.")
        else:
            self.skipTest("Pagination has only one page.")

    @attr(priority="high")
    #@SkipTest
    def test_ast_114_to_test_pagination_previous_button_disabled(self):
        """
        Test : test_ast_114
        Description :To Test pagination previous button. First page is active.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        if self.pagination.pagination_total_pages() >=1 :
            self.pagination.pagination_drop_down_click(0)
            sleep(2)
            current_page_num = self.pagination.pagination_active_page()
            flag = 1
            while flag:
                if int(current_page_num) == int(1):
                    flag = 0
                else:
                    self.pagination.pagination_previous()
                    current_page_num = self.pagination.pagination_active_page()
            previous_page_num = self.pagination.pagination_active_page()
            self.assertEqual(current_page_num, previous_page_num, "Previous Arrow button is not disabled.")
        else:
            self.skipTest("Pagination has only one page.")

    @attr(priority="high")
    #@SkipTest
    def test_ast_115_to_test_pagination_page_group_select(self):
        """
        Test : test_ast_115
        Description :To verify that page group is selected from drop down menu
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        self.pagination.get_pg_drop_down_arrow.click()
        sleep(2)
        list_of_page_drop_down = self.pagination.get_pg_list_of_page_groups
        sleep(2)
        self.pagination.get_pg_drop_down_arrow.click()
        sleep(2)
        if len(list_of_page_drop_down) >= 1:
            self.pagination.pagination_drop_down_click(-1)
            self.pagination.get_pg_drop_down_arrow.click()
            last_page = (list_of_page_drop_down[-1].text.encode('utf-8')).split("-")[1]
            last_page_first = (list_of_page_drop_down[-1].text.encode('utf-8')).split("-")[0]
            self.pagination.get_pg_drop_down_arrow.click()
            if int(last_page) >= 5:
                first_page = int(last_page)-4
            else:
                first_page = last_page_first
            start_value, end_value = self.pagination.pagination_start_end_node_value()
            actual_group = [str(start_value), str(end_value)]
            expected_group = [str(first_page), str(last_page)]
            self.assertListEqual(actual_group, expected_group, "Selected Group value is not matching with Actual.")
        else:
            self.skipTest("There is only one page available.")

    @attr(priority="high")
    #@SkipTest
    def test_ast_116_to_test_direct_click_first_page(self):
        """
        Test : test_ast_116
        Description :To verify that first page is selected directly and previous button is disabled.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        page_count = self.pagination.pagination_total_pages()
        list_of_nodes = self.pagination.get_pg_list_of_nodes
        if str(page_count) == str(1):
            previous_node_value = list_of_nodes[0].get_attribute("class")
            next_node_value = list_of_nodes[-1].get_attribute("class")
            if (previous_node_value == "previous disabled") and (next_node_value == "next disabled"):
                self.assertTrue(True, "There is only one page and next/previous button is enabled.")
            else:
                self.assertFalse(True, "There is only one page and next/previous button is enabled.")

        elif str(page_count) > str(1):
            self.pagination.pagination_drop_down_click(0)
            sleep(2)
            list_of_nodes = self.pagination.get_pg_list_of_nodes
            sleep(2)
            list_of_nodes[1].click()
            sleep(2)
            if list_of_nodes[0].get_attribute("class") == "previous disabled":
                self.assertTrue(True, "Current Page number is One but previous button is enabled.")
            else:
                self.assertFalse(True, "Current Page number is One but previous button is enabled.")

    @attr(priority="high")
    #@SkipTest
    def test_ast_117_to_test_direct_click_last_page(self):
        """
        Test : test_ast_117
        Description :To verify that last page is selected directly and next button is disabled.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        page_count = self.pagination.pagination_total_pages()
        list_of_nodes = self.pagination.get_pg_list_of_nodes
        if str(page_count) == str(1):
            previous_node_value = list_of_nodes[0].get_attribute("class")
            next_node_value = list_of_nodes[-1].get_attribute("class")
            if (previous_node_value == "previous disabled") and (next_node_value == "next disabled"):
                self.assertTrue(True, "There is only one page and next/previous button is enabled.")
            else:
                self.assertFalse(True, "There is only one page and next/previous button is enabled.")
        elif str(page_count) > str(1):
            self.pagination.pagination_drop_down_click(-1)
            sleep(2)
            list_of_nodes = self.pagination.get_pg_list_of_nodes
            list_of_nodes[-3].click()
            sleep(2)
            if list_of_nodes[-1].get_attribute("class") == "next disabled":
                self.assertTrue(True, "Displayed Page is last page but next button is enabled.")
            else:
                self.assertFalse(True, "Displayed Page is last page but next button is enabled.")

    @attr(priority="high")
    #@SkipTest
    def test_ast_118_to_test_search_asset_pagination(self):
        """
        Test : test_ast_118
        Description :To verify that if searched asset is not available than pagination should be disabled.
        Revision:
        Author : Bijesh
        :return: None
        """
        self.basepage.reset_and_search_clear()
        self.ast.get_search_assessment_textbox.send_keys("zaqwerty")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element
              ((By.XPATH, self.ast._ast_assessmentlist_No_Matching_Records_Found_locator), "No matching records found"))
        if self.ast.get_assessmentlist_no_matching_records_found.is_displayed():
            list_of_nodes = self.pagination.get_pg_list_of_nodes
            node_length = len(list_of_nodes)
            previous_node_text = list_of_nodes[0].get_attribute("class")
            next_node_text = list_of_nodes[-1].get_attribute("class")
            sleep(20)
            if(previous_node_text == "previous disabled") and (next_node_text == "next disabled") and (node_length==3):
                self.assertTrue(True, "No Pages available but still next and previous button is enabled.")
            else:
                self.assertFalse(True, "No Pages available but still next and previous button is enabled.")
        self.ast.get_search_assessment_textbox.clear()
        self.basepage.reset_and_search_clear()