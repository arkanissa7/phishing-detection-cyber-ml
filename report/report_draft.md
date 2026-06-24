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
