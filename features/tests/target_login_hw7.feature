Feature: Target Login (HW7 bonus)

  @requires_credentials
  Scenario: Registered user signs in with email and password
    Given user opens Target homepage
    When user opens account menu
    And user clicks Sign In from side menu
    And user enters email and password
    And user submits the sign-in form
    Then user is signed in
