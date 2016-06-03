__author__ = 'Deepa.Sivadas'

from nose.plugins.attrib import attr
from time import sleep
from nose.plugins.skip import SkipTest
from pages.assetpage import AssetPage
from pages.assessmentpage import AssessmentPage
from pages.basepage import BasePage
from pages.loginpage import LoginPage
from pages.IconListPage import IconListPage
from pages.mappage import MapPage
from pages.threatstreamspage import ThreatStreamPage
from pages.incidentspage import IncidentsPage
from pages.timelinepage import TimelinePage
from pages.eventspage import EventsPage
from pages.fieldinterviewspage import FieldInterviewsPage
from testcases.basetestcase import BaseTestCase

class SmokeTest(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        super(SmokeTest, cls).setUpClass()
        loginpage = LoginPage(cls.driver)
        loginpage.loginDashboard()
        # self.username = loginpage.usernameText
        cls.appicon = IconListPage(cls.driver)

    def setUp(self):
        self.errors_and_failures = self.tally()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        basepage = BasePage(self.driver)
        basepage.accessURL()

    @attr(priority="high")
    #@SkipTest
    def test_01_asset_smoke(self):
        self.assetpage = AssetPage(self.driver)
        self.appicon.click_asset_icon()
        self.assertTrue(self.assetpage.get_asset_create_asset, "Create assest button not available")
        self.assertTrue(self.assetpage.get_filter_drop_down.is_displayed(), "Type filter dropdown not available")
        self.assertTrue(self.assetpage.get_asset_select_action_drop_down.is_displayed(), "Select action dropdown not available")
        self.assertTrue(self.assetpage.get_asset_reset_button.is_displayed(), "Reset button not available")
        self.assetpage.get_asset_reset_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_02_assessment_smoke(self):
        self.ast = AssessmentPage(self.driver)
        self.appicon.click_assessments_icon()
        self.assertTrue(self.ast.get_main_create_assessment_button, "Create assessment button not available")
        self.assertTrue(self.ast.get_ast_typefilter_dropdown.is_displayed(), "Type filter dropdown not available")
        self.assertTrue(self.ast.get_ast_statusfilter_dropdown.is_displayed(), "Status filter dropdown not available")
        self.assertTrue(self.ast.get_resetfilter_button.is_displayed(), "Reset button not available")
        self.ast.get_resetfilter_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_03_threatstream_smoke(self):
        self.tstream = ThreatStreamPage(self.driver)
        self.appicon.click_threatstream()
        sleep(20)
        self.assertTrue(self.tstream.get_ts_threat_dropdown_filter.is_displayed(), "Dropdown filter not available")

    @attr(priority="high")
    #@SkipTest
    def test_04_incident_smoke(self):
        self.incident = IncidentsPage(self.driver)
        self.appicon.click_incidents_icon()
        self.assertTrue(self.incident.get_main_create_incident_button, "Create incidents button not available")
        self.assertTrue(self.incident.get_Type_dropdown.is_displayed(), "Type filter dropdown not available")
        self.assertTrue(self.incident.get_status_dropdown.is_displayed(), "Status filter dropdown not available")
        self.incident.get_settings_button.click()
        self.incident.get_close_button.click()

    @attr(priority="high")
    #@SkipTest
    def test_05_fieldinterviews_smoke(self):
        self.fieldinterviews = FieldInterviewsPage(self.driver)
        self.appicon.click_fieldinterview_icon()
        self.assertTrue(self.fieldinterviews.get_field_interviews_app_name_label.is_displayed(), "Field Interviews")
        self.assertTrue(self.fieldinterviews.get_contact_type_drop_down.is_displayed(),
                        "Type filter dropdown not available")

    @attr(priority="high")
    #@SkipTest
    def test_06_timeline_smoke(self):
        self.timeline = TimelinePage(self.driver)
        self.appicon.click_timeline_icon()
        self.assertTrue(self.timeline.get_time_line_app_name_label.is_displayed(),"Timeline app name is not available.")

    @attr(priority="high")
    #@SkipTest
    def test_07_events_smoke(self):
        self.events = EventsPage(self.driver)
        self.appicon.click_events_icon()
        self.assertTrue(self.events.get_Type_dropdown.is_displayed(), "Type filter dropdown not available")
        self.assertTrue(self.events.get_main_create_incident_button, "Create incidents button not available")

    @attr(priority="high")
    #@SkipTest
    def test_08_map_smoke(self):
        self.mappage = MapPage(self.driver)
        self.appicon.click_map_icon()
        self.assertTrue(self.mappage.get_map_water_fall_scrollable.is_displayed(), "Map is not loaded fully")