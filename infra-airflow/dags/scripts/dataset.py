import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import timedelta

fake = Faker()
Faker.seed(42)
np.random.seed(42)

def transaction_generate(fraud=False):
    user_id = fake.uuid4()
    account_id = fake.uuid4()
    transaction_id = fake.uuid4()
    timestamp = fake.date_time_between(start_date='-30d', end_date='now')
    amount = round(np.random.exponential(scale=200), 2)
    currency = random.choice(['BRL', 'USD', 'EUR'])
    transaction_type = random.choice(['compra', 'saque', 'transferência', 'depósito'])
    merchant_id = fake.uuid4() if transaction_type == 'compra' else None
    location = fake.city()
    device_id = fake.uuid4()
    channel = random.choice(['app', 'web', 'ATM', 'POS'])
    is_international = random.choice([True, False])
    is_high_risk_country = is_international and random.random() < 0.3
    previous_balance = round(np.random.uniform(1000, 10000), 2)
    new_balance = previous_balance - amount if transaction_type in ['compra', 'saque', 'transferência'] else previous_balance + amount
    flagged_fraud = fraud

    if fraud:
        amount *= random.uniform(5, 20)
        location = random.choice(['Pyongyang', 'Teerã', 'Caracas'])
        channel = random.choice(['web', 'app'])
        device_id = fake.uuid4()
        timestamp = timestamp.replace(hour=random.choice([2, 3, 4]))
    
    return {
        'transaction_id': transaction_id,
        'timestamp': timestamp,
        'user_id': user_id,
        'account_id': account_id,
        'amount': round(amount, 2),
        'currency': currency,
        'transaction_type': transaction_type,
        'merchant_id': merchant_id,
        'location': location,
        'device_id': device_id,
        'channel': channel,
        'is_international': is_international,
        'is_high_risk_country': is_high_risk_country,
        'previous_balance': previous_balance,
        'new_balance': round(new_balance, 2),
        'flagged_fraud': flagged_fraud,
    }

def generate_fake_transactions(num_transacoes=10000, fraude_ratio=0.02, output_path=r'.\dados\raw\transactions3.parquet'):
    transactions = []
    for _ in range(num_transacoes):
        is_fraud = random.random() < fraude_ratio
        transactions.append(transaction_generate(fraud=is_fraud))
    
    df = pd.DataFrame(transactions)
    df.to_parquet(output_path, index=False)
    print(f"Arquivo salvo em: {output_path}")

generate_fake_transactions()
