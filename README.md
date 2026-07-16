<<<<<<< HEAD
# 📦 **Ecommerce Data Pipeline — End‑to‑End Cloud Data Engineering Project**

`https://img.shields.io/badge/Python-3.10-blue?logo=python`
`https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql`
`https://img.shields.io/badge/AWS-S3-orange?logo=amazonaws`
`https://img.shields.io/badge/AWS-Glue-purple?logo=amazonaws`
`https://img.shields.io/badge/ETL-Pipeline-green`
`https://img.shields.io/badge/PowerBI-Dashboard-yellow?logo=powerbi`

A fully functional **cloud-based data engineering pipeline** built using:

- **Python ETL**
- **Pandas data cleaning**
- **AWS S3 storage**
- **PostgreSQL (local + RDS-ready)**
- **AWS Glue + Athena (coming next)**
- **Power BI analytics dashboard**

This project demonstrates real-world data engineering skills across ingestion, transformation, cloud storage, SQL modeling, and BI visualization.

---

## 🏗️ **Architecture Overview**

### **High-Level Pipeline**

```
                Kaggle CSV
                     │
                     ▼
          Python Extract Script
                     │
                     ▼
               Raw Data Folder
                     │
                     ▼
          Pandas Data Cleaning
                     │
                     ▼
           Processed CSV File
                     │
        Upload to AWS S3 Bucket
                     │
                     ▼
      Load into PostgreSQL (Local/RDS)
                     │
                     ▼
           SQL Business Queries
                     │
                     ▼
            Power BI Dashboard
```

---

## ☁️ **Cloud Architecture (AWS)**

```
                Local ETL
                   │
                   ▼
             AWS S3 Bucket
                   │
                   ▼
         AWS Glue Crawler (Next Step)
                   │
                   ▼
             AWS Glue Catalog
                   │
                   ▼
              AWS Athena SQL
                   │
                   ▼
           BI / Analytics Layer
```

---

## 📁 **Project Structure**

```
ecommerce-data-pipeline/
│
├── data/
│   ├── raw/               # Raw CSV from Kaggle
│   └── processed/         # Cleaned CSV from ETL
│
├── scripts/
│   ├── extract.py         # Load raw CSV
│   ├── transform.py       # Clean + enrich data
│   ├── upload_s3.py       # Push processed data to S3
│   ├── load_postgres.py   # Load into PostgreSQL
│   └── config.py          # Credentials & settings
│
├── sql/
│   ├── schema.sql         # Table definitions
│   ├── views.sql          # Reusable SQL views
│   └── business_queries.sql
│
├── dashboard/
│   └── EcommerceDashboard.pbix
│
├── screenshots/
│   └── dashboard.png
│
├── requirements.txt
└── README.md
```

---

## 🔧 **Technologies Used**

### **Programming**
- Python (Pandas, SQLAlchemy, psycopg2, boto3)

### **Cloud**
- AWS S3  
- AWS Glue (coming next)  
- AWS Athena (coming next)  
- Amazon RDS (optional upgrade)

### **Database**
- PostgreSQL

### **Visualization**
- Power BI

---

## 🧹 **Data Cleaning Steps**

- Remove duplicates  
- Handle missing values  
- Convert date formats  
- Remove negative prices  
- Add derived fields:
  - `sales = quantity × price`
  - `year`, `month`, `weekday`
  - `profit` (optional)

---

## 🗄️ **SQL Analytics**

### Top Selling Products
```sql
SELECT product, SUM(sales)
FROM sales
GROUP BY product
ORDER BY SUM(sales) DESC;
```

### Monthly Revenue
```sql
SELECT month, SUM(sales)
FROM sales
GROUP BY month;
```

### Payment Method Distribution
```sql
SELECT payment_method, COUNT(*)
FROM sales
GROUP BY payment_method;
```

---

## 📊 **Power BI Dashboard**

### **Executive Dashboard**
- Total Revenue  
- Orders  
- Customers  
- Average Order Value  
- Monthly Revenue Trend  
- Revenue by Category  
- Top Products  
- Sales by State  

### **Customer Dashboard**
- Top Customers  
- Repeat Customers  
- Customer Lifetime Value  

### **Product Dashboard**
- Best Sellers  
- Category Performance  

---

## 🚀 **Next Steps (Planned Enhancements)**

### **Phase 1 — AWS Glue + Athena**
- Create Glue crawler  
- Build Glue Data Catalog  
- Query S3 data using Athena  
- Replace PostgreSQL with serverless SQL  

### **Phase 2 — Automation**
- Airflow (optional)  
- AWS Lambda triggers  

### **Phase 3 — Containerization**
- Dockerize ETL  
- Deploy on ECS  

---

## 🧑‍💻 **How to Run Locally**

### 1️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 2️⃣ Run ETL
```
python scripts/extract.py
python scripts/transform.py
```

### 3️⃣ Upload to S3
```
python scripts/upload_s3.py
```

### 4️⃣ Load into PostgreSQL
```
python scripts/load_postgres.py
```

---


