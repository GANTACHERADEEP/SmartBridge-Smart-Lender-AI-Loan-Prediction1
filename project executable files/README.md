# 🏦 Smart Lender - AI Powered Loan Eligibility Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-KNN-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Overview

Smart Lender is a Machine Learning-powered web application that predicts whether a loan application should be **Approved** or **Rejected** based on applicant information.

The application helps financial institutions make faster, consistent, and data-driven lending decisions by using machine learning algorithms trained on historical loan application data.

The trained model is deployed using **Flask**, allowing users to submit loan details through a web interface and receive real-time predictions.

---

## 🚀 Features

- AI-powered loan eligibility prediction
- Real-time prediction using Flask
- User-friendly web interface
- Data preprocessing pipeline
- Machine Learning model comparison
- Confidence-based prediction
- Responsive UI
- Easy deployment on IBM Cloud

---

## 🧠 Machine Learning Models Compared

The following classification algorithms were trained and evaluated:

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost

### Best Performing Model

| Model | Testing Accuracy |
|---------|----------------|
| **K-Nearest Neighbors (KNN)** | **84.55%** |

The KNN model achieved the highest testing accuracy and was selected for deployment.

---

## 📂 Project Structure

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

## 📊 Dataset Features

The model uses the following applicant information:

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

Target Variable:

- Loan Status (Approved / Rejected)

---

## ⚙️ Technologies Used

### Programming

- Python

### Machine Learning

- Scikit-learn
- KNN
- Decision Tree
- Random Forest
- XGBoost

### Web Development

- Flask
- HTML5
- CSS3
- Bootstrap 5

### Libraries

- Pandas
- NumPy
- Matplotlib
- Joblib

---

## 🔄 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Handle Missing Values
4. Encode Categorical Variables
5. Feature Scaling
6. Train-Test Split
7. Train Multiple ML Models
8. Compare Performance
9. Select Best Model
10. Deploy Using Flask

---

## ▶️ How to Run

### Clone Repository

```bash
git clone <repository-url>
```

### Move into project

```bash
cd Smart-Lender
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📈 Model Evaluation

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

## 📷 Application Screenshots

### Home Page

(Add Screenshot)

### Prediction Result

(Add Screenshot)

### Confusion Matrix

(Add Screenshot)

---

## 🌍 Future Enhancements

- Explainable AI (SHAP/LIME)
- Loan Default Probability
- User Authentication
- Database Integration
- Admin Dashboard
- Cloud Deployment
- Email Notification
- PDF Report Generation

---

## 👨‍💻 Author

**Cheradeep Ganta**

B.Tech CSE (AI & ML)

Anil Neerukonda Institute of Technology and Sciences

---

## ⭐ Acknowledgement

This project was developed as part of a Machine Learning and Flask-based Smart Lender application for intelligent loan eligibility prediction.
