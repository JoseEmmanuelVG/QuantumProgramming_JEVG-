from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

# Creación de registros
q = QuantumRegister(1, 'q_reg')
c = ClassicalRegister(1, 'c_reg')

# Creación del circuito
qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.measure(q[0], c[0])

# Dibujando el circuito
fig = qc.draw(output='mpl')
fig.show()

