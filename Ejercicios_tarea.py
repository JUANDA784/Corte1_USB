
print('1. Un programa que imprima todas los numeros impares desde el uno hasta dicho numero.')
print('2. Un programa que calcule el numero factorial de un numero seleccionado.')
print('3. Un programa que indique si es primo o no. Y ademas imprima los numeros primos hasta dicho numero.')

while True:

    punto = int(input('\nIngrese el punto que desea seleccionar. Si desea salir del programa escriba "4": '))

    if punto == 4:
        break
    else:    
        if punto==1:
            num = int(input('Ingrese un numero entero: '))
            n=0
            while n<num:
                n+=1
                if n%2!=0:
                    print(n, end= ', ')

        elif punto==2:
            fact = int(input('Ingrese un numero entero: '))
            print(fact, end= '! -> ')
            f1=1
            for i in range(fact,1,-1):
                f1 = f1*i
                print(i, end=' x ')
            print('1 =',f1)
            
        elif punto==3:
            num2 = int(input('Ingrese un numero entero: '))
            if num2>1:
                for i in range(2,num2+1):
                    cont = 2
                    primo = True
                    while primo and cont < i:
                        if i % cont == 0:
                            primo = False
                        else:
                            cont += 1
                    if primo:
                        print(i, end= ', ')
                print('\n')
                if primo:
                    print(f'El {num2} es un numero primo') 
                else:
                    print(f'El {num2} NO es un numero primo')
            else:
                print('El numero tiene que ser mayor que 1')
    
            
        
    