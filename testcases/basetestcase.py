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
            display = Display(visible=0, size=(1280, 800))
            display.start()
        # create a new Firefox session


        # chromedriver = "../drivers/chromedriver"
        # os.environ["webdriver.chrome.driver"]= chromedriver
        # cls.driver = webdriver.Chrome(chromedriver)

        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(40)
        cls.driver.set_window_size(1280, 1024)
        cls.driver.maximize_window()

        # navigate to the application home page
        basepage = BasePage(cls.driver)
        basepage.accessURL()

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


    def pagination_info(self):
        sleep(20)
        pg_list_of_nodes_locator = "//div[contains(@class,'dataTables_paginate paging_numbered')]/div/ul/li"
        list_of_nodes = self.driver.find_elements_by_xpath(pg_list_of_nodes_locator)
        pagination_start = list_of_nodes[1].text
        pagination_end = list_of_nodes[-3].text
        print "Pagination start at page number : ", pagination_start
        print "Pagination end at page number : ", pagination_end
        pg_active_page_locator = "//li[contains(@class, 'active')]//a"
        active_page = self.driver.find_element_by_xpath(pg_active_page_locator)
        print "Current Active page number is :", active_page.text
        pg_drop_down_arrow_locator = "//li[contains(@class, 'dropup')]"
        drop_down_arrow = self.driver.find_element_by_xpath(pg_drop_down_arrow_locator)
        drop_down_arrow.click()
        sleep(1)
        pg_list_of_drop_down_locator = "//li[contains(@class, 'dropup')]//ul/li/a"
        list_of_page_drop_down = self.driver.find_elements_by_xpath(pg_list_of_drop_down_locator)
        print "Total number of pages available in pagination are :",(list_of_page_drop_down[-1].text).split("-")[1]
        for index, item in enumerate(list_of_page_drop_down):
            print index+1, "Page group is : ",item.text
        drop_down_arrow.click()
        sleep(1)

    def pagination_next(self):
        pg_list_of_nodes_locator = "//div[contains(@class,'dataTables_paginate paging_numbered')]/div/ul/li"
        list_of_nodes = self.driver.find_elements_by_xpath(pg_list_of_nodes_locator)
        pg_active_page_locator = "//li[contains(@class, 'active')]//a"
        if list_of_nodes[-1].get_attribute("class") == "next":
            list_of_nodes[-1].click()
            sleep(3)
        elif list_of_nodes[-1].get_attribute("class") == "next disabled":
            print "This is last page. No more next page available."
        active_page = self.driver.find_element_by_xpath(pg_active_page_locator)
        print "Current Active page number is :", active_page.text

    def pagination_previous(self):
        pg_list_of_nodes_locator = "//div[contains(@class,'dataTables_paginate paging_numbered')]/div/ul/li"
        list_of_nodes = self.driver.find_elements_by_xpath(pg_list_of_nodes_locator)
        pg_active_page_locator = "//li[contains(@class, 'active')]//a"
        if list_of_nodes[0].get_attribute("class") == "previous":
            list_of_nodes[0].click()
        elif list_of_nodes[0].get_attribute("class") == "previous disabled":
            print "This is first page. No more previous page available."
        active_page = self.driver.find_element_by_xpath(pg_active_page_locator)
        print "Current Active page number is :", active_page.text


    def pagination_drop_down_click(self, page_index):
        pg_drop_down_arrow_locator = "//li[contains(@class, 'dropup')]"
        drop_down_arrow = self.driver.find_element_by_xpath(pg_drop_down_arrow_locator)
        drop_down_arrow.click()
        sleep(1)
        pg_list_of_drop_down_locator = "//li[contains(@class, 'dropup')]//ul/li/a"
        list_of_page_drop_down = self.driver.find_elements_by_xpath(pg_list_of_drop_down_locator)
        if len(list_of_page_drop_down)>=1:
            list_of_page_drop_down[page_index].click()
