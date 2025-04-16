from dataclasses import dataclass
from pathlib import Path

# data ingestion 
@dataclass(frozen=True)
class DataIngestionConfig:
    """
        @dataclass
            Auto-creates constructor, makes code clean 🧼
        frozen=True
            Makes the class read-only 🔒 (no changes allowed after creation)
            Perfect for configs/settings 📁✅
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# base model 
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int


# training 
@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list


# Evaluation 
@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int