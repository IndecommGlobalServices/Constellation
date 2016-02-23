from selenium.webdriver.common.keys import Keys
from pages.loginpage import LoginPage
from time import sleep
from pages.IconListPage import IconListPage
from pages.assetpage import AssetPage
from random import randint


from testcases.basetestcase import BaseTestCase

class LoginPageTest(BaseTestCase):

    @classmethod
    def setUpClass(self):
        super(LoginPageTest, self).setUpClass()
        self.loginpage = LoginPage(self.driver)

    def setUp(self):
        self.errors_and_failures = self.tally()

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            self.take_screenshot()
        #self.loginpage.return_to_apps_main_page()

    def test_G_01_04_login_valid(self):
        self.loginpage = LoginPage(self.driver)
        self.iconpage = IconListPage(self.driver)
        self.loginpage.loginDashboard()
        sleep(5)
        self.assertEqual("https://constellation-qa.haystax.com/apps/#/", self.driver.current_url)
        self.assertTrue(self.iconpage.get_top_logo.is_displayed, "Constellation Logo not displayed.")
        # print self.iconpage.get_loggedin_username.text
        self.iconpage.get_loggedin_username.click()
        self.iconpage.get_logout.click()
        sleep(5)
        self.assertTrue(self.loginpage.get_big_logo.is_displayed, "Constellation big logo is not displayed.")

    def test_G_02_01_login_invalid_email(self):
        self.loginpage.email.clear()
        self.loginpage.email.send_keys("deepa.sivadas1@indecomm.com")
        self.loginpage.password.clear()
        self.loginpage.password.send_keys("myhaystax")
        self.loginpage.login.click()
        sleep(10)
        self.assertEqual("Login attempt failed because the username and/or password are incorrect.", self.loginpage.loginerror.text )

    def test_G_02_02_login_invalid_password(self):
        self.loginpage.email.clear()
        self.loginpage.email.send_keys("deepa.sivadas@indecomm.com")
        self.loginpage.password.clear()
        self.loginpage.password.send_keys("myhaystax2")
        self.loginpage.login.click()
        sleep(10)
        self.assertEqual("Login attempt failed because the username and/or password are incorrect.", self.loginpage.loginerror.text )

    def test_G_03_login_blank_email_and_password(self):
        self.loginpage.email.clear()
        self.loginpage.password.clear()
        sleep(2)
        self.assertTrue(not (self.loginpage.login.is_enabled()), "Login button is enabled.")

    def test_G_05_register_new_user_successful(self):
        self.loginpage.get_login_main_register.click()
        self.loginpage.clearallfields()
        email1 = "kk" + str(randint(0000,9999)) + "@yahoo.com"
        self.loginpage.get_register_username_email.send_keys(email1)
        self.loginpage.get_register_first_name.send_keys("kiran")
        self.loginpage.get_register_last_name.send_keys("kumar")
        self.loginpage.get_register_password_1.send_keys("welcome123@@")
        self.loginpage.get_register_password_2.send_keys("welcome123@@")
        self.loginpage.get_register_13_year.click()
        self.loginpage.get_register_agree_service_terms.click()
        self.loginpage.get_register_register.click()
        sleep(5)
        self.assertEqual("Registration successful. Check your email for a verification message before trying to log in.", self.loginpage.loginerror.text)


    def test_G_06_07_register_invalid_email(self):
        self.driver.refresh()
        self.loginpage.get_login_main_register.click()
        self.loginpage.clearallfields()
        self.loginpage.get_register_username_email.send_keys("kiran@")
        self.loginpage.get_register_password_1.send_keys("welcome123@@")
        self.loginpage.get_register_password_2.send_keys("welcome123@@")
        self.loginpage.get_register_13_year.click()
        self.loginpage.get_register_agree_service_terms.click()
        self.loginpage.get_register_register.click()
        sleep(10)
        self.assertEqual("Account email address is in an invalid format.", self.loginpage.get_register_error_status_message.text)

    def test_G_08_register_invalid_firstname(self):
        self.driver.refresh()
        self.loginpage.get_login_main_register.click()
        self.loginpage.clearallfields()
        self.loginpage.get_register_username_email.send_keys("kir123@yahoo.com")
        self.loginpage.get_register_password_1.send_keys("welcome123@@")
        self.loginpage.get_register_password_2.send_keys("welcome123@@")
        self.loginpage.get_register_13_year.click()
        self.loginpage.get_register_agree_service_terms.click()
        self.loginpage.get_register_register.click()
        sleep(10)
        self.assertEqual("Account givenName cannot be null, empty, or blank.", self.loginpage.get_register_error_status_message.text)

    def test_G_10_01_register_empty_passwords(self):
        self.driver.refresh()
        self.loginpage.get_login_main_register.click()
        self.loginpage.clearallfields()
        self.loginpage.get_register_13_year.click()
        self.loginpage.get_register_agree_service_terms.click()
        self.loginpage.get_register_register.click()
        sleep(10)
        self.assertEqual("Account password minimum length not satisfied.", self.loginpage.get_register_error_status_message.text)

    def test_G_10_02_register_password_length(self):
        self.driver.refresh()
        self.loginpage.get_login_main_register.click()
        self.loginpage.clearallfields()
        self.loginpage.get_register_password_1.send_keys("wel")
        sleep(10)
        self.assertEqual("Password must be at least 8 characters long.", self.loginpage.get_register_error_password_status_message.text)

    def test_G_12_01_register_uncheckbox_13_year_disable_register_button(self):
        self.driver.refresh()
        self.loginpage.get_login_main_register.click()
        self.loginpage.clearallfields()
        if self.loginpage.get_register_13_year.is_selected():
            self.loginpage.get_register_13_year.click()
        self.loginpage.get_register_agree_service_terms.click()
        sleep(10)
        self.assertTrue(not (self.loginpage.get_register_register.is_enabled()), "Register button is enabled.")

    def test_G_12_02_register_uncheckbox_agree_service_terms_disable_register_button(self):
        self.driver.refresh()
        self.loginpage.get_login_main_register.click()
        self.loginpage.clearallfields()
        self.loginpage.get_register_13_year.click()
        if self.loginpage.get_register_agree_service_terms.is_selected():
            self.loginpage.get_register_agree_service_terms.click()
        sleep(10)
        self.assertTrue(not (self.loginpage.get_register_register.is_enabled()), "Register button is enabled.")

    def test_G_13_register_cancel_button(self):
        self.driver.refresh()
        self.loginpage.get_login_main_register.click()
        self.loginpage.clearallfields()
        self.loginpage.get_register_13_year.click()
        self.loginpage.get_register_agree_service_terms.click()
        self.loginpage.get_register_cancel.click()
        sleep(5)
        self.assertTrue(not (self.loginpage.get_register_cancel.is_displayed()), "Cancel button is displayed.")

    def test_G_14_01_forgot_password_invalid_email(self):
        self.driver.refresh()
        self.loginpage.get_reset_password.click()
        self.loginpage.get_forgot_pwd_username.clear()
        self.loginpage.get_forgot_pwd_username.send_keys("wel@wlssk")
        self.loginpage.get_forgot_pwd_reset.click()
        sleep(5)
        self.assertEqual("email property is an invalid value.", self.loginpage.get_forgot_pwd_error_status_message.text)

    def test_G_14_02_forgot_password_username_empty_disable_reset_button(self):
        self.driver.refresh()
        self.loginpage.get_reset_password.click()
        self.loginpage.get_forgot_pwd_username.clear()
        sleep(5)
        self.assertTrue(not (self.loginpage.get_forgot_pwd_reset.is_enabled()), "Reset button is enabled.")

    def test_G_14_03_forgot_password_email_sent_successful(self):
        self.driver.refresh()
        self.loginpage.get_reset_password.click()
        self.loginpage.get_forgot_pwd_username.clear()
        self.loginpage.get_forgot_pwd_username.send_keys("kiran.k@indecomm.net")
        self.loginpage.get_forgot_pwd_reset.click()
        sleep(5)
        self.assertEqual("Reset request successful. Check your email for instructions on how to complete the process.",
                         self.loginpage.loginerror.text)

    def test_G_16_Main_Page_valid(self):
        self.loginpage = LoginPage(self.driver)
        self.iconpage = IconListPage(self.driver)
        self.loginpage.loginDashboard()
        sleep(5)
        self.assertEqual("https://constellation-qa.haystax.com/apps/#/", self.driver.current_url)
        self.assertTrue(self.iconpage.get_top_logo.is_displayed, "Constellation Logo not displayed.")
        # print "Constellation Logo is displayed."
        self.assertTrue(self.iconpage.get_loggedin_username.is_displayed, "Logged in user name not displayed.")
        # print "Logged in user name is displayed as " + self.iconpage.get_loggedin_username.text
        self.iconpage.get_loggedin_username.click()
        sleep(5)
        self.assertTrue(self.iconpage.get_profile.is_displayed, "Profile not displayed.")
        # print "Profile link is displayed."
        self.assertTrue(self.iconpage.get_logout.is_displayed, "Log out not displayed.")
        # print "Logout link is displayed."
        self.assertTrue(self.iconpage.get_my_organisation.is_displayed, "My Organisation not displayed.")
        # print "My Organisation link is displayed."
        self.assertTrue(self.iconpage.get_invite_members.is_displayed, "Invite Members not displayed.")
        # print "Invite Members link is displayed."
        self.assertTrue(self.iconpage.get_manage_access.is_displayed, "Manage Access not displayed.")
        # print "Manage Access link is displayed."
        self.assertTrue(self.iconpage.get_pending_invitation.is_displayed, "Pending Invitation not displayed.")
        # print "Pending Invitation link is displayed."
        self.assertTrue(self.iconpage.get_status.is_displayed, "Status not displayed.")
        # print "Status link is displayed."
        self.assertTrue(self.iconpage.get_help.is_displayed, "Help not displayed.")
        # print "Help link is displayed."
        self.assertTrue(self.iconpage.get_feedback.is_displayed, "Feedback icon not displayed.")
        # print "Feedback icon is displayed."
        self.assertTrue(self.iconpage.get_app_asset_icon.is_displayed, "Asset icon not displayed.")
        # print "Asset icon is displayed."
        self.assertTrue(self.iconpage.get_app_assessments_icon.is_displayed, "Assessments icon not displayed.")
        # print "Assessments icon is displayed."
        self.assertTrue(self.iconpage.get_app_map_icon.is_displayed, "Map icon not displayed.")
        # print "Map icon is displayed."
        self.assertTrue(self.iconpage.get_app_dashboard_icon.is_displayed, "Dashboard icon not displayed.")
        # print "Dashboard icon is displayed."
        self.assertTrue(self.iconpage.get_app_incidents_icon.is_displayed, "Incidents icon not displayed.")
        # print "Incidents icon is displayed."
        self.assertTrue(self.iconpage.get_app_threatstreams_icon.is_displayed, "Threat Streams icon not displayed.")
        # print "Threat Streams icon is displayed."
        self.iconpage.get_logout.click()
        self.assertTrue(self.loginpage.get_big_logo.is_displayed, "Constellation big logo is not displayed.")

    def test_G_17_Global_Naviagation(self):
        self.loginpage = LoginPage(self.driver)
        self.iconpage = IconListPage(self.driver)
        self.loginpage.loginDashboard()
        sleep(5)
        #self.assertEqual("https://constellation-qa.haystax.com/apps/#/", self.driver.current_url)
        self.assertTrue(self.iconpage.get_top_logo.is_displayed, "Constellation Logo not displayed.")
        # print "Constellation Logo is displayed."
        self.assertTrue(self.iconpage.get_loggedin_username.is_displayed, "Logged in user name not displayed.")
        # print "Logged in user name is displayed as " + self.iconpage.get_loggedin_username.text
        self.assertTrue(self.iconpage.get_status.is_displayed, "Status not displayed.")
        # print "Status link is displayed."
        self.iconpage.get_status.click()
        sleep(5)
        self.iconpage.get_top_logo.click()
        sleep(5)
        self.assertTrue(self.iconpage.get_loggedin_username.is_displayed, "Logged in user name not displayed.")
        self.assertTrue(self.iconpage.get_help.is_displayed, "Help not displayed.")
        # print "Help link is displayed."
        sleep(5)
        self.iconpage.get_help.click()
        sleep(5)
        self.iconpage.get_top_logo.click()
        sleep(5)
        self.assertTrue(self.iconpage.get_loggedin_username.is_displayed, "Logged in user name not displayed.")
        sleep(5)
        self.assertTrue(self.iconpage.get_app_asset_icon.is_displayed, "Asset icon not displayed.")
        # print "Asset icon is displayed."
        self.iconpage.get_app_asset_icon.click()
        sleep(5)
        self.iconpage.get_top_logo.click()
        sleep(5)
        self.assertTrue(self.iconpage.get_loggedin_username.is_displayed, "Logged in user name not displayed.")
        sleep(5)
        self.assertTrue(self.iconpage.get_app_assessments_icon.is_displayed, "Assessments icon not displayed.")
        # print "Assessments icon is displayed."
        self.iconpage.get_app_assessments_icon.click()
        sleep(5)
        self.iconpage.get_top_logo.click()
        sleep(5)
        self.assertTrue(self.iconpage.get_loggedin_username.is_displayed, "Logged in user name not displayed.")
        sleep(5)
        self.assertTrue(self.iconpage.get_app_dashboard_icon.is_displayed, "Dashboard icon not displayed.")
        # print "Dashboard icon is displayed."
        if self.iconpage.get_app_dashboard_icon.is_enabled:
            self.iconpage.get_app_dashboard_icon.click()
            self.iconpage.get_top_logo.click()
            self.assertTrue(self.iconpage.get_loggedin_username.is_displayed, "Logged in user name not displayed.")
        else:
            print "Dashboard is disabled."
        self.assertTrue(self.iconpage.get_app_incidents_icon.is_displayed, "Incidents icon not displayed.")
        # print "Incidents icon is displayed."
        if self.iconpage.get_app_incidents_icon.is_enabled:
            self.iconpage.get_app_incidents_icon.click()
            sleep(5)
            self.iconpage.get_top_logo.click()
            self.assertTrue(self.iconpage.get_loggedin_username.is_displayed, "Logged in user name not displayed.")
        else:
            print "Incidents is disabled."
        self.iconpage.get_top_logo.click()
        sleep(5)
        self.assertTrue(self.iconpage.get_app_threatstreams_icon.is_displayed, "Threat Streams icon not displayed.")
        # print "Threat Streams icon is displayed."
        self.iconpage.get_app_threatstreams_icon.click()
        sleep(5)
        self.iconpage.get_top_logo.click()
        sleep(5)
        self.assertTrue(self.iconpage.get_loggedin_username.is_displayed, "Logged in user name not displayed.")
        self.iconpage.get_loggedin_username.click()
        sleep(5)
        self.iconpage.get_logout.click()
        sleep(5)
        self.assertTrue(self.loginpage.get_big_logo.is_displayed, "Constellation big logo is not displayed.")

    def test_G_18_profile_saved_successfully(self):
        self.loginpage = LoginPage(self.driver)
        self.iconpage = IconListPage(self.driver)
        self.loginpage.loginDashboard()
        sleep(5)
        self.assertEqual("https://constellation-qa.haystax.com/apps/#/", self.driver.current_url)
        self.assertTrue(self.iconpage.get_top_logo.is_displayed, "Constellation Logo not displayed.")
        sleep(5)
        self.iconpage.get_loggedin_username.click()
        sleep(5)
        self.iconpage.get_profile.click()
        sleep(5)
        self.assertTrue(self.iconpage.get_profile_email.is_displayed, "Profile email not displayed.")
        firstname = "Deepa 1"
        lastname = " Sivadas"
        name = firstname + lastname
        self.iconpage.get_profile_first_name.clear()
        self.iconpage.get_profile_first_name.send_keys(firstname)
        sleep(2)
        self.iconpage.get_profile_last_name.clear()
        self.iconpage.get_profile_last_name.send_keys(lastname)
        sleep(2)
        self.iconpage.get_profile_save.click()
        sleep(2)
        # print name
        # print self.iconpage.get_loggedin_username.text
        self.assertEqual(self.iconpage.get_loggedin_username.text, name, "profile username doesnot match.")
        sleep(2)
        self.iconpage.get_loggedin_username.click()
        sleep(2)
        self.iconpage.get_logout.click()
        sleep(5)
        self.assertTrue(self.loginpage.get_big_logo.is_displayed, "Constellation big logo is not displayed.")

    def test_G_19_profile_FN_LN_validation(self):
        self.loginpage = LoginPage(self.driver)
        self.iconpage = IconListPage(self.driver)
        self.loginpage.loginDashboard()
        sleep(5)
        self.assertEqual("https://constellation-qa.haystax.com/apps/#/", self.driver.current_url)
        self.assertTrue(self.iconpage.get_top_logo.is_displayed, "Constellation Logo not displayed.")
        sleep(5)
        self.iconpage.get_loggedin_username.click()
        sleep(5)
        self.iconpage.get_profile.click()
        sleep(5)
        self.assertTrue(self.iconpage.get_profile_email.is_displayed, "Profile email not displayed.")
        firstname = ""
        lastname = ""
        self.iconpage.get_profile_first_name.clear()
        self.iconpage.get_profile_first_name.send_keys(firstname)
        sleep(2)
        self.iconpage.get_profile_last_name.clear()
        self.iconpage.get_profile_last_name.send_keys(lastname)
        sleep(2)
        self.assertTrue(not (self.iconpage.get_profile_save.is_enabled()), "SAVE button is enabled.")
        sleep(2)
        self.iconpage.get_profile_cancel.click()
        self.iconpage.get_loggedin_username.click()
        self.iconpage.get_logout.click()
        sleep(5)
        self.assertTrue(self.loginpage.get_big_logo.is_displayed, "Constellation big logo is not displayed.")
