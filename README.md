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

The portfolio analytics phase addresses the core business question: **"Where is Credit Default Risk Concentrated?"** (*Nợ xấu đang tập trung ở đâu?*), analyzing borrower segments and loan structures across all **32,566 applications**.

<div align="center">
  <img src="images/02_data_analytics.png" alt="Credit Default Analysis Dashboard" width="100%" />
</div>

### 📌 Portfolio High-Level KPIs

<div align="center">

| Total Applications (Số hồ sơ) | Default Cases (Hồ sơ nợ xấu) | Overall Default Rate (Tỷ lệ nợ xấu) | Total Bad Debt (Tổng tiền vay nợ xấu) |
| :---: | :---: | :---: | :---: |
| **32,566** | **7,107** | **21.82%** | **2,010 Billion VND** |

</div>

### 💡 Core Strategic Insights (*Nhận xét chính từ phân tích danh mục*)

> [!IMPORTANT]
> **01. GÁNH NẶNG NỢ (DEBT BURDEN):**
> * **Tỷ lệ nợ xấu leo thang phi mã theo đòn bẩy tài chính:** Cả hai chỉ số LTI và DTI đều cho thấy mối quan hệ đồng biến cực mạnh với rủi ro vỡ nợ.
> * Nhóm vay có **LTI ≥ 0.40** ghi nhận tỷ lệ nợ xấu **74.54%** (cao gấp **6.5 lần** so với nhóm an toàn < 0.10 ở mức 11.51%).
> * Nhóm **DTI ≥ 0.70** có tỷ lệ nợ xấu chạm đỉnh **79.04%** (cao gấp **7.1 lần** nhóm < 0.20 ở mức 11.08%).
> * *Quy mô rủi ro:* Phân khúc **LTI từ 0.30 – 0.40** gánh lượng nợ xấu lớn nhất toàn danh mục với **673.8 tỷ VND**, trong khi phân khúc **DTI từ 0.35 – 0.70** tập trung tới **1,477.2 tỷ VND** nợ xấu.

> [!WARNING]
> **02. CHI PHÍ VAY (BORROWING COSTS):**
> * **Lãi suất cao tạo vòng xoáy mất khả năng thanh toán:** Lãi suất càng cao, nợ xấu càng nghiêm trọng. Nhóm khách hàng chịu lãi suất **≥ 16%** có tỷ lệ nợ xấu lên tới **63.23%**.
> * Nhóm lãi suất cận cao **12 – 15.99%** nắm giữ khối lượng tiền vay nợ xấu lớn nhất danh mục (**799.3 tỷ VND**, chiếm ~40% tổng dư nợ xấu), cho thấy chi phí vốn nặng nề trực tiếp bóp nghẹt dòng tiền trả nợ hàng tháng.

> [!TIP]
> **03. NĂNG LỰC THU NHẬP (EARNING CAPACITY):**
> * **Lớp đệm thu nhập bảo vệ danh mục an toàn:** Tỷ lệ nợ xấu nghịch biến rõ rệt với quy mô thu nhập của khách hàng.
> * Nhóm thu nhập thấp nhất (**< 782 triệu VND**) có tỷ lệ vỡ nợ lên tới **47.08%**, nhưng tỷ lệ này giảm liên tục xuống chỉ còn **8.73%** ở nhóm có thu nhập cao (**≥ 3.91 tỷ VND**).
> * Phân khúc khách hàng trung lưu (**782 triệu – 1.96 tỷ VND**) là nhóm tích tụ giá trị nợ xấu lớn nhất danh mục (**1,330.8 tỷ VND**), đòi hỏi quy trình thẩm định dòng tiền chặt chẽ hơn thay vì chỉ dựa vào quy mô thu nhập danh nghĩa.

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

The relative contribution of each feature is quantified using standardized absolute coefficient values scaled by feature standard deviations, ensuring rigorous comparability across different numerical scales:

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


### 🟢 1. Rescue Layer: FP → TN (*Lớp Gỡ – Giải oan khách hàng tốt*)

* **Target Population:** `prediction_test_non_default.csv` (All **5,092 applications** that did **not** default in reality).
* **Pre-Adjustment Baseline:**
  * **TN (Correct Approvals):** **3,704 cases**
  * **FP (False Alarms / Wrongly Rejected):** **1,388 cases**
* **Adjustment Condition:**
  $$\mathbf{0.1987 \le LTI \le 0.342}$$
* **Cases Rescued (Lấy được):** **1,157 cases** successfully converted from **FP → TN** (eligible creditworthy borrowers unlocked for loan revenue).
* **Cases Remaining (Còn lại ngoài dải):** **231 cases** remain as FP (conservative risk buffers retained).
* **Post-Adjustment Result:**
  * **TN increased:** $3,704 \rightarrow \mathbf{4,861 \text{ cases}}$
  * **FP reduced:** $1,388 \rightarrow \mathbf{231 \text{ cases}}$ *(83.36% false alarms eliminated)*


