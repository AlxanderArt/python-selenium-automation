Feature: Target sign-in negative test (HW9)

  @requires_credentials
  Scenario: Wrong password shows an error on the sign-in page
    Given Open sign in page
    When user enters correct email
    And user clicks Continue
    And user enters incorrect password
    And user clicks Sign in with password
    Then sign-in error message is shown
