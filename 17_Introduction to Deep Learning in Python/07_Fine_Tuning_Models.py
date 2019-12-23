# Changing optimization parameters
# It's time to get your hands dirty with optimization. You'll now try optimizing a model at a very low learning rate, a very high learning rate, and a "just right" learning rate. You'll want to look at the results after running this exercise, remembering that a low value for the loss function is good.

# For these exercises, we've pre-loaded the predictors and target values from your previous classification models (predicting who would survive on the Titanic). You'll want the optimization to start from scratch every time you change the learning rate, to give a fair comparison of how each learning rate did in your results. So we have created a function get_new_model() that creates an unoptimized model to optimize.
# Import the SGD optimizer
from keras.optimizers import SGD

# Create list of learning rates: lr_to_test
lr_to_test = [.000001, 0.01, 1]

# Loop over learning rates
for lr in lr_to_test:
    print('\n\nTesting model with learning rate: %f\n'%lr )
    
    # Build new model to test, unaffected by previous models
    model = get_new_model()
    
    # Create SGD optimizer with specified learning rate: my_optimizer
    my_optimizer = SGD(lr = lr)
    
    # Compile the model
    model.compile(optimizer = my_optimizer, loss='categorical_crossentropy')
    
    # Fit the model
    model.fit(predictors, target)

# Evaluating model accuracy on validation dataset
# Now it's your turn to monitor model accuracy with a validation data set. A model definition has been provided as model. Your job is to add the code to compile it and then fit it. You'll check the validation score in each epoch.
# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]
input_shape = (n_cols,)

# Specify the model
model = Sequential()
model.add(Dense(100, activation='relu', input_shape = input_shape))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
hist = model.fit(predictors, target, validation_split=0.3)

# Early stopping: Optimizing the optimization
# Now that you know how to monitor your model performance throughout optimization, you can use early stopping to stop optimization when it isn't helping any more. Since the optimization stops automatically when it isn't helping, you can also set a high value for epochs in your call to .fit(), as Dan showed in the video.
# The model you'll optimize has been specified as model. As before, the data is pre-loaded as predictors and target.
# Import EarlyStopping
from keras.callbacks import EarlyStopping

# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]
input_shape = (n_cols,)

# Specify the model
model = Sequential()
model.add(Dense(100, activation='relu', input_shape = input_shape))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Define early_stopping_monitor
early_stopping_monitor = EarlyStopping(patience = 2)

# Fit the model
model.fit(predictors,target, epochs=30, validation_split = 0.3, callbacks = [early_stopping_monitor])
# Because optimization will automatically stop when it is no longer helpful, it is okay to specify the maximum number of epochs as 30 rather than using the default of 10 that you've used so far. Here, it seems like the optimization stopped after 7 epochs.
# <script.py> output:
#     Train on 623 samples, validate on 268 samples
#     Epoch 1/30
    
#  32/623 [>.............................] - ETA: 1s - loss: 5.6563 - acc: 0.4688
# 623/623 [==============================] - 0s - loss: 1.6420 - acc: 0.5714 - val_loss: 1.0775 - val_acc: 0.6642
#     Epoch 2/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 1.8352 - acc: 0.4688
# 623/623 [==============================] - 0s - loss: 0.8322 - acc: 0.6067 - val_loss: 0.5692 - val_acc: 0.7276
#     Epoch 3/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 0.8555 - acc: 0.6250
# 623/623 [==============================] - 0s - loss: 0.7181 - acc: 0.6501 - val_loss: 0.5278 - val_acc: 0.7649
#     Epoch 4/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 1.0081 - acc: 0.6562
# 623/623 [==============================] - 0s - loss: 0.6745 - acc: 0.6742 - val_loss: 0.5268 - val_acc: 0.7351
#     Epoch 5/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 0.5481 - acc: 0.7812
# 623/623 [==============================] - 0s - loss: 0.6718 - acc: 0.6517 - val_loss: 0.6719 - val_acc: 0.6754
#     Epoch 6/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 0.4679 - acc: 0.7812
# 623/623 [==============================] - 0s - loss: 0.6233 - acc: 0.6982 - val_loss: 0.5794 - val_acc: 0.7090
#     Epoch 7/30
    
