Feature: The API can give me some FizzBuzz love

    Scenario: I can check an individual number for a result
        Given i provide the number "27"
        When i check this against the api
        Then i will get "Fizz" back

    Scenario: I can check a range for a result
        Given i provide the numbers "1" and "51"
        When i check these against the api
        Then i will get a list back "50" in length

    Scenario: The API can handle invalid input
        Given i provide the number "y"
        When i check this against the api
        Then i will get the correct http error code

    Scenario: The API will max out at a high of 1001
        Given i provide the numbers "1" and "1005"
        When i check these against the api
        Then i will get a list back "1000" in length