# BB84-QKD-Protocol Simulation

# What is QKD?

Quantum key Distribution refers to the process of generating and distributing private keys for cryptography between two parties over an unsecure public channel. This process of distribution is provably secure from principles of quantum mechanics. The basic idea is as follows : a party cannot gain information from the transmission of the qubits without disturbing their state. A qubit also cannot be cloned as a result of the no cloning theorem.  


# BB84 (Bennett and Brassard 1984)  Protocol

1. Alice generates two random bit strings of (4 + ∆)n bits, one for the key, d, and the other for the basis,b.
2. Alice picks the |0〉|1〉basis or the |+〉 | -〉depending on the corresponding bit in b being 0 or 1.
3. Alice sends |0〉(|+〉) or |1〉( | -〉) if the bit in d is 0 or 1 respectively.
4. She sends this qubit to Bob over a quantum channel.
5. Bob prepares a random bit string of (4 + ∆)n bits,b' and measures each successive qubit in |0〉|1〉or  |+〉 | -〉basis if it is 0 or 1 respectively, and obtains a bitstring d'.
6. Alice and Bob publicly announce their choices of basis b and b'.
7. Both discard the bits in d and d' for which b ≠ b'. They should approximately have 2n bits.
8. They should have the same bitstrings remaining since Bob measures in the basis that Alice sends. They will also have some errors due to noise.
9. Alice and Bob pick a sequence of n bits from the message, communicate it publicly over the classical channel, and calculate the error rate. If it is large, they abort the protocol.
10. If the error is below a certain threshold, they perform information reconciliation and privacy amplification in the remaining n bits to obtain the shared key.
