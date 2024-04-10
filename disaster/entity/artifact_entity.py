from dataclasses import dataclass


# Data ingestion artifacts
@dataclass
class DataIngestionArtifacts:
    data_file_path: str
    # test_data_file_path: str


@dataclass
class DataTransformationArtifacts:
    transformed_data_path: str