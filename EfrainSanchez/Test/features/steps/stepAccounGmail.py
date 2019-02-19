@given(u'ingresar a la url {page:S}')
def step_impl(context,page):
    raise NotImplementedError(u'STEP: Given ingresar a la url https://accounts.google.com/signup')

@given(u'registrar con nombre: {nombres:D} con apellidos {apellidos:D}')
def step_impl(context,nombres,apellidos):
    raise NotImplementedError(u'STEP: Given registrar con nombre: Efrain con apellidos Sanchez Arispe')

@given(u'escoger un usuario {correo:S}')
def step_impl(context,correo):
    raise NotImplementedError(u'STEP: Given escoger un usuario aragon0302@gmail.com')

@given(u'crear un password con valor : {password}')
def step_impl(context,password):
    raise NotImplementedError(u'STEP: Given crear un password con valor : abc123456')

@given(u'confirmar password con valor: {password}')
def step_impl(context,password):
    raise NotImplementedError(u'STEP: Given confirmar password con valor: abc123456')

@given(u'ingresar fecha de nacimiento Mes: {month:D} , Dia: {day:d} , año: {year:d}')
def step_impl(context,month,day,year):
    raise NotImplementedError(u'STEP: Given ingresar fecha de nacimiento Mes: Febrero , Dia: 3 , año: 1988')

@given(u'Selecionar genero: {genero:D}')
def step_impl(context,genero):
    raise NotImplementedError(u'STEP: Given Selecionar genero: Masculino')

@given(u'Seleccionar el Pais: {pais:D} con numero: {numero:d}')
def step_impl(context,pais,numero):
    raise NotImplementedError(u'STEP: Given Seleccionar el Pais: Bolvia con numero: 69247572')

@given(u'ingresar su correo Gmail actual : {correo:S}')
def step_impl(context,correo):
    raise NotImplementedError(u'STEP: Given ingresar su correo Gmail actual : aragon0302@gmail.com')

@when(u'Clic en boton Registrar')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Clic en boton Registrar')


@then(u'como resultado usuario registrado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then como resultado usuario registrado')
