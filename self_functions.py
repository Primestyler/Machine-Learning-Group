import seaborn as sns
import missingno as msno
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

class DataVisualizer:
    @staticmethod
    def histplot(df):
        sns.histplot(df)
        plt.show()

    @staticmethod
    def corrplot(df, target_column, method='pearson'):
        corrs = df.corr(method=method)[target_column]
        sns.heatmap(corrs.to_frame(), annot=True)
        plt.show()

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def scale_features(self, df, columns):
        df[columns] = self.scaler.fit_transform(df[columns])
        return df[columns]
