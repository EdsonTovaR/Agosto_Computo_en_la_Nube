#Escriba una función que tome tres números como parámetros

def val_mediana(n1,n2,n3):
    numeros=[n1,n2,n3]
    numeros.sort()

    return numeros[1]


def main():
    n1=int(input("Ingresa el primer valor: "))
    n2=int(input("Ingresa el segundo valor: "))
    n3=int(input("Ingresa el tercer valor: "))

    mediana=val_mediana(n1,n2,n3)
    print(f"La mediana de los numeros {n1}, {n2}, {n3} es {mediana}")






if __name__ == "__main__":
    main()