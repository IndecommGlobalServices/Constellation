__author__ = 'Deepa.Sivadas'

from lib.base import BasePageClass
from pages.IconListPage import IconListPage
from selenium.webdriver.common.keys import Keys
from time import sleep
from loginpage import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ThreatStreamPage(BasePageClass):


    _ts_app_name_text = ".//*[@id='header']/span[contains(@class,'ng-scope active')]/span"
    _ts_setting_link_locator = ".//*[@id='page_content']/div[contains(@class,'header icon_bar')]/img[@title='Settings']"
    _ts_setting_window_locator = ".//div[@id='threatstream_settings_modal']//h4[@class='modal-title']"
    _ts_setting_window_compact_view_checkbox_locator = ".//form[contains(@class,'ng-pristine ng-valid')]/div[@class='modal-body']/div/label/span/span"
    _ts_setting_window_save_button_locator = ".//*[@id='threatstream_settings_modal']//div[@class='modal-footer']/button[contains(text(),'Save')]"
    _ts_setting_window_close_button_locator = ".//*[@id='threatstream_settings_modal']//div[@class='modal-footer']/button[contains(text(),'Close')]"

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
    _ts_filter_create_type_refresh_button_locator = "//div[contains(@class,'leftcolumn')]//div[@class='modal-body']/div/a/img"
    _ts_filter_create_visibility_dropdown_locator = "//div[contains(@class,'leftcolumn')]//div[@label='Visibility']//button[@data-toggle='dropdown']"
    _ts_filter_create_visibility_groups_locator = "//div[contains(@class,'leftcolumn')]//a[text()='Groups']"
    _ts_filter_create_visibility_tenant_locator = "//div[contains(@class,'leftcolumn')]//a[text()='Tenant']"
    _ts_filter_create_visibility_user_locator = "//div[contains(@class,'leftcolumn')]//a[text()='User']"
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

    #Twitter or RSS/ATOM content locator
    _ts_feeds_list_locator = "//div[contains(@class,'leftcolumn')]//ul[contains(@class,'squintems')]//li"
    _ts_feeds_list_text_locator = "//div[contains(@class,'leftcolumn')]//ul[contains(@class,'squintems')]//li/span[@ng-bind-html='squint.header_with_links']"
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
                          + self._ts_filter_create_phrases_add_button_locator  + err.message)

    @property
    def get_ts_filter_create_phrases_delete_icon(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_filter_create_phrases_delete_icon_locator)
        except Exception, err:
            raise type(err)("Filter create window Phrases delete icon is not available - " \
                          + self._ts_filter_create_phrases_delete_icon_locator  + err.message)

    @property
    def get_ts_filter_create_save_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_save_button_locator)
        except Exception, err:
            raise type(err)("Filter create window Save button is not available - " \
                          + self._ts_filter_create_save_button_locator  + err.message)

    @property
    def get_ts_filter_create_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_cancel_button_locator)
        except Exception, err:
            raise type(err)("Filter create window Cancel button is not available - " \
                          + self._ts_filter_create_cancel_button_locator  + err.message)

    @property
    def get_ts_filter_create_delete_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_delete_button_locator)
        except Exception, err:
            raise type(err)("Filter create window Delete button is not available - " \
                          + self._ts_filter_create_delete_button_locator  + err.message)

    @property
    def get_ts_filter_create_confirm_delete_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_confirm_delete_button_locator)
        except Exception, err:
            raise type(err)("Filter create Delete confirm window's Delete button is not available - " \
                          + self._ts_filter_create_confirm_delete_button_locator  + err.message)

    @property
    def get_ts_filter_create_confirm_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_filter_create_confirm_cancel_button_locator)
        except Exception, err:
            raise type(err)("Filter create Delete confirm window's Cancel button is not available - " \
                          + self._ts_filter_create_confirm_cancel_button_locator  + err.message)

    @property
    def get_ts_feeds_list(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_feeds_list_locator)
        except Exception, err:
            raise type(err)("In feed Detail link is not available - "
                          + self._ts_feeds_list_locator  + err.message)

    @property
    def get_ts_feeds_list_text_value(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_feeds_list_text_locator)
        except Exception, err:
            raise type(err)("In feed Detail link is not available - "
                          + self._ts_feeds_list_text_locator  + err.message)

    @property
    def get_ts_feed_data_details_link(self):
        try:
            return self.driver.find_elements_by_xpath(self._ts_feed_data_details_link_locator)
        except Exception, err:
            raise type(err)("In feed Detail link is not available - "
                          + self._ts_feed_data_details_link_locator  + err.message)
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
                          + self._ts_feed_email_window_title_locator  + err.message)

    @property
    def get_ts_feed_email_window_email_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_feed_email_window_email_textbox_locator)
        except Exception, err:
            raise type(err)("Email share window Email text box is not available - " \
                          + self._ts_feed_email_window_email_textbox_locator  + err.message)
    @property
    def get_ts_feed_email_window_comment_textbox(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_feed_email_window_comment_textbox_locator)
        except Exception, err:
            raise type(err)("Email share window Comment text box is not available - " \
                          + self._ts_feed_email_window_comment_textbox_locator  + err.message)

    @property
    def get_ts_feed_email_window_send_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_feed_email_window_send_button_locator)
        except Exception, err:
            raise type(err)("Email share window Send button is not available - " \
                          + self._ts_feed_email_window_send_button_locator  + err.message)

    @property
    def get_ts_feed_email_window_cancel_button(self):
        try:
            return self.driver.find_element_by_xpath(self._ts_feed_email_window_cancel_button_locator)
        except Exception, err:
            raise type(err)("Email share window Cancel button is not available - " \
                          + self._ts_feed_email_window_cancel_button_locator  + err.message)


    def get_ts_new_filter_name(self, file_name):
        xpath = "//div[contains(@class,'leftcolumn')]//a[contains(text(),'"+str(file_name)+"')]"
        try:
            return self.driver.find_element_by_xpath(xpath)
        except Exception, err:
            raise type(err)("Newly created filter name is not available - "+ xpath  + err.message)

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
        loginpage = LoginPage(self.driver)
        loginpage.loginDashboard()
        self.username = loginpage.usernameText
        appicon = IconListPage(self.driver)
        appicon.click_threatstream()
        sleep(20)