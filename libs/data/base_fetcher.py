from abc import ABC, abstractmethod
import pandas as pd


class BaseFetcher(ABC):
    @abstractmethod
    def get_daily(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        """获取日线数据"""
        pass

    @abstractmethod
    def get_minutely(self, symbol: str, start_date: str, end_date: str, freq: str = '1min') -> pd.DataFrame:
        """获取分钟线数据"""
        pass
