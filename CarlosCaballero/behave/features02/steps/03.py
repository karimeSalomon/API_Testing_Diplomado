from data.clients import clients,purchases

@given(u'I have a list of ${data}')
def step_impl(context,data):
    if 'data' in context:
        context.data = {}
    if data not in context.data:
        if data == 'clients':
            context.data['clients'] = clients()
        elif data == 'purchases':
            context.data['purchases'] = purchases()

@when(u'I search the client "${name}"')
def step_impl(context,name):
    context.name = name

@then(u'I receive the total $${total:d}')
def step_impl(context,total):
    pass

@when(u'I check the client "${name}"')
def step_impl(context,name):
    pass

@then(u'I receive a ${type} value')
def step_impl(context,type):
    pass

