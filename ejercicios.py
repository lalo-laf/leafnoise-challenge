# Ejercicio 1: Voy leyendo la palabra desde ambos extremos
def esPalindromo(palabra):
    palabra = palabra.lower()   # Asumo que una palabra es palíndromo independientemente de las mayúsculas.
    longitud = len(palabra)
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud-i-1]:
            return False
    return True


# Ejercicio 2: Si veo un abierto lo cuento. Si veo un cerrado descuento un abierto, y si no puedo descontar o termino con algún abierto => no está balanceado.
def parentesisBalanceados(palabra):
    abiertos = 0
    for i in range (len(palabra)):
        if palabra[i] == "(":
            abiertos += 1
        elif palabra[i] == ")":
            abiertos -= 1
            if abiertos < 0:
                return False
    return abiertos == 0


# Ejercicio 3: Separo las palabras y las voy insertando en orden inverso.
def invertirPalabras(palabras):
    palabrasEnLista = palabras.split()
    res = []
    for i in palabrasEnLista:
        res.insert(0, i)
    return " ".join(res)


# Tests
print(not esPalindromo("hola mundo") and
    not esPalindromo("   a ") and
    esPalindromo("oso") and
    esPalindromo("reconocer") and
    esPalindromo("a") and
    esPalindromo(""))

print(parentesisBalanceados("(hola)") and
    parentesisBalanceados("a(j(d) (  j)9)") and
    parentesisBalanceados("(((ht)( sdfg(fds(h) ))g())d)") and
    parentesisBalanceados("texto sin parentesis") and
    not parentesisBalanceados("a(a()") and
    not parentesisBalanceados(")a("))

print(invertirPalabras("") == "" and
    invertirPalabras("unaSola") == "unaSola" and
    invertirPalabras("dos palabras") == "palabras dos" and
    invertirPalabras("unas cuantas palabras mas") == "mas palabras cuantas unas" and
    invertirPalabras(" varios   espacios     ") == "espacios varios")
