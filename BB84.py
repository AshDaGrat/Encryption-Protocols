import numpy as np
from qiskit.providers.aer import QasmSimulator
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute


length = 32 #length of Qubits sent. Typically 4n , where n is the length of the key


# Create a Quantum Circuit acting on a quantum register of 4n qubits
qreg = QuantumRegister(length, "qreg")
creg = ClassicalRegister(length, "creg")
circ = QuantumCircuit(qreg, creg)



# Alice's part
Alice = np.random.choice([0,1], size=(2, length)) #Generate two random bitstrings, for Alice's data and choice of bases


#flipping all necessary data bits to 1 since qiskit initialises qubits to 0
count = 0
for i in Alice[0]:
  if i:
    circ.x(count)
  count += 1


# Applying hadamard to necessary bits to change basis
count = 0
for i in Alice[1]:
  if i:
    circ.h(count)
  count += 1



# Bob's part
Bob_basis = np.random.choice([0,1], size=( length))


#Applying Hadamard gate to bits where Bob wants to measure in the|+>|> basis
count = 0
for i in Bob_basis:
  if i:
    circ.h(count)
  count += 1


#Bob measuring the qubits
circ.measure(qreg, creg)


#Running the quantum simulation
key = execute(circ.reverse_bits(),backend=QasmSimulator(),shots=1).result().get_counts().most_frequent()



#Postprocessing step where Alice and Bob discard the bits which they measured in the opposite basis
encryption_key = ''
for i in range(length):
    if Alice[1][i] == Bob_basis[i]:
         encryption_key += str(key[i])

        
            
#Printing everything
print(f"Alice's Bases:\t {np.array2string(Alice[1])}")
print(f"Bob's Bases:\t {np.array2string(Bob_basis)}")
print(f"Alice's State:\t {np.array2string(Alice[0])}")
print(key)
print(f"Key: {encryption_key}")