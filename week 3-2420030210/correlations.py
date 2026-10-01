"""import pandas as pd
df=pd.DataFrame({
    'X': [10, 20, 30, 40, 50],
    'Y': [12, 24, 33, 45, 60]   })
corr_mattrix = df.corr(method='pearson')
print("Pearson Correlation Matrix:\n", corr_mattrix)"""

#three subjects marks
"""import pandas as pd
df = pd.DataFrame({
    'DS': [85, 78, 92, 70, 88],
    'TOC': [80, 75, 90, 65, 85],
    'CD': [88, 82, 95, 72, 90]
})
corr_matrix = df.corr(method='pearson')
print("Pearson Correlation Matrix:\n", corr_matrix)"""

#pearson correlation
"""import pandas as pd
df=pd.read_csv('Iris.csv')
corr_matrix = df.corr(method='pearson', numeric_only=True)
print("Pearson Correlation Matrix:\n", corr_matrix)"""

#spearmen correlation
"""import pandas as pd
from scipy.stats import spearmanr
df=pd.DataFrame({
    'X': [10, 20, 30, 40, 50],
    'Y': [12, 24, 33, 45, 60]   })
corr_value,p_value = spearmanr(df['X'], df['Y'])
print(f"Spearman Correlation Coefficient: {corr_value}")
print(f"P-value: {p_value}")"""

#for three subjects
"""import pandas as pd
from scipy.stats import spearmanr
df = pd.DataFrame({
    'Maths': [10, 20, 30, 40, 50],
    'Science': [12, 24, 33, 45, 60],
    'English': [15, 18, 35, 42, 55]
})
corr_matrix = df.corr(method='spearman')
print("Spearman Correlation Matrix:")
print(corr_matrix)"""

#for csv file
"""import pandas as pd
df = pd.read_csv('Iris.csv')
corr_matrix = df.corr(method='spearman', numeric_only=True)
print("Spearman Correlation Matrix:\n", corr_matrix)"""

