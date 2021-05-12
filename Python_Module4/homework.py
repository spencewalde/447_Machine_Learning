import numpy as np
import pandas as pd
dataset = pd.read_csv('HW_TestingMetrics.csv', header = None , skiprows=1, keep_default_na=False)
print(dataset)
target = dataset.iloc[:1,2:].values.astype(str)
output = dataset.iloc[1:2,2:].values.astype(str)
print(target)
print(output)
