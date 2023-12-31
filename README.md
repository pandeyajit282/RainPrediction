# Rain_Prediction

A project on predicting whether it will rain tomorrow or not by using the Rainfall in Australia dataset. This project is tested over different models like catboost, logistic regression, xgboost, random forest, bagging classifier etc.. Out of these models bagging performed best giving an accuracy of 0.86 . In this, I also performed Hyperparameter tuning for all the models.

### [Download random forest model](https://drive.google.com/file/d/1wbcmGsb4qdkflORx5xFMuTGdQk8xiMNW/view?usp=sharing)

### Web App link: https://rainprediction-jtfsdsjdgqrbw6pveunym8.streamlit.app/

## Workflow

### Data Collection:
- [Rainfall Prediction in Australia dataset](https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package) from Kaggle

### Data Preprocessing:
- Missing Values Handled by Random Sample imputation to maintain the variance
- Categorical Values like location, wind direction are handled by using Target guided encoding
- Outliers are handled using IQR and boxplot
- Feature Scaling was done
- Imbalanced Dataset was handled using SMOTE

###  Model Creation:
- Different types of models were tried like logistic regression, KNN, random forest, Adaboost, xgboost.
- All the models worked with random search cross validation.
- Out of these random forest gave the best accuracy.

### Model Deployment
The model is deployed using streamlit at streamlit cloud server.




