Feature: Target search results card validation

  Scenario: Every product result on a search page shows a name and an image
    Given user opens Target homepage
    When user searches for "coffee mug"
    Then every result on the search page has a product name and a product image
