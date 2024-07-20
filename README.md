# Encryption Protocols

Cryptography is the practice and study of techniques for secure communication in the presence of adversarial behaviour. More specifically it is the process of obfuscating and deobfuscating data using certain cryptographic techniques. 

This project simulates three encryption protocols
1. Vigenere Ciphers
2. RSA Encryption
3. QKD Protocol (BB84)


# Vigenere Cipher

The Vigenère cipher is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key. The Vigenère cipher is therefore a special case of a polyalphabetic substitution. 

For example, if the plaintext is attacking tonight and the key is OCULORHINOLARINGOLOGY, then
1. The first letter a of the plaintext is shifted by 14 positions in the alphabet (because the first letter O of the key is the 14th letter of the alphabet, counting from zero), yielding o;
2. The second letter t is shifted by 2 (because the second letter C of the key means 2) yielding v;
3. The third letter t is shifted by 20 (U) yielding n, with wrap-around;
4. Yielding the message ovnlqbpvt hznzouz. If the recipient of the message knows the key, they can recover the plaintext by reversing this process.


# RSA Encryption

In 1977 Ron Rivest, Adi Shamir and Leonard Adleman developed RSA encryption. An asymmetric key distribution system, where everyone has access to what is known as a “public key” and can use it to encrypt messages. But only the party to whom the message is destined has access to the “private key” to decrypt messages. 

1. The first step in RSA encryption is to select two large primes, p and q. This is usually done by just generating a random number then performing the Rabin-Miller primality test. Typically the primes selected are 1024 to 2048 bits long. 
2. We then compute the product of these two primes, denoted by n.  
3. We also compute the Euler Totient function (n) = (p-1)(q-1)
4. We then select a random small off integer that is co-prime to (n) 
5. Finally we compute d, the multiplicative inverse of e modulo (n)
6. Our RSA public key is P = (e,n) and our secret key is S = (d,n)


# QKD

Quantum key Distribution refers to the process of generating and distributing private keys for cryptography between two parties over an unsecure public channel. This process of distribution is provably secure from principles of quantum mechanics. The basic idea is as follows : a party cannot gain information from the transmission of the qubits without disturbing their state. A qubit also cannot be cloned as a result of the no cloning theorem.  

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
