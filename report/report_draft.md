# Phishing Attack Detection using Machine Learning — Report Draft

## Executive Summary

This project critically evaluates the GitHub tutorial/repository **Phishing Attack Detection using Machine Learning** by RimTouny. The selected source addresses a binary cybersecurity classification problem: deciding whether a URL is phishing or benign. The original project uses a large URL feature dataset and trains multiple machine-learning models.

The reproduction study focuses not only on model performance but also on whether the author's claims are supported by the available code, data, and evaluation methodology. A major finding at the beginning of the reproduction is that the final processed dataset is not included in the repository, and the notebook loads it from a local Windows path. This creates a reproducibility limitation and suggests that some preprocessing steps may be hidden.

## 1. Summary of the Source

### Problem
Phishing attacks attempt to deceive users into visiting malicious websites and submitting sensitive information. The project tries to detect phishing URLs automatically.

### Why the Problem Is Important
In phishing detection, a false negative can allow a malicious URL to reach a user, while a false positive can block legitimate access. Therefore, evaluation must consider precision, recall, F1, MCC, ROC-AUC, and confusion matrices, not only accuracy.

### Proposed Solution
The author proposes extracting lexical/statistical URL features and training classification models to distinguish phishing URLs from benign URLs.

### Dataset
The original README states that the dataset combines:
- PhishStorm URL dataset
- ISCX-URL2016 dataset
- Malicious URL dataset from Kaggle

The processed notebook output shows approximately 737,032 rows and 26 columns.

### Models / Methodology
The original project uses LazyClassifier and several ML models, plus ensemble methods such as stacking and voting.

## 2. Critical Evaluation

### Main Claims
The author claims that the project advances phishing defense using ML models trained on a large and diverse URL dataset.

### Evidence and Support
The repository includes a notebook and README, but the final CSV dataset is not included. The notebook uses a local path:
`E:\data\data_Features (2).csv`

This weakens reproducibility.

### Weaknesses / Limitations
- Dataset not directly available in the repository.
- Hidden preprocessing may exist.
- Some dependencies are heavy and version-sensitive.
- The feature `malicious_probability` may require careful investigation because it could introduce information leakage if it was computed using an external classifier or label-related information.
- No temporal features are available, so temporal drift cannot be evaluated directly.

## 3. Feature Engineering Analysis

The dataset contains URL-based features:
- length/count features: `url_length`, `domain_length`, `digits`, `letters`, `path_count`
- boolean indicators: `ipv`, `short`, `is_encoded`, `sus`
- calculated features: `entropy`, `ratio`, `malicious_probability`

These features are meaningful for phishing detection because phishing URLs often use obfuscation, unusual characters, long paths, digits, and suspicious domain patterns.

## 4. Reproducibility Analysis

The original code cannot be executed directly unless the missing processed CSV is supplied. The repository contains a notebook, README, and license, but not the final feature CSV. Therefore, reproduction requires either downloading the original raw datasets and recreating the features, or obtaining the author's processed dataset.

## 5. Experimental Results

To be completed after running the starter notebook.

Suggested models:
- Logistic Regression
- Random Forest
- HistGradientBoosting

Suggested metrics:
- Accuracy
- Precision
- Recall
- F1
- MCC
- ROC-AUC
- Confusion Matrix

## 6. Error Analysis

To be completed after running the starter notebook.

Discuss:
- false positives: benign URLs blocked as phishing
- false negatives: phishing URLs missed by the model
- why false negatives are more dangerous in phishing defense
- whether changing the decision threshold improves the security trade-off

## 7. Conclusions

Initial conclusion:
The source is relevant and useful for the course project, but it has reproducibility weaknesses. The chosen project is still a good selection because it allows a strong critical evaluation, especially around missing data, hidden preprocessing, feature leakage, and proper cybersecurity metrics.
