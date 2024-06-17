from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path



@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_X_path: Path
    train_y_path: Path
    test_X_path: Path
    test_y_path: Path
    model_name: str
    alpha: float
    l1_ratio: float

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_X_path: Path
    test_y_path: Path
    model_path: Path
    metric_file_name: Path
    all_params: dict
    metric_file_name: Path
    mlflow_uri: str