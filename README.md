<div align="center">

# Credit Risk Analytics & Default Prediction

### Data Analytics + Machine Learning | Power BI | Python | PostgreSQL

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/Status-In%20Progress-7B61FF?style=for-the-badge">
</p>

<p>
  An end-to-end <strong>Data Analytics + Machine Learning</strong> project for
  credit-risk analysis, default prediction, model evaluation, and risk-review support.
</p>

</div>

## 📌 Project Overview

### 🏢 Business Context

Management needs a comprehensive view of the **customer loan portfolio** to monitor loan applications, assess credit profiles, and manage potential credit risks.

The project consolidates key information including **customer characteristics, loan details, credit history, repayment behavior, and risk indicators** to provide a data-driven view of portfolio quality and support credit decision-making.

### 🎯 Project Objective

This project combines **Data Analytics and Data Science** to:

- 📊 Monitor and analyze the overall **loan portfolio**
- 🔍 Explore **customer and credit characteristics**
- ⚠️ Identify factors associated with **credit risk**
- 🤖 Build a predictive model to estimate the **probability of credit risk**
- 📈 Develop an interactive dashboard to support **portfolio monitoring and decision-making**

### 💡 Project Outcome

The final solution integrates **business analytics, data visualization, and machine learning** to provide:

- **Business Insights** — Understand customer profiles, loan characteristics, and portfolio risk patterns.
- **Risk Analysis** — Identify key factors associated with credit risk and analyze model predictions.
- **Predictive Assessment** — Estimate the probability of credit risk using a machine learning model.
- **Decision Support** — Provide interactive visualizations and data-driven insights to support credit evaluation and portfolio management.

The final Power BI report brings these two perspectives together to support **credit-risk review and decision support**. It is not intended to replace a bank's formal credit policy or automatically approve/reject applications.

---

## 🔄 Credit Risk Analysis Workflow: From Raw Data to Actionable Insights

The project implements an **End-to-End Credit Risk Analysis Pipeline**, combining **Data Analytics, Data Science, SQL, and Business Intelligence (BI)** to transform raw credit data into actionable insights for portfolio monitoring and credit decision-making.

<div align="center">
  <img src="images/credit_risk_workflow.png" alt="Credit Risk Analysis Workflow" width="100%" />
</div>

* **Step 1 - Raw Credit Data (Microsoft Excel):**
  * Collect and manage raw data including **loan applications, customer information, credit history, loan history, transaction records, and reference data**.

* **Step 2 - Data Preparation & EDA (Python & Pandas):**
  * Perform **data cleaning**, handle missing values, validate data quality, analyze feature distributions and relationships, and identify potential **risk patterns and indicators** before modeling.

* **Step 3 - Modeling & Evaluation (Scikit-learn):**
  * Build a **Logistic Regression** classification model to predict credit risk. Perform train/test splitting, hyperparameter tuning, and model evaluation using **Accuracy, Precision, Recall, F1-score, ROC-AUC, and Confusion Matrix**.
     
* **Step 4 - FP / FN Analysis (DBeaver - SQL):**
  * Use **SQL queries** to compare predicted and actual outcomes, identify **False Negative (FN)** and **False Positive (FP)** cases, and investigate customer and loan characteristics associated with model misclassification.

* **Step 5 - Risk Adjustment (Python Rules):**
  * Apply **Business Policy Rules** based on FP/FN analysis to adjust model predictions, refine risk classifications, and generate **Final Risk Scores / Risk Segments** for business analysis.

* **Step 6 - Decision Support (Power BI):**
  * Build an **interactive Power BI dashboard** to visualize the loan portfolio, risk segments, customer characteristics, and key risk indicators, supporting **portfolio monitoring, risk assessment, and credit decision-making**.

---

# 📊 Data Analytics

## 1. Data Understanding

The project starts by understanding four main groups of information used to describe credit risk:

| Data Group | Examples | Purpose |
|---|---|---|
| Customer profile | Age, employment, housing | Understand customer stability |
| Financial capacity | Income, DTI, LTI | Evaluate repayment capacity |
| Loan information | Loan amount, purpose, term, interest rate | Understand loan size and cost |
| Credit history | Previous default, credit history, late payment | Understand past credit behaviour |

The Power BI report includes a dedicated **Data Dictionary** page explaining the meaning and usage of important variables and model terminology.

---

## 2. Derived Risk Metrics

Several metrics are derived to make the credit analysis more interpretable.

### DTI — Debt-to-Income Ratio

