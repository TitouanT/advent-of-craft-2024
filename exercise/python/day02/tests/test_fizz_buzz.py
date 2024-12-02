import unittest

from assertpy import assert_that

from games.fizz_buzz import FizzBuzz, Whiz_Bang_Config
from tests.ValidInput import ValidInput
class Custom_Config:
    def __init__(self, min, max, fizzy_stuff):
        self.min = min
        self.max = max
        self.fizzy_stuff = fizzy_stuff


class FizzBuzzTests(unittest.TestCase):
    def test_returns_its_numbers_representation(self):
        test_data = [
            ValidInput(1, "1"),
            ValidInput(67, "67"),
            ValidInput(82, "82"),
            ValidInput(3, "Fizz"),
            ValidInput(66, "Fizz"),
            ValidInput(99, "Fizz"),
            ValidInput(5, "Buzz"),
            ValidInput(50, "Buzz"),
            ValidInput(85, "Buzz"),
            ValidInput(15, "FizzBuzz"),
            ValidInput(30, "FizzBuzz"),
            ValidInput(45, "FizzBuzz")
        ]

        for data in test_data:
            with ((self.subTest(data=data))):
                assert_that(
                    FizzBuzz().convert(data.input)
                ).is_equal_to(data.expected_result)

    def test_fails_for_numbers_out_of_range(self):
        test_data = [0, -1, 101]

        for value in test_data:
            with self.subTest(value=value):
                assert_that(FizzBuzz().convert(value)).is_none()

    def test_whiz_bang_config(self):
        test_data = [
            ValidInput(1, "1"),
            ValidInput(67, "67"),
            ValidInput(82, "82"),
            ValidInput(3, "Fizz"),
            ValidInput(66, "Fizz"),
            ValidInput(99, "FizzBang"),
            ValidInput(5, "Buzz"),
            ValidInput(50, "Buzz"),
            ValidInput(85, "Buzz"),
            ValidInput(15, "FizzBuzz"),
            ValidInput(30, "FizzBuzz"),
            ValidInput(45, "FizzBuzzBang"),
            ValidInput(63, "FizzWhizzBang"),

            ValidInput(3*5, "FizzBuzz"),
            ValidInput(3*7, "FizzWhizz"),
            ValidInput(3*9, "FizzBang"),
            ValidInput(5*7, "BuzzWhizz"),
            ValidInput(3*5*2, "FizzBuzz"),
            ValidInput(3*7*2, "FizzWhizz"),
            ValidInput(3*9*2, "FizzBang"),
            ValidInput(5*7*2, "BuzzWhizz"),
        ]

        for data in test_data:
            with ((self.subTest(data=data))):
                assert_that(
                    FizzBuzz(Whiz_Bang_Config).convert(data.input)
                ).is_equal_to(data.expected_result)

    def test_custom_empty_config(self):
        min = 10
        max = 20
        test_data = [
            ValidInput(i, str(i))
            for i in range(min, max+1)
        ]
        cc = Custom_Config(min=min, max=max, fizzy_stuff=[])
        game = FizzBuzz(config=cc)
        for data in test_data:
            with ((self.subTest(data=data))):
                assert_that(
                    game.convert(data.input)
                ).is_equal_to(data.expected_result)

    def test_custom_config(self):
        min = 10
        max = 20
        test_data = [
            ValidInput(10, 'ab'),
            ValidInput(11, 'a'),
            ValidInput(12, 'abc'),
            ValidInput(13, 'a'),
            ValidInput(14, 'ab'),
            ValidInput(15, 'a'),
            ValidInput(16, 'abc'),
            ValidInput(17, 'a'),
            ValidInput(18, 'ab'),
            ValidInput(19, 'a'),
            ValidInput(20, 'abc'),

        ]
        cc = Custom_Config(min=min, max=max, fizzy_stuff=[
            (2, 'b'),
            (1, 'a'),
            (4, 'c'),
        ])
        game = FizzBuzz(cc)
        for data in test_data:
            with ((self.subTest(data=data))):
                assert_that(
                    game.convert(data.input)
                ).is_equal_to(data.expected_result)


if __name__ == "__main__":
    unittest.main()
