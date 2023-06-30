https://www.geeksforgeeks.org/underfitting-and-overfitting-in-machine-learning/

# First, let's talk about Bias and Variance
## Bias
- Error rate of the training data
- High value of error rate = High Bias
- Low value of error rate = Low Bias
## Variance
- The gap of bias between training and testing data
- High gap = High Variance
- Low gap = Low Variance
- Usually, low varinace is preferred to generalize a model

# Underfitting
* When model cannot capture the underlying trend of data
	* i.e. It only performs well on training data but performs poorly on testing data
* Meaning, the model is not fit the data
## **Reasons for** Underfitting
1. High bias and low variance.
2. The size of the training dataset used is not enough.
3. The model is too simple.
4. Training data is not cleaned and also contains noise in it.
## Techniques to Reduce Underfitting
1. Increase model complexity.
2. Increase the number of features, performing feature engineering
3. Remove noise from the data.
4. Increase the number of epochs or increase the duration of training to get better results.
# Overfitting
- When the model does not make accurate predictions on testing data.
	- When a model gets trained with so much data, it starts learning from the noise and inaccurate data entries in our data set. 
## Reasons for Overfitting
 1. High variance and low bias.
 2. The model is too complex.
 3. The size of the training data.
## Techniques to Reduce Overfitting
1. Increase training data.
2. Reduce model complexity.
3. Early stopping during the training phase
4. Ridge Regularization and Lasso Regularization.
5. Use dropout for neural networks to tackle overfitting.