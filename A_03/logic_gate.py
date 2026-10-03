import numpy as np

class LogicGate:
    def __init__(self):
        self.w1 = None
        self.w2 = None
        self.th = None
        self.out = None
        self.x1 = None
        self.x2 = None

    def print_output(self, gate):
        if gate == "AND":
            print(f"Output of AND logic is: {self.out}, with x1 = {self.x1}, x2 = {self.x2}")
        elif gate == "NAND":
            print(f"Output of NAND logic is: {self.out}, with x1 = {self.x1}, x2 = {self.x2}")
        elif gate == "OR":
            print(f"Output of OR logic is: {self.out}, with x1 = {self.x1}, x2 = {self.x2}")
        elif gate == "NOR":
            print(f"Output of NOR logic is: {self.out}, with x1 = {self.x1}, x2 = {self.x2}")
        elif gate == "XOR":
            print(f"Output of XOR logic is: {self.out}, with x1 = {self.x1}, x2 = {self.x2}")

    def and_gate(self, x1, x2):
        self.w1 = 0.5
        self.w2 = 0.5
        self.th = 0.99
        self.x1 = x1
        self.x2 = x2
        
        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])
        
        if np.dot(x, w) > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0

    def nand_gate(self, x1, x2):
        self.w1 = -0.5
        self.w2 = -0.5
        self.th = -0.7
        self.x1 = x1
        self.x2 = x2
        
        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])
        
        if np.dot(x, w) > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0

    def or_gate(self, x1, x2):
        self.w1 = 0.5
        self.w2 = 0.5
        self.th = 0.0
        self.x1 = x1
        self.x2 = x2
        
        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])
        
        if np.dot(x, w) > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0

    def nor_gate(self, x1, x2):
        self.w1 = -0.5
        self.w2 = -0.5
        self.th = -0.1
        self.x1 = x1
        self.x2 = x2
        
        x = np.array([x1, x2])
        w = np.array([self.w1, self.w2])
        
        if np.dot(x, w) > self.th:
            self.out = 1
            return 1
        else:
            self.out = 0
            return 0

    def xor_gate(self, x1, x2):        
        s1 = self.nand_gate(x1, x2)
        s2 = self.or_gate(x1, x2)
        out = self.and_gate(s1, s2)

        self.x1 = x1
        self.x2 = x2
        self.out = out
        return out


if __name__ == "__main__":
    gate = LogicGate()
    
    print("--- Testing Logic Gates directly in logic_gate.py ---")
    gate.and_gate(1, 1)
    gate.print_output("AND")
    
    gate.nand_gate(1, 1)
    gate.print_output("NAND")
    
    gate.or_gate(1, 0)
    gate.print_output("OR")
    
    gate.nor_gate(0, 0)
    gate.print_output("NOR")
    
    gate.xor_gate(1, 0)
    gate.print_output("XOR")