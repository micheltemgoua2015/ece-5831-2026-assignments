# Assignment 07: Neural Network with Backpropagation

## Overview
This directory contains the implementation of **Assignment 07** for **ECE 5831**. The assignment focuses on building, training, and evaluating a 2-layer Neural Network (`TwoLayerNetBackprop`) from scratch using analytical **Backpropagation** on the MNIST handwritten digit classification benchmark.

## Dataset
- **MNIST Handwritten Digits**: $28 \times 28$ grayscale images loaded directly via Keras (`tensorflow.keras.datasets.mnist`).
- **Training Set**: 60,000 samples.
- **Test Set**: 10,000 samples.

## File Structure

A_07/
├── module7.ipynb      # Main Assignment Jupyter Notebook
└── README.md          # Assignment Documentation

## Network Architecture
- **Input Layer**: 784 neurons ($28 \times 28$ flattened normalized pixels).
- **Hidden Layer**: 100 neurons with ReLU activation.
- **Output Layer**: 10 neurons with Softmax activation.
- **Loss Function**: Categorical Cross-Entropy Loss.
- **Optimization Algorithm**: Stochastic Mini-batch Gradient Descent via Analytical Backpropagation.

## Results
- **Training Epochs**: 10
- **Batch Size**: 64
- **Learning Rate**: 0.1
- **Final Test Accuracy**: ~97%+