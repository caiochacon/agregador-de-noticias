import sys
import pytest
import pandas as pd

sys.path.append('..')

from utils.top_news_catcher import TopNewsCatcher

@pytest.fixture

def sample_data():

    path_to_csv = "tests/data/sample_data_test.csv"
    #pd.DataFrame(data).to_csv(path_to_csv, index=False)
    return path_to_csv

def test_catch_top_news(sample_data):
    catcher = TopNewsCatcher()
    dataset_top_news, df_to_recommendations = catcher.catch_top_news(sample_data)
    
    assert len(dataset_top_news) == 9  # All news should be captured
    assert len(df_to_recommendations) == 0  # No news should remain for recommendations

def test_get_news(sample_data):
    catcher = TopNewsCatcher()
    dataset_top_news, _ = catcher.catch_top_news(sample_data)
    
    assert len(dataset_top_news) == 9  # All news should be captured
    assert set(dataset_top_news['source'].unique()) == {'Source A', 'Source B', 'Source C'}  # Should contain all sources
    
    # Asserting order of news within each source
    for source in ['Source A', 'Source B', 'Source C']:
        source_news_dates = pd.to_datetime(dataset_top_news[dataset_top_news['source'] == source]['publication_date'])
        assert (source_news_dates == source_news_dates.sort_values(ascending=False)).all()  # News should be ordered by publication date