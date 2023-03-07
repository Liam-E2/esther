from pathlib import Path
import os
import logging
import configparser
import json

def get_project_root() -> Path:
    return Path(__file__).parent.parent


def configure_logs(logger_name: str, log_subfolder: str, logfile_name: str) -> logging.Logger:
    """
    Configures logs in /Esther/logs
    """
    log_root = str(get_project_root().joinpath('logs'))
    log_folder = os.path.join(log_root, log_subfolder)
    log_file = os.path.join(log_folder, logfile_name)

    if not os.path.exists(log_folder):
        os.makedirs(log_folder, exist_ok=True)

    # create logger with 'spam_application'
    logger = logging.getLogger(f'{logger_name}')
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(fh)

    return logger


def read_configs(config_path: str = None) -> dict:
    """
    Loads config file 
    """
    if config_path is None:
        with open(os.path.join(str(get_project_root()), 'esther_config.json'), 'r') as f:
            return json.load(f)

