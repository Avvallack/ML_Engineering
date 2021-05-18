import json
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_percentage_error


TARGET_COL = 'PT08.S2(NMHC)'


if __name__ == '__main__':
    df = pd.read_csv('prepared_data.csv')
    scaler = StandardScaler()
    train, test = train_test_split(df, test_size=0.2)
    regressor = LinearRegression()
    train_x = train.drop(columns=TARGET_COL)
    train_y = train[TARGET_COL].values
    scaled_x = scaler.fit_transform(train_x)
    regressor.fit(scaled_x, train_y)

    test_x = test.drop(columns=TARGET_COL)
    test_y = test[TARGET_COL].values
    scaled_test = scaler.transform(test_x)
    prediction = regressor.predict(scaled_test)

    mse = mean_squared_error(test_y, prediction)
    mape = mean_absolute_percentage_error(test_y, prediction)
    r2 = r2_score(test_y, prediction)

    with open("metrics.json", 'w') as outfile:
        json.dump({"r2_score": r2, "MSE": mse, "MAPE": mape}, outfile)
