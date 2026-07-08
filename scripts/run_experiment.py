"""
Optional script for running the phishing detection experiment.

The notebook is still the main implementation file.
This script provides a simple reproducible command-line entry point.
"""

from pathlib import Path
import sys

from sklearn.model_selection import train_test_split


# Make sure the project root is available for importing from src/
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.preprocessing import load_dataset, prepare_feature_matrix
from src.models import get_models
from src.evaluation import evaluate_models


RANDOM_STATE = 42


def main():
    """Run preprocessing, train models, evaluate them, and save results."""
    dataset_path = PROJECT_ROOT / "data" / "dataset_phishing.csv"
    results_dir = PROJECT_ROOT / "results"
    results_dir.mkdir(exist_ok=True)

    print("Loading dataset...")
    data = load_dataset(dataset_path)

    print("Preparing feature matrix...")
    X, y, preprocessing_info = prepare_feature_matrix(data)

    print("Preprocessing info:")
    print(preprocessing_info)

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=RANDOM_STATE,
        stratify=y
    )

    print("Training and evaluating models...")
    models = get_models(random_state=RANDOM_STATE)
    results_df = evaluate_models(models, X_train, X_test, y_train, y_test)

    output_path = results_dir / "model_metrics_from_script.csv"
    results_df.to_csv(output_path, index=False)

    print("Experiment completed.")
    print(f"Results saved to: {output_path}")
    print(results_df)


if __name__ == "__main__":
    main()
