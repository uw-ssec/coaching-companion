import yaml
import pytest

class TestYamlLoader:
    
    def __init__(self) -> None:
        pass
    
    @pytest.fixture
    def load_yaml(file_path):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)