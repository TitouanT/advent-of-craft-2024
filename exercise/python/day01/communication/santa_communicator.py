class SantaCommunicator:
    def __init__(self, number_of_days_to_rest):
        self.number_of_days_to_rest = number_of_days_to_rest

    def compose_message(self, reindeer, number_of_days_before_christmas):
        days_before_return = self._days_before_return(reindeer, number_of_days_before_christmas)
        return f"Dear {reindeer.name}, please return from {reindeer.location} in {days_before_return} day(s) to be ready and rest before Christmas."

    def is_overdue(self, reindeer, number_of_days_before_christmas, logger):
        if self._days_before_return(reindeer, number_of_days_before_christmas) <= 0:
            logger.log(f"Overdue for {reindeer.name} located {reindeer.location}.")
            return True
        return False

    def _days_before_return(self, reindeer, number_of_days_before_christmas):
        return number_of_days_before_christmas - reindeer.travel_time - self.number_of_days_to_rest
