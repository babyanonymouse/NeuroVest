# app/analytics/engine.py

def analyze_spending(user_id, period):
    """
    Stub: return dummy spending breakdown and totals.
    Replace with real logic later.
    """
    return {
        'user_id': user_id,
        'period': period,
        'total_spent': 0.0,
        'by_category': {}
    }

def forecast_health(user_id, horizon):
    """
    Stub: return dummy forecast.
    Replace with real forecasting logic later.
    """
    return {
        'user_id': user_id,
        'horizon': horizon,
        'projected_score': 0.0,
        'details': {}
    }
