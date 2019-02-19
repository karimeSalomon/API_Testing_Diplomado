Feature:
  Dado que estoy en google realizando busquedas
  Como usuario
  Encuentro lo ingresado en el buscador

Scenario: Buscar pagina de  java en google

Given Dado que ingreso a un navegador
  And Ingreso al URL de google
  And Ingreso la palabra  java en el campo del buscador
When  Cuando hago click en el boton "buscar"
Then  Se despliega los resultados encontrados en el browser
  And Selecciono la url oficial
  And accedo a la pagina de java


Scenario: Buscar imagenes medianas en  google
Given Dado que estoy en el buscador de google buscando imagenes medianas
When  cuando realizo la accion buscar
  And selecciono la opcion solo imagenes medianas
Then  encuentro varis imagenes medianas

