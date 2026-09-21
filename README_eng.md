<div align="center">

# Credit Risk Analysis & Default Prediction

### Data Analytics + Machine Learning | Power BI | Python | PostgreSQL

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/Status-In%20Progress-7B61FF?style=for-the-badge">
</p>

<p>
  An <strong>Data Analytics + Machine Learning</strong> project following an end-to-end workflow,
  focused on credit risk analysis, default prediction, model evaluation, and risk review support.
</p>

</div>

---

## 📌 Project Overview

### 🏢 Business Context

Management needs a comprehensive view of the **customer loan portfolio** to monitor loan applications, assess credit characteristics, and manage potential credit risks.

The project consolidates key information including **customer characteristics, loan information, credit history, repayment behavior, and risk indicators**, providing a data-driven view of portfolio quality and supporting the assessment of new loan applications.

### 🎯 Project Objective

The project combines **Data Analysis and Data Science** to:

- 📊 Monitor and analyze the overall **loan portfolio**
- 🔍 Analyze **customer and credit characteristics**
- ⚠️ Identify factors associated with **credit risk**
- 🤖 Build a model to predict the **probability of credit default**
- 📈 Develop an interactive dashboard to support **portfolio monitoring and decision-making**

### 💡 Project Outcome

The final solution integrates **business analysis, data visualization, and Machine Learning** to provide:

- **Business Insights** — Understand customer characteristics, loan characteristics, and risk patterns across the portfolio.
- **Risk Analysis** — Identify key factors associated with credit risk and analyze model prediction results.
- **Prediction Evaluation** — Estimate the probability of credit default using a Machine Learning model.
- **Decision Support** — Provide interactive visualizations and data-driven analyses to support credit assessment and portfolio management.

The final Power BI report combines these perspectives to support **credit risk review and decision-making**. It is not intended to replace the bank's official credit policy or automatically approve/reject loan applications.

---

## 🔄 Credit Risk Analysis Workflow: From Raw Data to Actionable Insights

The project implements an **end-to-end Credit Risk Analysis workflow**, combining **Data Analysis, Data Science, SQL, and Business Intelligence (BI)** to transform raw credit data into actionable insights that support portfolio monitoring and credit decision-making.

<div align="center">
  <img src="images/credit_risk_workflow.png" alt="Credit Risk Analysis Workflow" width="100%" />
</div>

* **Step 1 - Raw Credit Data (Microsoft Excel):**
  * Collect and manage raw data including **loan applications, customer information, credit history, loan history, transaction data, and reference data**.

* **Step 2 - Data Preparation & EDA (Python & Pandas):**
  * Perform **data cleaning**, handle missing values, check data quality, analyze distributions and relationships between variables, and identify **potential risk patterns and indicators** before model development.

* **Step 3 - Model Building & Evaluation (Scikit-learn):**
  * Build a **Logistic Regression** classification model to predict credit risk. Perform a train/test split, hyperparameter tuning, and model evaluation using **Accuracy, Precision, Recall, F1-Score, ROC-AUC, and Confusion Matrix**.

* **Step 4 - FP / FN Analysis (DBeaver - SQL):**
  * Use **SQL** to compare predicted outcomes with actual outcomes, identify **False Negative (FN)** and **False Positive (FP)** cases, and analyze customer and loan characteristics associated with model misclassifications.

* **Step 5 - Risk Adjustment (Python Rules):**
  * Apply **business rules** based on FP/FN analysis to adjust model predictions, refine risk classification, and generate **Final Risk Scores / Risk Segments** for business analysis.

* **Step 6 - Decision Support (Power BI):**
  * Build an **interactive Power BI dashboard** to visualize the loan portfolio, risk segments, customer characteristics, and key risk indicators, supporting **portfolio monitoring, risk assessment, and credit decision-making**.

---

# 📊 Data Analysis

## 1. Data Understanding

The project begins by examining four main groups of information used to describe credit risk:

