import math

def calcular_hipotenusa(a, b):
    hipotenusa = math.sqrt(a**2 + b**2)
    return hipotenusa

def main():
        
        lado1 = float(input("Ingrese la longitud del primer lado: "))
        lado2 = float(input("Ingrese la longitud del segundo lado: "))
        
        hipotenusa = calcular_hipotenusa(lado1, lado2)
        print(f"La longitud de la hipotenusa es: {hipotenusa}")
    

if __name__ == "__main__":
    main()