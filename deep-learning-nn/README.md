# Deep Neural Networks

## DNN for regression

Combining a data reduction techniques with non-linear regression to hopefully further decrease computational time of the numerical simulations of reacting flows.

## Plotting NN performance data

Once you have the model fitted:

```python
history = model.fit(...)
```

You can plot the performance of the network:

```python
# Plot training and validation accuracy values
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Plot training and validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
```
