Feature: Crear una nueva cuenta GMAIL
  Gmail es un servicio de correo electrónico gratuito proporcionado por la
  empresa estadounidense Google, Inc a partir del 1 de abril de 2004.
  Tras más de cinco años, el 7 de julio de 2009, el servicio de Gmail,
  junto con Google Calendar, Google Docs (ahora integrado en Google Drive),
  Hangouts y Google Buzz (cerrado), dejaron su calidad de Beta y pasaron a
  ser considerados productos terminados
  Scenario: Que permita registrar con datos no numericos en los campos de Name
    Given ingresar a la url https://accounts.google.com/signup
    And registrar con nombre: Efrain con apellidos Sanchez Arispe
    And escoger un usuario aragon0302@gmail.com
    And crear un password con valor : abc123456
    And confirmar password con valor: abc123456
    And ingresar fecha de nacimiento Mes: Febrero , Dia: 3 , año: 1988
    And Selecionar genero: Masculino
    And Seleccionar el Pais: Bolvia con numero: 69247572
    And ingresar su correo Gmail actual : aragon0302@gmail.com

    When Clic en boton Registrar
    Then como resultado usuario registrado


