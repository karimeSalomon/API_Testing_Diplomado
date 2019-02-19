
@given(u'I have {amount} in my account')
def step_impl(context, amount):
    raise NotImplementedError(u'STEP: Given I have $100 in my account')


@when(u'I request $20 # the event(s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I request $20')


@then(u'$20 should be dispensed # the outcome(s)')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then $20 should be dispensed')

