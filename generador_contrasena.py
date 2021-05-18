import random

def generar_contrasena():
    may = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minu = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    sim = ['!', '@', '#', '$', '%', '&', '/']
    num = ['1', '2', '3', '4', '5', '6', '7']

    caracteres = may + minu + sim + num
    password = []

    for i in range(15):
        caracteres_random = random.choice(caracteres) # choice : elige un caracter al azar y guarda el caracter en la lista
        password.append(caracteres_random)
    password = "".join(password) # "".join(nombre_lista): convertimos la lista en un string
    return password

def main():
    password = generar_contrasena()
    print("Tu nueva contraseña es: " + password )

if __name__ == '__main__':
    main()


