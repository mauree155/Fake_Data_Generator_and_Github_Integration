# transform
import re

def transform_data(batch):
    """
    Standardizes phone numbers to 11-digit numeric format.
    """
    for record in batch:
        phone = re.sub(r'\D', '', record['Phone Number'])
        if len(phone) == 10:
            phone = '1' + phone
        elif len(phone) > 11:
            phone = phone[-11:]
        record['Phone Number'] = phone
    return batch
