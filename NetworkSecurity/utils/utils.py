from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging
import numpy as np
import pickle
import dill
import os, sys
import yaml


def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path,'rb') as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise NetworkSecurityException(e,sys)

def write_yaml(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'w') as f:
            yaml.dump(content,f)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    

def save_numpy_array_data(file_path: str, array: np.array) -> None:
    try:
      dir_name = os.path.dirname(file_path)
      os.makedirs(dir_name,exist_ok=True)

      with open(file_path,'wb') as file:
        np.save(file,array)  

    except Exception as e:
        raise NetworkSecurityException(e,sys)    

def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info('Entered into a save object utility function')
        os.makedirs( os.path.dirname(file_path), exist_ok=True )

        with open(file_path,'wb') as file:
            pickle.dump(obj,file)
        
        logging.info('Successfully saved the object')

    except Exception as e:
        raise NetworkSecurityException(e,sys)    
            