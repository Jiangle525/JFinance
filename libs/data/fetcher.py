from libs.data.fetchers.fetcher_tushare import TushareFetcher
from .base_fetcher import BaseFetcher

class FetcherFactory:
    @staticmethod
    def get_fetcher(source: str) -> BaseFetcher:
        if source == "tushare":
            return TushareFetcher()
        else:
            raise ValueError(f"未知的数据源类型: {source}")


