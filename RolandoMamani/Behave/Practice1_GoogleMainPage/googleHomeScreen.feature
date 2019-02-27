Feature:  Search field
  Scenario: Text field to enter the keywords to search is available
    Given Access to Google URL
    When Being in home page
    Then Search field should be available in the home page

  Scenario: Google Search button is enabled
    Given Accessed to Google URL
    When Being in home page
    Then Google Search button is enabled
      And it is clickable

  Scenario: I'm Feeling Lucky button is enabled
    Given Accessed to Google URL
    When Being in home page
    Then I'm Feeling Lucky button is enabled
      And it is clickable
