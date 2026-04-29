# Medallion-Data-Pipeline-Sample
Sample Data pipeline with medallion architecture, built entirely in open source

## About
An end-to-end, open source data medallion data pipeline implementinmg Bronze -> Silver -> Gold architecture.

### Software and Tools Used
- MinIO
- DuckDB
- dbt Core
- Apache Airflow
- Great Expectations
- Docker Compose

### Purpose
This is a demo project. It demonstrates:
- ingestion from public API
- ELT: raw -> transformed -> analytical modeled data layers
- SQL based transformations with dbt
- data quality checks
- orchestration with Airflow
- reproducible local development

## Project Structure
- dbt/      		# dbt models, tests, and documentation
- data/				# local data and MinIO buckets
- docker/      		# Docker Compose environment
- docker/airflow/	# DAGs and orchestration
- scripts/			# ingestion and utility scripts
- tests/      		# data quality and unit tests
- docs/      		# architecture diagrams and documentation