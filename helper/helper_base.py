from pageObjects.homePage import *
from utils.assertutils import *


class Functions:
    """
    function class implementation is used as technique to utilize shared functions been used around project
    Removes code redundancy.
    """

    @staticmethod
    def search_brand_name_and_verify(driver, brand_name, element_locator):
        """
           Shared function - Searches for brand name as mentioned in feature files, clicks on brand name links from drop down
           and verifies if correct brand page is open

           :Args
            - driver : webdriver instance
            - brand_name : brand to search and verify
            - element_locator : webelement locator (string)
           """
        driver.find_element_by_xpath(element_locator).send_keys(brand_name)

        brand_name_homepage = driver.find_element_by_xpath(
            '//span[contains(text(), "{value}")]'.format(value=brand_name))
        brand_name_homepage.click()

        # assertion for correct brand name results on search results page
        brand_name_search_results_page = driver.find_element_by_xpath(
            '//span[contains(text(), "{value}")]'.format(value=brand_name))

        return brand_name_search_results_page

    @staticmethod
    def search_text_for_auto_complete(driver, keyword, text):
        """"
            enters substring on search bar to verify autocompletion and clicks on the brand name
            Also, verifies if correct brand name is resulted on search results page

             :Args
             - driver : webdriver instance
             - keyword : brand to search and verify
             - text : substring of brand name
            """
        search_bar = driver.find_element_by_xpath(textbox_search_field_xpath)
        search_bar.send_keys(text)

        auto_complete_brand_name = driver.find_element_by_xpath(
            "//span[contains(text(), '{value}')]".format(value=keyword))

        if auto_complete_brand_name.is_displayed():
            auto_complete_brand_name.click()

        brand_name_search_results_page = driver.find_element_by_xpath(
            '//span[contains(text(), "{value}")]'.format(value=keyword))
        try:
            Assert.assert_true(brand_name_search_results_page.text == keyword, "user is not on correct page")
            print("[Verification-Pass]: user is on {brand} page".format(brand=keyword))
        except AssertionError:
            print("[Verification-Fail]: user is not on correct page")
        driver.find_element_by_xpath("//*[@class='logo-image']").click()
