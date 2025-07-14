import pandas as pd
from faker import Faker
import random

fake = Faker()
Faker.seed(42)
random.seed(42)

n_rows = 100000  # Simulate large volume

data = []
for _ in range(n_rows):
    transaction_id = fake.uuid4()
    customer_id = random.randint(1000, 5000)
    transaction_time = fake.date_time_this_year()
    amount = round(random.uniform(1, 10000), 2)
    merchant = fake.company()
    category = random.choice(['groceries', 'electronics', 'travel', 'entertainment', 'utilities'])
    is_fraud = random.choices([0, 1], weights=[0.995, 0.005])[0]  # 0.5% fraud

    data.append([transaction_id, customer_id, transaction_time, amount, merchant, category, is_fraud])

df = pd.DataFrame(data, columns=[
    'transaction_id', 'customer_id', 'transaction_time',
    'amount', 'merchant', 'category', 'is_fraud'
])

df.to_csv('../data/raw_transactions.csv', index=False)
