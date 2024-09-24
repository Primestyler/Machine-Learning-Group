import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

def histplot(x):
    sns.histplot(x=x)
    plt.show()
    
def corrplot(df):
    plt.figure(figsize=(20, 20))
    sns.heatmap(df.corr(), annot=True)
    plt.show()
    
def sta_sca(sc, df, cols):
    for i in cols:
        df[i] = sc.fit_transform(df[[i]])