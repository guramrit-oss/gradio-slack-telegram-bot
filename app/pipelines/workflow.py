class Workflow:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def run(self, input_data):
        output_data = input_data
        for step in self.steps:
            output_data = step.execute(output_data)
        return output_data