'''
Codigo desarrollado por Javier "JaviHax" Rivas 2019.
'''

import matplotlib.pyplot as plt #<-- libreria para hacer plots
import math #<-- libreria para hacer funciones matematicas avanzadas
import time as tm #<-- libreria para importar funciones de tiempo
from os import system #<-- libreria para traer funciones del sistema operativo

def inicio():
    print("\033[1;32;40m ")
    print("  __  __       _   _       _____ ____  ")
    print(" |  \/  |     | | | |     |_   _/ __ \ ")
    print(" | \  / | __ _| |_| |__     | || |  | |")
    print(" | |\/| |/ _` | __| '_ \    | || |  | |")
    print(" | |  | | (_| | |_| | | |_ _| || |__| |")
    print(" |_|  |_|\__,_|\__|_| |_(_)_____\____/  v2.0")
    print(" By JaviHax")
    menu()

def menu():
    b = input('''
    Seleccione el metodo a realizar.
    1- Aproximaciones sucesivas.
    2- Metodo de biseccion.
    3- Metodo de Newton-Raphson.
    4- Metodo de la secante.
    5- Salir.
    Su decision: ''')
    if b == '1':#metodo de aproximaciones sucesivas
        aproximaciones_sucesivas()
    elif b == '2':
        #metodo de biseccion
        biseccion()
    elif b == '3':
        #newton
        Newton_Raphson()
    elif b == '4':
        #secante
        secante()
    elif b == '5':#salida
        #salir
        print("gracias por usar el servicio, saliendo...")
        tm.sleep(3)
        exit()
    else:#"try/catch"
        print("Valor desconocido, regresando al inicio...")
        tm.sleep(2)
        system("clear")
        inicio()

def aproximaciones_sucesivas():
    system("clear")
    print("Bienvenido al metodo de aproximacion sucesiva.")
    print("Este metodo resolvera la funcion:")
    print("F(x) = 2 Sen(√xi)")
    
    while True:#Numero de iteraciones
        try:
            iteraciones = float(input("Ingrese el minimo error buscado: "))
            break
        except ValueError:
            print("No hay numero valido, intente de nuevo.")
    
    while True:#Valor inicial
        try:
            x = float(input("Ingrese un valor inicial a su funcion: "))
            break
        except ValueError:
            print("Valor invalido, intente nuevamente.")

    #estas seran las listas que voy a plotear
    valx = []
    valy = []

    valx.append(x)#<-- se le da el primer valor de x
    valy.append(0)#<-- se le da un valor cero inicial para poder plotear

    system("clear")
    control = True
    print("TABLA DE RESULTADOS")
    while control :#<-- pequena iteradora
        
        #X = (x**5) - (2*(x**4)) + (2*(x**3)) - (3*(x**2)) + (6*x) - 6
        X = 2 * math.sin(math.sqrt(x))#<-- equacion matematica
        valy.append(X)#<-- append para x
        error = abs(((x - X) / X) * 100)#<-- ecuacion del error porcentual
        x = X #<-- re asignacion de valores
        valx.append(x) #<-- append para x en X
        print(f"El valor de la funcion es: {round(X, 6)}")
        print(f"El porcentaje de error es: {round(error, 3)}%\n")
        
        if error > iteraciones:#<-- comprobacion del bucle
            control = True
        else:
            control = False

    #aca se llama al metodo plotter que se encarga de dibujar
    plotter(valx, valy)

    b = input("1- Volver al menu.\n2- Intentar otros valores\nSu desicion: ")
    if b == '1':
        inicio()
    elif b == '2':
        aproximaciones_sucesivas()
    else:
        print("Valor desconocido, retornando al menu.")
        menu()

