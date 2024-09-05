"""cadena = "Python es genial"
caracter = cadena [2:10]
print(caracter)
caracter2 = cadena[0:10:2]
print(caracter2)
reversa = cadena[::-1]
print(reversa)"""

lenguajes_de_programacion = "pyhon go c# php java javascript"
lista_lenguajes = lenguajes_de_programacion.split(" ")
print(lista_lenguajes)

print(lista_lenguajes[2:4])

email = "usuario@ed.team"
dominio = email[email.index("@") + 1:]
print(dominio)