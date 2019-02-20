Feature: Customre search

Search for total proced values for a client

Scenario Outline: Searching for total priced on a list

  Given I send the name <Name> of a client
  And I send the id <ID> of this client
  When I start searching for the client
  Then I should get the price $<Price>

  Examples:
  | Name        | ID | Price |
  | jhon doe    | 1  | 34    |
  | killer bee  | 2  | 45    |
  | foo bar     | 3  | 23    |
  | stepway     | 4  | 234   |
  | motun couga | 5  | 332   |

Scenario: Client exists on database

  Given I send the name foo bar of a client
  And I send the id 3 of this client
  When I start searching for the client
  Then The client should be found with same name as foo bar