Feature: Add Product to Cart

  Scenario: User adds a product to the cart
    Given user opens Target homepage
    When user searches for "AAA batteries"
    And user opens the first search result
    And user adds the product to cart
    And user clicks the cart icon
    Then cart has at least 1 item
