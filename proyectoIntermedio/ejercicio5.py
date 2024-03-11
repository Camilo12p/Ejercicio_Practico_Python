import os

def registrarCiudad(source:list):
    if len(source)<5: 
        nombre=str(input('Ingrese el nombre de la ciudad a registrar: ')).capitalize()
        if verificarNombre(source,nombre):
            source.append([nombre,[]])
            print(source)
        else:
            print('El nombre ya ha sido inscrito')
    else:
        print('Ya llego al numero maximo de sismos')

def verificarNombre(source:list,nombre:str):
    verificar=True
    for item in source:
        if item[0]==nombre:
            verificar=False
    return verificar        

def validarinfo(source:list):
    

    if len(source)!=0:
        for item in source:
            promedio=0
            suma=0
            for i in range(len(item[1])):
                suma+=item[1][i]    

            promedio=suma/len(source[0][1])
            
            if promedio<=2.5:
                item.append('Amarillo')
                pass
            elif promedio>2.5 and promedio<=4.5:
                item.append('Naranja')
                pass
            elif promedio>4.5:
                item.append('Rojo')
                pass


def registrarSismos(source:list):
    sismo=0
    validar=True
    diferencias=diferencia(source)

    while validar:  
        if numeroSismo(source):
            for item in source:
                sismo=float(input(f'ingrese el sismo numero {len(item[1])+1} en la ciudad de {item[0]}: '))
                item[1].append(sismo)
            validar=bool(input('Deseas añadir mas sismos\nS. SI\nEnter. NO\n'))
            
        else:
            for i,item in enumerate(source):
                if diferencias[i]>0:
                    if i==0:
                        print(f'Todas la ciudades deben tener la misma cantidad de sismo\nA {item[0]} le faltan {diferencias[i]} sismos ')
                        for j in range(diferencias[i]):
                            sismo=float(input(f'ingrese el sismo numero {(len(item[1])+1)} en la ciudad de {item[0]}: '))
                            item[1].append(sismo)
                    elif i==1:
                        print(f'Todas la ciudades deben tener la misma cantidad de sismo\nA {item[0]} le faltan {diferencias[i]} sismos ')
                        for j in range(diferencias[i]):
                            sismo=float(input(f'ingrese el sismo numero {(len(item[1])+1)} en la ciudad de {item[0]}: '))
                            item[1].append(sismo)
                    elif i==2:
                        print(f'Todas la ciudades deben tener la misma cantidad de sismo\nA {item[0]} le faltan {diferencias[i]} sismos ')
                        for j in range(diferencias[i]):
                            sismo=float(input(f'ingrese el sismo numero {(len(item[1])+1)} en la ciudad de {item[0]}: '))
                            item[1].append(sismo)
                    elif i==3:
                        print(f'Todas la ciudades deben tener la misma cantidad de sismo\nA {item[0]} le faltan {diferencias[i]} sismos ')
                        for j in range(diferencias[i]):
                            sismo=float(input(f'ingrese el sismo numero {(len(item[1])+1)} en la ciudad de {item[0]}: '))
                            item[1].append(sismo)
                    elif i==4:
                        print(f'Todas la ciudades deben tener la misma cantidad de sismo\nA {item[0]} le faltan {diferencias[i]} sismos ')
                        for j in range(diferencias[i]):
                            sismo=float(input(f'ingrese el sismo numero {(len(item[1])+1)} en la ciudad de {item[0]}: '))
                            item[1].append(sismo)

    validarinfo(source)
    print(source)


def numeroSismo(source:list):
    validacion=True
    lens=len(source[0][1])
    for item in source:
        if len(item[1])!=lens:
            validacion=False
        lens=len(item[1])

    return validacion

def diferencia(source:list):
    numeromayor=len(source[0][1])
    diferencias=[]
    for item in source:
        if len(item[1])>=numeromayor:
            numeromayor=len(item[1])
    
    for item in source:
        diferencias.append((numeromayor-len(item[1])))
    
    return diferencias

def buscar(source:list):
    nombre= str(input('ingresa el nombre del la ciudad a buscar: ')).capitalize()
    estadobusqueda=True
    for item in source:
        if item[0]==nombre:
            print('nombre: ',item[0])
            print('Sismos: ',item[1])
            print('Estado de riesgo: ', item[2])
            estadobusqueda=False
    if estadobusqueda: 
        print('La ciudad no se encuentra')

def informes(source:list):
    for item in source:
        if item[2]=='Amarillo':
            print(item[0], ': Amarillo (Sin riesgo) : El promedio de los sismos es < 2,5')
        elif item[2]=='Naranja':
            print(item[0], ': Naranja (Riesgo medio) : El promedio de los sismos esta entre 2.6 y 4.5')
        elif item[2]=='Rojo':
            print(item[0], ': Rojo (Riesgo alto) : El promedio de los sismos es mayor a 4.5')