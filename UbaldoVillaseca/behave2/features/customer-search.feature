Feature: Search
    Scenario Outline: Search total price for a list of clients
        Given a client with name <Name>
        When requesting the list of prices for that client 
        Then the list of total price <Price> is returned
        
    Examples:
    |Name|Price|
    |Peterete|42|
    |Torombolo|30|
    |Crapulito|75|
    
    Scenario: Search existing client
        When searching client by name Peterete
        Then found is True
        
    Scenario: Search inexisting client
        When searching client by name Dabadi
        Then found is False