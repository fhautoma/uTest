@use.chrome.browser

Feature: Create User
  the purpose of this test is to register new user n U_Test page


  Background: have at least browser installed

  Scenario: Create User in U_Test page
    Given a browser is used to load the URL "https://www.utest.com/"
    When make click in JoinToday button
    # Then fail if not found or pass if found the word "automation" on the google search page