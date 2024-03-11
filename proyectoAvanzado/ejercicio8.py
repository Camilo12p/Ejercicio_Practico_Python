from tabulate import tabulate

def RegistrarParticipante(source:dict):
    nombre=str(input('Ingrese el nombre del participante: ')).capitalize()
    edad=int(input('ingrese la edad del participante: '))
    participante={
        'nombre':nombre,
        'edad':edad,
        'pj':0,
        'pg':0,
        'pp':0,
        'pa':0,
        'tp':0
    }

    if edad<15:
        print('El jugador no tiene edad suficiente para participar')
    elif edad>=15 and edad<=16:
        print('debido a la edad el participante solo puede participar en la categoria novato')
        print('1.Desea participar\n2.No desea partipar')
        validar2=True
        while validar2:
            op=int(input('Selecciona una respuesta'))
            if op==1:
                source['novato'].update({len(source['novato'])+1:participante})
                validar2=False
            else:
                validar2=False
    elif edad>16 and edad<=20:
        print('debido a la edad el participante solo puede participar en la categoria intermedio')
        print('1.Desea participar\n2.No desea partipar')
        validar2=True
        while validar2:
            op=int(input('Selecciona una respuesta: '))
            if op==1:
                source['intermedio'].update({len(source['intermedio'])+1:participante})
                validar2=False
            else:
                validar2=False
    elif edad>20 and edad<=120:
        print('debido a la edad el participante solo puede participar en la categoria avanzado')
        print('1.Desea participar\n2.No desea partipar')
        validar2=True
        while validar2:
            op=int(input('Selecciona una respuesta'))
            if op==1:
                source['avanzado'].update({len(source['avanzado'])+1:participante})
                validar2=False
            else:
                validar2=False

def registraFecha(fechas:dict,source:dict):
    

    print('1.Categoria novato\n2.Categoria intermedio\n3.Categoria Avanzada')
    op=int(input('Selecciona la categoria: '))
    
    if op==1:
        print(len(source['novato']))
        if len(source['novato'])<2:
            print('No se puede jugar fechas porque no hay 5 equipos')
        else:
            fecha(fechas['novato'],source['novato'])
    elif op==2:   
        if len(source['intermedio'])<5:
            print('No se puede jugar fechas porque no hay 5 equipos')
        else:
            fecha(fechas['intermedio'],source['intermedio'])
    elif op==3:    
        if len(source['avanzado'])<5:
            print('No se puede jugar fechas porque no hay 5 equipos')
        else:
            fecha(fechas['avanzado'],source['avanzado'])

   
   
def fecha(fecha:dict, source:dict,contador=1):

        idx=1
        partido={}
        for key,value in source.items():
            print(f'{idx}.',value['nombre'])
            idx+=1
        
        for i in range(1,3):
            if i==1:
                local=int(input('ingrese el equipo local: '))
                golesL=int(input('Cuantos puntos marco?: '))
            else:
                visitante=int(input('ingrese el equipo visitante: '))
                golesv=int(input('Cuantos puntos marco?: '))

        partido.update({'local':source[local]['nombre'],'golesL':golesL,'visitante':source[visitante]['nombre'],'golesv':golesv})
                
        fechaday=int(input('Que fecha se esta jugando: '))
        fecha[fechaday].update({contador:partido})
    #  participante={
    #     'nombre':nombre,
    #     'edad':edad,
    #     'pj':0,
    #     'pg':0,
    #     'pp':0,
    #     'pa':0,
    #     'tp':0
    # }
        if golesL>golesv:
            source[local]['pg']+=1
            source[local]['tp']+=2
            source[visitante]['pp']+=1
            source[local]['pa']+=golesL-golesv
            
            
            
        elif golesL<golesv:
            source[local]['pp']+=1
            source[visitante]['pg']+=1
            source[visitante]['tp']+=2
            source[visitante]['pa']+=golesv-golesL
            
            
        
        source[local]['pj']+=1
        source[visitante]['pj']+=1
        
        
        contador+=1
        if contador<=len(source)/2:
            definirFechas(fechas,source,contador)
                

def hacertabla(source:dict):
    tabla=[]
    for key,value in source.items():
        tabla.append([value['nombre'],value['pj'],value['pg'],value['pp'],value['pa'],value['tp']])

    headers=['nombre','PJ','PG','PP','PA','TP']

    print(tabulate(tabla, headers=headers,tablefmt='grid'))
    return tabla

def mostrarTabla(source:dict):
    print('1.Categoria novato\n2.Categoria intermedio\n3.Categoria Avanzada')
    op=int(input('Selecciona la categoria: '))

    if op==1:
        hacertabla(source['novato'])
    elif op==2:   
        hacertabla(source['intermedio'])
    elif op==3:    
        hacertabla(source['avanzado'])

def elegirganador(source:dict,categoria:str):
    tabla=hacertabla(source)
    pa=tabla[0][4]
    tp=tabla[0][5]
    nombre=''
    for item in tabla:
        if item[4]>=pa and item[5]>=tp:
            pa=item[4]
            tp=item[5]
            nombre=item[0]
    
    print(f'El ganador de la categoria {categoria} es {nombre}')

def ganador(source:dict):
    print('1.Categoria novato\n2.Categoria intermedio\n3.Categoria Avanzado')
    op=int(input('Seleccione la categoria: '))
    categorias=['Novato','Intermedio','Avanzado']
    for i in range(3):
        if op==i+1:
            elegirganador(source[categorias[i].lower()],categorias[i+1])