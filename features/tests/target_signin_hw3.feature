Feature: Target Sign In Navigation (HW3)

  Scenario: Guest user navigates to sign in form from the right side menu
    Given user opens Target homepage
    When user opens account menu
    And user clicks Sign In from side menu
    Then Sign In form is opened
