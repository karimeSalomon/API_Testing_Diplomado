from compare import expect
from dictionaries import clients_list, price_list

@given(u'A Search a client {client_name}')
def step_impl(context, client_name):
    context.client_name = client_name


@given(u'I set the client {id}')
def step_impl(context, id):
   context.id = id


@when(u'I search the client')
def step_impl(context):
   client_name = clients_list.list.get(context.id)
   expect(client_name).to_equal(context.price)
   context.dictionary = client_name
   context.price = price_list.get(context.id)


@then(u'I get the price $<price> for the specific client')
def step_impl(context, price):
    expect(price).to.equal(context.price)


@then(u'I get the same client found which is {client_name}')
def step_impl(context, client_name):
    expect(client_name).to.equal(context.dictionary)

