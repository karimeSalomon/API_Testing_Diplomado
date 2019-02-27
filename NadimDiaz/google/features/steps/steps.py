@given(u'Open a Web browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Open a Web browser')


@when(u'Go to "{link}"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Go to "https://www.google.com/"')


@then(u'Google logo is loaded properly')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Google logo is loaded properly')


@then(u'Input text is loaded properly')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Input text is loaded properly')


@then(u'"{buttonName}" button is loaded properly')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "Google Search" button is loaded properly')

@then(u'traslation elements are loaded properly')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then traslation elements are loaded properly')


@then(u'"{linkName}" link is loaded properly')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "Gmail" link is loaded properly')

@then(u'menu icon is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then menu icon is displayed')


@then(u'log in is enabled')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then log in is enabled')
