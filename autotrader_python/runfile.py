# runfile.py
from autotrader import AutoTrader

at = AutoTrader()
at.configure(show_plot=True, verbosity=1, feed='yahoo',
             mode='continuous', update_interval='1h') 
at.add_strategy('macd') 
at.backtest(start = '1/1/2021', end = '1/1/2022')
at.virtual_account_config(leverage=30)
at.run()