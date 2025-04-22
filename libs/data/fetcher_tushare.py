import logging
import os

from .base_fetcher import BaseFetcher
import pandas as pd
import tushare as ts
from tushare.stock import cons as ct


class TushareFetcher(BaseFetcher):
    logger = logging.getLogger(__name__)
    if not logging.getLogger().handlers:
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def __init__(self):
        token = ts.get_token()
        user_home = os.path.expanduser('~')
        fp = os.path.join(user_home, ct.TOKEN_F_P)
        if token is None:
            error_msg = "请在 [Tushare] 官网申请 token 并在 {} 中添加".format(ct.TOKEN_F_P)
            self.logger.error(error_msg)


    def get_daily(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        self.logger.info(f"[Tushare] 获取 {symbol} 从 {start_date} 到 {end_date} 的日线数据")
        # 这里填 tushare 的实际调用逻辑
        return pd.DataFrame()

    def get_minutely(self, symbol: str, start_date: str, end_date: str, freq: str = '1min') -> pd.DataFrame:
        self.logger.info(f"[Tushare] 获取 {symbol} 从 {start_date} 到 {end_date} 的 {freq} 数据")
        # 这里填 tushare 的实际调用逻辑
        return pd.DataFrame()
