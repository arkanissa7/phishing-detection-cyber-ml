"""
Preprocessing utilities for the phishing detection project.

The notebook remains the main implementation file.
This module contains reusable preprocessing functions based on the notebook.
"""

from pathlib import Path

import numpy as np
import pandas as pd


def load_dataset(dataset_path: str | Path) -> pd.DataFrame:
    """Load the phishing dataset from a CSV file."""
    dataset_path = Path(dataset_path)

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    return pd.read_csv(dataset_path)


def encode_target(data: pd.DataFrame, target_column: str = "status") -> pd.Series:
    """
    Encode the target labels into numeric values.

    legitimate -> 0
    phishing   -> 1
    """
    if target_column not in data.columns:
        raise ValueError(f"Target column '{target_column}' was not found.")

    encoded = data[target_column].map({
        "legitimate": 0,
        "phishing": 1
    })

    if encoded.isna().any():
        raise ValueError("Target column contains unexpected labels.")

    return encoded.astype(int)


def find_duplicate_columns(data: pd.DataFrame) -> list:
    """Return pairs of columns that contain exactly the same values."""
    hashes = {}
    duplicates = []

    for column in data.columns:
        column_hash = pd.util.hash_pandas_object(data[column], index=False).sum()

        if column_hash in hashes:
            for previous_column in hashes[column_hash]:
                if data[column].equals(data[previous_column]):
                    duplicates.append((previous_column, column))
            hashes[column_hash].append(column)
        else:
            hashes[column_hash] = [column]

    return duplicates


def prepare_feature_matrix(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series, dict]:
    """
    Prepare feature matrix X and target vector y.

    This function follows the same preprocessing logic used in the notebook:
    target encoding, removing raw URL/target columns, keeping numeric features,
    removing constant columns, removing duplicated features, and filling missing values.
    """
    data = data.copy()

    if "label" not in data.columns:
        data["label"] = encode_target(data, target_column="status")

    y = data["label"].astype(int)

    X = data.drop(columns=["url", "status", "label"], errors="ignore").copy()
    X = X.select_dtypes(include=[np.number])

    constant_columns = [
        column for column in X.columns
        if X[column].nunique(dropna=False) <= 1
    ]
    X = X.drop(columns=constant_columns)

    duplicate_pairs = find_duplicate_columns(X)
    duplicated_columns_to_remove = sorted({second for _, second in duplicate_pairs})
    X = X.drop(columns=duplicated_columns_to_remove, errors="ignore")

    X = X.fillna(X.median(numeric_only=True))

    preprocessing_info = {
        "constant_columns": constant_columns,
        "duplicated_columns_removed": duplicated_columns_to_remove,
        "final_feature_count": X.shape[1]
    }

    return X, y, preprocessing_info
