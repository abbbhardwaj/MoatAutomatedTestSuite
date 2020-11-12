from behave import *
from helper.helper_base import *
from pageObjects.homePage import *
from pageObjects.searchResultsPage import *
import time
from utils.assertutils import *
from helper.launch_config import LaunchConfig
from Configuration.setup import *
from utils.wrapperlogging import ReportLogMain
from utils import loggerutils


class RandomBrandGenerator:
    """
    Step definition file for random brand link generates random data feature
    """
    random_brand_generated_data = ''
    driver_static = ''

    @given('user is on search results page')
    def navigate_search_results_page(context):
        loggerutils.setup_logging()
        loggerutils.setup_formatted_logging(context)
        ReportLogMain.start_test_case(context)
        ReportLogMain.log_info(context, "Launching browser session")
        driver = LaunchConfig.launch_browser(browser_type)
        ReportLogMain.log_info(context,
                               "[Verification - Pass]: {browser} browser is running".format(browser=browser_type))
        driver.get(baseURL)
        driver.implicitly_wait(30)

        # search for random brands from feature file parameters
        for row in context.table:
            brand_name = row['brand']
            ReportLogMain.start_test_step(context,
                                          "Verify Random Brand Feature on search results page for brand: " + brand_name)
            ReportLogMain.log_info(context, "brand name: " + brand_name + " is entered in search bar")

            # calling shared function for search and click brand name on homepage screen
            brand_name_search_results_page = Functions.search_brand_name_and_verify(driver, brand_name,
                                                                                    textbox_search_field_xpath)
            ReportLogMain.log_info(context, "Assertions passed and brand name in drop-down is found and clicked")

            try:
                Assert.assert_true(brand_name_search_results_page.text == brand_name, "user is not on correct page")
                ReportLogMain.log_info(context, "[Verification-Pass]: user is on {brand} page".format(brand=brand_name))
                RandomBrandGenerator.random_brand_generated_data = brand_name_search_results_page.text
            except AssertionError:
                ReportLogMain.log_error(context, "[Verification-Fail]: user is not on correct page")
            time.sleep(3)

        RandomBrandGenerator.driver_static = driver

    @when('user click on Random brand link')
    def click_random_brand(context):
        context.driver = RandomBrandGenerator.driver_static
        context.driver.find_element_by_link_text(btn_random_brand_linktext).click()
        ReportLogMain.log_info(context, "Random brand button is clicked")

    @then('verify random brand advertiser is displayed')
    def verify_random_brand_generation(context):
        random_brand_name = context.driver.find_element_by_xpath(
            "//*[@class='entity-label']/span[@class='page-type']").text
        ReportLogMain.log_info(context,
                               random_brand_name + " is the new brand name that appears on search results page")
        try:
            Assert.assert_true(RandomBrandGenerator.random_brand_generated_data != random_brand_name
                               , "random brand link is functioning properly")
            ReportLogMain.log_info(context, "[Verification-Pass]: random brand is generated!")
        except AssertionError:
            ReportLogMain.log_error(context, "[Verification-Fail]: Random brand button is not generating random data")
        time.sleep(5)
        ReportLogMain.log_info(context, "closing the browser")
        context.driver.quit()
        ReportLogMain.end_test_step(context)
        ReportLogMain.end_test_case(context)
