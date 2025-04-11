def preprocess_input(data):
    # Example feature engineering logic
    features = []
    features.append(data.get('transaction_amount', 0))
    features.append(data.get('account_age_days', 0))
    features.append(data.get('num_previous_transactions', 0))
    features.append(1 if data.get('device_type') == 'mobile' else 0)
    return [features]
