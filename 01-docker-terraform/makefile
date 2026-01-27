include .env

DATA_URL_0=https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet
DATA_URL_1=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
DATA_DIR=data

.PHONY: all download_data up up-no-cache down clean load_db

all: download_data down up

download_data:
	mkdir -p $(DATA_DIR)
	wget -nc -P $(DATA_DIR) $(DATA_URL_0)
	wget -nc -P $(DATA_DIR) $(DATA_URL_1)
	chmod 666 $(DATA_DIR)/green_tripdata_2025-11.parquet
	chmod 666 $(DATA_DIR)/taxi_zone_lookup.csv

up-no-cache:
	POSTGRES_USER=$(POSTGRES_USER) POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) POSTGRES_DB=$(POSTGRES_DB) POSTGRES_HOST=$(POSTGRES_HOST) POSTGRES_PORT=$(POSTGRES_PORT) \
	PGADMIN_DEFAULT_EMAIL=$(PGADMIN_DEFAULT_EMAIL) PGADMIN_DEFAULT_PASSWORD=$(PGADMIN_DEFAULT_PASSWORD) PGADMIN_PORT=$(PGADMIN_PORT) \
	docker-compose build --no-cache && \
	docker-compose up -d

up:
	POSTGRES_USER=$(POSTGRES_USER) POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) POSTGRES_DB=$(POSTGRES_DB) POSTGRES_HOST=$(POSTGRES_HOST) POSTGRES_PORT=$(POSTGRES_PORT) \
	PGADMIN_DEFAULT_EMAIL=$(PGADMIN_DEFAULT_EMAIL) PGADMIN_DEFAULT_PASSWORD=$(PGADMIN_DEFAULT_PASSWORD) PGADMIN_PORT=$(PGADMIN_PORT) \
	docker-compose up -d

down:
	docker-compose down -v

clean:
	docker-compose down -v
	rm -rf $(DATA_DIR)

load_db:
	POSTGRES_USER=$(POSTGRES_USER) POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) POSTGRES_DB=$(POSTGRES_DB) POSTGRES_HOST=$(POSTGRES_HOST) POSTGRES_PORT=$(POSTGRES_PORT) \
	docker-compose exec python python data/db_init.py