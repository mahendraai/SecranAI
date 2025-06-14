import datetime
import string
import math

def calculate_entropy(secret_value: str) -> float:
    """
    Shannon entropy: measures complexity (higher = more secure).
    """
    if not secret_value:
        return 0.0
    entropy = 0
    for x in set(secret_value):
        p_x = float(secret_value.count(x)) / len(secret_value)
        entropy -= p_x * math.log2(p_x)
    return entropy


def days_since(timestamp_str: str) -> int:
    try:
        timestamp = datetime.datetime.fromisoformat(timestamp_str)
        delta = datetime.datetime.utcnow() - timestamp
        return delta.days
    except Exception:
        return 9999  # default risk


def score_secret(secret: dict) -> dict:
    """
    Given a secret dictionary, compute risk score (0-100).
    """
    score = 0
    labels = []

    # 1. Rotation age
    age_days = days_since(secret.get('last_rotated') or secret.get('created_date', ''))
    if age_days > 180:
        score += 40
        labels.append("Stale (>180d)")
    elif age_days > 90:
        score += 20
        labels.append("Old (>90d)")

    # 2. Entropy (if available)
    secret_value = secret.get('value')  # optional
    if secret_value:
        entropy = calculate_entropy(secret_value)
        if entropy < 3.5:
            score += 30
            labels.append("Low Entropy")
        elif entropy < 4.0:
            score += 15
            labels.append("Medium Entropy")
    
    # 3. Missing rotation info
    if not secret.get('last_rotated'):
        score += 10
        labels.append("Missing Rotation Info")

    # 4. Placeholder check
    if secret.get("name", "").lower() in ["test", "demo", "example"]:
        score += 20
        labels.append("Default/Test Key")

    return {
        **secret,
        "risk_score": min(score, 100),
        "risk_labels": labels
    }
