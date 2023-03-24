from coingecko import get_historical_data, several_historical_data
import seaborn as sn
import matplotlib.pyplot as plt

token_list = ["bitcoin", "ethereum", "fantom", "link", "litecoin"]

if __name__ == "__main__":
    historical_df = several_historical_data(token_list=token_list, days="365")
    correlation = historical_df.corr()
    print(correlation)

    sn.heatmap(correlation, annot=True)
    plt.show()