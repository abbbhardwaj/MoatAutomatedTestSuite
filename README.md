# Moat Assignment Automated Test Suite

Automated Test suite for executing UI level test cases on Moat.com

## Description

The test suite is a BDD (Behavior driven development) Behave framework, Selenium webdriver, Gherkin, Python(3.4). 
1. Framework is based on page object model.
2. Test cases are designed as features in feature files using python-behave
3. Test execution logging
4. Reporting using Allure report.

Scenarios covered with the framework :-
1.	Verify the search bar autocomplete drop down text.
2.	Verify the creatives count on the search results page is correct for these 3 search terms: Saturn, Saturday’s Market, and Krux.
3.	Verify the “Random Brand” link on the search results page is random.
4.	Verify the “Share” ad feature (it appears on overlay when hovering over an ad). 


## Install dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependent packages in requirements.txt using 
```bash
pip install -r requirements.txt
```

Note: Install Allure CLI for converting json files to html reports from [Allure](https://docs.qameta.io/allure/)

## Modify test data for test cases

In order to modify a test case using the Framework, you have to follow the below steps:

* In features folder, open a feature file and change the parameters in table under Examples or Given statements.


## Run the test case with Allure Reports

In order to run entire test framework with all feature files, use below commands:

```bash
behave -f allure_behave.formatter:AllureFormatter -o reports features
```

```bash
allure serve reports\
```

To run individual test cases, run below commands

```bash
behave features\\shareAd.feature
```

## Logging

To view execution logs, navigate to logs folder in root folder directory with recent time and date