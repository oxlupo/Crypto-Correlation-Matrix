from coingecko import get_historical_data
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

fantom = get_historical_data(id="fantom", days='365', interval="daily", vs_currency="usd")
bitcoin = get_historical_data(id="bitcoin", days='365', interval="daily", vs_currency="usd")


df = pd.DataFrame({"fantom": fantom,
                   "bitcoin": bitcoin,
                   })

correlation = df.corr()
print(correlation)

sn.heatmap(correlation, annot=True)
plt.show()