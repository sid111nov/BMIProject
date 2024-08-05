
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_percentage_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from xgboost import XGBRegressor

class Models:
    def get_Model_Dict(self):
        models = {
            "Linear Regression": LinearRegression(),
            "Lasso": Lasso(),
            "Ridge": Ridge(),
            "K-Neighbors Regressor": KNeighborsRegressor(),
            "Decision Tree": DecisionTreeRegressor(),
            "Random Forest Regressor": RandomForestRegressor(),
            "XGBRegressor": XGBRegressor()
            
        }
        return models
    
    def get_Hyper_Params(self):
        hyper = {
                
            "Linear Regression": {
                'alpha': [0.1, 0.5, 1, 5, 10],
                'l1_ratio': [0.1, 0.5, 0.9],
                'solver': ['svd', 'cholesky', 'lsqr'],
                'tol': [1e-4, 1e-5, 1e-6],
                'max_iter': [100, 500, 1000],
                'fit_intercept': [True, False],
                'normalize': [True, False]
            },
            "Lasso": {
                'alpha': [0.1, 0.5, 1, 5, 10],
                'max_iter': [100, 500, 1000],
                'tol': [1e-4, 1e-5, 1e-6],
                'fit_intercept': [True, False],
                'normalize': [True, False]
            },
            "Ridge": {
                'alpha': [0.1, 0.5, 1, 5, 10],
                'max_iter': [100, 500, 1000],
                'tol': [1e-4, 1e-5, 1e-6],
                'fit_intercept': [True, False],
                'normalize': [True, False]
            },
            "K-Neighbors Regressor": {
                'n_neighbors': [3, 5, 7, 9],
                'weights': ['uniform', 'distance'],
                'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute']
            },
            "Decision Tree": {
                'max_depth': [3, 5, 7, None],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 5, 10]
            },
            "Random Forest Regressor": {
                'n_estimators': [10, 50, 100],
                'max_depth': [3, 5, 7, None],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 5, 10]
            },
            "XGBRegressor": {
                'learning_rate': [0.1, 0.5, 1],
                'max_depth': [3, 5, 7],
                'n_estimators': [10, 50, 100],
                'gamma': [0, 0.1, 0.5],
                'subsample': [0.5, 0.8, 1],
                'colsample_bytree': [0.5, 0.8, 1]
            }
        }

        return hyper
    
    def get_Scores(self,Y_true,Y_pred):
            score = []
            mse = mean_squared_error(Y_true,Y_pred)
            r2  = r2_score(Y_true,Y_pred)
            mape = mean_absolute_percentage_error(Y_true,Y_pred)
            score.extend([mse,r2,mape])
            return score