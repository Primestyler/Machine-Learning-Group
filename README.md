| Attempt | Model | Hyperparameters | Train set F1-score | Kaggle score |
| ------- | ----- | --------------- | ------------------ | ------------ |
| 1 | KNN | {'algorithm': 'ball_tree', 'n_neighbors': 5, 'weights': 'uniform'} | 0.732912841543329 | 0.02985 |
| 1 | LR | {'C': 0.1, 'class_weight': None, 'penalty': 'l2', 'solver': 'newton-cg'} | 0.7972094791854771 | 0.04449 |
| 1 | SVC | {'C': 1.0, 'degree': 2, 'gamma': 'auto', 'kernel': 'rbf'} | 0.7896628012306766 | 0.02853 |
| 1 | DT | {'criterion': 'log_loss', 'max_depth': 3, 'max_features': 'log2', 'min_samples_leaf': 40, 'min_samples_split': 3} | 0.7865739505176125 | 0.04493 | 
| 1 | RF | {'bootstrap': True, 'criterion': 'entropy', 'max_depth': 4, 'max_features': 'log2', 'min_samples_leaf': 3, 'min_samples_split': 2, 'n_estimators': 50} | 0.7961498457891335 | 0.05213 |
| 1 | GB | {'criterion': 'friedman_mse', 'loss': 'log_loss', 'max_depth': 2, 'max_features': 'log2', 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 50} | 0.7958872622710376 | 0.06674 |