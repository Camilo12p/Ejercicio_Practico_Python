import menu as m

controlRiesgo=[
    # ["Bogota", [6.2, 5.5, 4.8], 'Amarillo'],
    # ["Medellin", [4.5, 5.7], 'Rojo'],
    # ["Cali", [5.8, 6.1, 4.9], 'Naranja'],
    # ["Barranquilla", [4.7, 5.9], 'Amarillo'],
    # ["Cartagena", [6.0], 'Rojo']
]
energiaCiudad={}
productos={
    1:{
        'codigo':1,
        'nombre':'A',
        'valorCompra':10,
        'valorVenta':20,
        'stockMinimo':10,
        'stockMaximo':60,
        'stock':100,
        'nombreProveedor':'Camilo'
    },
    2:{
        'codigo':1,
        'nombre':'B',
        'valorCompra':10,
        'valorVenta':20,
        'stockMinimo':10,
        'stockMaximo':60,
        'stock':9,
        'nombreProveedor':'Camilo'
    },
    3:{
        'codigo':1,
        'nombre':'C',
        'valorCompra':10,
        'valorVenta':20,
        'stockMinimo':10,
        'stockMaximo':60,
        'stock':11,
        'nombreProveedor':'Camilo'
    },
    4:{
        'codigo':1,
        'nombre':'D',
        'valorCompra':10,
        'valorVenta':20,
        'stockMinimo':10,
        'stockMaximo':60,
        'stock':50,
        'nombreProveedor':'Camilo'
    },
    5:{
        'codigo':1,
        'nombre':'E',
        'valorCompra':10,
        'valorVenta':20,
        'stockMinimo':10,
        'stockMaximo':160,
        'stock':100,
        'nombreProveedor':'Camilo'
    },
    6:{
        'codigo':1,
        'nombre':'F',
        'valorCompra':10,
        'valorVenta':20,
        'stockMinimo':20,
        'stockMaximo':60,
        'stock':10,
        'nombreProveedor':'Camilo'
    },
}
validar=True
while validar:

    try:
        m.Principal()
        print('1.Ejercicio 5\n2.Ejercicio 6\n3.ejercicio 7\n4.Salir\n')
        op=int(input('Seleccione una opcion: '))
        if op==1:
            m.eje5(controlRiesgo)
            input()
            pass
        elif op==2:
            m.eje6(energiaCiudad)
            input()
            pass
        elif op==3:
            m.eje7(productos)
            input()
            pass
        elif op==4:
            validar=False
                   
        else:
            print('Selecciona un valor valido')
            input()    
    except ValueError:
        print('Selecciona un valor valido')
        input()
