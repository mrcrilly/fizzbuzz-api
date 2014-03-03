Feature: The API can give me some FizzBuzz love

    Scenario: I can check an individual number for a result
        Given i provide the number "27"
        When i check this again the api
        Then i will get Fizz back

    Scenario: I can check a range for a result
        Given i provide the numbers "1" and "51"
        When i check this against the api
        Then i will get a range of results back

    Scenario: The API can handle invalid input
        Given i provide the letter "y"
        When i check this against the api
        Then i will get the correct http error code