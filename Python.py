import random

opciones = ["piedra", "papel", "tijeras"]
Usuario =  input("Hola instructor,escoge cual opcion vas a eligir si Piedra, papel o tijeras:").lower()
Computadora = random.choice(opciones)

print (f"El computador escogio:{Computadora}")
print (f"El usuario escogio:{Usuario}")


if Usuario == Computadora:
    print("Empate")

elif (Usuario == 'piedra' and Computadora == 'tijeras') or (Usuario == 'tijeras' and Computadora == 'papel') or (Usuario == 'papel' and Computadora == 'piedra'):
    print ("Ganaste la Partida")

else:
    print ("Perdiste la Partida")

while True:
    jugar_nuevamente = input("¿Quieres jugar de nuevo? (si/no): ").lower()
    
    if jugar_nuevamente == 'si':
        opciones = ["piedra", "papel", "tijeras"]
        
        Usuario = input("Escoge de nievo cual opcion vas a eligir si piedra, papel o tijeras:").lower()
        
        Computadora = random.choice(opciones)
        
        print(f"El computador escogio:{Computadora}")
        
        print(f"El usuario escogio:{Usuario}")

        if Usuario == Computadora:
            print("Empate")

        elif (Usuario == 'piedra' and Computadora == 'tijeras') or (Usuario == 'tijeras' and Computadora == 'papel') or (Usuario == 'papel' and Computadora == 'piedra'):
            print("Ganaste la Partida")

        else:
            print("Perdiste la Partida")
            
    elif jugar_nuevamente == 'no':
        print("Gracias por jugar. ¡Hasta luego!")
        break

    else:
        print("Entrada no válida instructor. Por favor, responde con 'si' o 'no', muchas gracias.")
