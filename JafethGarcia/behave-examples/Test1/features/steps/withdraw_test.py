from compare import expect


@given(u'I have ${amount:d} in my account')
def step_impl(context, amount):
    context.amount = amount


@when(u'I choose to withdraw the fixed amount of ${fixed_amount:d}')
def step_impl(context, fixed_amount):
    context.fixed_amount = fixed_amount


@then(u'I should receive ${cash:d} cash')
def step_impl(context, cash):
    print('This is your', cash)


@then(u'the balance of my account should be ${balance:d}')
def step_impl(context, balance):
    balance_calculated = context.amount - context.fixed_amount
    expect(balance).to_equal(balance_calculated)
