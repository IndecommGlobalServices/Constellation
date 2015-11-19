import unittest
import os
from datetime import datetime
from selenium import webdriver
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.basepage import BasePage
import ConfigParser
from pyvirtualdisplay import Display
import sys


class BaseTestCase(unittest.TestCase):
    username = ""

    @classmethod
    def setUpClass(self):
        #display = Display(visible=0, size=(1024,768))
        #display.start()
        # create a new Firefox session
        #self.driver = webdriver.Firefox()

        '''
        browser_list = ['Firefox', 'Ie', 'Chrome']

        for browser in browser_list:
            print "Running tests with", browser
            os.environ['BROWSER'] = browser

            if os.environ['BROWSER'] == 'Firefox':
                self.driver = webdriver.Firefox()
            elif os.environ['BROWSER'] == 'Ie':
                self.driver = webdriver.Ie("D:\\Project\\10OCT15\\Constellation\\IEDriverServer.exe")
            elif os.environ['BROWSER'] == 'Chrome':
                self.driver = webdriver.Chrome("D:\\Project\\10OCT15\\Constellation\\chromedriver.exe")
        '''
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open('baseconfig.cfg'))
        self.seleniumDriver = 'Selenium'
        config_browser_type = self.config.get('Selenium', 'browser')
        config_chrome_path = self.config.get('Selenium', 'chromedriver_path')
        config_ie_path = self.config.get('Selenium', 'iedriver_path')

        if config_browser_type.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif config_browser_type.lower() == 'chrome':
            self.driver = webdriver.Chrome(config_chrome_path)
        elif config_browser_type.lower() == 'ie':
            self.driver = webdriver.Ie(config_ie_path)

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
