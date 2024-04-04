from cmath import exp, pi
from math import sin,cos,pi

# FFT extraido de
# https://www.geeksforgeeks.org/fast-fourier-transformation-poynomial-multiplication/
def FFT(a, inverse=False):

	n = len(a)

	# if input contains just one element
	if n == 1:
		return [a[0]]

	# For storing n complex nth roots of unity
	theta = -2*pi/n

	# Inversa de la FFT, para obtener los coeficientes de los polinomios hay que
	# rotar en sentido contrario
	if inverse:
		theta *= -1

	w = list( complex(cos(theta*i), sin(theta*i)) for i in range(n) ) 
	
	# Separe coefficients
	Aeven = a[0::2]
	Aodd = a[1::2]

	# Recursive call for even indexed coefficients
	Yeven = FFT(Aeven) 

	# Recursive call for odd indexed coefficients
	Yodd = FFT(Aodd)

	# for storing values of y0, y1, y2, ..., yn-1.
	Y = [0]*n
	
	middle = n//2
	for k in range(n//2):
		w_yodd_k = w[k] * Yodd[k]
		yeven_k = Yeven[k]
		
		Y[k]		 = round_complex(yeven_k + w_yodd_k)
		Y[k + middle] = round_complex(yeven_k - w_yodd_k)
	
	if inverse:
		Y = [y / n for y in Y]
	return Y

def round_complex(c, precision=4):
	real = round(c.real, precision)
	imag = round(c.imag, precision) * 1j

	if real == int(real):
		real = int(real)

	if imag == 0:
		return real
	return real + imag

def evaluate(p, x):
	res = p[-1]
	for i in range(len(p)-2, -1, -1):
		res = res * x + p[i]
	return res


if __name__ == "__main__":
	p = [1, 6, 1, 0, 3, 7, 1, 0]
	w = exp(2j * pi / 8)

	print("FFT = ")
	pts = FFT(p)
	for x in pts:
		print(x)

	print()
	print("P = ")
	for i in range(len(p)):
		theta = -2*pi/8
		w = complex(cos(theta*i), sin(theta*i))
		x = round_complex(w)
		y = round_complex(evaluate(p, w))
		print(f"{x:>16}\t---->\t{y:<}")
		assert pts[i] == y