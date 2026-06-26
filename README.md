# Phishing Detection Cyber ML

Final project for **Data Science in Cybersecurity**.

This project is an adapted reproduction and critical evaluation of the GitHub project **“Phishing Attack Detection using Machine Learning”** by RimTouny.

## Project Description

This project focuses on the cybersecurity problem of **phishing URL detection**.
The goal is to classify URLs as either:

* `legitimate`
* `phishing`

Phishing is an important cybersecurity problem because attackers use fake or malicious URLs to steal passwords, personal information, and financial data from users.

The selected original project proposes using machine learning models trained on URL-based features to detect phishing URLs. In this project, the original methodology was critically evaluated and adapted using an approved phishing dataset.

The work includes:

* Data loading and inspection
* Exploratory Data Analysis
* Feature engineering and preprocessing
* Model training
* Model evaluation
* Cross-validation
* Error analysis
* Critical evaluation of the original source
* Reproducibility analysis

## Selected Source

The selected source for this project is the GitHub project:

**Phishing Attack Detection using Machine Learning**
Author: RimTouny

Link to the selected source / original GitHub repository:
[https://github.com/RimTouny/Phishing-Attack-Detection-using-Machine-Learning](https://github.com/RimTouny/Phishing-Attack-Detection-using-Machine-Learning)

## Original GitHub Repository

Original repository:
[https://github.com/RimTouny/Phishing-Attack-Detection-using-Machine-Learning](https://github.com/RimTouny/Phishing-Attack-Detection-using-Machine-Learning)

The original project uses URL-based features and machine learning classifiers to detect whether a URL is phishing or benign.

## Dataset Source

The original processed CSV file used by the selected GitHub project was not directly available in the repository.
The original notebook loads the dataset from a local Windows path, which creates a reproducibility limitation.

Therefore, this project uses the approved dataset:

`dataset_phishing.csv`

Dataset used in this adapted reproduction:

* 11,430 URL samples
* 89 original columns
* Target column: `status`
* Classes: `legitimate` and `phishing`
* Balanced dataset:

  * 5,715 legitimate URLs
  * 5,715 phishing URLs

The target was encoded as:

* `legitimate` → `0`
* `phishing` → `1`

## Repository Structure

```text
phishing-detection-cyber-ml/
│
├── data/
│   └── dataset_phishing.csv
│
├── Phishing_Detection.ipynb
│
├── results/
│   ├── model_metrics.csv
│   ├── threshold_analysis.csv
│   └── cross_validation_summary.csv
│
├── report/
│   └── phishing_detection_final_report.pdf
│
├── README.md
└── requirements.txt
```

## Models Used

The adapted notebook trains and compares several machine learning models:

* Logistic Regression
* Decision Tree
* Random Forest
* Extra Trees
* Gradient Boosting
* K-Nearest Neighbors

The best-performing model was **Random Forest**.

## Main Results

Random Forest achieved the best performance:

* Accuracy: `0.9624`
* Phishing Recall: `0.9676`
* Phishing F1-score: `0.9626`
* ROC-AUC: `0.9934`

Confusion Matrix results:

* True Legitimate: `1094`
* False Positive: `49`
* False Negative: `37`
* True Phishing: `1106`

The model correctly classified most URLs, but the false negatives are especially important because they represent phishing URLs that were incorrectly classified as legitimate.

## Execution Instructions

### 1. Clone the repository

```bash
git clone https://github.com/arkanissa7/phishing-detection-cyber-ml.git
cd phishing-detection-cyber-ml
```

### 2. Install required libraries

```bash
pip install -r requirements.txt
```

### 3. Make sure the dataset exists

The dataset should be located at:

```text
data/dataset_phishing.csv
```

### 4. Run the notebook

Open the notebook:

```text
Phishing_Detection.ipynb
```

You can run it using Jupyter Notebook, JupyterLab, or Google Colab.

In Google Colab:

1. Upload the notebook.
2. Upload `dataset_phishing.csv`.
3. Run all cells.

```text
Runtime → Run all
```

The notebook will generate model evaluation results and save output files into the `results/` folder.

## Requirements

The main Python libraries used are:

* pandas
* numpy
* matplotlib
* scikit-learn
* jupyter

## Reproducibility Note

The original GitHub project could not be reproduced exactly because the processed CSV file was not directly available in the original repository.
For this reason, this project performs an **adapted reproduction** using an approved phishing dataset.

The adapted notebook improves reproducibility by:

* using a clear dataset path
* documenting preprocessing steps
* using a fixed random seed
* saving model results
* including evaluation and error analysis
* providing this README and execution instructions

## Final Conclusion

The adapted reproduction supports the general idea that machine learning can be useful for phishing URL detection when meaningful URL and webpage-based features are available.
However, the original project has reproducibility limitations because the processed dataset was missing, and the results should be interpreted carefully.

This project shows that strong cybersecurity machine learning work requires not only high model performance, but also transparent data, reproducible code, appropriate metrics, and careful error analysis.
