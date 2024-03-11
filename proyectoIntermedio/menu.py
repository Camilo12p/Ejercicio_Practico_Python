import os 
import ejercicio5 as e5
import ejercicio6 as e6
import ejercicio7 as e7
# import ejercicio7 as e7
# import ejercicio8 as e8

def Principal():
    titulo='''
        ++++++++++++++++++++++++++++
        +  Ejercicios Intermedios  +
        ++++++++++++++++++++++++++++
        '''
    os.system('clear')
    print(titulo)

def eje5(source:dict):
    titulo='''

        ++++++++++++++++++++++++++++
        +  Ejercicios Intermedios  +
        ++++++++++++++++++++++++++++
    
        1. Registrar Ciudad
        2. Registrar Sismo
        3. Buscar sismos por ciudad
        4. Informe de riesgo
        5. Salir
    '''
   

    validar=True
    while validar: 
        os.system('cls')   
        print(titulo)
        op=int(input('Seleccione una opcion: '))
        
        if op==1:
            e5.registrarCiudad(source)
            input()
            pass
        elif op==2:
            e5.registrarSismos(source)
            input()
            pass
        elif op==3:
            e5.buscar(source)
            input()
            pass
        elif op==4:
            e5.informes(source)
            input()
            pass
        elif op==5:
            validar=False
            input()   
        else:
            print('Selecciona un valor valido')  
            input()  


def eje6(source:dict):
    titulo='''

        ++++++++++++++++++++++++++++
        +  Ejercicios Intermedios  +
        ++++++++++++++++++++++++++++
    
        1. Registrar Dependencia
        2. Registrar consumo por dependencia :
        3. Ver CO2 producido
        4. Dependencia que produce mayor CO2
        5. Salir
    '''
   

    validar=True
    while validar: 
        os.system('cls')   
        print(titulo)
        op=int(input('Seleccione una opcion: '))
        
        if op==1:
            e6.registrarDependencia(source)
            input()
            pass
        elif op==2:
            e6.registrarconsumo(source)
            input()
            pass
        elif op==3:
            e6.verConsumo(source)
            input()
            pass
        elif op==4:
            e6.mayorCo2(source)
            input()
            pass
        elif op==5:
            validar=False
            input()   
        else:
            print('Selecciona un valor valido')  
            input()  


def eje7(source:dict):
    titulo='''

        ++++++++++++++++++++++++++++
        +  Ejercicios Intermedios  +
        ++++++++++++++++++++++++++++
    
        1.Registrar Producto.
        2.Visualizacion de productos.
        3.Actualizar stock.
        4.Informe productos criticos.
        5.Ganancia potencial.
        6.Salir
    '''
    validar=True
    while validar: 
        os.system('cls')   
        print(titulo)
        op=int(input('Seleccione una opcion: '))
        
        if op==1:
            e7.registrarProducto(source)
            input(source)
            input()
            pass
        elif op==2:
            e7.visualizar(source)
            input()
            pass
        elif op==3:
            e7.actualizarStock(source)
            input()
            pass
        elif op==4:
            e7.informes(source)
            input()
            pass
        elif op==5:
            e7.calcularGanancias(source)
            input()
            pass
        elif op==6:
            validar=False
            input()   
        else:
            print('Selecciona un valor valido')  
            input()