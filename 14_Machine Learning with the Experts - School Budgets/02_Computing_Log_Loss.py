# Computing log loss with NumPy
# To see how the log loss metric handles the trade-off between accuracy and confidence, we will use some sample data generated with NumPy and compute the log loss using the provided function compute_log_loss(), which Peter showed you in the video.

# 5 one-dimensional numeric arrays simulating different types of predictions have been pre-loaded: actual_labels, correct_confident, correct_not_confident, wrong_not_confident, and wrong_confident.

# Your job is to compute the log loss for each sample set provided using the compute_log_loss(predicted_values, actual_values). It takes the predicted values as the first argument and the actual values as the second argument.
import numpy as np
actual_labels = np.array([1., 1., 1., 1., 1., 0., 0., 0., 0., 0.])
correct_confident = np.array([0.95, 0.95, 0.95, 0.95, 0.95, 0.05, 0.05, 0.05, 0.05, 0.05])
correct_not_confident = np.array([0.65, 0.65, 0.65, 0.65, 0.65, 0.35, 0.35, 0.35, 0.35, 0.35])
wrong_not_confident = np.array([0.35, 0.35, 0.35, 0.35, 0.35, 0.65, 0.65, 0.65, 0.65, 0.65])
wrong_confident = np.array([0.05, 0.05, 0.05, 0.05, 0.05, 0.95, 0.95, 0.95, 0.95, 0.95])

import numpy as np
def compute_log_loss(predicted, actual, eps=1e-14):
 """ Computes the logarithmic loss between predicted and
 actual when these are 1D arrays.
 :param predicted: The predicted probabilities as floats between 0-1
 :param actual: The actual binary labels. Either 0 or 1.
 :param eps (optional): log(0) is inf, so we need to offset our
 predicted values slightly by eps from 0 or 1.
 """
 predicted = np.clip(predicted, eps, 1 - eps)
 loss = -1 * np.mean(actual * np.log(predicted)
 + (1 - actual)
 * np.log(1 - predicted))

 return loss
 
# Compute and print log loss for 1st case
correct_confident_loss = compute_log_loss(correct_confident, actual_labels)
print("Log loss, correct and confident: {}".format(correct_confident_loss)) 

# Compute log loss for 2nd case
correct_not_confident_loss = compute_log_loss(correct_not_confident, actual_labels)
print("Log loss, correct and not confident: {}".format(correct_not_confident_loss)) 

# Compute and print log loss for 3rd case
wrong_not_confident_loss = compute_log_loss(wrong_not_confident, actual_labels)
print("Log loss, wrong and not confident: {}".format(wrong_not_confident_loss)) 

# Compute and print log loss for 4th case
wrong_confident_loss = compute_log_loss(wrong_confident, actual_labels)
print("Log loss, wrong and confident: {}".format(wrong_confident_loss)) 

# Compute and print log loss for actual labels
actual_labels_loss = compute_log_loss(actual_labels, actual_labels)
print("Log loss, actual labels: {}".format(actual_labels_loss)) 
# <script.py> output:
#     Log loss, correct and confident: 0.05129329438755058
#     Log loss, correct and not confident: 0.4307829160924542
#     Log loss, wrong and not confident: 1.049822124498678
#     Log loss, wrong and confident: 2.9957322735539904
#     Log loss, actual labels: 9.99200722162646e-15
# Log loss penalizes highly confident wrong answers much more than any other type. This will be a good metric to use on your models.