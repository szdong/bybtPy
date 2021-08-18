import requests


class BybtPy:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def _get_request(self, url: str):
        headers = {
            'bybtSecret': self.api_key
        }
        response = requests.request("GET", url, headers=headers, data={})
        return response.json()

    def get_futures_open_interest(self, interval: int, symbol: str):
        """

        :param interval: 0: ALL, 1H: 2, 4H: 1, 12H: 4
        :param symbol: ex: BTC, ETH
        :return: dict()
        """
        url = f"https://open-api.bybt.com/api/pro/v1/futures/openInterest?interval={interval}&symbol={symbol}"
        return self._get_request(url=url)

    def get_futures_open_interest_chart(self, interval: int, symbol: str):
        """

        :param interval: 0: ALL, 1H: 2, 4H: 1, 12H: 4
        :param symbol: ex: BTC, ETH
        :return: dict()
        """
        url = f"https://open-api.bybt.com/api/pro/v1/futures/openInterest/chart?interval={interval}&symbol={symbol}"
        return self._get_request(url=url)

    def get_futures_liquidation(self, exName: str = None, symbol: str = None):
        """

        :param exName: Exchange Name, ex: Binance
        :param symbol: ex: BTC, ETH
        :return: dict()
        """
        url = f"https://open-api.bybt.com/api/pro/v1/futures/liquidation_chart"
        if exName is not None:
            url += f"?exName={exName}"
        if symbol is not None:
            url += f"&symbol={symbol}"
        return self._get_request(url=url)

    def get_futures_liquidation_chart(self, timeType: str, symbol: str = None):
        """

        :param timeType: 9: 1m, 3: 5m, 10: 15m, 11: 30m, 1: 4H, 4: 12H, 18: 90D
        :param symbol: ex: BTC, ETH
        :return: dict()
        """
        url = f"https://open-api.bybt.com/api/pro/v1/futures/liquidation/detail/chart"
        url += f"?timeType={timeType}&symbol={symbol}"
        return self._get_request(url=url)

    def get_futures_long_short_chart(self, interval: int, symbol: str):
        """

        :param interval: 2: 1H, 1: 4H, 4: 12H, 5: 24H
        :param symbol: ex: BTC, ETH
        :return: dict()
        """
        url = f"https://open-api.bybt.com/api/pro/v1/futures/longShort_chart?interval={interval}&symbol={symbol}"
        return self._get_request(url=url)

    def get_futures_funding_rates_chart(self, symbol: str, request_type: str = None):
        """

        :param symbol: C: Token Margined, U: USDT or USD Margined, default: C
        :param request_type: ex: BTC, ETH
        :return: dict()
        """
        url = f"https://open-api.bybt.com/api/pro/v1/futures/funding_rates_chart?symbol={symbol}"
        if request_type is not None:
            url += f"&type={request_type}"
        return self._get_request(url=url)

    def get_futures_funding_rates_newest(self, symbol: str = None):
        """

        :param symbol: ex: BTC, ETH
        :return:  dict()
        """
        url = "https://open-api.bybt.com/api/pro/v1/futures/funding_rates"
        if symbol is not None:
            url += f"?symbol={symbol}"
        return self._get_request(url=url)

    def get_futures_exchange_vol(self, symbol: str):
        """

        :param symbol: ex: BTC, ETH
        :return: dict()
        """
        url = f"https://open-api.bybt.com/api/pro/v1/futures/vol/chart?symbol={symbol}"
        return self._get_request(url=url)

    def get_options_open_interest(self, symbol: str = None):
        """

        :param symbol: ex: BTC, ETH
        :return: dict()
        """
        url = f"https://open-api.bybt.com/api/pro/v1/option/openInterest"
        if symbol is not None:
            url += f"?symbol={symbol}"
        return self._get_request(url=url)

    def get_options_open_interest_chart(self, interval: int, symbol: str):
        """

        :param interval: 0: ALL, 2: 1H, 1: 4H, 4: 12H, 5: 24H
        :param symbol: ex: BTC, ETH
        :return: dict()
        """
        url = f"https://open-api.bybt.com/api/pro/v1/option/openInterest/history/chart" \
              f"?interval={interval}&symbol={symbol}"
        return self._get_request(url=url)

    def get_options_exchanges_vol(self, symbol: str):
        """

        :param symbol: ex: BTC, ETH
        :return: dict()
        """
        url = f"https://open-api.bybt.com/api/pro/v1/option/vol/history/chart?symbol={symbol}"
        return self._get_request(url=url)
