
# Simulacion del microscopio de efecto tunel
# Muestra el flujo de electrones transferidos, de acuerdo al
# punto en el espacio que se encuentra la punta del microscopio

# David Mena y Jose Ocampo

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

t = np.linspace(-5, 5, num=40, endpoint = False)

x_right_lim = 10
x_left_lim = -10
y_top_lim = 5
y_bottom_lim = -5

# Solo es necesario anadir la funcion aqui, lo demas se hace automatico:

hbar = 1.0518 * np.float_power(10, -34) # J*s
me = 9.109 * np.float_power(10, -31) # kg
W = 3.4 * 1.60218*np.float_power(10,-19) # eV to J
e = 1.60218 * np.float_power(10, -19) # Coloumb
V = 2*np.float_power(10, -3)   # milivolts # voltaje anadido para asegurar que el flujo de electrones sea desde la muestra hacia la punta

def funcDensidadCorriente(L): # en funcion de la distancia variable entre la punta
                            # del microscopio y el punto que examina en la muestra
    validar = False
    while not validar:
        d= hbar/np.sqrt(2*me*(W)) # pentration depth
        relacionLD = L/d
        test = np.float_power(e, (2*L/d))
        funcion = ( (np.float_power(e,2) * V ) / (4 * np.float_power(np.pi, 2) * L * d * hbar) )* np.float_power(e, (2*L/d)) # eq d. corriente
        if funcion != 0.0:
            validar = True
        print("funcion", funcion)
        print("test", test)
        print("d:", d)
        print("Relacion:", relacionLD)
    return funcion

def funcPlataforma(x):
    validar = False
    while not validar:
        funcion = 0.5*np.float_power(10, -12) * np.cos(x) + 0.5*np.float_power(10,-12) # aqui
        if funcion != 0:
            validar = True
    return funcion

def funcPlataforma2(x):
    validar = False
    while not validar:
        funcion = np.cos(x) +3
        if funcion != 0:
            validar = True
    return funcion


def arrayOfFuncPlataforma(arr):
    funcArr = np.array([])
    for x in np.nditer(arr):
        calc = funcPlataforma(x)
        print(calc)
        funcArr = np.append(funcArr, calc)
    print( funcArr )
    return funcArr

def arrayOfFuncPlataforma2(arr):
    funcArr = np.array([])
    for x in np.nditer(arr):
        calc = funcPlataforma2(x)
        print(calc)
        funcArr = np.append(funcArr, calc)
    print( funcArr )
    return funcArr

y_top_lim = 2.9 * np.float_power(10,-11)
y_bottom_lim = 0 * np.float_power(10,-11)

y2_top_lim = 7
y2_bottom_lim = 0
x2_left_lim = -5
x2_right_lim = 5


def animate(ts):
    print(funcPlataforma(ts))
    init=(funcPlataforma(ts) - y_bottom_lim) + y_bottom_lim
    print("init", init)
    L = y_top_lim - (funcPlataforma(ts) - y_bottom_lim) # distancia entre punta y superficie de atomos
    print("L Distancia:", L)
    print("func(l)", funcDensidadCorriente( L ))
    numPuntos = funcDensidadCorriente( L ) /50
    print("numPuntos:", numPuntos)

    flujo = np.arange(init, y_top_lim, np.abs( numPuntos ) / 100 )  # start, stop, step
    print("FLUJO", flujo)

    print("y_top_lim", y_top_lim)
    print("y_bottom_lim", y_bottom_lim)
    print(flujo)
    print(flujo.size)
    x = np.ones(flujo.size)
    print (x)
    x.fill(ts)
    print (x)

    ejeX = np.linspace(x_left_lim, x_right_lim, num=100, endpoint = False)
    cosEjeX = arrayOfFuncPlataforma(ejeX)

    ejeX2 = np.linspace(x2_left_lim, x2_right_lim, num=100, endpoint=False)
    init2 = (funcPlataforma2(ts) - y2_bottom_lim) + y2_bottom_lim
    print("ts2:", ts)
    print("init2:", init2)
    print("funcPlataforma2(ts)", funcPlataforma2(ts))
    print("y2_bottom_lim", y2_bottom_lim)
    flujo2 = np.arange(init2, y2_top_lim, np.abs( numPuntos )/10)  # start, stop, step
    print("flujo2")
    for x in flujo2:
        print (x)
    print("numpuntos2", np.abs( numPuntos ))
    print("y2_top_lim", y2_top_lim)
    cos2EjeX = arrayOfFuncPlataforma2(ejeX)
    x2 = np.ones(flujo2.size)
    x2.fill(ts)

    plt.cla()
    plt.xlim(x2_left_lim, x2_right_lim)
    plt.ylim(y2_bottom_lim, y2_top_lim) # cambiar los ejes de acuerdo a la funcion que se ingresa
    plt.autoscale(False)

    plt.plot(x2, flujo2, ".b", ejeX2, cos2EjeX,'g')
    plt.legend(['ts=%4.2f' % ts])

anim = animation.FuncAnimation(plt.gcf(), animate, frames=t, interval = 750) # interaval da la velocidad de la animacion
plt.show()