import cirq

q = [cirq.GridQubit(0,i) for i in range(2)]

circuit = cirq.Circuit(
    cirq.H(q[0]),
    cirq.CNOT(q[0], q[1]),
    cirq.measure(q[0]),
    cirq.measure(q[1])
)

print(circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results: ")
print(result)