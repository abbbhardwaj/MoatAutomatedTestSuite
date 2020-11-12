from behave import *
from helper.helper_base import *
import time
from Configuration.setup import *
from helper.launch_config import LaunchConfig
from utils.wrapperlogging import ReportLogMain
from utils import loggerutils


class AutoCompleteTextSteps:
    """
    Step definition class for autocomplete feature
    """
    driver_static = ''

    @given('launch moat website')
    def launch_browser(context):
        loggerutils.setup_logging()
        loggerutils.setup_formatted_logging(context)
        ReportLogMain.start_test_case(context)
        ReportLogMain.log_info(context, "Launching browser session")
        driver = LaunchConfig.launch_browser(browser_type)
        ReportLogMain.log_info(context,
                               "[Verification - Pass]: {browser} browser is running".format(browser=browser_type))
        driver.get(baseURL)
        driver.implicitly_wait(30)
        AutoCompleteTextSteps.driver_static = driver

    @when('user enters keyword')
    def enter_keyword(context):
        ReportLogMain.start_test_step(context, "Verify Auto completion on Ad search text box")
        context.driver = AutoCompleteTextSteps.driver_static

        for row in context.table:
            keyword = row['keyword']
            ReportLogMain.log_info(context, "Enter substring for brand name: " + keyword)
            if len(keyword) <= 6:
                ReportLogMain.log_info(context, keyword[:5] + " is entered for brand: " + keyword)
                Functions.search_text_for_auto_complete(context.driver, keyword, keyword[:3])
            else:
                ReportLogMain.log_info(context, keyword[:5] + " is entered")
                Functions.search_text_for_auto_complete(context.driver, keyword, keyword[:5])
            ReportLogMain.log_info(context, "Assertions passed and brand name in drop-down is found and clicked")
            time.sleep(2)

    @then('verify the search bar autocompletes the drop down text')
    def verify_autocomplete(context):
        ReportLogMain.log_info(context, "browser is being closed")
        context.driver.quit()
        ReportLogMain.end_test_step(context)
        ReportLogMain.end_test_case(context)
