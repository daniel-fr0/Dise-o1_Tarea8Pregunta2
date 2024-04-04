# La Criba de Eratóstenes se puede usar para ver si un número es primo. ¿Se podrá
# modificar para calcular algo más?

# este algoritmo es una optimizacion de la criba de eratostenes que permite
# obtener todos los numeros primos menores o iguales a N en O(N)
# extraido de: https://cp-algorithms-es.github.io/algebra/primos/criba-de-eratostenes-lineal.html
def primos(N):
	lp = [0] * (N+1)
	pr = []

	for i in range(2, N+1):
		if lp[i] == 0:
			lp[i] = i
			pr.append(i)
		j = 0
		while j < len(pr) and pr[j] <= lp[i] and i * pr[j] <= N:
			lp[i * pr[j]] = pr[j]
			j += 1

	return pr

print(primos(200))