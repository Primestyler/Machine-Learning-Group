| Attempt | Model | Hyperparameters | Train set F1-score | Kaggle score | Sampling |
| ------- | ----- | --------------- | ------------------ | ------------ | -------- |
| 1 | KNN | {'algorithm': 'ball_tree', 'n_neighbors': 5, 'weights': 'uniform'} | 0.732912841543329 | 0.02985 | Random Undersampling |
| 1 | LR | {'C': 0.1, 'class_weight': None, 'penalty': 'l2', 'solver': 'newton-cg'} | 0.7972094791854771 | 0.04449 | Random Undersampling |
| 1 | SVC | {'C': 1.0, 'degree': 2, 'gamma': 'auto', 'kernel': 'rbf'} | 0.7896628012306766 | 0.02853 | Random Undersampling |
| 1 | DT | {'criterion': 'log_loss', 'max_depth': 3, 'max_features': 'log2', 'min_samples_leaf': 40, 'min_samples_split': 3} | 0.7865739505176125 | 0.04493 | Random Undersampling | 
| 1 | RF | {'bootstrap': True, 'criterion': 'entropy', 'max_depth': 4, 'max_features': 'log2', 'min_samples_leaf': 3, 'min_samples_split': 2, 'n_estimators': 50} | 0.7961498457891335 | 0.05213 | Random Undersampling |
| 1 | GB | {'criterion': 'friedman_mse', 'loss': 'log_loss', 'max_depth': 2, 'max_features': 'log2', 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50} | 0.7958872622710376 | 0.06674 | Random Undersampling |
|  |  |  |  |  |  |
| 2 | KNN | {'algorithm': 'ball_tree', 'n_neighbors': 5, 'weights': 'uniform'} | 0.780265157053129 | 0.05711 | No sampling |
| 2 | LR | {'C': 0.1, 'penalty': 'l1', 'solver': 'liblinear'} | 0.7952321925088596 | 0.05298 | No sampling |
| 2 | SVC | {'C': 0.01, 'degree': 2, 'gamma': 'auto', 'kernel': 'linear'} | 0.7928410177376314 | 0.05128 | No sampling |
| 2 | DT | {'criterion': 'gini', 'max_depth': 3, 'max_features': 'sqrt'} | 0.7824656693269317 | 0.05370 | No sampling | 
| 2 | RF | {'bootstrap': True, 'criterion': 'entropy', 'max_depth': 3, 'max_features': 'sqrt', 'n_estimators': 50} | 0.7940226736665905 | 0.05144 | No sampling |
| 2 | GB | {'criterion': 'friedman_mse', 'loss': 'log_loss', 'max_depth': 3, 'max_features': 'sqrt', 'n_estimators': 50} | 0.7896094906908887 | 0.06513 | No sampling |
|  |  |  |  |  |  |
| 3 | KNN | {'algorithm': 'brute', 'n_neighbors': 1, 'weights': 'uniform'} | 0.046306361865738464 | 0.03571 | SMOTE |
| 3 | LR | {'C': 0.001, 'penalty': 'l1', 'solver': 'liblinear'} | 0.0 | 0.00000 | SMOTE |
| 3 | SVC | {'C': 0.001, 'degree': 2, 'gamma': 'auto', 'kernel': 'linear'} | 0.0 | 0.00000 | SMOTE |
| 3 | DT | {'criterion': 'gini', 'max_depth': 10, 'max_features': 'log2'} | 0.031596544998606854 | 0.05555 | SMOTE | 
| 3 | RF | {'bootstrap': True, 'criterion': 'gini', 'max_depth': 3, 'max_features': 'sqrt', 'n_estimators': 50} | 0.0 | 0.00000 | SMOTE |
| 3 | GB | {'criterion': 'friedman_mse', 'loss': 'log_loss', 'max_depth': 10, 'max_features': 'sqrt', 'n_estimators': 50} | 0.041848563631940394 | 0.00000 | SMOTE |
|  |  |  |  |  |  |
| 4 | KNN | {'algorithm': 'brute', 'n_neighbors': 3, 'weights': 'uniform'} | 0.8881477423791307 | 0.04739 | Random Undersampling |
| 4 | LR | {'C': 0.001, 'penalty': 'l1', 'solver': 'liblinear'} | 0.7961058702755084 | 0.05144 | Random Undersampling |
| 4 | SVC | {'C': 1.0, 'degree': 2, 'gamma': 'auto', 'kernel': 'rbf'} | 0.7966445438611243 | 0.05228 | Random Undersampling |
| 4 | DT | {'criterion': 'gini', 'max_depth': 10, 'max_features': 'log2'} | 0.8413312864254378 | 0.03601 | Random Undersampling | 
| 4 | RF | {'bootstrap': True, 'criterion': 'gini', 'max_depth': 10, 'max_features': 'log2', 'n_estimators': 50} | 0.8698319062248533 | 0.04440 | Random Undersampling |
| 4 | GB | {'criterion': 'squared_error', 'loss': 'log_loss', 'max_depth': 10, 'max_features': 'log2', 'n_estimators': 50} | 0.9122955371594136 | 0.03967 | Random Undersampling |
|  |  |  |  |  |  |
| 5 | KNN | {'algorithm': 'ball_tree', 'n_neighbors': 3, 'weights': 'uniform'} | 0.7871283370028331 | 0.05255 | No sampling |
| 5 | LR | {'C': 0.01, 'penalty': 'l1', 'solver': 'liblinear'} | 0.8086006634200519 | 0.05132 | No sampling |
| 5 | SVC | {'C': 0.01, 'degree': 2, 'gamma': 'auto', 'kernel': 'linear'} | 0.8108169267354814 | 0.05000 | No sampling |
| 5 | DT | {'criterion': 'log_loss', 'max_depth': 5, 'max_features': 'log2'} | 0.7979568323422035 | 0.06534 | No sampling | 
| 5 | RF | {'bootstrap': True, 'criterion': 'entropy', 'max_depth': 6, 'max_features': 'log2', 'n_estimators': 50} | 0.8126182140249576 | 0.05243 | No sampling |
| 5 | GB | {'criterion': 'squared_error', 'loss': 'log_loss', 'max_depth': 3, 'max_features': 'sqrt', 'n_estimators': 50} | 0.8122200713700967 | 0.05313 | No sampling |
|  |  |  |  |  |  |
| 6 | KNN | {'algorithm': 'ball_tree', 'n_neighbors': 1, 'weights': 'uniform'} | 0.034069993118971506 | 0.03571 | SMOTE |
| 6 | LR | {'C': 0.001, 'penalty': 'l1', 'solver': 'liblinear'} | 0.0 | 0.00000 | SMOTE |
| 6 | SVC | {'C': 0.001, 'degree': 2, 'gamma': 'auto', 'kernel': 'linear'} | 0.0 | 0.00000 | SMOTE |
| 6 | DT | {'criterion': 'gini', 'max_depth': 9, 'max_features': 'log2'} | 0.028287927203159386 | 0.00000 | SMOTE | 
| 6 | RF | {'bootstrap': True, 'criterion': 'entropy', 'max_depth': 10, 'max_features': 'sqrt', 'n_estimators': 50} | 0.0041666666666666675 | 0.00000 | SMOTE |
| 6 | GB | {'criterion': 'friedman_mse', 'loss': 'log_loss', 'max_depth': 9, 'max_features': 'sqrt', 'n_estimators': 50} | 0.03736243353489092 | 0.07594 | SMOTE |
|  |  |  |  |  |  |
| 7 | KNN | {'algorithm': 'ball_tree', 'n_neighbors': 3, 'weights': 'uniform'} | 0.8953336136535854 | 0.04258 | No sampling |
| 7 | LR | {'C': 0.001, 'penalty': 'l1', 'solver': 'liblinear'} | 0.7974738160756464 | 0.05147 | No sampling |
| 7 | SVC | {'C': 1.0, 'degree': 2, 'gamma': 'auto', 'kernel': 'rbf'} | 0.7980947089741174 | 0.05230 | No sampling |
| 7 | DT | {'criterion': 'gini', 'max_depth': 10, 'max_features': 'log2'} | 0.8415657351195541 | 0.04388 |  No sampling |
| 7 | RF | {'bootstrap': True, 'criterion': 'gini', 'max_depth': 10, 'max_features': 'log2', 'n_estimators': 50} | 0.8717849188670568 | 0.04421 | No sampling |
| 7 | GB | {'criterion': 'squared_error', 'loss': 'log_loss', 'max_depth': 10, 'max_features': 'log2', 'n_estimators': 50} | 0.9164921490500427 | 0.03919 | No sampling |