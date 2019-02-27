Feature: Search in Google
  test main page of google
  Scenario:
     As a google user
     I want to perform a search on Google on a specific language.
     So that I could found many references, information related to the search.
  Given I open www.google.com home page
  When I write a English text in the search field
    AND I press enter
  Then A list of links related to text search are listed

