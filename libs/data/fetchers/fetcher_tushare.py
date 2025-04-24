import logging
import os

from libs.data.base_fetcher import BaseFetcher
import pandas as pd
import tushare as ts
from tushare.stock import cons as ct

logger = logging.getLogger(__name__)


class TushareFetcher(BaseFetcher):

    def __init__(self):
        token = ts.get_token()
        user_home = os.path.expanduser('~')
        fp = os.path.join(user_home, ct.TOKEN_F_P)
        if token is None:
            error_msg = "请在 [Tushare] 官网申请 token 并在 {} 中添加".format(fp)
            logger.error(error_msg)
            raise Exception(error_msg)
        self.pro = ts.pro_api()

    def get_daily(self, symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        logger.info(f"[Tushare] 获取 {symbol} 从 {start_date} 到 {end_date} 的日线数据")
        df = pd.DataFrame()
        # df = self.pro.daily(trade_date='20200325')
        # 这里填 tushare 的实际调用逻辑
        return df

    def get_minutely(self, symbol: str, start_date: str, end_date: str, freq: str = '1min') -> pd.DataFrame:
        logger.info(f"[Tushare] 获取 {symbol} 从 {start_date} 到 {end_date} 的 {freq} 数据")
        # 这里填 tushare 的实际调用逻辑
        return pd.DataFrame()
