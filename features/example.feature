Feature: Reproducible example of hanging test

  Scenario: Run a non hanging test
    Given we have behave installed
     When we run a test
     Then the test is completed

  Scenario: Run a hanging test
    Given we run a test that exits
     Then we never reach here
