from textsummarizer.logging import logger
from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


STAGE_NAME = 'data Ingestion Stage'
try:
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} Started <<<<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} Completed <<<<<<\n\nx=============x')
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = 'data Validation Stage'
try:
    logger.info(f'>>>>>>>>>> stage {STAGE_NAME} Started <<<<<<<<<')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} Completed <<<<<<\n\nx=============x')
except Exception as e:
        logger.exception(e)
        raise e