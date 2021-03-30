@use.chrome.browser

Feature: Create User
  the purpose of this test is to register new user n U_Test page


  Background: have at least browser installed

  Scenario: Create User in U_Test page
    Given a browser is used to load the URL "https://www.utest.com/"
    When make click in JoinToday button
    Then wait until user form page loads
    When fill user fields in form
    Then click in next button
    Then click in next button in address page



