import menu as m
import ejercicio1 as e1
import ejercicio2 as e2
import os

campus={
    # 1:{'nombre':'Camilo',
    #     'edad':21,
    #     'peso':70,
    #     'estatura':1.75,
    #     'imc':'imc',
    #     'estadoImc':'normal'
    # },
    
    # 2:{'nombre':'Jose',
    #     'edad':21,
    #     'peso':70,
    #     'estatura':1.75,
    #     'imc':'imc',
    #     'estadoImc':'sobrepeso'
    # },
    
    # 3:{'nombre':'real',
    #     'edad':21,
    #     'peso':70,
    #     'estatura':1.75,
    #     'imc':'imc',
    #     'estadoImc':'obesidad 1'
    # },
    
    # 4:{'nombre':'Camilo2',
    #     'edad':21,
    #     'peso':70,
    #     'estatura':1.75,
    #     'imc':'imc',
    #     'estadoImc':'obesidad 2'
    # },

    # 5:{'nombre':'Camilo3',
    #     'edad':21,
    #     'peso':70,
    #     'estatura':1.75,
    #     'imc':'imc',
    #     'estadoImc':'obesidad 3'
    # }
    
    #todos son de estado normal si se quiere usar estos ejemplo debe cambiar el peso y estatura 
}
validar=True
while validar:
    try:
        m.Principal()
        print('1.Ejercicio 1\n2.Ejercicio 2\n3.ejercicio 3\n4.ejercicio 4\n5.Salir\n')
        op=int(input('Seleccione una opcion: '))
        if op==1:
            m.ejercicio1()
            e1.ejercicio1()
            input()
            pass
        elif op==2:
            m.ejercicio2(campus)
            input()
            pass
        elif op==3:
            m.ejercicio3(campus)
            input()
            pass
        elif op==4:
            m.ejercicio4()
            input()
            pass
        elif op==5:
            validar=False
            input()
        else:
            print('Selecciona un valor valido')
            input()   
    except ValueError:
        print('Selecciona un valor valido1')
        input()