| Data Group | Examples | Purpose |
|---|---|---|
| Customer Profile | Age, employment, home ownership | Assess customer stability |
| Financial Capacity | Income, DTI, LTI | Assess repayment capacity |
| Loan Information | Loan amount, purpose, term, interest rate | Understand loan size and borrowing cost |
| Credit History | Previous default, credit history length, late payments | Assess past credit behavior |

The Power BI report includes a dedicated **Data Dictionary** page explaining the meaning and usage of key variables and model terminology.

---

## 2. Calculated Risk Metrics

Several metrics are calculated to make credit analysis easier to interpret.

### DTI — Debt-to-Income Ratio

```text
DTI = (Loan Amount + Other Debt) / Annual Income
```

Reflects the total debt burden relative to annual income.

### LTI — Loan-to-Income Ratio

```text
LTI = Loan Amount / Annual Income
```

Measures the requested loan amount relative to annual income.

### Default Rate

```text
Default Rate = Number of Default Cases / Total Cases
```

These metrics are used throughout the Power BI analysis and model development workflow.

---

## 3. Exploratory Data Analysis (EDA) & Insights

The portfolio analysis focuses on answering the core business question:

**"Where are defaults concentrated?"**

The analysis examines customer segments and loan structures across all **32,566 applications**.

### 📌 Portfolio Overview KPIs

<div align="center">

| Total Applications | Default Cases | Overall Default Rate | Total Defaulted Loan Amount |
| :---: | :---: | :---: | :---: |
| **32,566** | **7,107** | **21.82%** | **2,010 billion VND** |

</div>

### 💡 Key Strategic Insights

> [!IMPORTANT]
> **01. DEBT BURDEN:**
> * **Default risk rises sharply with financial leverage:** Both LTI and DTI show a strong positive relationship with default risk.
> * Borrowers with **LTI ≥ 0.40** record a **74.54%** default rate, approximately **6.5 times** the 11.51% rate of the low-risk group with LTI < 0.10.
> * The **DTI ≥ 0.70** group reaches a default rate of **79.04%**, approximately **7.1 times** the 11.08% rate of the DTI < 0.20 group.
> * *Risk exposure:* The **LTI 0.30–0.40** segment carries the largest defaulted loan amount at **673.8 billion VND**, while the **DTI 0.35–0.70** segment contains **1,477.2 billion VND** in defaulted loans.

> [!WARNING]
> **02. BORROWING COSTS:**
> * **Higher interest rates are associated with greater repayment pressure:** Customers with interest rates **≥ 16%** have a default rate of **63.23%**.
> * The **12–15.99%** interest-rate segment holds the largest defaulted loan amount in the portfolio at **799.3 billion VND**, accounting for approximately 40% of total defaulted loan value, indicating substantial repayment pressure from borrowing costs.

> [!TIP]
> **03. EARNING CAPACITY:**
> * **Higher income provides a stronger financial buffer:** Default rates decline clearly as customer income increases.
> * The lowest-income group (**< 782 million VND**) has a default rate of **47.08%**, while the rate steadily falls to **8.73%** among high-income customers (**≥ 3.91 billion VND**).
> * The middle-income segment (**782 million–1.96 billion VND**) accumulates the largest defaulted loan value at **1,330.8 billion VND**, suggesting that cash-flow assessment should remain important rather than relying only on nominal income.

---

# 🤖 Machine Learning: Default Prediction

## 4. Model Architecture & Preprocessing Workflow

The predictive framework uses **Logistic Regression** to estimate the **Probability of Default (PD)**.

Data integrity is maintained through a **Stratified 80/20 Train/Test Split** based on repayment status.

```text
Original Dataset (32,566 rows)
         │
         ▼  Stratified 80/20 Split
┌─────────────────────────────┬─────────────────────────┐
│ Training Set (26,052 rows)  │ Test Set (6,514 rows)  │
└─────────────────────────────┴─────────────────────────┘
         │
         ▼
Raw Probability Predictions (Test Set)
         │
         ▼
Risk Adjustment Layer (LTI Thresholds & Business Rules)
         │
         ▼
Final Validated Credit Risk Assessment
```

