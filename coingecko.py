import pandas as pd
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


def get_price_token(token_name, pair):
    """get price of a token or Coin at the moment"""
    if not isinstance(token_name, dict):

        return cg.get_price(ids=token_name, vs_currencies=pair)
    else:
        raise Exception("An Error was occur don't use Dict for token_list")


def get_historical_data(id: str, days: str, interval: str, vs_currency: str):
    """
    id='bitcoin'
    days= '150'
    interval= 'daily'
    vs_currency= 'usd'
    """

    try:
        token_hist = cg.get_coin_market_chart_by_id(id=id, vs_currency=vs_currency, days=days, interval=interval)["prices"]
        historical_list = list(map(lambda index: index[1], token_hist))
        return historical_list
    except Exception as e:
        print(e)


def several_historical_data(token_list: list, days: str):
    """
    token_list -> ["bitcoin", "ethereum", "fantom", "link", "litecoin"]:param
    """
    historical_dict = dict()

    for token in token_list:
        hist = get_historical_data(id=token, days=days, interval="daily", vs_currency="usd")
        historical_dict[token] = hist
    hist_df = pd.DataFrame(historical_dict)
    return hist_df
