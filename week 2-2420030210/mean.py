#mean median mode
"""import pandas as pd
import numpy as np
df=pd.DataFrame({  'Age': [25,30,np.nan,40,35],'Department': ['HR', 'Finance', 'Finance', np.nan,'IT']})
print(df)
df['Age']=df['Age'].fillna(df['Age'].mean())
df['Department']=df['Department'].fillna(df['Department'].mode()[0])
print(df)"""

#forward fill
"""import pandas as pd
import numpy as np
df=pd.DataFrame({  'Age': [25,30,np.nan,40,35],'Department': ['HR', 'Finance', 'Finance', np.nan,'IT']})
print("Original Dataset (with Missing Values):")
print(df)
df_ffill = df.copy()
df_ffill.ffill(inplace=True)
print(df_ffill)"""

#backwardfill
"""import pandas as pd
import numpy as np
df=pd.DataFrame({  'Age': [25,30,np.nan,40,35],'Department': ['HR', 'Finance', 'Finance', np.nan,'IT']})
print("Original Dataset (with Missing Values):")
print(df)
df_bfill = df.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)"""

#drop rows contains missing values
"""import pandas as pd
import numpy as np
df=pd.DataFrame({  'Age': [25,30,np.nan,40,35],'Department': ['HR', 'Finance', 'Finance', np.nan,'IT']})
print("Original Dataset")
print(df)
df_drop_rows = df.dropna()
print("After dropping rows:\n",df_drop_rows)"""

#Drop rows and columns with axis
"""import pandas as pd
import numpy as np
df=pd.DataFrame({  'Age': [25,30,np.nan,40,35],'Department': ['HR', 'Finance', 'Finance', np.nan,'IT']})
print("Original Dataset")
print(df)
df_drop_cols = df.dropna(axis=1)
print("After dropping columns:\n",df_drop_cols)"""

#rows deleting with axis
"""import pandas as pd
import numpy as np
df=pd.DataFrame({  'Age': [25,30,np.nan,40,35],'Department': ['HR', 'Finance', 'Finance', np.nan,'IT']})
print("Original Dataset")
print(df)
df_drop_rows = df.dropna(axis=0)
print("After dropping columns:\n",df_drop_rows)"""

#removing duplicates
"""import pandas as pd
# Sample dataset with duplicates
df = pd.DataFrame({
    'ID': [1, 2, 2, 3, 4, 4],
    'Name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'David'],
    'Age': [25, 30, 30, 35, 40, 40]
})
print("Original Data:\n", df)
# Remove exact duplicates
df_exact = df.drop_duplicates()
print("\nAfter Exact Match Removal:\n", df_exact)"""



# Remove duplicates based on selected key columns (e.g., ID or Name).
# Remove duplicates based only on 'ID'
"""import pandas as pd
df = pd.DataFrame({
    'ID': [1, 2, 2, 3, 4, 4, 5],
    'Name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'David', 'David'],
    'Age': [25, 30, 30, 35, 40, 40, 40]
})
print("Original Data:\n", df)
df_subset_id = df.drop_duplicates(subset=['ID'])
print("\nAfter Subset-Based Removal (ID):\n", df_subset_id)
df_subset_name = df.drop_duplicates(subset=['Name'])
print("\nAfter Subset-Based Removal (Name):\n", df_subset_name)"""


# Correcting Inconsistent Formats
import pandas as pd
df = pd.DataFrame({
    'Date': ['2025-01-05', '05/01/2025', 'Jan 5, 2025', '2025.01.05']
})
print("Original Data:\n", df)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
print(df)

# Case Normalization (lowercase / uppercase)
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'BOB', 'charlie', 'DAVID']
})
df['Name_lower'] = df['Name'].str.lower()
df['Name_upper'] = df['Name'].str.upper()
print(df)