```text
DTI = (Loan Amount + Other Debt) / Annual Income
```

Represents the overall debt burden relative to annual income.

### LTI — Loan-to-Income Ratio

```text
LTI = Loan Amount / Annual Income
```

Measures the size of the requested loan relative to annual income.

### Default Rate

```text
Default Rate = Number of Default Cases / Total Cases
```

These metrics are used throughout the Power BI analysis and the modelling workflow.

---

## 3. Exploratory Data Analytics (EDA) & Data Insights

The analytical phase investigates risk concentration across 32,566 loan records to identify descriptive patterns before model building.

### 📌 Portfolio Snapshot

<div align="center">

| Total Applications | Default Cases | Overall Default Rate | Total Non-Performing Loan Value |
| :---: | :---: | :---: | :---: |
| **32,566** | **7,107** | **21.82%** | **~2,010 Billion VND** |

</div>

### 🔍 Key Observed Risk Patterns

1. **Loan-to-Income (LTI) as the Dominant Burden Factor:**
   * Applications with **LTI > 0.35** exhibit an exponential surge in default probability (>45%).
   * Borrowers requesting more than one-third of their annual income struggle significantly with debt serviceability.
2. **Interest Rate Risk Cascading:**
   * Higher-risk borrower segments are typically priced at higher interest rates (>14.5%), which paradoxically compounds debt-service pressure and drives elevated observed defaults.
3. **Income and Housing Stability:**
   * **Renters** show an observed default rate nearly **1.8× higher** than home owners.
   * Lower-income brackets account for over 40% of all default instances in the observed portfolio.
4. **Loan Purpose Variation:**
   * Loans for *Debt Consolidation* and *Medical Emergencies* demonstrate significantly higher default rates compared to *Education* or *Home Improvement*.

---

# 🤖 Machine Learning: Default Prediction

## 4. Modeling Architecture & Preprocessing Pipeline

The predictive modeling framework uses **Logistic Regression** to estimate the Probability of Default ($PD$). The pipeline enforces strict data integrity with **Stratified Splitting (80% Train / 20% Test)** based on the repayment status label.

```text
Raw Dataset (32,566 rows)
         │
         ▼  Stratified 80/20 Split
┌─────────────────────────┬─────────────────────────┐
│ Train Set (26,052 rows) │  Test Set (6,514 rows)  │
└─────────────────────────┴─────────────────────────┘
         │
         ▼
Feature Preprocessing (Log Transform + StandardScaler + Balanced Weights)
         │
         ▼
Logistic Regression Estimator
         │
         ▼
Raw Probability Predictions (Test Set)
         │
         ▼
Step 4: Risk Adjustment Layer (LTI Thresholds & Business Rules)
         │
         ▼
Final Validated Credit Risk Assessment
```

---

## 5. Feature Importance & Variable Contribution

The relative contribution of each feature is quantified using standardized absolute coefficient values scaled by feature standard deviations ($|\beta_j \times \sigma_j|$), ensuring rigorous comparability across different numerical scales:

<div align="center">

| Rank | Feature Name | Contribution (%) | Business Interpretation |
| :---: | :--- | :---: | :--- |
| **01** | **Loan-to-Income Ratio (LTI)** | **38.28%** | Primary risk driver: excessive leverage relative to annual income capacity. |
| **02** | **Loan Interest Rate (%)** | **28.16%** | Cost of debt burden directly compounding monthly repayment strain. |
| **03** | **Requested Loan Amount (VND)** | **20.43%** | Capital exposure scale: larger loans amplify loss-given-default risk. |
| **04** | **Annual Income (VND)** | **4.44%** | Baseline earning capacity and financial debt-service buffer. |
| **05** | **Home Ownership Status** | **3.04%** | Indicator of personal asset stability and collateral strength. |
| **06** | **Historical Default Record** | **2.77%** | Prior credit delinquency and historical repayment discipline. |
| **07** | **Debt-to-Income Ratio (DTI)** | **2.44%** | Aggregate multi-obligation debt load. |
| **08** | **Loan Purpose** | **0.43%** | Segmented capital utilization intent. |
| | **Total** | **100.00%** | **Top 3 features account for 86.87% of overall model decision weight.** |

</div>

---

## 6. Model Evaluation & Performance Metrics

The model was validated on the **unseen Test Set (6,514 applications)** after incorporating the Step 5 Risk Adjustment Layer.

### 📈 Core Performance Summary

<div align="center">

