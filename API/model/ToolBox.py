# -*- coding: utf-8 -*-
# ToolBox
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import numpy as np
def numberOfNaNFeature(dataframe):
   numberNaNPerCategory = dataframe.isna().sum()
   numberNaNPerCategoryPerc = (dataframe.isna().sum() / len(dataframe))*100
   numberNaNPerCategoryPerc = pd.DataFrame(numberNaNPerCategoryPerc).sort_values(by=0,ascending=False)
   return numberNaNPerCategoryPerc
def print_score(clf,X_train,X_test,y_train,y_test,train = False):
    if train:
        print("Train Result : \n")
        print("Accuracy Score : {0:.4f}\n".format(accuracy_score(y_train,clf.predict(X_train))))
        print("Classification Report : \n {} \n".format(classification_report(y_train,clf.predict(X_train))))
        print("Confusion Matrix : \n {} \n".format(confusion_matrix(y_train,clf.predict(X_train))))
        res = cross_val_score(clf, X_train, y_train, cv=10, scoring = 'accuracy')
        print("Average Accuracy: \t {0:.4f}".format(np.mean(res)))
        print("Accuracy SD : \t\t {0:.4f}".format(np.std(res)))
    elif not train:
        '''
        test perf
        '''
        print('Test Result:\n')
        print("Accuracy score : {0:.4f}\n".format(accuracy_score(y_test,clf.predict(X_test))))
        print("Classification Report : \n {} \n".format(classification_report(y_test,clf.predict(X_test))))
        print("Confusion Matrix : \n {} \n".format(confusion_matrix(y_test,clf.predict(X_test))))
def rstr(df, pred=None):
    obs = df.shape[0]
    types = df.dtypes
    counts = df.apply(lambda x: x.count())
    uniques = df.apply(lambda x: [x.unique()])
    nulls = df.apply(lambda x: x.isnull().sum())
    distincts = df.apply(lambda x: x.unique().shape[0])
    missing_ration = (df.isnull().sum()/ obs) * 100
    skewness = np.abs(df.skew())
    kurtosis = np.abs(df.kurt())
    print('Data shape:', df.shape)
   
    if pred is None:
        cols = ['types', 'counts', 'distincts', 'nulls', 'missing ration', 'uniques', 'skewness', 'kurtosis']
        str = pd.concat([types, counts, distincts, nulls, missing_ration, uniques, skewness, kurtosis], axis = 1)
 
    else:
        corr = np.abs(df.corr()[pred])
        str = pd.concat([types, counts, distincts, nulls, missing_ration, uniques, skewness, kurtosis, corr], axis = 1, sort=False)
        corr_col = 'corr '  + pred
        cols = ['types', 'counts', 'distincts', 'nulls', 'missing_ration', 'uniques', 'skewness', 'kurtosis', corr_col ]
   
    str.columns = cols
    dtypes = str.types.value_counts()
    print('___________________________\nData types: \n',str.types.value_counts())
    print('___________________________')
    return str
# Add in the rest of the parameters
def return_weights(vocab, original_vocab, vector, vector_index, top_n):
    zipped = dict(zip(vector[vector_index].indices, vector[vector_index].data))
    
    # Let's transform that zipped dict into a series
    zipped_series = pd.Series({vocab[i]:zipped[i] for i in vector[vector_index].indices})
    
    # Let's sort the series to pull out the top n weighted words
    zipped_index = zipped_series.sort_values(ascending=False)[:top_n].index
    return [original_vocab[i] for i in zipped_index]
def words_to_filter(vocab, original_vocab, vector, top_n):
    filter_list = []
    for i in range(0, vector.shape[0]):
    
        # Here we'll call the function from the previous exercise, and extend the list we're creating
        filtered = return_weights(vocab, original_vocab, vector, i, top_n)
        filter_list.extend(filtered)
    # Return the list in a set, so we don't get duplicate word indices
    return set(filter_list) 

