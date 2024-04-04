# La Criba de Eratóstenes se puede usar para ver si un número es primo. ¿Se podrá
# modificar para calcular algo más?
def eratostenes(n):
	primes = [i for i in range(2, n + 1)]
	i = 0
	while i < len(primes):
		p = primes[i]

		j = i + 1
		while j < len(primes):
			if primes[j] % p == 0:
				del primes[j]
			else:
				j += 1

		i += 1
	
	return primes

print(eratostenes(200))