@smoke @fast @ui
Feature: Target Help center dropdown navigation (HW9)

  Scenario: User picks Promotions and Coupons from the help dropdown
    Given Open Help page for Returns
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened

  Scenario: User picks Target Circle from the help dropdown
    Given Open Help page for Returns
    When Select Help topic Target Circle™
    Then Verify help About Target Circle page opened
