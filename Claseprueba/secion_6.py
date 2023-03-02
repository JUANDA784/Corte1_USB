print('Escoja una de las siguientes opciones:\n')
print('1. For in range(final)')

print('2. For in range(inicio, final)')
print('3. For in range(inicio, final, paso)')

opc =  input('Escoja una opcion: ')

if opc == '1':
    for i in range(10):
        print(i+1)
    print('fin del proceso')
elif opc == '2':
    for i in range(5,10):
        print(i+1)
    print('fin del proceso')
elif opc == '3':
    for i in range(1,10,2):
        print(i)
    print('fin del proceso')
elif opc == '4':
    for i in range(11,1,-2):
        print(i)
    print('Fin del proceso')
