Feature: Verificar que carge la pagina principal de google
  Google es una compañía estadounidense fundada en septiembre de 1998
  cuyo producto principal es un motor de búsqueda creado por Larry Page y Sergey Brin
  Scenario: Verificar que carge el logo y el cuadro de busqueda
    Given la computadora tiene que tener internet
      And anotar https://www.google.com.bo en la url del navegador
    When precionar enter cuando el cursor esta en la url
    Then debe mostrar el logo de Google
      And debe mostrar el cuadro de texto de busqueda
      And no debe tardar menos de 30 Segundos en cargar

  Scenario: Buscar en Google cuando introdusca un texto en cuadro de busqueda
    Given La computadora tiene que tener internet
      And anotar https://www.google.com.bo en la url del navegador
      And precionar enter cuando el cursor en el navegador
      And introducir un texto en el cuadro de texto de busqueda de Google
    When presionar click en el boton de Buscar con Google
    Then debe mostrar una lista de enlaces referente al texto introducido


