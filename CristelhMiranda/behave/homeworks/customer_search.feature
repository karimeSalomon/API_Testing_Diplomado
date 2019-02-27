Feature: Customer Search
  As a user
  I want to search of a total priced for list clients

  Scenario Outline: Search of a total priced for a list client
    When I send <id> as id of client
    Then I should see name:<name> and total priced: <total_priced>
    Examples:
    |id|name |total_priced|
    |1 |Juan |100         |
    |2 |Pepe |200         |
    |3 |Maira|500         |
    |4 |Rene |150         |
    |5 |Ana  |88          |

  Scenario: Search of a total priced for a client
    When I send 1 as id of client
    Then I should see name:Juan and total priced:100

  Scenario: Search of a total priced for a client
    When I send 2 as id of client
    Then I should see name:Pepe and total priced:200

  Scenario: Search of a total priced for a client
    When I send 3 as id of client
    Then I should see name:Maira and total priced:500

  Scenario: Search of a total priced for a client
    When I send 4 as id of client
    Then I should see name:Rene and total priced:150

  Scenario: Search of a total priced for a client
    When I send 5 as id of client
    Then I should see name:Ana and total priced:88