Feature: Target Empty Cart

  Scenario: Empty cart message is shown when cart has no items
    Given user opens Target homepage
    When user clicks the cart icon
    Then empty cart message is displayed
