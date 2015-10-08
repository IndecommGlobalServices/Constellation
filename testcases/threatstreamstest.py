__author__ = 'Deepa.Sivadas'
from testcases.basetestcase import BaseTestCase
from pages.threatstreamspage import ThreatStreamPage
from nose.plugins.attrib import attr
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class ThreatStreamTest(BaseTestCase):

    @attr(priority="high")
    #@SkipTest
    @attr(status='smoke')
    def test_threat_steams(self):
        tstream = ThreatStreamPage(self.driver)
        # WebDriverWait(self.driver,20).until(expected_conditions.presence_of_element_located(By.XPATH, tstream._ts_app_name_text))
        self.assertEqual(tstream.get_ts_app_name.text, "Threat Streams")

