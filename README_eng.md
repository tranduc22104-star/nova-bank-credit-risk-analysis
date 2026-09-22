<div align="center">

# Credit Risk Analysis & Default Prediction
[English](README_eng.md) | Vietnamese
### Data Analytics + Machine Learning | Power BI | Python | PostgreSQL

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
</p>

<p>
  An end-to-end <strong>Data Analytics + Machine Learning</strong> project,
  focusing on credit risk analysis, default prediction, model evaluation, and risk review support.
</p>

</div>

---

## 📌 Project Overview

### 🏢 Business Context

Management needs a comprehensive view of the **customer loan portfolio** to monitor loan applications, assess credit characteristics, and manage potential credit risks.

The project consolidates key information including **customer characteristics, loan information, credit history, repayment behavior, and risk indicators**, providing a data-driven view of portfolio quality and supporting the assessment of new credit applications.

### 🎯 Project Objective

The project combines **Data Analytics and Data Science** to:

- 📊 Monitor and analyze the overall **loan portfolio**
- 🔍 Analyze **customer and credit characteristics**
- ⚠️ Identify factors associated with **credit risk**
- 🤖 Build a predictive model to estimate the **probability of credit risk**
- 📈 Develop an interactive dashboard to support **portfolio monitoring and decision-making**

### 💡 Project Outcome

The final solution integrates **business analysis, data visualization, and Machine Learning** to provide:

- **Business Insights** — Understand customer characteristics, loan characteristics, and risk patterns within the portfolio.
- **Risk Analysis** — Identify key factors associated with credit risk and analyze model prediction results.
- **Predictive Assessment** — Estimate the probability of credit risk using a Machine Learning model.
- **Decision Support** — Provide interactive visualizations and data-driven analysis to support credit assessment and portfolio management.

The final Power BI report combines these two perspectives to support **credit risk review and decision-making**. The report is not intended to replace the bank's formal credit policy or automatically approve/reject applications.

---

## 🔄 Credit Risk Analysis Workflow: From Raw Data to Actionable Insights

The project implements an **end-to-end Credit Risk Analysis workflow**, combining **Data Analytics, Data Science, SQL, and Business Intelligence (BI)** to transform raw credit data into actionable insights for portfolio monitoring and credit decision-making.

<div align="center">
  <img src="images/credit_risk_workflow.png" alt="Credit Risk Analysis Workflow" width="100%" />
</div>

- **Step 1 - Raw Credit Data (Microsoft Excel):**
  - Collect and manage input data including **loan applications, customer information, credit history, loan history, transaction data, and reference data**.

- **Step 2 - Data Preparation & Exploratory Data Analysis (Python & Pandas):**
  - Perform **data cleaning**, handle missing values, check data quality, analyze distributions and relationships between variables, and explore **potential data patterns and risk indicators** before model development.

- **Step 3.1 - Model Development & Evaluation (Scikit-learn):**
  - Build a **Logistic Regression** model to predict credit risk. Split the data into training/testing sets and evaluate the model using **Accuracy, Precision, Recall, F1-score, ROC-AUC, and Confusion Matrix**.

- **Step 3.2 - Data Segmentation & Risk Management Dashboard Development (Power BI):**
  - Perform **customer and loan segmentation** based on credit characteristics and risk indicators. Build a **Risk Management Dashboard** to visualize customer segments, portfolio characteristics, and key risk metrics for analysis.

- **Step 4 - False Positive (FP) / False Negative (FN) Case Analysis (DBeaver - SQL):**
  - Use **SQL** to compare predicted results with actual outcomes, identify **False Negative (FN)** and **False Positive (FP)** cases, and analyze the customer and loan characteristics associated with incorrect model predictions.

- **Step 5 - Risk Adjustment (Python):**
  - Analyze FP/FN results and **adjust model predictions** based on identified risk characteristics, preparing **final risk scores and classification results** for business analysis.

