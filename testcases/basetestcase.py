import unittest
import os
from datetime import datetime
from selenium import webdriver
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.basepage import BasePage
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display
from time import sleep

class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.getenv("OS") == None:
            display = Display(visible=0, size=(1280,800))
            display.start()
        #create a new Firefox session

        cls.driver = webdriver.Firefox()
        '''
        chromedriver = "../drivers/windows/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        cls.driver = webdriver.Chrome(chromedriver)
        '''
        cls.driver.implicitly_wait(40)
        cls.driver.set_window_size(1280, 1024)
        cls.driver.maximize_window()

        # navigate to the application home page
        #basepage = BasePage(cls.driver)
        cls.basepage = BasePage(cls.driver)

        cls.basepage.accessURL()

        homepage = HomePage(cls.driver)
        homepage.loginlink.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()# close the browser

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

