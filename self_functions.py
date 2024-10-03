import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

def histplot(x):
    sns.histplot(x=x)
    plt.show()
    
def corrplot(df, col, method='pearson'):
    corrs = df.corr(method=method)[col]
    
    # Create a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corrs.to_frame(), annot=True, cmap='coolwarm', cbar=True)
    plt.title(f'Correlation of {col} with other variables')
    plt.show()
    
def sta_sca(sc, df, cols):
    for i in cols:
        df[i] = sc.fit_transform(df[[i]])
        
def z_score(x):
    return (x - x.mean()) / x.std()