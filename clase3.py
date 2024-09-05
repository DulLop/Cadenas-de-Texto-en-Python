texto = """Python es un lenguaje de alto nivel de programación
interpretado cuya filosofía hace hincapié en la legibilidad
de su código. Se trata de un lenguaje de programación
multiparadigma, ya que soporta parcialmente la orientación
a objetos, programación imperativa y, en menor medida,
programación funcional."""

texto = texto.replace("Python", "python", 1)
palabra_busqueda = input("Ingrese palabra a buscar:")
index = texto.find(palabra_busqueda)

if (index != -1):
    print(f"{palabra_busqueda}, se encontó en el indice {index}")

    total_encontrados = texto.count(palabra_busqueda)
    print(f"{palabra_busqueda} aparece {total_encontrados} veces")

else:
    print("No se encontró la palabra")