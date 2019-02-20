@given(u'I go to \'{url}\'')
def step_impl(context, url):
    print("URL:", url)


@given(u'I click on \'{link}\' link')
def step_impl(context, link):
    print("Link:", link)


@when(u'I fill \'{value}\' in \'{field}\' field')
def step_impl(context, value, field):
    print("Field:", field, "Value: ", value)


@when(u'I select \'{value}\' in \'{dropdown}\' dropdown')
def step_impl(context, value, dropdown):
    print("Dropdown:", dropdown, "Value: ", value)


@when(u'I click on \'{buttonName}\' button')
def step_impl(context, button):
    print("Button:", button)


@then(u'the message \'{message}\' is displayed')
def step_impl(context, message):
    print("Message:", message)