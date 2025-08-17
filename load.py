# load
import csv
import os

def load_data(batch, filename):
    """
    Saves batch data to a CSV file. Creates file if not exists.
    """
    fieldnames = ['Full Name', 'Phone Number', 'Email Address', 'Job Title', 'City']
    mode = 'a' if os.path.exists(filename) else 'w'
    
    with open(filename, mode, newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if mode == 'w':
            writer.writeheader()
        for record in batch:
            writer.writerow(record)
    
    print(f" Saved {len(batch)} records to {filename}")
