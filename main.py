from NetworkSecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig, DataTransformationConfig
from NetworkSecurity.componnets.data_transformation import DataTransformation
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.componnets.data_validation import DataValidation
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
        logging.info('Initializing Data Validation')
        data_validation_config = DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,data_ingestion_artifact=artifacts)
        data_validation_artifacts = data_validation.initiate_data_validation()
        print(data_validation_artifacts)
        logging.info('Alhumdullillah DataValidation completed!')
        logging.info('Initializing the data transformation process')
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(data_transformation_config=data_transformation_config, data_validation_artifact=data_validation_artifacts)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info('Data Transformation is completed Alhumdullillah')
        print(f'Data Transformation artifact: {data_transformation_artifact} ')



    except Exception as e:
        raise NetworkSecurityException(e,sys)
