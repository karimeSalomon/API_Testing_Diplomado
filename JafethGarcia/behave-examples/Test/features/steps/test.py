from behave import *


@given(u'I insert my PIN')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I insert my PIN')


@given(u'I have $100 on my account')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have $100 in my account')


@when(u'I select withdrawal')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select withdrawal')


@when(u'I request $20')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I request $20')


@then(u'$20 should be dispensed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then $20 should be dispensed')


@then(u'the balance is 80$')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the balance is 80$')
