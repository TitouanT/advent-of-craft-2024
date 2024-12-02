from typing import Optional, Protocol

class FizzBuzzConfig(Protocol):
    min: int
    max: int
    fizzy_stuff: list[tuple[int, str]]

class Default_Fizz_Buzz_Config:
    min = 1
    max = 100
    fizzy_stuff = [
        (3, 'Fizz'),
        (5, 'Buzz'),
    ]

class Whiz_Bang_Config:
    min = 1
    max = 100
    fizzy_stuff = [
        (3, 'Fizz'),
        (5, 'Buzz'),
        (7, 'Whizz'),
        (9, 'Bang'),
    ]

class FizzBuzz:
    def __init__(self, config: FizzBuzzConfig = Default_Fizz_Buzz_Config):
        self.config = config

    def convert(self, input: int) -> Optional[str]:
        if self.is_out_of_range(input):
            return None
        else:
            return self.convert_safely(input)

    def convert_safely(self, input: int) -> str:
        matches = [name for divisor, name in sorted(self.config.fizzy_stuff) if FizzBuzz.is_divisible_by(divisor, input)]
        return ''.join(matches) or str(input)

    def is_out_of_range(self, input: int) -> bool:
        return not self.config.min <= input <= self.config.max

    @staticmethod
    def is_divisible_by(divisor: int, input: int) -> bool:
        return input % divisor == 0

