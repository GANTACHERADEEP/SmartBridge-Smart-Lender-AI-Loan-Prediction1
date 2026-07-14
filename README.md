# 🏦 Smart Lender – AI-Powered Loan Eligibility Prediction

An end-to-end Machine Learning web application that predicts whether a loan application is likely to be **Approved** or **Rejected** based on an applicant's financial and demographic information. The application is built with **Python**, **Scikit-learn**, and **Flask**, providing real-time predictions through a simple and responsive web interface.

---

## 🔗 Live Demo

**Application:** https://smart-lender-ai-loan-prediction.onrender.com

**Source Code:** https://github.com/GANTACHERADEEP/Smart-Lender-AI-Loan-Prediction

---

## 📌 Project Overview

Smart Lender leverages supervised machine learning to assist financial institutions in evaluating loan eligibility. Multiple classification algorithms were trained and compared, with the best-performing model deployed as a Flask web application.

The project demonstrates the complete machine learning lifecycle, including:

* Data preprocessing and cleaning
* Feature engineering
* Model training and evaluation
* Model selection
* Flask application development
* Real-time prediction deployment

---

## ✨ Key Features

* AI-powered loan eligibility prediction
* Real-time predictions using Flask
* Responsive and user-friendly interface
* Automated data preprocessing pipeline
* Multiple machine learning model comparison
* Model evaluation using standard classification metrics
* Production-ready project structure
* Cloud deployment on Render

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* K-Nearest Neighbors (KNN)
* Decision Tree Classifier
* Random Forest Classifier
* XGBoost

### Web Development

* Flask
* HTML5
* CSS3
* Bootstrap 5

### Libraries

* Pandas
* NumPy
* Matplotlib
* Joblib

---

## 📊 Dataset Features

The model predicts loan eligibility using the following applicant details:

| Feature             |
| ------------------- |
| Gender              |
| Married             |
| Dependents          |
| Education           |
| Self Employed       |
| Applicant Income    |
| Co-applicant Income |
| Loan Amount         |
| Loan Amount Term    |
| Credit History      |
| Property Area       |

**Target Variable**

* Loan Status (Approved / Rejected)

---

## 🤖 Machine Learning Models

The following classification models were trained and evaluated:

* Decision Tree
* Random Forest
* K-Nearest Neighbors (KNN)
* XGBoost

### Best Performing Model

| Model                         | Test Accuracy |
| ----------------------------- | ------------: |
| **K-Nearest Neighbors (KNN)** |    **84.55%** |

Based on evaluation metrics, the **K-Nearest Neighbors (KNN)** model achieved the highest testing accuracy and was selected for deployment.

---

## 📈 Model Evaluation

The trained models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

---

## 🔄 Machine Learning Pipeline

1. Data Collection
2. Data Cleaning
3. Missing Value Handling
4. Label Encoding
5. Feature Scaling
6. Train-Test Split
7. Model Training
8. Performance Comparison
9. Best Model Selection
10. Flask Deployment

---

## 📁 Project Structure

```
Smart-Lender/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── Procfile
├── README.md
│
├── datasets/
│   ├── loan_prediction.csv
│   ├── X_train.csv
│   ├── X_test.csv
│   ├── y_train.csv
│   └── y_test.csv
│
├── models/
│   ├── loan_model.pkl
│   ├── scaler.pkl
│   ├── label_encoders.pkl
│   ├── model_comparison.csv
│   └── evaluation_metrics.csv
│
├── notebooks/
│   ├── 01_data_analysis.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/GANTACHERADEEP/Smart-Lender-AI-Loan-Prediction.git
```

### Navigate to the Project Directory

```bash
cd Smart-Lender-AI-Loan-Prediction
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Application Preview

### Home Page

<img width="1832" height="891" alt="Home Page" src="https://github.com/user-attachments/assets/b8f50bc2-6b14-47c0-b78e-ba53ac61547b" />

### Prediction Result

<img width="1836" height="910" alt="Prediction Result" src="https://github.com/user-attachments/assets/d38cc1c2-b0aa-4286-a6e3-a5adb6f623a6" />

### Confusion Matrix

<img width="558" height="454" alt="Confusion Matrix" src="https://github.com/user-attachments/assets/990c8a8e-651b-4432-b2f0-dc75b5f71edb" />

---

## 🌱 Future Enhancements

* Explainable AI using SHAP or LIME
* Loan default risk prediction
* User authentication and authorization
* Database integration
* Admin dashboard
* Email notifications
* PDF report generation
* REST API support
* Docker containerization
* CI/CD pipeline implementation

---

## 👨‍💻 Author

**Cheradeep Ganta**

B.Tech – Computer Science & Engineering (AI & ML)

Anil Neerukonda Institute of Technology & Sciences

---

## 📄 License

This project is intended for educational and learning purposes. Feel free to fork and extend it for your own projects.

---

⭐ If you found this project helpful, consider giving it a **star** on GitHub.
