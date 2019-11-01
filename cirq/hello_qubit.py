import cirq

# pick a qubit
qubit = cirq.GridQubit(0,0)

# create a circuit
circuit = cirq.Circuit(
    cirq.X(qubit)**0.5, # square root of X
    cirq.measure(qubit, key='m') # measurement
)
print("Circuit: ")
print(circuit)

# simulate the circuit several times
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results: ")
print(result)