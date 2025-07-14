# 🚨 Bank Transaction Fraud Detection System

A **production-ready machine learning pipeline** to detect fraudulent transactions for a **banking or fintech firm**, built entirely with **Python** and **MySQL**.  
This project simulates large-scale financial transaction data, performs **advanced feature extraction**, trains **multiple fraud detection models**, and visualizes fraud patterns to help businesses reduce fraud risk.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [How to Run](#how-to-run)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## ✨ Overview

Banks lose millions to fraudulent activities every year. Detecting suspicious transactions in real-time is critical to protect both the institution and its customers.

This project:
- Creates a **realistic, large transactional dataset** using `Faker`.
- Loads the data into a **MySQL database** for robust querying.
- Performs **feature engineering** (time-based features, amount binning, one-hot encoding).
- Trains **multiple ML models** — Logistic Regression, Random Forest, XGBoost — to detect fraud.
- Evaluates models with confusion matrices, ROC-AUC, and Precision-Recall.
- Visualizes fraud patterns to extract actionable insights.

---

## ✅ Features

- 📂 **Big Synthetic Banking Dataset:** Simulates 100,000+ transactions.
- 🗃️ **MySQL Integration:** Stores transactions in a relational DB for realistic pipelines.
- ⚙️ **Feature Engineering:** Hourly transaction trends, amount binning, categorical encoding.
- 🤖 **Multiple ML Algorithms:** Compare performance of popular classifiers.
- 📈 **Data Visualization:** Fraud distribution, correlation heatmaps.
- 🧩 **Modular Codebase:** Organized in scripts, notebooks, and SQL files.
- 📚 **Reproducible:** Fully documented and ready to clone & run.

---

## 🧑‍💻 Tech Stack

- **Python 3.10+**
- **MySQL**
- **Faker** (for synthetic data)
- **Pandas**, **NumPy**
- **Scikit-Learn**, **XGBoost**
- **Matplotlib**, **Seaborn**
- **Jupyter Notebook**

---

## 📂 Project Structure

bank-fraud-detection/
│
├── data/ # Raw & processed datasets
│ ├── raw_transactions.csv
│ ├── processed_transactions.csv
│
├── database/ # Database schema & data loading scripts
│ ├── create_db.sql
│ ├── load_data.sql
│
├── notebooks/ # End-to-end pipeline notebooks
│ ├── 01_EDA.ipynb
│ ├── 02_Feature_Engineering.ipynb
│ ├── 03_Model_Training.ipynb
│ ├── 04_Model_Evaluation.ipynb
│ ├── 05_Visualization.ipynb
│
├── scripts/ # Python scripts for data gen, DB connection, utilities
│ ├── generate_fake_data.py
│ ├── connect_mysql.py
│ ├── utils.py
│
├── requirements.txt
├── README.md
└── .gitignore



## 🔍 How It Works

1️⃣ **Data Simulation:**  
   - `generate_fake_data.py` uses `Faker` to create realistic transactions.
   - Small % are labeled fraudulent for class imbalance realism.

2️⃣ **Database Integration:**  
   - `create_db.sql` creates the MySQL schema.
   - `load_data.sql` loads the generated CSV into `transactions` table.

3️⃣ **Feature Engineering:**  
   - Extracts transaction hour.
   - Bins transaction amounts.
   - Encodes categorical features.

4️⃣ **Model Training:**  
   - Trains Logistic Regression, Random Forest, and XGBoost classifiers.
   - Splits train/test using stratification for imbalanced classes.

5️⃣ **Evaluation:**  
   - Confusion Matrix, ROC-AUC, Precision-Recall.
   - Identifies best-performing model.

6️⃣ **Visualization:**  
   - Class distribution plot.
   - Feature correlation heatmap.

---

## ⚙️ How to Run

✅ **1. Clone the Repo**

git clone https://github.com/hrishabhkothary/Bank-Transaction-Fraud-Detection-and-Analysis-System.git
cd bank-fraud-detection

✅ 2. Install Dependencies


pip install -r requirements.txt
✅ 3. Generate Synthetic Data


cd scripts
python generate_fake_data.py

✅ 4. Set Up MySQL Database

Open database/create_db.sql in MySQL Workbench & execute.

Copy raw_transactions.csv to your MySQL secure-file-priv folder.

Run database/load_data.sql to import CSV into the transactions table.

✅ 5. Run Notebooks


jupyter notebook
Open notebooks/ and run:

01_EDA.ipynb → Explore Data

02_Feature_Engineering.ipynb → Engineer Features

03_Model_Training.ipynb → Train Models

05_Visualization.ipynb → See Insights

📊 Results
Class imbalance handled with careful splitting.

Achieves high precision and recall for minority class.

Random Forest and XGBoost outperform baseline Logistic Regression.

Visualizations show clear fraud vs. non-fraud trends.

🚀 Future Improvements
✅ Integrate real streaming data APIs.
✅ Deploy a real-time prediction API.
✅ Add alert system for flagged transactions.
✅ Experiment with deep learning (AutoEncoders).
✅ Build an interactive dashboard with Streamlit or Tableau.

📜 License
This project is open-sourced for educational use.

🙌 Author
Hrishabh Kothari — Data Scientist & ML Enthusiast

✨ If you find this useful, leave a ⭐ on the repo!
