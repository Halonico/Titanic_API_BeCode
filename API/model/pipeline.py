# -*- coding: utf-8 -*-
from sklearn.pipeline import Pipeline
import preprocessing as pp
from sklearn.ensemble import RandomForestClassifier
columns_to_drop = ['Name', 'Parch', 'SibSp', 'Ticket', 'Cabin']
dic_title = {'Mr':1, 'Mrs':4,'Miss':8, 'Master':3, 'Mme':3, 'Mlle':8, 'Capt':2, 'Col':3, 'Dr':3, 'Countess':4,'Dona':3, 'Don':3, 'Jonkheer':3, 'Lady':8, 'Major':4, 'Ms':4, 'Rev':1, 'Sir':5}
dic_embarked = {'S':1, 'Q':4, 'C':7}
list_pclass = {1:6, 2:4, 3:1}
prediction_pipeline = Pipeline([
    ('ExtractTitle',pp.ExtractTitle()),
    ('FillAgeByTitle',pp.FillAgeByTitle()),
    ('CalculateFamilySize',pp.CalculateFamilySize()),
    ('DropUselessColumns',pp.DropUselessColumns(columns_to_drop)),
    ('ReplaceTitleWithNumber',pp.ReplaceTitleWithNumber(dic_title)),
    ('ReplaceSexByNumber',pp.ReplaceSexByNumber()),
    ('ConvertFare',pp.ConvertFare()),
    ('FillMissingAge',pp.FillMissingAge()),
    ('FillEmbarked',pp.FillEmbarked()),
    ('ReplaceEmbarkedByNumber',pp.ReplaceEmbarkedByNumber(dic_embarked)),
    ('ReplacePclassByNumber',pp.ReplacePclassByNumber(list_pclass)),
    ('ModelPrediction',RandomForestClassifier(random_state=18))
])