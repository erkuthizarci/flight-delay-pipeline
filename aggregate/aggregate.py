import pandas as pd

def aggregate():
    input_path = "../data/filtered_flights_Q1_2015.csv"
    output_path = "../data/aggregated_flights_Q1_2015.csv"

    print("📥 Loading preprocessed data...")
    df = pd.read_csv(input_path)

    print("📊 Aggregating daily flight stats...")
    grouped = df.groupby("FL_DATE").agg({
        "FL_DATE": "count",
        "ARRIVAL_DELAY": "mean"
    }).rename(columns={
        "FL_DATE": "flight_count",
        "ARRIVAL_DELAY": "avg_arrival_delay"
    }).reset_index()

    print("✅ Aggregation complete.")
    grouped.to_csv(output_path, index=False)
    print(f"💾 Saved aggregated data to: {output_path}")

if __name__ == "__main__":
    aggregate()
