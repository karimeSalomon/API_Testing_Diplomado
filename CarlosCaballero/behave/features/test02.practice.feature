Feature: check de frontpage of google
Want to check that the components of the main google page are visible.

    Scenario: successful load for button "Iniciar sesión"
        Given the main google page is loaded
        When  the page has been fully loaded
        Then  its display the button "Iniciar sesión"

    Scenario: successful load for search text
        Given the main google page is loaded
        When  the page has been fully loaded
        Then  its display the text field for search

    Scenario: successful load for button "Buscar con Google"
        Given the main google page is loaded
        When  the page has been fully loaded
        Then  its display the button "Buscar con Google"

    Scenario: successful load for button "Me siento con suerte"
        Given the main google page is loaded
        When  the page has been fully loaded
        Then  its display the button "Me siento con suerte"

