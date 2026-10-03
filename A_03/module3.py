import logic_gate as lg

def run_tests():
    gate = lg.LogicGate()
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    
    print("================ AND GATE TEST ================")
    for x1, x2 in inputs:
        gate.and_gate(x1, x2)
        gate.print_output("AND")

    print("\n================ NAND GATE TEST ================")
    for x1, x2 in inputs:
        gate.nand_gate(x1, x2)
        gate.print_output("NAND")

    print("\n================ OR GATE TEST ================")
    for x1, x2 in inputs:
        gate.or_gate(x1, x2)
        gate.print_output("OR")

    print("\n================ NOR GATE TEST ================")
    for x1, x2 in inputs:
        gate.nor_gate(x1, x2)
        gate.print_output("NOR")

    print("\n================ XOR GATE TEST ================")
    for x1, x2 in inputs:
        gate.xor_gate(x1, x2)
        gate.print_output("XOR")

if __name__ == "__main__":
    run_tests()