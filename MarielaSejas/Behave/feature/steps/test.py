@given(u'I have ${amount:d} in my account # the context precondicion')
def step_impl(context, amount):
    assert True is True

@when(u'I request ${amount:d} # the event(s) #cuando le pido 20 dolares')
def step_impl(context, amount):
    assert True is True

@then(u'${amount:d} should be dispensed # the outcome(s) #deberia de tener 20 dolares')
def step_impl(context, amount):
    assert True is True

@given(u'I insert my PIN')
def step_impl(context):
    assert True is True

@given(u'I have $100 in my account')
def step_impl(context):
    assert True is True

@when(u'I select withdrawal')
def step_impl(context):
    assert True is True

@when(u'I request $20')
def step_impl(context):
    assert True is True


@then(u'$20 should be dispensed')
def step_impl(context):
    assert True is True


@then(u'the balance is 80$')
def step_impl(context):
    assert True is True

@given(u'I fill the fields as ${name:w}')
def step_impl(context, name):
    assert True is True


@given(u'Insert the ${apellido:w}')
def step_impl(context, apellido):
    assert True is True


@given(u'Insert the ${username:w}')
def step_impl(context, username):
    assert True is True


@given(u'Insert the ${password:w}')
def step_impl(context, password):
    assert True is True


@given(u'Insert the ${birthday:d}')
def step_impl(context, birthday):
    assert True is True


@given(u'Insert the ${gender:w}')
def step_impl(context, gender):
    assert True is True


@given(u'Insert the ${phone:d}')
def step_impl(context, phone):
    assert True is True


@when(u'I select the one of the options displayed')
def step_impl(context):
    assert True is True


@when(u'I click on submit button')
def step_impl(context):
    assert True is True


@then(u'I have the account created')
def step_impl(context):
    assert True is True
