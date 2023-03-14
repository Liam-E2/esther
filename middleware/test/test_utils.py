import pytest
import os
from src.utils import get_project_root, read_configs


def test_get_project_root():
    root = get_project_root()
    assert os.path.split(str(root))[1].lower() == 'esther'


def test_read_configs():
    config_data = read_configs()
    assert config_data.get('author') == 'Liam Earley'
