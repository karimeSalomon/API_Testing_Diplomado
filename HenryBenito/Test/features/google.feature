Feature: Google main page

  Scenario: All components are displayed
    When I go to google home page
    Then I should see Google logo
      And I should see the search box
      And I should see the gmail link
      And I should see the images link
      And I should see the google apps button
      And I should see the search voice button
      And I should see the search with google button
      And I should see the I feel lucky button

  Scenario: Do a sum operation using search box
    Given I go to google home page
    When I write 5+2 in search box
      And I press Enter button
    Then I watch 7 as a result