from time import sleep
from selenium import webdriver

class Pagination(object):
    
    def __init__(self, driver):
        self.driver = driver
    
    #pagination
    _pg_list_of_nodes_locator = "//div[contains(@class,'dataTables_paginate paging_numbered')]/div/ul/li"
    _pg_active_page_locator = "//li[contains(@class, 'active')]//a"
    _pg_drop_down_arrow_locator = "//li[contains(@class, 'dropup')]"
    _pg_list_of_page_groups_locator = "//li[contains(@class, 'dropup')]//ul/li/a"

    @property
    def get_pg_list_of_nodes(self):
        try:
            return self.driver.find_elements_by_xpath(self._pg_list_of_nodes_locator)
        except Exception, err:
            raise type(err)("Pagination nodes are not available - searched XPATH - " \
                          + self._pg_list_of_nodes_locator + err.message)

    @property
    def get_pg_active_page(self):
        try:
            return self.driver.find_element_by_xpath(self._pg_active_page_locator)
        except Exception, err:
            raise type(err)("Pagination Active page is not displayed - searched XPATH - " \
                          + self._pg_active_page_locator + err.message)

    @property
    def get_pg_drop_down_arrow(self):
        try:
            return self.driver.find_element_by_xpath(self._pg_drop_down_arrow_locator)
        except Exception, err:
            raise type(err)("Pagination drop down arrow is not displayed - searched XPATH - " \
                          + self._pg_drop_down_arrow_locator + err.message)

    @property
    def get_pg_list_of_page_groups(self):
        try:
            return self.driver.find_elements_by_xpath(self._pg_list_of_page_groups_locator)
        except Exception, err:
            raise type(err)("Pagination drop down arrow is not displayed - searched XPATH - " \
                          + self._pg_list_of_page_groups_locator + err.message)
  
    def get_pagination_info(self):
        list_of_nodes = self.get_pg_list_of_nodes
        pagination_start = list_of_nodes[1].text
        pagination_end = list_of_nodes[-3].text
        print "Pagination start at page number : ", pagination_start
        print "Pagination end at page number : ", pagination_end
        print "Current Active Page Number is :", self.pagination_active_page()
        drop_down_arrow = self.get_pg_drop_down_arrow
        drop_down_arrow.click()
        sleep(1)
        print "Total number of total pages available are:",self.pagination_total_pages()

    def pagination_total_pages(self):
        drop_down_arrow = self.get_pg_drop_down_arrow
        drop_down_arrow.click()
        sleep(2)
        list_of_group_pages_dropdown = self.get_pg_list_of_page_groups
        if len(list_of_group_pages_dropdown) == 0:
            return 0
        else:
            total_pages = (list_of_group_pages_dropdown[-1].text).split("-")[1]
            drop_down_arrow.click()
            sleep(2)
            return total_pages

    def pagination_next(self):
        list_of_nodes = self.get_pg_list_of_nodes
        if list_of_nodes[-1].get_attribute("class") == "next":
            list_of_nodes[-1].click()
            sleep(3)
        elif list_of_nodes[-1].get_attribute("class") == "next disabled":
            pass
            #print "This is last page. No more next page available."

    def pagination_previous(self):
        list_of_nodes = self.get_pg_list_of_nodes
        if list_of_nodes[0].get_attribute("class") == "previous":
            list_of_nodes[0].click()
            sleep(3)
        elif list_of_nodes[0].get_attribute("class") == "previous disabled":
            pass
            #print "This is first page. No more previous page available."

    def pagination_drop_down_click(self, page_index):
        self.get_pg_drop_down_arrow.click()
        sleep(2)
        list_of_page_drop_down = self.get_pg_list_of_page_groups
        if len(list_of_page_drop_down) >= 1:
            list_of_page_drop_down[page_index].click()
        else:
            pass
            #print "Pagination does not have page groups"

    def pagination_active_page(self):
        sleep(2)
        active_page = self.get_pg_active_page
        #print "Current Active page number is :", active_page.text
        return int(active_page.text)

    def pagination_start_end_node_value(self):
        sleep(2)
        list_of_nodes = self.get_pg_list_of_nodes
        sleep(2)
        pagination_start_node = list_of_nodes[1].text.encode('utf-8')
        pagination_end_node = list_of_nodes[-3].text.encode('utf-8')
        return (pagination_start_node, pagination_end_node)
