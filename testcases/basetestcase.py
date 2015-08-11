import unittest
import os
from datetime import datetime
from time import sleep
from selenium import webdriver
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from ddt import ddt, data, unpack
import json


SCREEN_DUMP_LOCATION = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'screendumps')
L1 = os.path.abspath('data/json_login.json')

#@ddt
class BaseTestCase(unittest.TestCase):
    @classmethod
    #@data(loginData.get_data("data/loginData1.csv"))
    #@unpack
    def setUpClass(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("https://constellation-qa.haystax.com/#/")

        homepage = HomePage(self.driver)
        homepage.loginlink.click()
        #self.assertEqual("https://constellation-dev.haystax.com/#/login", self.driver.current_url)
        loginpage = LoginPage(self.driver)

        print "Getting Login data from Json"
        with open(L1) as data_file:
            data_text = json.load(data_file)

            for each in data_text:
                usernameText = each["username"]
                passwordText = each["password"]
                #loginpage.email.send_keys("Deepa.Sivadas@indecomm.net")
                loginpage.email.send_keys(usernameText)
                #loginpage.password.send_keys("myhaystax")
                loginpage.password.send_keys(passwordText)
                #loginpage.password.send_keys(pwd)
                loginpage.login.click()
                #self.assertEqual("https://constellation-dev.haystax.com/apps/#", self.driver.current_url)
                sleep(10)
                # click on Assets
                lnkAssets_field = self.driver.find_element_by_id("app_assets")
                lnkAssets_field.click()
                sleep(10)

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
        '''
        #st = datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
        st = datetime.now().isoformat().replace(':', '.')[:19]
        file_name = "Screenshot " + st + ".png"
        self.driver.save_screenshot(file_name)

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

