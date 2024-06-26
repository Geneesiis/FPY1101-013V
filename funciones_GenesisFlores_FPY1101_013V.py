libros = []

def registrar():
    titulo = input("Ingrese el nombre del libro: ")
    autor = input("Ingrese el autor dl libro: ")
    publicacion = input("Ingrese año de publicación del libro: ")
    sku = input("Ingrese el SKU del libro")
    
    if titulo and autor and publicacion and sku:
        r_libros = {
            'Titulo': titulo,
            'Autor': autor,
            'Año de publicación': publicacion,
            'SKU': sku
        }
        libros.append(r_libros)
        print("Datos ingresados correctos")
    else: 
        print("Intenta nuevamente")

def prestar():
    usuario = input("Ingrese nombre del usuario: ")
    sku = input("Ingrese SKU del libro: ")
    if usuario and sku:
        p_libros = {
            'Nombre usuario': usuario,
            'SKU': sku
        }
        libros.append(p_libros)
        print("Libro disponible")
    else: 
        print("Libro no encontrado")

def listar():
    print("Lista de todos los libros ")
    with open('lista_libros.txt','w') as lista:
        lista.write("Título   Autor    Año de publicación      SKU")
        lista.write(f"TÍTULO\tAUTOR\tAÑO DE PUBLICACIÓN\tSKU\n{titulo}\t{autor}\t{publiucacion}\t{sku}")
    with open('lis_libros.txt', 'r') as lista:
        contenido = lista.read()
        print(contenido)

def imprimir():
    print("Imprimir reporte de prestamos")
    with open('im_libros.txt','w') as imprimir:
        imprimir.write("USUARIO     TÍTULO     FECHA DEL PRESTAMO")
        imprimir.write(f"USUARIO\tTÍTULO\tFECHA DEL PRESTAMO\n{usuario}\t{titulo}\t{publicacion}")
    with open('im_libros.txt', 'r') as imprimir:
        contenido = imprimir.read()
        print(contenido)

def salir():
    print("Programa finalizado...\nDesarrollado por Genesis Flores\nRUN: 21.563.657-7")

def menu():
    while True:
        try:
            print("M E N Ú")
            opcion = int(input("1. Registrar libro\n2. Prestar libro\n3. Lista de todos los libros\n4. Imprimir reporte de préstamos\n5. Salir del programa\nOp: "))
            if opcion >= 1 and opcion <= 5:
                if opcion == 1:
                    registrar()
                if opcion == 2:
                    prestar()
                if opcion == 3:
                    listar()
                if opcion == 4:
                    imprimir()
                if opcion == 5:
                    salir()
                    break 
                else:
                    print("Opción incorrecta")

        except ValueError:
            print("Error. Intente de nuevo.")