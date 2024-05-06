
import pandas as pd

class TopNewsCatcher:

    def catch_top_news(self, path_to_csv):

        self.df = pd.read_csv(path_to_csv, low_memory=False, encoding="UTF-8")
        self.df = self.df.dropna(subset=['title','publication_date'])
        self.df = self.df.drop_duplicates(subset=['title'])
        self.df = self.df[self.df['title'] != 'title']

        dataset_top_news = self._get_news(self.df)

        df_to_recomendations = self.df.drop(dataset_top_news.index.values)

        return dataset_top_news, df_to_recomendations

    def _get_news(self, df):

        results = []
        df_not_charges = df[(df['category'] != "quadrinhos") & (df['category'] != "charges")]
        groups = df_not_charges.groupby('source')

        for name_groups, group in groups:
            
            group_ordered = group.sort_values(by='publication_date', ascending=False)
            first_three = group_ordered.head(3)
            results.append(first_three)

        final_result = pd.concat(results)

        return final_result
    



