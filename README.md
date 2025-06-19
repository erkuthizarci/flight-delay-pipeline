# ✈️ Flight Delay Data Pipeline (Batch Processing)

This project implements a **modular, Dockerized batch-processing pipeline** for quarterly machine learning retraining using flight delay data from Kaggle.

## 📦 Architecture Overview

Kaggle → Ingestion → Preprocessing → Aggregation → Output
| | |
Docker PySpark PostgreSQL / CSV


All services are run as Docker containers and orchestrated using `docker-compose`.

## 📁 Microservices

| Service       | Purpose                                        |
|---------------|------------------------------------------------|
| `ingest`      | Downloads flight dataset from Kaggle           |
| `preprocess`  | Filters Q1 2015 flights, adds `FL_DATE`        |
| `aggregate`   | Calculates daily flight count & avg delay      |
| `spark_runner`| Executes Spark-based PySpark scripts           |
| `db`          | PostgreSQL database with pre-created tables    |

## ⚙️ Technologies Used

- Python 3.10
- PySpark (Spark 3+)
- Docker & Docker Compose
- PostgreSQL 15
- Kaggle API

## 🚀 How to Run the Project

1. Make sure Docker Desktop is installed and running.
2. Add your Kaggle API token to your system (`~/.kaggle/kaggle.json`).
3. Clone the repository and navigate to the folder.

```bash
git clone https://github.com/erkuthizarci/flight-delay-pipeline.git
cd flight-delay-pipeline

4. Build all containers:
docker-compose build

5. Start services in the background:
docker-compose up -d

6. Run Spark jobs manually (from within the container):
docker-compose run spark_runner bash
spark-submit preprocess_spark.py
spark-submit aggregate_spark.py


📊 Output
Results will be saved in the data/ folder:

filtered_flights_Q1_2015_spark.csv/

aggregated_flights_Q1_2015_spark.csv/


🔐 Notes
The .env file is excluded via .gitignore

Data volume is shared across all services via ./data

PostgreSQL container includes raw_data and aggregated_data tables (optional)

✍️ Author
Built for the IU Data Engineering course – Portfolio Assignment








