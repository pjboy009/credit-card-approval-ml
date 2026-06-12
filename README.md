# Credit Card Approval System using Machine Learning

## 📌 Project Overview
This project aims to automate the credit card approval process using machine learning. The system predicts whether an application should be approved or rejected based on applicant details.

---

## 🎯 Objective
- Reduce manual effort in application processing  
- Provide consistent decision-making  
- Build a data-driven approval system  

---

## 📊 Dataset
We used a real-world credit approval dataset containing features such as:
- Credit Score  
- Income  
- Debt  
- Employment Status  
- Prior Default  

---

## 🔍 Exploratory Data Analysis (EDA)
Key insights:
- Higher credit score increases approval chances  
- Prior default leads to higher rejection  
- Income and employment impact decisions  

---

## 🤖 Model Used
- Random Forest Classifier  
- Chosen for better accuracy and handling complex data  

---

## 📈 Model Performance
- Accuracy: **87%**  
- Model performs well on unseen data  

---

## 🌐 Web Application
- Built using Flask  
- User inputs details through form  
- System predicts approval status  

---

## ⭐ Features
- Predict approval or rejection  
- Show probability of prediction  
- Highlight key influencing factors  

---

## 🛠️ Tech Stack
- Python  
- Flask  
- Scikit-learn  
- Pandas  
- HTML & CSS  

---

## 📂 Project Structure

```text
credit-card-approval-ml/
│
├── app.py
├── requirements.txt
├── README.md
│
├── artifacts/
│   └── credit_model.pkl
│
├── notebooks/
│   ├── EDA.ipynb
│   └── model_training.ipynb
│
├── src/
│   ├── __init__.py
│   ├── logger.py
│   ├── exception.py
│   ├── utils.py
│   └── data_ingestion.py
│
├── templates/
│   ├── index.html
│   └── result.html
```
---

## 🚀 Conclusion
This project demonstrates how machine learning can be used to automate financial decision-making efficiently and accurately.
