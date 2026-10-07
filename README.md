# Contract Compliance Monitoring System — V1

A Python-based **contract compliance monitoring system** that extracts clauses from PDF contracts, standardizes them, checks them against predefined compliance rules, and calculates a risk score.

## 🔍 Workflow

```text
Contract PDF
     ↓
Text Extraction
     ↓
Cleaning & Preprocessing
     ↓
Clause Extraction
     ↓
Clause Standardization
     ↓
Compliance Checking
     ↓
Risk Scoring
```

## ✨ Features

* Extracts text from contract PDFs
* Cleans and preprocesses contract text
* Identifies important contractual clauses
* Standardizes clauses into predefined categories
* Performs rule-based compliance checking
* Classifies clauses as `PASS`, `REVIEW`, or `FAIL`
* Calculates an overall contract risk score

### Supported Clauses

* Payment Terms
* Termination
* Confidentiality
* Intellectual Property
* Liability
* Force Majeure
* Governing Law
* Dispute Resolution
* Scope of Work
* Renewal

### Risk Scoring

| Status | Weight |
| ------ | -----: |
| PASS   |      0 |
| REVIEW |      5 |
| FAIL   |     15 |

## 🛠️ Tech Stack

* Python
* Pandas
* Regular Expressions
* PDF Text Extraction
* JSON
* Git & GitHub

## 📂 Project Structure

```text
contract-compliance/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── cleaned/
│
├── extract.py
├── clean.py
├── clause_extraction.py
├── standardize.py
├── compliance.py
├── risk_score.py
│
├── requirements.txt
└── README.md
```

## ▶️ Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Place the contract PDF inside:

```text
data/raw/
```

Run the pipeline:

```bash
python extract.py
python clean.py
python clause_extraction.py
python standardize.py
python compliance.py
python risk_score.py
```

## 📊 Example Output

```text
Payment Terms       → PASS
Confidentiality     → FAIL
Liability           → REVIEW
Termination         → PASS

Risk Score: 20
```

## 🚀 Future Development

**V2:** RAG, embeddings, vector database, and semantic search.

**V3:** AI-powered compliance explanations, contract comparison, dashboard, and cloud deployment.

## 📌 Status

**Version:** V1
**Status:** ✅ Completed

This project is built for educational and portfolio purposes.





