# Signal-Based Fault Classification Using a Custom NumPy Neural Network and 1D-CNN Benchmark

**Course:** ECE 5831 – Pattern Recognition and Neural Networks  
**Institution:** University of Michigan–Dearborn  
**Team Members:** Michel Ludovic Temgoua, Suraj Datta, Venkat Ramisetty  

---

## Overview

Accurate fault diagnosis and condition monitoring from high-frequency sensor signals (such as motor phase currents and accelerometer vibrations) are essential for predictive maintenance in industrial and automotive systems. This project implements an end-to-end machine learning pipeline evaluated on the **Paderborn University Bearing Dataset**.

The repository compares two distinct neural network paradigms:
1. **Custom 3-Layer Multi-Layer Perceptron (MLP) from Scratch (`NumPy`):** Built without deep learning frameworks, implementing analytical forward propagation, He weight initialization, ReLU/Softmax activations, categorical cross-entropy loss, and mini-batch gradient descent backpropagation.
2. **1D Convolutional Neural Network Benchmark (`TensorFlow/Keras`):** A modern deep learning architecture designed to extract local spectral harmonics directly from 1D frequency-domain signals, evaluated against the custom NumPy engine for classification accuracy, F1-score, convergence speed, and parameter efficiency.

---

## Dataset & Preprocessing Pipeline

### **Paderborn University Bearing Dataset**
* **Sampling Frequency:** $64\text{ kHz}$ ($4\text{-second}$ recordings $\approx 256,000\text{ samples}$ per measurement).
* **Operating Conditions:** Evaluated across varying rotational speeds ($900\text{–}1,500\text{ rpm}$), load torques ($0.1\text{–}0.7\text{ Nm}$), and radial forces ($400\text{–}1,000\text{ N}$).
* **Fault Classes Evaluated:**
  * **Class `0` – Healthy (`K0`):** Undamaged baseline reference bearings (`K001`).
  * **Class `1` – Outer-Race Damage (`KA`):** Bearings with outer-ring defects (`KA01`).
  * **Class `2` – Inner-Race Damage (`KI`):** Bearings with inner-ring defects (`KI01`).

### **Signal Processing & Augmentation Steps**
1. **Sliding-Window Segmentation:** Continuous $64\text{ kHz}$ vibration signals are partitioned into non-overlapping frames of **$4,096\text{ samples}$** ($\approx 64\text{ ms}$ per window).
2. **Fast Fourier Transform (FFT):** Each $4,096$-sample time window is transformed into the frequency domain via real FFT (`np.fft.rfft`), retaining the first **$2,048\text{ positive frequency magnitude bins}$** to isolate periodic fault harmonics.
3. **Min-Max Normalization:** Scales every frequency spectrum vector cleanly into $[0.0, 1.0]$ to stabilize gradient descent convergence.
4. **Gaussian Noise Augmentation:** Injects synthetic Gaussian noise ($\sigma = 0.02$) into the training set to simulate real-world sensor noise and improve generalization.
5. **Tensor Formatting:**
   * **Custom NumPy MLP:** $2\text{D}$ feature matrix of shape `(N, 2048)` paired with One-Hot Encoded targets `(N, 3)`.
   * **Keras 1D-CNN:** $3\text{D}$ sequential tensor of shape `(N, 2048, 1)` paired with integer class labels `(N,)`.

---

## Model Architectures & Evaluation Methodology

### **1. Custom 3-Layer NumPy MLP**
* **Architecture:** `Input (2048)` $\rightarrow$ `Dense (256, ReLU)` $\rightarrow$ `Dense (128, ReLU)` $\rightarrow$ `Output (3, Softmax)`
* **Initialization & Optimization:** Uses **He Initialization** ($\sqrt{2 / n_{\text{in}}}$) to prevent vanishing gradients across layers and trains via mini-batch gradient descent (`batch_size = 64`, `lr = 0.05`).

### **2. Keras 1D-CNN Benchmark**
* **Architecture:** Three progressive `Conv1D` blocks (`32`, `64`, and `128` filters with kernel sizes `7`, `5`, and `3`), `BatchNormalization`, `MaxPooling1D`, `GlobalAveragePooling1D`, `Dense (64, ReLU)`, `Dropout (0.2)`, and `Dense (3, Softmax)`.
* **Advantage:** Captures local spectral patterns across adjacent frequency bins while reducing trainable parameters by ~90% compared to a fully connected dense architecture.

### **Evaluation Metrics**
* **Categorical Cross-Entropy Loss:** Measures probabilistic calibration of the Softmax output distribution.
* **Classification Accuracy & Macro F1-Score:** Ensures balanced precision and recall across both healthy and damaged bearing classes.
* **Confusion Matrices & Convergence Curves:** Visualizes class-level misclassification rates alongside training speed and parameter efficiency.

---

## Repository Structure

```text
Project_Bearing_Fault_Classification/
├── bearing_fault_classification.ipynb   # Main end-to-end Jupyter Notebook pipeline
├── README.md                            # Project documentation and setup guide
├── .gitignore                           # Excludes large raw .mat and .rar dataset files
└── raw_data/                            # Local directory for Paderborn .mat files (ignored by Git)
    ├── K001/                            # Healthy bearing recordings
    ├── KA01/                            # Outer-race fault recordings
    └── KI01/                            # Inner-race fault recordings
```

---

## How to Run Locally

1. **Activate the Conda Environment:**
   ```powershell
   conda activate ece-5831-2026
   ```
2. **Prepare Dataset:** Download the `.rar` archives (`K001.rar`, `KA01.rar`, `KI01.rar`) from the Paderborn University Bearing DataCenter and extract them into `raw_data/`.
3. **Execute Notebook:** Open `bearing_fault_classification.ipynb` in VS Code, select the `ece-5831-2026` kernel, and click **Run All**.