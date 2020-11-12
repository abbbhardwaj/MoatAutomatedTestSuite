from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class LaunchConfig:
    """
    helper class for initializing web driver every time a new feature file is executed/run
    """

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def launch_browser(browser):
        """
        static method used to start browser session for each feature file
        :param browser: name of browser to run i.e. chrome or firefox
        :return: webdriver instance
        """
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_experimental_option("detach", True)
            return webdriver.Chrome(executable_path=".\Drivers\chromedriver.exe", options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start-maximized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        raise Exception("Provide valid driver name")
