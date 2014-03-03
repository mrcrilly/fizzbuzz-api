Feature: Check if 3, 5 or 3 & 5 are factors of a given number

    Scenario: Factor of Three - I provide a valid number, I want to see a true reponse
        Given i pass the number "9"
        When i divide it by 3
        Then i will get true

    Scenario: Factor of Three - I provide an invalid number, I want to see a false response
        Given i pass the number "7"
        When i divide it by 3
        Then i will get false

    Scenario: Factor of Five - I provide a valid number, I want to see a true response
        Given i pass the number "15"
        When i divide it by 5
        Then i will get true

    Scenario: Factor of Five - I provide an invalid number, I want to see a false response
        Given i pass the number "17"
        When i divide it by 5
        Then i will get false

    Scenario: Factor of Three and Five: I provide a valid number, I get true
        Given i pass the number "15"
        When i divide it by 3 and 5
        Then i will get true

    Scenario: Factor of Three and Five: I provide an invalid number, I get false
        Given i pass the number "18"
        When i divide it by 3 and 5
        Then I will get false

    Scenario: Factor of Three and Five: I provide an invalid number, I get false
        Given i pass the number "20"
        When i divide it by 3 and 5
        Then I will get false

