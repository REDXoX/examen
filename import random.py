import random
def listaAleatorios(n):
      listasueldos = [0]  * n
      for i in range(n):
          listasueldos[i] = random.randint(300000, 2500000)
      return listasueldos
n=10
aleatorios=listaAleatorios(n)
trabajadores = ["Juan Pérez","María García","Carlos López","na Martínez","Pedro Rodríguez",
                "Laura Hernández","MiguelSánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
def sueldosmenores():
        print("""Sueldos menores a $800.000
Nombre empleado       Sueldo""")
        if aleatorios[0] < 800000:
            print(trabajadores[0],"          $",aleatorios[0])
        if aleatorios[1] < 800000:
            print(trabajadores[1],"        $",aleatorios[1])
        if aleatorios[2] < 800000:
            print(trabajadores[2],"        $",aleatorios[2])
        if aleatorios[3] < 800000:
            print(trabajadores[3],"         $",aleatorios[3])
        if aleatorios[4] < 800000:
            print(trabajadores[4],"     $",aleatorios[4])
        if aleatorios[5] < 800000:
            print(trabajadores[5],"     $",aleatorios[5])
        if aleatorios[6] < 800000:
            print(trabajadores[6],"       $",aleatorios[6])
        if aleatorios[7] < 800000:
            print(trabajadores[7],"        $",aleatorios[7])
        if aleatorios[8] < 800000:
            print(trabajadores[8],"      $",aleatorios[8])
        if aleatorios[9] < 800000:
            print(trabajadores[9],"     $",aleatorios[9])
        print("""Sueldos entre $800.000 y $2.000.000
Nombre empleado       Sueldo""")
        if aleatorios[0] > 800000 and aleatorios[0] < 2000000:
            print(trabajadores[0],"          $",aleatorios[0])
        if aleatorios[1] > 800000 and aleatorios[1] < 2000000:
            print(trabajadores[1],"        $",aleatorios[1])
        if aleatorios[2] > 800000 and aleatorios[2] < 2000000:
            print(trabajadores[2],"        $",aleatorios[2])
        if aleatorios[3] > 800000 and aleatorios[3] < 2000000:
            print(trabajadores[3],"         $",aleatorios[3])
        if aleatorios[4] > 800000 and aleatorios[4] < 2000000:
            print(trabajadores[4],"     $",aleatorios[4])
        if aleatorios[5] > 800000 and aleatorios[5] < 2000000:
            print(trabajadores[5],"     $",aleatorios[5])
        if aleatorios[6] > 800000 and aleatorios[6] < 2000000:
            print(trabajadores[6],"       $",aleatorios[6])
        if aleatorios[7] > 800000 and aleatorios[7] < 2000000:
            print(trabajadores[7],"        $",aleatorios[7])
        if aleatorios[8] > 800000 and aleatorios[8] < 2000000:
            print(trabajadores[8],"      $",aleatorios[8])
        if aleatorios[9] > 800000 and aleatorios[9] < 2000000:
            print(trabajadores[9],"     $",aleatorios[9])
        print("""Sueldos superiores a $2.000.000
Nombre empleado       Sueldo""")
        if aleatorios[0] > 2000000:
            print(trabajadores[0],"          $",aleatorios[0])
        if aleatorios[1] > 2000000:
            print(trabajadores[1],"        $",aleatorios[1])
        if aleatorios[2] > 2000000:
            print(trabajadores[2],"        $",aleatorios[2])
        if aleatorios[3] > 2000000:
            print(trabajadores[3],"         $",aleatorios[3])
        if aleatorios[4] > 2000000:
            print(trabajadores[4],"     $",aleatorios[4])
        if aleatorios[5] > 2000000:
            print(trabajadores[5],"     $",aleatorios[5])
        if aleatorios[6] > 2000000:
            print(trabajadores[6],"       $",aleatorios[6])
        if aleatorios[7] > 2000000:
            print(trabajadores[7],"        $",aleatorios[7])
        if aleatorios[8] > 2000000:
            print(trabajadores[8],"      $",aleatorios[8])
        if aleatorios[9] > 2000000:
            print(trabajadores[9],"     $",aleatorios[9])
salir = 0
while salir != 1:
    print("""opciones del menu:
    1. Asignar sueldos aleatorios
    2. Clasificar sueldos
    3. Ver estadísticas.
    4. Reporte de sueldos
    5. Salir del programa""")
    opcion=input("seleccione una opcion del menu:")
    if opcion == "1":
        aleatorios.sort()
    elif opcion == "2":
        sueldosmenores()
    elif opcion == "3":
        print("sueldo mas bajo:",trabajadores[0],aleatorios[0])
        print("sueldo mas alto:",trabajadores[9],aleatorios[9])
    elif opcion == "4":
        print
    elif opcion == "5":
        salir = salir + 1
    else:
        print("!opcion invalida vuelva a seleccionar¡")

print("""Finalizando programa…
Desarrollado por Luis Paredes
RUT 21.941.384-K""")