#  32/623 [>.............................] - ETA: 0s - loss: 0.6601 - acc: 0.6562
# 623/623 [==============================] - 0s - loss: 0.6419 - acc: 0.6998 - val_loss: 0.6777 - val_acc: 0.6493

# Experimenting with wider networks
# Now you know everything you need to begin experimenting with different models!

# A model called model_1 has been pre-loaded. You can see a summary of this model printed in the IPython Shell. This is a relatively small network, with only 10 units in each hidden layer.

# In this exercise you'll create a new model called model_2 which is similar to model_1, except it has 100 units in each hidden layer.

# After you create model_2, both models will be fitted, and a graph showing both models loss score at each epoch will be shown. We added the argument verbose=False in the fitting commands to print out fewer updates, since you will look at these graphically instead of as text.

# Because you are fitting two models, it will take a moment to see the outputs after you hit run, so be patient.
# Define early_stopping_monitor
early_stopping_monitor = EarlyStopping(patience=2)

# Create the new model: model_2
model_2 = Sequential()

# Add the first and second layers
model_2.add(Dense(100, activation='relu', input_shape=input_shape))
model_2.add(Dense(100, activation='relu'))

# Add the output layer
model_2.add(Dense(2, activation='softmax'))

# Compile model_2
model_2.compile(optimizer = 'adam', loss='categorical_crossentropy', metrics = ['accuracy'])

# Fit model_1
model_1_training = model_1.fit(predictors, target, epochs=15, validation_split=0.2, callbacks=[early_stopping_monitor], verbose=False)

# Fit model_2
model_2_training = model_2.fit(predictors, target, epochs=15, validation_split=0.2, callbacks=[early_stopping_monitor], verbose=False)

# Create the plot
plt.plot(model_1_training.history['val_loss'], 'r', model_2_training.history['val_loss'], 'b')
plt.xlabel('Epochs')
plt.ylabel('Validation score')
plt.show()
# The blue model is the one you made, the red is the original model. Your model had a lower loss value, so it is the better model. 

# Adding layers to a network
# You've seen how to experiment with wider networks. In this exercise, you'll try a deeper network (more hidden layers).
# Once again, you have a baseline model called model_1 as a starting point. It has 1 hidden layer, with 50 units. You can see a summary of that model's structure printed out. You will create a similar network with 3 hidden layers (still keeping 50 units in each layer).
# This will again take a moment to fit both models, so you'll need to wait a few seconds to see the results after you run your code.
# The input shape to use in the first hidden layer
input_shape = (n_cols,)

# Create the new model: model_2
model_2 = Sequential()

# Add the first, second, and third hidden layers
model_2.add(Dense(50, activation='relu', input_shape = input_shape))
model_2.add(Dense(50, activation='relu'))
model_2.add(Dense(50, activation='relu'))

# Add the output layer
model_2.add(Dense(2, activation='softmax'))

# Compile model_2
model_2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit model 1
model_1_training = model_1.fit(predictors, target, epochs=20, validation_split=0.4, callbacks=[early_stopping_monitor], verbose=False)

# Fit model 2
model_2_training = model_2.fit(predictors, target, epochs=20, validation_split=0.4, callbacks=[early_stopping_monitor], verbose=False)

# Create the plot
plt.plot(model_1_training.history['val_loss'], 'r', model_2_training.history['val_loss'], 'b')
plt.xlabel('Epochs')
plt.ylabel('Validation score')
plt.show()
# The blue model is the one you made and the red is the original model. The model with the lower loss value is the better model.

# Experimenting with model structures
# You've just run an experiment where you compared two networks that were identical except that the 2nd network had an extra hidden layer. You see that this 2nd network (the deeper network) had better performance. Given that, which of the following would be a good experiment to run next for even better performance?

# ANSWER # Use more units in each hidden layer.
# Increasing the number of units in each hidden layer would be a good next step to try achieving even better performance.