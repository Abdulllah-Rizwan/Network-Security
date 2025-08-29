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
    
            