import funciones_SebastianSeguel_FPY1101_011V as fn
libros = []
librosPrestados = []
while True:
    print ("--------MENU PRINCIPAL--------")
    print ("1. Registrar Libro")
    print ("2. Prestar Libro")
    print ("3. listar todos los libros")
    print ("4. imprimir reporte de prestamos")
    print ("5. Salir salir del programa")

    try:
        op = int(input("Elija una opción: "))
        if op == 1:
            fn.RegistrarLibro(libros)
        elif op == 2:
            fn.PrestarLibro(libros, librosPrestados)
        elif op == 3:
            fn.listarLibros(libros)
        elif op == 4:
            fn.imprimirReporte(librosPrestados)
        elif op == 5:
            print ("programa finalizado...")
            print ("desarrollado por: Sebastian Seguel")
            print ("Rut: 20.056.356-5 ")
            break
        else :
            print ("Opción no válida. Intente nuevamente.")
    except ValueError:
        print ("Solo se admiten números ")

    
