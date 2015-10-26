__author__ = 'Deepa.Sivadas'

from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from selenium.webdriver.common.keys import Keys
from time import sleep

class ThreatStreamPage(BasePageClass):


    _ts_app_name_text = ".//*[@id='header']/span[@class='ng-scope active']/span"
    _ts_setting_link_locator = ".//*[@id='page_content']/div[contains(@class,'header icon_bar')]/img[@title='Settings']"
    _ts_setting_window_locator = ".//div[@id='threatstream_settings_modal']//h4[@class='modal-title']"
    _ts_setting_window_compact_view_checkbox_locator = ".//form[contains(@class,'ng-pristine ng-valid')]/div[@class='modal-body']/div/label/span/span"
    _ts_setting_window_save_button_locator = ".//*[@id='threatstream_settings_modal']//div[@class='modal-footer']/button[contains(text(),'Save')]"
    _ts_setting_window_close_button_locator = ".//*[@id='threatstream_settings_modal']//div[@class='modal-footer']/button[contains(text(),'Close')]"

    #Threat Stream dropdown selection
    _ts_threat_dropdown_filter_locator = ".//div[contains(@class,'leftcolumn')]//div[contains(@class,'squintemheader')]//a[@data-toggle='dropdown']/span/span"
    _ts_threat_dropdown_starred_filter_locator = "//div[contains(@class,'leftcolumn')]//div[contains(@class,'squintemheader')]//a[contains(text(),'Starred')]"
    _ts_threat_dropdown_stream_filter_locator = "//div[contains(@class,'leftcolumn')]//div[contains(@class,'squintemheader')]//a[contains(text(),'Stream')]"
    _ts_threat_dropdown_trendinglastday_filter_locator = "//div[contains(@class,'leftcolumn')]//div[contains(@class,'squintemheader')]//a[contains(text(),'Trending Last Day')]"
    _ts_threat_dropdown_trendinglasthour_filter_locator = "//div[contains(@class,'leftcolumn')]//div[contains(@class,'squintemheader')]//a[contains(text(),'Trending Last Hour')]"
    _ts_threat_dropdown_add_new_filter_locator = "//div[contains(@class,'leftcolumn')]//div[contains(@class,'squintemheader')]//a[contains(text(),'Add new')]"
    _ts_threat_filter_name_text_locator = "//div[contains(@class,'leftcolumn')]//div[contains(@class,'squintemheader')]/span/a[@data-toggle='dropdown']/span"

    #Threat Stream New Filter Window
    _ts_filter_create_title_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-header']/h4"
    _ts_filter_create_name_textbox_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-body']//input[@placeholder='Name']"
    _ts_filter_create_type_dropdown_arrow_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-body']//button[@data-toggle='dropdown']"
    _ts_filter_create_type_dropdown_rss_atom_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-body']//a[contains(text(),'Rss')]"
    _ts_filter_create_type_dropdown_twitter_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-body']//a[contains(text(),'Twitter')]"
    _ts_filter_create_type_refresh_button_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-body']/div/a/img"
    _ts_filter_create_tags_textbox_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-body']//input[@ng-model='newTag']"
    _ts_filter_create_tags_add_button_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-body']//button[contains(@ng-click,'addTag')]"
    _ts_filter_create_tags_delete_icon_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-body']//a[contains(@ng-click,'deleteTag')]"
    _ts_filter_create_phrases_textbox_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-body']//input[@ng-model='newItemName']"
    _ts_filter_create_phrases_add_button_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-body']//button[contains(@ng-click,'addItem')]"
    _ts_filter_create_phrases_delete_icon_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-body']//a[contains(@ng-click,'deleteItem')]"
    _ts_filter_create_save_button_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-footer']//button[contains(text(),'Save')]"
    _ts_filter_create_cancel_button_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-footer']//button[contains(@ng-click,'cancel_squintem_filter_edit')]"
    _ts_filter_create_delete_button_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-footer']//button[contains(@ng-click,'delete_filter_edit')]"
    _ts_filter_create_confirm_delete_button_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-footer']//button[contains(@ng-click,'submit_filter_delete')]"
    _ts_filter_create_confirm_cancel_button_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-footer']//button[contains(@ng-click,'cancel_filter_delete')]"

    @property
    def get_ts_app_name(self):
        return self.driver.find_element_by_xpath(self._ts_app_name_text)

    @property
    def get_ts_setting_link(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_setting_link_locator)
        except Exception, err:
            raise type(err)("Setting Link is disabled or not appearing- search XPATH - " \
                          + self._ts_setting_link_locator + err.message)

    @property
    def get_ts_setting_window_checkbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_setting_window_compact_view_checkbox_locator)
        except Exception, err:
            raise type(err)("Compact view check box is not available - " \
                          + self._ts_setting_window_compact_view_checkbox_locator + err.message)

    @property
    def get_ts_setting_window_save_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_setting_window_save_button_locator)
        except Exception, err:
            raise type(err)("In Setting window Save button is not displayed - " \
                          + self._ts_setting_window_save_button_locator + err.message)

    @property
    def get_ts_setting_window_close_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_setting_window_close_button_locator)
        except Exception, err:
            raise type(err)("In Setting window Close button is not displayed - " \
                          + self._ts_setting_window_close_button_locator + err.message)

    @property
    def get_ts_threat_dropdown_filter(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_dropdown_filter_locator)
        except Exception, err:
            raise type(err)("Threat selection drop down filter arrow is not available - " \
                          + self._ts_threat_dropdown_filter_locator + err.message)

    @property
    def get_ts_threat_dropdown_starred_filter(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_dropdown_starred_filter_locator)
        except Exception, err:
            raise type(err)("In Dropdown menu Starred option is not available - " \
                          + self._ts_threat_dropdown_starred_filter_locator + err.message)

    @property
    def get_ts_threat_dropdown_stream_filter(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_dropdown_stream_filter_locator)
        except Exception, err:
            raise type(err)("In Dropdown menu Stream option is not available - " \
                          + self._ts_threat_dropdown_stream_filter_locator + err.message)

    @property
    def get_ts_threat_dropdown_trendinglastday_filter(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_dropdown_trendinglastday_filter_locator)
        except Exception, err:
            raise type(err)("In Dropdown menu Trending Last Day option is not available - " \
                          + self._ts_threat_dropdown_trendinglastday_filter_locator + err.message)

    @property
    def get_ts_threat_dropdown_trendinglasthour_filter(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_dropdown_trendinglasthour_filter_locator)
        except Exception, err:
            raise type(err)("In Dropdown menu Trending Last Hour option is not available - " \
                          + self._ts_threat_dropdown_trendinglasthour_filter_locator + err.message)

    @property
    def get_ts_threat_dropdown_addnew_filter(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_dropdown_add_new_filter_locator)
        except Exception, err:
            raise type(err)("In Dropdown menu Trending Last Hour option is not available - " \
                          + self._ts_threat_dropdown_add_new_filter_locator + err.message)

    @property
    def get_ts_threat_filter_name_text(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_filter_name_text_locator)
        except Exception, err:
            raise type(err)("Threat Filter name is not available - " \
                          + self._ts_threat_filter_name_text_locator + err.message)

    @property
    def get_ts_filter_create_title_text(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_title_locator)
        except Exception, err:
            raise type(err)("Filter create window title is not available - " \
                          + self._ts_filter_create_title_locator + err.message)

    @property
    def get_ts_filter_create_name_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_name_textbox_locator)
        except Exception, err:
            raise type(err)("Filter create window Name textbox is not available - " \
                          + self._ts_filter_create_name_textbox_locator + err.message)

    @property
    def get_ts_filter_create_type_dropdown_arrow(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_type_dropdown_arrow_locator)
        except Exception, err:
            raise type(err)("Filter create window Type dropdown arrow is not available - " \
                          + self._ts_filter_create_type_dropdown_arrow_locator + err.message)

    @property
    def get_ts_filter_create_type_dropdown_rss_atom(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_type_dropdown_rss_atom_locator)
        except Exception, err:
            raise type(err)("Filter create window RSS Atom Type dropdown is not available - " \
                          + self._ts_filter_create_type_dropdown_rss_atom_locator + err.message)

    @property
    def get_ts_filter_create_type_dropdown_twitter(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_type_dropdown_twitter_locator)
        except Exception, err:
            raise type(err)("Filter create window Twitter Type dropdown is not available - " \
                          + self._ts_filter_create_type_dropdown_twitter_locator + err.message)

    @property
    def get_ts_filter_create_type_refresh_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_type_refresh_button_locator)
        except Exception, err:
            raise type(err)("Filter create window Type refresh button is not available - " \
                          + self._ts_filter_create_type_refresh_button_locator + err.message)

    @property
    def get_ts_filter_create_tags_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_tags_textbox_locator)
        except Exception, err:
            raise type(err)("Filter create window Tags text box is not available - " \
                          + self._ts_filter_create_tags_textbox_locator + err.message)

    @property
    def get_ts_filter_create_tags_add_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_tags_add_button_locator)
        except Exception, err:
            raise type(err)("Filter create window Tags Add button is not available - " \
                          + self._ts_filter_create_tags_add_button_locator + err.message)

    @property
    def get_ts_filter_create_tags_delete_icon(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_tags_delete_icon_locator)
        except Exception, err:
            raise type(err)("Filter create window Tags delete icon is not available - " \
                          + self._ts_filter_create_tags_delete_icon_locator + err.message)

    @property
    def get_ts_filter_create_phrases_textbox_locator(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_phrases_textbox_locator)
        except Exception, err:
            raise type(err)("Filter create window Phrases text box is not available - " \
                          + self._ts_filter_create_phrases_textbox_locator + err.message)

    @property
    def get_ts_filter_create_phrases_add_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_phrases_add_button_locator )
        except Exception, err:
            raise type(err)("Filter create window Phrases Add button is not available - " \
                          + self._ts_filter_create_phrases_add_button_locator  + err.message)

    @property
    def get_ts_filter_create_phrases_delete_icon(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_phrases_delete_icon_locator )
        except Exception, err:
            raise type(err)("Filter create window Phrases delete icon is not available - " \
                          + self._ts_filter_create_phrases_delete_icon_locator  + err.message)

    @property
    def get_ts_filter_create_save_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_save_button_locator )
        except Exception, err:
            raise type(err)("Filter create window Save button is not available - " \
                          + self._ts_filter_create_save_button_locator  + err.message)

    @property
    def get_ts_filter_create_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_cancel_button_locator )
        except Exception, err:
            raise type(err)("Filter create window Cancel button is not available - " \
                          + self._ts_filter_create_cancel_button_locator  + err.message)

    @property
    def get_ts_filter_create_delete_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_delete_button_locator )
        except Exception, err:
            raise type(err)("Filter create window Delete button is not available - " \
                          + self._ts_filter_create_delete_button_locator  + err.message)

    @property
    def get_ts_filter_create_confirm_delete_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_confirm_delete_button_locator )
        except Exception, err:
            raise type(err)("Filter create Delete confirm window's Delete button is not available - " \
                          + self._ts_filter_create_confirm_delete_button_locator  + err.message)

    @property
    def get_ts_filter_create_confirm_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_confirm_cancel_button_locator )
        except Exception, err:
            raise type(err)("Filter create Delete confirm window's Cancel button is not available - " \
                          + self._ts_filter_create_confirm_cancel_button_locator  + err.message)

    def __init__(self, driver):
        super(ThreatStreamPage, self).__init__(driver)
        appicon = IconListPage(self.driver)
        appicon.click_threatstream()
        sleep(10)