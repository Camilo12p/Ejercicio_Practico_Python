def ejercicio1():
    valor=0
    suma=0
    
    for i in range(3):
        validar=True
        while validar:
            valor=int(input(f'Ingrese el valor numero {i+1}: '))
            if valor>=0:
                suma+=valor
                validar=False
            else:
                print('el valor ingresado no es positivo')   
    print(f'La suma de los tres numeros es: {suma}')

