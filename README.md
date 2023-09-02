# SBSPS-Challenge-10970-Slient-Speech-Recognition-Automatic-Lip-reading-Model-using-3D-CNN-and-GRU
Slient Speech Recognition : Automatic Lip reading Model using 3D CNN and GRU


## IBM HACK CHALLENGE 2023: By Team Radiators 
Description of a Convolutional Neural Network (CNN) used for visual speech recognition. 

1. Training Accuracy and Validation Accuracy:
   - Training Accuracy: 0.94 (94%)
   - Validation Accuracy: 0.51 (51%)
   - These are performance metrics that indicate how well the model is doing in terms of accuracy during training and on a separate validation dataset.

2. Task and Dataset:
   - The task is visual speech recognition, which involves recognizing speech by analyzing visual cues like lip movements.
   - The model is trained on a dataset called MIRACL.

3. Model Architecture:
   - The model architecture is VGG16 with two fully connected layers on top.
   - There is a Dropout layer with a dropout rate of 0.5 after the fully connected layers.
   - L2 regularization with values 0.1 and 0.5 has been applied to address over training.

4. Parameters:
   - Optimizer: Stochastic Gradient Descent (SGD)
     - Learning rate: 0.0005
     - Decay: 1e-6
     - Momentum: 0.9
   - These are hyper parameters that control how the model is trained.

5. Results:
   - Accuracy Chart: The results are shown over 80 epochs. The training accuracy reaches 93% by the end when using L2 regularization with a value of 0.1.
   - Validation accuracy peaks at 51% at epoch 21 with the same L2 regularization value of 0.1.
   - This suggests that the model is performing better on the validation set when regularization is applied.

6. Confusion Matrix:
   - A confusion matrix for lip reading has been generated to evaluate the model's performance. It's shown in an image, but the specific details are not provided in the text.

It's important to note that while the model achieves high training accuracy, the validation accuracy is considerably lower. This could be indicative of over fitting, especially given the use of dropout and L2 regularization to address it. Further tuning and analysis may be necessary to improve the model's performance on the validation set.
