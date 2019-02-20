from behave import *
from compare import expect

@given(u'I have ${balance:d} in my account')
def step_impl(context, balance):
    context.balance = balance


@when(u'I choose to withdraw the fixed amount of ${withdraw:d}')
def step_impl(context, withdraw):
    context.withdraw = withdraw


@then(u'I should receive ${cash:d} cash')
def step_impl(context, cash):
    expect(context.withdraw).to_equal(cash)
    print(f"This is your ${cash}")


@then(u'the Balance of my account should be ${balance:d}')
def step_impl(context, balance):
    expect(balance).to_equal(context.balance - context.withdraw)