---

## 5. Feature Importance & Variable Contribution

The relative contribution of each feature is quantified using the normalized absolute value of the model coefficient, adjusted by each feature's standard deviation to ensure comparability across variables with different scales:

<div align="center">

| Rank | Feature Name | Contribution (%) | Business Interpretation |
| :---: | :--- | :---: | :--- |
| **01** | **Loan-to-Income Ratio (LTI)** | **38.28%** | Primary risk factor: excessive leverage relative to annual income capacity. |
| **02** | **Loan Interest Rate (%)** | **28.16%** | Higher debt cost directly increases monthly repayment pressure. |
| **03** | **Requested Loan Amount (VND)** | **20.43%** | Exposure size: larger loans increase potential loss when default occurs. |
| **04** | **Annual Income (VND)** | **4.44%** | Income-generating capacity and financial buffer for debt repayment. |
| **05** | **Home Ownership Status** | **3.04%** | Indicator of personal asset stability and financial position. |
| **06** | **Previous Default History** | **2.77%** | Historical credit delinquency and past repayment discipline. |
| **07** | **Debt-to-Income Ratio (DTI)** | **2.44%** | Total debt burden across multiple financial obligations. |
| **08** | **Loan Purpose** | **0.43%** | Categorizes the intended use of borrowed funds. |
| | **Total** | **100.00%** | **The top 3 features account for 86.87% of the model's total feature contribution.** |

</div>

---

## 6. Model Evaluation & Performance Metrics

The model is evaluated on an **unseen Test Set of 6,514 applications** after integrating the risk adjustment layer from Step 5.

### 📈 Performance Overview

<div align="center">

| Metric | Result | Interpretation |
| :--- | :---: | :--- |
| **Accuracy** | **94.80%** | Overall proportion of correctly classified good and defaulted loans. |
| **ROC-AUC** | **0.8593** | Ability to discriminate between defaulting and non-defaulting customers. |
| **Recall (Sensitivity)** | **92.41%** | Correctly identifies **92.41%** of actual default cases in the portfolio. |
| **Precision** | **85.05%** | When the model flags a default risk, it is correct **85.05%** of the time. |
| **Specificity** | **95.46%** | Correctly identifies **95.46%** of non-defaulting customers. |
| **F1-Score** | **88.57%** | Balances default detection and prediction precision. |
| **K-S Statistic** | **0.5850** | Indicates strong separation between risk groups. |
| **PR-AUC** | **0.7450** | Measures precision-recall performance under class imbalance (~21.8% defaults). |
| **Brier Score / Log Loss** | **0.101 / 0.335** | Measures the quality and reliability of predicted probabilities. |

</div>

### 🎯 Confusion Matrix (Test Set: 6,514 Applications)

<div align="center">

| | **Predicted: Default (Risk Alert)** | **Predicted: Non-Default** |
| :--- | :---: | :---: |
| **Actual: Default (1,422 cases)** | **1,314 TP** *(Defaults detected)* | **108 FN** *(Defaults missed)* |
| **Actual: Non-Default (5,092 cases)** | **231 FP** *(False alerts)* | **4,861 TN** *(Good loans correctly identified)* |

</div>

---

# 🔍 Deep-Dive Analysis: FP / FN Using SQL & Business Rule Adjustment

## 7. Error Audit & Cost-Sensitive Analysis (DBeaver / SQL)

### 🟢 1. Rescue Layer: FP → TN (*Recovering Good Customers*)

* **Scope:** `prediction_test_non_default.csv` (all **5,092 applications** that did not actually default).
* **Baseline before adjustment:**
  * **TN (Correct Non-Default Predictions):** **3,704 cases**
  * **FP (False Alerts):** **1,388 cases**
* **Adjustment Condition:**
  $$\mathbf{0.1987 \le LTI \le 0.342}$$
