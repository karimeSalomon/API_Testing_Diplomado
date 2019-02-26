# Suppose you create a feature file for a customer search

# 1. Add an scenario outline to simulate a search of a total priced for a list clients

# You should send the name of the client
# The ID of the client
# The Total priced of purchase

# On behind you should create a module with a dictionary containing the list of clients and the ID
# and another dictionary with the ID of the client and the Total_priced, to perform the comparison between this values and the expected sent in the feature file.

# 2. Add a normal scenario to simulate the search of a client and verify that exists into the client list(using the first has created before).

Feature:  Customer search
  As a cashier of the store
  I want to query for clients and its total priced
  in order to display the total priced by each client.

  Scenario Outline: Searching for the total priced for each asked client
    Given The <Client Name>
      And the <Client ID>
      And the <Total Priced> of purchase for each client
    When Asking for <Total Priced> by clients
    Then <Client Name> and its <Total Priced> are printed

    Examples:
    |Client Name|Client ID|Total Priced|
    |Jose       |1        |200         |
    |Roberto    |2        |350         |
    |Adrian     |3        |250         |
    |Mario      |4        |320         |
    |Elvis      |5        |1520        |
    |Tito       |6        |5000        |
    |Nair       |7        |1450        |
    |Raul       |8        |3000        |
    |Marco      |9        |1500        |
    |Fernando   |10       |450         |
