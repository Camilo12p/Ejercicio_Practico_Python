def contador(source:dict):
    peso1={}
    peso2={}
    peso3={}
    peso4={}
    peso5={}
    Totalpersonas=[]

    for key,value in source.items():
        if 'normal' in value['estadoImc']:
            peso1.update({len(peso1)+1:value})    
    
        elif 'obesidad 1' in value['estadoImc']:
            peso2.update({len(peso2)+1:value})


        elif 'obesidad 2' in value['estadoImc']:
            peso3.update({len(peso3)+1:value})

        elif 'obesidad 3' in value['estadoImc']:
            peso4.update({len(peso4)+1:value})

        elif 'sobrepeso' in value['estadoImc']:
            peso5.update({len(peso5)+1:value})

      
    
    Totalpersonas.append(len(peso1))
    Totalpersonas.append(len(peso2))
    Totalpersonas.append(len(peso3))
    Totalpersonas.append(len(peso4))
    Totalpersonas.append(len(peso5))
    return Totalpersonas

