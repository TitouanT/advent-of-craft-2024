class SantaCommunicator:
    def __init__(self, number_of_days_to_rest):
        self.number_of_days_to_rest = number_of_days_to_rest

    def compose_message(self, reindeer_name, current_location, number_of_days_before_christmas):
        days_before_return = self._days_before_return(current_location, number_of_days_before_christmas)
        return f"Dear {reindeer_name}, please return from {current_location.name} in {days_before_return} day(s) to be ready and rest before Christmas."

    def is_overdue(self, reindeer_name, current_location, number_of_days_before_christmas, logger):
        if self._days_before_return(current_location, number_of_days_before_christmas) <= 0:
            logger.log(f"Overdue for {reindeer_name} located {current_location.name}.")
            return True
        return False

    def _days_before_return(self, current_location, number_of_days_before_christmas):
        return number_of_days_before_christmas - current_location.travel_time - self.number_of_days_to_rest
