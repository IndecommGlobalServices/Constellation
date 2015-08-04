import unittest
from selenium import webdriver
from homepage import HomePage
from loginpage import LoginPage
from time import sleep

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("https://constellation-dev.haystax.com/#/")

        homepage = HomePage(self.driver)
        homepage.loginlink.click()
        #self.assertEqual("https://constellation-dev.haystax.com/#/login", self.driver.current_url)
        loginpage = LoginPage(self.driver)
        loginpage.email.send_keys("Deepa.Sivadas@indecomm.net")
        loginpage.password.send_keys("myhaystax")
        loginpage.login.click()
        #self.assertEqual("https://constellation-dev.haystax.com/apps/#", self.driver.current_url)
        sleep(10)
        # click on Assets
        lnkAssets_field = self.driver.find_element_by_id("app_assets")
        lnkAssets_field.click()
        sleep(10)

    @classmethod
    def tearDownClass(self):
        # close the browser
        self.driver.quit()



