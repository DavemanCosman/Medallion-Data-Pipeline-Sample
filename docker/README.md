# Docker

## Prerequisites (Windows)
- Virtualization enabled in BIOS
- WSL2 installed and set as default
- Docker Desktop installed and running

Also make sure you create a directory called `../docker/airflow/logs` for this project.

## Initial Setup (run once)
These commands only need to be executed the **first time** you set up the environment.
1. `docker compose run airflow-webserver airflow db init`
2. ```docker compose run airflow-webserver airflow users create \
    --username <your-username> \
    --password <your-password> \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com``` (change these creds for your own implementation)
3. `docker compose up -d`
4. `docker ps` (check for status)

## Daily Usage (start the environment)
1. `docker compose up -d` (wait a couple seconds to let containers start)
2. Visit Airflow at http://localhost:8080
3. Visit MinIO at http://localhost:9001
4. `docker compose down` (when you're done)

If you see warnings about orphan containers, then instead of step 4, run this:
	`docker compose down --remove-orphans`

## Default login details

*REMEMBER*: these are just default credentials. They are NEVER to be used in live environments that are deployed. It is HIGHLY recommended you change them for your own implementation.

### Airflow
local url: http://localhost:8080
user: airflow
password: airflow

### minIO
local url: http://localhost:9001
user: minioadmin
password: minioadmin