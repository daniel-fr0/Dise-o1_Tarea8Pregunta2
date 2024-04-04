# la idea es tener un polinomio con las potencias desde 1 hasta N-1
# y multiplicarlo por si mismo

# cada coeficiente consistiria en la cantidad de formas de descomponer
# el sumando (indicado por el grado del coeficiente) en dos factores,
# esto es igual a la cantidad de factores que tiene el sumando

# al multiplicar dos coeficientes, el grado del coeficiente resultante indica
# el X = grado1 + grado2, es decir, el numero que se obtiene al sumar los sumandos
# y el coeficiente indica entonces la cantidad de formas de descomponer X de la
# forma X = ab + cd, donde a y b son factores del primer sumando y c y d son factores
# del segundo sumando

from multiplicacionDePolinomios import multiplicarFFT, multiplicar_ingenuo
from eratostenes import factores

# utiliza la criba de Eratostenes optimizada para obtener los factores de los numeros
# y luego multiplica los polinomios de factores utilizando FFT
# finalmente busca el maximo coeficiente entre 1 y N
# el peso mayor de este algoritmo es la multiplicacion de polinomios, que es O(N log N)
# por lo que el algoritmo es O(N log N)
def respuesta(N):
	# Obtengo la cantidad de factores para cada numero entre 1 y N-1
	# esto utiliza la criba de Eratostenes optimizada y tiene un costo de O(N log N)
	p = factores(N-1)

	# se incluye el 0 para que haya un coeficiente para el grado 0
	p = [0] + p

	# Multiplico los polinomios de factores, utilizando FFT esto tomaria O(N log N)
	q = multiplicarFFT(p, p) # tiene problemas con los resultados al ser numeros complejos

	# La cantidad de formas de descomponer un Y en dos sumandos es el coeficiente de x^Y
	# si se quiere obtener el maximo, se busca el indice el mayor coeficiente entre 1 y N
	maximo = 0
	indice = -1
	for i in range(N, 0, -1):	# O(N)
		if q[i] > maximo:
			maximo = q[i]
			indice = i
	return maximo, indice




print(respuesta(5)) # 14 para el numero 5
print(respuesta(12)) # 80 para el numero 12
print(respuesta(100)) # 2488 para el numero 96
print(respuesta(1000)) # 64200 para el numero 960