* **Cases Rescued:** **1,157 cases** are moved from **FP → TN**, restoring lending opportunities for customers who were actually able to repay.
* **Remaining Cases:** **231 cases** remain FP, preserving a conservative risk buffer.
* **Post-Adjustment Result:**
  * **TN increases:** $3,704 \rightarrow \mathbf{4,861 \text{ cases}}$
  * **FP decreases:** $1,388 \rightarrow \mathbf{231 \text{ cases}}$ *(83.36% of false alerts removed)*

### 🔴 2. Catch Layer: FN → TP (*Catching Hidden Defaults*)

* **Scope:** `prediction_test_has_default.csv` (all **1,422 applications** that actually defaulted).
* **Baseline before adjustment:**
  * **TP (Defaults Detected):** **865 cases**
  * **FN (Missed Defaults):** **557 cases**
* **Adjustment Condition:**
  $$\mathbf{0.0653 \le LTI \le 0.1907}$$
* **Cases Recovered:** **449 cases** are moved from **FN → TP**, reducing the risk of missed default cases.
* **Remaining Cases:** **108 cases** remain FN and are monitored or escalated for manual credit review.
* **Post-Adjustment Result:**
  * **TP increases:** $865 \rightarrow \mathbf{1,314 \text{ cases}}$
  * **FN decreases:** $557 \rightarrow \mathbf{108 \text{ cases}}$ *(80.61% of previously missed defaults recovered)*

---

## 8. Decision Support System

### Review Level by Risk Probability

| Level | Probability | Review Process |
| :---: | :---: | :--- |
| 🟢 **1** | < 20% | Standard review: verify KYC, income, DTI, LTI, loan purpose, default history, and duplicate applications. |
| 🟡 **2** | 20–35% | Enhanced review (including all Level 1 checks): perform detailed repayment-capacity analysis, request additional documents such as bank statements and employment contracts, cross-check information, and conduct verification calls when necessary. |
| 🔴 **3** | ≥ 35% | In-depth assessment: verify income sources, review unusually high DTI/LTI values, and cross-check Declaration ↔ Supporting Documents ↔ Bank Statements ↔ CIC. ⚠️ *Level 3 does not mean automatic rejection.* |

### What Should Be Checked for High-Risk Applications?

| # | Aspect | Key Indicators | Guidance |
| :---: | :--- | :--- | :--- |
| 01 | **Data Quality** | Missing · Anomalous · Outdated | Verify input data before relying on model results. |
| 02 | **Repayment Capacity** | Income · DTI · LTI | Assess the overall financial burden; do not conclude from a single variable. |
| 03 | **Loan Structure** | Loan Amount · Interest Rate · Term | Review loan size and borrowing cost relative to financial capacity. |
| 04 | **Credit History** | Previous Default · Credit History Length | Review past credit behavior before determining the level of risk. |
| 05 | **Verification & Authority** | Documents · Third-Party Verification | Verify high-risk or incomplete applications, escalate for further review when necessary, and strictly comply with data privacy requirements. |

### Segments with High Observed Default Rates Requiring Priority Review

> *Used to guide in-depth review — not as automatic rejection thresholds.*

| Risk Segment | Observed Default Rate |
| :--- | :---: |
| Debt-to-Income Ratio (DTI) ≥ 0.70 | ≈ **79.0%** |
| Loan-to-Income Ratio (LTI) ≥ 0.40 | ≈ **74.5%** |
| Loan Interest Rate ≥ 16% | ≈ **63.2%** |
| Annual Income < 782 million VND | ≈ **47.1%** |
| Previous Default History | ≈ **37.8%** *(vs. ~18.4% for customers without previous defaults)* |

> **General Principle:** Conduct a multi-dimensional assessment covering financial capacity, loan structure, credit behavior, and application quality. Do not use model probabilities for automatic rejection. Comply with applicable laws and protect personal data throughout all verification activities.

---

## 9. Repository Structure

