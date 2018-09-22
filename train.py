# python 3 

# OP 
import pandas as pd, numpy as np

# ML 
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split, KFold, cross_val_score


# -----------------------------
# train 



def main():
	# load data 
	df_train = pd.read_csv('data/train.csv')
	df_test = pd.read_csv('data/test.csv')
	# data preprocess
	X = df_train[['acousticness',
				'danceability',
				'energy',
				'instrumentalness',
				'key', 
				'liveness',
				'loudness', 
				'mode',
				'speechiness', 
				'tempo', 
				'valence']]
	y = df_train['ratings']
	# train-test split 
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
	# ML 
	# model 1) : RF 
	# config 
	skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
	# need to tune super-parameter later 
	RF_params = {'max_depth': range(1,11),'min_samples_split' : range(5,20)}
	# model train 
	RF = RandomForestClassifier()
	RF_grid = GridSearchCV(RF,RF_params ,cv=skf, n_jobs=-1, verbose=True)
	RF_grid.fit(X_train, y_train)
	RF_grid.best_estimator_, RF_grid.best_score_
	# prdict on test set 
	predict_rate = RF_grid.predict(X_test)
	X_test['predict_rate'] = predict_rate
	# merge back to origin df 
	prediction_ = pd.merge(X_test,df_train,left_index=True,right_index=True)
	# print final predict result 
	print (prediction_[['id','predict_rate','ratings' ]])
	return prediction_
	"""
	---------------- TODO ---------------- 
	1) predict on test data
	2) tune the super-parameter / 
	3) modify train func let users can randomly rate songs 
	---------------- TODO ---------------- 

	"""




# -----------------------------

if __name__ == '__main__':
	main()




