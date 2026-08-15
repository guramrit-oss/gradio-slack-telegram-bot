from abc import ABC, abstractmethod

class Step(ABC):
    @abstractmethod
    def execute(self, data):
        pass

class ExampleStep(Step):
    def execute(self, data):
        # Example processing logic
        return data + " processed by ExampleStep"

class AnotherStep(Step):
    def execute(self, data):
        # Another processing logic
        return data + " processed by AnotherStep"