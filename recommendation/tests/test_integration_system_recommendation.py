import sys
sys.path.append('..')

import numpy as np
import pytest
import pandas as pd
from src.run_recommendation_system import RunRecomendationSystem

@pytest.fixture
def sample_data():
    data = {
        'title': ['News 1', 'News 2', 'News 3', 'News 4', 'News 5', 'News 6', 'News 7', 'News 8', 'News 9'],
        'source': ['Source A', 'Source A', 'Source A', 'Source B', 'Source B', 'Source B', 'Source C', 'Source C', 'Source C'],
        'publication_date': ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-01', '2024-05-02', '2024-05-03',
                             '2024-05-01', '2024-05-02', '2024-05-03']
    }
    df = pd.DataFrame(data)
    return df

def test_run(sample_data):
    # Create an instance of RunRecomendationSystem
    recommender = RunRecomendationSystem()

    # Generate sample data for testing
    df_top_news, df_to_recommendations = sample_data, sample_data

    # Run the recommendation system
    dataset_topnews, dataset_recomendations = recommender.run(df_top_news, df_to_recommendations)

    # Check if the datasets have the correct shapes
    assert dataset_topnews.shape[0] == 9
    assert dataset_recomendations.shape[0] == 27

    # Check if the recommended news have the correct format
    assert all(isinstance(title, str) for title in dataset_recomendations['title'].values)

    # Check if the recommended news are different from each other
    assert (len(dataset_recomendations['title'].values)) == len(dataset_recomendations)
    
    assert all(isinstance(date, str) for date in dataset_recomendations['publication_date'].dt.strftime('%Y-%m-%d').values)