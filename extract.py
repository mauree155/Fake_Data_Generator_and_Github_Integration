# extract
from faker import Faker

def generate_sample_data(num_records=100, locale='en_UK'):
    """
    Generates fake personal data records.
    """
    fake = Faker(locale)
    data = []
    for _ in range(num_records):
        record = {
            'Full Name': fake.name(),
            'Phone Number': fake.phone_number(),
            'Email Address': fake.email(),
            'Job Title': fake.job(),
            'City': fake.city()
        }
        data.append(record)
    return data

if __name__ == "__main__":
    sample = generate_sample_data(5)
    print(sample)
