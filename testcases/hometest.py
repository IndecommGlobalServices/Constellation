import unittest

from pages.homepage import HomePage
from testcases.basetestcase import BaseTestCase


class HomePageTest(BaseTestCase):
    #def test_Home_Landing_Logo(self):
    #    homepage = HomePage(self.driver)

    def test_ClickLogin(cls):
        homepage = HomePage(cls.driver)
        homepage.loginlink.click()
        cls.assertEqual("https://constellation-dev.haystax.com/#/login", self.driver.current_url)

if __name__ =='__main__':
    unittest.main(verbosity=2)