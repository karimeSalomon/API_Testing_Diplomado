from compare import expect
from data import clients
from data import prices


@given(u'I get the id of client searching by "{client_name}" name')
def step_impl(context, client_name):
    for client_id, name in clients.clients_list.items():
        if name == client_name:
            context.client_id = client_id
            break


@when(u'I search the id on price list')
def step_impl(context):
    context.price_from_client = prices.prices_list[context.client_id]


@then(u'the price is {expected_price:g}')
def step_impl(context, expected_price):
    expect(expected_price).to_equal(context.price_from_client)
