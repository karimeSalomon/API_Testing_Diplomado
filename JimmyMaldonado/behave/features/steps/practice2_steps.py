@given(u'I go to \'{url}\'')
def step_impl(context, url):
    print("URL:", url)


@given(u'I click on {link} link')
def step_impl(context, link):
    print("LINK:", link)


@given(u'I have the user \'{username}\' created')
def step_impl(context, username):
    print("Username:", username)


@when(u'I fill \'{firstName}\' in First Name field')
def step_impl(context, firstName):
    print("Value for First Name:", firstName)


@when(u'I fill \'{lastName}\' in Last Name field')
def step_impl(context, lastName):
    print("Value for Last Name:", lastName)


@when(u'I fill \'{username}\' in Username field')
def step_impl(context, username):
    print("Value for Username:", username)


@when(u'I fill \'{password}\' in Password field')
def step_impl(context, password):
    print("Value for Password:", password)


@when(u'I fill \'{confirm}\' in Confirm field')
def step_impl(context, confirm):
    print("Value for Confirm:", confirm)


@when(u'I select \'{month}\' in Month dropdown')
def step_impl(context, month):
    print("Value for Month:", month)


@when(u'I fill \'{day:d}\' in Day field')
def step_impl(context, day):
    print("Value for Day:", day)


@when(u'I fill \'{year:d}\' in Year field')
def step_impl(context, year):
    print("Value for Year:", year)


@when(u'I select \'{gender}\' in Gender dropdown')
def step_impl(context, gender):
    print("Value for Gender:", gender)


@when(u'I fill \'{phone:d}\' in Mobile Phone field')
def step_impl(context, phone):
    print("Value for Gender:", phone)


@when(u'I fill \'{currentEmail}\' in Your current email address field')
def step_impl(context, currentEmail):
    print("Value for Your current email address:", currentEmail)


@when(u'I click on Save button')
def step_impl(context):
    print("Click on Save button!!")


@then(u'the message \'{message}\' is displayed')
def step_impl(context, message):
    print("Message:", message)