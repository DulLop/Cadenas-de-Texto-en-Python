name = "Dulce"
age = 30
print(f"Mi nombre es {name} y tengo {age} años")
print("Mi nombre es {} y tengo {} años".format(name,age+10))

sql_insert = "Insert into users(name,age) values ({},{})".format(name,age)
print(sql_insert)

print("nombre: {1}, Edad : {0}".format(age,name))

#Print con parámetros
producto = "Celular iphone 12"
precio = 599

print("Producto: {prod}, Precio: {prec}".format(prod = producto, prec = precio))

#Formatear números
num = 12345.6789
print("{:.2f}".format(num))
print("{:,}".format(num))
print("{:e}".format(num)) 

#Formatear fechas
from datetime import datetime
now = datetime.now()
print("Fecha y hora: {:%d/%m/%Y %H/%M/%S}".format(now))

#alineación y relleno
number = 42
print("Número : {:>10}".format(number))
print("Número : {:0<5}".format(number))
