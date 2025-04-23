import config.logger

from libs.data.fetcher import FetcherFactory

if __name__ == '__main__':
    fetcher = FetcherFactory.get_fetcher("tushare")
    df = fetcher.get_daily("600000.SH", "2021-01-01", "2021-01-31")
    print(df)
