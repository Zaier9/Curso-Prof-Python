#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, os

#Para limpiar la pantalla, detecta el sistema operativo y usa el comando adecuado.
def cls():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

#Devuelve una matriz de dimensiones i * j rellena de s
def matriz(i,j,s):
    mat = []
    for a in range(i):
        mat.append([])
        for b in range(j):
            mat[a].append(s)
    return(m)

#Cuenta la cantidad de veces que se repite b en la matriz mat
def cont(m,b):
    c = 0
    for a in range(len(m)):
        c = c + m[a].count(b)
    return(c)

#Funcion Principal
def minSweep(i,j,mines):
    camp = matriz(i,j,0)
    a = 0
    #Este while rellena la matriz de minas "*"
    while cont(camp,"*") < mines:
        camp[random.randint(0,i-1)][random.randint(0,j-1)] = "*"
        a += 1
        #Este if sirve para que si se pusieron mas minas que cuadrados disponibles, te lo diga y se reinicie el codigo.
        if mines > (i*j):
            print('Has puesto mas minas que cuadrados electricos')
            raw_input()
            cls()
            minSweep(input('Columnas?: '), input('Filas?: '), input('Minas?: '))
    
    #Esta serie de for pone en cada posicion de la matriz que no sea una mina el numero de minas que hay alrededor.
    for x in range(i):
        for y in range(j):
            if camp[x][y] != "*":
                count = 0
                for a in [1,0,-1]:
                    for b in [1,0,-1]:
                        try:
                            if camp[x + a][y + b] == "*":
                                if (x + a > -1 and y + b > -1):
                                    count += 1
                        except:
                            pass
                camp[x][y] = count
    
    #Se crea la matriz que se le enseña al usuario
    campShow = matriz(i,j,"#")
    #A partir de este while, es la "interfaz", aquello que el usuario puede ver
    while True:
        try:
            #Enseña que la matriz resuelta. es algo que se tuvo que hacer para que estuviera en el mismo formato que la matriz campShow, dado que la fn printmin ademas de imprimir la matriz que se le manda, tambien la modifica.
            printmin(camp,i,j)
            minasdesc = cont(campShow, "* ")
            cls() #Borramos la pantalla
            printmin(campShow,i,j)
            #Si las minas restantes por descubrir y las descubiertas son iguales y ademas, no queda ningun "# " en campShow, se termina el juego.
            