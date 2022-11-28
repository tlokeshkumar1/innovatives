import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# create the x and y input and outputs
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# create the weight vector as a tensor
w = torch.tensor([[1.0]], requires_grad=True)

# run a learning loop and fir the regressor with SGD
learning_rate = 0.01

optimizer = optim.SGD ([w], lr=learning_rate)

# Create the loss function
loss_fn = nn.MSELoss (reduction="sum")

# Create the training loop
for iteration in range(1000):
    # 1. Clear the gradients
    optimizer.zero_grad()
    # 2. Make a prediction
    y_pred = x.mm(w)
    #3. Calculate the loss
    loss = loss_fn(y_pred, y)
    #4. Compute the gradients
    loss.backward()
    # 5. Update the parameters
    optimizer.step()
# Print the results
print(f'Prediction: (y_pred)')
print(f'Loss: {loss}')
print(f'Weights: {w}')