import behave
from Clients_Priced import *

@given(u'the {c_name} as input parameter')
def step_impl(context, c_name):
    context.client_name = c_name

@given(u'the {c_id}')
def step_impl(context, c_id):
    context.client_id = c_id

@given(u'also given the {t_priced} of purchase for each client')
def step_impl(context, t_priced):
    context.total_priced = t_priced

@when(u'It is asked for {t_priced} by clients')
def step_impl(context, t_priced):
    context.total_priced = t_priced

@then(u'{c_name} and its {t_priced} are printed')
def step_impl(context, c_name, t_priced):
    print(context.client_name + "  has total priced: " str(return_total_priced(context.client_name)))

