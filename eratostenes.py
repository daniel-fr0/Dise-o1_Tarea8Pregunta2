# La Criba de Eratóstenes se puede usar para ver si un número es primo. ¿Se podrá
# modificar para calcular algo más?

# este algoritmo es una optimizacion de la criba de eratostenes que permite
# obtener todos los numeros primos menores o iguales a N en O(N)
# extraido de: https://cp-algorithms-es.github.io/algebra/primos/criba-de-eratostenes-lineal.html
# alli se explica que la version original de la criba de eratostenes tiene una complejidad de O(N log log N)
# y que esta version es una optimizacion que permite obtener los primos en O(N)
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


# esta modificacion puede calcular la cantidad de factores primos de cada numero entre 1 y N
# en O(N log N)
def factores(N):		
	lp = [0] * (N+1)
	pr = []

	def count_factors(x):
		# contar los factores supone un costo de O(log x), porque
  		# se divide x por el menor factor primo de x y se repite
		# hasta que x sea 1
		# por lo tanto el costo total es O(log 2) + O(log 3) + ... + O(log N)
		factor = lp[x]
		exponente = 0

		count = 0
		while x > 1:
			x //= lp[x]
			exponente += 1
			if factor != lp[x]:
				count += exponente + 1
				factor = lp[x]
				exponente = 0
		return count
	
	res = [1] * (N+1)

	for i in range(2, N+1):
		if lp[i] == 0:
			lp[i] = i
			pr.append(i)
		j = 0
		while j < len(pr) and pr[j] <= lp[i] and i * pr[j] <= N:
			lp[i * pr[j]] = pr[j]
			j += 1
		
		# se le agrega esto al algoritmo, lo que agregaria un costo de O(log N)
		res[i] = count_factors(i)

	return res[1:]
print(primos(200))