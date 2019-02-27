Feature: Main page
  As an administrator
  I want to have a main page
  So that members use it as searching start point

  @acceptance
  Scenario: Textfield is displayed and is editable
    Given I have navigate to the https://www.google.com/ page
    When I review the page
    Then I can see an outlined textfield with "Search Google or type a URL" message
    And I can enter a text to the textfield

  @acceptance
  Scenario: Text can be searched by entering it to the Textfield
    Given I have navigated to the https://www.google.com/ page
    When I enter "Testing tools" text to the search textfield
    And I press enter key
    Then I can see "Testing tools" in the search's result

  @acceptance
  Scenario: Search by voice button is displayed and enabled
    Given I have navigated to the https://www.google.com/ page
    When I review the page
    Then I can see "Search by voice" button is displayed and enabled

  @acceptance
  Scenario: Google icon is displayed
    Given I have navigated to the https://www.google.com/ page
    When I review the page
    Then I can see Google icon correctly

  @acceptance
  Scenario: About link is displayed and redirects to proper page
    Given I have navigated to the https://www.google.com/ page
    When I review the left down page
    Then I can see "About" link
    When I click the About link
    Then I can see https://about.google/ page is opened

  @acceptance
  Scenario: Advertising link is displayed and redirects to proper page
    Given I have navigated to the https://www.google.com/ page
    When I review the left down page
    Then I can see "Advertising" link
    When I click the Advertising link
    Then I can see https://ads.google.com/ page is opened

  @acceptance
  Scenario: Business link is displayed and redirects to proper page
    Given I have navigated to the https://www.google.com/ page
    When I review the left down page
    Then I can see "Business" link
    When I click the Business link
    Then I can see https://www.google.com/services/ page is opened

  @functional
  Scenario: long text can be searched by entering it to the Textfield
    Given I have navigated to the https://www.google.com/ page
    When I enter "What makes TestRail stand out among software testing tools" text to the search textfield
    And I press enter key
    Then I can see "What makes TestRail stand out among software testing tools" in the search's result

  @functional
  Scenario: text with special characters can be searched by entering it to the Textfield
    Given I have navigated to the https://www.google.com/ page
    When I enter "Sign in to create your own set! Ⓐ ⓐ ⒜ A a Ạ ạ Å å Ä ä Ả ả Ḁ ḁ Ấ ấ Ầ ầ Ẩ ẩ Ȃ ȃ Ẫ ẫ Ậ ậ Ắ ắ Ằ ằ Ẳ ẳ Ẵ ẵ Ặ ặ Ā ā Ą ą Ȁ ȁ Ǻ ǻ Ȧ ȧ Á á Ǟ ǟ Ǎ ǎ" text to the search textfield
    And I press enter key
    Then I can see "Sign in to create your own set! Ⓐ ⓐ ⒜ A a Ạ ạ Å å Ä ä Ả ả Ḁ ḁ Ấ ấ Ầ ầ Ẩ ẩ Ȃ ȃ Ẫ ẫ Ậ ậ Ắ ắ Ằ ằ Ẳ ẳ Ẵ ẵ Ặ ặ Ā ā Ą ą Ȁ ȁ Ǻ ǻ Ȧ ȧ Á á Ǟ ǟ Ǎ ǎ" in the search's result

  @functional
  Scenario: Can login with valid gmail account
    Given I have navigated to the https://www.google.com/ page
    When I click "Sing in" button
    And I enter valid credentials
    And I click Next button
    Then I can see I am successfully logged in

  @functional
  Scenario: Cannot see the login icon when open open browser as incognito
    Given I have navigated to the https://www.google.com/ page
    When I review the page at the right top
    Then I cannot see the Sing in button

  @functional
  Scenario: Can see shortcuts
    Given I have navigated to the https://www.google.com/ page
    When I review the page at middle
    Then I can see shortcuts displayed

  @functional
  Scenario: Can edit a shortcut
    Given I have navigated to the https://www.google.com/ page
    When I click "edit shortcut" at the shortcut's right top
      And I edit the Name
      And I edit the url
      And I click save button
    Then I can see shortcuts updated

  @functional
  Scenario: Can delete a shortcut
    Given I have navigated to the https://www.google.com/ page
    When I click "edit shortcut" at the shortcut's right top
      And I click delete button
    Then I should not see the shortcut anymore

  @functional
  Scenario: Can see Gmail link
    Given I have navigated to the https://www.google.com/ page
    When I review the page at the right top
    Then I can see the Gmail link

  @functional
  Scenario: Gmail link opens the Gmail page
    Given I have navigated to the https://www.google.com/ page
    When I click Gmail link at the right top
    Then I should see https://mail.google.com/mail opened

  @functional
  Scenario: Images link opens the Google-images
    Given I have navigated to the https://www.google.com/ page
    When I click Images link at the right top
    Then I should see https://www.google.com.bo/imghp opened

  @functional
  Scenario: Google applications icon displays shortcuts
    Given I have navigated to the https://www.google.com/ page
    When I click  Google applications icon at the right top
    Then I should see a set of shortcuts

  @functional
  Scenario: Notifications bell is not displayed when google account is not signed in
    Given I have navigated to the https://www.google.com/ page
    When I review the page at the right top
    Then I should not see the bell icon
