from communication.logger import Logger


class LoggerTest(Logger):
    def __init__(self):
        self.message = None

    def log(self, message):
        self.message = message

    def get_log(self):
        return self.message
