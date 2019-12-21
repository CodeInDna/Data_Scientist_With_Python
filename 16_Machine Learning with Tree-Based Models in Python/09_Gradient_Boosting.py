# Define the GB regressor
# You'll now revisit the Bike Sharing Demand dataset that was introduced in the previous chapter. Recall that your task is to predict the bike rental demand using historical weather data from the Capital Bikeshare program in Washington, D.C.. For this purpose, you'll be using a gradient boosting regressor.
# As a first step, you'll start by instantiating a gradient boosting regressor which you will train in the next exercise.
# Import GradientBoostingRegressor
from sklearn.ensemble import GradientBoostingRegressor

# Instantiate gb
gb = GradientBoostingRegressor(n_estimators=200, 
            max_depth=4,
            random_state=2)

# Train the GB regressor
# You'll now train the gradient boosting regressor gb that you instantiated in the previous exercise and predict test set labels.
# The dataset is split into 80% train and 20% test. Feature matrices X_train and X_test, as well as the arrays y_train and y_test are available in your workspace. In addition, we have also loaded the model instance gb that you defined in the previous exercise.
# Fit gb to the training set
gb.fit(X_train, y_train)

# Predict test set labels
y_pred = gb.predict(X_test)

# Evaluate the GB regressor
# Now that the test set predictions are available, you can use them to evaluate the test set Root Mean Squared Error (RMSE) of gb.
# y_test and predictions y_pred are available in your workspace.
# Import mean_squared_error as MSE
from sklearn.metrics import mean_squared_error as MSE

# Compute MSE
mse_test = MSE(y_test, y_pred)

# Compute RMSE
rmse_test = mse_test ** (0.5)

# Print RMSE
print('Test set RMSE of gb: {:.3f}'.format(rmse_test))
# <script.py> output:
#     Test set RMSE of gb: 52.065