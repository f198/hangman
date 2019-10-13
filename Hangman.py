import random

def colgado(malas,usadas,adivinanza):
    dibujo = []
    dibujo.append('_____')
    dibujo.append("|    |")
    dibujo.append("|    O")
    dibujo.append("|   /|\\")
    dibujo.append("|   / \\")
    dibujo.append("|   FIRE ")
    for x in range(0,malas):
        print(dibujo[x])
    print('Has usado estas letras :',usadas)
    print('Resolver: ',adivinanza)


palabra = []

def definir_linea():
    with open('/Users/francisco198/Desktop/Python/Script.txt','r') as file:
        texto = file.read()
        lineas = texto.split()
        lnumber = random.randint(0,len(lineas))
        palabra3 = lineas[lnumber]
        palabra3 = palabra3.lower()
        return palabra3

while len(palabra) <=3:
    palabra = definir_linea()




largo = len(palabra)
adivinanza = []
palabra2 = []
usadas = []

for i in range(0,largo):
    adivinanza.append("_")
    palabra2.append(palabra[i])


Oportunidades = 6

print('Tienes que adivinar esto: ', adivinanza)

while Oportunidades > 0:
    if '_' in adivinanza:
        letra = input('Jugador 2 adivina una letra: ')

        if letra in palabra2:
            print('Acertaste')
            j = palabra2.index(letra)
            palabra2[j] = '_'
            adivinanza[j] = letra

            print('Palabra es: ',adivinanza)
        else:
            Oportunidades -= 1
            usadas.append(letra)
            colgado(6-Oportunidades,usadas,adivinanza)
    else:
        print('Ganaste la palabra era: ',palabra)
        break


if Oportunidades ==0:
    print('Perdiste, la palabra era: ',palabra)
