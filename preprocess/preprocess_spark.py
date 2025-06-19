from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, concat_ws

def preprocess():
    spark = SparkSession.builder \
        .appName("FlightPreprocessing") \
        .getOrCreate()

    input_path = "../data/flights.csv"
    output_path = "../data/filtered_flights_Q1_2015_spark.csv"

    print("📥 Reading CSV with Spark...")
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    print("🧠 Creating FL_DATE and filtering for Q1 2015...")
    df = df.withColumn("FL_DATE", to_date(concat_ws("-", col("YEAR"), col("MONTH"), col("DAY"))))

    df_q1 = df.filter((col("FL_DATE") >= "2015-01-01") & (col("FL_DATE") < "2015-04-01"))

    print(f"✅ Filtered rows: {df_q1.count()}")

    print("💾 Writing filtered data...")
    df_q1.write.csv(output_path, header=True, mode="overwrite")

    spark.stop()

if __name__ == "__main__":
    preprocess()
