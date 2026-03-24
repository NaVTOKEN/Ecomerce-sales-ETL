# E-commerce ETL Pipeline 🚀

## 📌 Project Overview
This project simulates a real-world ETL pipeline for an e-commerce company.

## ⚙️ Tech Stack
- Python (Pandas)
- SQLite
- Apache Airflow
- SQL

## 🔄 ETL Pipeline
1. Extract data from CSV
2. Transform (clean + feature engineering)
3. Load into SQLite DB

## 📊 Business Insights
- Daily sales trends
- Top-selling products
- Regional performance
- Payment insights

## ⏰ Orchestration
Airflow DAG automates the ETL pipeline.

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone <your_repo_link>
cd ecommerce-etl-pipeline
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run ETL pipeline
```bash
python etl/main.py
```

### 4. Check output
- Database created in `db/ecommerce.db`
- Table: `sales`


## 📂 Output

After running the pipeline:

- SQLite DB: `db/ecommerce.db`
- Table: `sales`
- Ready for SQL analysis & dashboards
