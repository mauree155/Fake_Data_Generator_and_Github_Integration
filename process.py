# process
import time

def process_data(data, batch_size=50, delay_seconds=2):
    """
    Yields data in batches with a delay between batches.
    """
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]
        print(f"Waiting {delay_seconds} seconds before next batch...")
        time.sleep(delay_seconds)
