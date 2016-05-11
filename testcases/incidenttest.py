import ConfigParser

__author__ = 'Deepa.Sivadas'
from selenium.webdriver.common.keys import Keys
from pages.incidentspage import IncidentsPage
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


class IncidentsPageTest(BaseTestCase):
    filepath = "data" + os.sep + "json_SearchAssessments.json"
    cwd = os.getcwd()
    os.chdir('..')
    searchasset_filepath = os.path.join(os.getcwd(), filepath)
    os.chdir(cwd)

    @classmethod
    def setUpClass(cls):
        super(IncidentsPageTest, cls).setUpClass()
        cls.AssessmentSections = 'AssessmentSections'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))
        cls.incident = IncidentsPage(cls.driver)
        cls.incident.logintoapp()
        cls.pagination = Pagination(cls.driver)


    def setUp(self):
        self.errors_and_failures = self.tally()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()

    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_incident_smoke(self):
        self.assertTrue(self.incident.get_main_create_incident_button, "Create incidents button not available")
        self.assertTrue(self.incident.get_Type_dropdown.is_displayed(), "Type filter dropdown not available")
        self.assertTrue(self.incident.get_status_dropdown.is_displayed(), "Status filter dropdown not available")
        self.incident.get_settings_button.click()
        self.incident.get_close_button.click()

        # self.assertTrue(self.incident.get_resetfilter_button.is_displayed(), "Reset button not available")
        # self.incident.get_resetfilter_button.click()

