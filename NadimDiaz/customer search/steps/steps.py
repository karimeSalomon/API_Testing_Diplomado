from compare import expect

@given(u'I have the client with name "{name:D}"')
def step_impl(context,name):
    idByName =	{
        "Nadim Diaz" : "0123",
        "Juan Perez" :"1234",
        "Maria Fuentes" :"2345"
    }
    if name in idByName:
        context.clientId = idByName.get(name)


@when(u'I perform the search')
def step_impl(context):
    pass


@then(u'The total priced should be "{totalprice:d}"')
def step_impl(context,totalprice):
    priceById =	{
        "0123": 200,
        "1234": 300,
        "2345": 400
    }
    total_price = False
    if context.clientId in priceById:
        total_price = priceById.get(context.clientId)
    
    expect(total_price).to_equal(totalprice)
    
    