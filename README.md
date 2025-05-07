
# Detecting Malicious Web Requests Using Enhanced TextCNN

This repository provides an implementation of a malicious web request detection system based on the research paper *Detecting Malicious Web Requests Using an Enhanced TextCNN*. The system combines deep learning techniques (TextCNN) and statistical feature engineering to identify harmful web requests with high accuracy.

## Introduction

Web applications face increasing threats from malicious requests such as SQL injection, Cross-Site Scripting (XSS), and other parameter tampering attacks. This project implements a hybrid approach that:

- Uses TextCNN to automatically extract semantic features from web requests.
- Defines transferable statistical features to enhance detection capabilities.
- Combines both types of features and feeds them into a Support Vector Machine (SVM) classifier to improve classification performance.

The implementation is based on the HTTP CSIC 2010 dataset but can be adapted for other datasets.

## Project Structure

- **`URL_Extraction.py`**: Extracts URLs from raw HTTP traffic files and processes GET and POST requests.
- **`Convert2Database.py`**: Decodes, cleans, and tokenizes the extracted URLs, labels them (malicious/benign), and creates training and testing datasets in CSV format.
- **`Model.py`**: Implements the enhanced TextCNN model with the following features:
    - Word2Vec-based embedding layer.
    - 1D Convolutional layers for feature extraction.
    - Max pooling and dense layers for classification.
    - Final evaluation metrics: accuracy, precision, recall, F1-score.

## Features

- **Data Preprocessing:**
    - Handles raw HTTP GET and POST requests.
    - Removes duplicates and decodes URLs multiple times to expose hidden payloads.
    - Tokenizes URLs based on special characters.

- **Model Architecture:**
    - Embedding layer initialized with Word2Vec vectors.
    - Convolutional layers with ReLU activation.
    - Dropout layers for regularization.
    - Fully connected layers for final classification.
    - Statistical features like URL decoding count, illegal key/value pattern detection.

- **Hybrid Detection:**
    - TextCNN extracts abstract semantic features.
    - Statistical features capture domain-specific anomalies (e.g., parameter tampering).
    - Combined features fed into SVM for robust classification.

## Requirements

- Python 3.7+
- TensorFlow / Keras
- gensim
- numpy
- scikit-learn
- pandas

(Install dependencies via `pip install -r requirements.txt` if provided.)

## Dataset

The implementation uses the **HTTP Dataset CSIC 2010**, which contains 72,000 normal and 25,000 anomalous web requests. You should ensure your dataset is placed in the `Database/dataset_cisc_train_test/` directory or update the paths accordingly.

## Usage

### 1. Extract URLs

Extract URLs from the dataset (both malicious and normal):

```bash
python URL_Extraction.py
```

### 2. Prepare Database

Convert the extracted URLs into labeled datasets (train/test splits):

```bash
python Convert2Database.py
```

### 3. Train and Evaluate the Model

Train the enhanced TextCNN model and evaluate its performance:

```bash
python Model.py
```

The script prints out key metrics:
- Accuracy
- Precision
- Recall
- F1-score

## Model Overview

The core of the model is an enhanced TextCNN architecture:

- **Word2Vec Embedding:** Generates semantic word vectors.
- **Convolution + MaxPooling:** Extracts meaningful local patterns.
- **Dense Layers:** Final classification using sigmoid activation.
- **SVM Layer (paper-based):** Optionally, the last layer can be replaced with an SVM for improved generalization, as described in the paper.

## Experimental Results

In the referenced paper, the hybrid model achieves:

- **Accuracy:** ~99.33%
- **Precision:** ~99.53%
- **Recall:** ~99.09%

The system outperforms traditional machine learning and other deep learning models like LSTM and RCNN.

## Reference

The implementation is based on the following research paper (included in the repository):

**Detecting Malicious Web Requests Using an Enhanced TextCNN**  
Lian Yu, Lihao Chen, Jingtao Dong, et al.  
2020 IEEE 44th Annual Computers, Software, and Applications Conference (COMPSAC)

---
