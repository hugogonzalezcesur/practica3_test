lista_numero_letras=[]

palabra = input("Introduzca una palabra ")
intentos = int(input("Introduzca número intentos permitidos: "))

while True:
    numero_letras = int(input("Adivine el número de letras: "))
    print("El dato introducido no es correcto")

    longitud_palabra = len(palabra)
    lista_numero_letras.append(numero_letras)

    if numero_letras > longitud_palabra:
        intentos = intentos - 1
        print("Intento erróneo. El número de letras es menor.", intentos, "intentos disponibles.")

    elif numero_letras < longitud_palabra:
        intentos = intentos - 1
        print("Intento erróneo. El número de letras es mayor", intentos, "intentos disponibles.")

    else:
        numero_letras == longitud_palabra
        print("Has acertado el número! La palabra tiene" ,numero_letras, "letras la lista del numero de letras ha sido " ,lista_numero_letras[:])
        break

    if intentos == 0:
        print("Ha superado el limite de intentos de letras, las letras introducidas han sido: ",lista_numero_letras[:])
        break

lista_letras_adivinadas = []
print('_' * len(palabra))

while True:
    while True:
        letra_adivinar = input("Adivina una letra: ")

        if (len(letra_adivinar) != 1 and letra_adivinar.isnumeric()):
            print("Eso no es una letra intenta con una sola letra")
        else:
            if letra_adivinar.lower() in lista_letras_adivinadas:
                print("Ya habias intentado con esa letra intenta con otra por favor")
            else:
                lista_letras_adivinadas.append(letra_adivinar)

                if letra_adivinar.lower() in palabra:
                    print("Felicidades adivinaste una letra")
                    break
                else:
                    intentos = intentos - 1
                    print("La letra introducida no se encuentra te quedan" ,intentos, "intentos")
                    break

    if intentos == 0:
        print("Has perdido la palabra era: " + palabra, "Los intentos de letra han sido " ,lista_letras_adivinadas[:])
        break

    estatus_letra = ""

    letras_que_faltan = 0
    for letra in palabra:

        if letra in lista_letras_adivinadas:
            estatus_letra = estatus_letra + letra

        else:
            estatus_letra = estatus_letra + "_"
            letras_que_faltan = letras_que_faltan + 1
    print(estatus_letra)

    if letras_que_faltan == 0:
        print("Felicidades has adivinado todas las letras")
        print("La palabra es: " + palabra)
        break
