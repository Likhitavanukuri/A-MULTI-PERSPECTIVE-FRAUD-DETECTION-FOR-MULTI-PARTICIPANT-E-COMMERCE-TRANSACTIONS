# Multi-Perspective Fraud Detection for Multi-Participant E-Commerce Transactions

This project implements a machine learning-powered fraud detection system for complex e-commerce environments involving buyers, sellers, and platform interactions. 
It includes a Flask-based API and Salesforce integration.


### 🔍 Fraud Detection Flow

1. **Salesforce** triggers an HTTP request to the Flask API when a new Order is placed.
2. **Flask API** receives transaction and user details, preprocesses the data, and performs prediction using a trained model.
3. **Model Output** includes:
   - `prediction`: 1 for fraud, 0 for non-fraud
   - `fraud_score`: probability score between 0 and 1
4. **Salesforce** updates the Order with this fraud risk score and optionally triggers a Case or alert.

👩‍💻 Author
Vanukuri Likhita (KHIT, AIML)
Academic Project Year: 2024–2025


