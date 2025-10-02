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
