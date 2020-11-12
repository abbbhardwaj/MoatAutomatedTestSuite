#author - Abhinav Bhardwaj

Feature: Creatives count verification

  Scenario Outline: verify creatives count for Saturn, Saturday’s Market, and Krux on search results page
    Given user is on moat homepage
    When user search for "<brand_name>" brand
    Then compare creatives count "<creatives_count>" of brand
    Examples: creatives-count
      | brand_name        | creatives_count |
      | Saturn            | 203             |
      | Saturday's Market | 8               |
      | Krux              | 50              |