def registrarDependencia(source:dict):
    nombre=str(input('Ingrese el nombre de la dependencia registrar: ')).capitalize()
    

    dependencia={
        'nombre':nombre
    }
    source.update({len(source)+1:dependencia})


def registrarconsumo(source:dict):
    
    nombre=str(input('ingrese el nombre de la dependencia: ')).capitalize()
    
   

    for key,value in source.items():
        dispositivo={}
        vehiculos={}
        if nombre==value['nombre']:
            n=int(input('ingrese el numero de dispositivos: '))
            m=int(input('Cuantos vehiculos contiene su dependencia: '))
            for i in range(m):
                a=float(input(f'ingrese la cantidad de kilometraje que recorre su vehiculo numero {i+1}: '))
                vehiculos.update({len(vehiculos):{'kilometraje':a}})
            for i in range(n):
                n=str(input('ingrese el nombre del dispositivo: '))
                x=float(input(f'ingrese la potencia de {n}: '))
                y=int(input('ingrese las horas promedio que usa el dispositivo: '))
                dispositivo.update({n:{'potencia':x}})
                dispositivo[n].update({'horas':y})
                 
            value.update({'numeroDispositivos':n})
            value.update({'dispositivos':dispositivo})
            value.update({'vehiculos':vehiculos})
            validarinfo(source)
            
    


def validarinfo(source:dict):
    
    factor=164,38 #gramos por kwh
    for key,value in source.items():
        kwh=0
        imcv=0
        if 'dispositivos' in value:
            for key2,value2 in value['dispositivos'].items():
                kwh+=(value2['potencia']*value2['horas'])/1000
        if 'vehiculos' in value:    
            for key3,value3 in value['vehiculos'].items():
                imcv+=value3['kilometraje']
            
        
            value.update({'consumototal':30*kwh})
            value.update({'emisionCo2':30*kwh*164.38}) 

def verConsumo(source:dict):

    nombre=str(input('ingrese el nombre de la dependencia: ')).capitalize()

    for key,value in source.items():
        if nombre==value['nombre']:
            print(f'El consumo de CO2 es: ' ,value['emisionCo2'],' g/Kwh')

def mayorCo2(source:dict):
    mayorco2=0
    nombre=''
    for key,value in source.items():
        if 'emisionCo2' in value: 
            if mayorco2<value['emisionCo2']:
                mayorco2=value['emisionCo2']
                nombre=value['nombre']

    print(f'La dependencia que mayor CO2 emite es {nombre} con {mayorco2} g/Kwh')