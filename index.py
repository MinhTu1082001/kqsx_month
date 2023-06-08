import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

xsmb = pd.read_csv("nam1.csv")

# xsmb['odd'] = xsmb['KQ'].apply(lambda x: 0 if x%2==0 else 1)
# xsmb.head()

# xsmb_odd_even = xsmb.groupby('odd').count().reset_index()
# xsmb_odd_even

xsmb['last2digit'] = xsmb['KQ'].apply(lambda x: int(str(x)[-2:]))
# print(xsmb)

plt.figure(figsize=(15,8))
sns.displot(xsmb['last2digit'], bins=100, height=5, aspect=3, color='green')
plt.tight_layout()
# plt.show()
xsmb=xsmb['last2digit'].value_counts()
n_smallest_values = xsmb.nsmallest(3)
print(n_smallest_values)

# sns.displot(xsmb['last2digit'], bins=10, height=5, aspect=3)
# plt.tight_layout()