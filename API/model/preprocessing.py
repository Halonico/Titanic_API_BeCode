# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
class ExtractTitle(BaseEstimator,TransformerMixin):
    def fit(self,X,y):
        return self
    def transform(self,X):
        X = X.copy()
        X['title'] = X['Name'].str.extract('(\w+)\.')
        print("Titre extrait")
        return X
class FillAgeByTitle(BaseEstimator,TransformerMixin):
    def fit(self,X,y):
        self.a = X.groupby('title').Age.mean()
        return self
    def transform(self,X):
        X = X.copy()
        for i in X[X.Age.isnull()].index:
            X.loc[i,'Age'] = self.a[X.loc[i].title]
        print("Age manquant remplis")
        return X
class CalculateFamilySize(BaseEstimator,TransformerMixin):
    def fit(self,X,y):
        return self
    def transform(self,X):
        X = X.copy()
        X['family'] = X['SibSp'] + X['Parch']
        X['family'] = X['family'].apply(lambda x: 4 if x >=1 else 1)
        print("Taille famille calculée")
        return X
class DropUselessColumns(BaseEstimator,TransformerMixin):
    def __init__(self,columnsToDrop):
        self.columnsToDrop = columnsToDrop
    def fit(self,X,y):
        return self
    def transform(self,X):
        X = X.copy()
        X = X.drop(columns=self.columnsToDrop)
        print("Retire colonne inutiles")        
        return X
class ReplaceTitleWithNumber(BaseEstimator,TransformerMixin):
    def __init__(self,dic_title):
        self.dic_title = dic_title
    def fit(self,X,y):
        return self
    def transform(self,X):
        X = X.copy()
        X["title"].replace(self.dic_title, inplace=True)
        X['title']=X['title'].astype('int')
        print("Remplace titre par nombre")
        return X
class ReplaceSexByNumber(BaseEstimator,TransformerMixin):
    def fit(self,X,y):
        return self
    def transform(self,X):
        X = X.copy()
        X['Sex'] = X['Sex'].apply(lambda x: 15 if x == 'female' else 1)
        print("Remplace Sexe par nombre")
        return X
class ConvertFare(BaseEstimator,TransformerMixin):
    def fit(self,X,y):
        return self
    def transform(self,X):
        X = X.copy()
        X['Fare'] = X['Fare'].apply(lambda x: 4 if x >= 52 else 1)
        print("Convert Fare")
        return X
class FillMissingAge(BaseEstimator,TransformerMixin):
    def fit(self,X,y):
        return self
    def transform(self,X):
        X = X.copy()
        X['Age'] = X['Age'].apply(lambda x: 5 if x <= 9 else (3 if x in range(22,56) else 1 ))
        print("Remplacer age par valeurs manquante")
        return X
class FillEmbarked(BaseEstimator,TransformerMixin):
    def fit(self,X,y):
        self.mode = X["Embarked"].mode()[0]
        return self
    def transform(self,X):
        X = X.copy()
        X['Embarked'] = X['Embarked'].fillna(self.mode)
        print("Remplacer valeurs manquantes Embarked")
        return X
class ReplaceEmbarkedByNumber(BaseEstimator,TransformerMixin):
    def __init__(self,dic_embarked):
        self.dic_embarked = dic_embarked
    def fit(self,X,y):
        return self
    def transform(self,X):
        X = X.copy()
        X["Embarked"].replace(self.dic_embarked, inplace=True)
        print("Embarked remplacé")
        return X
class ReplacePclassByNumber(BaseEstimator,TransformerMixin):
    def __init__(self,dict_pclass):
        self.dict_pclass = dict_pclass
    def fit(self,X,y):
        return self
    def transform(self,X):
        X = X.copy()
        X['Pclass'].replace(self.dict_pclass, inplace=True)
        print("Remplace valeurs Pclass")
        return X
