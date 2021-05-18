import numpy as np
import pandas as pd
dataset = pd.read_csv('score.csv')
subject = input('please tell me the subject:')
x = input("please tell me your score:")
x = int(x)
score = 15 - x
print(dataset.at[score, subject])
print('the percentage of the subject is', +dataset.at[score, subject])

