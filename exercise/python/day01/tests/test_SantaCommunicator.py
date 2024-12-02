import unittest

from assertpy import assert_that

from communication.santa_communicator import SantaCommunicator
from communication.reindeer import Reindeer
from tests.doubles.logger import LoggerTest


class SantaCommunicatorTest(unittest.TestCase):
    def setUp(self):
        self.number_of_days_to_rest = 2
        self.number_of_day_before_christmas = 24
        self.logger = LoggerTest()
        self.communicator = SantaCommunicator(self.number_of_days_to_rest)

    def test_compose_message(self):
        reindeer = Reindeer(name="Dasher", location="North Pole", travel_time=5)
        message = self.communicator.compose_message(reindeer, self.number_of_day_before_christmas)
        assert_that(message).is_equal_to(
            "Dear Dasher, please return from North Pole in 17 day(s) to be ready and rest before Christmas."
        )

    def test_is_overdue_detect_overdue_reindeer(self):
        reindeer = Reindeer(name="Dasher", location="North Pole", travel_time=self.number_of_day_before_christmas)
        overdue = self.communicator.is_overdue(
            reindeer,
            self.number_of_day_before_christmas,
            self.logger
        )
        assert_that(overdue).is_true()
        assert_that(self.logger.get_log()).is_equal_to("Overdue for Dasher located North Pole.")

    def test_is_overdue_return_false_when_not_overdue(self):
        reindeer = Reindeer(
            name="Dasher",
            location="North Pole",
            travel_time=self.number_of_day_before_christmas - self.number_of_days_to_rest - 1
        )
        overdue = self.communicator.is_overdue(
            reindeer,
            self.number_of_day_before_christmas,
            self.logger
        )
        assert_that(overdue).is_false()


if __name__ == "__main__":
    unittest.main()