| Metric | Score | Industry Benchmark & Interpretation |
| :--- | :---: | :--- |
| **Accuracy** | **94.80%** | Overall correct classification rate across good and bad loans. |
| **ROC-AUC** | **0.8593** | Outstanding discrimination power between defaulters and non-defaulters. |
| **Recall (Sensitivity)** | **92.41%** | Successfully captures **92.41%** of all actual default cases in the portfolio. |
| **Precision** | **85.05%** | When the model flags default risk, it is correct **85.05%** of the time. |
| **Specificity** | **95.46%** | Protects **95.46%** of creditworthy customers from wrongful rejection. |
| **F1-Score** | **88.57%** | Optimal harmonic balance between risk detection and commercial retention. |
| **K-S Statistic** | **0.5850** | Strong separation capability ($>0.40$ indicates excellent scorecard quality). |
| **PR-AUC** | **0.7450** | High reliability under the natural credit class imbalance (~21.8% default rate). |
| **Brier Score / Log Loss** | **0.101 / 0.335** | Well-calibrated probabilistic confidence scores. |

</div>

### 🎯 Confusion Matrix (Test Set: 6,514 Applications)

<div align="center">

| | **Predicted: Default (Risk Flagged)** | **Predicted: Non-Default (Approved)** |
| :--- | :---: | :---: |
| **Actual: Default (1,422 cases)** | **1,314 TP** *(Defaults Caught)* | **108 FN** *(Missed Defaults)* |
| **Actual: Non-Default (5,092 cases)** | **231 FP** *(False Alarms)* | **4,861 TN** *(Good Loans Approved)* |

</div>

---

# 🔍 Deep Dive: FP / FN SQL Analysis & Business Adjustment

## 7. Error Audit & Cost-Sensitive Analysis (DBeaver / SQL)

In commercial retail banking, classification errors carry asymmetric financial impacts:

$$\text{Financial Loss}(\text{FN}) \gg \text{Opportunity Cost}(\text{FP})$$

* **False Negatives (FN - 108 cases):** Insolvent borrowers classified as creditworthy. This directly causes **severe principal capital write-offs**.
* **False Positives (FP - 231 cases):** Creditworthy customers mistakenly flagged as high-risk. This results in **lost interest revenue and customer friction**.

Using **DBeaver and advanced SQL queries**, individual error cohorts were audited against credit attributes to formulate business adjustment cut-offs.

```text
Model Probability Score
           │
           ▼
┌──────────────────────────────────────────────────────────┐
│                   DBeaver SQL Auditing                   │
│   • Identify boundary cases (Prob: 0.40 - 0.60)          │
│   • Investigate extreme LTI vs. Employment Stability     │
└──────────────────────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────────────┐
│         Step 4: Rule-Based Policy Adjustment Layers       │
│                                                          │
│  [Rescue Layer - FP → TN]                                │
│  • Criteria: Low LTI (<0.20) + High Seniority (>5 yrs)   │
│  • Impact: Rescues creditworthy loans for revenue        │
│                                                          │
│  [Catch Layer - FN → TP]                                 │
│  • Criteria: LTI > 0.35 + Interest Rate > 15%            │
│  • Impact: Overrides model to prevent capital loss       │
└──────────────────────────────────────────────────────────┘
           │
           ▼
Final Calibrated Risk Decision
```

---

# 📊 Power BI Dashboard & Decision Support System

The Power BI solution translates complex statistical probabilities into an interactive decision-support interface for credit underwriters and risk committees.

## 8. Multi-Tier Review Framework

Rather than automating binary approvals, applications are mapped into **Three Actionable Review Tiers**:

```text
┌───────────────────────────────────────────────────────────────────────────┐
│                      CREDIT UNDERWRITING TIERS                            │
├─────────────────┬───────────────────┬─────────────────────────────────────┤
│   Risk Tier     │  Estimated PD     │ Recommended Underwriting Action     │
├─────────────────┼───────────────────┼─────────────────────────────────────┤
│ 🟢 Tier 1 (Low) │    PD < 20%       │ Fast-track standard approval        │
│ 🟡 Tier 2 (Mid) │ 20% ≤ PD ≤ 50%    │ Enhanced due diligence & collateral │
│ 🔴 Tier 3 (High)│    PD > 50%       │ Policy override / Direct rejection  │
└─────────────────┴───────────────────┴─────────────────────────────────────┘
```

