__author__ = 'Deepa.Sivadas'
from lib.base import BasePageClass
from lib.base import InvalidPageException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.basepage import BasePage
from loginpage import LoginPage
from pages.IconListPage import IconListPage
import inspect


class FieldInterviewsPage(BasePageClass, object):
    _fi_interviews_app_name_locator = ".//*[@id='header']//span[contains(text(),'Field Interview')]"
    _fi_contact_type_drop_down_locator = "//button[contains(text(),'Contact type')]/following-sibling::button"
    _fi_contact_type_gang_option_locator = "//a[contains(text(),'Gang Activity')]"
    _fi_contact_type_probation_option_locator = "//a[contains(text(),'Probation')]"
    _fi_contact_type_circumstances_option_locator = "//a[contains(text(),'Suspicious Circumstances')]"
    _fi_contact_type_person_option_locator = "//a[contains(text(),'Suspicious Person')]"
    _fi_contact_type_vehicle_option_locator = "//a[contains(text(),'Suspicious Vehicle')]"
    _fi_contact_type_traffic_option_locator = "//a[contains(text(),'Traffic Stop')]"
    _fi_reset_filters_button_locator = ".//*[@id='span_filters']/button"
    _fi_search_textbox_locator = ".//*[@id='txt_search_fieldinterviews']"
    _fi_search_error_message_locator = ".//*[@id='fieldinterviewsTable']/tbody/tr/td"
    _fi_select_action_drop_down_locator = "//button[contains(text(),'Select action')]/following-sibling::button"
    _fi_select_action_delete_option_locator = ".//*[@id='fieldinterview_actions_dropdown']/ul/li/a"
    _fi_app_link_locator = "Field Interviews"
    _fi_settings_link_locator = ".//*[@id='page_content']//img[@title='Settings']"
    _fi_settings_window_periodic_refresh_checkbox_locator = "//label[contains(text(),'Periodic refresh')]"
    _fi_settings_window_alert_on_new_fi_checkbox_locator = "//label[contains(text(),'Alert on new field interviews')]"
    _fi_settings_window_badge_number_textbox_locator = "//label[contains(text(),'Badge number')]/.." \
                                                       "/following-sibling::td/input"
    _fi_settings_window_rank_textbox_locator = "//label[contains(text(),'Rank')]/../following-sibling::td/input"
    _fi_settings_window_close_button_locator = ".//*[@id='fieldinterview_settings_modal']//button" \
                                               "[contains(text(),'Close')]"
    _fi_settings_window_save_button_locator = ".//*[@id='fieldinterview_settings_modal']//button" \
                                              "                                               [contains(text(),'Save')]"
    _fi_settings_window_heading_locator = ".//*[@id='fieldinterview_settings_modal']//h4"
    _fi_field_interviews_checkbox_locator = ".//*[@id='fieldinterviewsTable']//label"
    _fi_selected_filter_button_text_locator = " .//*[@id='span_filters']/div/div/button[@type='button']"
    _fi_selected_filter_column_text_locator = ".//*[@id='fieldinterviewsTable']//td[5]"
    _fi_delete_window_heading_text_locator = ".//*[@id='delete_fieldinterview_modal']//h4"
    _fi_delete_window_cancel_button_locator = ".//*[@id='delete_fieldinterview_modal']//button[text()='Cancel']"
    _fi_delete_window_delete_button_locator = ".//*[@id='delete_fieldinterview_modal']//button[text()='Delete']"

    @property
    def get_field_interviews_app_name_label(self):
        try:
            return self.basepage.findElementByXpath(self._fi_interviews_app_name_locator)
        except Exception, err:
            raise type(err)(" App name label not found.  " + err.message)

    @property
    def get_contact_type_drop_down(self):
        try:
            return self.basepage.findElementByXpath(self._fi_contact_type_drop_down_locator)
        except Exception, err:
            raise type(err)("Contact Type drop down is not available - searched XPATH - "\
                          + self._fi_contact_type_drop_down_locator + err.message)

    @property
    def get_contact_type_gang_option(self):
        try:
            return self.basepage.findElementByXpath(self._fi_contact_type_gang_option_locator)
        except Exception, err:
            raise type(err)("In Contact Type drop down menu Gang option is not available - searched XPATH - "\
                          + self._fi_contact_type_gang_option_locator + err.message)

    @property
    def get_contact_type_probation_option(self):
        try:
            return self.basepage.findElementByXpath(self._fi_contact_type_probation_option_locator)
        except Exception, err:
            raise type(err)("In Contact Type drop down menu Probation option is not available - searched XPATH - "\
                          + self._fi_contact_type_probation_option_locator + err.message)

    @property
    def get_contact_type_circumstances_option(self):
        try:
            return self.basepage.findElementByXpath(self._fi_contact_type_circumstances_option_locator)
        except Exception, err:
            raise type(err)("In Contact Type drop down menu Circumstances option is not available - searched XPATH - "\
                          + self._fi_contact_type_circumstances_option_locator + err.message)

    @property
    def get_contact_type_person_option(self):
        try:
            return self.basepage.findElementByXpath(self._fi_contact_type_person_option_locator)
        except Exception, err:
            raise type(err)("In Contact Type drop down menu Person option is not available - searched XPATH - "\
                          + self._fi_contact_type_person_option_locator + err.message)

    @property
    def get_contact_type_vehicle_option(self):
        try:
            return self.basepage.findElementByXpath(self._fi_contact_type_vehicle_option_locator)
        except Exception, err:
            raise type(err)("In Contact Type drop down menu Vehicle option is not available - searched XPATH - "\
                          + self._fi_contact_type_vehicle_option_locator + err.message)

    @property
    def get_contact_type_traffic_option(self):
        try:
            return self.basepage.findElementByXpath(self._fi_contact_type_traffic_option_locator)
        except Exception, err:
            raise type(err)("In Contact Type drop down menu Traffic option is not available - searched XPATH - "\
                          + self._fi_contact_type_traffic_option_locator + err.message)

    @property
    def get_fi_reset_filters_button(self):
        try:
            return self.basepage.findElementByXpath(self._fi_reset_filters_button_locator)
        except Exception, err:
            raise type(err)("Reset button is not available - searched XPATH - "\
                          + self._fi_reset_filters_button_locator + err.message)

    @property
    def get_fi_search_textbox(self):
        try:
            return self.basepage.findElementByXpath(self._fi_search_textbox_locator)
        except Exception, err:
            raise type(err)("Search text box is not available - searched XPATH - "\
                          + self._fi_search_textbox_locator + err.message)

    @property
    def get_fi_search_error_message(self):
        try:
            return self.basepage.findElementByXpath(self._fi_search_error_message_locator)
        except Exception, err:
            raise type(err)("Search error message is not available - searched XPATH - "\
                          + self._fi_search_error_message_locator + err.message)

    @property
    def get_field_interviews_select_action_drop_down(self):
        try:
            return self.basepage.findElementByXpath(self._fi_select_action_drop_down_locator)
        except Exception, err:
            raise type(err)("Field Interview Select Action dropdown is not available - searched XPATH - "\
                          + self._fi_select_action_drop_down_locator + err.message)

    @property
    def get_field_interviews_select_action_delete_option(self):
        try:
            return self.basepage.findElementByXpath(self._fi_select_action_delete_option_locator)
        except Exception, err:
            raise type(err)("Field Interview Select Action Delete option is not available - searched XPATH - "\
                          + self._fi_select_action_delete_option_locator + err.message)

    @property
    def get_field_interviews_settings_link(self):
        try:
            return self.basepage.findElementByXpath(self._fi_settings_link_locator)
        except Exception, err:
            raise type(err)("Field Interview Settings link is not available - searched XPATH - "\
                          + self._fi_settings_link_locator + err.message)

    @property
    def get_fi_settings_window_periodic_refresh_checkbox(self):
        try:
            return self.basepage.findElementByXpath(self._fi_settings_window_periodic_refresh_checkbox_locator)
        except Exception, err:
            raise type(err)("In FI settings window periodic refresh checkbox is not available - searched XPATH - "\
                          + self._fi_settings_window_periodic_refresh_checkbox_locator + err.message)

    @property
    def get_fi_settings_window_alert_on_new_fi_checkbox(self):
        try:
            return self.basepage.findElementByXpath(self._fi_settings_window_alert_on_new_fi_checkbox_locator)
        except Exception, err:
            raise type(err)("In FI settings window alert on new fi checkbox is not available - searched XPATH - "\
                          + self._fi_settings_window_alert_on_new_fi_checkbox_locator + err.message)

    @property
    def get_fi_settings_window_badge_number_textbox(self):
        try:
            return self.basepage.findElementByXpath(self._fi_settings_window_badge_number_textbox_locator)
        except Exception, err:
            raise type(err)("In FI settings window badge number textbox is not available - searched XPATH - "\
                          + self._fi_settings_window_badge_number_textbox_locator + err.message)

    @property
    def get_fi_settings_window_rank_textbox(self):
        try:
            return self.basepage.findElementByXpath(self._fi_settings_window_rank_textbox_locator)
        except Exception, err:
            raise type(err)("In FI settings window rank textbox is not available - searched XPATH - "\
                          + self._fi_settings_window_rank_textbox_locator + err.message)

    @property
    def get_fi_settings_window_close_button(self):
        try:
            return self.basepage.findElementByXpath(self._fi_settings_window_close_button_locator)
        except Exception, err:
            raise type(err)("In FI settings window close button is not available - searched XPATH - "\
                          + self._fi_settings_window_close_button_locator + err.message)

    @property
    def get_fi_settings_window_save_button(self):
        try:
            return self.basepage.findElementByXpath(self._fi_settings_window_save_button_locator)
        except Exception, err:
            raise type(err)("In FI settings window Save button is not available - searched XPATH - "\
                          + self._fi_settings_window_save_button_locator + err.message)

    @property
    def get_fi_settings_window_heading(self):
        try:
            return self.basepage.findElementByXpath(self._fi_settings_window_heading_locator)
        except Exception, err:
            raise type(err)("In FI settings window heading is not available - searched XPATH - "\
                          + self._fi_settings_window_heading_locator + err.message)

    @property
    def get_field_interviews_checkboxes(self):
        try:
            return self.basepage.findElementsByXpath(self._fi_field_interviews_checkbox_locator)
        except Exception, err:
            raise type(err)("Field Interviews checkboxes are not available - searched XPATH - "\
                          + self._fi_field_interviews_checkbox_locator + err.message)

    @property
    def get_selected_filter_button_text(self):
        try:
            return self.basepage.findElementByXpath(self._fi_selected_filter_button_text_locator)
        except Exception, err:
            raise type(err)("Selected Filter button text is not available - searched XPATH - "\
                          + self._fi_selected_filter_button_text_locator + err.message)

    @property
    def get_selected_filter_column_text(self):
        try:
            return self.basepage.findElementsByXpath(self._fi_selected_filter_column_text_locator)
        except Exception, err:
            raise type(err)("Selected Filter column texts are not available - searched XPATH - "\
                          + self._fi_selected_filter_column_text_locator + err.message)

    @property
    def get_fi_delete_window_heading_text(self):
        try:
            return self.basepage.findElementByXpath(self._fi_delete_window_heading_text_locator)
        except Exception, err:
            raise type(err)("FI Delete Window heading is not available - searched XPATH - "\
                          + self._fi_delete_window_heading_text_locator + err.message)

    @property
    def get_fi_delete_window_heading_text(self):
        try:
            return self.basepage.findElementByXpath(self._fi_delete_window_heading_text_locator)
        except Exception, err:
            raise type(err)("FI Delete Window heading is not available - searched XPATH - "\
                          + self._fi_delete_window_heading_text_locator + err.message)

    @property
    def get_fi_delete_window_delete_button(self):
        try:
            return self.basepage.findElementByXpath(self._fi_delete_window_delete_button_locator)
        except Exception, err:
            raise type(err)("In FI Delete Window delete button is not available - searched XPATH - "\
                          + self._fi_delete_window_delete_button_locator + err.message)

    @property
    def get_fi_delete_window_cancel_button(self):
        try:
            return self.basepage.findElementByXpath(self._fi_delete_window_cancel_button_locator)
        except Exception, err:
            raise type(err)("In FI Delete Window cancel button is not available - searched XPATH - "\
                          + self._fi_delete_window_cancel_button_locator + err.message)

    @property
    def get_filed_interview_header(self):
        try:
            self.driver.find_element_by_xpath(self._fi_interviews_app_name_locator)
        except:
            return False
        return True

    def return_to_apps_main_page(self):
        """
        Description : This function will helps to go back to field interviews page.
        Revision:
        :return: None
        """
        if not self.get_filed_interview_header:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                    (By.LINK_TEXT, self._fi_app_link_locator))).click()
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located \
                                                               ((By.XPATH,self._fi_interviews_app_name_locator)))
            except:
                inspectstack = inspect.stack()[1][3]
                self.recoverapp(inspectstack)

    def recoverapp(self, inspectstack):
        """
        Description : This function helps to go back to field interviews page. Inspect stack prints the test name from
                      which this function is called.
        Revision:
        :return: None
        """
        print ("Application recovering called from " + inspectstack)
        basepage = BasePage(self.driver)
        basepage.accessURL()
        iconlistpage = IconListPage(self.driver)
        iconlistpage.click_fieldinterview_icon()

    def open_field_interviews_app(self):
        loginpage = LoginPage(self.driver)
        loginpage.loginDashboard()
        appicon = IconListPage(self.driver)
        appicon.click_fieldinterview_icon()

    def field_interviews_count(self):
        count_string =  self.basepage.findElementByXpath(".//*[@id='fieldinterviewsTable_info']").text.encode('utf-8')
        count_string = (((count_string.split("\n" )[2]).split("of ")[1]).split(" entries")[0])
        return (int(count_string))

    def __init__(self, driver):
        super(FieldInterviewsPage,self).__init__(driver)
        self.basepage = BasePage(self.driver)


