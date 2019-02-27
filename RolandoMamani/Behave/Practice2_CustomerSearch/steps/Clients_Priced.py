"""
# Suppose you create a feature file for a customer search

# 1. Add an scenario outline to simulate a search of a total priced for a list clients

# You should send the name of the client
# The ID of the client
# The Total priced of purchase

# On behind you should create a module with a dictionary containing the list of clients and the ID
# and another dictionary with the ID of the client and the Total_priced, to perform the comparison between this values and the expected sent in the feature file.

# 2. Add a normal scenario to simulate the search of a client and verify that exists into the client list(using the first has created before).
"""

clients = {'Jose': 1, 'Roberto': 2,'Adrian': 3,'Mario': 4,'Elvis': 5,'Tito': 6,'Nair': 7,'Raul': 8,'Marco': 9,'Fernando': 10}
total_priced = {1: 200, 2: 350, 3: 250, 4: 320, 5: 1520, 6: 5000, 7: 1450, 8: 3000, 9: 1500, 10: 450}

def return_total_priced(name):
    return total_priced[clients[name]]
