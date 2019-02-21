

@given(u'I open www.google.com home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I open www.google.com home page')


@when(u'I write a English text in the search field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I write a English text in the search field')


@when(u'I press enter')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I press enter')


@then(u'A list of links related to text search are listed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then A list of links related to text search are listed')
