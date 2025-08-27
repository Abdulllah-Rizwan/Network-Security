from NetworkSecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.componnets.data_ingestion import DataIngestion
from NetworkSecurity.logging.logger import logging
import sys

if __name__ == '__main__':
    try:
        logging.info('Entering try block to initiate data ingestion')
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(config=data_ingestion_config)
        artifacts = data_ingestion.initiate_data_ingestion()
        print(artifacts)
        logging.info('Data Ingestion executed successfully')
    except Exception as e:
        raise NetworkSecurityException(e,sys)
