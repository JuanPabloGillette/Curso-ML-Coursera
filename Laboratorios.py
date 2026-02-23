#Labo 1

import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1.0, 2.0])   #features
y_train = np.array([300.0, 500.0])   #target value

def funcion_lineal(x_modelo, pendiente_m , odo_b):
    lenX = len(x_modelo)
    print(lenX)
    y_predict = np.zeros(lenX)
    for i in range (lenX):
      y_predict[i] = pendiente_m *x_modelo[i]+ odo_b
    return y_predict

def funcion_lineal1(x_modelo,pendiente_m,odo_b):
  return pendiente_m *x_modelo+ odo_b

y_prediccion = funcion_lineal(x_train,200,100)
#Grafico:

plt.scatter(x_train, y_train, marker = "x", c="b")
plt.plot(x_train, y_prediccion, c = "r", label = "funcion lineal con b y w arbitrarios")
plt.title("Ejemplo de juampi")
plt.ylabel("titulo de las y")
plt.xlabel("titulo de las x")
plt.show()
