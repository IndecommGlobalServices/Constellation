import unittest
from selenium import webdriver
from homepage import HomePage
from loginpage import LoginPage
from time import sleep

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get("https://constellation-dev.haystax.com/#/")

        homepage = HomePage(cls.driver)
        homepage.loginlink.click()
        #cls.assertEqual("https://constellation-dev.haystax.com/#/login", cls.driver.current_url)
        loginpage = LoginPage(cls.driver)
        loginpage.email.send_keys("Deepa.Sivadas@indecomm.net")
        loginpage.password.send_keys("myhaystax")
        loginpage.login.click()
        #self.assertEqual("https://constellation-dev.haystax.com/apps/#", self.driver.current_url)
        sleep(10)
        # click on Assets
        lnkAssets_field = cls.driver.find_element_by_id("app_assets")
        lnkAssets_field.click()
        sleep(10)

    @classmethod
    def tearDown(cls):
        # close the browser
        cls.driver.quit()



