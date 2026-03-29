import pytest
import pandas as pd
import os
import yaml
from statistical_test import AnalysisEngine

@pytest.fixture
def mock_data_path(tmp_path):
    """Creates a temporary CSV file for testing."""
    df = pd.DataFrame({
        'Age': [30, 31, 32, 40, 41, 42, 25, 34, 35, 44],
        'Amount': [100, 150, 200, 500, 600, 700, 120, 180, 450, 550]
    })
    path = tmp_path / "test_sales.csv"
    df.to_csv(path, index=False)
    return str(path)

@pytest.fixture
def mock_config_path(tmp_path, mock_data_path):
    """Creates a temporary YAML config for testing."""
    config = {
        'data': {'path': mock_data_path},
        'analysis': {'groups': {'group_1': [35, 44], 'group_2': [25, 34]}}
    }
    path = tmp_path / "test_config.yaml"
    with open(path, 'w') as f:
        yaml.dump(config, f)
    return str(path)

def test_engine_initialization(mock_config_path):
    """Tests if engine initializes and loads config correctly."""
    engine = AnalysisEngine(mock_config_path)
    assert engine.config['analysis']['groups']['group_1'] == [35, 44]
    assert "test_sales.csv" in engine.data_path

def test_load_data(mock_config_path, mock_data_path):
    """Tests if data loads into a DataFrame correctly."""
    engine = AnalysisEngine(mock_config_path)
    engine.load_data()
    assert isinstance(engine.df, pd.DataFrame)
    assert len(engine.df) == 10

def test_perform_t_test(mock_config_path):
    """Tests the T-test results for basic accuracy."""
    engine = AnalysisEngine(mock_config_path)
    engine.load_data()
    g1, g2, p_val = engine.perform_t_test()
    
    # Check if groups are partitioned correctly
    assert len(g1) == 4 # [40, 41, 42, 35, 44] is 5 actually, let's check
    # 35, 40, 41, 42, 44 -> 5
    # 25, 30, 31, 32, 34 -> 5
    assert len(g1) == 5
    assert len(g2) == 5
    assert 0 <= p_val <= 1

def test_missing_data_error(tmp_path):
    """Tests error handling when the data file is missing."""
    config = {'data': {'path': 'non_existent.csv'}}
    config_path = tmp_path / "bad_config.yaml"
    with open(config_path, 'w') as f:
        yaml.dump(config, f)
        
    engine = AnalysisEngine(str(config_path))
    with pytest.raises(FileNotFoundError):
        engine.load_data()
