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
|  |  |  |  |  |  |
| 8 | KNN | {'algorithm': 'ball_tree', 'n_neighbors': 5, 'weights': 'uniform'} | 0.7812271258946091 | 0.05231 | Random Undersampling |
| 8 | LR | {'C': 1.0, 'penalty': 'l1', 'solver': 'liblinear'} | 0.7991429129160128 | 0.05364 | Random Undersampling |
| 8 | SVC | {'C': 1.0, 'degree': 2, 'gamma': 'auto', 'kernel': 'rbf'} | 0.7995850249326868 | 0.05359 | Random Undersampling |
| 8 | DT | {'criterion': 'gini', 'max_depth': 6, 'max_features': 'log2'} | 0.7755218128184336 | 0.04917 |  Random Undersampling |
| 8 | RF | {'bootstrap': True, 'criterion': 'log_loss', 'max_depth': 4, 'max_features': 'log2', 'n_estimators': 50} | 0.8078962733402457 | 0.05100 | Random Undersampling |
| 8 | GB | {'criterion': 'friedman_mse', 'loss': 'log_loss', 'max_depth': 4, 'max_features': 'sqrt', 'n_estimators': 50} | 0.7986902871317192 | 0.05503 | Random Undersampling |
| 8 | XGB | {'gamma': 3, 'learning_rate': 0.01, 'max_depth': 7, 'n_estimators': 50, 'objective': 'binary:logistic'} | 0.8040266428061328 | 0.05494 | Random Undersampling |
| 8 | VC_Hard | | 0.8014472245375431 | 0.05263 | Random Undersampling |
| 8 | VC_Soft | | 0.8008455750780138 | 0.05365 | Random Undersampling |
|  |  |  |  |  |  |
| 9 | KNN | {'algorithm': 'ball_tree', 'n_neighbors': 1, 'weights': 'uniform'} | 0.3693721992887028 | 0.11981 | Instant Hardness Threshold |
| 9 | LR | {'C': 0.001, 'penalty': None, 'solver': 'newton-cholesky'} | 0.12572063234345973 | 0.00000 | Instant Hardness Threshold |
| 9 | SVC | {'C': 0.1, 'degree': 4, 'gamma': 'auto', 'kernel': 'poly'} | 0.1071333984972799 | 0.02898 | Instant Hardness Threshold |
| 9 | DT | {'criterion': 'entropy', 'max_depth': 10, 'max_features': 'log2'} | 0.3105107174229027 | 0.12403 |  Instant Hardness Threshold |
| 9 | RF | {'bootstrap': True, 'criterion': 'gini', 'max_depth': 10, 'max_features': 'log2', 'n_estimators': 50} | 0.3027609336805059 | 0.11009 | Instant Hardness Threshold |
| 9 | GB | {'criterion': 'friedman_mse', 'loss': 'log_loss', 'max_depth': 10, 'max_features': 'sqrt', 'n_estimators': 50} | 0.3607623794299673 | 0.11976 | Instant Hardness Threshold |
| 9 | XGB | {'gamma': 0, 'learning_rate': 1.0, 'max_depth': 9, 'n_estimators': 50, 'objective': 'binary:logistic'} | 0.36683873054124766 | 0.10370 | Instant Hardness Threshold |
| 9 | VC_Hard | | 0.2683554563836443 | 0.05940 | Instant Hardness Threshold |
| 9 | VC_Soft | | 0.2912360025173698 | 0.08080 | Instant Hardness Threshold |
|  |  |  |  |  |  |
| 10 | KNN | {'n_neighbors': 1, 'p': 2} | 0.3933719124261561 | 0.12871 | Instant Hardness Threshold |
| 10 | LR | {'C': 1.0, 'max_iter': 100} | 0.12967892627247585 | 0.00000 | Instant Hardness Threshold |
| 10 | SVC | {'C': 0.1, 'gamma': 2, 'kernel': 'rbf', 'max_iter': 400} | 0.30000396801742246 | 0.04347 | Instant Hardness Threshold |
| 10 | DT | {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 4, 'splitter': 'best'} | 0.3022319015651108 | 0.07352 |  Instant Hardness Threshold |
| 10 | RF | {'criterion': 'log_loss', 'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 100} | 0.2971243054613969 | 0.12631 | Instant Hardness Threshold |
| 10 | GB | {'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 6, 'n_estimators': 100} | 0.3941928526035431 | 0.16438 | Instant Hardness Threshold |
| 10 | XGB | {'gamma': 0, 'learning_rate': 1.0, 'max_depth': 5, 'n_estimators': 100} | 0.34653065889912027 | 0.11290 | Instant Hardness Threshold |
| 10 | VC_Hard | | 0.3104911324566141 | 0.08080 | Instant Hardness Threshold |
| 10 | VC_Soft | | 0.38978325786191964 | 0.16176 | Instant Hardness Threshold |
|  |  |  |  |  |  |
| 11 | KNN | {'n_neighbors': 1, 'p': 3} | 0.36631762286820974 | 0.11483 | Instant Hardness Threshold |
| 11 | LR | {'C': 1.0, 'max_iter': 50} | 0.12355677767807416 | 0.00000 | Instant Hardness Threshold |
| 11 | SVC | {'C': 0.1, 'gamma': 3, 'kernel': 'rbf'} | 0.27489290774783126 | 0.12371 | Instant Hardness Threshold |
| 11 | DT | {'max_depth': 12, 'min_samples_leaf': 3, 'min_samples_split': 9} | 0.3093676376596971 | 0.09756 |  Instant Hardness Threshold |
| 11 | RF | {'max_depth': 13, 'min_samples_leaf': 3, 'min_samples_split': 4} | 0.25054719494697303 | 0.09090 | Instant Hardness Threshold |
| 11 | GB | {'max_depth': 13, 'min_samples_leaf': 5, 'min_samples_split': 5} | 0.40495272867535775 | 0.15384 | Instant Hardness Threshold |
| 11 | XGB | {'gamma': 0, 'learning_rate': 1.0, 'max_depth': 4} | 0.3590310773587727 | 0.10526 | Instant Hardness Threshold |
| 11 | VC_Hard | | 0.2924801849192789 | 0.08888 | Instant Hardness Threshold |
| 11 | VC_Soft | | 0.3894622441200358 | 0.10606 | Instant Hardness Threshold |