- **Step 6 - Decision Support (Power BI):**
  - Consolidate results from **data analysis and predictive modeling** into an interactive dashboard to support **loan portfolio monitoring, risk assessment, and credit decision-making**.

---

# 📊 Data Analysis

## 1. Data Understanding

The project begins by understanding four key information groups used to describe credit risk:

| Data Group | Examples | Purpose |
|---|---|---|
| Customer Profile | Age, employment, housing | Assess customer stability |
| Financial Capacity | Income, DTI, LTI | Assess repayment capacity |
| Loan Information | Loan amount, purpose, term, interest rate | Understand loan size and cost |
| Credit History | Previous defaults, credit history, late payments | Assess past credit behavior |

The Power BI report includes a dedicated **Data Dictionary** page explaining the meaning and usage of important variables and model-related terms.

---

## 2. Calculated Risk Metrics

Several metrics are calculated to make credit analysis easier to interpret.

### DTI — Debt-to-Income Ratio

```text
DTI = (Loan Amount + Other Debt) / Annual Income
```

Measures the total debt burden relative to annual income.

### LTI — Loan-to-Income Ratio

```text
LTI = Loan Amount / Annual Income
```

Measures the requested loan size relative to annual income.

### Default Rate

```text
Default Rate = Number of Default Cases / Total Number of Cases
```

These metrics are used throughout the Power BI analysis and model development workflow.

---

## 3. Exploratory Data Analysis (EDA) & Insights

The portfolio analysis focuses on the core business question:

**"Where is default risk concentrated?"**

The analysis examines customer segments and loan structures across the full dataset of **32,566 applications**.

### 📌 Portfolio Overview Metrics

<div align="center">

| Total Applications | Default Applications | Overall Default Rate | Total Default Loan Amount |
| :---: | :---: | :---: | :---: |
| **32,566** | **7,107** | **21.82%** | **VND 2,010 billion** |

</div>

### 💡 Key Strategic Insights

**01. DEBT BURDEN:**
* **Default risk increases sharply with financial leverage:** Both LTI and DTI show a very strong positive relationship with default risk.
* The **LTI ≥ 0.40** group records a default rate of **74.54%** (6.5 times higher than the safer < 0.10 group at 11.51%).
* The **DTI ≥ 0.70** group reaches a default rate of **79.04%** (7.1 times higher than the < 0.20 group at 11.08%).
* *Risk exposure:* The **LTI 0.30 – 0.40** segment carries the largest default loan amount across the portfolio at **VND 673.8 billion**, while the **DTI 0.35 – 0.70** segment contains **VND 1,477.2 billion** in default loan exposure.

**02. BORROWING COSTS:**
* **Higher interest rates create greater repayment pressure:** The higher the interest rate, the more severe the default risk. Customers with interest rates **≥ 16%** have a default rate of up to **63.23%**.
* The high-rate **12 – 15.99%** segment holds the largest amount of default loan exposure in the portfolio (**VND 799.3 billion**, approximately 40% of total default loan exposure), indicating that high borrowing costs can directly increase monthly repayment pressure.

**03. INCOME CAPACITY:**
* **Income provides a protective financial buffer:** Default rates show a clear inverse relationship with customer income.
* The lowest-income group (**< VND 782 million**) has a default rate of **47.08%**, while the rate continuously declines to only **8.73%** for the high-income group (**≥ VND 3.91 billion**).
* The middle-income segment (**VND 782 million – 1.96 billion**) accumulates the largest amount of default loan exposure in the portfolio (**VND 1,330.8 billion**), requiring stronger cash-flow assessment rather than relying solely on nominal income levels.

---

# 🤖 Machine Learning: Default Prediction

## 4. Model Architecture & Preprocessing Workflow

The predictive modeling framework uses **Logistic Regression** to estimate the **Probability of Default (PD)**.

The workflow ensures data integrity through an **80% Training / 20% Testing stratified split** based on repayment status.

