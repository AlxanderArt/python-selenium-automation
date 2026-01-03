Feature: Test cases for Cart

  Scenario: User can see Empty Cart message
    Given Open Target main page
    When Click on cart icon
    Then Empty Cart message is shown
