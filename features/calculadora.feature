Feature: calculadora

    Scenario Outline: Get sum total
        Given two numbers <values> to sum
        When the calc sum the values
        Then the sum is <total>
        Examples: values
            | values | total |
            | 7,4    | 11    |
            | 8,4    | 12    |
            | 100,20 | 120   |
            | -2,-5  | -7    |

    Scenario Outline: Get substract total
        Given two numbers <values> to substract
        When the calc substract the values
        Then the substract is <total>
        Examples: values
            | values | total |
            | 7,4    | 3     |
            | 8,0    | 8     |
            | 100,-2 | 102   |
            | -2,5   | -7    |

    Scenario Outline: Get product total
        Given two numbers <values> to product
        When the calc product the values
        Then the product is <total>
        Examples: values
            | values | total |
            | 7,4    | 28    |
            | 8,0    | 0     |
            | 100,-2 | -200  |
            | -2,5   | -10   |

    Scenario Outline: Get divide total
        Given two numbers <values> to divide
        When the calc divide the values
        Then the divide is <total>
        Examples: values
            | values | total          |
            | 10,2   | 5              |
            | 2,10   | 0.2            |
            | 100,-2 | -50            |
            | -50,-5 | 10             |
            | 5,0    | operationError |

    Scenario Outline: Get power total
        Given two numbers <values> to power
        When the calc power the values
        Then the power is <total>
        Examples: values
            | values | total    |
            | 0,2    | 0        |
            | 10,2   | 100      |
            | 2,0    | 1        |
            | 100,-2 | 0.0001   |
            | -5,-5  | -0.00032 |

    Scenario Outline: Get factorial total
        Given one number <values> to factorial
        When the calc factorial the value
        Then the factorial is <total>
        Examples: values
            | values | total          |
            | 0      | 1              |
            | 5      | 120            |
            | 10     | 3628800        |
            | -5     | operationError |