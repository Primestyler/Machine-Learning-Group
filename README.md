| Attempt | Model | Hyperparameters | Train set F1-score | Kaggle score |
| ------- | ----- | --------------- | ------------------ | ------------ |
| 1 | KNN | {'algorithm': 'ball_tree', 'n_neighbors': 5, 'weights': 'uniform'} | 0.732912841543329 | 0.02985 |
| 1 | LR | {'C': 0.1, 'class_weight': None, 'penalty': 'l2', 'solver': 'newton-cg'} | 0.7972094791854771 | 0.04449 |
| 1 | SVC | {'C': 1.0, 'degree': 2, 'gamma': 'auto', 'kernel': 'rbf'} | 0.7896628012306766 | 0.02853 |
| 1 | DT | {'criterion': 'log_loss', 'max_depth': 3, 'max_features': 'log2', 'min_samples_leaf': 40, 'min_samples_split': 3} | 0.7865739505176125 | 0.04493 | 
| 1 | RF | {'bootstrap': True, 'criterion': 'entropy', 'max_depth': 4, 'max_features': 'log2', 'min_samples_leaf': 3, 'min_samples_split': 2, 'n_estimators': 50} | 0.7961498457891335 | 0.05213 |
| 1 | GB | {'criterion': 'friedman_mse', 'loss': 'log_loss', 'max_depth': 2, 'max_features': 'log2', 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50} | 0.7958872622710376 | 0.06674 |
|  |  |  |  |  |
| 2 | KNN | {'algorithm': 'ball_tree', 'n_neighbors': 5, 'weights': 'uniform'} | 0.780265157053129 | 0.05711 |
| 2 | LR | {'C': 0.1, 'penalty': 'l1', 'solver': 'liblinear'} | 0.7952321925088596 | 0.05298 |
| 2 | SVC | {'C': 0.01, 'degree': 2, 'gamma': 'auto', 'kernel': 'linear'} | 0.7928410177376314 | 0.05128 |
| 2 | DT | {'criterion': 'gini', 'max_depth': 3, 'max_features': 'sqrt'} | 0.7824656693269317 | 0.05370 | 
| 2 | RF | {'bootstrap': True, 'criterion': 'entropy', 'max_depth': 3, 'max_features': 'sqrt', 'n_estimators': 50} | 0.7940226736665905 | 0.05144 |
| 2 | GB | {'criterion': 'friedman_mse', 'loss': 'log_loss', 'max_depth': 3, 'max_features': 'sqrt', 'n_estimators': 50} | 0.7896094906908887 | 0.06513 |
|  |  |  |  |  |
| 3 | KNN | {'algorithm': 'brute', 'n_neighbors': 1, 'weights': 'uniform'} | 0.046306361865738464 | 0.03571 |
| 3 | LR | {'C': 0.001, 'penalty': 'l1', 'solver': 'liblinear'} | 0.0 | 0.00000 |
| 3 | SVC | {'C': 0.001, 'degree': 2, 'gamma': 'auto', 'kernel': 'linear'} | 0.0 | 0.00000 |
| 3 | DT | {'criterion': 'gini', 'max_depth': 10, 'max_features': 'log2'} | 0.031596544998606854 | 0.05555 | 
| 3 | RF | {'bootstrap': True, 'criterion': 'gini', 'max_depth': 3, 'max_features': 'sqrt', 'n_estimators': 50} | 0.0 | 0.00000 |
| 3 | GB | {'criterion': 'friedman_mse', 'loss': 'log_loss', 'max_depth': 10, 'max_features': 'sqrt', 'n_estimators': 50} | 0.041848563631940394 | 0.00000 |
|  |  |  |  |  |
| 4 | KNN | {'algorithm': 'brute', 'n_neighbors': 3, 'weights': 'uniform'} | 0.8881477423791307 | 0.04739 |
| 4 | LR | {'C': 0.001, 'penalty': 'l1', 'solver': 'liblinear'} | 0.7961058702755084 | 0.05144 |
| 4 | SVC | {'C': 1.0, 'degree': 2, 'gamma': 'auto', 'kernel': 'rbf'} | 0.7966445438611243 | 0.05228 |
| 4 | DT | {'criterion': 'gini', 'max_depth': 10, 'max_features': 'log2'} | 0.8413312864254378 | 0.03601 | 
| 4 | RF | {'bootstrap': True, 'criterion': 'gini', 'max_depth': 10, 'max_features': 'log2', 'n_estimators': 50} | 0.8698319062248533 | 0.04440 |
| 4 | GB | {'criterion': 'squared_error', 'loss': 'log_loss', 'max_depth': 10, 'max_features': 'log2', 'n_estimators': 50} | 0.9122955371594136 | 0.03967 |