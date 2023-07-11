import os
def clear():
    if os.name=="posix":
        os.system("clear")   
    elif os.name in ["ce","nt","dos"]:
        os.system ("cls")    
        
def val_op(min,max):
    mensaje="Opcion Invalida... Intentelo nuevamente"
    try:
        op=int(input())
        if op<min or op>max:
            print(mensaje)
            return val_op(min,max)
        else:
            return op
    except:
        print(mensaje)
        return val_op(min,max)
    
def val_rut():
    mensaje="RUT invalido... verifique la informacion e intentelo nuevamente..."
    try:
        rut=int(input("RUT:     sin puntos ni guion ni digito verificador ejemplo 12345678 \n"))
    except:
        print(mensaje)
        return val_rut()
    if len(str(rut)) not in [7,8]:
        print(mensaje)
        return val_rut()
    return rut

def mostrar_depto(matriz):
    print("Piso  A   B   C   D")
    linea="     ━━━╋━━━╋━━━╋━━━"
    print(linea)
    for i in range(10):
        if i == 9:
            linea=" "
        if i==0:
            print(" ",10-i,end=" ")
        else:
            print("  ",10-i,end=" ")
        for j in range(4):
            if j==3:
                print(matriz[i][j])
            else:
                print(matriz[i][j],end="┃")
        print(linea)
        
def val_tipo():
    mensaje="Opcion Invalida... Intentelo nuevamente"
    try:
        op=input().upper()
        if op not in ["A","B","C","D"]:
            print(mensaje)
            return val_tipo()
        else:
            if op=="A":
                return 0,"A"
            elif op=="B":
                return 1,"B"
            elif op=="C":
                return 2,"C"
            elif op=="D":
                return 3,"D"
    except:
        print(mensaje)
        return val_tipo()
    
def ord_cliente(cliente,dato):
    if len(cliente)==0:
        cliente.append(dato)
        return
    for i in range(len(cliente)):
        if cliente[i][0]==dato[0]:
            cliente.insert(i+1,dato)
            return
        elif cliente[i][0]>dato[0]:
            cliente.insert(i,dato)
            return
            
        
    
        
def selec_depto(disponibilidad,info):
    cliente=[]
    print("ingrese el numero de Piso")
    fila=val_op(1,10)
    fila=10-fila
    print("Ingrese el Tipo de depto")
    columna,tipo=val_tipo()
    if disponibilidad[fila][columna]=="   ":
        print(" ")
        print(f"departamento {tipo}{10-fila}")
        print(f"Tipo {info[columna][0]}")
        print(f"Precio: {info[columna][1]} UF")
        print("\nEl lote se encuentra disponible")
        print("¿Desea Adquirirlo?\n")
        print("1.- SI \n2.- NO\n")
        selec=val_op(1,2)
        if selec==1:
            print("ingrese su Rut")
            aux=int(val_rut())
            cliente.append(aux)
            cliente.append(info[columna][0])
            cliente.append(info[columna][1])
            disponibilidad[fila][columna]=" X "
            print("\nSolicitud de Adquisicion ingresada \nnuestros Ejecutivos se pondran en contacto con ud. para finalizar la transaccion")
            return cliente
        return
    else:
        print("\n No está disponible")
        print("¿desea seleccinar otro?")
        print("1.- SI \n2.-NO\n")
        selec=val_op(1,2)
        if selec==1:
            return selec_depto(disponibilidad,info)
        return
    
def mostrar_cliente(cliente):
    for info in cliente:
        print(" ")
        print(f"Rut:         {info[0]}")
        print(f"Depto Tipo:  {info[1]}")
        print(f"Precio:      {info[2]} UF")
        
def calcular_Ganancias(cliente):
    tipoA=[0,0]
    tipoB=[0,0]
    tipoC=[0,0]
    tipoD=[0,0]
    total_final=[0,0]
    for info in cliente:
        if info[1]=="A":
            tipoA[0]+=1
            tipoA[1]+=info[2]
        elif info[1]=="B":
            tipoB[0]+=1
            tipoB[1]+=info[2]
        elif info[1]=="C":
            tipoC[0]+=1
            tipoC[1]+=info[2]
        elif info[1]=="D":
            tipoD[0]+=1
            tipoD[1]+=info[2]
        total_final[0]+=1
        total_final[1]+=info[2]
    print("Tipo de Departamento  Cantidad   Total")
    print(f"Tipo A 3.800 UF     {tipoA[0]}     {tipoA[1]}")
    print(f"Tipo B 3.000 UF     {tipoB[0]}     {tipoB[1]}")
    print(f"Tipo C 2.800 UF     {tipoC[0]}     {tipoC[1]}")
    print(f"Tipo D 3.500 UF     {tipoD[0]}     {tipoD[1]}")
    print(f"TOTAL               {total_final[0]}     {total_final[1]}") 
    
            