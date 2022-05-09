#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:37:56 2022

@author: connorduncan
"""

import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('../data/bank.csv', sep=';')

train, test = train_test_split(data, test_size = .2, random_state=42)

train.to_csv('../data/bank_train.csv', index=False)
test.to_csv('../data/bank_test.csv', index=False)