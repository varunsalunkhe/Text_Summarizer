from text_Summarizer.config.configuration import ConfigurationManager
from text_Summarizer.conponents.model_evalution import ModelEvaluation
from text_Summarizer.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()