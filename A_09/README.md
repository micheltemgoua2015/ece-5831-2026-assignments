# ECE 5831 – Assignment 09: Data Augmentation, Transfer Learning, and Text Processing

**Author:** Michel Ludovic Temgoua  
**Course:** ECE 5831 – Pattern Recognition and Neural Networks (Fall 2026)  

---

## Overview
This assignment explores two core deep learning workflows using TensorFlow/Keras:
1. **Part 1 (`Module_9_1.ipynb`):** Combating overfitting on a limited image dataset (`cat` vs. `dog`) using online **Data Augmentation** and **Transfer Learning** (pretrained convolutional backbone), benchmarked directly against a CNN trained from scratch on the exact same limited dataset.
2. **Part 2 (`Module_9_2.ipynb`):** Building a custom **`TextProcess`** pipeline to tokenize, encode text into numerical integer sequences, and decode sequences back into human-readable text.

---

## Folder Structure
```text
A_09/
├── Module_9_1.ipynb      # Part 1: DataAug, CatsDogsLimit, CatsDogsPre, and Model Comparison
├── Module_9_2.ipynb      # Part 2: TextProcess encoding, decoding, and round-trip verification
├── README.md             # Assignment documentation and key results summary
└── .gitignore            # Excludes local image folders (dataset/, dataset_limit/)