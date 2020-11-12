from behave import *
from helper.launch_config import LaunchConfig
from helper.helper_base import Functions
from pageObjects.homePage import *
from pageObjects.searchResultsPage import *
import time
from Configuration.setup import *
from utils.assertutils import *
from pageObjects.shareAdWindow import *
from selenium.webdriver.common.action_chains import ActionChains
from utils.wrapperlogging import ReportLogMain
from utils import loggerutils


class ShareAdVerification:
    """
    step file for share Ad link feature
    """
    brand_name = 'Random House'
    driver_static = ''

    @given('search results page')
    def navigate_search_results_page(context):
        loggerutils.setup_logging()
        loggerutils.setup_formatted_logging(context)
        ReportLogMain.start_test_case(context)
        ReportLogMain.log_info(context, "Launching browser session")
        driver = LaunchConfig.launch_browser(browser_type)
        driver.get(baseURL)
        driver.implicitly_wait(30)
        ReportLogMain.log_info(context,
                               "[Verification - Pass]: {browser} browser is running".format(browser=browser_type))

        ReportLogMain.start_test_step(context, "Share Ad feature on Ad overlay ")

        ReportLogMain.log_info(context, ShareAdVerification.brand_name + " is being searched")

        brand_name_search_results_page = Functions.search_brand_name_and_verify(driver, ShareAdVerification.brand_name,
                                                                                textbox_search_field_xpath)

        ReportLogMain.log_info(context,
                               "user is navigated on search results page for brand : "
                               + brand_name_search_results_page.text)

        try:
            Assert.assert_true(brand_name_search_results_page.text == ShareAdVerification.brand_name, "user is not on "
                               + brand_name_search_results_page.text + " page")
            ReportLogMain.log_info(context, "[Verification-Pass]: user is on {brand} page".format(
                brand=ShareAdVerification.brand_name))
        except AssertionError:
            ReportLogMain.log_error(context, "[Verification-Fail]: user is not on correct page")
        time.sleep(3)
        ShareAdVerification.driver_static = driver
        ReportLogMain.end_test_step(context)

    @when('user hover over an ad')
    def hover_over_ad(context):
        ReportLogMain.start_test_step(context, "Hover over Ad")
        context.driver = ShareAdVerification.driver_static
        action = ActionChains(context.driver)
        ad_search_results = context.driver.find_element_by_xpath(img_ad_xpath)
        action.move_to_element(ad_search_results).perform()
        ReportLogMain.log_info(context, "Ad overlay is displayed when cursor is hover")
        ReportLogMain.end_test_step(context)

    @then('verify share Ad link is displayed on overlay')
    def verify_share_link(context):
        ReportLogMain.start_test_step(context, "Verify Share link is displayed")
        share_link = context.driver.find_element_by_xpath(btn_share_xpath)
        if share_link.text == 'Share':
            ReportLogMain.log_info(context, 'share link is present on Ad overlay')
        ReportLogMain.end_test_step(context)

    # scenario - 2: share link functioning
    @when('user is on Ad overlay')
    def open_ad_overlay(context):
        ReportLogMain.start_test_step(context, "Ad overlay verifications")
        ad_popup_header = context.driver.find_element_by_xpath(text_Ad_popup_xpath).text

        try:
            Assert.assert_true(ad_popup_header == ShareAdVerification.brand_name, "user is not on Ad overlay window")
            ReportLogMain.log_info(context, "[Verification-Pass]: user is on Ad overlay window")
        except AssertionError:
            ReportLogMain.log_error(context, "[Verification-Fail]: user is not on Ad overlay window")
        ReportLogMain.end_test_step(context)

    @then('user clicks on share link')
    def click_share_btn(context):
        ReportLogMain.start_test_step(context, "Verify Share link functioning")
        context.driver.find_element_by_xpath(btn_share_xpath).click()
        ReportLogMain.log_info(context, 'share link is clicked')

    @when('share window popup is displayed')
    def verify_share_window(context):
        share_window_popup_header = context.driver.find_element_by_xpath(text_share_popup_header_xpath).text
        if share_window_popup_header == 'Share':
            ReportLogMain.log_info(context, "user is on share window popup page")

    @then('user clicks on copy link')
    def click_copy_link(context):
        action = ActionChains(context.driver)
        copy_link = context.driver.find_element_by_xpath(btn_copy_link_xpath)
        action.move_to_element(copy_link).click().perform()
        ReportLogMain.log_info(context, 'copy link is clicked')

    @then('verify url is copied')
    def verify_url_statement(context):
        url_copy_statement = context.driver.find_element_by_xpath(text_url_copy_xpath).text
        shareable_url = context.driver.find_element_by_xpath(text_shareable_url_xpath).get_attribute("value")

        try:
            Assert.assert_true(str(url_copy_statement).__contains__("URL copied to clipboard!"),
                               "url copied statement is not displayed")
            ReportLogMain.log_info(context, "copied url is: " + shareable_url)
            ReportLogMain.log_info(context, "[Verification-Pass]: url is copied to clipboard successfully")
        except AssertionError:
            ReportLogMain.log_error(context, "[Verification-Fail]: url is not copied to clipboard using copy link")
        time.sleep(3)

    @then('close the share window')
    def close_share_window(context):
        context.driver.find_element_by_xpath(btn_share_close_xpath).click()
        ReportLogMain.log_info(context, 'share window is closed')
        ReportLogMain.log_info(context, "browser is being closed")
        context.driver.quit()
        ReportLogMain.end_test_step(context)
        ReportLogMain.end_test_case(context)
