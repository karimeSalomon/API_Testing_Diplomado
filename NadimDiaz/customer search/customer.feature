Feature: Client search for total price

Scenario Outline: Verify is possible for a client search total priced

    Given I have the client with name <Client>
    When I perform the search
    Then The total priced should be <Total_Price>

    Examples:
	| Client | Total_Price |
	| "Nadim Diaz"     | "200"           |
	| "Juan Perez"     | "300"          |
	| "Maria Fuentes"     | "400"          |
