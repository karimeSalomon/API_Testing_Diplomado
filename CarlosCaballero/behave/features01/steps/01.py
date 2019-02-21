@given(u'I insert my PIN')
def step_impl(context):
    pass

@given(u'I have ${amount:d} in my Account')
def step_impl(context,amount):
    print('amount:',amount)

@when(u'I select withdrawal')
def step_impl(context):
    pass

@when(u'I request ${cash}')
def step_impl(context,cash):
    pass

