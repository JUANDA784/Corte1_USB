import fcn_ext

def main():
    nombre = input('Escriba su nombre: ')
    fcn_ext.Saludo(nombre)
    print('Funcion: ', __name__)

if __name__=="__main__":
    main()