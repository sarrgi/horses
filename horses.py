import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import preprocessing


# https://www.kaggle.com/jankoch/scikit-learn-pipelines-and-pandas

def split_data(dataframe, ratio):
    """
    Randomly split a dataframe into 2 based on a specific ratio.
    """
    msk = np.random.rand(len(df)) < ratio
    train = df[msk]
    test = df[~msk]

    return train, test


def eval(predictions, targets):
    # acc = metrics.accuracy_score(targets, predictions)
    # print("Accurayc:", acc)
    #
    cf = metrics.confusion_matrix(test_targets, predictions)
    print(cf)

    for i in range(len(predictions)):
        if predictions[i] == 1:
            print(predictions[i], targets[i])




if __name__ == "__main__":

    # read in data
    df = pd.read_csv("pre_processed.csv")
    train, test = split_data(df, 0.8)

    # set targets
    train_targets = train.set_index("UniqueID")["Finishingposition"]
    train_set = train.set_index("UniqueID")
    test_set = test.set_index("UniqueID")
    test_targets = test.set_index("UniqueID")["Finishingposition"]

    # remove targets from fields
    train_set = train_set.drop("Finishingposition", axis = 1)
    test_set = test_set.drop("Finishingposition", axis = 1)


    c = 0
    for t in test_targets:
        if t == 1: c += 1

    print("C:", c)


    # run model
    # model = RandomForestClassifier()
    # model.fit(train_set, train_targets)
    # predictions = model.predict(test_set)
    #
    # # eval
    # eval(predictions, test_targets)
