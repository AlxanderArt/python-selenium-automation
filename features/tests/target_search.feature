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

#  Scenario Outline: Login error shown for invalid login
#    Given Open login page
#    When Enter login username <username>
#    And Enter login password <password>
#    Then Verify login error message <err_message>
#    Examples:
#    |username  |password        |err_message             |
#    |non_exist |password122     |this account not found  |
#    |user123   |incorrect_pass  |this password is not correct  |



