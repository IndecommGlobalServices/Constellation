__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys

class BasePage(BasePageClass):
    _home_page_landing_logo_locator = "//*[@id='page_content']/div[1]/div[1]/span"
    _reset_button_locator = ".//*[@id='span_filters']//button[contains(text(),'Reset filter')]"
    _search_text_box_locator = ".//*[@id='span_filters']/following-sibling::input"

    def __init__(cls, driver):
        super(BasePage,cls).__init__(driver)

    def accessURL(self):
        self.driver.get("https://constellation-qa.haystax.com/#/")

    def findElementByXpath(self, xpath):
        wait = WebDriverWait(self.driver, 100, poll_frequency=5, ignored_exceptions=[StaleElementReferenceException, ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element

    def findElementsByXpath(self, xpath):
        wait = WebDriverWait(self.driver, 100, poll_frequency=5, ignored_exceptions=[StaleElementReferenceException, ElementNotVisibleException, ElementNotSelectableException])
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        return elements

    def findIfElementVisible(self, xpath):
        wait = WebDriverWait(self.driver, 50, poll_frequency=5, ignored_exceptions=[StaleElementReferenceException, ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return element

    def findIfElementNotVisible(self, xpath):
        wait = WebDriverWait(self.driver, 100, poll_frequency=5, ignored_exceptions=[StaleElementReferenceException, ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(EC.invisibility_of_element_located((By.XPATH, xpath)))
        return element

    def findElementById(self, id):
        wait = WebDriverWait(self.driver, 100, poll_frequency=5, ignored_exceptions=[StaleElementReferenceException, ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(EC.presence_of_element_located((By.ID, id)))
        return element

    def findElementByName(self, name):
        wait = WebDriverWait(self.driver, 100, poll_frequency=5, ignored_exceptions=[StaleElementReferenceException, ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(EC.presence_of_element_located((By.NAME, name)))
        return element

    def findElementByLinkText(self, name):
        wait = WebDriverWait(self.driver, 100, poll_frequency=5, ignored_exceptions=[StaleElementReferenceException, ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, name)))
        return element
    @property
    def get_reset_button(self):
        try:
            return self.driver.find_element_by_xpath(self._reset_button_locator)
        except Exception, err:
            raise type(err)("Reset button is not available - searched XPATH -"+self._reset_button_locator + err.message)

    @property
    def get_search_text_box(self):
        try:
            return self.driver.find_element_by_xpath(self._search_text_box_locator)
        except Exception, err:
            raise type(err)("Search text box is not available - searched XPATH - " \
                            + self._search_text_box_locator + err.message)


    def reset_and_search_clear(self):
        self.get_reset_button.click()
        sleep(5)
        # self.reset_and_search_clear()
        # sleep(1)
        self.get_search_text_box.send_keys(Keys.CONTROL, "a", Keys.DELETE)
        sleep(8)

