def suma(a,b):
    resultado = a + b
    return resultado
n = 'si'
while n =='si':
 
    a = int(input('ingrese un numero: '))
    b = int(input('ingrese un numero: '))
    res = suma(a,b)
    print(res)
    n = input('¿Quieres sumar otro numero? (si/no)')