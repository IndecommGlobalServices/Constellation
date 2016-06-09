__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.basepage import BasePage


class IconListPage(BasePageClass, object):
    _app_asset_icon_locator  = "app_assets"
    # _app_asset_icon_locator = "//div[contains(text(),'Assets')]"
    # _app_asset_icon_locator = "//img[@src = '../images/app_icon_assets.png']"
    _app_assessments_icon_locator = "app_assessments"
    # _app_assessments_icon_locator = "//*[@id='app_assessments']/div/img"
    #_app_map_icon_locator = "//img[@src = '../images/app_icon_map.png']"
    # _app_map_icon_locator = "//*[@id='app_map']/div/img"
    _app_map_icon_locator = "//*[@id='app_map']/div/img"   #"app_map"
    _app_dashboard_icon_locator = "app_dashboard"
    # _app_threatstreams_icon_locator = "//*[@id='app_threatstreams']/div/img"
    _app_threatstreams_icon_locator = "app_threatstreams"
    _app_incidents_icon_locator = "app_incidents"
    _app_timeline_icon_locator = "//div[@id = 'app_events']//img[@src='../images/app_icon_timeline.png']"
    _app_events_icon_locator = "//div[@id = 'app_events']//img[@src='../images/app_icon_events2.png']"
    _app_fieldinterview_locator = "app_fieldinterviews"
    _app_scroll_bar_locator = ".//*[@id='apparea']"

    #Loggedin
    _loggedin_top_logo_id_locator = "toplogo"
    _icon_username_xpath = ".//*[@id='navbar-collapse-01']/ul/li[1]/a"


    # Profile and Logout

    _icon_profile_link = ".//*[@id='navbar-collapse-01']/ul/li[1]/ul/li[1]/a"
    _icon_logout_link = "Logout"
    #    _icon_logout_link = ".//*[@id='navbar-collapse-01']/ul/li[1]/ul/li[2]/a"


    # My Organisation
    _icon_my_organisation = ".//*[@id='navbar-collapse-01']/ul/li[2]/a"
    _icon_invite_members = ".//*[@id='navbar-collapse-01']/ul/li[2]/ul/li[1]/a"
    _icon_manage_access = ".//*[@id='navbar-collapse-01']/ul/li[2]/ul/li[2]/a"
    _icon_pending_invitation = ".//*[@id='navbar-collapse-01']/ul/li[2]/ul/li[3]/a"

    # Status
    _icon_status = ".//*[@id='navbar-collapse-01']/ul/li[3]/a"

    #Help
    _icon_help = ".//*[@id='navbar-collapse-01']/ul/li[5]/a"

    # Feedback icon
    _icon_feedback = ".//*[@id='page_applist']/img"

    # Update profile
    _profile_header = ".//*[@id='profile_modal']/div/div/div/h4"
    _profile_email_read_only = ".//*[@id='profile_modal']/div/div/form/div[1]/div[1]/span"
    _profile_first_name_name_locator = "profile_firstname"
    _profile_last_name_name_locator = "profile_lastame"
    _profile_cancel = ".//*[@id='profile_modal']/div/div/form/div[2]/button[1]"
    _profile_save = ".//*[@id='profile_modal']/div/div/form/div[2]/button[2]"

    @property
    def get_app_asset_icon(self):
        return self.basepage.findElementById(self._app_asset_icon_locator)

    @property
    def get_app_assessments_icon(self):
        return self.basepage.findElementById(self._app_assessments_icon_locator)

    @property
    def get_app_map_icon(self):
        return self.basepage.findElementByXpath(self._app_map_icon_locator)

    @property
    def get_app_dashboard_icon(self):
        return self.basepage.findElementById(self._app_dashboard_icon_locator)

    @property
    def get_app_threatstreams_icon(self):
        return self.basepage.findElementById(self._app_threatstreams_icon_locator)

    @property
    def get_app_incidents_icon(self):
        return self.basepage.findElementById(self._app_incidents_icon_locator)

    @property
    def get_app_timeline_icon(self):
        return self.basepage.findElementByXpath(self._app_timeline_icon_locator)

    @property
    def get_app_events_icon(self):
        return self.basepage.findElementByXpath(self._app_events_icon_locator)

    @property
    def get_app_fieldinterview_icon(self):
        return self.basepage.findElementById(self._app_fieldinterview_locator)

    @property
    def get_app_scroll_bar(self):
        return self.driver.find_element_by_xpath(self._app_scroll_bar_locator)



    @property
    def get_loggedin_username(self):
        return self.driver.find_element_by_xpath(self._icon_username_xpath)

    #
    @property
    def get_profile(self):
        return self.driver.find_element_by_xpath(self._icon_profile_link)

    @property
    def get_logout(self):
        return self.driver.find_element_by_link_text(self._icon_logout_link)

    #
    @property
    def get_my_organisation(self):
        return self.driver.find_element_by_xpath(self._icon_my_organisation)

    @property
    def get_invite_members(self):
        return self.driver.find_element_by_xpath(self._icon_invite_members)

    @property
    def get_manage_access(self):
        return self.driver.find_element_by_xpath(self._icon_manage_access)

    #
    @property
    def get_pending_invitation(self):
        return self.driver.find_element_by_xpath(self._icon_pending_invitation)

    @property
    def get_status(self):
        return self.driver.find_element_by_xpath(self._icon_status)

    @property
    def get_help(self):
        return self.driver.find_element_by_xpath(self._icon_help)

    @property
    def get_feedback(self):
        return self.driver.find_element_by_xpath(self._icon_feedback)

    @property
    def get_top_logo(self):
        try:
            return self.basepage.findElementById(self._loggedin_top_logo_id_locator)
        except Exception, err:
            raise type(err)("Top Logo - searched ID - "
                            + self._loggedin_top_logo_id_locator + err.message)

    @property
    def get_loggedin_username(self):
        return self.driver.find_element_by_xpath(self._icon_username_xpath)

    #
    @property
    def get_profile(self):
        return self.driver.find_element_by_xpath(self._icon_profile_link)

    #
    @property
    def get_my_organisation(self):
        return self.driver.find_element_by_xpath(self._icon_my_organisation)

    @property
    def get_invite_members(self):
        return self.driver.find_element_by_xpath(self._icon_invite_members)

    @property
    def get_manage_access(self):
        return self.driver.find_element_by_xpath(self._icon_manage_access)

    #
    @property
    def get_pending_invitation(self):
        return self.driver.find_element_by_xpath(self._icon_pending_invitation)

    @property
    def get_status(self):
        return self.driver.find_element_by_xpath(self._icon_status)

    @property
    def get_help(self):
        return self.driver.find_element_by_xpath(self._icon_help)

    @property
    def get_feedback(self):
        return self.driver.find_element_by_xpath(self._icon_feedback)

    # Update profile

    @property
    def get_profile_header(self):
        return self.driver.find_element_by_xpath(self._profile_header)

    @property
    def get_profile_email(self):
        return self.driver.find_element_by_xpath(self._profile_email_read_only)

    @property
    def get_profile_first_name(self):
        return self.driver.find_element_by_name(self._profile_first_name_name_locator)

    @property
    def get_profile_last_name(self):
        return self.driver.find_element_by_name(self._profile_last_name_name_locator)

    @property
    def get_profile_cancel(self):
        return self.driver.find_element_by_xpath(self._profile_cancel)

    @property
    def get_profile_save(self):
        return self.driver.find_element_by_xpath(self._profile_save)


    def __init__(self, driver):
        super(IconListPage,self).__init__(driver)
        self.basepage = BasePage(self.driver)



    def click_asset_icon(self):
        try:
            self.get_app_asset_icon.click()
        except:
            pass

    def click_assessments_icon(self):
        try:
            self.get_app_assessments_icon.click()
        except:
            pass

    def click_map_icon(self):
        try:
            # WebDriverWait(self.driver, 50).until(expected_conditions.presence_of_element_located(
            #     (By.XPATH, self._app_map_icon_locator)))
            self.get_app_map_icon.click()
        except Exception, err:
            raise type(err)("Map Icon not displayed - " \
                          + err.message)

    def click_dashboard(self):
        try:
            self.get_app_dashboard_icon.click()
        except:
            pass

    def click_incidents_icon(self):
        try:
            self.get_app_incidents_icon.click()
        except:
            pass

    def click_threatstream(self):
        try:
            self.get_app_scroll_bar.send_keys(Keys.ARROW_DOWN)
            self.get_app_scroll_bar.send_keys(Keys.ARROW_DOWN)
            self.get_app_threatstreams_icon.click()
        except:
            pass

    def click_timeline_icon(self):
        try:
            self.get_app_timeline_icon.click()
        except Exception, err:
            raise type(err)("Timeline Icon not displayed - " \
                          + err.message)

    def click_events_icon(self):
        try:
            self.get_app_events_icon.click()
        except Exception, err:
            raise type(err)("Events Icon not displayed - " \
                          + err.message)

    def click_fieldinterview_icon(self):
        try:
            self.get_app_fieldinterview_icon.click()
        except Exception, err:
            raise type(err)("Field interview icon not displayed - " \
                          + err.message)