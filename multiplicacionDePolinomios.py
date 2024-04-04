from FFT import FFT, round_complex, evaluate
from cmath import exp, pi

def multiplicar(p, q):
	# Multiplicacion de polinomios de grados n y m resulta en uno de grado n+m
	n = len(p) + len(q) - 1
	
	# Para el procedimiento hace falta que los grados sean potencia de 2
	m = 1
	while m < n:
		m *= 2
	w = round_complex(exp(2j * pi / m))

	# Se rellenan los polinomios con ceros para que tengan el mismo grado y potencia de 2
	p += [0] * (m - len(p))
	q += [0] * (m - len(q))

	# Se aplica la FFT a los polinomios y se multiplica punto a punto
	p = FFT(p, w)
	q = FFT(q, w)
	res = [a * b for a, b in zip(p, q)]

	# Para volver a la representacion de polinomios se obtiene la inversa de la
	# DFT, evaluando la matriz con w^-1 y dividiendola por m
	res = FFT(res, round_complex(1/w))

	# Se divide cada valor por m para equivaler la division a la matriz de DFT
	return [round_complex(r/m) for r in res]