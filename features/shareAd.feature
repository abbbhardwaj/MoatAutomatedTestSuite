# author - Abhinav Bhardwaj

Feature: Share Ad feature on overlay verification
  Scenario: Verify the share Ad link appears on overlay when hovering over an ad
    Given search results page
    When user hover over an ad
    Then verify share Ad link is displayed on overlay
    When user is on Ad overlay
    Then user clicks on share link
    When share window popup is displayed
    Then user clicks on copy link
    Then verify url is copied
    Then close the share window