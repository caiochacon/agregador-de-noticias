from datetime import datetime
import numpy as np

class DataScorerCalculator:

    def calculate_data_score(self, dates):
        today = datetime.today()
        self.date_scores = [(today - date).days for date in dates]
        self.min_score = np.min(self.date_scores)
        self.max_score = np.max(self.date_scores)

        return self._normalyze_data_score(self.date_scores)

    def _normalyze_data_score(self, date_scores):
        return [(score - self.min_score) / (self.max_score - self.min_score) for score in date_scores]
