import random
import string

def generar_contrasena():
    longitud = random.randint(7, 10)  # Longitud aleatoria entre 7 y 10 caracteres
    contrasena = ''.join(random.choice(string.printable[33:127]) for _ in range(longitud))
    return contrasena

def main():
    contrasena_generada = generar_contrasena()
    print(f"Contraseña generada aleatoriamente: {contrasena_generada}")

if __name__ == "__main__":
    main()