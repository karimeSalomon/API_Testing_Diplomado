@given(u'I go to gmail')
def step_impl(context):
    pass


@given(u'I click on Create Account button')
def step_impl(context):
    pass


@when(u'I fill "{field_name}" text field with "{value:w}" value')
def step_impl(context, field_name, value):
    pass


@when(u'I fill {field_name}" date field with "{month:w}/{day:d}/{year:d}" value')
def step_impl(context, field_name, month, day , year):
    pass


@when(u'I select "{field_name}" select field with "{value:S}" value')
def step_impl(context, field_name, value):
    pass


@when(u'I fill "{field_name}" number field with "{value:d}" value')
def step_impl(context, field_name, value):
    pass


@when(u'I fill "{field_name}" email field with "{value:S}" value')
def step_impl(context, field_name, value):
    pass
