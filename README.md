# Forecasting Financial Inclusion in Ethiopia

## 📌 Project Overview
This project explores and forecasts financial inclusion trends in Ethiopia using unified datasets that combine survey data, policy events, infrastructure indicators, and impact links.  
The goal is to understand **drivers of access and usage**, identify **data gaps**, and build toward **impact modeling** that can inform policy and market strategies.

---

## ⚙️ Setup Instructions
1. **Clone the repository:**
```bash
   git clone https://github.com/<your-username>/forecasting-financial-inclusion-ethiopia.git
   cd forecasting-financial-inclusion-ethiopia
```
2. **Create and activate a virtual environment:**
``` bash
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      #windows
```
3. **Install dependencies:**

```bash
    pip install -r requirements.txt
```
4. **Launch Jupyter Notebook:**

```bash
jupyter notebook
Select the kernel Python (venv).
```

## Repository Structure
```bash
├── data
│   ├── raw/                  # Original datasets (ethiopia_fi_unified_data.csv, reference_codes.csv)
│   ├── processed/            # Enriched datasets (ethiopia_fi_unified_data_enriched.csv)
├── notebooks/
│   ├── task_1_exploration.ipynb   # Data exploration & enrichment
│   ├── task_2_eda.ipynb           # Exploratory data analysis
├── src/                    # Source code modules (data loaders, utils)
├── data_enrichment_log.md  # Documentation of enrichment additions
├── requirements.txt        # Python dependencies
├── .gitignore              # Excludes venv, __pycache__, large files
└── README.md               # Project documentation
```
## Data Sources
World Bank Global Findex – Account ownership, mobile money, disaggregated indicators

GSMA – Digital payment adoption, infrastructure coverage

ITU – Mobile penetration statistics

World Bank Development Indicators – ATM density and financial infrastructure

National Bank of Ethiopia (NBE) – Policy milestones (NFIS-II update, interoperability mandate)

## Unified Schema
The unified dataset follows a consistent schema across record types:

Field	Description
record_type	Type of record: observation, event, impact_link, target
pillar	Dimension: access, usage, infrastructure, policy
indicator	Name of the indicator (e.g., Account Ownership, Mobile Money Adoption)
indicator_code	Short code for indicator (e.g., ACC_OWN_T, MM_ACC_T)
value_numeric	Numeric value of the indicator
observation_date	Year or date of observation/event
source_name	Source institution (World Bank, GSMA, ITU, NBE)
source_url	URL to source data
confidence	Confidence level: high, medium, low
original_text	Original phrasing from source
collected_by	Contributor name (e.g., Rediet)
collection_date	Date of collection
notes	Contextual notes explaining relevance
Impact Links connect events to indicators via parent_id, showing expected directional effects (positive/negative) with evidence basis.

## Completed Tasks
**Task 1: Data Exploration & Enrichment**

-Loaded raw datasets

-Documented schema understanding

-Explored records by type, pillar, confidence

-Added enriched records (observations, events, impact links)

-Logged enrichment in data_enrichment_log.md

**Task 2: Exploratory Data Analysis**

-Comprehensive EDA notebook with:

-Dataset overview & temporal coverage

-Access trajectory (2011–2024) & gender gap

-Usage trends (mobile money, digital payments)

-Infrastructure analysis (mobile penetration, 4G coverage, ATM density)

-Event timeline visualization

-Correlation analysis

-Key insights & data limitations