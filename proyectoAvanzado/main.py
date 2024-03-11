import menu as m
import ejercicio8 as e8

torneo={
    'novato':{}, #{1: {'nombre': 'Camilo', 'edad': 15, 'pj': 1, 'pg': 1, 'pp': 0, 'pa': 1, 'tp': 2}, 2: {'nombre': 'Jose', 'edad': 16, 'pj': 1, 'pg': 0, 'pp': 1, 'pa': 0, 'tp': 0}},
    'intermedio':{},
    'avanzado':{}
}
fechas={
    'novato':{1:{},2:{},3:{},4:{},5:{}},
    'intermedio':{1:{},2:{},3:{},4:{},5:{}},
    'avanzado':{1:{},2:{},3:{},4:{},5:{}}
}

validar=True
while validar:

    try:
        m.Principal()
        print('1.Registra Participantes\n2.Registrar fechas\n3.Mostrar tabla\n4.Mostra ganador\n5.Salir\n')
        op=int(input('Seleccione una opcion: '))
        if op==1:
            e8.RegistrarParticipante(torneo)
            print(torneo)
            input()
            pass
        elif op==2:
            e8.registraFecha(fechas,torneo)
            print(torneo)
            input()
            pass
        elif op==3:
            e8.mostrarTabla(torneo)
            input()
            pass
        elif op==4:
            e8.ganador(torneo)
            input()
        elif op==5:
            validar=False
            input()
        else:
            print('Selecciona un valor valido')
            input()    
    except ValueError:
        print('Selecciona un valor valido')
        input()
