#author - Abhinav Bhardwaj

  Feature: Random brand link verification
    Scenario: verify Random brand link on search results page is random
      Given user is on search results page
      |brand|
      |Game of Thrones (game)|
#      |Eaglebank             |
      When user click on Random brand link
      Then verify random brand advertiser is displayed
