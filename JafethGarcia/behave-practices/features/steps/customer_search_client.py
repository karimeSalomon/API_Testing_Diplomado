from compare import expect
from common import client, price


@given(u'I send the name {name} of a client')
def step_impl(context, name):
    context.name = name


@given(u'I send the id {id} of this client')
def step_impl(context, id):
    context.id = id


@when(u'I start searching for the client')
def step_impl(context):
    name = client.list.get(context.id)
    expect(name).to_equal(context.name)
    context.onDBName = name
    context.priced = price.list.get(context.id)


@then(u'I should get the price ${price:d}')
def step_impl(context, price):
    expect(price).to_equal(context.priced)


@then(u'The client should be found with same name as {name}')
def step_impl(context, name):
    expect(name).to_equal(context.onDBName)
