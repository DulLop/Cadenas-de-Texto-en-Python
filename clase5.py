import re

cadena = "vamos a aprender expresiones regulares con pyton"

busqueda = re.search("aprender", cadena)
print(busqueda)

#Busqueda de fechas en base a un patron
texto = "La fecha de vencimiento es 2023-12-31 y la fecha de inicio fue 2023-01-15"
patron_fecha = r"\d{4}-\d{2}-\d{2}"
fechas_encontradas = re.findall(patron_fecha, texto)
print(fechas_encontradas)

#remplazo de texto basado en patrones
texto = "El numero de telefono es 123-456-78"
patron_numero = r"\d{3}-\d{3}-\d{2}"
nuevo_texto = re.sub(patron_numero, "####", texto)
print(nuevo_texto)

#Extraccioón de url en un html
html = "<p>Enlace uno <a href="https://www.google.com.mx">Enlace 1 </a>"
patron_url = r"<a href="(.*?)">(.*?)</a>"
enlaces = re.findall(patron_url, html)
for enlace in enlaces:
    url, texto = enlace
    print(f"URL: {url}, texto : {texto}")