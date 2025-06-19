import pandas as pd
import os

def preprocess():
    input_path = "../data/flights.csv"  # adjust if file name is different
    output_path = "../data/filtered_flights_Q1_2015.csv"

    print("📥 Loading dataset...")
    df = pd.read_csv(input_path)

    print("🧹 Cleaning and filtering data...")
    # Create FL_DATE from YEAR, MONTH, DAY_OF_MONTH
    df["FL_DATE"] = pd.to_datetime(df[["YEAR", "MONTH", "DAY"]])

    # Filter for Q1 2015
    df_q1 = df[
        (df["FL_DATE"] >= "2015-01-01") &
        (df["FL_DATE"] < "2015-04-01")
    ]

    print(f"✅ Filtered data contains {len(df_q1):,} rows")

    df_q1.to_csv(output_path, index=False)
    print(f"💾 Saved filtered data to: {output_path}")

if __name__ == "__main__":
    preprocess()
