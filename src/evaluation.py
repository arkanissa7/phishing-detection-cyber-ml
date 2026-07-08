"""
Evaluation utilities for the phishing detection project.
"""

import numpy as np
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    fbeta_score,
    matthews_corrcoef,
    precision_score,
    recall_score,
    roc_auc_score
)


def get_prediction_scores(model, X_test):
    """Return prediction scores for ROC-AUC when available."""
    if hasattr(model, "predict_proba"):
        return model.predict_proba(X_test)[:, 1]

    if hasattr(model, "decision_function"):
        return model.decision_function(X_test)

    return None


def evaluate_model(model_name, model, X_train, X_test, y_train, y_test) -> dict:
    """Train and evaluate one classification model."""
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_score = get_prediction_scores(model, X_test)

    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

    return {
        "model": model_name,
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1": f1_score(y_test, y_pred, zero_division=0),
        "f2": fbeta_score(y_test, y_pred, beta=2, zero_division=0),
        "mcc": matthews_corrcoef(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_score) if y_score is not None else np.nan,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "tp": tp
    }


def evaluate_models(models: dict, X_train, X_test, y_train, y_test) -> pd.DataFrame:
    """Train and evaluate multiple models."""
    results = []

    for model_name, model in models.items():
        result = evaluate_model(
            model_name,
            model,
            X_train,
            X_test,
            y_train,
            y_test
        )
        results.append(result)

    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values("f1", ascending=False).reset_index(drop=True)

    return results_df
