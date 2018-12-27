import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

DATA_FILE = './data_ai/Iris.csv'

SPECIES_LABEL_DICT = {
    'Iris-setosa': 0,
    'Iris-versicolor': 1,
    'Iris-virginica': 2
}

FEAT_COLS = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']


def main():
    iris_data = pd.read_csv(DATA_FILE, index_col='Id')
    iris_data['Label'] = iris_data['Species'].map(SPECIES_LABEL_DICT)

    X = iris_data[FEAT_COLS].values
    y = iris_data['Label'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 / 3, random_state=10)

    knn_model = KNeighborsClassifier()
    knn_model.fit(X_train, y_train)

    accuracy = knn_model.score(X_test, y_test)
    print('预测准确率:{:.2f}%'.format(accuracy * 100))

    idx = 25
    test_sample_feat = [X_test[idx,:]]
    y_true = y_test[idx]
    y_pred = knn_model.predict(test_sample_feat)

    print('真实标签{},预测标签{}'.format(y_true, y_pred))


if __name__ == '__main__':
    main()
