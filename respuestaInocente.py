# primero se obtienen todas las formas de descomponer N en dos sumandos
# a,b tal que a+b=N

# los numeros del 1 al N//2 cada uno suma con su complemento a N
# i + (N-i) = N
def sumandos(n):
	return [(i, n-i) for i in range(1, n)]

# luego se obtienen los divisores de a y b y se unen a las formas de
# descomponer a los sumandos de N
def divisores(n):
	return [(i, n//i) for i in range(1, n+1) if n % i == 0]

# revisar todas las formas de descomponer N en dos sumandos y para cada
# una revisar todos los divisores de cada sumando
# para cada divisor de a y b se obtiene una respuesta
# esta seria la forma inocente de resolver el problema y tomaria O(N^3)
def decompSecuencias(n):
	return [(a, b, c, d) for p,q in sumandos(n) for a,b in divisores(p) for c,d in divisores(q)]

# Si solo se necesita la cantidad de respuestas y no las respuestas en si
# se puede hacer en O(N^2)
def decomp(n):
	return sum( len(divisores(p)) * len(divisores(q)) for p,q in sumandos(n) )

# si se busca el mayor valor ejecutando esto entre 1 y N
# se obtiene la respuesta inocente en O(N^3)
def respuestaInocente(n):
	return max([decomp(i) for i in range(1, n+1)])


n = 12
print(f"Sumandos de {n}:")
for r in sumandos(n):
	print(r)

print(f"Divisores de {n}:")
for r in divisores(n):
	print(r)

print(f"Respuesta Inocente de {n}:")
for r in decompSecuencias(n):
	print(r)

print(f"En total son {len(decompSecuencias(n))}")

print(f"Respuesta del maximo de las descomposiciones entre 1 y 100: {respuestaInocente(100)}")