# Implimentation of RSA Encryption

# TODO impliment Rabin Miller Primality test for finding large primes
# Arbitrarily decided prime numbers. 
p = 101 
q = 137
e = 7

msg = int(input("enter message (integer) to be encrypted : "))

# Euclid's extended division algorithm
x, y = 0, 1
def gcdExtended(a, b):
	global x, y
	if (a == 0): #Base Case
		x = 0
		y = 1
		return b
	gcd = gcdExtended(b%a, a) #recursive call
	temp1, temp2 = x, y
	x = temp2 - (b // a) * temp1
	y = temp1
	return gcd

# Multiplicative inverse for e modulo psy(n)
def mod_inverse(e, psy):
	g = gcdExtended(e, psy)
	res = (x % psy + psy) % psy
	return res

# Encryption function
def encrypt(msg, public_key):
    a = (msg ** public_key[0])
    b = a % public_key[1]
    return b

# Decryption Function
def decrypt(msg, secret_key):
    a = (msg ** secret_key[0])
    b = a % secret_key[1]
    return b

# Calculating public and secret keys
n = p*q
psy = (p-1)*(q-1) 
d = mod_inverse(e,psy)

public_key = [e, n]
secret_key = [d, n]

print("encrypted : ", encrypt(msg, public_key))
print("decrypted : ", decrypt(encrypt(msg, public_key), secret_key) )