#def Saludo(nombre):
#    print(f'Hola {nombre}')
#    return
#nombre = input('Ingrese el nombre: ')
#Saludo(nombre)

def factorial(x): 
    f=1
    for i in range(1,x+1):
         f*=i
    return f



m = int(input('Ingrese un numero: ')) 
n = int(input('Ingrese un numero: '))
b=m-n
c = factorial(m)/(factorial(n)*factorial(b))
print(c)




#import math
#
#resultado = math.factorial(4)/(math.factorial(2)*math.factorial(4-2))
#print(resultado)
#
#def area(r):
#    pi = 3.1416
#    a = pi*(r**2)
#    return a
#
#def volumen(h,A):
#    v = A*h
#    return v
#
#r = int(input('Ingrese el valor del radio: '))
#h = int(input('Ingrese el valor del altura: '))
#
#A = area(r)
#v = volumen(h,A)
#
#print(f'El area es {A} y volumen es {v}')
#
#def suma(a,b):
#    resultado = a + b
#    return resultado
#
#def imprimir(nombre):
#    print(nombre, 'Su resultado es: ')
#
#n = 'si'
#while n =='si':
#    nombre = input('ingrese su nombre: ')
#    a = int(input('ingrese un numero: '))
#    b = int(input('ingrese un numero: '))
#    res = suma(a,b)
#    imprimir(nombre)
#    print(res)
#    n = input('¿Quieres sumar otro numero? (si/no)')
#