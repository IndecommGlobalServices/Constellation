__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException
from time import sleep

class BasePage(BasePageClass):
    _home_page_landing_logo_locator = "//*[@id='page_content']/div[1]/div[1]/span"

    # #pagination
    # _pg_list_of_nodes_locator = "//div[contains(@class,'dataTables_paginate paging_numbered')]/div/ul/li"
    # _pg_active_page_locator = "//li[contains(@class, 'active')]//a"
    # _pg_drop_down_arrow_locator = "//li[contains(@class, 'dropup')]"
    # _pg_list_of_page_groups_locator = "//li[contains(@class, 'dropup')]//ul/li/a"
    #
    # @property
    # def get_pg_list_of_nodes(self):
    #     try:
    #         return self.driver.find_elements_by_xpath(self._pg_list_of_nodes_locator)
    #     except Exception, err:
    #         raise type(err)("Pagination nodes are not available - searched XPATH - " \
    #                       + self._pg_list_of_nodes_locator + err.message)
    #
    # @property
    # def get_pg_active_page(self):
    #     try:
    #         return self.driver.find_element_by_xpath(self._pg_active_page_locator)
    #     except Exception, err:
    #         raise type(err)("Pagination Active page is not displayed - searched XPATH - " \
    #                       + self._pg_active_page_locator + err.message)
    #
    # @property
    # def get_pg_drop_down_arrow(self):
    #     try:
    #         return self.driver.find_element_by_xpath(self._pg_drop_down_arrow_locator)
    #     except Exception, err:
    #         raise type(err)("Pagination drop down arrow is not displayed - searched XPATH - " \
    #                       + self._pg_drop_down_arrow_locator + err.message)
    #
    # @property
    # def get_pg_list_of_page_groups(self):
    #     try:
    #         return self.driver.find_elements_by_xpath(self._pg_list_of_page_groups_locator)
    #     except Exception, err:
    #         raise type(err)("Pagination drop down arrow is not displayed - searched XPATH - " \
    #                       + self._pg_list_of_page_groups_locator + err.message)
    #

    def __init__(cls, driver):
        super(BasePage,cls).__init__(driver)

    def accessURL(self):
        self.driver.get("https://constellation-qa.haystax.com/#/")

