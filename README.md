# Data Science in Cyber — Phishing Detection Project

This repository contains a reproduction and critical evaluation of:

RimTouny / Phishing-Attack-Detection-using-Machine-Learning

## Project Description

The goal is to evaluate a machine-learning solution for phishing URL detection. The project reproduces the original methodology where possible and critically examines the claims, dataset, feature engineering, reproducibility, and evaluation metrics.

## Original Source

Original GitHub repository:
https://github.com/RimTouny/Phishing-Attack-Detection-using-Machine-Learning

## Dataset

The original project references:
- PhishStorm URL dataset
- ISCX-URL2016 dataset
- Kaggle malicious URL dataset

The final processed CSV is not included in the original GitHub repository. Place the recreated/obtained dataset here:

```text
data/data_features.csv
```

## How to Run

1. Create a Python environment.
2. Install dependencies:

```bash
pip install pandas numpy matplotlib scikit-learn
```

3. Put the processed CSV at:

```text
data/data_features.csv
```

4. Run:

```bash
jupyter notebook notebooks/phishing_detection_reproduction_starter.ipynb
```

## Outputs

The notebook saves metrics to:

```text
results/model_metrics.csv
```