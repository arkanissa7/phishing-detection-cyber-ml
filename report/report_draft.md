# Phishing Attack Detection using Machine Learning — Final Project Report

## Selected Source

The selected source for this project is the GitHub repository “Phishing Attack Detection using Machine Learning” by RimTouny.

Original GitHub repository:  
https://github.com/RimTouny/Phishing-Attack-Detection-using-Machine-Learning

The project belongs to the field of Data Science in Cybersecurity, specifically phishing detection. This topic is relevant to the course because phishing detection is one of the cybersecurity problems in which data science and machine learning can be used to detect malicious behavior.

The selected source clearly defines a cybersecurity problem, proposes a machine learning-based solution, provides an implementation in a GitHub repository, and describes the use of URL-based features and datasets for model training and evaluation.

---

## 1. Summary of the Source

The selected source addresses the problem of phishing URL detection. Phishing is a cyberattack technique in which attackers create fake websites or malicious URLs that appear legitimate in order to trick users into revealing sensitive information such as passwords, personal details, or financial credentials.

The problem is important because phishing attacks are common and can cause serious damage to users and organizations. If a phishing URL is not detected, users may enter private information into a fake website. Therefore, an automated phishing detection system can help reduce the risk of such attacks.

The proposed solution is based on machine learning. The author extracts features from URLs and uses them to train classification models that distinguish between phishing URLs and benign URLs. The task is a binary classification problem, where each URL is classified as either phishing or benign.

The features used in the project include URL-based characteristics such as URL length, domain length, number of digits, number of letters, number of special characters, entropy, encoding indicators, and other suspicious patterns. These features are meaningful because phishing URLs often contain unusual structures, long strings, suspicious domains, or encoded characters.

According to the project description, the dataset is built from several URL datasets and contains a large number of URLs. The original notebook shows a dataset of approximately 737,000 samples and 26 columns. The target variable is the label, where phishing and benign URLs are represented as two different classes.

The methodology of the original project includes data preparation, feature extraction, exploratory data analysis, feature selection, handling class imbalance, training multiple machine learning models, and evaluating their performance using classification metrics such as accuracy, precision, recall, F1-score, and confusion matrix.

---

## 2. Critical Evaluation

The main claim of the original project is that machine learning can be used to improve phishing URL detection. The author presents the project as a phishing defense system trained on a large and diverse dataset of approximately 737,000 URLs.

This claim is reasonable because phishing URLs often contain patterns that can be captured using URL-based features, such as long URL length, suspicious domain structure, many digits or special characters, encoded characters, and unusual entropy values. Machine learning models can learn such patterns and use them to classify URLs as phishing or benign.

However, the evidence provided by the original repository has some important limitations. The repository includes a notebook and a README file, but the final processed CSV dataset is not included directly in the repository. In the original notebook, the dataset is loaded from a local Windows path rather than from a public or relative project path. This means that the project cannot be executed immediately by another user without obtaining or reconstructing the missing dataset.

This creates a reproducibility problem. A strong data science project should allow other researchers or students to run the code, inspect the data, and verify the reported results. In this case, hidden preprocessing steps may exist because the final feature dataset is already prepared before being loaded into the notebook. Therefore, it is not fully clear how all features were created or whether the same dataset can be reconstructed exactly.

Another limitation is that the project uses many models and reports performance, but the evaluation should be examined carefully. In phishing detection, accuracy alone is not sufficient. A model may achieve high accuracy if the dataset is imbalanced, but still fail to detect important phishing examples. For this reason, recall, precision, F1-score, MCC, ROC-AUC, and the confusion matrix are more informative.

The most dangerous type of error in this problem is a false negative, where a phishing URL is classified as benign. This can expose users to malicious websites. A false positive, where a benign URL is classified as phishing, is also problematic because it may block legitimate websites, but it is usually less dangerous than missing a real phishing attack.

A further point that requires careful analysis is the feature called `malicious_probability`. If this feature was computed using another detector, blacklist, or label-related information, it could introduce data leakage. In such a case, the model may appear to perform very well, but the performance may not reflect true generalization to unseen URLs. Therefore, in the reproduction notebook, it is important to compare model performance with and without this feature.

Overall, the original project addresses an important cybersecurity problem and proposes a reasonable machine learning approach. However, the author’s conclusions should be treated carefully because the repository has reproducibility limitations, possible hidden preprocessing, and potential feature leakage. The project is useful as a basis for analysis, but its claims should be validated through independent experiments.
