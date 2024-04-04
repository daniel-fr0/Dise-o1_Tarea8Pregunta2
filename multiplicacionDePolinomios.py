from FFT import FFT, round_complex, evaluate
from cmath import exp, pi

def multiplicarFFT(a, b):
	# Multiplicacion de polinomios de grados n y m resulta en uno de grado n+m
	n = len(a) + len(b) - 1
	
	# Para el procedimiento hace falta que los grados sean potencia de 2
	m = 1
	while m < n:
		m *= 2

	# Se rellenan los polinomios con ceros para que tengan el mismo grado y potencia de 2
	a += [0] * (m - len(a))
	b += [0] * (m - len(b))

	# Se aplica la FFT a los polinomios y se multiplica punto a punto
	a = FFT(a)
	b = FFT(b)
	res = [a * b for a, b in zip(a, b)]

	# Para volver a la representacion de polinomios se utiliza la FFT inversa
	res = FFT(res, inverse=True)
	res = [round_complex(x) for x in res]
	return res

def multiplicar_ingenuo(a, b):
	n = len(a) + len(b) - 1
	res = [0] * n

	# rellenar con ceros para que tengan el mismo grado
	a += [0] * (n - len(a))
	b += [0] * (n - len(b))

	for i in range(n):
		res[i] = sum(a[j] * b[i-j] for j in range(i+1))
	
	return res

if __name__ == "__main__":
	print("Multiplicacion de polinomios")
	a = [1, 2, 3]
	b = [1, 2, 3]
	print(f"a = {a}")
	print(f"b = {b}")
	print(f"Multiplicacion ingenua: {multiplicar_ingenuo(a, b)}")
	print(f"Multiplicacion con FFT: {multiplicarFFT(a, b)}")

