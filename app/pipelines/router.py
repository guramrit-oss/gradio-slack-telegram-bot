from app.pipelines.base import Pipeline

class Router:
    def __init__(self):
        self.pipelines = {}

    def register_pipeline(self, source, pipeline):
        self.pipelines[source] = pipeline

    def route(self, source, message):
        if source in self.pipelines:
            pipeline = self.pipelines[source]
            return pipeline.process(message)
        else:
            raise ValueError(f"No pipeline registered for source: {source}")