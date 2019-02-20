@given(u'I insert {first_name:w} as first name')
def step_impl(context, first_name):
    print('first name inserted', first_name)


@given(u'I insert {last_name:w} as last name')
def step_impl(context, last_name):
    print('last name inserted', last_name)


@given(u'I insert {username:S} as username')
def step_impl(context, username):
    print('username inserted', username)


@given(u'I insert {password:S} as password')
def step_impl(context, password):
    print('password inserted', password)


@given(u'I insert {confirmation_password:S} as confirm password')
def step_impl(context, confirmation_password):
    print('confirmation password inserted', confirmation_password)


@given(u'I insert {month:S} {day:d} of {year:d} as birthday date')
def step_impl(context, day, month, year):
    print('birthday inserted', day, month, year)


@given(u'I insert {phone:d} as a mobile phone')
def step_impl(context, phone):
    print('mobile phone inserted', phone)


@given(u'I insert {email:S} as email address')
def step_impl(context, email):
    print('email inserted', email)


@when(u'I click on submit button')
def step_impl(context):
    print('first name inserted')


@then(u'An account with username as {username:S} is created')
def step_impl(context, username):
    print('google account created', username)


@then(u'An account with username as {username:S} is not created')
def step_impl(context, username):
    print('google account NOT created', username)
