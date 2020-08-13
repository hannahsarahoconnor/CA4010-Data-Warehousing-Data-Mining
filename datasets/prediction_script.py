import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from catboost import Pool, CatBoostRegressor

trained = trained_set.drop('price', axis=1)
trained_price = np.log(trained_set['price'])

X_trained, X_test, y_trained, y_test = train_test_split(trained, trained_price,test_size=0.33, random_state=42,
                                                                                                 shuffle=False)
#X_test stays the same
X_test, X_values, y_test, y_values = train_test_split(X_test,y_test, test_size=0.33, random_state=42, shuffle=False)

trained_pool = Pool(X_trained.values, y_trained.values)
test_pool = Pool(X_test.values)
values_pool = Pool(X_values.values, y_values.values)

cbr = CatBoostRegressor(iterations=99, 
                        depth=10, 
                        learning_rate=0.3, 
                        loss_function='RMSE',
                        random_seed=42,
                        eval_metric='RMSE',
                        use_best_model=True
                        )
cbr.fit(trained_pool, eval_set=values_pool, early_stopping_rounds=80)
predictions = cbr.predict(test_pool)
# calculate MAE, MSE, RMSE
print('RMSE: {}'.format(math.sqrt(mean_squared_error(y_test.values, predictions))))
print('MAE: {}'.format(math.sqrt(mean_absolute_error(y_test.values, predictions))))
print('MSE: {}'.format(mean_squared_error(y_test.values, predictions)))