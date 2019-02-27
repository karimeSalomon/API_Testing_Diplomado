Feature: Test search goes to expected results according search criteria provided.

  Scenario: Successful search results looking with regular sentence text
    Given I insert a search criteria text
    When I click on search with google button
    Then I am redirected to my results page with my search criteria

  Scenario: Successful search results looking by voice
    Given I click on voice microphone icon
    And I record a voice search criteria
    Then I am redirected to my results page with my search criteria

  Scenario: I feel lucky page is opened with no searching text
    When I click on I feel lucky button
    Then I am redirected to doodles page