def biseccion():
    system("clear")
    print('''Bienvenido al metodo de biseccion.
    este metodo trabaja solo con la funcion
        F(x) = X^4 + 3X^3 - 2''')

    valx = []#<-- lista de valores de x para la funcion
    valfx = []#<-- lista de los valores de la funcion

    check = True
    while check:#Control del ploteo
        b = input("Desea ingresar valores al plot?\n1- Si(5 valores).\n2- No(autorrellenar).\nSu respuesta: ")
        
        if b == '1':# Si desea ingresar los valores de forma manual (obligatorio 10)
            for i in range(5):
                while True:
                    try:
                        b = float(input("Ingrese valor: "))
                        break
                    except ValueError:
                        print("Valor incorrecto, intentelo nuevamente.")

                valx.append(b)
            check = False

        elif b == '2':#si desea autorrellenar los valores
            for i in range(-2, 3):
                valx.append(i)
            check = False

        else:#capturadora de errores
            print("El valor ingresado es desconocido, intentelo nuevamente.")
            tm.sleep(2)
            system("clear")         
            check = True

    for i in valx:#procedimiento matematico
        b = (i**4) + 3*(i**3) - 2
        valfx.append(b)

    plotter(valx,valfx)#grafica de la funcion valorizada

    for i in valfx:#aca busco la raiz
        if i > 0:
            val = valfx.index(i)
            xa = valx[val-1]
            xb = valx[val]
            break

    print(f"la raiz principal se encontro en el intervalo compuesto por {xa} y {xb} ambos sobre el eje X")
    b = float(input("a continuacion se procedera a iterar, por favor ingrese el error porcentual minimo aceptado: "))
    #la primera "iteracion ocurre afuera"
    print("\nPrimera iteracion.\n")
    Xr = round(((xa + xb) / 2), 2)#valor de la ecuacion de Xr
    print(f"El Valor de Xr es: {Xr}")
    fxr = (Xr**4) + 3*(Xr**3) - 2#valor de F(Xr)
    fxr = round(fxr, 2)
    fxa = (xa**4) + 3*(xa**3) - 2#valor de F(Xa)
    fxa = round(fxa, 2)
    print(f"El valor de la funcion evaluada en Xr es: {fxr}")
    prod = round(fxa * fxr, 2)
    print(f"El valor del producto de F(xa) y F(xr) es igual a: {prod}")
    xr = round(Xr, 2)
    #comprovacion de valores
    if prod > 0:
        xa = Xr
    if prod < 0:
        xb = Xr
    #aca comienzan las nuevas iteraciones.

    control = True
    while control:
        print("///////////////////////////")
        print("Iteracion.")
        print("///////////////////////////")
        Xr = round(((xa + xb) / 2), 2)#valor de la ecuacion de Xr
        Ep = abs(((xr - Xr)/ Xr) * 100)
        fxr = (Xr**4) + 3*(Xr**3) - 2#valor de F(Xr)
        fxr = round(fxr, 2)
        fxa = (xa**4) + 3*(xa**3) - 2#valor de F(Xa)
        fxa = round(fxa, 2)
        prod = round(fxa * fxr, 2)
        print(f"El Valor de Xr es: {Xr}")
        print(f"El valor de la funcion evaluada en Xr es: {fxr}")
        print(f"El valor del producto de F(xa) y F(xr) es igual a: {prod}")
        print(f"El porcentaje de error es: {Ep}%")
        xr = round(Xr, 2)
        i += 1
        #comprovacion de valores
        if prod > 0:
            xa = Xr
        if prod < 0:
            xb = Xr

        #clausula de escape
        if Ep < b:
            print("Error minimo alcanzado.")
            control = False
    
    b = input("1- Volver al menu.\n2- Intentar otros valores\nSu desicion: ")
    if b == '1':
        inicio()
    elif b == '2':
        biseccion()
    else:
        print("Valor desconocido, retornando al menu.")
        menu()

