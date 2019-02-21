# Consider you will be in charge of testing google main page.
#
# Create a feature file describing your feature, and adding
# all the scenarios that you consider that need to be add to
# be sure that page is working as expected
#
# Add the validation steps using Given, Then, When and also
# sing And /But or *.

Feature: Google Search

  Scenario: Verify auto-suggestion in google search
    Given I go to 'https://www.google.com'
    When I fill 'google' in Search field
    Then the following results should be displayed in Search field
      |google          |
      |google maps     |
      |google translate|
      |google drive    |
      |google earth    |
      |google docs     |

  Scenario: Verify response for a specific text is correct and related with the text
    Given I go to 'https://www.google.com'
    When I fill 'test' in Search field
      And I click on Google Search button
    Then the following results should be displayed on Google Search page
      |Speedtest by Ookla - The Global Broadband Speed Test|
      |Fast.com: Internet Speed Test                       |
      |Xfinity Speed Test                                  |
      |AT&T High Speed Internet Speed Test                 |
      |MyBroadband Speed Test                              |

  Scenario: Verify misspelled text gets corrected in response
    Given I go to 'https://www.google.com'
    When I fill 'mispelled' in Search field
      And I click on Google Search button
    Then the following message should be displayed on Google Search page
      """
      Showing results for misspelled
      Search instead for mispelled
      """
      And the following results should be displayed on Google Search page
        |Misspelled Define Misspelled at Dictionary.com      |
        |Misspell Definition of Misspell by Merriam-Webster  |
        |MISSPELL meaning in the Cambridge English Dictionary|
        |Misspell or Mispell Which Is Correct? - Grammarly   |

  Scenario: Verify response for special characters is correct
    Given I go to 'https://www.google.com'
    When I fill '$"{format}" C#' in Search field
      And I click on Google Search button
    Then the following results should be displayed on Google Search page
      |Use Of String.Format() To Format Strings In C# - C# Corner|
      |String.Format Method (System) Microsoft Docs              |
      |$ - string interpolation - C# Reference Microsoft Docs    |

  Scenario: Verify total number of results are fetched for a specific text
    Given I go to 'https://www.google.com'
    When I fill 'test' in Search field
      And I click on Google Search button
    Then the following message should be displayed on Google Search page
      """
      About 9,080,000,000 results
      """