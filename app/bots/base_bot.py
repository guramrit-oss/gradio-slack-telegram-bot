from abc import ABC, abstractmethod


class BaseBot(ABC):
    def __init__(self, processor):
        self.processor = processor
        self.running = False

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def process_message(self, message):
        pass

    def is_running(self):
        return self.running