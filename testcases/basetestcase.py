import unittest
import os
from datetime import datetime
from selenium import webdriver
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.basepage import BasePage
from pyvirtualdisplay import Display

class BaseTestCase(unittest.TestCase):
    username = ""

    @classmethod
    def setUpClass(self):
        display = Display(visible=0, size=(1024,768))
        display.start()
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        basepage = BasePage(self.driver)
        basepage.accessURL()

        homepage = HomePage(self.driver)
        homepage.loginlink.click()

        loginpage = LoginPage(self.driver)
        loginpage.loginDashboard()
        self.username = loginpage.usernameText

    @classmethod
    def tearDownClass(self):
        self.driver.quit()# close the browser


    def take_screenshot(self):
        cwd = os.getcwd()
        st = datetime.now().isoformat().replace(':', '.')[:19]
        os.chdir('..')
        path = os.path.join(os.getcwd(), "Screenshots")
        os.chdir(cwd)
        filename = self._testMethodName + "_Screenshot " + st + ".png"
        if not os.path.exists(path):
            os.makedirs(path)
        SaveLocation = os.path.join(path, filename)
        self.driver.save_screenshot(SaveLocation)

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)
