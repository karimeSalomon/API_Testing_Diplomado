from compare import expect


customer_list = {1: "Juan", 2: "Pepe", 3: "Maira", 4: "Rene", 5: "Ana"}
customer_price = {1: 100, 2: 200, 3: 500, 4: 150, 5: 88}


@when(u'I send {id:d} as id of client')
def step_impl(context, id):
    context.id = id


@then(u'I should see name:{name} and total priced:{price:d}')
def step_impl(context, name, price):
    saved_price = customer_price[context.id]
    saved_name = customer_list[context.id]

    expect(price).to_equal(saved_price)
    expect(name).to_equal(saved_name)
