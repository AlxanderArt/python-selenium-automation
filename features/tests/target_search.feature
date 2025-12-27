# Created by lana at 12/27/25
Feature: Tests for search

  Scenario: User can search for a tea on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown

  Scenario: User can search for a book on Target
    Given Open Target main page
#    When Search for tea
#    Then Search results for tea are shown

