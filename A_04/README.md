# Assignment 04: Multilayer Perceptron Implementation

## Overview
This repository folder contains the implementation and evaluation of a **Multilayer Perceptron (MLP)** built from scratch using **NumPy**. 

The objective of this assignment is to design a multi-layer neural network architecture featuring custom matrix dot products, bias additions, and activation functions across sequential hidden and output layers.

## Network Architecture
* **Input Layer:** 3 neurons (accepts a 3-element feature vector $\mathbf{x}$)
* **Hidden Layer 1:** 5 neurons with **Sigmoid** activation
* **Hidden Layer 2:** 5 neurons with **Sigmoid** activation
* **Hidden Layer 3:** 2 neurons with **Sigmoid** activation
* **Output Layer (Layer 4):** 2 neurons with **ReLU** activation

## File Structure

```text
A_04/
├── multilayer_perceptron.py  # MultilayerPerceptron class with forward propagation logic
├── module4.py                # Python test script executing the MLP model
├── module4.ipynb             # Jupyter Notebook demonstrating interactive execution & outputs
└── README.md                 # Assignment documentation