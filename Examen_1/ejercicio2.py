from ejercicio1 import es_primo

def nextPrime(n):
    if n<=1:
        n=2
    else:
        n+=1

    while True:
        if es_primo(n):
            return n
        n+=1

def main():
    numero=int(input("Ingresa un numero: "))

    if numero< 0:
        print("Ingresa un numero pósitivo")
    else:
        siguente_numero=nextPrime(numero)
        print(f"El primer numero primero mayor que {numero} es {siguente_numero}")

if __name__  == "__main__":
    main()