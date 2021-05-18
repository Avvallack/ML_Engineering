import pandas as pd
import numpy as np


def bring_to_float(x):
    if type(x) == float:
        return x
    return float(x.replace(',', '.'))

def replace_nan(x):
    if x == -200:
        return np.nan
    return x


if __name__ == '__main__':
    df = pd.read_csv('AirQualityUCI.csv', sep=';',
                     infer_datetime_format=True, usecols=['CO(GT)', 'PT08.S1(CO)', 'NMHC(GT)',
                                                          'C6H6(GT)', 'PT08.S2(NMHC)', 'NOx(GT)', 'PT08.S3(NOx)',
                                                          'NO2(GT)', 'PT08.S4(NO2)', 'PT08.S5(O3)', 'T', 'RH', 'AH'])

    for col in ['CO(GT)', 'C6H6(GT)', 'T', 'RH', 'AH']:
        df[col] = df[col].apply(bring_to_float)
    
    df.dropna(inplace=True)

    df.to_csv('prepared_data.csv', index=False)

