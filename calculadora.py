def sumar(a,b):
    return (a + b)
def restar(a,b):
    return (a - b)
def multiplicar(a,b):
    return (a * b)
def dividir(a,b):
    if b != 0:
        return (a / b)
    else:
        return "Error: División por cero"

numero1=10
numero2=5

print("La suma es: ", sumar(numero1, numero2))
print("La resta es: ", restar(numero1, numero2))