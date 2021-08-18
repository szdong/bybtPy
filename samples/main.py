from bybtPy.bybt import BybtPy


def main():
    bybt_api_key = "YOUR_API_KEY"
    bybt = BybtPy(api_key=bybt_api_key)

    print(bybt.get_options_open_interest(symbol="BTC"))
    print(bybt.get_options_open_interest_chart(interval=5, symbol="BTC"))
    print(bybt.get_futures_liquidation(exName="Binance", symbol="BTC"))


if __name__ == '__main__':
    main()
