import unittest

from basetestcase import BaseTestCase

class LoginPageTest(BaseTestCase):
    #def test_Home_Landing_Logo(self):
    #    homepage = HomePage(self.driver)

    def test_Login(self):
        homepage = HomePage(self.driver)
        homepage.loginlink.click()
        self.assertEqual("https://constellation-dev.haystax.com/#/login", self.driver.current_url)
        loginpage = LoginPage(self.driver)
        loginpage.email.send_keys()


if __name__ =='__main__':
    unittest.main(verbosity=2)
