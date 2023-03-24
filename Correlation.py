import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.DataFrame({"1": [1, 2, 3, 4],
                   "2": [2, 4, 5, 1],
                   })

correlation = df.corr()
print(correlation)

sn.heatmap(correlation, annot=True)
plt.show()