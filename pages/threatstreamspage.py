__author__ = 'Deepa.Sivadas'

from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from selenium.webdriver.common.keys import Keys
from loginpage import LoginPage
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class ThreatStreamPage(BasePageClass):


    _ts_app_name_text = ".//*[@id='header']/span[contains(@class,'ng-scope active')]/span"
    _ts_setting_link_locator = "//img[contains(@alt,'Settings')]"
    _ts_setting_window_title_locator = ".//*[@id='threatstream_settings_modal']//h4[@class='modal-title']"
    _ts_setting_window_compact_view_checkbox_locator = "//label[contains(text(),'Compact View')]"
    _ts_setting_window_save_button_locator = ".//*[@id='threatstream_settings_modal']//button[contains(text(),'Save')]"
    _ts_setting_window_close_button_locator = ".//*[@id='threatstream_settings_modal']//button[contains(text(),'Close')]"

    #Threat Stream dropdown selection
    _ts_threat_dropdown_filter_locator = ".//div[contains(@class,'leftcolumn')]//div[contains(@class,'squintemheader')]//a[@data-toggle='dropdown']/span/span"
    _ts_threat_filter_edit_cog_wheel_locator = ".//div[contains(@class,'leftcolumn')]//a[contains(@ng-click,'edit_filter')]"
    _ts_threat_dropdown_starred_filter_locator = "//div[contains(@class,'leftcolumn')]//a[contains(text(),'Starred')]"
    _ts_threat_dropdown_stream_filter_locator = "//div[contains(@class,'leftcolumn')]//a[contains(text(),'Stream')]"
    _ts_threat_dropdown_trendinglastday_filter_locator = "//div[contains(@class,'leftcolumn')]//a[contains(text(),'Trending Last Day')]"
    _ts_threat_dropdown_trendinglasthour_filter_locator = "//div[contains(@class,'leftcolumn')]//a[contains(text(),'Trending Last Hour')]"
    _ts_threat_dropdown_add_new_filter_locator = "//div[contains(@class,'leftcolumn')]//a[contains(text(),'Add new')]"
    _ts_threat_filter_name_text_locator = "//div[contains(@class,'leftcolumn')]//span/a[@data-toggle='dropdown']/span"
    _ts_threat_second_filter_dropdown_locator = ".//div[contains(@class,'leftcolumn')]//div[contains(@class,'squintemheader')]//div/a/span"
    _ts_threat_filter_dropdown_relevance_locator = ".//div[contains(@class,'leftcolumn')]//li/a[contains(text(),'Relevance')]"
    _ts_threat_filter_dropdown_time_locator = ".//div[contains(@class,'leftcolumn')]//li/a[contains(text(),'Time')]"
    _ts_threat_second_filter_name_text_locator = "//div[contains(@class,'leftcolumn')]//div/a[@data-toggle='dropdown']"

    #Threat Stream New Filter Window
    _ts_filter_create_title_locator = "//div[contains(@class,'leftcolumn')]//div[@editfilter='editfilter']//div[@class='modal-header']/h4"
    _ts_filter_create_name_textbox_locator = "//div[contains(@class,'leftcolumn')]//input[@placeholder='Name']"
    _ts_filter_create_type_text_locator = "//div[contains(@class,'leftcolumn')]//div[@label='Type']//button[@type='button']"
    _ts_filter_create_type_dropdown_arrow_locator = "//div[contains(@class,'leftcolumn')]//div[@label='Type']//button[@data-toggle='dropdown']"
    _ts_filter_create_type_dropdown_rss_atom_locator = "//div[contains(@class,'leftcolumn')]//a[contains(text(),'Rss')]"
    _ts_filter_create_type_dropdown_twitter_locator = "//div[contains(@class,'leftcolumn')]//a[contains(text(),'Twitter')]"
    _ts_filter_create_type_refresh_button_locator = "//div[contains(@class,'leftcolumn')]//div/a[contains(@ng-click,'reset_type')]"
    _ts_filter_create_visibility_dropdown_locator = "//div[contains(@class,'leftcolumn')]//div[@label='Visibility']//button[@data-toggle='dropdown']"
    _ts_filter_create_visibility_groups_locator = "//div[contains(@class,'leftcolumn')]//a[text()='Groups']"
    _ts_filter_create_visibility_tenant_locator = "//div[contains(@class,'leftcolumn')]//a[text()='Tenant']"
    _ts_filter_create_visibility_user_locator = "//div[contains(@class,'leftcolumn')]//a[text()='User']"
    _ts_filter_create_visibility_text_locator = "//div[label='Visibility']//button[@type='button']"
    _ts_filter_create_tags_textbox_locator = "//div[contains(@class,'leftcolumn')]//input[@ng-model='newTag']"
    _ts_filter_create_tags_add_button_locator = "//div[contains(@class,'leftcolumn')]//button[contains(@ng-click,'addTag')]"
    _ts_filter_create_tags_delete_icon_locator = "//div[contains(@class,'leftcolumn')]//a[contains(@ng-click,'deleteTag')]"
    _ts_filter_create_phrases_textbox_locator = "//div[contains(@class,'leftcolumn')]//input[@ng-model='newItemName']"
    _ts_filter_create_phrases_add_button_locator = "//div[contains(@class,'leftcolumn')]//button[contains(@ng-click,'addItem')]"
    _ts_filter_create_phrases_delete_icon_locator = "//div[contains(@class,'leftcolumn')]//a[contains(@ng-click,'deleteItem')]"
    _ts_filter_create_save_button_locator = "//div[contains(@class,'leftcolumn')]//button[contains(text(),'Save')]"
    _ts_filter_create_cancel_button_locator = "//div[contains(@class,'leftcolumn')]//div[@class='modal-footer']//button[contains(@ng-click,'cancel_squintem_filter_edit')]"
    _ts_filter_create_delete_button_locator = "//div[contains(@class,'leftcolumn')]//button[contains(@ng-click,'delete_filter_edit')]"
    _ts_filter_create_confirm_delete_button_locator = "//div[contains(@class,'leftcolumn')]//button[contains(@ng-click,'submit_filter_delete')]"
    _ts_filter_create_confirm_cancel_button_locator = "//div[contains(@class,'leftcolumn')]//button[contains(@ng-click,'cancel_filter_delete')]"
    _ts_filter_create_advance_link_locator = "//div[contains(@class,'leftcolumn')]//label/span[contains(text(), 'Advanced')]"
    _ts_filter_create_advance_filter_check = ".//div[contains(@class,'leftcolumn')]//div[@ng-show='showAdvancedFilters']"
    _ts_filter_create_location_icon_locator = "//div[contains(@class,'leftcolumn')]//div[label='Location']//img"
    _ts_filter_create_location_icon_check = "//div[contains(@class,'leftcolumn')]//div[contains(@class, 'location-show-hide')]"
    _ts_filter_create_location_latitude_textbox_locator = "//div[contains(@class,'leftcolumn')]//label[contains(text(),'Latitude')]/following-sibling::input"
    _ts_filter_create_location_latitude_error_message_locator = "//div[contains(@class,'leftcolumn')]//span[contains(@ng-show,'form_filter_edit.latitude')]/small"
    _ts_filter_create_location_longitude_textbox_locator = "//div[contains(@class,'leftcolumn')]//label[contains(text(),'Longitude')]/following-sibling::input"
    _ts_filter_create_location_longitude_error_message_locator = "//div[contains(@class,'leftcolumn')]//span[contains(@ng-show,'form_filter_edit.longitude')]/small"
    _ts_filter_create_location_radius_textbox_locator = "//div[contains(@class,'leftcolumn')]//label[contains(text(),'Radius')]/following-sibling::input"
    _ts_filter_create_location_radius_error_message_locator = "//div[contains(@class,'leftcolumn')]//span[contains(@ng-show,'form_filter_edit.radius')]/small"
    _ts_filter_create_location_text_locator = "//div[contains(@class,'leftcolumn')]//span[contains(@class,'smalllocationtext')]"
    _ts_filter_create_assets_textbox_locator = "//div[contains(@class,'leftcolumn')]//label[contains(text(),'Assets')]/following-sibling::typeahead/div/input"
    _ts_filter_create_assets_add_button_locator = "//div[contains(@class,'leftcolumn')]//label[contains(text(),'Assets')]/following-sibling::button"
    _ts_filter_create_assets_delete_icon_locator = "//div[contains(@class,'leftcolumn')]//a[contains(@ng-click,'deleteAsset')]"
    _ts_filter_create_assets_name_list_locator = "//div[contains(@class,'leftcolumn')]//label[contains(text(),'Assets')]/following-sibling::typeahead//li"


    #Twitter or RSS/ATOM content locator
    _ts_feeds_list_locator = "//div[contains(@class,'leftcolumn')]//ul[contains(@class,'squintems')]//li"
    _ts_feeds_list_text_locator = "//div[contains(@class,'leftcolumn')]//ul[contains(@class,'squintems')]//li/span[@bind-html-compile='squint.header_html']"
    _ts_feed_data_details_link_locator = "//div[contains(@class,'leftcolumn')]//a[contains(@ng-click,'expand_squintem')]"
    _ts_feed_data_important_button_locator = "//div[contains(@class,'leftcolumn')]//div[@class='squintem-details']//span//button[@id='btn-important']"
    _ts_feed_data_hide_button_locator = "//div[contains(@class,'leftcolumn')]//div[@class='squintem-details']//span//button[contains(@ng-click,'hide')]"
    _ts_feed_data_share_button_locator = "//div[contains(@class,'leftcolumn')]//div[@class='squintem-details']//span//button[contains(@ng-click,'share')]"

    #Email Share Window locator
    _ts_feed_email_window_title_locator = ".//div[contains(@class,'modal in')]//h4[@id='H1']"
    _ts_feed_email_window_email_textbox_locator = ".//div[contains(@class,'modal in')]//input[@placeholder='Email']"
    _ts_feed_email_window_comment_textbox_locator = ".//div[contains(@class,'modal in')]//input[@placeholder='Optional comment']"
    _ts_feed_email_window_send_button_locator = ".//div[contains(@class,'modal in')]//button[contains(text(),'Send')]"
    _ts_feed_email_window_cancel_button_locator = ".//div[contains(@class,'modal in')]//button[contains(text(),'Cancel')]"

    #Manage Feeds Locator
    _ts_manage_feeds_link_locator = "//img[contains(@alt,'Manage feeds')]"
    _ts_manage_feeds_app_text_locator = ".//*[@id='header']//span[contains(text(),'Manage Feeds')]"
    _ts_manage_feeds_filter_type_text_locator = "//*[@id='span_filters']/div/div/button[@type='button']"
    _ts_manage_feeds_filter_type_drop_down_locator = "//*[@id='span_filters']/div/div/button[contains(@class,'dropdown-toggle')]"
    _ts_manage_feeds_type_dropdown_rss_atom_locator = ".//*[@id='span_filters']/div/div/ul//a[text()='Rss/atom']"
    _ts_manage_feeds_type_dropdown_rss_atom_off_locator = ".//*[@id='span_filters']/div/div/ul//a[text()='Rss/atom-OFF']"
    _ts_manage_feeds_type_dropdown_twitter_locator = ".//*[@id='span_filters']/div/div/ul//a[text()='Twitter']"
    _ts_manage_feeds_reset_filters_locator = ".//*[@id='span_filters']/button"
    _ts_manage_feeds_search_feeds_locator = ".//*[@id='txt_search_feeds']"
    _ts_manage_feeds_text_locator = ".//*[@id='feedstable']/tbody/tr/td[2]"

    _ts_threat_streams_link_locator = ".//*[@id='header']//a[contains(text(),'Threat Streams')]"

    #Settings Locator
    #_ts_settings_link_locator = "//img[contains(@alt,'Settings')]"

    #Dashboard Locators
    _ts_dashboard_link_locator = "//img[@title='Dashboard']"
    _ts_dashboard_document_graph_locator = "//span[@id='dynamicsparklinetotal']"
    _ts_dashboard_rss_graph_locator = "//span[@id='dynamicsparklinerss']"
    _ts_dashboard_twitter_graph_locator = "//span[@id='dynamicsparklinetwitter']"

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
    def get_ts_threat_filter_edit_cog_wheel(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_filter_edit_cog_wheel_locator)
        except Exception, err:
            raise type(err)("Threat edit cog wheel is not available - " \
                          + self._ts_threat_filter_edit_cog_wheel_locator + err.message)

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
    def get_ts_threat_second_filter_dropdown(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_second_filter_dropdown_locator)
        except Exception, err:
            raise type(err)("Second Filter Threat selection drop down arrow is not available - " \
                          + self._ts_threat_second_filter_dropdown_locator + err.message)

    @property
    def get_ts_threat_second_filter_name_text(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_second_filter_name_text_locator)
        except Exception, err:
            raise type(err)("Threat Second Filter name is not available - " \
                          + self._ts_threat_second_filter_name_text_locator + err.message)

    @property
    def get_ts_threat_filter_dropdown_relevance(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_filter_dropdown_relevance_locator)
        except Exception, err:
            raise type(err)("In Dropdown menu Relevance option is not available - " \
                          + self._ts_threat_filter_dropdown_relevance_locator + err.message)

    @property
    def get_ts_threat_filter_dropdown_time(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_filter_dropdown_time_locator)
        except Exception, err:
            raise type(err)("In Dropdown menu Time option is not available - " \
                          + self._ts_threat_filter_dropdown_time_locator + err.message)


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
    def get_ts_filter_create_type_text(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_type_text_locator)
        except Exception, err:
            raise type(err)("Filter create window Type Text is not available - " \
                          + self._ts_filter_create_type_text_locator + err.message)

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
    def get_ts_filter_create_visibility_dropdown_arrow(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_visibility_dropdown_locator)
        except Exception, err:
            raise type(err)("Filter create window Visibility dropdown arrow is not available - " \
                          + self._ts_filter_create_visibility_dropdown_locator + err.message)

    @property
    def get_ts_filter_create_visibility_groups(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_visibility_groups_locator)
        except Exception, err:
            raise type(err)("Filter create window Visibility Groups not available - " \
                          + self._ts_filter_create_visibility_groups_locator + err.message)


    @property
    def get_ts_filter_create_visibility_tenant(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_visibility_tenant_locator)
        except Exception, err:
            raise type(err)("Filter create window Visibility Tenant not available - " \
                          + self._ts_filter_create_visibility_tenant_locator + err.message)

    @property
    def get_ts_filter_create_visibility_user(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_visibility_user_locator)
        except Exception, err:
            raise type(err)("Filter create window Visibility User not available - " \
                          + self._ts_filter_create_visibility_user_locator + err.message)

    @property
    def get_ts_filter_create_visibility_text(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_visibility_text_locator)
        except Exception, err:
            raise type(err)("Filter create window Visibility User not available - " \
                          + self._ts_filter_create_visibility_text_locator + err.message)

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
            return self.driver.find_elements_by_xpath(self._ts_filter_create_tags_delete_icon_locator)
        except Exception, err:
            raise type(err)("Filter create window Tags delete icon is not available - " \
                          + self._ts_filter_create_tags_delete_icon_locator + err.message)

    @property
    def get_ts_filter_create_phrases_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_phrases_textbox_locator)
        except Exception, err:
            raise type(err)("Filter create window Phrases text box is not available - " \
                          + self._ts_filter_create_phrases_textbox_locator + err.message)

    @property
    def get_ts_filter_create_phrases_add_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_phrases_add_button_locator)
        except Exception, err:
            raise type(err)("Filter create window Phrases Add button is not available - " \
                          + self._ts_filter_create_phrases_add_button_locator + err.message)

    @property
    def get_ts_filter_create_phrases_delete_icon(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_filter_create_phrases_delete_icon_locator)
        except Exception, err:
            raise type(err)("Filter create window Phrases delete icon is not available - " \
                          + self._ts_filter_create_phrases_delete_icon_locator + err.message)

    @property
    def get_ts_filter_create_save_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_save_button_locator)
        except Exception, err:
            raise type(err)("Filter create window Save button is not available - " \
                          + self._ts_filter_create_save_button_locator + err.message)

    @property
    def get_ts_filter_create_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_cancel_button_locator)
        except Exception, err:
            raise type(err)("Filter create window Cancel button is not available - " \
                          + self._ts_filter_create_cancel_button_locator + err.message)

    @property
    def get_ts_filter_create_delete_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_delete_button_locator)
        except Exception, err:
            raise type(err)("Filter create window Delete button is not available - " \
                          + self._ts_filter_create_delete_button_locator + err.message)

    @property
    def get_ts_filter_create_confirm_delete_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_confirm_delete_button_locator)
        except Exception, err:
            raise type(err)("Filter create Delete confirm window's Delete button is not available - " \
                          + self._ts_filter_create_confirm_delete_button_locator + err.message)

    @property
    def get_ts_filter_create_confirm_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_confirm_cancel_button_locator)
        except Exception, err:
            raise type(err)("Filter create Delete confirm window's Cancel button is not available - " \
                          + self._ts_filter_create_confirm_cancel_button_locator + err.message)

    @property
    def get_ts_filter_create_advance_link(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_advance_link_locator)
        except Exception, err:
            raise type(err)("Filter create Advanced link is not available - " \
                          + self._ts_filter_create_advance_link_locator + err.message)

    @property
    def get_ts_filter_create_advance_filter_check(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_advance_filter_check)
        except Exception, err:
            raise type(err)("Filter create Advanced options are not available - " \
                          + self._ts_filter_create_advance_filter_check + err.message)

    @property
    def get_ts_filter_create_location_icon(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_location_icon_locator)
        except Exception, err:
            raise type(err)("Filter create location option are not available - " \
                          + self._ts_filter_create_location_icon_locator + err.message)

    @property
    def get_ts_filter_create_location_icon_check(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_location_icon_check)
        except Exception, err:
            raise type(err)("Filter create location check not is not available - " \
                          + self._ts_filter_create_location_icon_check + err.message)

    @property
    def get_ts_filter_create_location_latitude_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_location_latitude_textbox_locator)
        except Exception, err:
            raise type(err)("Filter create location latitude textbox is not available - " \
                          + self._ts_filter_create_location_latitude_textbox_locator + err.message)

    @property
    def get_ts_filter_create_location_latitude_error_message(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_location_latitude_error_message_locator)
        except Exception, err:
            raise type(err)("Filter create location latitude error message is not available - " \
                          + self._ts_filter_create_location_latitude_error_message_locator + err.message)

    @property
    def get_ts_filter_create_location_longitude_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_location_longitude_textbox_locator)
        except Exception, err:
            raise type(err)("Filter create location longitude textbox is not available - " \
                          + self._ts_filter_create_location_longitude_textbox_locator + err.message)

    @property
    def get_ts_filter_create_location_longitude_error_message(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_location_longitude_error_message_locator)
        except Exception, err:
            raise type(err)("Filter create location longitude error message is not available - " \
                          + self._ts_filter_create_location_longitude_error_message_locator + err.message)

    @property
    def get_ts_filter_create_location_radius_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_location_radius_textbox_locator)
        except Exception, err:
            raise type(err)("Filter create location Radius textbox is not available - " \
                          + self._ts_filter_create_location_radius_textbox_locator + err.message)

    @property
    def get_ts_filter_create_location_radius_error_message(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_location_radius_error_message_locator)
        except Exception, err:
            raise type(err)("Filter create location radius error message is not available - " \
                          + self._ts_filter_create_location_radius_error_message_locator + err.message)

    @property
    def get_ts_filter_create_location_text(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_location_text_locator)
        except Exception, err:
            raise type(err)("Filter create location longitude textbox is not available - " \
                          + self._ts_filter_create_location_text_locator + err.message)

    @property
    def get_ts_filter_create_assets_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_assets_textbox_locator)
        except Exception, err:
            raise type(err)("Filter create Assets textbox is not available - " \
                          + self._ts_filter_create_assets_textbox_locator + err.message)

    @property
    def get_ts_filter_create_assets_add_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_assets_add_button_locator)
        except Exception, err:
            raise type(err)("Filter create Assets textbox is not available - " \
                          + self._ts_filter_create_assets_add_button_locator + err.message)

    @property
    def get_ts_filter_create_assets_delete_icon(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_filter_create_assets_delete_icon_locator)
        except Exception, err:
            raise type(err)("Filter create Assets textbox is not available - " \
                          + self._ts_filter_create_assets_delete_icon_locator + err.message)

    @property
    def get_ts_filter_create_assets_name_list(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_filter_create_assets_name_list_locator)
        except Exception, err:
            raise type(err)("Filter create Assets name list is not available - " \
                          + self._ts_filter_create_assets_name_list_locator + err.message)

    @property
    def get_ts_feeds_list(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_feeds_list_locator)
        except Exception, err:
            raise type(err)("In feed Detail link is not available - "
                          + self._ts_feeds_list_locator + err.message)

    @property
    def get_ts_feeds_list_text_value(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_feeds_list_text_locator)
        except Exception, err:
            raise type(err)("In feed Detail link is not available - "
                          + self._ts_feeds_list_text_locator + err.message)

    @property
    def get_ts_feed_data_details_link(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_feed_data_details_link_locator)
        except Exception, err:
            raise type(err)("In feed Detail link is not available - "
                          + self._ts_feed_data_details_link_locator + err.message)

    @property
    def get_ts_feed_data_important_button(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_feed_data_important_button_locator)
        except Exception, err:
            raise type(err)("In feed Mark Important button is not available - "
                          + self._ts_feed_data_important_button_locator + err.message)

    @property
    def get_ts_feed_data_share_button_locator(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_feed_data_share_button_locator)
        except Exception, err:
            raise type(err)("In feed Share button is not available - "
                          + self._ts_feed_data_share_button_locator + err.message)
    @property
    def get_ts_feed_data_hide_button_locator(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_feed_data_hide_button_locator)
        except Exception, err:
            raise type(err)("In feed Hide button is not available - "
                          + self._ts_feed_data_hide_button_locator + err.message)

    @property
    def get_ts_feed_share_email_window_title(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_feed_email_window_title_locator)
        except Exception, err:
            raise type(err)("Email share window title is not available - " \
                          + self._ts_feed_email_window_title_locator + err.message)

    @property
    def get_ts_feed_email_window_email_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_feed_email_window_email_textbox_locator)
        except Exception, err:
            raise type(err)("Email share window Email text box is not available - " \
                          + self._ts_feed_email_window_email_textbox_locator + err.message)

    @property
    def get_ts_feed_email_window_comment_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_feed_email_window_comment_textbox_locator)
        except Exception, err:
            raise type(err)("Email share window Comment text box is not available - " \
                          + self._ts_feed_email_window_comment_textbox_locator + err.message)

    @property
    def get_ts_feed_email_window_send_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_feed_email_window_send_button_locator)
        except Exception, err:
            raise type(err)("Email share window Send button is not available - " \
                          + self._ts_feed_email_window_send_button_locator + err.message)

    @property
    def get_ts_feed_email_window_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_feed_email_window_cancel_button_locator)
        except Exception, err:
            raise type(err)("Email share window Cancel button is not available - " \
                          + self._ts_feed_email_window_cancel_button_locator + err.message)

    @property
    def get_ts_manage_feeds_link(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_manage_feeds_link_locator)
        except Exception, err:
            raise type(err)("Manage Feeds Link is not available - " \
                          + self._ts_manage_feeds_link_locator + err.message)

    @property
    def get_ts_manage_feeds_filter_type_drop_down_arrow(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_manage_feeds_filter_type_drop_down_locator)
        except Exception, err:
            raise type(err)("Manage Feeds Drop Down Filter Arrow is not available - " \
                          + self._ts_manage_feeds_filter_type_drop_down_locator + err.message)

    @property
    def get_ts_manage_feeds_type_dropdown_rss_atom_menu_item(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_manage_feeds_type_dropdown_rss_atom_locator)
        except Exception, err:
            raise type(err)("Manage feeds drop down Rss/Atom menu item is not available - " \
                          + self._ts_manage_feeds_type_dropdown_rss_atom_locator + err.message)

    @property
    def get_ts_manage_feeds_type_dropdown_rss_atom_off_menu_item(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_manage_feeds_type_dropdown_rss_atom_off_locator)
        except Exception, err:
            raise type(err)("Manage feeds drop down Rss/Atom-Off menu item is not available - " \
                          + self._ts_manage_feeds_type_dropdown_rss_atom_off_locator + err.message)

    @property
    def get_ts_manage_feeds_type_dropdown_twitter_menu_item(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_manage_feeds_type_dropdown_twitter_locator)
        except Exception, err:
            raise type(err)("Manage feeds drop down Twitter menu item is not available - " \
                          + self._ts_manage_feeds_type_dropdown_twitter_locator + err.message)

    @property
    def get_ts_manage_feeds_filter_type_text(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_manage_feeds_filter_type_text_locator)
        except Exception, err:
            raise type(err)("Manage feeds filter text is not available - " \
                          + self._ts_manage_feeds_filter_type_text_locator + err.message)

    @property
    def get_ts_manage_feeds_reset_filter(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_manage_feeds_reset_filters_locator)
        except Exception, err:
            raise type(err)("Manage feeds reset filter button is not available - " \
                          + self._ts_manage_feeds_reset_filters_locator + err.message)

    @property
    def get_ts_manage_feeds_search_feeds_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_manage_feeds_search_feeds_locator)
        except Exception, err:
            raise type(err)("Manage feeds reset filter button is not available - " \
                          + self._ts_manage_feeds_search_feeds_locator + err.message)

    @property
    def get_ts_manage_feeds_search_feeds_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_manage_feeds_search_feeds_locator)
        except Exception, err:
            raise type(err)("Manage feeds search feeds filter is not available - " \
                          + self._ts_manage_feeds_search_feeds_locator + err.message)

    @property
    def get_ts_manage_feeds_app_text(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_manage_feeds_app_text_locator)
        except Exception, err:
            raise type(err)("Manage feeds app text button is not available - " \
                          + self._ts_manage_feeds_app_text_locator + err.message)

    @property
    def get_ts_threat_streams_link(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_threat_streams_link_locator)
        except Exception, err:
            raise type(err)("Manage feeds app text button is not available - " \
                          + self._ts_threat_streams_link_locator + err.message)

    @property
    def get_ts_settings_window_title(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_setting_window_title_locator)
        except Exception, err:
            raise type(err)("Settings Window Title is not available - " \
                          + self._ts_setting_window_title_locator + err.message)

    @property
    def get_ts_manage_feeds_texts_list(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_manage_feeds_text_locator)
        except Exception, err:
            raise type(err)("Search feeds text are not available - " \
                          + self._ts_manage_feeds_text_locator + err.message)

    @property
    def get_ts_dashboard_link(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_dashboard_link_locator)
        except Exception, err:
            raise type(err)("Dashboard link is  not available - " + self._ts_dashboard_link_locator + err.message)

    @property
    def get_ts_dashboard_document_graph(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_dashboard_document_graph_locator)
        except Exception, err:
            raise type(err)("Dashboard document graph is not available - " \
                            + self._ts_dashboard_document_graph_locator + err.message)

    @property
    def get_ts_dashboard_rss_graph(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_dashboard_rss_graph_locator)
        except Exception, err:
            raise type(err)("Dashboard rss graph is not available - " \
                            + self._ts_dashboard_rss_graph_locator + err.message)

    @property
    def get_ts_dashboard_twitter_graph(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_dashboard_twitter_graph_locator)
        except Exception, err:
            raise type(err)("Dashboard twitter graph is not available - " \
                            + self._ts_dashboard_twitter_graph_locator + err.message)


    def get_ts_new_filter_name(self, file_name):
        xpath = "//div[contains(@class,'leftcolumn')]//a[contains(text(),'"+str(file_name)+"')]"
        try:
            return self.driver.find_element_by_xpath(xpath)
        except Exception, err:
            raise type(err)("Newly created filter name is not available - "+ xpath  + err.message)

    def delete_created_filter(self, filter_name):
        self.get_ts_threat_dropdown_filter.click()
        sleep(1)#required to update dropdown menu
        self.get_ts_new_filter_name(filter_name).click()
        #sleep(5)#required to update filter window title
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                        self._ts_threat_filter_edit_cog_wheel_locator)))
        self.get_ts_threat_filter_edit_cog_wheel.click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, \
                                                                         self._ts_filter_create_title_locator)))
        self.get_ts_filter_create_delete_button.click()
        sleep(4)#required to display delete confirm popup
        self.get_ts_filter_create_confirm_delete_button.click()
        #sleep(7)#required to update threat stream apps
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, \
                                                self._ts_threat_filter_name_text_locator),"Stream"))

    def show_advance_info(self):
            sleep(1)
            if "ng-hide" in self.get_ts_filter_create_advance_filter_check.get_attribute("class"):
                self.get_ts_filter_create_advance_link.click()
                sleep(1)

    def show_location_options(self):
            sleep(1)
            if " ng-hide" in self.get_ts_filter_create_location_icon_check.get_attribute("class"):
                self.get_ts_filter_create_location_icon.click()
                sleep(1)

    def show_dashboard_info(self):
        sleep(1)
        if "toggle-off" in self.get_ts_dashboard_link.get_attribute("class"):
                self.get_ts_dashboard_link.click()
                sleep(1)

    def return_to_apps_main_page(self):
        """
        Description : This function will helps to go back to threat stream page.
        Revision:
        :return: None
        """
        # if not self.get_asset_create_asset:
        #     try:
        #         WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
        #             (By.LINK_TEXT, self._asset_link_locator))).click()
        #         WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self._asset_create_asset)))
        #     except:
        #         inspectstack = inspect.stack()[1][3]
        #         self.recoverapp(inspectstack)



    def __init__(self, driver):
        super(ThreatStreamPage, self).__init__(driver)

    def logintoapp(self):
        loginpage = LoginPage(self.driver)
        loginpage.loginDashboard()
        # self.username = loginpage.usernameText
        appicon = IconListPage(self.driver)
        appicon.click_threatstream()
        sleep(20)