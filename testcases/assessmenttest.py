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
            self.assertTrue(assessmentpage.get_search_textbox)
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
        for item in ast.get_xpath(ast.get_table_tr_index("Status")):
            self.assertTrue(item.text, "In Progress")
        ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_26_2_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_statusfilter_dropdown.click()
        ast.get_statusfilter_Submitted_link.click()
        sleep(2)
        for item in ast.get_xpath(ast.get_table_tr_index("Status")):
            self.assertTrue(item.text, "Submitted")
        ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_26_3_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_statusfilter_dropdown.click()
        ast.get_statusfilter_NotStarted_link.click()
        sleep(2)
        for item in ast.get_xpath(ast.get_table_tr_index("Status")):
            self.assertTrue(item.text, "Not Started")
        ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_AST_27_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_typefilter_dropdown.click()
        ast.get_typefilter_haystax_link.click()
        sleep(2)
        for item in ast.get_xpath(ast.get_table_tr_index("Assessment")):
            self.assertTrue(item.text, "Haystax School Safety")
        ast.get_resetfilter_button.click()


    @attr(priority="high")
    #@SkipTest
    def test_AST_28_To_Test_Different_filters_on_Assessment_page(self):
        ast = AssessmentPage(self.driver)
        ast.get_ast_statusfilter_dropdown.click()
        ast.get_statusfilter_NotStarted_link.click()
        self.assertEqual(ast.get_ast_statusfilter_dropdown.text, "Not Started")
        ast.get_ast_typefilter_dropdown.click()
        ast.get_typefilter_haystax_link.click()
        self.assertEqual(ast.get_ast_typefilter_dropdown.text, "Haystax School Safety")
        ast.get_resetfilter_button.click()
        self.assertEqual(ast.get_ast_statusfilter_dropdown.text, "Status")
        self.assertEqual(ast.get_ast_typefilter_dropdown.text, "Type")

if __name__ == '__main__':
    unittest.main(verbosity=2)


