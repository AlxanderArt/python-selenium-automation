Feature: Amazon Sign In Page Validation

  Scenario: Verify all sign-in page elements are present
    Given user is on Amazon sign in page
    Then all primary elements are visible
    And all secondary elements are visible
