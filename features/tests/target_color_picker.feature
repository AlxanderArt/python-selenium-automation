Feature: Target product color swatch selection

  Scenario: Every color swatch on a multi-color product can be selected
    Given user opens the Target smocked blouse product page
    When user clicks every available color swatch
    Then every color reports as selected after its click
