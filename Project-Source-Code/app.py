from flask import Flask, render_template, request
import numpy as np
import joblib
from datetime import datetime

app = Flask(__name__)

# Load Model & Preprocessors
model = joblib.load("models/loan_model.pkl")
scaler = joblib.load("models/scaler.pkl")
encoders = joblib.load("models/label_encoders.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:

        # Get User Inputs
        gender = request.form["Gender"]
        married = request.form["Married"]
        dependents = request.form["Dependents"]
        education = request.form["Education"]
        self_employed = request.form["Self_Employed"]

        applicant_income = float(request.form["ApplicantIncome"])
        coapplicant_income = float(request.form["CoapplicantIncome"])
        loan_amount = float(request.form["LoanAmount"])
        loan_term = float(request.form["Loan_Amount_Term"])
        credit_history = float(request.form["Credit_History"])

        property_area = request.form["Property_Area"]

        # Encode Inputs
        gender = encoders["Gender"].transform([gender])[0]
        married = encoders["Married"].transform([married])[0]
        dependents = encoders["Dependents"].transform([dependents])[0]
        education = encoders["Education"].transform([education])[0]
        self_employed = encoders["Self_Employed"].transform([self_employed])[0]
        property_area = encoders["Property_Area"].transform([property_area])[0]

        # Feature Vector
        features = np.array([[
            gender,
            married,
            dependents,
            education,
            self_employed,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term,
            credit_history,
            property_area
        ]])

        # Scale Features
        features = scaler.transform(features)

        # Prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0]

        confidence = round(np.max(probability) * 100, 2)

        if prediction == 1:
            status = "APPROVED"
            status_color = "#16a34a"

            recommendation = (
                "Applicant satisfies the major loan eligibility criteria. "
                "Loan can be considered for approval."
            )

        else:
            status = "REJECTED"
            status_color = "#dc2626"

            recommendation = (
                "Loan application appears risky. "
                "Further verification is recommended before approval."
            )

        if confidence >= 90:
            risk = "LOW"
        elif confidence >= 75:
            risk = "MEDIUM"
        else:
            risk = "HIGH"
        current_time = datetime.now().strftime("%d %B %Y | %I:%M %p")

        return render_template(

    "result.html",

    prediction=status,
    color=status_color,
    confidence=confidence,
    risk=risk,
    recommendation=recommendation,
    algorithm="K-Nearest Neighbors",
    accuracy="84.55 %",
    prediction_time=current_time,

    gender=request.form["Gender"],
    married=request.form["Married"],
    education=request.form["Education"],
    dependents=request.form["Dependents"],
    self_employed=request.form["Self_Employed"],
    applicant_income=applicant_income,
    coapplicant_income=coapplicant_income,
    loan_amount=loan_amount,
    loan_term=loan_term,
    credit_history="Good" if credit_history == 1 else "Bad",
    property_area=request.form["Property_Area"]

)

    except Exception as e:
        return f"<h2>Error:</h2><br>{e}"


if __name__ == "__main__":
    app.run(debug=True)