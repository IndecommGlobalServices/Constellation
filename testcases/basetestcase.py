import unittest
import os
from datetime import datetime
from time import sleep
from selenium import webdriver
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.basepage import BasePage
from pages.IconListPage import IconListPage
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener

from pyvirtualdisplay import Display
import json

cwd = os.getcwd()
os.chdir('..')
SCREEN_DUMP_LOCATION = os.path.join(os.getcwd(), "Screenshots")
os.chdir(cwd)



class BaseTestCase(unittest.TestCase):
    @classmethod
    
    def setUpClass(self):
        #display = Display(visible=0, size=(1024,768))
        #display.start()
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

        #iconlistpage = IconListPage(cls.driver)
        #iconlistpage.click_asset_icon()




    @classmethod
    def tearDownClass(self):
        '''
        if self._test_has_failed():
            if not os.path.exists(SCREEN_DUMP_LOCATION):
                os.makedirs(SCREEN_DUMP_LOCATION)
            for ix, handle in enumerate(self.driver.window_handles):
                self._windowid=ix
                self.driver.switch_to_window(handle)
                self.take_screenshot()
                self.dump_html()

        #st = datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')

        '''
        st = datetime.now().isoformat().replace(':', '.')[:19]
        os.chdir('..')
        path = os.path.join(os.getcwd(), "Screenshots")
        file_name = "Screenshot " + st + ".png"
        SaveLocation = os.path.join(path, file_name)
        self.driver.save_screenshot(SaveLocation)


        # close the browser
        self.driver.quit()
        #super(BaseTestCase).tearDown()


    def _test_has_failed(self):
        for method, error in self._outcome.errors:
            if error:
                return  True
            return False

    def take_screenshot(self):
        filename = self._get_filename() + '.png'
        print('screenshotting to', filename)
        self.driver.get_screenshot_as_file(filename)

    def dump_html(self):
        filename = self._get_filename() + '.html'
        print('dumping page HTML to', filename)
        with open(filename, 'w') as f:
            f.write(self.driver.page_source)

    def _get_filename(self):
        timestamp = datetime.now().isoformat().replace(':', '.')[:19]
        return '{folder}/{classname.{method}-window{window}-{timestamp}'.format(
            folder=SCREEN_DUMP_LOCATION,
            classname=self.__class__.__name__,
            method=self._testMethodName,
            windowid=self._windowid,
            timestamp=timestamp
        )

