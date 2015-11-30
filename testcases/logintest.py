from pages.loginpage import LoginPage
from time import sleep

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

    def test_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.loginDashboard()
        sleep(5)
        self.assertEqual("https://constellation-qa.haystax.com/apps/#/", self.driver.current_url)
