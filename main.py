from cnnClassifier import logger 
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 

"""
    Data ingestion stage 📥
"""
STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} Completer <<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e

