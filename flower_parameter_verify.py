import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="sklearn")

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
    model_dict = {'kNN': (KNeighborsClassifier(),
                          {'n_neighbors': [5, 15, 25],
                           'p': [1, 2]}),
                  'Logistic Regression': (LogisticRegression(),
                                          {'C': [1e-2, 1, 1e2]}),
                  'SVM': (SVC(),
                          {'C': [1e-2, 1, 1e2]})
                  }

    for model_name, (model, model_params) in model_dict.items():
        clf = GridSearchCV(estimator=model, param_grid=model_params, cv=5)
        clf.fit(X_train, y_train)
        best_model = clf.best_estimator_

        acc = best_model.score(X_test, y_test)

        print('{} model predict accuracy:{:.2f}%'.format(model_name,acc*100))
        print('{} model most suitable params:{}'.format(model_name,clf.best_params_))

if __name__ == '__main__':
    main()
