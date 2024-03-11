from tabulate import tabulate

def registrarProducto(source:dict):
    codigo=int(input('Ingrese el codigo del producto a registrar: '))
    nombre=str(input('Ingrese el nombre del producto a registrar: ')).capitalize()
    valorCompra=float(input('Ingrese el valor de la compra del producto a registrar: '))
    valorVenta=float(input('Ingrese el valor de la venta del producto a registrar: '))
    stockMinimo=int(input('Ingrese el stock Minimo del producto a registrar: '))
    stockMaximo=int(input('Ingrese el stock maximo del producto a registrar: '))
    stock=int(input('Ingrese la cantidad de stock que contiene: '))
    nombreProveedor=str(input('Ingrese el nombre del poveedor del producto a registrar: ')).capitalize()
    

    dependencia={
        'codigo':codigo,
        'nombre':nombre,
        'valorCompra':valorCompra,
        'valorVenta':valorVenta,
        'stockMinimo':stockMinimo,
        'stockMaximo':stockMaximo,
        'stock':stock,
        'nombreProveedor':nombreProveedor
    }
    source.update({len(source)+1:dependencia})


def visualizar(source:dict):
    table=[]
    for key,value in source.items():
        table.append([value['codigo'],value['nombre'],value['valorCompra'],value['valorVenta'],value['stockMinimo'],value['stockMaximo'],value['stock'],value['nombreProveedor']])

    headers=['codigo','nombre','valor Compra', 'valor Venta', 'Stock Minimo','stock Maximo','stock','Nombre proveedor']
    print(tabulate(table, headers=headers, tablefmt='grid'))

def actualizarStock(source:dict):
    nombre=str(input('ingrese el nommbre del producto: ')).capitalize()
    
    
    for key,value in source.items():
        if nombre==value['nombre']:
            print('1.Desea añadir productos\n2.Desea eliminar producto')
            op=int(input('selecciona una opcion: '))
            if op==1:
                n=int(input('Cuantos productos desea añadir: '))
                value['stock']+=n
                pass
            elif op==2:
                n=int(input('Cuantos productos desea eliminar: '))
                value['stock']-=n
                pass
            else:
                print('selecciona la respuesta correcta')

def informes(source:dict):
    maximo={}
    minimo={}

    print('1.Productos sobrepasados del maximo\n2.Productos que tienen menos del minimo')
    op=int(input('Ingrese un valor: '))
    if op==1:
        for key,value in source.items():
            if value['stock']>=value['stockMaximo']:
                maximo.update({len(maximo):value})
            
        visualizar(maximo)
        pass
    elif op==2:
        for key,value in source.items():
            if value['stock']<=value['stockMinimo']:
                minimo.update({len(minimo):value})
            
        visualizar(minimo)

        pass
    else:
        print('selecciona la respuesta correcta')

def calcularGanancias(source:dict):
    ganancias=[]
    for key,value in source.items():
        ganancias.append([value['codigo'],value['nombre'],value['valorVenta'],value['valorCompra'],(value['valorVenta']-value['valorCompra'])])

    headers=['codigo','nombre','valor Venta','valor compra', 'ganancias']

    print(tabulate(ganancias,headers=headers,tablefmt='grid'))    