def Newton_Raphson():
    print("Bienvenido al metodo de Newton-Raphson.")
    print("Este metodo trbajara con la ecuacion F(x) = X^3 - 10X - 5 y su derivada.")
    valx = [-5,-4.5,-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,1,1.5,2,2.5,3,3.5,4,4.5,5]#lista inicializada para mejor ploteo
    valy = []#lista no inicializada por motivos de resolucion.

    for i in valx:#resolucion de la ecuacion para la creacion de la grafica
        y = (i**3) - (10*i) - (5)#ecuacion para el valor y = F(x)
        valy.append(y)
    plotter(valx, valy)

    indices = []
    for i in valy:#captacion del primer indice
        if i > 0:
            indice = valy.index(i)
            indices.append(indice)
            break
    
    for i in valy[indice:]:#captacion del segundo indice
        if i < 0:
            indice = valy.index(i)
            indices.append(indice)
            break

    for i in valy[indice:]:#ultima captacion
        if i > 0:
            indice = valy.index(i)
            indices.append(indice)
            break
    inter = indices[0]
    system("clear")
    #PRIMERA RAIZ
    print(f"La primera raiz se encontro en el intervalo [{valx[inter-1]}, {valx[inter]}], en funcion de esto,")
    X = float(input("Ingrese el valor inicial de su X: "))
    
    ite = 1
    control = True
    while control:
        xi = X - f(X) / df(X)
        X = xi
        print("///////ITERACION/////////")
        print(f"El valor de la iteracion {ite} es: {round(X, 4)}")
        print("/////////////////////////")

        ite += 1
        b = input("Desea iterar nuevamente?\n1- Si.\n2- No.\nSu respuesta: ")
        if b == '1':
            control = True
        elif b == '2':
            print("Iteraciones terminadas")
            R1 = round(X, 3)#<---- valor de la primera raiz
            control = False
        else:
            print("Valor desconocido, intentelo nuevamente.")
            control = True

    inter = indices[1]
    system("clear")
    #SEGUNDA RAIZ
    print(f"La segunda raiz se encontro en el intervalo [{valx[inter-1]}, {valx[inter]}], en funcion de esto,")
    X = float(input("Ingrese el valor inicial de su X: "))

    ite = 1
    control = True
    while control:
        xi = X - f(X) / df(X)
        X = xi
        print("///////ITERACION/////////")
        print(f"El valor de la iteracion {ite} es: {round(X, 4)}")
        print("/////////////////////////")

        ite += 1
        b = input("Desea iterar nuevamente?\n1- Si.\n2- No.\nSu respuesta: ")
        if b == '1':
            control = True
        elif b == '2':
            print("Iteraciones terminadas")
            R2 = round(X, 3)#<---- valor de la segunda raiz
            control = False
        else:
            print("Valor desconocido, intentelo nuevamente.")
            control = True

    inter = indices[2]
    system("clear")
    #TERCERA RAIZ
    print(f"La tercera raiz se encontro en el intervalo [{valx[inter-1]}, {valx[inter]}], en funcion de esto,")
    X = float(input("Ingrese el valor inicial de su X: "))

    ite = 1
    control = True
    while control:
        xi = X - f(X) / df(X)
        X = xi
        print("///////ITERACION/////////")
        print(f"El valor de la iteracion {ite} es: {round(X, 4)}")
        print("/////////////////////////")

        ite += 1
        b = input("Desea iterar nuevamente?\n1- Si.\n2- No.\nSu respuesta: ")
        if b == '1':
            control = True
        elif b == '2':
            print("Iteraciones terminadas")
            R3 = round(X, 3)#<---- valor de la segunda raiz
            control = False
        else:
            print("Valor desconocido, intentelo nuevamente.")
            control = True
    
    system("clear")
    print("Las iteraciones han terminado de forma exitosa y la busqueda de raices se ha realizado exitosamente.")
    print(f"Las Raices encontradas son las siguientes.")
    print(f'''La raiz 1 fue encontrada en el punto {R1}
    La raiz 2 fue encontrada en el punto {R2}
    La raiz 3 fue encontrada en el punto {R3}''')
    print("En 5 segundos se mostraran de forma grafica y localizada.")
    tm.sleep(5)
    plotter2(valx, valy, R1, R2, R3)

    b = input("1- Volver al menu.\n2- Intentar otros valores\nSu desicion: ")
    if b == '1':
        inicio()
    elif b == '2':
        Newton_Raphson()
    else:
        print("Valor desconocido, retornando al menu.")
        menu()

