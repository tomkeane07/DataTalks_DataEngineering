DATA_URL_0=https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet
DATA_URL_1=https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
DATA_DIR=data
INIT_DIR=db_init

.PHONY: all download_data up clean

all: download_data up

download_data:
	mkdir -p $(DATA_DIR)
	wget -nc -P $(DATA_DIR) $(DATA_URL_0)
	wget -nc -P $(DATA_DIR) $(DATA_URL_1)
	chmod 666 $(DATA_DIR)/green_tripdata_2025-11.parquet
	chmod 666 $(DATA_DIR)/taxi_zone_lookup.csv
# 	gunzip -f $(DATA_DIR)/green_tripdata_2019-10.csv.gz

up:
	docker-compose down -v && docker-compose up --build

clean:
	docker-compose down -v
	rm -rf $(DATA_DIR) $(INIT_DIR)