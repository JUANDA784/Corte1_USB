num = int(input('Ingrese la cantidad de numeros que desee: '))
j = 2 ;x = 0; n = 2
print('1')
while x <= num:
    div = n % j
    if div == 0:
        if n == j:
            print(n)
            x += 1
        j=2
        n += 1
    else:
        j+=1

#Punto 2 del parcial.
num = int(input('Ingrese la cantidad de numeros: '))
a=0
b=1
print(a,',',b, end= ', ')
for i in range(num-2):
   c = a + b
   a = b
   b = c
   print(c, end=', ')
   
#Punto 1 del parcial.
n = int(input('Ingrese un numero de 2 a 8 digitos: '))
cont1=0
cont2=0
while n!=0:
    x=(n//10)
    y=x*10
    dig= n-y
    n=x
    if dig == 5:
        cont1+=1
        print('salto')
    else:
        cont2+=1
        print(dig)
print(f'digitos iguales 5: {cont1}')
print(f'digitos diferentes 5: {cont2}')
print(f'digitos diferentes 5: {cont1+cont2}')