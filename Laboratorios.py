#Labo 1

import numpy as np
import matplotlib as plt

x_train1 = np.array([1,2,3,4])
y_train1 = np.array([2,4,16,32])

def funcion_lineal(x_modelo, pendiente_m , odo_b):
    lenX = len(x_modelo)
    print(lenX)
    y_predict = np.zeros(lenX)
    for i in range (lenX):
      y_predict[i] = pendiente_m *x_modelo[i]+ odo_b
    return y_predict

def funcion_lineal1(x_modelo,pendiente_m,odo_b):
  return pendiente_m *x_modelo+ odo_b

y_prediccion = funcion_lineal(x_train1,200,100)
print (y_prediccion)
#Grafico:

plt.scatter(x_train1, y_train1, marker = "x", c="b")
plt.plot(x_train1, y_prediccion, c = "r", label = "funcion lineal con b y w arbitrarios")
plt.title("Ejemplo de juampi")
plt.ylabel("titulo de las y")
plt.xlabel("titulo de las x")
plt.show()
