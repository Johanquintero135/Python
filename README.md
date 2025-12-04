Juegos en Python: Piedra, Papel o Tijeras & Ahorcado

Este repositorio contiene dos juegos clásicos desarrollados en Python:

Piedra, Papel o Tijeras

Ahorcado

Ambos están hechos para practicar lógica, condiciones, ciclos, manejo de cadenas y la interacción con el usuario.

 Estructura del proyecto
 juegos_python
│── piedra_papel_tijeras.py
│── ahorcado.py
│── README.md

 Juego: Piedra, Papel o Tijeras

Este programa permite jugar Piedra, Papel o Tijeras contra la computadora, con opción para repetir la partida todas las veces que quieras.

 ¿Cómo jugar?

Ejecuta el archivo:

python piedra_papel_tijeras.py


El usuario elige entre:

piedra

papel

tijeras

La computadora selecciona una opción aleatoria.

El programa evalúa quién gana.

Al final, pregunta si deseas jugar de nuevo.

 Código
import random

opciones = ["piedra", "papel", "tijeras"]
Usuario = input("Hola instructor, escoge cual opción vas a elegir si piedra, papel o tijeras: ").lower()
Computadora = random.choice(opciones)

print(f"El computador escogió: {Computadora}")
print(f"El usuario escogió: {Usuario}")

if Usuario == Computadora:
    print("Empate")

elif (Usuario == 'piedra' and Computadora == 'tijeras') or \
     (Usuario == 'tijeras' and Computadora == 'papel') or \
     (Usuario == 'papel' and Computadora == 'piedra'):
    print("Ganaste la partida")

else:
    print("Perdiste la partida")

while True:
    jugar_nuevamente = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    
    if jugar_nuevamente == 'si':
        opciones = ["piedra", "papel", "tijeras"]

        Usuario = input("Escoge de nuevo cuál opción vas a elegir (piedra/papel/tijeras): ").lower()
        Computadora = random.choice(opciones)

        print(f"El computador escogió: {Computadora}")
        print(f"El usuario escogió: {Usuario}")

        if Usuario == Computadora:
            print("Empate")

        elif (Usuario == 'piedra' and Computadora == 'tijeras') or \
             (Usuario == 'tijeras' and Computadora == 'papel') or \
             (Usuario == 'papel' and Computadora == 'piedra'):
            print("Ganaste la partida")

        else:
            print("Perdiste la partida")

    elif jugar_nuevamente == 'no':
        print("Gracias por jugar. ¡Hasta luego!")
        break

    else:
        print("Entrada no válida. Por favor, responde con 'si' o 'no'.")

 Juego: Ahorcado

El clásico Ahorcado, donde debes adivinar una palabra letra por letra antes de que se te acaben los intentos.

 ¿Cómo jugar?

Ejecuta el archivo:

python ahorcado.py


El programa elige una palabra al azar.

Debes adivinar escribiendo una letra por turno.

Cada error resta un intento.

Ganas si completas la palabra antes de quedarte sin intentos.

 Código
import random

# Lista de palabras
palabras = ["python", "codigo", "ahorcado", "programa"]
palabra = random.choice(palabras)
palabra_oculta = ["_" for _ in palabra]
intentos = 6
letras_usadas = []

while intentos > 0 and "_" in palabra_oculta:
    print("\nPalabra: ", " ".join(palabra_oculta))
    print("Intentos restantes:", intentos)
    print("Letras usadas:", ", ".join(letras_usadas))

    letra = input("Adivina una letra: ").lower()

    if letra in letras_usadas:
        print("Ya usaste esa letra.")
        continue

    letras_usadas.append(letra)

    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_oculta[i] = letra
        print("¡Bien! La letra está en la palabra.")
    else:
        intentos -= 1
        print("Incorrecto. Pierdes un intento.")

if "_" not in palabra_oculta:
    print("\n¡Felicidades! Adivinaste la palabra:", palabra)
else:
    print("\nHas perdido. La palabra era:", palabra)

 Conceptos aprendidos

Uso de condiciones (if, elif, else)

Uso de bucles (while)

Listas y manejo de strings

Funciones del módulo random

Interacción con el usuario mediante input()

Control básico de errores y validaciones
