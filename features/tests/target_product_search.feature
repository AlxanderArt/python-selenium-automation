Feature: Target Product Search

  Scenario Outline: User searches for a product on Target
    Given user opens Target homepage
    When user searches for "<term>"
    Then product results for "<term>" are shown

    Examples:
      | term          |
      | AAA batteries |
      | notebook      |
      | water bottle  |
