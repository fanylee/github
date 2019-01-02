import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

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
    model_dict = {'kNN': KNeighborsClassifier(n_neighbors=7),
                  'Logistic Regression': LogisticRegression(C=1e5),
                  'SVM': SVC(C=1e5)}

    for model_name, model in model_dict.items():
        model.fit(X_train, y_train)
        acc = model.score(X_train, y_train)
        print('{}model predict accuracy:{:.2f}%'.format(model_name, acc * 100))


if __name__ == '__main__':
    main()
