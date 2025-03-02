#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:13:27 2019

@author: jaisi8631
"""
# -------------------------
# IMPORT NECESSARY MODULES
# -------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle


# -------------------------------------
# LOAD PRE-BUILT CLASSIFIER AND SCALER
# -------------------------------------
with open('predictor.pkl', 'rb') as fid:
    classifier = pickle.load(fid)

scalerfile = 'scaler.save'
sc = pickle.load(open(scalerfile, 'rb'))


# -------------------------
# DATA PREPROCESSING
# -------------------------
# load required files and allocate data
data = pd.read_csv('data/stage1_dataset.csv', header=None)
X = data.iloc[:, 4:].values
case = X.xs('0', axis=1, level=0).dropna()
ctrl = X.xs('1', axis=1, level=0).dropna()
X = X(case.values.ravel(), ctrl.values.ravel(), equal_var=False)

# apply scalar to data
X = sc.transform(X)


# -------------------------
# GENERATING PREDICTIONS
# -------------------------
# predict probabilities of team 1 winning each matchup
predictions = classifier.predict_proba(X)
predictions = predictions[:, 1]


# -------------------------
# PREDICTIONS STORAGE
# -------------------------
# load in the sample submissions spreadsheet
template = pd.read_csv('SampleSubmissionStage1.csv')
spreadsheet = template.iloc[:, :].values

# add the prediction to each prediction index
for i in range(0, len(predictions)):
    spreadsheet[i][1] = round(predictions[i], 5)

# create dataframe to match sample submissions spreadsheet
results = pd.DataFrame(data=spreadsheet, columns=["ID", "Pred"])

# save new submissions spreadsheet as csv to disk
results.to_csv('SubmissionStage1.csv', sep=',', encoding='utf-8', index=False)

# output feedback
print()
print()
print("Stage 1 Predictions creation complete.")
print()
print()
