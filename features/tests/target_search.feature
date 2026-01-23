Feature: Tests for search

  Scenario: User can search for a tea on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown

#  Scenario: User can search for a mug on Target
#    Given Open Target main page
#    When Search for mug
#    Then Search results for mug are shown

  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <product>
    Then Search results for <product_result> are shown
    Examples:
    |product  |product_result   |
    |tea      |tea              |
    |mug      |mug              |
    |coffee   |coffee           |

  Scenario: Verify that user can see product names and images
    Given Open Target main page
    When Search for AirPods
    Then Verify that every product has a name and an image

  Scenario: User can see favorites tooltip for search results
    Given Open Target main page
    When Search for tea
    And Hover favorites icon
    Then Favorites tooltip is shown