### 🔴 2. Catch Layer: FN → TP (*Lớp Vớt – Bắt nợ xấu tiềm ẩn*)

* **Target Population:** `prediction_test_has_default.csv` (All **1,422 applications** that actually defaulted).
* **Pre-Adjustment Baseline:**
  * **TP (Defaults Flagged):** **865 cases**
  * **FN (Missed Defaults / Leakage):** **557 cases**
* **Adjustment Condition:**
  $$\mathbf{0.0653 \le LTI \le 0.1907}$$
* **Cases Caught (Lấy được):** **449 cases** successfully converted from **FN → TP** (preventing severe capital write-offs).
* **Cases Remaining (Còn lại ngoài dải):** **108 cases** remain as FN (monitored for manual credit committee review).
* **Post-Adjustment Result:**
  * **TP increased:** $865 \rightarrow \mathbf{1,314 \text{ cases}}$
  * **FN reduced:** $557 \rightarrow \mathbf{108 \text{ cases}}$ *(80.61% missed defaults recovered)*

---

## 8. Decision Support System

### Mức độ rà soát hồ sơ theo xác suất rủi ro

| Mức | Xác suất | Quy trình rà soát |
| :---: | :---: | :--- |
| 🟢 **1** | < 20% | Rà soát tiêu chuẩn: xác minh KYC, kiểm tra thu nhập, DTI, LTI, mục đích vay, lịch sử vỡ nợ, trùng lặp hồ sơ. |
| 🟡 **2** | 20–35% | Rà soát tăng cường (gồm toàn bộ Mức 1): phân tích chi tiết khả năng trả nợ, yêu cầu chứng từ bổ sung (sao kê, hợp đồng lao động), đối chiếu chéo thông tin, gọi xác minh khi cần. |
| 🔴 **3** | ≥ 35% | Thẩm định chuyên sâu: xác minh nguồn thu nhập, kiểm tra DTI/LTI đặc biệt cao, đối chiếu Tờ khai ↔ Chứng từ ↔ Sao kê ↔ CIC. ⚠️ *Mức 3 không đồng nghĩa tự động từ chối.* |

### Hồ sơ rủi ro cao cần kiểm tra gì?

| # | Khía cạnh | Chỉ số trọng yếu | Hướng dẫn |
| :---: | :--- | :--- | :--- |
| 01 | **Chất lượng dữ liệu** | Thiếu · Bất thường · Lỗi thời | Xác minh dữ liệu đầu vào trước khi dựa vào kết quả mô hình. |
| 02 | **Năng lực trả nợ** | Thu nhập · DTI · LTI | Đánh giá gánh nặng tài chính; không kết luận từ một biến đơn lẻ. |
| 03 | **Cấu trúc khoản vay** | Số tiền vay · Lãi suất · Kỳ hạn | Rà soát quy mô và chi phí khoản vay so với năng lực tài chính. |
| 04 | **Lịch sử tín dụng** | Từng vỡ nợ · Thâm niên tín dụng | Đối chiếu hành vi tín dụng trước đây trước khi kết luận mức độ rủi ro. |
| 05 | **Xác minh & Thẩm quyền** | Chứng từ · Xác minh bên thứ ba | Xác minh hồ sơ rủi ro cao hoặc thiếu dữ liệu; chuyển cấp xem xét khi cần, tuân thủ nghiêm bảo mật dữ liệu. |

### Phân khúc có tỷ lệ nợ xấu cao cần ưu tiên rà soát

> *Dùng để định hướng rà soát chuyên sâu — không phải ngưỡng tự động từ chối.*

| Phân khúc rủi ro | Tỷ lệ nợ xấu quan sát |
| :--- | :---: |
| Tỷ lệ tổng nợ / thu nhập (DTI) ≥ 0,70 | ≈ **79,0%** |
| Tỷ lệ khoản vay / thu nhập (LTI) ≥ 0,40 | ≈ **74,5%** |
| Lãi suất khoản vay ≥ 16% | ≈ **63,2%** |
| Thu nhập < 782 triệu đồng/năm | ≈ **47,1%** |
| Lịch sử từng vỡ nợ | ≈ **37,8%** *(vs. ~18,4% nhóm không vỡ nợ)* |

> **Nguyên tắc chung:** Đánh giá đa chiều (năng lực tài chính + cấu trúc khoản vay + hành vi tín dụng + chất lượng hồ sơ); không dùng xác suất mô hình để tự động từ chối; tuân thủ pháp luật và bảo mật dữ liệu cá nhân trong mọi hoạt động xác minh.
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
