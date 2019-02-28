from behave import *
from compare import expect

clients = {
    'Peterete': 1,
    'Torombolo': 2,
    'Crapulito': 3
}

prices = {
    1: 42,
    2: 30,
    3: 75
}

@given(u'a client with name {name}')
def step_impl(context, name):
    context.customer_id = clients[name]


@when(u'requesting the list of prices for that client')
def step_impl(context):
    context.price = prices[context.customer_id]


@then(u'the list of total price {price:d} is returned')
def step_impl(context, price):
    expect(context.price).to_equal(price)
    
@when(u'searching client by name {name}')
def step_impl(context, name):
    context.is_customer_found = (clients.get(name) != None)

    
@then(u'found is {is_found_literal}')
def step_impl(context, is_found_literal):
    is_found = (is_found_literal.lower() == 'true')
    expect(context.is_customer_found).to_equal(is_found)