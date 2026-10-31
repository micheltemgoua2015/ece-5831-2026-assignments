# Assignment 06: TwoLayerNet Training using Numerical Gradients

## Overview
This folder contains the complete implementation for **Assignment 06**, focusing on building, training, and evaluating a 2-layer Neural Network (`TwoLayerNet`) trained from scratch using numerical gradients (central difference formula) across two benchmarks:
1. **Part 1: Iris Dataset** — Multi-class classification of Iris plant species based on 4 morphological features.
2. **Part 2: MNIST Handwritten Digit Dataset** — Digit recognition ($28 \times 28$ grayscale images) trained via mini-batch stochastic numerical gradient updates.

---

## File Structure
```text
A_06/
├── module6.ipynb                   # Main assignment notebook (Part 1: Iris, Part 2: MNIST)
├── README.md                       # Assignment documentation
├── iris.csv                        # Iris dataset (150 samples, 4 features, 3 classes)
├── mnist/                          # MNIST gzip dataset directory
│   ├── train-images-idx3-ubyte.gz
│   ├── train-labels-idx1-ubyte.gz
│   ├── t10k-images-idx3-ubyte.gz
│   └── t10k-labels-idx1-ubyte.gz
├── temgoua_iris_nn_model.pkl       # Saved trained weights dictionary for Iris model
└── temgoua_mnist_nn_model.pkl      # Saved trained weights dictionary for MNIST model