import os
import pandas as pd
import seaborn as sns
import datetime as dt

from matplotlib import pyplot as plt
from argparse import ArgumentParser



def plot_results(tick_name, date):
    date = dt.datetime.strptime(date, "%Y-%m-%d-%H")
    str_date = date.strftime("%Y-%m-%d")
    path = f'/opt/airflow/data/{tick_name}/moving_averages/{str_date}'
    filenames = os.listdir(path)
    sma5_files = [f for f in filenames if '5SMA_' in f]
    sma20_files = [f for f in filenames if '20SMA_' in f]

    sma5_df = pd.read_csv(path + '/' + sma5_files[0], parse_dates=True)
    for file in sma5_files[1:]:
        df_append = pd.read_csv(path + '/' + file, parse_dates=True)
        sma5_df = sma5_df.append(df_append, ignore_index=True)

    sma5_df['Datetime'] = pd.to_datetime(sma5_df['Datetime'])

    sma20_df = pd.read_csv(path + '/' + sma20_files[0])
    for file in sma20_files[1:]:
        df_append = pd.read_csv(path + '/' + file, parse_dates=True)
        sma20_df = sma20_df.append(df_append, ignore_index=True)

    sma20_df['Datetime'] = pd.to_datetime(sma20_df['Datetime'])

    df = sma5_df.join(sma20_df[['20SMA']])

    path = os.path.abspath('/opt/airflow/data/plots/' + tick_name + '/' + str_date)
    if not os.path.exists(path):
        os.makedirs(path)
        print("Directory ", path, " Created ")

    plt.figure(figsize=(30, 12))
    sns.lineplot(data=df, x='Datetime', y='Mean')
    sns.lineplot(data=df, x='Datetime', y='5SMA')
    sns.lineplot(data=df, x='Datetime', y='20SMA')
    plt.xticks(rotation=45, ha='right')

    plt.savefig(path + f'/moving_averages_{str_date}.png', dpi=300)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--tick_name', type=str, default='AAPL')
    parser.add_argument('--date', type=str, default=dt.datetime.now().strftime("%Y-%m-%d-%H"))
    args = parser.parse_args()

    plot_results(**vars(args))
