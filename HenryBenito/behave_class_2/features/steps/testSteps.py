from compare import expect


@given(u'I have ${amount:d} in my account')
def step_impl(context, amount):
    context.amount = amount


@when(u'I choose to withdraw the fixed amount of ${withdraw:d}')
def step_impl(context, withdraw):
    context.withdraw = withdraw


@then(u'I should receive ${cash:d} cash')
def step_impl(context, cash):
    context.cash = cash
    expect(context.withdraw).to_equal(context.cash)
    print("This is your $", context.cash)

@then(u'the balance of my account should be ${balance:d}')
def step_impl(context, balance):
    remaining = context.amount - context.withdraw
    expect(remaining).to_equal(balance)
