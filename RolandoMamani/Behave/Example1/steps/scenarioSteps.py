import compare

@given(u'I have ${balance} in my account')
def step_impl(context, balance):
    context.balance = int(balance)

@when(u'I choose to withdraw the fixed amount of ${withdraw}')
def step_impl(context, withdraw):
    context.withdraw = int(withdraw)

@then(u'I should receive ${cash} cash')
def step_impl(context, cash):
    context.cash = int(cash)

@then(u'the balance of my account should be ${balance}')
def step_impl(context, balance):
    remaining = context.balance - context.withdraw
    compare.expect(remaining).to_equal(int(balance))
