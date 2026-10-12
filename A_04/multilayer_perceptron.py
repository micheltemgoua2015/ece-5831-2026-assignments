import numpy as np

class MultilayerPerceptron:
    def __init__(self):
        # Initialize network weights and biases based on the specified architecture:
        # Input (3) -> Hidden 1 (5) -> Hidden 2 (5) -> Hidden 3 (2) -> Output Layer 4 (2)
        self.network = {}
        
        # Set random seed for reproducibility
        np.random.seed(42)
        
        # Layer 1: Weights (3, 5), Biases (5,)
        self.network["W1"] = np.random.randn(3, 5)
        self.network["b1"] = np.zeros(5)
        
        # Layer 2: Weights (5, 5), Biases (5,)
        self.network["W2"] = np.random.randn(5, 5)
        self.network["b2"] = np.zeros(5)
        
        # Layer 3: Weights (5, 2), Biases (2,)
        self.network["W3"] = np.random.randn(5, 2)
        self.network["b3"] = np.zeros(2)
        
        # Output Layer (Layer 4): Weights (2, 2), Biases (2,)
        self.network["W4"] = np.random.randn(2, 2)
        self.network["b4"] = np.zeros(2)

    def sigmoid(self, s):
        """Sigmoid activation function for Hidden Layers 1, 2, and 3."""
        return 1 / (1 + np.exp(-s))

    def relu(self, s):
        """ReLU activation function for Output Layer 4."""
        return np.maximum(0, s)

    def forward(self, x):
        """Performs forward propagation from the input layer to the output layer."""
        # Hidden Layer 1 (5 neurons, Sigmoid)
        a1 = x @ self.network["W1"] + self.network["b1"]
        z1 = self.sigmoid(a1)

        # Hidden Layer 2 (5 neurons, Sigmoid)
        a2 = z1 @ self.network["W2"] + self.network["b2"]
        z2 = self.sigmoid(a2)

        # Hidden Layer 3 (2 neurons, Sigmoid)
        a3 = z2 @ self.network["W3"] + self.network["b3"]
        z3 = self.sigmoid(a3)

        # Output Layer 4 (2 neurons, ReLU)
        a4 = z3 @ self.network["W4"] + self.network["b4"]
        output = self.relu(a4)

        return {
            "hidden_1": z1,
            "hidden_2": z2,
            "hidden_3": z3,
            "output_layer_4": output
        }