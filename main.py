# main
import os
from extract import generate_sample_data
from transform import transform_data
from process import process_data
from load import load_data

def main():
    NUM_RECORDS = 200
    BATCH_SIZE = 50
    DELAY_SECONDS = 2

    # Save CSV to Desktop
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    OUTPUT_FILE = os.path.join(desktop, "fake_data.csv")

    print("Extracting data...")
    data = generate_sample_data(NUM_RECORDS, locale='en_UK')

    print("Processing data in batches...")
    for batch in process_data(data, BATCH_SIZE, DELAY_SECONDS):
        transformed = transform_data(batch)
        load_data(transformed, OUTPUT_FILE)

    print("ETL process completed successfully!")
    print(f" CSV saved at: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
