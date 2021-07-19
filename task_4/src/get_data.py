import yfinance as yf
import datetime as dt
import os
from argparse import ArgumentParser


def get_hour_data(tick_name, date):
    date = dt.datetime.strptime(date, "%Y-%m-%d-%H")
    ticker = yf.Ticker(tick_name)
    date = date - dt.timedelta(hours=1)
    hist_df = ticker.history(period="1h", interval='1m', end=date)
    hour = str(date.hour)
    print(hour)
    str_date = date.strftime("%Y-%m-%d")
    path = os.path.abspath('/opt/airflow/data/original/' + tick_name + '/' + str_date)
    if not os.path.exists(path):
        os.makedirs(path)
        print("Directory ", path, " Created ")
    hist_df.to_csv(path + '/' + hour + '.csv')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--tick_name', type=str, default='AAPL')
    parser.add_argument('--date', type=str, default=dt.datetime.now().strftime("%Y-%m-%d-%H"))
    args = parser.parse_args()

    get_hour_data(**vars(args))