### 🖥️ Dashboard Analytical Views
* **Executive Summary:** Portfolio KPIs, overall NPL volume, and portfolio default distribution.
* **Portfolio Segmentation:** Interactive breakdowns by Loan Purpose, Term, Age Group, and Income Bracket.
* **Risk Driver Matrix:** Real-time exploration of LTI vs. Interest Rate intersections.
* **Model Diagnostic Page:** ROC Curve, confusion matrix toggles, and probability threshold simulators.
* **Underwriter Decision Workbench:** Case-by-case lookup with customer risk scorecard profiling.

---

## 9. Repository Structure

```text
├── docs/
│   ├── PIPELINE.md               # End-to-end technical pipeline specification
│   ├── HIEN_TRANG_HE_THONG.md    # System architecture & deployment status
│   └── NHAT_KY_CONG_VIEC.md      # Development engineering changelog
├── images/
│   └── credit_risk_workflow.png  # High-resolution pipeline infographic
├── repo_source/
│   ├── step_1/                   # Data ingestion, cleaning & stratified split
│   ├── step_2/                   # Baseline Logistic Regression model training
│   ├── step_3/                   # Model inference & prediction splitting
│   ├── step_4/                   # FP/FN audit, contribution analysis & LTI cut-offs
│   ├── run_pipeline.py           # Master execution script (Steps 1 to 4)
│   ├── db_import.py              # PostgreSQL database ingestion script
│   └── metrics_after_cut.py      # Final metrics calculation & audit script
├── Phân tích nợ xấu.pbix         # Interactive Power BI report file
└── README.md                     # Project documentation
```

---

## 10. Execution & Reproduction Guide

### Prerequisites
* Python 3.10+
* PostgreSQL (Optional, for database storage)

### Installation
```bash
# Clone the repository
git clone https://github.com/your-username/credit-risk-analytics.git
cd credit-risk-analytics

# Create and activate virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r repo_source/requirements.txt
```

### Running the End-to-End Pipeline
Execute the full data pipeline from raw dataset to final evaluated predictions:
```bash
python repo_source/run_pipeline.py
```

### Auditing Final Evaluation Metrics
```bash
python repo_source/metrics_after_cut.py
```

---

# 📚 What I Learned

### Data Analytics

- Translating a business problem into analytical questions
- Building derived financial indicators such as DTI and LTI
- Segmenting a portfolio by meaningful risk dimensions
- Building Power BI dashboards around KPIs and business questions
- Turning exploratory results into concise business findings

### Machine Learning

- Building a Logistic Regression baseline
- Designing financial and interaction features
- Handling skewed variables with transformation
- Standardizing model inputs
- Evaluating ROC-AUC, Recall, Accuracy and Specificity
- Reading confusion matrices and investigating FP/FN cases

### Analytics + ML

- Connecting descriptive patterns with model outputs
- Interpreting model features in a business context
- Using error analysis to design additional review rules
- Communicating model results as decision-support information

---

# ⚠️ Limitations & Responsible Use

This project is a portfolio/analytical implementation and should not be treated as a production credit-decision system.

- Observed relationships in the dataset do not by themselves establish causality.
- Risk-group thresholds are review guidance, not automatic approval/rejection rules.
- Model performance depends on the dataset and evaluation setup.
- The current Logistic Regression model may not capture nonlinear relationships as well as more advanced models.
- The Power BI report is intended to support human review rather than replace credit policy, compliance requirements or professional judgement.
- The Power BI semantic model and database may require synchronization after pipeline changes.

---

# 📖 Documentation

- [`PIPELINE.md`](docs/PIPELINE.md) — end-to-end processing pipeline and model workflow
- [`HIEN_TRANG_HE_THONG.md`](docs/HIEN_TRANG_HE_THONG.md) — current system/database state
- [`NHAT_KY_CONG_VIEC.md`](docs/NHAT_KY_CONG_VIEC.md) — project work log
- [`Phân tích nợ xấu.pdf`](Phân%20tích%20nợ%20xấu.pdf) — exported Power BI report

---

## 💼 Skills Demonstrated

<div align="center">

`Data Analysis` · `EDA` · `Power BI` · `DAX` · `Excel` · `Business Intelligence` ·  
`Python` · `pandas` · `scikit-learn` · `Logistic Regression` · `Feature Engineering` ·  
`Model Evaluation` · `PostgreSQL` · `Risk Analytics` · `Decision Support`

</div>

---

<div align="center">

### Author

**Đức**

_Data Analyst / Data Science Portfolio_

**Project Timeline:** 10/08/2026 – Present

</div>
