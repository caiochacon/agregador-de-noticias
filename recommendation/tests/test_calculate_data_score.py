import sys
sys.path.append('..')

from datetime import datetime, timedelta
import numpy as np
from utils.data_scorer_calculator import DataScorerCalculator

def test_calculate_data_score():
    # Create an instance of the class
    calculator = DataScorerCalculator()

    # Example dates
    today = datetime.today()
    dates = [today - timedelta(days=10), today - timedelta(days=5), today - timedelta(days=2)]

    # Calculate scores
    scores = calculator.calculate_data_score(dates)

    # Check if the results are correct
    assert len(scores) == len(dates)
    assert all(0 <= score <= 1 for score in scores)

    # Test a special case with a single date
    single_date = [today - timedelta(days=1)]
    single_score = calculator.calculate_data_score(single_date)
    assert single_score == [1.0]

    # Test a special case with identical dates
    identical_dates = [today - timedelta(days=5)] * 3
    identical_scores = calculator.calculate_data_score(identical_dates)
    assert all(score == identical_scores[0] for score in identical_scores)

    # Test a special case with a future date
    future_date = [today + timedelta(days=5)]
    future_score = calculator.calculate_data_score(future_date)
    assert future_score == [1.0]