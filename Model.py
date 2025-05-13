import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split

# load the cleaned data
df = pd.read_csv('deploy_df')

# Drop the unnamed index column if present
if 'Unnamed: 0' in df.columns:
    df.drop('Unnamed: 0', axis=1, inplace=True)

# get the indepentedn variables

x= df.drop('Price',axis=1)

# get the dependent variable y

y=df['Price']

# split the dtaa into train test
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 50)

# run the model

from catboost import CatBoostRegressor

cat=CatBoostRegressor()
cat.fit(X_train,y_train)
# predict
# predict using catboost
y_pred=cat.predict(X_test)

# pickle the model

import pickle
pickle.dump(cat,open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
print(y_pred)

