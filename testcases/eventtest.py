import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from pages.eventspage import EventsPage
from testcases.basetestcase import BaseTestCase
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from time import sleep
import json, os, re, inspect
from selenium.webdriver.common.action_chains import ActionChains
import ConfigParser
from lib.pagination import Pagination

class EventpageTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(EventpageTest, cls).setUpClass()
        cls.eventpage = EventsPage(cls.driver)
        cls.pagination = Pagination(cls.driver)
        cls.eventpage.open_event_app()
        cls.section = 'EventsMessages'
        cls.config = ConfigParser.ConfigParser()
        cls.config.readfp(open('baseconfig.cfg'))

    def setUp(self):
        self.errors_and_failures = self.tally()
        WebDriverWait(self.driver, 50). until(EC.presence_of_element_located(
            (By.XPATH, self.eventpage._event_select_action_delete_select_xpath_locator)))

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        self.eventpage.return_to_apps_main_page()

    @attr(priority="high")
    #@SkipTest
    def test_EV_001(self):
        """
        Test : test_AS_01
        Description : To verify delete functionality when no events are available. Delete button should be disabled.
        Revision:
        Author : Kiran
        :return: None
        """
        self.eventpage.get_event_select_action_drop_down.click()
        if len(self.eventpage.get_event_name_list)<= 0:
            self.assertFalse(self.eventpage.get_event_link_delete_text.is_enabled(),
                             self.config.get(self.section, 'MESSAGE_WHEN_NO_EVENTS_AVAILABLE'))
        else:
            self.skipTest(self.config.get(self.section, 'MESSAGE_TEST_CAN_NOT_BE_VALIDATED'))
