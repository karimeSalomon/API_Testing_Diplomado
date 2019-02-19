@given(u'I go to \'${url}\'')
def step_impl(context, url):
    print(url)


@given(u'I click on {link} link')
def step_impl(context, link):
    print(link)


@when(u'I fill "${value:w}" in First Name field')
def step_impl(context, value):
    print(value)


@when(u'I fill \'Perez\' in Last Name field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill \'Perez\' in Last Name field')


@when(u'I fill \'juan.perez\' in Username field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill \'juan.perez\' in Username field')


@when(u'I fill \'Control123\' in Password field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill \'Control123\' in Password field')


@when(u'I fill \'Control123\' in Confirm field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill \'Control123\' in Confirm field')


@when(u'I select \'December\' in Month dropdown')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select \'December\' in Month dropdown')


@when(u'I fill \'25\' in Day field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill \'25\' in Day field')


@when(u'I fill \'2000\' in Year field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill \'2000\' in Year field')


@when(u'I select \'Male\' in Gender dropdown')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select \'Male\' in Gender dropdown')


@when(u'I fill \'123456789\' in Mobile Phone field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I fill \'123456789\' in Mobile Phone field')


@when(u'I click on Save')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on Save')


@then(u'the message \'Your account was created successfully\' is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the message \'Your account was created successfully\' is displayed')