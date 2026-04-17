Feature: StackOverflow Create Account Page

  Scenario: Create Account page loads with all required components
    Given user opens StackOverflow signup page
    Then signup form is fully loaded
    And social authentication options are available
    And legal links are present
