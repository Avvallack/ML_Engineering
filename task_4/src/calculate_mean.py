import os
import pandas as pd
import numpy as np
import datetime as dt
from argparse import ArgumentParser


def calculate_mean(tick_name, date):
    date = dt.datetime.strptime(date, "%Y-%m-%d-%H")
    date = date - dt.timedelta(hours=1)
    hour = str(date.hour)
    str_date = date.strftime("%Y-%m-%d")
    df = pd.read_csv('/opt/airflow/data/original/' + tick_name + '/' + str_date + '/' + hour + '.csv', index_col=0)
    df['Mean'] = np.mean((df['High'].values, df['Low'].values), axis=0)
    path = os.path.abspath('/opt/airflow/data/' + tick_name + '/average/' + str_date)
    if not os.path.exists(path):
        os.makedirs(path)
        print("Directory ", path, " Created ")
    df.to_csv(path + '/' + hour + '.csv')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--tick_name', type=str, default='AAPL')
    parser.add_argument('--date', type=str, default=dt.datetime.now().strftime("%Y-%m-%d-%H"))
    args = parser.parse_args()

    calculate_mean(**vars(args))
