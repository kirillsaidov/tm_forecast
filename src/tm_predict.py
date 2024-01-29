# module tm_predict

# system
import sys
from datetime import datetime
from datetime import timedelta

# data processing and plotting
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import yfinance as yahooFinance

# ml/dl
from pmdarima import auto_arima, AutoARIMA
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'h', 'help']:
        print(f'USAGE: ./tm_predict.py [COMMAND]')
        print(f'COMMAND:')
        print(f'         run    train model and predict')
        print(f'    download    download or update tick data')
        print(f'        help    This help information.')
        exit()
    
    # validate command
    command = sys.argv[1]
    if command not in ['run', 'download']:
        print(f'Error: unrecognized command <{command}>!')
        
        
        
