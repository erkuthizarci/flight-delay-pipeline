from pyspark.sql import SparkSession
from pyspark.sql.functions import count, avg, col

def aggregate():
    spark = SparkSession.builder \
        .appName("FlightAggregation") \
        .getOrCreate()

    input_path = "../data/filtered_flights_Q1_2015_spark.csv"
    output_path = "../data/aggregated_flights_Q1_2015_spark.csv"

    print("📥 Loading filtered data with Spark...")
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    print("📊 Grouping and aggregating...")
    grouped = df.groupBy("FL_DATE").agg(
        count("*").alias("flight_count"),
        avg("ARRIVAL_DELAY").alias("avg_arrival_delay")
    )

    print("💾 Saving results...")
    grouped.write.csv(output_path, header=True, mode="overwrite")

    spark.stop()

if __name__ == "__main__":
    aggregate()
