from tabulate import tabulate

datos=[["Intentos", "Usuario"]]
for i in range(3):
    datos.append([input("Nombre: "), input("Edad: ")])

print(tabulate(datos))

import turtle

turtle.color('green')

turtle.shape('turtle')

for x in range(1,12):
        turtle.forward(10)
        turtle.circle(100)
        turtle.right(60)
        turtle.left(30)
       