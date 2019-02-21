# suppose you create a feature file for a customer search
#
# 1. add an scenario outline to simulate a search of a total priced for a
#    list clients.
#
#    you should send:
#        - the name of the client
#        - the id of the client
#        - the total priced of purchase
#
#    on behind you should create a module with a dictionary containing the list of
#    clients and the id
#    and another dictionary with the id of the client and the total_priced, to
#    perform the comparison between this values and the expected sent in the
#    feature file.
#
#    2. add a normal scenario to simulate the search of a client and verify that
#    exists into the client list (using the first has created before).

Feature: Customer search in product

    Scenario Outline: Search of a total priced for a list clients.
        Given I have a list of clients
          And I have a list of purchases
         When I search the client "<name>"
         Then I receive the total $<total>

        Examples:
            |         name |  id | total |
            | Alvaro Arias | E01 |   120 |
            |  Boris Bueno | E02 |  3400 |
            |  Carlos Cruz | E03 |   135 |
            |   Diego Diaz | E04 |  1230 |
            |   Erick Edul | E05 | 10000 |

    Scenario: Search of a client and verify that exists
        Given I have a list of clients
         When I check the client "Carlos Cruz"
         Then I receive a valid value

    Scenario: Search of a client and verify that exists
        Given I have a list of clients
         When I check the client "Federico Fernandez"
         Then I receive a null value

