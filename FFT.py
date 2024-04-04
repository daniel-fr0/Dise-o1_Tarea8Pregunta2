from cmath import exp, pi

def FFT(a, w):
	if w == 1:
		return a
	n = len(a)
	par = FFT(a[0::2], round_complex(w*w))
	impar = FFT(a[1::2], round_complex(w*w))
	res = [0]*n

	x = 1
	for i in range(n//2):
		res[i] = par[i] + x*impar[i]
		res[i+n//2] = par[i] - x*impar[i]
		x *= w
		res[i] = round_complex(res[i])
		res[i+n//2] = round_complex(res[i+n//2])

	return res

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
	pts = FFT(p, w)
	for x in pts:
		print(x)

	print()
	print("P = ")
	for i in range(len(p)):
		x = round_complex(w**i)
		y = round_complex(evaluate(p, w**i))
		print(f"{x:>16}\t---->\t{y:<}")