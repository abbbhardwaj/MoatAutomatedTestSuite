from behave import *
from helper.helper_base import *
from pageObjects.homePage import *
from pageObjects.searchResultsPage import *
import time
from utils import loggerutils
from utils.assertutils import *
from helper.launch_config import LaunchConfig
from Configuration.setup import *
from utils.wrapperlogging import ReportLogMain


class CreativeCountVerify:
    """
    step file for creatives count feature on search results page
    """
    driver_static = ''

    @given('user is on moat homepage')
    def launch_website(context):
        loggerutils.setup_logging()
        loggerutils.setup_formatted_logging(context)
        ReportLogMain.start_test_case(context)
        ReportLogMain.log_info(context, "Launching browser session")
        driver = LaunchConfig.launch_browser(browser_type)
        ReportLogMain.log_info(context,
                               "[Verification - Pass]: {browser} browser is running".format(browser=browser_type))
        driver.get(baseURL)
        driver.implicitly_wait(30)
        CreativeCountVerify.driver_static = driver

    @when('user search for "{brand_name}" brand')
    def search_brand(context, brand_name):
        ReportLogMain.start_test_step(context, "Creatives count verification for brand - " + brand_name)

        context.driver = CreativeCountVerify.driver_static

        ReportLogMain.log_info(context, brand_name + " is being searched")
        brand_name_search_results_page = Functions.search_brand_name_and_verify(context.driver, brand_name,
                                                                                textbox_search_field_xpath)

        ReportLogMain.log_info(context, "user is on page" + brand_name_search_results_page.text)

        try:
            Assert.assert_true(brand_name_search_results_page.text == brand_name, "user is not on correct page")
            ReportLogMain.log_info(context, "[Verification-Pass]: user is on {brand} page".format(brand=brand_name))
        except AssertionError as e:
            ReportLogMain.log_error(context, "user is not on correct page! Error: %s" % e)
        time.sleep(3)
        ReportLogMain.end_test_step(context)

    @then('compare creatives count "{creatives_count}" of brand')
    def compare_creatives_count(context, creatives_count):

        ReportLogMain.start_test_step(context, "Comparing count in feature file and on UI")
        count_from_ui = context.driver.find_element_by_xpath(text_creatives_count_xpath).text
        creative_count_split = str(count_from_ui).split()

        try:
            Assert.assert_equals(creative_count_split[0], creatives_count, 'creative count does not match')
            ReportLogMain.log_info(context, "[Verification-Pass]: creative count in feature file: " + creatives_count +
                                   " and on UI: " +
                                   creative_count_split[0] + " is same ")
        except AssertionError:
            ReportLogMain.log_error(context, "[Verification-Fail]: creative count is not same")
        time.sleep(5)
        ReportLogMain.log_info(context, "closing the browser")
        context.driver.quit()
        ReportLogMain.end_test_step(context)
        ReportLogMain.end_test_case(context)
