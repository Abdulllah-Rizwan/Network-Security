import NetworkSecurity
from NetworkSecurity.constants.training_pipeline import TARGET_COLUMN, DATA_TRANSFORMATION_IMPUTER_PARAMS
from NetworkSecurity.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact
from NetworkSecurity.utils.utils import save_numpy_array_data,save_object
from NetworkSecurity.entity.config_entity import DataTransformationConfig
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
import sys, os


class DataTransformation:
    def __init__(
        self,
        data_validation_artifact: DataValidationArtifact,
        data_transformation_config: DataTransformationConfig
        ):
            try:
                self.data_validation_artifact = data_validation_artifact
                self.data_transformation_config = data_transformation_config
            except Exception as e:
                raise NetworkSecurityException(e,sys)
    
    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def get_data_transformer_obj(cls) -> Pipeline:
        logging.info('Entered into data transformer object')
        try:
            imputer: KNNImputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)

            logging.info(f'Initialized KKNImputer with: {imputer}')
            
            processor: Pipeline = Pipeline([('imputer',imputer)])

            return processor
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            logging.info('Entered into the initiate data transformation block')
            
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)    
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)

            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1,0)

            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1,0)

            preprocessor = self.get_data_transformer_obj()

            preprocessor_obj = preprocessor.fit(input_feature_train_df)

            transformed_input_feature_train_df = preprocessor_obj.transform(input_feature_train_df)
            transformed_input_test_feature = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[transformed_input_feature_train_df, np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_test_feature, np.array(target_feature_test_df)]

            save_numpy_array_data(
                self.data_transformation_config.transformed_train_file_path,
                train_arr
                )
            
            save_numpy_array_data(
                self.data_transformation_config.transformed_test_file_path,
                test_arr
            )

            save_object(
                self.data_transformation_config.transformed_object_file_path,
                preprocessor_obj
            )

            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_file_path = self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path = self.data_transformation_config.transformed_test_file_path,
                transformed_object_file_path = self.data_transformation_config.transformed_object_file_path
            )

            return data_transformation_artifact
        
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