```text
Original Dataset (32,566 rows)
         │
         ▼  80/20 Stratified Split
┌─────────────────────────┬────────────────────────────────┐
│ Training Set (26,052 rows) │ Testing Set (6,514 rows) │
└─────────────────────────┴────────────────────────────────┘
         │
         ▼
Raw Probability Prediction (Testing Set)
         │
         ▼
Risk Adjustment Layer (LTI Thresholds & Business Rules)
         │
         ▼
Final Validated Credit Risk Assessment
```

---

## 5. Feature Importance & Variable Contribution

The relative contribution of each feature is quantified using the absolute standardized value of the model coefficient, adjusted for the standard deviation of each feature to ensure comparability across variables with different scales:

<div align="center">

| Rank | Feature Name | Contribution (%) | Business Interpretation |
| :---: | :--- | :---: | :--- |
| **01** | **Loan-to-Income Ratio (LTI)** | **38.28%** | Primary risk factor: excessive leverage relative to annual income capacity. |
| **02** | **Loan Interest Rate (%)** | **28.16%** | Direct borrowing cost that increases monthly repayment pressure. |
| **03** | **Requested Loan Amount (VND)** | **20.43%** | Exposure size: larger loans increase potential loss exposure in the event of default. |
| **04** | **Annual Income (VND)** | **4.44%** | Income-generating capacity and financial buffer for repayment. |
| **05** | **Home Ownership Status** | **3.04%** | Indicator of personal asset stability and collateral strength. |
| **06** | **Previous Default History** | **2.77%** | Past credit delinquency and repayment behavior. |
| **07** | **Debt-to-Income Ratio (DTI)** | **2.44%** | Total debt burden from multiple financial obligations. |
| **08** | **Loan Purpose** | **0.43%** | Segmentation of the intended use of borrowed funds. |
| | **Total** | **100.00%** | **Top 3 features account for 86.87% of the model's total decision weight.** |

</div>

---

## 6. Model Evaluation & Performance Metrics

The model is evaluated on the **unseen Test Set (6,514 applications)** after integrating the risk adjustment layer from Step 5.

### 📈 Performance Overview

<div align="center">

| Metric | Result | Industry Benchmark & Interpretation |
| :--- | :---: | :--- |
| **Accuracy** | **94.80%** | Overall proportion of correctly classified good and default loans. |
| **ROC-AUC** | **0.7264** | Ability to discriminate between defaulting and non-defaulting customers. |
| **Recall** | **92.41%** | Correctly identifies **92.41%** of all actual default cases in the portfolio. |
| **Precision** | **85.05%** | When the model flags default risk, the prediction is correct **85.05%** of the time. |
| **Specificity** | **95.46%** | Correctly protects **95.46%** of customers who can repay from being incorrectly rejected. |
| **F1-score** | **88.57%** | Balance between detecting risk and retaining good customers. |
| **K-S Statistic** | **0.3542** | Ability to separate different risk groups. |
| **PR-AUC** | **0.4492** | Discriminative performance under imbalanced credit data (~21.8% default rate). |
| **Brier Score / Log Loss** | **0.2004 / 0.5871** | Reliability of predicted probabilities. |

</div>

### 🎯 Confusion Matrix (Test Set: 6,514 Applications)

<div align="center">

| | **Predicted: Default (Risk Alert)** | **Predicted: Non-default (Approved)** |
| :--- | :---: | :---: |
| **Actual: Default (1,422 cases)** | **1,314 TP** *(Default detected)* | **108 FN** *(Default missed)* |
| **Actual: Non-default (5,092 cases)** | **231 FP** *(False alert)* | **4,861 TN** *(Good loan approved)* |

</div>

---

# 🔍 Deep-Dive Analysis: FP / FN Using SQL & Business Adjustment

## 7. Error Checking & Cost-Based Analysis (DBeaver / SQL)

### 🟢 1. FP → TN Layer (*Clearing Good Customers*)

* **Target:** `prediction_test_non_default.csv` (all **5,092 cases** that did not actually default).
* **Initial Results Before Adjustment:**
  * **TN (Correctly Approved):** **3,704 cases**
  * **FP (False Alert / Incorrect Rejection):** **1,388 cases**
