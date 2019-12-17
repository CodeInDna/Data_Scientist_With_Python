# Regularization I: Lasso
# In the video, you saw how Lasso selected out the 'RM' feature as being the most important for predicting Boston house prices, while shrinking the coefficients of certain other features to 0. Its ability to perform feature selection in this way becomes even more useful when you are dealing with data involving thousands of features.

# In this exercise, you will fit a lasso regression to the Gapminder data you have been working with and plot the coefficients. Just as with the Boston data, you will find that the coefficients of some features are shrunk to 0, with only the most important ones remaining.

# The feature and target variable arrays have been pre-loaded as X and y

# Import Lasso
from sklearn.linear_model import Lasso

# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.4, normalize = True)

# Fit the regressor to the data
lasso.fit(X,y).coef_

# Compute and print the coefficients
lasso_coef = lasso.fit(X,y).coef_
print(lasso_coef)

# Plot the coefficients
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)
plt.show()
# <script.py> output:
#     [-0.         -0.         -0.          0.          0.          0.       -0.         -0.07087587]

 # According to the lasso algorithm, it seems like 'child_mortality' is the most important feature when predicting life expectancy.

#  Regularization II: Ridge
# Lasso is great for feature selection, but when building regression models, Ridge regression should be your first choice.

# Recall that lasso performs regularization by adding to the loss function a penalty term of the absolute value of each coefficient multiplied by some alpha. This is also known as L1 regularization because the regularization term is the L1 norm of the coefficients. This is not the only way to regularize, however.

# If instead you took the sum of the squared values of the coefficients multiplied by some alpha - like in Ridge regression - you would be computing the L2 norm. In this exercise, you will practice fitting ridge regression models over a range of different alphas, and plot cross-validated R2 scores for each, using this function that we have defined for you, which plots the R2 score as well as standard error for each alpha:

# def display_plot(cv_scores, cv_scores_std):
#     fig = plt.figure()
#     ax = fig.add_subplot(1,1,1)
#     ax.plot(alpha_space, cv_scores)

#     std_error = cv_scores_std / np.sqrt(10)

#     ax.fill_between(alpha_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2)
#     ax.set_ylabel('CV Score +/- Std Error')
#     ax.set_xlabel('Alpha')
#     ax.axhline(np.max(cv_scores), linestyle='--', color='.5')
#     ax.set_xlim([alpha_space[0], alpha_space[-1]])
#     ax.set_xscale('log')
#     plt.show()
# Don't worry about the specifics of the above function works. The motivation behind this exercise is for you to see how the R2 score varies with different alphas, and to understand the importance of selecting the right value for alpha. You'll learn how to tune alpha in the next chapter.

# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Setup the array of alphas and lists to store scores
alpha_space = np.logspace(-4, 0, 50)
ridge_scores = []
ridge_scores_std = []

# Create a ridge regressor: ridge
ridge = Ridge(normalize=True)

# Compute scores over range of alphas
for alpha in alpha_space:

    # Specify the alpha value to use: ridge.alpha
    ridge.alpha = alpha
    
    # Perform 10-fold CV: ridge_cv_scores
    ridge_cv_scores = cross_val_score(ridge,X,y,cv=10)
    
    # Append the mean of ridge_cv_scores to ridge_scores
    ridge_scores.append(np.mean(ridge_cv_scores))
    
    # Append the std of ridge_cv_scores to ridge_scores_std
    ridge_scores_std.append(np.std(ridge_cv_scores))

# Display the plot
display_plot(ridge_scores, ridge_scores_std)