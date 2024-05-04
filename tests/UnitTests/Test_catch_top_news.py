import pytest
import pandas as pd
import sys
sys.path.append('..')
from src.top_news_catcher import TopNewsCatcher

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