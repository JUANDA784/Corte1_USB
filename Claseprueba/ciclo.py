num = int(input('Ingrese un numero de 2 a 8 digitos: '))

for i in range(10,100000000):
    cont = num/i
    resul = cont/i
    nu1 = cont-resul
    print(cont)
    print(resul)
    print(nu1)