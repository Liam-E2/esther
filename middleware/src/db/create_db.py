#!/usr/bin/env python3
import sqlite3
import sys
import os
import traceback
import logging
import pathlib

from src.utils import get_project_root


def create_songs_table(db_name) -> int:
    """
    Create sqlite3 table to hold songs data from phish.net api
    """




def create_database(db_name: str) -> int:
    """
    Function to create esther database
    """
    root_path = get_project_root()
    try:
        if not os.path.exists(root_path.joinpath(db_name)):
            sqlite3.connect(os.path.join(str(root_path), db_name))
    
    except Exception as e:
        pass

    return 0
