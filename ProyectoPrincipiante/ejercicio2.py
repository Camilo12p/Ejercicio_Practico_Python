def AgregarEstudiante(source:dict):
    
    nombre=str(input('Ingrese el nombre del estudiante: ')).capitalize()
    edad=int(input('Ingrese la edad del estudiante: '))
    peso=float(input('Ingrese el peso en (Kg) del estudiante: '))
    estatura=float(input('Ingrese la estatura en (m) del estudiante: '))
    
    estudiante={
        'nombre':nombre,
        'edad':edad,
        'peso':peso,
        'estatura':estatura,
        'imc':'imc',
        'estadoImc':'estadoimc'
    }
    asignarEstado(source)
    source.update({len(source)+1:estudiante})
    
def asignarEstado(source:dict):
    for key,value in source.items():
        
        imc=value['peso']/(value['estatura']*value['estatura'])
        value['imc']=imc
        if imc>18.5 and imc<25:
            value['estadoImc']='normal'
            pass
        elif imc>=25 and imc<30:
            value['estadoImc']='sobrepeso'
            pass
        elif imc>=30 and imc<35:
            value['estadoImc']='obesidad 1'
            pass
        elif imc>=35 and imc<40:
            value['estadoImc']='obesidad 2'
            pass
        elif imc>=40:
            value['estadoImc']='obesidad 3'
        else:
            pass
    

def verEstudiante(source:dict):
    estudiante=str(input('Ingrese el nombre del estudiante: ')).capitalize()
    contador=0
    for key,value in source.items():
        if estudiante==value['nombre']:
            print('Nombre:',value['nombre'])
            print('Edad:',value['edad'])
            print('imc:',value['imc'])
            print('Estado IMC:',value['estadoImc'])
        else:
            contador=1
            

    if contador==1 or len(source)==0:
        print(f'El estudiante {estudiante} no se encuentra en el sistema')