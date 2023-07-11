import Examen_Funciones as ef
cliente=[]
depto=[["   ","   ","   ","   "],
       ["   ","   ","   ","   "],
       ["   ","   ","   ","   "],
       ["   ","   ","   ","   "],
       ["   ","   ","   ","   "],
       ["   ","   ","   ","   "],
       ["   ","   ","   ","   "],
       ["   ","   ","   ","   "],
       ["   ","   ","   ","   "],
       ["   ","   ","   ","   "]]
infodepto=[["A",3800],["B",3000],["C",2800],["D",3500]]

while True:
       ef.clear()
       print("Bienvenido a Casa Feliz\n")
       print(" 1. Comprar departamento\n 2. Mostrar departamentos disponibles\n 3. Ver listado de compradores\n 4. Mostrar ganancias totales\n 5. Salir\n")
       print("Seleccione un opcion: \n")
       opcion=ef.val_op(1,5)
       if opcion==1:
              ef.mostrar_depto(depto)
              print("¿Desea Seleccionar un Lote?")
              print("1.- SI\n2.- NO")
              opcion=ef.val_op(1,2)
              if opcion==1:
                     aux=ef.selec_depto(depto,infodepto)
                     ef.ord_cliente(cliente,aux)
                     pause=input("\nprecione cualquier tecla para continuar")
                     ef.clear()
       elif opcion==2:
              ef.mostrar_depto(depto)
              pause=input("\nprecione cualquier tecla para continuar")
              ef.clear()
       elif opcion==3:
              ef.mostrar_cliente(cliente)
              pause=input("\nprecione cualquier tecla para continuar")
              ef.clear()
       elif opcion==4:
              ef.calcular_Ganancias(cliente)
              pause=input("\nprecione cualquier tecla para continuar")
              ef.clear()
       elif opcion==5:
              print("10 Julio 2023")
              print("Bastian Aguirre Muñoz")
              break
