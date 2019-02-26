import Clients_Priced as cp
import compare

@given(u'The {c_name}')
def step_impl(context, c_name):
    context.client_name = c_name

@given(u'the {c_id}')
def step_impl(context, c_id):
    context.client_id = c_id

@given(u'the {t_priced} of purchase for each client')
def step_impl(context, t_priced):
    context.total_priced = t_priced

@when(u'Asking for {total_priced} by clients')
def step_impl(context, t_priced):
    context.total_priced = t_priced

@then(u'<Client Name> and its <Total Priced> are printed')
def step_impl(context, c_name, t_priced):
    context
