Feature: Verify Google Home functionality

  Scenario: Verify the page is loaded with the most important elements for search

    Given Open a Web browser
    When Go to "https://www.google.com/"
    Then Google logo is loaded properly
    And Input text is loaded properly
    And "Google Search" button is loaded properly
    And "I'm feel lucky" button is loaded properly
    And traslation elements are loaded properly

  Scenario: Verify the page is loaded with the gmail options
    Given Open a Web browser
    When Go to "https://www.google.com/"
    Then "Gmail" link is loaded properly
    And "Images" link is loaded properly
    And menu icon is displayed
    And log in is enabled


  Scenario: Verify the page is loaded with bottom options
    Given Open a Web browser
    When Go to "https://www.google.com/"
    Then "Privay" link is loaded properly
    And "Terms" link is loaded properly
    And "Settings" link is loaded properly
    And "Advertising" link is loaded properly
    And "Business" link is loaded properly
    And "About" link is loaded properly