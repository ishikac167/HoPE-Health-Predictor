import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

data = pd.read_excel('PCOS_final_data - Copy.xlsx')
data = data.iloc[:,1:]

X = data.iloc[:,:19]

y = data.iloc[:,19:]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.naive_bayes import GaussianNB
NB_classifier = GaussianNB()
NB_classifier.fit(X_train, y_train)

pickle.dump(NB_classifier, open("PCOD_model.sav", "wb"))