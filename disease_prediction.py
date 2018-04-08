import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
def predict(lis):
	data = pd.read_csv('Data/data_pivoted.csv')
	data = data.fillna(0)
	cols = data.columns.tolist()
	cols.remove('disease')
	x = data[cols]
	y = data.disease
	mnb = MultinomialNB()
	mnb = mnb.fit(x, y)
	dict_ = {}
	i=0
	for dat in data.iloc[[0]]:
		dict_[dat]=i
		i += 1
	x1 = np.zeros(len(cols))
	for sym in lis:
		x1[dict_[sym]-1]=1
	x1=x1.reshape(1, -1)
	y1=mnb.predict(x1)
	pred=''.join(y1)
	return pred
lis=[]
print(predict(lis))