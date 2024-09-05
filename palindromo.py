#Palindromo



def palindromo (texto):
    texto_der = texto.replace(" ", "")
    texto_izq = texto[::-1].replace(" ","")

    if(texto_der == texto_izq):
        print("Es palindromo")
    else:
        print("No es palindromo")

if __name__ == "__main__":

    texto = input("Ingresa una frase:")
    palindromo(texto)