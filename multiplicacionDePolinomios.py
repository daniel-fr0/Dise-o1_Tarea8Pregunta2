from FFT import FFT, round_complex
from cmath import exp, pi

def multiplicarFFT(a, b):
	# Multiplicacion de polinomios de grados n y m resulta en uno de grado n+m
	n = len(a) + len(b) - 1
	
	# Para el procedimiento hace falta que los grados sean potencia de 2
	m = 1
	while m < n:
		m *= 2
	w = exp(2j * pi / m)

	# Se rellenan los polinomios con ceros para que tengan el mismo grado y potencia de 2
	a += [0] * (m - len(a))
	b += [0] * (m - len(b))

	# Se aplica la FFT a los polinomios y se multiplica punto a punto
	a = FFT(a, w)
	b = FFT(b, w)
	res = [a * b for a, b in zip(a, b)]

	# Para volver a la representacion de polinomios se utiliza la FFT inversa
	res = FFT(res, 1/w, inverse=True)
	return [round_complex(x, 0) for x in res]

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
	a = [1, 2, 3, 4, 5, 6, 7]
	b = [1, 2, 3, 4, 5, 6, 7]
	print(f"a = {a}")
	print(f"b = {b}")
	abIngenuo = multiplicar_ingenuo(a.copy(), b.copy())
	abFFT = multiplicarFFT(a.copy(), b.copy())
	print(f"Multiplicacion ingenua: {abIngenuo}")
	print(f"Multiplicacion con FFT: {abFFT}")

	for i in range(len(abIngenuo)):
		assert abIngenuo[i] == abFFT[i]

