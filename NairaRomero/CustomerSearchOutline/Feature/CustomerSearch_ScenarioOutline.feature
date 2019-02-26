Feature: Customer Search
  Scenario Outline: Search of a total priced for a list clients

    Given A Search a client <client_name>
    And I set the client <id>
    When I search the client
    Then I get the price $<price> for the specific client

    Examples:
    |client_name         | id | price |
    | Ana Perez          | a  | 20    |
    | Maria Gonzales     | b  | 25    |
    | Leonardo Gutierrez | c  | 30    |
    | Clara Lopez        | d  | 35    |
    | Dante Mendez       | e  | 350   |
    | Gabriela Torrez    | f  | 78    |
    | Helen Mendieta     | g  | 56    |
    | Alex Bell          | h  | 100   |

  Scenario: Search client in Dictionary

    Given A Search a client Helen Mendieta
    And I set the client id g
    When I search the client
    Then I get the same client found which is Helen Mendieta
