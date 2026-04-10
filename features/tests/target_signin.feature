Feature: Target Sign In Flow

  Scenario: User navigates to sign in page
    Given user is on Target homepage
    When user opens account menu
    And user clicks sign in
    Then sign in page is displayed