* **Adjustment Condition:**
  $$\mathbf{0.1987 \le LTI \le 0.342}$$
* **Cases Cleared:** **1,157 cases** were moved from **FP → TN** (customers with repayment capacity were given another opportunity to borrow).
* **Remaining Cases:** **231 cases** remained FP (retaining a conservative risk buffer).
* **Results After Adjustment:**
  * **TN increased:** $3,704 \rightarrow \mathbf{4,861 \text{ cases}}$
  * **FP decreased:** $1,388 \rightarrow \mathbf{231 \text{ cases}}$ *(83.36% of false alerts eliminated)*

### 🔴 2. FN → TP Layer (*Capturing Hidden Defaults*)

* **Target:** `prediction_test_has_default.csv` (all **1,422 cases** that actually defaulted).
* **Initial Results Before Adjustment:**
  * **TP (Default Detected):** **865 cases**
  * **FN (Missed Default / Leakage):** **557 cases**
* **Adjustment Condition:**
  $$\mathbf{0.0653 \le LTI \le 0.1907}$$
* **Cases Recovered:** **449 cases** were moved from **FN → TP** (reducing the risk of significant capital losses).
* **Remaining Cases:** **108 cases** remained FN (monitored and referred to the credit committee for manual review).
* **Results After Adjustment:**
  * **TP increased:** $865 \rightarrow \mathbf{1,314 \text{ cases}}$
  * **FN decreased:** $557 \rightarrow \mathbf{108 \text{ cases}}$ *(80.61% of missed defaults recovered)*

---

## 8. Decision Support System

## 📊 Analysis of Actual Default Cases by Predicted Probability of Default from the Logistic Regression Model

### 🟢 Level 1 – Groups with a probability of default below 25%

**Characteristics:**
- Customers have the highest income (**VND 3.3 billion**).
- Very low debt burden (**LTI = 0.06; DTI = 0.24**).
- Collateral-backed loans account for the majority (**59%**).
- Primarily customers taking out debt consolidation loans.

**Issue:**
- **58%** of customers have a previous default history.
- However, the model predicts a **0% probability of default**, making this group difficult to detect if relying only on conventional financial indicators.

---

### 🟡 Level 2 – Groups with a probability of default from 25% to below 50%

**Characteristics:**
- Income of approximately **VND 1.3 billion**.
- Smallest loan amount (**VND 158 million**).
- **LTI = 0.12; DTI = 0.29**.
- Home purchase loans account for approximately **27%**.

**Issue:**
- **62.5%** of customers have a previous default history.
- However, the model still estimates a probability of default **below 50%**.
- Therefore, this group may **pass through the standard risk assessment process**.

---

### 🟠 Level 3 – Groups with a probability of default from 50% to below 75%

**Characteristics:**
- Has the highest proportion of applications.
- Lowest income (**VND 1.07 billion**).
- Debt burden increases significantly (**LTI = 0.31; DTI = 0.49**).
- Highest proportion of renters (**79%**).
- Highest previous default rate (**73.8%**).

**Performance:**
- The model correctly identifies **100% of customers** falling into the default group.
- Although this group has a relatively low loan interest rate (**12.37%**).

---

### 🔴 Level 4 – Groups with a probability of default of 75% or higher

**Characteristics:**
- Debt burden exceeds the safe threshold (**LTI = 0.43; DTI = 0.61**).
- Highest loan income among the groups (**VND 637 million**).
- Approximately **77%** of customers are renters.

**Performance:**
- The model correctly captures **100% of default cases**.

### What Should Be Checked for High-Risk Applications?

| # | Aspect | Key Indicators | Guidance |
| :---: | :--- | :--- | :--- |
| 01 | **Data Quality** | Missing · Anomalies · Outdated | Verify input data before relying on model results. |
| 02 | **Repayment Capacity** | Income · DTI · LTI | Assess financial burden; do not conclude based on a single variable. |
| 03 | **Loan Structure** | Loan Amount · Interest Rate · Term | Review loan size and cost relative to financial capacity. |
| 04 | **Credit History** | Previous Default · Credit Tenure | Check past credit behavior before concluding risk level. |
| 05 | **Verification & Authority** | Documents · Third-Party Verification | Verify high-risk or incomplete cases; escalate for review when necessary and strictly comply with data privacy requirements. |

