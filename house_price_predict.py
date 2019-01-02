import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import ai_utils

DATA_FILE = './data_ai/house_data.csv'

FEAT_COLS = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement']


def main():
    house_data = pd.read_csv(DATA_FILE, usecols=FEAT_COLS + ['price'])
    ai_utils.plot_feat_and_price(house_data)

    X = house_data[FEAT_COLS].values
    y = house_data['price'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=10)
    linear_reg_model = LinearRegression()
    linear_reg_model.fit(X_train, y_train)
    r2_score = linear_reg_model.score(X_test, y_test)
    print("model's R2 value", r2_score)

    i = 50
    single_test_feat = X_test[i, :]
    y_true = y_test[i]
    y_pred = linear_reg_model.predict([single_test_feat])
    print('sample feature:', single_test_feat)
    print('true price:{},predict price:{}'.format(y_pred, y_pred))


if __name__ == '__main__':
    main()