=======
# 📦 **Ecommerce Data Pipeline — End‑to‑End Cloud Data Engineering Project**

`https://img.shields.io/badge/Python-3.10-blue?logo=python`
`https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql`
`https://img.shields.io/badge/AWS-S3-orange?logo=amazonaws`
`https://img.shields.io/badge/AWS-Glue-purple?logo=amazonaws`
`https://img.shields.io/badge/ETL-Pipeline-green`
`https://img.shields.io/badge/PowerBI-Dashboard-yellow?logo=powerbi`

A fully functional **cloud-based data engineering pipeline** built using:

- **Python ETL**
- **Pandas data cleaning**
- **AWS S3 storage**
- **PostgreSQL (local + RDS-ready)**
- **AWS Glue + Athena (coming next)**
- **Power BI analytics dashboard**

This project demonstrates real-world data engineering skills across ingestion, transformation, cloud storage, SQL modeling, and BI visualization.

---

## 🏗️ **Architecture Overview**

### **High-Level Pipeline**

```
                Kaggle CSV
                     │
                     ▼
          Python Extract Script
                     │
                     ▼
               Raw Data Folder
                     │
                     ▼
          Pandas Data Cleaning
                     │
                     ▼
           Processed CSV File
                     │
        Upload to AWS S3 Bucket
                     │
                     ▼
      Load into PostgreSQL (Local/RDS)
                     │
                     ▼
           SQL Business Queries
                     │
                     ▼
            Power BI Dashboard
```

---

## ☁️ **Cloud Architecture (AWS)**

```
                Local ETL
                   │
                   ▼
             AWS S3 Bucket
                   │
                   ▼
         AWS Glue Crawler (Next Step)
                   │
                   ▼
             AWS Glue Catalog
                   │
                   ▼
              AWS Athena SQL
                   │
                   ▼
           BI / Analytics Layer
```

---

## 📁 **Project Structure**

```
ecommerce-data-pipeline/
│
├── data/
│   ├── raw/               # Raw CSV from Kaggle
│   └── processed/         # Cleaned CSV from ETL
│
├── scripts/
│   ├── extract.py         # Load raw CSV
│   ├── transform.py       # Clean + enrich data
│   ├── upload_s3.py       # Push processed data to S3
│   ├── load_postgres.py   # Load into PostgreSQL
│   └── config.py          # Credentials & settings
│
├── sql/
│   ├── schema.sql         # Table definitions
│   ├── views.sql          # Reusable SQL views
│   └── business_queries.sql
│
├── dashboard/
│   └── EcommerceDashboard.pbix
│
├── screenshots/
│   └── dashboard.png
│
├── requirements.txt
└── README.md
```

---

## 🔧 **Technologies Used**

### **Programming**
- Python (Pandas, SQLAlchemy, psycopg2, boto3)

### **Cloud**
- AWS S3  
- AWS Glue (coming next)  
- AWS Athena (coming next)  
- Amazon RDS (optional upgrade)

### **Database**
- PostgreSQL

### **Visualization**
- Power BI

---

## 🧹 **Data Cleaning Steps**

- Remove duplicates  
- Handle missing values  
- Convert date formats  
- Remove negative prices  
- Add derived fields:
  - `sales = quantity × price`
  - `year`, `month`, `weekday`
  - `profit` (optional)

---

## 🗄️ **SQL Analytics**

### Top Selling Products
```sql
SELECT product, SUM(sales)
FROM sales
GROUP BY product
ORDER BY SUM(sales) DESC;
```

### Monthly Revenue
```sql
SELECT month, SUM(sales)
FROM sales
GROUP BY month;
```

### Payment Method Distribution
```sql
SELECT payment_method, COUNT(*)
FROM sales
GROUP BY payment_method;
```

---

## 📊 **Power BI Dashboard**

### **Executive Dashboard**
- Total Revenue  
- Orders  
- Customers  
- Average Order Value  
- Monthly Revenue Trend  
- Revenue by Category  
- Top Products  
- Sales by State  

### **Customer Dashboard**
- Top Customers  
- Repeat Customers  
- Customer Lifetime Value  

### **Product Dashboard**
- Best Sellers  
- Category Performance  

---

## 🚀 **Next Steps (Planned Enhancements)**

### **Phase 1 — AWS Glue + Athena**
- Create Glue crawler  
- Build Glue Data Catalog  
- Query S3 data using Athena  
- Replace PostgreSQL with serverless SQL  

### **Phase 2 — Automation**
- Airflow (optional)  
- AWS Lambda triggers  

### **Phase 3 — Containerization**
- Dockerize ETL  
- Deploy on ECS  

---

## 🧑‍💻 **How to Run Locally**

### 1️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 2️⃣ Run ETL
```
python scripts/extract.py
python scripts/transform.py
```

### 3️⃣ Upload to S3
```
python scripts/upload_s3.py
```

### 4️⃣ Load into PostgreSQL
```
python scripts/load_postgres.py
```

---


>>>>>>> 1582d2dd236ed417d5c40eecb5e9ca3bc9919277
