import pandas as pd
import numpy as np

def calc_wap(df, level:int = None):

    if not level:
        raise ValueError('need a level (1 or 2) argument')

    return (df[f'bid_price{level}'] * df[f'ask_size{level}'] + df[f'ask_price{level}'] * df[f'bid_size{level}']) / (df[f'bid_size{level}'] + df[f'ask_size{level}'])


def calc_log_return(list_stock_prices):
    return np.log(list_stock_prices).diff()


def calc_realized_volatility(series_log_return):
    return np.sqrt(np.sum(series_log_return**2))


def add_wap(df, level=None):
    df[f'wap{level}'] = calc_wap(df, level)
    return df


def add_log_return(df, level=None):
    df[f'log_return{level}'] = calc_log_return(df[f'wap{level}']) 
    return df


def add_realized_volatility(df, level=None):
    df[f'realized_volatility{level}'] = calc_realized_volatility(df[f'log_return{level}'])
    return df
