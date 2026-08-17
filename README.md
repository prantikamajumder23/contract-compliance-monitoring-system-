# Contract Compliance Monitoring System

An AI-powered contract compliance monitoring system that extracts, analyzes, and validates contractual clauses against predefined compliance rules.

The project is being developed in stages, starting with a rule-based contract compliance system and later integrating RAG and a vector database for intelligent document retrieval and explanations.

## 🎯 Project Goal

The goal of this project is to build a system that can:

- Extract text from contract PDFs
- Identify important contractual clauses
- Detect missing or incomplete clauses
- Extract important values such as dates, payment periods, and notice periods
- Compare contract terms against predefined compliance rules
- Detect potential inconsistencies and conflicts
- Generate a compliance report
- Later use RAG and a vector database to retrieve relevant contract sections and explain compliance decisions

## 🏗️ Planned Architecture

PDF Contract
↓
PDF Validation
↓
Text Extraction
↓
Text Preprocessing
↓
Clause Identification
↓
Information Extraction
↓
Compliance Rule Engine
↓
Compliance Report
↓
RAG + Vector Database
↓
Intelligent Compliance Explanation

## 📌 Current Progress

### Phase 1 — PDF Ingestion
- [x] PDF validation
- [x] PDF page detection
- [x] Page-by-page text extraction
- [x] Extracted text storage

### Phase 2 — Text Processing
- [ ] Text preprocessing
- [ ] Remove extraction artifacts
- [ ] Normalize whitespace
- [ ] Preserve clause structure

### Phase 3 — Contract Analysis
- [ ] Clause identification
- [ ] Key information extraction
- [ ] Missing clause detection
- [ ] Inconsistency detection

### Phase 4 — Compliance Engine
- [ ] Define compliance rules
- [ ] Compare contract terms against rules
- [ ] Generate compliance status
- [ ] Generate compliance report

### Phase 5 — RAG & Vector Database
- [ ] Document chunking
- [ ] Generate embeddings
- [ ] Set up vector database
- [ ] Implement semantic search
- [ ] Build RAG pipeline
- [ ] Generate evidence-based explanations

## 🛠️ Technologies

Currently:
- Python
- PyPDF
- Regular Expressions

Planned:
- Pandas
- Embeddings
- Vector Database
- RAG
- LangChain
- LLM
- Streamlit

## 📂 Project Structure

```text
contract-compliance-monitoring-system/
│
├── data/
│   ├── contracts/
│   └── processed/
│
├── src/
│
├── tests/
│
├── import.py
├── README.md
└── .gitignore