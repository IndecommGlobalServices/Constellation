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
        # create a new Firefox session

        # chromedriver = "../drivers/chromedriver"
        # os.environ["webdriver.chrome.driver"]= chromedriver
        # cls.driver = webdriver.Chrome(chromedriver)

        cls.driver = webdriver.Firefox()
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

    def pagination_info(self):
        sleep(20)
        list_of_nodes = self.basepage.get_pg_list_of_nodes
        pagination_start = list_of_nodes[1].text
        pagination_end = list_of_nodes[-3].text
        print "Pagination start at page number : ", pagination_start
        print "Pagination end at page number : ", pagination_end
        print "Current Active Page Number is :", self.pagination_active_page()
        drop_down_arrow = self.basepage.get_pg_drop_down_arrow
        drop_down_arrow.click()
        sleep(1)
        self.pagination_total_pages()

    def pagination_total_pages(self):
        drop_down_arrow = self.basepage.get_pg_drop_down_arrow
        drop_down_arrow.click()
        sleep(1)
        list_of_group_pages_dropdown = self.basepage.get_pg_list_of_page_groups
        total_pages = (list_of_group_pages_dropdown[-1].text).split("-")[1]
        for index, item in enumerate(list_of_group_pages_dropdown):
            print index+1, "Page group is : ", item.text
        #print "Total number of total pages available are:", total_pages
        drop_down_arrow.click()
        sleep(1)
        return total_pages

    def pagination_next(self):
        list_of_nodes = self.basepage.get_pg_list_of_nodes
        if list_of_nodes[-1].get_attribute("class") == "next":
            list_of_nodes[-1].click()
            sleep(3)
        elif list_of_nodes[-1].get_attribute("class") == "next disabled":
            print "This is last page. No more next page available."

    def pagination_previous(self):
        list_of_nodes = self.basepage.get_pg_list_of_nodes
        if list_of_nodes[0].get_attribute("class") == "previous":
            list_of_nodes[0].click()
            sleep(3)
        elif list_of_nodes[0].get_attribute("class") == "previous disabled":
            print "This is first page. No more previous page available."

    def pagination_drop_down_click(self, page_index):
        self.basepage.get_pg_drop_down_arrow.click()
        sleep(1)
        list_of_page_drop_down = self.basepage.get_pg_list_of_page_groups
        if len(list_of_page_drop_down) >= 1:
            list_of_page_drop_down[page_index].click()

    def pagination_active_page(self):
        sleep(2)
        active_page = self.basepage.get_pg_active_page
        #print "Current Active page number is :", active_page.text
        return int(active_page.text)
