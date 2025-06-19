CREATE TABLE IF NOT EXISTS raw_data (
    flight_date DATE,
    airline VARCHAR(10),
    origin_airport VARCHAR(10),
    destination_airport VARCHAR(10),
    arrival_delay NUMERIC
);

CREATE TABLE IF NOT EXISTS aggregated_data (
    flight_date DATE PRIMARY KEY,
    flight_count INTEGER,
    avg_arrival_delay NUMERIC
);
