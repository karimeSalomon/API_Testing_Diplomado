from compare import expect
from data.clients import clients,purchases

@given(u'I have a list of {data:w}')
def step_impl(context,data):
    if data == 'clients':
        context.clients = clients()
    elif data == 'purchases':
        context.purchases = purchases()

@when(u'I search the client "{name}"')
def step_impl(context,name):
    context.name = name

@when(u'I check the client "{name}"')
def step_impl(context,name):
    context.name = name

@then(u'I receive the total ${total:d}')
def step_impl(context,total):
    code = None

    for key,name in context.clients.items():
        if name == context.name:
            code = key

    if code is None:
        expect(total).to_be_none()
        pass
    else:
        expect(total).to_equal(context.purchases[code])

@then(u'I receive a {type:w} value')
def step_impl(context,type):
    code = None

    for key,name in context.clients.items():
        if name == context.name:
            code = key

    if type == 'null':
        expect(code).to_be_none()
    elif type == 'valid':
        expect(code).to_be_truthy()
    else:
        expect(True).to_equal(False)

