#author - Abhinav Bhardwaj

Feature: Search bar Autocomplete

  Scenario: search bar autocomplete drop down text
    Given launch moat website
    When user enters keyword
      | keyword         |
      | Autumn Festival |
      | Wine.com        |
    Then verify the search bar autocompletes the drop down text