import numpy as np
from multilayer_perceptron import MultilayerPerceptron

def run_tests():
    print("================ MULTILAYER PERCEPTRON TEST ================")
    
    # Instantiate model
    mlp = MultilayerPerceptron()
    
    # Example input vector with 3 features
    x = np.array([0.5, -1.2, 0.8])
    print(f"Input vector x: {x}")
    
    # Execute forward propagation
    results = mlp.forward(x)
    
    # Print outputs for each layer clearly for grading
    print("\n--- Forward Propagation Results ---")
    print("Hidden Layer 1 Output (5 neurons, Sigmoid):", np.round(results["hidden_1"], 4))
    print("Hidden Layer 2 Output (5 neurons, Sigmoid):", np.round(results["hidden_2"], 4))
    print("Hidden Layer 3 Output (2 neurons, Sigmoid):", np.round(results["hidden_3"], 4))
    print("Output Layer 4 Output (2 neurons, ReLU)   :", np.round(results["output_layer_4"], 4))

if __name__ == "__main__":
    run_tests()