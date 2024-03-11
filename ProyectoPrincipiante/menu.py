import os 
import ejercicio1 as e1
import ejercicio2 as e2
import ejercicio3 as e3
def Principal():
    titulo='''
        ++++++++++++++++++++++++++++
        + Ejercicios Principiantes +
        ++++++++++++++++++++++++++++
        '''
    os.system('clear')
    print(titulo)
    

def ejercicio1():
    titulo='''
        ++++++++++++++++++++++++++++
        +    Ejercicios Numero 1   +
        ++++++++++++++++++++++++++++
        '''
    
    os.system('clear')
    print(titulo)
    
def ejercicio2(source:dict):
    titulo='''
        ++++++++++++++++++++++++++++
        +    Ejercicio Numero 2    +
        ++++++++++++++++++++++++++++
        '''
    os.system('clear')
    
    validar=True
    while validar:
        
        print(titulo)
    
        print('1.Agregar estudiante\n2.Eliminar estudiante\n3.Ver estudiante\n4.salir\n')
        op=int(input('Selecciona una opcion: '))
        if op==1:
            e2.AgregarEstudiante(source)
            input()
            pass
        elif op==2:
            os.system('pause')
            input()
            pass
        elif op==3:
            e2.asignarEstado(source)
            e2.verEstudiante(source)
            input()
            pass
        elif op==4:
            validar=False
            pass
        else:
            print('Selecciona un valor valido')    
    
def ejercicio3(source:dict):
    titulo='''  
            ++++++++++++++++++++++++++++++++++++++
            +   Estadistica de los estudiantes   +
            ++++++++++++++++++++++++++++++++++++++

            a. Cuantos estudiantes se encuentran en el peso ideal.
            b. Cuantos estudiantes se encuentran en obesidad grado I
            c. Cuantos estudiantes se encuentran en obesidad grado II
            d. Cuantos estudiantes se encuentran en obesidad grado III
            e. Cuantos estudiantes se encuentran en Sobrepeso
            f. Salir
        '''
    validar=True    
    while validar:    
        os.system('cls')
        print(titulo)
        op=str(input('Selecciona una opcion: ')).lower()
        Totalpersonas=e3.contador(source)

        if op=='a':
            print(f'total de persona con peso ideal {Totalpersonas[0]}')
            input()
        elif op=='b':
            print(f'total de persona con obesidad 1: {Totalpersonas[1]}')
            input()
        elif op=='c':
            print(f'total de persona con obesidad 2: {Totalpersonas[2]}')
            input()
        elif op=='d':
            print(f'total de persona con obesidad 3: {Totalpersonas[3]}')
            input()
        elif op=='e':
            print(f'total de persona con sobrepeso: {Totalpersonas[4]}')
            input()
        elif op=='f':
            validar=False
            

def ejercicio4():
    titulo='''  
            ++++++++++++++++++++++++++++++++++++++
            +           Ejercicio #4             +
            ++++++++++++++++++++++++++++++++++++++

            '''
    titulo2='''
            a. Total de números ingresados
            b. Total de números pares ingresados
            c. Promedio de los números pares
            d. Promedio de los números impares
            e. Cuantos números son menores que 10
            f. Cuantos números están entre 20 y 50
            g. Cuantos números son mayores que 100
            h. Salir
    
        '''
    os.system('cls')
    print(titulo)
    numeros=[]
    numero=0
    i=1
    while True:
        numero=float(input(f'Ingrese el numero {i}: '))
        if numero>=0:
            numeros.append(numero)
            i+=1
        else:
            break


    if numero<0:
        
        validar=True
        
        while validar:
            os.system('clear')
            print(titulo)
            print(titulo2)
            op=str(input('Selecciona una opcion: ')).lower()
            if op=='a':
                print(f'total de numeros ingresados: {len(numeros)}')
                input()
            elif op=='b':
                idx=0
                for item in numeros:
                    if item%2==0:
                        idx+=1
                print(f'total de numeros pares: {idx}')
                input()
            elif op=='c':
                idx=0
                for item in numeros:
                    if item%2==0:
                        idx+=1
                print(f'Promedio de pares: {(idx)/len(numeros)}')
                input()
            elif op=='d':
                idx=0
                for item in numeros:
                    if item%2==0:
                        idx+=1
                print(f'Promedio impares: {(len(numeros)-idx)/len(numeros)}')
                input()
            elif op=='e':
                idx=0
                for item in numeros:
                    if item<10:
                        idx+=1
                print(f'Numeros menores que 10: {idx}')
                input()
            elif op=='f':
                idx=0
                for item in numeros:
                    if item>=20 and item<=50:
                        idx+=1
                print(f'Numeros entre 20 y 50: {idx}')
                input()
            elif op=='g':
                idx=0
                for item in numeros:
                    if item>100:
                        idx+=1
                print(f'Numeros mayores de 100: {idx}')
                input()
            elif op=='h':
                validar=False
                