### Segments with High Default Rates Requiring Priority Review

> *Used to guide deeper review — not as an automatic rejection threshold.*

| Risk Segment | Observed Default Rate |
| :--- | :---: |
| Debt-to-Income Ratio (DTI) ≥ 0.70 | ≈ **79.0%** |
| Loan-to-Income Ratio (LTI) ≥ 0.40 | ≈ **74.5%** |
| Loan Interest Rate ≥ 16% | ≈ **63.2%** |
| Income < VND 782 million/year | ≈ **47.1%** |
| Previous Default History | ≈ **37.8%** *(vs. ~18.4% for the non-default group)* |

> **General Principle:** Conduct a multidimensional assessment (financial capacity + loan structure + credit behavior + data quality); do not use model probability to automatically reject applications; comply with applicable laws and personal data privacy requirements in all verification activities.

---

## 9. Project Structure

```text
├── docs/
│   ├── PIPELINE.md               # End-to-end technical process specification
│   ├── HIEN_TRANG_HE_THONG.md    # System architecture & implementation status
│   └── NHAT_KY_CONG_VIEC.md      # Project development log
├── images/
│   └── credit_risk_workflow.png  # High-resolution workflow infographic
├── repo_source/
│   ├── step_1/                   # Data loading, cleaning & stratified splitting
│   ├── step_2/                   # Baseline Logistic Regression model training
│   ├── step_3/                   # Model inference & prediction result separation
│   ├── step_4/                   # FP/FN checking, contribution analysis & LTI thresholds
│   ├── run_quy trình.py          # Main execution script (Steps 1 to 4)
│   ├── db_import.py              # PostgreSQL data loading script
│   └── metrics_after_cut.py      # Final metric calculation & validation script
├── Phân tích nợ xấu.pbix         # Interactive Power BI dashboard report
└── README.md                     # Project documentation
```

# 📚 What I Learned

### Data Analysis

- Translate business problems into analytical questions
- Build financial metrics such as DTI and LTI
- Segment the portfolio across meaningful risk dimensions
- Build Power BI dashboards around business metrics and questions
- Turn EDA results into concise business findings

### Machine Learning

- Build a baseline Logistic Regression model
- Design financial and interaction features
- Handle skewed variables through transformations
- Standardize model inputs
- Evaluate ROC-AUC, Recall, Precision, and Specificity
- Read Confusion Matrices and investigate FP/FN cases

### Data Analytics + Machine Learning

- Connect descriptive patterns with model results
- Interpret model features in a business context
- Use error analysis to design additional review rules
- Communicate model results as decision-support information

---

# 📖 Documentation

- [`PIPELINE.md`](docs/PIPELINE.md) — end-to-end processing workflow and model workflow
- [`HIEN_TRANG_HE_THONG.md`](docs/HIEN_TRANG_HE_THONG.md) — current system/database status
- [`NHAT_KY_CONG_VIEC.md`](docs/NHAT_KY_CONG_VIEC.md) — project implementation log
- [`Phân tích nợ xấu.pdf`](Phân%20tích%20nợ%20xấu.pdf) — Power BI report exported as PDF

---

## 💼 Skills Demonstrated

<div align="center">

`Data Analytics` · `Exploratory Data Analysis` · `Power BI` · `DAX` · `Excel` · `Business Intelligence` ·  
`Python` · `pandas` · `scikit-learn` · `Logistic Regression` · `Feature Engineering` ·  
`Model Evaluation` · `PostgreSQL` · `Risk Analysis` · `Decision Support`

</div>

---

<div align="center">

### Author

**Đức**

_Data Analytics / Data Science Portfolio_

</div>
