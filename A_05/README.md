# Assignment 05: Forward Propagation Implementation

## Overview
This folder contains solutions for **Assignment 05**, covering forward propagation and model inference across two classification tasks:
1. **Rock–Paper–Scissors Classification** using a custom-trained Keras model exported from Google Teachable Machine.
2. **Custom Handwritten MNIST Digit Verification** evaluating a 3-layer neural network using personal handwritten digit images ($28 \times 28$ grayscale).

## File Structure
```text
A_05/
├── keras_model.h5            # Trained Teachable Machine model
├── labels.txt                # Class labels for Rock, Paper, Scissors
├── rock-paper-scissors.ipynb # Problem 1 notebook with Keras inference
├── rock.png                  # Test image for Rock gesture
├── paper.png                 # Test image for Paper gesture
├── scissor.png               # Test image for Scissors gesture
├── mnist.ipynb               # Problem 2 notebook with MNIST inference engine
├── mnist/                    # MNIST dataset & pre-trained weights
│   ├── sample_weight.pkl     # Neural network weights dictionary
│   ├── t10k-images-idx3-ubyte.gz
│   ├── t10k-labels-idx1-ubyte.gz
│   ├── train-images-idx3-ubyte.gz
│   └── train-labels-idx1-ubyte.gz
└── mnist_digits/             # Custom handwritten digit images (0_1.png to 9_5.png)
    ├── 0_1.png
    ├── 0_2.png
    ├── ...
    └── 9_5.png
└── README.md                 # Assignment documentation