def secante():
    print("Bienvenido al metodo de Secante.")
    print("Este metodo trbajara con la ecuacion F(x) = X^3 - 10X - 5 y su secante procesada.")
    valx = [0,1,1.5,2,2.5,3,3.5,4,4.5,5]#lista inicializada para mejor ploteo
    valy = []#lista no inicializada por motivos de resolucion.

    for i in valx:#resolucion de la ecuacion para la creacion de la grafica
        y = (i**3) - (10*i) - (5)#ecuacion para el valor y = F(x)
        valy.append(y)
    plotter(valx, valy)

    indices = []

    for i in valy:#ultima captacion
        if i > 0:
            indice = valy.index(i)
            indices.append(indice)
            break
    
    inter = indices[0]
    system("clear")
    #TERCERA RAIZ
    print(f"La tercera raiz se encontro en el intervalo [{valx[inter-1]}, {valx[inter]}], en funcion de esto,")
    X = float(input("Ingrese el valor inicial de su X: "))

    ite = 1
    control = True
    while control:
        xi = X - sup(X) / inf(X)
        X = xi
        print("///////ITERACION/////////")
        print(f"El valor de la iteracion {ite} es: {round(X, 4)}")
        print("/////////////////////////")

        ite += 1
        b = input("Desea iterar nuevamente?\n1- Si.\n2- No.\nSu respuesta: ")
        if b == '1':
            control = True
        elif b == '2':
            print("Iteraciones terminadas")
            R1 = round(X, 3)#<---- valor de la segunda raiz
            control = False
        else:
            print("Valor desconocido, intentelo nuevamente.")
            control = True
    
    system("clear")
    print("Las iteraciones han terminado de forma exitosa y la busqueda de raices se ha realizado exitosamente.")
    print(f"Las Raices encontradas son las siguientes.")
    print(f"La raiz 1 fue encontrada en el punto {R1}")
    print("En 5 segundos se mostraran de forma grafica y localizada.")
    tm.sleep(5)
    plotter1(valx, valy, R1)

    b = input("1- Volver al menu.\n2- Intentar otros valores\nSu desicion: ")
    if b == '1':
        inicio()
    elif b == '2':
        secante()
    else:
        print("Valor desconocido, retornando al menu.")
        menu()


def f(x):#funcion f N-R
    return((x**3)-(10*x)-(5))

def df(x):#derivada df(x) N-R
    return((3*(x**2)) - 10)

def sup(x):#funcion superior Sec
    return((x**3)-(10*x)-(5)) * ((x-1) - x)

def inf(x):#funcion inferior Sec
    return (((x-1)**3)-(10*(x-1))-(5)) - ((x**3)-(10*x)-(5))

def plotter(x, y):
    plt.plot(x, y, color = 'red')
    plt.plot([0,0],[-100,100], color = 'black')
    plt.plot([-100,100],[0,0], color = 'black')
    plt.title("PLOTEO DE F(x)")
    plt.ylabel("Eje Y")
    plt.xlabel("Eje X")
    plt.ylim(-10,10)
    plt.xlim(-10,10)
    plt.grid(linestyle = '-', linewidth = 0.5)
    plt.show()

def plotter1(x, y,R1):#plot de Newton Raphson
    plt.plot(x, y, color = 'red')
    plt.annotate(f'P({R1}, 0)', xy = (R1, 0),xytext = (-7, 5), arrowprops = dict(facecolor = 'black', shrink = 0.05))
    plt.plot([0,0],[-100,100], color = 'black')#eje y
    plt.plot([-100,100],[0,0], color = 'black')#eje X
    plt.title("PLOTEO DE F(x)")
    plt.ylabel("Eje Y")
    plt.xlabel("Eje X")
    plt.ylim(-10,10)
    plt.xlim(-10,10)
    plt.grid(linestyle = '-', linewidth = 0.5)
    plt.show()

def plotter2(x, y,R1,R2,R3):#plot de Newton Raphson
    plt.plot(x, y, color = 'red')
    plt.annotate(f'P({R1}, 0)', xy = (R1, 0),xytext = (-7, 5), arrowprops = dict(facecolor = 'black', shrink = 0.05))
    plt.annotate(f'P({R2}, 0)', xy = (R2, 0),xytext = (-0.5, 7), arrowprops = dict(facecolor = 'black', shrink = 0.05))
    plt.annotate(f'P({R3}, 0)', xy = (R3, 0),xytext = (7.5, 7.5), arrowprops = dict(facecolor = 'black', shrink = 0.05))
    plt.plot([0,0],[-100,100], color = 'black')#eje y
    plt.plot([-100,100],[0,0], color = 'black')#eje X
    plt.title("PLOTEO DE F(x)")
    plt.ylabel("Eje Y")
    plt.xlabel("Eje X")
    plt.ylim(-10,10)
    plt.xlim(-10,10)
    plt.grid(linestyle = '-', linewidth = 0.5)
    plt.show()

inicio()