```text
├── docs/
│   ├── PIPELINE.md               # End-to-end technical workflow specification
│   ├── HIEN_TRANG_HE_THONG.md    # System architecture & implementation status
│   └── NHAT_KY_CONG_VIEC.md      # Project development log
├── images/
│   └── credit_risk_workflow.png  # High-resolution workflow infographic
├── repo_source/
│   ├── step_1/                   # Data ingestion, cleaning & stratified split
│   ├── step_2/                   # Baseline Logistic Regression model training
│   ├── step_3/                   # Model inference & prediction result separation
│   ├── step_4/                   # FP/FN audit, contribution analysis & LTI thresholds
│   ├── run_pipeline.py           # Main execution script (Steps 1 to 4)
│   ├── db_import.py              # PostgreSQL data import script
│   └── metrics_after_cut.py      # Final metric calculation & validation script
├── Phân tích nợ xấu.pbix         # Interactive Power BI report file
└── README.md                     # Project documentation
```

---

## 10. Execution & Reproduction Guide

### Requirements

* Python 3.10+
* PostgreSQL (Optional, used for data storage)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/credit-risk-analytics.git
cd credit-risk-analytics

# Create and activate a virtual environment
python -m venv venv

# Windows:
.\venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r repo_source/requirements.txt
```

### Run the Full End-to-End Pipeline

Execute the complete data workflow from the raw dataset to the final prediction results:

```bash
python repo_source/run_pipeline.py
```

### Check Final Evaluation Metrics

```bash
python repo_source/metrics_after_cut.py
```

---

# 📚 What I Learned

### Data Analysis

- Translate business problems into analytical questions
- Build financial metrics such as DTI and LTI
- Segment the portfolio across meaningful risk dimensions
- Build a Power BI dashboard around KPIs and business questions
- Translate EDA results into concise business findings

### Machine Learning

- Build a baseline Logistic Regression model
- Design financial and interaction features
- Handle skewed variables using transformations
- Standardize model inputs
- Evaluate ROC-AUC, Recall, Accuracy, and Specificity
- Interpret the Confusion Matrix and investigate FP/FN cases

### Data Analytics + Machine Learning

- Connect descriptive patterns with model results
- Interpret model features in a business context
- Use error analysis to design additional review rules
- Communicate model results as decision-support information

---

# ⚠️ Limitations & Responsible Use

This project is a **portfolio/analytics implementation** and should not be considered a production credit decisioning system.

- Observed relationships in the dataset do not by themselves establish causality.
- Risk segmentation thresholds are intended only to guide review, not to serve as automatic approval/rejection rules.
- Model performance depends on the dataset and evaluation methodology.
- The current Logistic Regression model may not capture nonlinear relationships as effectively as more advanced models.
- The Power BI report is intended to support human review rather than replace credit policy, compliance requirements, or professional judgment.
- The Power BI semantic model and database may need to be synchronized again after pipeline changes.

---

# 📖 Documentation

- [`PIPELINE.md`](docs/PIPELINE.md) — end-to-end processing and model workflow
- [`HIEN_TRANG_HE_THONG.md`](docs/HIEN_TRANG_HE_THONG.md) — current system/database status
- [`NHAT_KY_CONG_VIEC.md`](docs/NHAT_KY_CONG_VIEC.md) — project execution log
- [`Phân tích nợ xấu.pdf`](Phân%20tích%20nợ%20xấu.pdf) — Power BI report exported as PDF

---

## 💼 Skills Demonstrated

<div align="center">

`Data Analysis` · `EDA` · `Power BI` · `DAX` · `Excel` · `Business Intelligence` ·  
`Python` · `pandas` · `scikit-learn` · `Logistic Regression` · `Feature Engineering` ·  
`Model Evaluation` · `PostgreSQL` · `Risk Analysis` · `Decision Support`

</div>

---

<div align="center">

### Author

**Đức**

_Data Analysis / Data Science Portfolio_

**Project Duration:** 10/08/2026 – Present

</div>
