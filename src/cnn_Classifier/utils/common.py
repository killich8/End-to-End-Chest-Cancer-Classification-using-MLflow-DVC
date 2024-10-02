import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded succefully")
            return Configbox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args: 
        path_to_directories (list): list of path of directories 
        ignore_log (bool, optional): ignore if multiple of dirs to be created. Defaults to False. 
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """saves json data

    Args: 
        path (Path): path to json file
        data (dict): data to be saved in json file    
    """
    with open(path,"w") as f:
        json.dump(data, f, indent=4)


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file data
     
    Args:
        path (Path): path to json file

    Returns:
         ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content=json.load(f)

    logger.info(f"json file is loaded succesfully from: {path}")


@ensure_annotations
def load_bin(path:Path) -> Any:
    """save binary file

    Args:
        path (Path): path to the binary file 

    Returns:
        Any: object stored in the file
    """
    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path to the file

    Returns:
         str: size in KB
    """
    size_in_kb= round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def decodeImage(imgstring, filename):
    imgdata= base64.b64decode(imgstring)
    with open(filename,"wb") as f:
        f.write(imgdata)
        f.close()


@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64decode(f.read())


  

