import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

def histplot(x):
    sns.histplot(x=x)
    plt.show()