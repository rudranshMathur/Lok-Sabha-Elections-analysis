import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

#data
data = pd.read_csv('sample_data/INDIA_NDA_encoded.csv')

#correlation
correlation = data[['Ratio', 'Winning Party']].corr()
print("Correlation:\n", correlation)


#Chi-square test
contingency_table = pd.crosstab(data['Ratio'], data['Winning Party'])
chi2, p, dof, expected = chi2_contingency(contingency_table)

print(f"Chi-square test: p-value = {p}")
