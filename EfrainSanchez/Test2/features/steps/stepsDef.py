from compare import expect

@given(u'i have ${saldo:d} in my account')
def step_impl(context,saldo):
    context.balance = saldo


@when(u'i choose to withdraw the fixed amount of ${extracto}')
def step_impl(context,extracto):
    context.extracto = int(extracto)


@then(u'i should receive ${cash} cash')
def step_impl(context,cash):
    context.cash = int(cash)
    print("this is your $",context.cash)


@then(u'the balance of my account should be ${balance2:d}')
def step_impl(context,balance2):
    remaining = context.balance -context.extracto
    expect(remaining).to_equal(balance2)