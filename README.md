# Forecasting Financial Inclusion in Ethiopia

Selam Analytics has developed Ethiopia’s first integrated financial inclusion forecasting system. This project supports a consortium of development finance institutions, mobile money operators, and the National Bank of Ethiopia by providing evidence‑based forecasts of **Access** (account ownership) and **Usage** (digital payment adoption) for 2025–2027.

The system combines enriched datasets, event impact modeling, forecasting methodologies, and an interactive dashboard to answer the consortium’s key questions:
- What drives financial inclusion in Ethiopia?
- How do events affect inclusion outcomes?
- What are projected rates for 2025–2027?

---

## Project Structure
```bash
├── data/
│   ├── raw/                         # Original datasets
│   ├── processed/                   # Enriched unified dataset
│   └── enrichment_log.md            # Documentation of added records
├── notebooks/
│   ├── task_2_exploratory_analysis.ipynb
│   ├── task_3_event_impact_modeling.ipynb
│   ├── task_4_forecasting.ipynb
│   └── interim_report.ipynb
├── dashboard/
│   └── app.py                        # Streamlit dashboard application
├── reports/
│   ├── interim_report.md
│   └── final_report.md
├── requirements.txt
└── README.md
```
---


---

## Methodology Overview

1. **Data Enrichment**  
   Unified schema integrating observations, events, impact links, and targets. Added records for female account ownership, infrastructure indicators (mobile penetration, 4G coverage, ATM density), and policy milestones (NFIS‑II update).

2. **Exploratory Analysis**  
   Visualized account ownership trajectory, gender gaps, mobile money adoption, digital payment usage, and infrastructure trends. Event timeline analysis contextualized changes.

3. **Event Impact Modeling**  
   Built an Event‑Indicator Association Matrix linking events to indicators. Validated Telebirr’s impact against observed Findex data; benchmarked Safaricom and M‑Pesa impacts using comparable country evidence.

4. **Forecasting (2025–2027)**  
   Applied trend regression augmented with event effects. Produced baseline, optimistic, base, and pessimistic scenarios with confidence intervals. Forecasted account ownership reaching 47–52% and digital payment usage 9–15% by 2027.

5. **Dashboard Development**  
   Created a Streamlit dashboard with four interactive sections:
   - **Overview:** Key metrics summary cards and growth highlights.
   - **Trends:** Interactive time series plots with date range selector.
   - **Forecasts:** Baseline vs event‑augmented forecasts with confidence intervals.
   - **Projections:** Scenario selector showing progress toward Ethiopia’s 60% inclusion target.

---

## Running the Dashboard

### Prerequisites
- Python 3.9+
- Virtual environment recommended

### Installation
```bash
pip install -r requirements.txt
```

### Launch
```bash
streamlit run dashboard/app.py
Open the local URL (usually http://localhost:8501) in your browser.
```

### Key Insights
1. Account ownership growth has slowed since 2017, highlighting structural barriers.

2. Telebirr’s launch produced measurable gains in mobile money adoption.

3. NFIS‑II interoperability mandate is expected to accelerate digital payment usage.

4. Safaricom and M‑Pesa will expand competition and adoption, but impacts are lagged.

5. Ethiopia is projected to reach 50% account ownership by 2027 under the base scenario, with digital payment usage between 9–15%.

6. Limitations and Future Work
Sparse Findex data (five points over thirteen years) limits precision.

7. Reliance on external benchmarks for Safaricom and M‑Pesa impacts.

8. Gender and rural/urban disaggregation incomplete.

8. Future work will expand data sources, enhance models with econometrics and machine learning, and incorporate ongoing monitoring and validation.

